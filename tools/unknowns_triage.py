"""Triage the `## Known unknowns` bullets of every page into asm / server / device / unclear.

Usage (repo root):
  python3 -I tools/unknowns_triage.py <docs-root> [--out docs/audit/KNOWN_UNKNOWNS_TRIAGE.md]
         [--json tools/out/unknowns.json] [--override docs/audit/unknowns_overrides.json]

Reads every `*.md` under <docs-root> except `docs/archive/**`, `docs/superpowers/**`, `docs/templates/**`,
`.superpowers/**`, `tools/out/**` and hidden or `node_modules` directories. Under a
Known-unknowns heading (`## Known unknowns`, `## Known unknowns on this page`, or the
`#### Known unknowns` of a command section; the section ends at the next heading of the
same or a higher level; fenced code is skipped) every
bullet that starts with `- ` is one row (the skeleton placeholders `<!-- TODO -->` and
`<open question>` carry no question and are skipped); indented lines that follow belong to it.
Standard library only; nothing outside --out and --json is written.

Classes (first matching rule wins, order server, device, asm; the rule goes to `hint`):
  server   the answer lives on the server side, not in the app
  device   needs a real device, a capture or firmware knowledge
  asm      resolvable by reading more of the disassembly
  unclear  no rule matched

--override: JSON {"<page>:<hash>": {"class": "...", "note": "..."}}, hand-maintained;
<hash> = first 10 hex of the sha1 of the bullet text (strip, whitespace collapsed), so a
line shift keeps the override (the row field `key` holds it). Identical bullets on one
page share a key. --rekey-overrides rewrites the file from the current pages: old
`<page>:<line>` keys are migrated by the bullet at that line, hash keys stay (a hash key cannot
be mapped to an edited bullet text); keys that match no bullet are kept and reported, or
dropped with --prune-stale (the bullet text changed, so the override is obsolete and the bullet
falls back to the heuristic class until it is classified again).
A missing key keeps the heuristic class; the row then has hint `override` and keeps
the heuristic class in `heuristic_class`. A key that matches no row is reported on
stderr with its page and the exit code stays 0 (exit 1 with --strict); an invalid class exits 2.
The "Manual pass" section of the markdown is generated from the override file.
"""
import argparse
import datetime
import hashlib
import json
import os
import re
import sys

CLASSES = ('asm', 'server', 'device', 'unclear')
SKIP_PREFIXES = ('docs/archive/', 'docs/superpowers/', 'docs/templates/', '.superpowers/', 'tools/out/')
SKIP_DIRS = {'node_modules', '__pycache__'}
HEADING = re.compile(r'^(#{2,4}) Known unknowns(?: on this page)?\s*$')
ANY_HEADING = re.compile(r'^(#{1,6}) ')
TRUNC = 160

# (class, rule name, compiled regex); ordered, first match wins
_W = lambda *words: re.compile(r'\b(?:%s)' % '|'.join(re.escape(w) for w in words), re.I)
RULES = [
    ('server', 'server-word', _W('server', 'accepts', 'rejects', 'enforces', 'returns',
                                 'cloud side', 'backend')),
    ('device', 'device-word', _W('firmware', 'device test', 'on a real', 'capture',
                                 'which devices', 'hardware')),
    ('asm', 'asm-word', _W('polarity', 'closure', 'register', 'not traced', 'not decoded',
                           'not re-derived', 'which function', 'caller', 'builder')),
    ('asm', 'asm-address', re.compile(r'@0x')),
]
PLACEHOLDER = re.compile(r'^(<!--\s*TODO\s*-->|<open question>)$')
LINK = re.compile(r'\[([^\]]*)\]\([^)]*\)')


def classify(text):
    for cls, name, rx in RULES:
        m = rx.search(text)
        if m:
            return cls, '%s:%s' % (name, m.group(0).lower())
    return 'unclear', 'no-rule'


def _skipped(rel):
    if rel.startswith(SKIP_PREFIXES):
        return True
    return any(p in SKIP_DIRS or p.startswith('.') and p != '.superpowers'
               for p in rel.split('/')[:-1]) or rel.split('/')[0] == '.superpowers'


def pages(root):
    out = []
    for dp, dns, fns in os.walk(root):
        dns[:] = sorted(d for d in dns if d not in SKIP_DIRS and not d.startswith('.'))
        for fn in sorted(fns):
            if fn.endswith('.md'):
                rel = os.path.relpath(os.path.join(dp, fn), root).replace(os.sep, '/')
                if not _skipped(rel):
                    out.append(rel)
    return sorted(out)


def bullets(text):
    """Yield (line number, text) of the bullets under `## Known unknowns`."""
    inside = 0          # heading level of the open Known-unknowns section, 0 = none
    fence = False
    cur = None
    for n, line in enumerate(text.split('\n'), 1):
        if line.lstrip().startswith(('```', '~~~')):
            fence = not fence
            continue
        if fence:
            continue
        m = ANY_HEADING.match(line)
        if m:
            level = len(m.group(1))
            if inside and level <= inside:
                if cur:
                    yield cur[0], cur[1]
                    cur = None
                inside = 0
            h = HEADING.match(line)
            if h and not inside:
                inside = len(h.group(1))
            continue
        if not inside:
            continue
        if line.startswith('- '):
            if cur:
                yield cur[0], cur[1]
            cur = (n, line[2:].strip())
        elif cur and line[:1] in (' ', '\t') and line.strip():
            cur = (cur[0], cur[1] + ' ' + line.strip())
        elif cur and not line.strip():
            yield cur[0], cur[1]
            cur = None
    if cur:
        yield cur[0], cur[1]


def text_key(text):
    norm = ' '.join(text.split())
    return hashlib.sha1(norm.encode('utf-8')).hexdigest()[:10]


def collect(root):
    rows = []
    for rel in pages(root):
        with open(os.path.join(root, rel), encoding='utf-8') as f:
            text = f.read()
        for n, t in bullets(text):
            if PLACEHOLDER.match(t):
                continue    # skeleton bullet, carries no question
            cls, hint = classify(t)
            rows.append({'page': rel, 'line': n, 'text': t, 'class': cls, 'hint': hint,
                         'key': '%s:%s' % (rel, text_key(t))})
    return rows


def load_overrides(path):
    with open(path, encoding='utf-8') as f:
        ov = json.load(f)
    bad = [k for k, v in ov.items() if v.get('class') not in CLASSES]
    return ov, bad


def apply_overrides(rows, ov):
    """Apply overrides in place; return the keys that match no row."""
    keys = {}
    for r in rows:
        keys.setdefault(r['key'], []).append(r)
    for k, v in ov.items():
        for r in keys.get(k, ()):
            r['heuristic_class'] = r['class']
            r['heuristic_hint'] = r['hint']
            r['class'] = v['class']
            r['hint'] = 'override'
            r['note'] = v.get('note', '')
    return sorted(k for k in ov if k not in keys)


def rekey(rows, ov, prune=False):
    """Return (new override dict, stale keys): `page:line` keys become `page:hash`.

    A key that matches no bullet (a hash key whose bullet text changed cannot be mapped to the
    new text) is kept as it is, or dropped when `prune` is true; it is listed in `stale` either way."""
    by_line = {'%s:%d' % (r['page'], r['line']): r['key'] for r in rows}
    live = {r['key'] for r in rows}
    out, stale = {}, []
    for k, v in ov.items():
        page, _, tail = k.rpartition(':')
        nk = by_line.get(k) if tail.isdigit() else (k if k in live else None)
        if nk is None:
            stale.append(k)
            if prune:
                continue
            nk = k
        out[nk] = v
    return out, sorted(stale)


def cell(text, limit=TRUNC):
    t = LINK.sub(r'\1', text).replace('|', '\\|')
    return t if len(t) <= limit else t[:limit - 1].rstrip() + '…'


def render(rows, date):
    n = len(rows)
    by = {c: [r for r in rows if r['class'] == c] for c in CLASSES}
    out = [
        '> Verified against: App 3.24.3 · Date: %s · Page type: audit table · Owner page: this page' % date,
        '',
        '# Audit: Known unknowns triage',
        '',
        'Generated by `python3 -I tools/unknowns_triage.py . --out docs/audit/KNOWN_UNKNOWNS_TRIAGE.md '
        '--json tools/out/unknowns.json --override docs/audit/unknowns_overrides.json` '
        '(see [tools/README.md](../../tools/README.md#8-known-unknowns-triage)); do not edit by hand. '
        'Each row is one bullet of a `## Known unknowns` section. `line` is the line of the bullet '
        'in the page as it was when the tool ran. Text is cut at %d characters and links are flattened.' % TRUNC,
        '',
        '## Summary',
        '',
        '| class | count | share |',
        '|---|---|---|',
    ]
    for c in CLASSES:
        out.append('| %s | %d | %.1f%% |' % (c, len(by[c]), 100.0 * len(by[c]) / n if n else 0))
    out.append('| total | %d | 100.0%% |' % n)
    out += ['', 'Classes: `asm` = resolvable by reading more of the disassembly; `server` = the answer is '
            'on the server side; `device` = needs a real device, a capture or firmware knowledge; '
            '`unclear` = no rule matched and the manual pass left it open. Rules are ordered keyword '
            'matches (server, then device, then asm; first match wins), see `RULES` in the tool.']
    for c in CLASSES:
        out += ['', '## Class %s (%d)' % (c, len(by[c])), '']
        if not by[c]:
            out.append('No rows.')
            continue
        out += ['| page | line | text | hint |', '|---|---|---|---|']
        for r in by[c]:
            hint = r['hint']
            if hint == 'override':
                hint = 'override (was %s)' % r['heuristic_class']
            out.append('| %s | %d | %s | %s |' % (r['page'], r['line'], cell(r['text']), cell(hint)))
    ovr = [r for r in rows if r['hint'] == 'override']
    out += ['', '## Manual pass', '',
            'Every row that the keyword rules left `unclear` was read once more by hand; where the text '
            'names who can answer it, the class was set in `docs/audit/unknowns_overrides.json` '
            '(keyed `page:hash`; a missing key keeps the heuristic class). Re-classified: %d.' % len(ovr)]
    if ovr:
        out += ['', '| page | line | new class | note |', '|---|---|---|---|']
        for r in ovr:
            out.append('| %s | %d | %s | %s |' % (r['page'], r['line'], r['class'], cell(r.get('note', ''))))
    return '\n'.join(out) + '\n'


def write_text(path, text):
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('root', help='repo root (docs root) to scan')
    ap.add_argument('--out', help='markdown output path')
    ap.add_argument('--json', help='JSON output path (one row per bullet)')
    ap.add_argument('--override', help='hand-maintained overrides JSON')
    ap.add_argument('--rekey-overrides', action='store_true',
                    help='rewrite the --override file with hash keys from the current pages')
    ap.add_argument('--prune-stale', action='store_true',
                    help='with --rekey-overrides: drop keys that match no bullet instead of keeping them')
    ap.add_argument('--strict', action='store_true', help='exit 1 on a stale override key')
    ap.add_argument('--date', default=datetime.date.today().isoformat())
    a = ap.parse_args(argv)
    rows = collect(a.root)
    stale = []
    if a.override and os.path.isfile(a.override):
        ov, bad = load_overrides(a.override)
        if bad:
            print('override entries with an invalid class (nothing written): %s' % ', '.join(bad),
                  file=sys.stderr)
            return 2
        if a.rekey_overrides:
            old = ov
            ov, stale = rekey(rows, old, prune=a.prune_stale)
            write_text(a.override, json.dumps(ov, indent=1, sort_keys=True, ensure_ascii=False) + '\n')
            migrated = sum(1 for k in old if k.rpartition(':')[2].isdigit() and k not in stale)
            print('%s: %d line keys rekeyed, %d hash keys kept, %d keys matched no bullet (%s)'
                  % (a.override, migrated, len(ov) - migrated - (0 if a.prune_stale else len(stale)),
                     len(stale), 'pruned' if a.prune_stale else 'kept'))
        stale = apply_overrides(rows, ov)
        for k in stale:
            print('stale override (page %s: no bullet with this text hash): %s'
                  % (k.rpartition(':')[0], k), file=sys.stderr)
    if a.out:
        write_text(a.out, render(rows, a.date))
    if a.json:
        write_text(a.json, json.dumps({'generated_by': 'tools/unknowns_triage.py',
                                       'app_version': '3.24.3', 'rows': rows},
                                      indent=1, sort_keys=True, ensure_ascii=False) + '\n')
    counts = {c: sum(1 for r in rows if r['class'] == c) for c in CLASSES}
    print(json.dumps({'rows': len(rows), 'pages': len({r['page'] for r in rows}), **counts},
                     sort_keys=True))
    return 1 if (stale and a.strict) else 0


if __name__ == '__main__':
    sys.exit(main())
