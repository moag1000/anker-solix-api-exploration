"""Model fields from `fromJson` factories in Blutter asm.

Usage:
  python3 -I tools/model_fields.py <asm_root> --version 3.24.3 \
      [--old-root <3.18.0 asm root>] [--out data/models.json] [--include-noise]

Each `Class.fromJson` is walked in order.  A JSON key is a non-empty string
literal that is followed within a few instructions by an indirect call (the
`map[key]` lookup).  The same key loaded twice in a row (null check, then
re-read) counts once.  Dart types come from the cast `r8 = <Type>`, nested
`X.fromJson()` calls and `_GrowableList` defaults; `unknown` when none is seen.

Output rows carry `key` = `package::Class` (package = first directory of the Dart
file; where two classes still share that key, the package part is extended to the
shortest unique directory path, then to the file path without `.dart`), plus the
short `class` name.  By default the `sentry` package (error-reporting SDK, not app
data) is dropped; `--include-noise` keeps it.  Classes without fields stay: an empty
`fromJson` may be an extractor limit, and consumers need to see the class exists.
Keys are computed before the filter, so a key does not depend on the flag.
"""
import argparse
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import asmparse as A  # noqa: E402

KEY_RE = re.compile(r'^r(?:16|30|17|1|2|3) = "(.+)"$')
CAST_RE = re.compile(r'^r8 = (.+)$')
NESTED_RE = re.compile(r'^r0 = ([A-Za-z0-9_$]+)\.fromJson\(\)$')
READER_RE = re.compile(r'^r0 = (int_|double_|bool_|string|num_|listOf|parseList)\(\)$')
READER_TYPES = {'int_': 'int', 'double_': 'double', 'bool_': 'bool', 'string': 'String',
                'num_': 'num', 'listOf': 'List', 'parseList': 'List'}
TYPE_RE = re.compile(r'^[A-Za-z_][A-Za-z0-9_$<>?, ]*$')
ELEM_RE = re.compile(r'^r1 = <([^>]+)>$')


def _is_call(text):
    return (text.startswith('blr') or text.startswith('r0 = GDT[')
            or text.startswith('r0 = _getValueOrData(')
            or bool(READER_RE.match(text)))


def _is_key(instrs, i):
    for j in range(i + 1, min(i + 9, len(instrs))):
        if _is_call(instrs[j].text):
            return True
        if A.ASSIGN_KEY_BREAK.match(instrs[j].text):
            return False
    return False


def parse_from_json(fn):
    segs = []  # [key, first_idx, last_idx]
    ins = fn.instrs
    for i, x in enumerate(ins):
        m = KEY_RE.match(x.text)
        if m and _is_key(ins, i):
            key = m.group(1)
            if segs and segs[-1][0] == key:
                continue
            segs.append([key, i, i, x.addr])
    fields = []
    for n, (key, start, _, addr) in enumerate(segs):
        end = segs[n + 1][1] if n + 1 < len(segs) else len(ins)
        cast = nested = elem = reader = None
        growable = tryparse = False
        null_check = False
        blr_seen = False
        since_blr = 0
        for j in range(start, end):
            t = ins[j].text
            m = READER_RE.match(t)
            if m and reader is None:
                reader = READER_TYPES[m.group(1)]
            if _is_call(t) and not blr_seen:
                blr_seen = True
                since_blr = 0
                continue
            if blr_seen and since_blr < 3:
                since_blr += 1
                if t.startswith('cmp') and 'NULL' in t and 'w0' in t:
                    null_check = True
            if cast is None:
                m = CAST_RE.match(t)
                if m and TYPE_RE.match(m.group(1)):
                    cast = m.group(1)
            m = NESTED_RE.match(t)
            if m and nested is None:
                nested = m.group(1)
            m = ELEM_RE.match(t)
            if m:
                elem = m.group(1)
            if 'GrowableList' in t or '_GrowableList' in ' '.join(ins[j].raw):
                growable = True
            if 'tryParse' in ' '.join(ins[j].raw):
                tryparse = True
        dtype, nullable = classify(cast, nested, elem, growable, tryparse, null_check, reader)
        fields.append({'json_key': key, 'dart_type': dtype, 'nullable': nullable,
                       'key_addr': addr})
    return fields


def classify(cast, nested, elem, growable, tryparse, null_check, reader):
    if nested and (cast is None or cast.startswith('Map')):
        return nested + ('?' if null_check else ''), null_check
    if cast and cast.startswith('List'):
        if elem:
            if growable:
                return 'List<%s>' % elem, False
            return 'List<%s>%s' % (elem, '?' if cast.endswith('?') else ''), cast.endswith('?')
        return cast, cast.endswith('?')
    if cast:
        return cast, cast.endswith('?') or null_check
    if reader:
        return reader, None
    if tryparse:
        return 'int?', True
    if null_check:
        return 'unknown', True
    return 'unknown', None


def scan_models(root, log=None):
    t0 = time.time()
    out = {}
    for p, rel in A.iter_dart_files(root):
        ok, _ = A.file_contains(p, ['.fromJson('])
        if not ok:
            continue
        for fn in A.iter_functions(p, rel):
            h = fn.header.strip()
            # `factory X.fromJson` and plain constructors written as `_ X.fromJson`
            if not (h.startswith('factory') or h.startswith('_ ')) or not fn.name.endswith('.fromJson'):
                continue
            cls = fn.name.rsplit('.', 1)[0]
            out[(rel, cls)] = {
                'class': cls, 'dart_file': rel, 'from_json_addr': fn.addr,
                'fields': parse_from_json(fn),
            }
    if log:
        log('models %s: %d in %.1fs' % (root, len(out), time.time() - t0))
    return out


def match_old(new, old):
    """Map new key -> old key; same (file, class), else a unique class name."""
    by_cls_new, by_cls_old = {}, {}
    for k in new:
        by_cls_new.setdefault(k[1], []).append(k)
    for k in old:
        by_cls_old.setdefault(k[1], []).append(k)
    m = {}
    for k in new:
        if k in old:
            m[k] = k
        elif len(by_cls_new[k[1]]) == 1 and len(by_cls_old.get(k[1], [])) == 1:
            m[k] = by_cls_old[k[1]][0]
    return m


def build_models(root, version, old_root=None, log=None):
    new = scan_models(root, log)
    old = scan_models(old_root, log) if old_root else None
    rows = []
    if old is None:
        for k in sorted(new):
            r = dict(new[k])
            r['since'] = None
            for f in r['fields']:
                f['since'] = None
            rows.append(r)
        return {'rows': rows, 'old': None}
    mp = match_old(new, old)
    for k in sorted(new):
        r = dict(new[k])
        r['fields'] = [dict(f) for f in r['fields']]
        if k in mp:
            ok = {f['json_key'] for f in old[mp[k]]['fields']}
            r['since'] = '≤3.18.0'
            for f in r['fields']:
                f['since'] = '≤3.18.0' if f['json_key'] in ok else version
            nk = {f['json_key'] for f in r['fields']}
            r['removed_keys'] = sorted(ok - nk)
        else:
            r['since'] = version
            r['removed_keys'] = []
            for f in r['fields']:
                f['since'] = version
        rows.append(r)
    matched_old = set(mp.values())
    for k in sorted(old):
        if k in matched_old:
            continue
        r = dict(old[k])
        r['fields'] = [dict(f, since='≤3.18.0') for f in r['fields']]
        r['since'] = '≤3.18.0'
        r['removed_in'] = version
        r['removed_keys'] = []
        rows.append(r)
    return {'rows': rows, 'old': old, 'new': new, 'match': mp}


def package_of(dart_file):
    """First directory of the Dart file path ('' for a file in the root)."""
    return dart_file.split('/', 1)[0] if '/' in dart_file else ''


def _labels(dart_file):
    """Key prefixes from the short package to the full file path (no `.dart`)."""
    parts = dart_file.split('/')
    dirs, stem = parts[:-1], '/'.join(parts)
    if stem.endswith('.dart'):
        stem = stem[:-5]
    out = ['/'.join(dirs[:d]) for d in range(1, len(dirs) + 1)] or [package_of(dart_file)]
    out.append(stem)
    return out


def assign_keys(rows):
    """Set `key` = `<package>::<class>` on every row; return the rows sorted by key."""
    groups = {}
    for r in rows:
        groups.setdefault((package_of(r['dart_file']), r['class']), []).append(r)
    for (pkg, cls), grp in groups.items():
        if len(grp) == 1:
            grp[0]['key'] = '%s::%s' % (pkg, cls)
            continue
        labels = [_labels(r['dart_file']) for r in grp]
        for lvl in range(max(map(len, labels))):
            pick = [l[min(lvl, len(l) - 1)] for l in labels]
            if len(set(pick)) == len(pick):
                break
        for r, p in zip(grp, pick):
            r['key'] = '%s::%s' % (p, cls)
    return sorted(rows, key=lambda r: r['key'])


def is_noise(r):
    """A class of the `sentry` package (field-less app classes are not noise)."""
    return package_of(r['dart_file']) == 'sentry'


def filter_noise(rows, include_noise):
    return list(rows) if include_noise else [r for r in rows if not is_noise(r)]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('asm_root')
    ap.add_argument('--version', required=True)
    ap.add_argument('--old-root', default=A.DEFAULT_OLD_ROOT)
    ap.add_argument('--snapshot', default=A.SNAPSHOT_3_24_3)
    ap.add_argument('--out', default='data/models.json')
    ap.add_argument('--include-noise', action='store_true',
                    help='keep the sentry package')
    a = ap.parse_args(argv)
    A.check_root(a.asm_root, a.version)
    t0 = time.time()
    res = build_models(a.asm_root, a.version, a.old_root,
                       log=lambda s: print(s, file=sys.stderr))
    gen = 'tools/model_fields.py asm_root --version %s' % a.version
    if a.include_noise:
        gen += ' --include-noise'
    keyed = assign_keys(res['rows'])
    rows = filter_noise(keyed, a.include_noise)
    A.write_json(a.out, gen, a.version, a.snapshot, rows)
    print('%d rows (%d dropped as noise) -> %s (%.1fs)'
          % (len(rows), len(keyed) - len(rows), a.out, time.time() - t0))
    return 0


if __name__ == '__main__':
    sys.exit(main())
