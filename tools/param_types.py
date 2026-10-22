"""param_type / cmd table from every caller of set_/get_site_device_param.

Usage:
  python3 -I tools/param_types.py <asm_root> --version 3.24.3 \
      [--upstream apitypes.py] [--out data/param_types.json]

Every function that holds `/power_service/v1/site/set_site_device_param` or
`/power_service/v1/site/get_site_device_param` is read.  `param_type` is the
string literal stored after the `"param_type"` key, or `variable` when the key
is stored from a register; for those the call sites of the wrapper are
searched (look-back window) for a numeric string literal, and the result is
recorded as `traced_from` so that a human can verify it.  `cmd` follows the
Smi rule (a `stur wzr` store into the slot is cmd 0).  `cmd_set` / `cmd_get`
are the values of the set_ / get_site_device_param senders; `cmd` equals `cmd_set`.  Names come from `SolixParmType` in the upstream apitypes.py.
"""
import argparse
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import asmparse as A  # noqa: E402
import endpoint_inventory as E  # noqa: E402

SET_URL = '/power_service/v1/site/set_site_device_param'
GET_URL = '/power_service/v1/site/get_site_device_param'
DIGITS_RE = re.compile(r'^r\d+ = "(\d{1,3})"$')


def _sym(r):
    return '%s::%s' % (r['class'], r['function'])


MAX_HOPS = 3
ENVELOPE = {'site_id', 'param_type', 'cmd', 'param_data', 'device_sn'}


def trace_variable(root, records, log=None):
    """Trace wrappers whose param_type is a register back to their callers.

    Returns ({wrapper symbol: [(value, value_addr, chain)]},
             {wrapper symbol: [unresolved chain]}), chain = [caller file::fn, ...].
    """
    found, lost = {}, {}
    open_ = []  # (wrapper symbol, class, function, chain)
    for r in records:
        if r['_req'] and r['_req'].get('param_type') == 'variable':
            open_.append((_sym(r), r['class'], r['function'], []))
    for hop in range(MAX_HOPS):
        if not open_:
            break
        syms = E.symbol_variants((c, f) for _, c, f, _ in open_)
        sites = E.scan_call_sites(root, syms, window=60, log=log)
        nxt = []
        for wrapper, cls, fname, chain in open_:
            owner = '%s::%s' % (cls, fname) if cls != '::' else '::' + fname
            lst = sites.get(owner, [])
            if not [x for x in lst if not (x[1] == fname and x[0].endswith('http_request_repository.dart'))]:
                lost.setdefault(wrapper, []).append(chain + ['(no call site)'])
            for rel, name, call_addr, win, ccls in lst:
                if name == fname and rel.endswith('http_request_repository.dart'):
                    continue  # interface stub forwarding to the Impl, not a real caller
                step = '%s::%s' % (rel, name)
                val = None
                for addr, text in reversed(win):
                    m = DIGITS_RE.match(text)
                    if m:
                        val = (m.group(1), addr)
                        break
                if val:
                    found.setdefault(wrapper, []).append(
                        (val[0], val[1], chain + [step]))
                elif hop + 1 < MAX_HOPS and '@' not in name:
                    nxt.append((wrapper, ccls, name, chain + [step]))
                else:
                    lost.setdefault(wrapper, []).append(
                        chain + [step, '(no numeric literal in look-back window)'])
        open_ = nxt
    return found, lost


def build_param_types(root, version, upstream=None, log=None):
    records, _ = E.scan_root(root, log)
    recs = [r for r in records if r['url'] in (SET_URL, GET_URL)]
    names = {}
    if upstream and os.path.isfile(upstream):
        _, names = A.load_upstream(upstream)
    found, lost = trace_variable(root, recs, log)
    groups = {}

    def group(pt):
        return groups.setdefault(pt, {
            'param_type': pt, 'name': names.get(pt), 'set_function': [],
            'get_function': [], 'cmd': None, 'cmd_raw': None, 'cmd_addr': None,
            'cmd_set': None, 'cmd_set_raw': None, 'cmd_set_addr': None,
            'cmd_get': None, 'cmd_get_raw': None, 'cmd_get_addr': None,
            'cmd_by_function': {}, 'keys': [], 'get_model': None,
            'dart_files': [], 'traced_from': [], 'unresolved': [],
            'function_sources': {}, 'param_type_source': None})

    def add(pt, r, label, source):
        g = group(pt)
        g['function_sources'][label] = source
        kind = 'set_function' if r['url'] == SET_URL else 'get_function'
        if label not in g[kind]:
            g[kind].append(label)
        req = r['_req'] or {}
        if req.get('cmd') is not None:
            g['cmd_by_function'][label] = req['cmd']
            if pt != 'variable':
                role = 'set' if r['url'] == SET_URL else 'get'
                g['cmd_' + role], g['cmd_%s_raw' % role], g['cmd_%s_addr' % role] = (
                    req['cmd'], req['cmd_raw'], req['cmd_addr'])
                if role == 'set':
                    # `cmd` stays the SET value (backward compatible)
                    g['cmd'], g['cmd_raw'], g['cmd_addr'] = (
                        req['cmd'], req['cmd_raw'], req['cmd_addr'])
        if r['url'] == SET_URL and pt != 'variable':
            for k in req.get('params', []):
                if k not in g['keys'] and k not in ENVELOPE:
                    g['keys'].append(k)
        if r['dart_file'] not in g['dart_files']:
            g['dart_files'].append(r['dart_file'])

    for r in recs:
        req = r['_req'] or {}
        pt = req.get('param_type')
        if pt is None:
            continue
        if pt != 'variable':
            add(pt, r, r['function'], 'literal')
            continue
        sym = _sym(r)
        add('variable', r, r['function'], 'variable')
        for val, addr, chain in found.get(sym, []):
            add(val, r, '%s (via %s)' % (chain[-1].split('::', 1)[1], r['function']),
                'traced')
            groups[val]['traced_from'].append(
                {'wrapper': r['function'], 'chain': chain, 'value_addr': addr})
        for chain in lost.get(sym, []):
            groups['variable']['unresolved'].append(
                {'wrapper': r['function'], 'dart_file': r['dart_file'],
                 'chain': chain})
    rows = []
    for pt, g in groups.items():
        srcs = set(g['function_sources'].values())
        g['param_type_source'] = ('variable' if pt == 'variable' else
                                  'literal' if 'literal' in srcs else 'traced')
        if len(g['unresolved']) > 0:
            seen = []
            for u in g['unresolved']:
                if u not in seen:
                    seen.append(u)
            g['unresolved'] = seen
        rows.append(g)
    rows.sort(key=lambda g: (g['param_type'] == 'variable',
                             int(g['param_type']) if g['param_type'].isdigit() else 0,
                             g['param_type']))
    return {'rows': rows}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('asm_root')
    ap.add_argument('--version', required=True)
    ap.add_argument('--upstream', default=A.DEFAULT_UPSTREAM)
    ap.add_argument('--snapshot', default=A.SNAPSHOT_3_24_3)
    ap.add_argument('--out', default='data/param_types.json')
    a = ap.parse_args(argv)
    A.check_root(a.asm_root, a.version)
    t0 = time.time()
    res = build_param_types(a.asm_root, a.version, a.upstream,
                            log=lambda s: print(s, file=sys.stderr))
    gen = 'tools/param_types.py asm_root --version %s' % a.version
    A.write_json(a.out, gen, a.version, a.snapshot, res['rows'])
    print('%d rows -> %s (%.1fs)' % (len(res['rows']), a.out, time.time() - t0))
    for g in res['rows']:
        print('  %-9s cmd_set=%-5s cmd_get=%-5s set=%d get=%d unresolved=%d %s' % (
            g['param_type'], g['cmd_set'], g['cmd_get'], len(g['set_function']),
            len(g['get_function']), len(g['unresolved']), g['name'] or ''))
    return 0


if __name__ == '__main__':
    sys.exit(main())
