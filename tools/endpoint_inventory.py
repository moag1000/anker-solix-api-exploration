"""Endpoint inventory from Blutter asm.

Usage:
  python3 -I tools/endpoint_inventory.py <asm_root> --version 3.24.3 \
      [--old-root <3.18.0 asm root>] [--upstream apitypes.py] [--out data/endpoints.json]

One row per (function, URL literal).  `role` is `sender` when the function
itself calls an `*Http*` helper and `url_provider` when it only holds the URL
(api_url.dart style); `resolve_senders` then follows the callers up to 3 levels
and records `sender`/`sender_via` (or `resolution`: mixin-gap | unresolved).  Parameters are read
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
SDK_SEND_RE = re.compile(
    r'(AKIoTKitManagerImpl|AkIotKitFlutter)::handle(WithProgress)?$')
MAX_DEPTH = 3
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
        called = (set(A.ALL_CALLEE_RE.findall(text))
                  | {'%s::%s' % m for m in FIELD_LOAD_RE.findall(text)}) & set(syms)
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


DEDUP_LIB = 'dart:mixin_deduplication'
# a static late field holding a URL (api_url.dart `Api.getPrice`) is read, not called
FIELD_LOAD_RE = re.compile(r'\] Field <([^>.\s]+)\.([^>\s]+)>')
# modules whose functions wrap the HTTP primitives (S1); a literal inside the
# generic HTTP manager is a path check, never a request
HELPER_FILE_RE = re.compile(r'(^|/)http_(helper|manager)\.dart$|_http_')
GENERIC_PROVIDER_RE = re.compile(r'(^|/)http_(helper|manager)\.dart$')
SKIP_CALLEE_LIB_RE = re.compile(r'^(dart:|package:flutter/|package:get/)')
GENERIC_FANIN = 30   # a callee called from more functions than this is a utility


def is_primitive(sym):
    """S0: the HTTP / SDK primitives, recognised by callee symbol."""
    return bool(SENDER_CALLEE_RE.search(sym) or SDK_SEND_RE.search(sym))


def owner_of(rec):
    """'Class::function' that holds a record; closures belong to their enclosing
    function, a closure without a known parent has no owner (None)."""
    fname = rec['function']
    if fname.startswith('<anonymous closure> in '):
        return fname[len('<anonymous closure> in '):]
    if fname.startswith('<'):
        return None
    return '%s::%s' % (rec['class'], fname) if rec['class'] != '::' else '::' + fname


def _pair(owner):
    cls, fname = owner.split('::', 1)
    return (cls or '::', fname)


def label(owner, addr):
    return '%s @%s' % (owner, addr)


def _lib_rel(lib):
    """asm-tree path of a `package:` library (None for dart:/field loads)."""
    if lib and lib.startswith('package:'):
        return lib[len('package:'):].replace('%20', ' ')
    return None


class Fn:
    """One function or closure of the dump with its calls in address order."""
    __slots__ = ('owner', 'addr', 'rel', 'calls', 'urls')

    def __init__(self, owner, addr, rel):
        self.owner, self.addr, self.rel = owner, addr, rel
        self.calls = []   # (addr int, symbol, lib or 'field')
        self.urls = set()

    def label(self):
        return label(self.owner, self.addr)


class Graph:
    def __init__(self):
        self.funcs = []
        self.by_addr = {}    # (rel, addr) -> Fn
        self.group = {}      # (rel, owner) -> [Fn] (a function and its closures)
        self.defs = {}       # callee symbol -> [(rel, exact, owner key)]
        self.sites = {}      # callee symbol -> [(Fn, addr int, lib)]
        self.s1 = set()      # (rel, owner) of http-module functions calling a primitive
        self.mixin_pairs = set()

    def callee_defs(self, sym, lib):
        """Fns with a body that define the callee symbol: the exact class and
        its Impl variant (an abstract interface method has no body)."""
        exact = [(rel, key) for rel, ex, key in self.defs.get(sym, ()) if ex]
        variant = [(rel, key) for rel, ex, key in self.defs.get(sym, ()) if not ex]
        if len({rel for rel, _ in exact}) > 1 and _lib_rel(lib):
            exact = [p for p in exact if p[0] == _lib_rel(lib)] or exact
        pool = exact + variant
        return [f for _, key in pool for f in self.group[key] if f.calls]

    def sends(self, fn, ref):
        """First send call of `fn` after address `ref`: (kind, symbol, target Fn)
        with kind 'self' (a primitive) or 'wrapper' (an S1 function), else None."""
        for addr, sym, lib in fn.calls:
            if addr <= ref:
                continue
            if is_primitive(sym):
                return 'self', sym, fn
            rel = _lib_rel(lib)
            for r2, is_exact, key in self.defs.get(sym, ()):
                if key in self.s1 and (rel is None or r2 == rel or not is_exact):
                    return 'wrapper', sym, self.group[key][0]
        return None

    def group_sends(self, key):
        for f in self.group[key]:
            h = self.sends(f, -1)
            if h:
                return f, h
        return None


def build_graph(root, log=None):
    t0 = time.time()
    g = Graph()
    mix = []
    for p, rel in A.iter_dart_files(root):
        with open(p, encoding='utf-8', errors='replace') as fh:
            text = fh.read()
        parents = A.closure_parents(text)
        for fn in A.iter_functions(p, rel):
            cls, cname = fn.cls, fn.name
            if cname == '<anonymous closure>':
                par = parents.get(fn.addr)
                owner = par if par else '%s::<anonymous closure>@%s' % (cls, fn.addr)
            else:
                owner = '%s::%s' % (cls, cname) if cls != '::' else '::' + cname
            f = Fn(owner, fn.addr, rel)
            for ins in fn.instrs:
                u = A.url_literal(ins.text)
                if u:
                    f.urls.add(u[1])
                for r in ins.raw:
                    m = A.CALLEE_RE.search(r)
                    if m:
                        f.calls.append((int(ins.addr, 16), m.group(2), m.group(1)))
                        if '&' in m.group(2).split('::')[0] and (
                                m.group(1) == DEDUP_LIB
                                or not m.group(1).startswith('dart:')):
                            mix.append(m.group(2))
                        continue
                    m = FIELD_LOAD_RE.search(r)
                    if m:
                        f.calls.append((int(ins.addr, 16), '%s::%s' % m.groups(),
                                        'field'))
            g.funcs.append(f)
            g.by_addr[(rel, fn.addr)] = f
            key = (rel, owner)
            g.group.setdefault(key, []).append(f)
    for key in g.group:
        rel, owner = key
        cls, fname = _pair(owner)
        names = {owner}
        if cls.endswith('Impl'):
            names.add('%s::%s' % (cls[:-4], fname))
        for n in names:
            g.defs.setdefault(n, []).append((rel, n == owner, key))
    for f in g.funcs:
        for addr, sym, lib in f.calls:
            g.sites.setdefault(sym, []).append((f, addr, lib))
    # S1: functions of http helper/manager modules that call a primitive
    for key, fns in g.group.items():
        if HELPER_FILE_RE.search(key[0]) and any(
                is_primitive(s) for f in fns for _, s, _ in f.calls):
            g.s1.add(key)
    # mixin applications whose body is absent: (class component, name) pairs
    for sym in mix:
        cls, name = sym.split('::', 1)
        if sym in g.defs:
            continue
        for comp in cls.split('&'):
            g.mixin_pairs.add((comp, name))
    if log:
        log('graph: %d functions, %d S1 wrappers in %.1fs'
            % (len(g.funcs), len(g.s1), time.time() - t0))
    return g


def _callers(g, fn):
    """Call sites of the owner function of `fn`: {caller Fn: first call addr}."""
    cls, fname = _pair(fn.owner)
    names = {fn.owner}
    if cls.endswith('Impl'):
        names.add('%s::%s' % (cls[:-4], fname))
    out = {}
    exact_rels = {k[0] for k in g.group if k[1] == fn.owner}
    for name in names:
        for cf, addr, lib in g.sites.get(name, ()):
            rel = _lib_rel(lib)
            if len(exact_rels) > 1 and rel is not None and rel != fn.rel:
                continue
            if cf.owner == fn.owner and cf.rel == fn.rel:
                continue
            if cf not in out or addr < out[cf]:
                out[cf] = addr
    return out


def _absent_mixin(g, sym, lib):
    """A mixin application symbol whose body is not in the dump (not a
    ubiquitous one such as `RxObjectMixin.value`, called from > GENERIC_FANIN
    functions)."""
    return ('&' in sym.split('::')[0] and sym not in g.defs
            and (lib == DEDUP_LIB or not lib.startswith('dart:'))
            and len({c[0] for c in g.sites.get(sym, ())}) <= GENERIC_FANIN)


def _nearest_in(g, fn, ref, url, gaps):
    """Rules (a) and (b) at one function: its own send call after `ref`, else a
    non-generic callee called after `ref` that sends.  Returns a hit dict."""
    h = g.sends(fn, ref)
    if h:
        kind, sym, target = h
        return {'order': 0, 'kind': kind, 'wrapper': sym, 'sender': target}
    for addr, sym, lib in fn.calls:
        if addr <= ref:
            continue
        if _absent_mixin(g, sym, lib):
            gaps.append(sym)
            continue
        if is_primitive(sym) or lib == 'field' or SKIP_CALLEE_LIB_RE.match(lib):
            continue
        if len({c[0] for c in g.sites.get(sym, ())}) > GENERIC_FANIN:
            continue
        for gfn in g.callee_defs(sym, lib):
            gkey = (gfn.rel, gfn.owner)
            if gkey == (fn.rel, fn.owner):
                continue
            if set().union(*(f.urls for f in g.group[gkey])) - {url}:
                continue   # it holds another endpoint's literal
            gs = g.group_sends(gkey)
            if not gs:
                gaps.extend(c[1] for f in g.group[gkey] for c in f.calls
                            if _absent_mixin(g, c[1], c[2]))
            if gs:
                return {'order': 1, 'kind': 'callee', 'wrapper': gs[1][1],
                        'sender': gs[0]}
    return None


def _nearest(g, fn, ref, url, gaps):
    """`_nearest_in` on the function itself, else on its sibling closures (the
    body of an async function lives in closures of the same owner; no address
    order across closures).  A sibling holding another endpoint's literal is
    skipped."""
    hit = _nearest_in(g, fn, ref, url, gaps)
    if hit:
        return hit
    for sib in g.group[(fn.rel, fn.owner)]:
        if sib is fn or sib.urls - {url} - fn.urls:
            continue
        hit = _nearest_in(g, sib, -1, url, gaps)
        if hit:
            hit['order'] = 2
            return hit
    return None


def _result(via, hit):
    s = hit['sender']
    res = {'sender': s.label(), 'sender_file': s.rel,
           'sender_via': [f.label() for f in via],
           'sender_via_files': [f.rel for f in via],
           'sender_kind': hit['kind'], 'sender_wrapper': hit['wrapper']}
    return res


def resolve_senders(root, records, max_depth=MAX_DEPTH, log=None, graph=None):
    """Resolve url_provider records to the function that sends.

    Nearest sender first.  At the function F that holds (or receives) the URL:
    (a) F calls an HTTP/SDK primitive or an http-module wrapper after the URL
    load, (b) a non-generic callee of F called after the URL load sends,
    (c) else repeat at the callers of F, at most `max_depth` levels.
    Returns {(dart_file, addr, url_addr): result}.  A result has `sender`,
    `sender_file`, `sender_via`/`sender_via_files` (functions walked up from the
    provider, excluding it, innermost first), `sender_kind` (self | wrapper |
    callee), `sender_wrapper` (the primitive or wrapper symbol called) and
    optionally `sender_also`; or `resolution`: generic-path-check | mixin-gap
    | unresolved.
    """
    t0 = time.time()
    g = graph or build_graph(root, log)
    out = {}
    for r in records:
        if r['role'] != 'url_provider':
            continue
        key = (r['dart_file'], r['addr'], r['url_addr'])
        if GENERIC_PROVIDER_RE.search(r['dart_file']):
            out[key] = {'resolution': 'generic-path-check'}
            continue
        fn0 = g.by_addr.get((r['dart_file'], r['addr']))
        if fn0 is None:
            continue
        ref0 = int(r['url_addr'], 16)
        gaps = []
        hit = _nearest(g, fn0, ref0, r['url'], gaps)
        if hit:
            res = _result([], hit)
            if hit['sender'] is fn0:
                res['sender_via'] = []
            out[key] = res
            continue
        frontier = [(fn0, [])]
        seen = {(fn0.rel, fn0.owner)}
        visited = [fn0.owner]
        res = None
        for _ in range(max_depth):
            hits, nxt = [], []
            for fn, via in frontier:
                for cf, addr in sorted(_callers(g, fn).items(),
                                       key=lambda kv: (kv[0].rel, kv[0].addr)):
                    h = _nearest(g, cf, addr, r['url'], gaps)
                    if h:
                        hits.append((via + [cf], h))
                    elif (cf.rel, cf.owner) not in seen:
                        seen.add((cf.rel, cf.owner))
                        visited.append(cf.owner)
                        nxt.append((cf, via + [cf]))
            if hits:
                hits.sort(key=lambda vh: (vh[1]['order'], vh[1]['sender'].label(),
                                          [f.label() for f in vh[0]]))
                res = _result(*hits[0])
                also = sorted({h['sender'].label() for _, h in hits[1:]}
                              - {res['sender']})[:5]
                if also:
                    res['sender_also'] = also
                same = [[f.label() for f in v] for v, h in hits[1:]
                        if h['sender'].label() == res['sender']]
                if same:
                    res['sender_via_also'] = same[:5]
                break
            frontier = nxt
        if res is None:
            gap = bool(gaps) or any(_pair(o) in g.mixin_pairs for o in visited)
            res = {'resolution': 'mixin-gap' if gap else 'unresolved'}
        out[key] = res
    if log:
        log('resolve senders: %d rows in %.1fs' % (len(out), time.time() - t0))
    return out


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
    resolved = resolve_senders(root, records, log=log)
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
        res = resolved.get((r['dart_file'], r['addr'], r['url_addr']))
        if res:
            row.update(res)
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
    A.check_root(a.asm_root, a.version)
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
