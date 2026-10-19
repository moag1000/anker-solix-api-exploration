"""Endpoint inventory from Blutter asm.

Usage:
  python3 -I tools/endpoint_inventory.py <asm_root> --version 3.24.3 \
      [--old-root <3.18.0 asm root>] [--upstream apitypes.py] [--out data/endpoints.json]

One row per (function, URL literal).  `role` is `sender` when the function
itself calls an `*Http*` helper and `url_provider` when it only holds the URL
(api_url.dart style); callers then lead to the senders.  Parameters are read
heuristically from map literals (string literals stored at even array slots),
so every row is `string-only` evidence until a human traces it.
"""
import argparse
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import asmparse as A  # noqa: E402
import smi  # noqa: E402

STR_RE = re.compile(r'^(r\d+) = "(.*)"$')
INT_RE = re.compile(r'^(r\d+) = (-?\d+)$')
CONST_RE = re.compile(r'^(r\d+) = (true|false|Null)$')
ASSIGN_RE = re.compile(r'^(r\d+) = ')
STORE_DEC_RE = re.compile(
    r'^(?:StoreField: r\d+->field_([0-9a-f]+)|ArrayStore: r\d+\[\d+\]) = (r\d+|rZR)')
ZR_STORE_RE = re.compile(r'\b(?:stur|str)\s+([wx])zr\b')
WRITE_RE = re.compile(
    r'^(?:ldur|ldr|mov|add|sub|and|orr|eor|movz|movk|sbfiz|sbfx)\s+[xw](\d+)')
OFF_RES = (re.compile(r'\[x\d+, #0x([0-9a-f]+)\]'),
           re.compile(r'add\s+x25, x\d+, #0x([0-9a-f]+)'))
SENDER_CALLEE_RE = re.compile(
    r'RequestHttp|requestHttp|postJML|HttpHelper::request$|StationApiClient::request$')
SEG_SNAKE_RE = re.compile(r'^/[a-z0-9_]+(/[a-z0-9_.]+)+$')
SEG_ANY_RE = re.compile(r'^/[A-Za-z0-9_\-]+(/[A-Za-z0-9_\-.]+)+$')


class Frame:
    def __init__(self, n):
        self.n = n
        self.keys = {}      # slot -> key text
        self.vals = {}      # key -> value descriptor
        self.children = {}  # slot -> child Frame
        self.json = False
        self.attached = False
        self.slot_of = {}


def leaves(frame, prefix=''):
    out = []
    for slot in sorted(frame.keys):
        k = frame.keys[slot]
        if k is None:
            continue
        child = frame.children.get(slot + 1)
        if child is not None:
            sub = leaves(child, prefix + k + '.')
            out.extend(sub if sub else [prefix + k])
        else:
            out.append(prefix + k)
    return out


def _store_slot(ins, off_hex):
    if off_hex is None:
        for r in ins.raw:
            for rx in OFF_RES:
                m = rx.search(r)
                if m:
                    off_hex = m.group(1)
                    break
            if off_hex:
                break
    if off_hex is None:
        return None
    off = int(off_hex, 16)
    if off < 0xf or (off - 0xf) % 4:
        return None
    return (off - 0xf) // 4


def extract_request(fn):
    """Walk one function and return the heuristic request description."""
    stack, popped = [], []
    lit = {}
    last = None      # last popped map that nobody has stored yet
    r0_child = None  # map currently held in r0 (result of Map._fromLiteral/jsonEncode)
    instrs = fn.instrs
    for idx, ins in enumerate(instrs):
        t = ins.text
        m = STR_RE.match(t)
        if m:
            lit[m.group(1)] = ('s', m.group(2), ins.addr)
            continue
        m = INT_RE.match(t)
        if m:
            lit[m.group(1)] = ('i', int(m.group(2)), ins.addr)
            continue
        m = CONST_RE.match(t)
        if m:
            lit[m.group(1)] = ('c', m.group(2), ins.addr)
            continue
        if t.startswith('r0 = AllocateArray('):
            r0_child = None
            n = lit.get('r2')
            stack.append(Frame(n[1] // 2 if n and n[0] == 'i' else 64))
            lit.pop('r0', None)
            continue
        if t.startswith('r0 = Map._fromLiteral('):
            prev = ' '.join(r for p in instrs[max(0, idx - 3):idx] for r in p.raw)
            if 'empty_array' not in prev and stack:
                fr = stack.pop()
                popped.append(fr)
                last = r0_child = fr
            else:
                r0_child = None
            lit.pop('r0', None)
            continue
        if t.startswith('r0 = jsonEncode('):
            if last is not None and not last.attached:
                last.json = True
                r0_child = last
            else:
                r0_child = None
            lit.pop('r0', None)
            continue
        m = STORE_DEC_RE.match(t)
        if m and stack:
            off_hex, src = m.group(1), m.group(2)
            slot = _store_slot(ins, off_hex)
            fr = stack[-1]
            if slot is not None and slot < fr.n:
                val = lit.get(src)
                zr = None
                if src == 'rZR':
                    # store of the zero register: value 0 (a Smi 0 is raw 0)
                    for rl in ins.raw:
                        zr = ZR_STORE_RE.search(rl)
                        if zr:
                            break
                    val = ('i', 0, ins.addr)
                if slot % 2 == 0:
                    fr.keys[slot] = val[1] if val and val[0] == 's' else None
                else:
                    key = fr.keys.get(slot - 1)
                    if val is None:
                        if src == 'r0' and r0_child is not None:
                            fr.children[slot] = r0_child
                            r0_child.attached = True
                            fr.vals[key] = {'type': 'map'}
                            last = r0_child = None
                        else:
                            fr.vals[key] = {'type': 'variable'}
                    elif val[0] == 's':
                        fr.vals[key] = {'type': 'str', 'value': val[1],
                                        'addr': ins.addr}
                    elif val[0] == 'i':
                        # single Smi implementation: smi.decode_following
                        if src == 'rZR':
                            d = {'width': zr.group(1) if zr else None,
                                 'value': 0 if zr else None, 'odd': False}
                        else:
                            d = smi.decode_following(int(src[1:]), val[1], ins.raw)
                        fr.vals[key] = {'type': 'int', 'value': d['value'],
                                        'raw': val[1], 'width': d['width'],
                                        'odd': d['odd'], 'addr': val[2]}
                    else:
                        fr.vals[key] = {'type': val[1]}
            continue
        m = ASSIGN_RE.match(t)
        if m:
            lit.pop(m.group(1), None)
            if m.group(1) == 'r0':
                r0_child = None
            continue
        m = WRITE_RE.match(t)
        if m:
            lit.pop('r' + m.group(1), None)
            if m.group(1) == '0':
                r0_child = None
            continue
        if t.startswith('bl') or any(r.startswith('bl ') for r in ins.raw):
            lit.clear()
            r0_child = None
    roots = [f for f in popped if not f.attached]
    return summarize(roots)


def summarize(roots):
    out = {'params': [], 'envelope': [], 'param_data_is_json': False,
           'param_type': None, 'param_type_source': None, 'cmd': None, 'cmd_note': None, 'cmd_raw': None, 'cmd_addr': None}
    json_child = None
    env_root = None
    for r in roots:
        for slot, ch in r.children.items():
            if ch.json:
                json_child, env_root = ch, r
    if json_child is not None:
        out['param_data_is_json'] = True
        out['params'] = leaves(json_child)
        out['envelope'] = [k for k in env_root.keys.values() if k]
    else:
        seen = []
        for r in roots:
            for k in leaves(r):
                if k not in seen:
                    seen.append(k)
        out['params'] = seen
    for r in ([env_root] if env_root else []) + roots:
        v = r.vals.get('param_type')
        if v is not None and out['param_type'] is None:
            out['param_type'] = v['value'] if v['type'] == 'str' else 'variable'
            out['param_type_source'] = 'literal' if v['type'] == 'str' else 'variable'
        v = r.vals.get('cmd')
        if v is not None and out['cmd_raw'] is None and v['type'] == 'int':
            out['cmd_raw'], out['cmd_addr'] = v['raw'], v['addr']
            if v['value'] is None:
                out['cmd_note'] = 'store width not found'
            elif v['odd']:
                out['cmd'] = v['value']
                out['cmd_note'] = 'odd raw value in a tagged slot, re-check'
            else:
                out['cmd'] = v['value']
    return out


def url_ok(url, role, known_services):
    if role == 'sender':
        return bool(SEG_ANY_RE.match(url))
    if not SEG_SNAKE_RE.match(url):
        return False
    first = url.split('/')[1]
    return url.count('/') >= 3 or first.endswith(('_svc', '_service'))


def scan_root(root, log=None):
    """Return (records, http_callees, closure parents not needed).

    A record is one (function, URL) pair with its request description.
    """
    t0 = time.time()
    records = []
    callee_stats = {}
    for p, rel in A.iter_dart_files(root):
        with open(p, encoding='utf-8', errors='replace') as fh:
            text = fh.read()
        if not A.URL_PRECHECK_RE.search(text):
            continue
        parents = None
        for fn in A.iter_functions(p, rel):
            urls = []
            for ins in fn.instrs:
                m = A.url_literal(ins.text)
                if m and m[1] not in [u for u, _ in urls]:
                    urls.append((m[1], ins.addr))
            if not urls:
                continue
            callees = sorted({c for _, _, c in fn.callees()})
            http = [c for c in callees if SENDER_CALLEE_RE.search(c)]
            need_arg = any('"needEncryption"' in r for i in fn.instrs for r in i.raw)
            fname = fn.name
            if fname == '<anonymous closure>':
                if parents is None:
                    parents = A.closure_parents(text)
                par = parents.get(fn.addr)
                fname = ('<anonymous closure> in %s' % par) if par else \
                    '<anonymous closure>@%s' % fn.addr
            for url, uaddr in urls:
                role = 'sender' if http else 'url_provider'
                records.append({
                    'url': url, 'url_addr': uaddr, 'role': role,
                    'class': fn.cls, 'function': fname, 'addr': fn.addr,
                    'dart_file': rel, 'http_callees': http,
                    'need_arg': need_arg, '_req': None,
                })
            # request walk once per function (cheap, only for URL functions)
            req = extract_request(fn)
            for r in records[-len(urls):]:
                r['_req'] = req
            for c in http:
                callee_stats[c] = callee_stats.get(c, 0) + 1
    known = {r['url'].split('/')[1] for r in records
             if r['role'] == 'sender' and SEG_ANY_RE.match(r['url'])}
    records = [r for r in records if url_ok(r['url'], r['role'], known)]
    if log:
        log('scan %s: %d records in %.1fs' % (root, len(records), time.time() - t0))
    return records, callee_stats


def symbol_variants(pairs):
    """Map callee symbol (as printed in bl comments) -> owner 'Class::function'.

    `pairs` is an iterable of (class, function).
    """
    syms = {}
    for cls, fname in pairs:
        if cls and not fname.startswith('<'):
            owner = '%s::%s' % (cls, fname) if cls != '::' else '::' + fname
            names = {owner}
            if cls.endswith('Impl'):
                names.add('%s::%s' % (cls[:-4], fname))
            for n in names:
                syms.setdefault(n, set()).add(owner)
    return syms


def scan_call_sites(root, syms, window=0, log=None):
    """Find every call to a symbol in `syms`.

    Returns {owner: [(rel, caller_name, call_addr, window, caller_class)]}
    where window is the list of (addr, text) of the `window` instructions
    before the call.  Closures are attributed to their enclosing function.
    """
    t0 = time.time()
    out = {}
    for p, rel in A.iter_dart_files(root):
        with open(p, encoding='utf-8', errors='replace') as fh:
            text = fh.read()
        called = set(A.ALL_CALLEE_RE.findall(text)) & set(syms)
        if not called:
            continue
        parents = A.closure_parents(text)
        for fn in A.iter_functions(p, rel):
            for idx, ins in enumerate(fn.instrs):
                for r in ins.raw:
                    m = A.CALLEE_RE.search(r)
                    if not (m and m.group(2) in called):
                        continue
                    cls, cname = fn.cls, fn.name
                    if cname == '<anonymous closure>':
                        par = parents.get(fn.addr)
                        if par and '::' in par:
                            cls, cname = par.split('::', 1)
                        else:
                            cname = cname + '@' + fn.addr
                    win = [(i.addr, i.text) for i in
                           fn.instrs[max(0, idx - window):idx]] if window else []
                    for owner in syms[m.group(2)]:
                        out.setdefault(owner, []).append(
                            (rel, cname, ins.addr, win, cls))
    if log:
        log('call sites %s: %.1fs' % (root, time.time() - t0))
    return out


def find_callers(root, records, log=None):
    """Map 'Class::function' (sender symbol) -> sorted caller names."""
    sites = scan_call_sites(
        root, symbol_variants((r['class'], r['function']) for r in records), 0, log)
    return {k: sorted({'%s::%s' % (site[0], site[1]) for site in v})
            for k, v in sites.items()}


def encryption_note(rec):
    cs = rec['http_callees']
    if not cs or any('encryptionRequestHttp' in c for c in cs):
        return None
    if rec['need_arg']:
        return ('plain callee; the call passes needEncryption (value not '
                'decoded), callee default is true')
    return 'plain callee; callee default needEncryption=true, not overridden here'


def service_of(url):
    return url.split('/')[1]


def pool_text(root):
    """Object-pool dump (`pp.txt`, one level above the asm root), '' if missing."""
    p = os.path.join(os.path.dirname(os.path.abspath(root)), 'pp.txt')
    if not os.path.isfile(p):
        return ''
    with open(p, encoding='utf-8', errors='replace') as fh:
        return fh.read()


def in_pool(pool, url):
    """Is the URL string (with or without leading slash) in the pool dump?"""
    return ('"%s"' % url in pool) or ('"%s"' % url.lstrip('/') in pool)


def build_inventory(root, version, old_root=None, upstream=None, log=None):
    records, callee_stats = scan_root(root, log)
    callers = find_callers(root, records, log)
    old_urls = set()
    old_records = []
    if old_root:
        old_records, _ = scan_root(old_root, log)
        old_urls = {r['url'] for r in old_records}
    up_eps = {}
    if upstream and os.path.isfile(upstream):
        eps, _ = A.load_upstream(upstream)
        for k, v in eps.items():
            up_eps.setdefault('/' + v.lstrip('/'), []).append(k)
    new_urls = {r['url'] for r in records}
    pool = pool_text(root) if old_root else ''
    rows = []
    for r in records:
        req = r['_req'] or {}
        sym = '%s::%s' % (r['class'], r['function'])
        keys = up_eps.get(r['url'], [])
        row = {
            'url': r['url'], 'service': service_of(r['url']),
            'function': r['function'], 'class': r['class'],
            'dart_file': r['dart_file'], 'addr': r['addr'],
            'url_addr': r['url_addr'], 'role': r['role'],
            'params': req.get('params', []),
            'envelope': req.get('envelope', []),
            'param_data_is_json': req.get('param_data_is_json', False),
            'param_type': req.get('param_type'),
            'cmd': req.get('cmd'), 'cmd_raw': req.get('cmd_raw'),
            'cmd_note': req.get('cmd_note'),
            'param_type_source': req.get('param_type_source'),
            'cmd_addr': req.get('cmd_addr'),
            'encrypted': any('encryptionRequestHttp' in c for c in r['http_callees']),
            'encryption_note': encryption_note(r),
            'http_callees': r['http_callees'],
            'callers': callers.get(sym, []),
            'upstream_key': keys[0] if keys else None,
            'since': ('≤3.18.0' if r['url'] in old_urls else version)
            if old_root else None,
        }
        rows.append(row)
    if old_root:
        for r in old_records:
            if r['url'] in new_urls:
                continue
            req = r['_req'] or {}
            keys = up_eps.get(r['url'], [])
            rows.append({
                'url': r['url'], 'service': service_of(r['url']),
                'function': r['function'], 'class': r['class'],
                'dart_file': r['dart_file'], 'addr': r['addr'],
                'url_addr': r['url_addr'], 'role': r['role'],
                'params': req.get('params', []),
                'envelope': req.get('envelope', []),
                'param_data_is_json': req.get('param_data_is_json', False),
                'param_type': req.get('param_type'),
                'cmd': req.get('cmd'), 'cmd_raw': req.get('cmd_raw'),
            'cmd_note': req.get('cmd_note'),
            'param_type_source': req.get('param_type_source'),
                'cmd_addr': req.get('cmd_addr'),
                'encrypted': any('encryptionRequestHttp' in c
                                 for c in r['http_callees']),
                'encryption_note': encryption_note(r),
                'http_callees': r['http_callees'],
                'callers': [], 'upstream_key': keys[0] if keys else None,
                'since': '≤3.18.0',
            })
            # removed_in = no literal at all in the new pool; a string that is
            # still in the pool but has no asm load is "pool-only", not removed
            if in_pool(pool, r['url']):
                rows[-1]['reference'] = 'pool-only'
            else:
                rows[-1]['removed_in'] = version
    rows.sort(key=lambda x: (x['url'], x['dart_file'], x['function']))
    return {'rows': rows, 'http_callees': callee_stats}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('asm_root')
    ap.add_argument('--version', required=True)
    ap.add_argument('--old-root', default=A.DEFAULT_OLD_ROOT)
    ap.add_argument('--upstream', default=A.DEFAULT_UPSTREAM)
    ap.add_argument('--snapshot', default=A.SNAPSHOT_3_24_3)
    ap.add_argument('--out', default='data/endpoints.json')
    a = ap.parse_args(argv)
    t0 = time.time()
    inv = build_inventory(a.asm_root, a.version, a.old_root, a.upstream,
                          log=lambda s: print(s, file=sys.stderr))
    gen = 'tools/endpoint_inventory.py %s --version %s' % (
        'asm_root', a.version)
    A.write_json(a.out, gen, a.version, a.snapshot, inv['rows'])
    print('%d rows -> %s (%.1fs)' % (len(inv['rows']), a.out, time.time() - t0))
    print('distinct *Http* callees in sender functions:')
    for k, v in sorted(inv['http_callees'].items()):
        print('  %5d  %s' % (v, k))
    return 0


if __name__ == '__main__':
    sys.exit(main())
