"""Request-body field extractor (read-only on the asm tree, standard library only).

For every endpoint row of data/endpoints.json the function that holds the URL
literal (the "builder": the sender itself for role=sender rows, the URL provider
otherwise) is replayed with a tiny register/slot tracker.  Every
`AllocateArray` that ends in `Map._fromLiteral` is a map literal; the string
literal stored in an even slot is the key, the value stored in the next slot is
classified by how its register was defined.  Everything is heuristic evidence:
`unknown` is emitted wherever the tracker cannot decide, and each field carries
the address of the key load and the raw instruction text of the value store.

Run from the repo root:
    python3 -I tools/request_fields.py <asm-root> --service power_service \
        --out tools/out/request_fields_power_service.json
    python3 -I tools/request_fields.py --check --out <file> [--models data/models.json]

Smi rule (../v3.24.3/audit/SMI_RULE.md): a 32-bit store of an immediate into a
tagged slot holds raw/2; an unboxed 64-bit value (BoxInt64Instr input) is raw.
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import asmparse as A  # noqa: E402

METHOD_POOL = {'0xa7e0': 'Method.post', '0x340e8': 'Method.get'}
POOL_RE = re.compile(r'\[pp\+(0x[0-9a-f]+)\]')
FROMJSON_RE = re.compile(r'^r\d+ = ([A-Za-z_$][\w$]*)\.(fromJson|fromMap)\(\)$')
REG_STR_RE = re.compile(r'^r(\d+) = "(.*)"$')
REG_INT_RE = re.compile(r'^r(\d+) = (-?\d+)$')
REG_BOOL_RE = re.compile(r'^r(\d+) = (true|false)$')
REG_NULL_RE = re.compile(r'^r(\d+) = Null$')
REG_BOX_RE = re.compile(r'^r(\d+) = BoxInt64Instr\(r(\d+)\)$')
REG_CALL_RE = re.compile(r'^r(\d+) = ([A-Za-z_$][\w$.<>]*)\(\)$')
REG_ANY_RE = re.compile(r'^r(\d+) = ')
GDT_RE = re.compile(r'^r\d+ = GDT\[cid_x0 \+ (0x[0-9a-f]+)\]\(\)$')
REGN = r'(?:x(\d+)|(lr))'
MOV_RE = re.compile(r'^mov\s+x(\d+), x(\d+)$')
LSL_RE = re.compile(r'^lsl\s+x(\d+), x(\d+), #1$')
DEFOP_RE = re.compile(r'^([a-z]+(?:\.[a-z]+)?)\s+[xw](\d+),')
NODEF_OPS = frozenset(('str', 'stur', 'strb', 'sturb', 'strh', 'stp', 'cmp', 'cmn',
                       'tst', 'cbz', 'cbnz', 'tbz', 'tbnz', 'b', 'bl', 'blr', 'ret'))
LDFP_RE = re.compile(r'^ldu?r\s+(?:x|r)?(\d+|lr), \[fp, #(-?)(0x[0-9a-f]+|\d+)\]$')
STFP_RE = re.compile(r'^stu?r\s+(?:x)?(\d+|lr), \[fp, #(-?)(0x[0-9a-f]+|\d+)\]$')
LDOTHER_RE = re.compile(r'^ld[a-z]*\s+[xw](\d+), \[')
SETUP_RE = re.compile(r'r(\d+) => r(\d+), fp-(0x[0-9a-f]+)')
STOREFIELD_RE = re.compile(r'^StoreField: r(\d+)->field_([0-9a-f]+) = r(\d+)')
ARRAYSTORE_RE = re.compile(r'^ArrayStore: r(\d+)\[(\d+)\] = r(\d+)')
LOADFIELD_RE = re.compile(r'^(?:LoadField|ArrayLoad): r(\d+) = ')
STORE_RAW_RE = re.compile(r'^(?:stur|str)\s+([wx])(\d+), \[x(\d+), #(0x[0-9a-f]+)\]$')
STORE_ADD_RAW_RE = re.compile(r'^add\s+x25, x(\d+), #(0x[0-9a-f]+)$')
STORE_X25_RE = re.compile(r'^str\s+([wx])(\d+), \[x25\]$')
SP_SPILL_RE = re.compile(r'^(?:stp\s+(x\d+|lr), (x\d+|lr)|str\s+(x\d+|lr)), \[SP(?:, #0x[0-9a-f]+)?\]!?$')
CMPNULL_RE = re.compile(r'^cmp\s+[wx]\d+, NULL$')
BRANCH_RE = re.compile(r'^b\.(?:eq|ne)\s+#(0x[0-9a-f]+)$')
CALLS_LIST_RE = re.compile(r'List|GrowableArray|_literal|_withData')
CALLS_MAP_RE = re.compile(r'Map\.|_Map|LinkedHashMap')

KINDS = ('const_smi', 'const_int64', 'const_string', 'const_bool', 'param',
         'field', 'list', 'map', 'unknown')


class V:
    """A tracked value: kind in str/imm/bool/null/box/arr/map/param/field/call/unk."""
    __slots__ = ('kind', 'data', 'addr', 'text')

    def __init__(self, kind, data=None, addr=None, text=''):
        self.kind, self.data, self.addr, self.text = kind, data, addr, text


def _hex(s):
    return int(s, 0)


def _reg(tok):
    tok = tok.lstrip('xr') if tok != 'lr' else tok
    return 30 if tok == 'lr' else int(tok)


def analyse_function(fn):
    """Return {'maps': [...], 'method': .., 'method_addr': .., 'cmp_null': [...]}.

    maps: [{'addr': literal call addr, 'slots': {idx: (V, store_addr, width, raw)},
            'len': elements, 'nested': bool}]
    """
    regs = {}
    slots = {}
    arrays = []
    spill = []             # registers stored to [SP...] since the last call
    method = None
    method_addr = None
    cmp_null = []          # (cmp_addr, branch_target)
    pending_cmp = None
    last_len = None
    body_calls = []
    calls = {}
    map_lits = 0
    for ins in fn.instrs:
        text = ins.text
        raws = ins.raw
        for r in raws:
            m = POOL_RE.search(r)
            if m and m.group(1) in METHOD_POOL and method is None:
                method, method_addr = METHOD_POOL[m.group(1)], ins.addr
        if pending_cmp is not None:
            m = BRANCH_RE.match(text)
            if m:
                cmp_null.append((pending_cmp, m.group(1)))
            pending_cmp = None
        if CMPNULL_RE.match(text):
            pending_cmp = ins.addr
        if text.startswith('SetupParameters('):
            for m in SETUP_RE.finditer(text):
                regs[int(m.group(2))] = V('param', 'fp-' + m.group(3), ins.addr, text)
                slots[-_hex(m.group(3))] = V('param', 'fp-' + m.group(3), ins.addr, text)
            continue
        m = STOREFIELD_RE.match(text) or ARRAYSTORE_RE.match(text)
        if m:
            base = regs.get(int(m.group(1)))
            val = regs.get(int(m.group(3)), V('unk', None, ins.addr, text))
            if base is not None and base.kind in ('arr', 'map'):
                off = None
                width = None
                rawtxt = None
                pend_add = None
                for r in raws:
                    mm = STORE_RAW_RE.match(r)
                    if mm and int(mm.group(3)) == int(m.group(1)):
                        width, off, rawtxt = mm.group(1), _hex(mm.group(4)), r
                        break
                    mm = STORE_ADD_RAW_RE.match(r)
                    if mm:
                        pend_add = _hex(mm.group(2))
                        continue
                    mm = STORE_X25_RE.match(r)
                    if mm and pend_add is not None:
                        width, off, rawtxt = mm.group(1), pend_add, r
                        break
                if off is None and text.startswith('StoreField'):
                    off = _hex(m.group(2))
                    width, rawtxt = '?', text
                if off is not None and off >= 0xf and (off - 0xf) % 4 == 0:
                    arr = arrays[base.data]
                    idx = (off - 0xf) // 4
                    arr['slots'][idx] = (val, ins.addr, width, rawtxt)
                    if val.kind in ('arr', 'map'):
                        arrays[val.data]['nested'] = True
            continue
        m = REG_BOX_RE.match(text)
        if m:
            src = regs.get(int(m.group(2)))
            if src is not None and src.kind == 'imm':
                regs[int(m.group(1))] = V('box', src.data, ins.addr, src.text)
            elif src is not None:
                regs[int(m.group(1))] = src
            else:
                regs[int(m.group(1))] = V('unk', None, ins.addr, text)
            continue
        m = REG_STR_RE.match(text)
        if m:
            regs[int(m.group(1))] = V('str', m.group(2), ins.addr, text)
            continue
        m = REG_BOOL_RE.match(text)
        if m:
            regs[int(m.group(1))] = V('bool', m.group(2) == 'true', ins.addr, text)
            continue
        m = REG_NULL_RE.match(text)
        if m:
            regs[int(m.group(1))] = V('null', None, ins.addr, text)
            continue
        m = REG_INT_RE.match(text)
        if m:
            regs[int(m.group(1))] = V('imm', int(m.group(2)), ins.addr, text)
            if int(m.group(1)) == 2:
                last_len = int(m.group(2))
            continue
        m = GDT_RE.match(text)
        if m:
            # candidate `map[key] = value`: receiver r1 is a tracked map, key r2 a
            # string literal, value r3 (the selector is not named by Blutter)
            rcv, key, val = regs.get(1), regs.get(2), regs.get(3)
            if rcv is not None and rcv.kind == 'map' and key is not None \
                    and key.kind == 'str' and val is not None:
                arrays[rcv.data].setdefault('extra', []).append(
                    (key, val, ins.addr, 'GDT[cid_x0 + %s]' % m.group(1)))
                if val.kind in ('arr', 'map'):
                    arrays[val.data]['nested'] = True
            regs = {0: V('unk', None, ins.addr, text)}
            spill = []
            continue
        m = REG_CALL_RE.match(text)
        if m:
            name = m.group(2)
            dst = int(m.group(1))
            if name in ('toJson', 'toMap', 'jsonEncode') and name not in body_calls:
                body_calls.append(name)
            if name == 'AllocateArray':
                arrays.append({'slots': {}, 'len': (last_len // 2) if last_len else None,
                               'nested': False, 'kind': None, 'addr': ins.addr})
                res = V('arr', len(arrays) - 1, ins.addr, text)
            elif name == 'Map._fromLiteral':
                map_lits += 1
                cands = [regs[r] for r in spill if r in regs and regs[r].kind == 'arr'
                         and arrays[regs[r].data]['kind'] is None]
                if cands:
                    arrays[cands[-1].data]['kind'] = 'map'
                    arrays[cands[-1].data]['lit_addr'] = ins.addr
                    res = V('map', cands[-1].data, ins.addr, text)
                else:
                    res = V('call', ('map', name), ins.addr, text)
            elif CALLS_MAP_RE.search(name):
                res = V('call', ('map', name), ins.addr, text)
            elif CALLS_LIST_RE.search(name):
                res = V('call', ('list', name), ins.addr, text)
            else:
                res = V('call', (None, name), ins.addr, text)
            calls.setdefault(name, ins.addr)
            # Dart keeps no value in a register across a call: only the result lives on
            regs = {dst: res}
            spill = []
            last_len = None
            continue
        m = MOV_RE.match(text)
        if m:
            regs[int(m.group(1))] = regs.get(int(m.group(2)),
                                             V('unk', None, ins.addr, text))
            continue
        m = LSL_RE.match(text)
        if m:
            # Smi tag of an unboxed value: the stored value is the source's value
            src = regs.get(int(m.group(2)))
            if src is not None and src.kind == 'imm':
                src = V('imm', src.data * 2, src.addr, src.text)
            regs[int(m.group(1))] = src if src is not None else \
                V('unk', None, ins.addr, text)
            continue
        m = LDFP_RE.match(text)
        if m:
            off = _hex(m.group(3)) * (-1 if m.group(2) else 1)
            if off > 0:
                v = V('param', 'fp+0x%x' % off, ins.addr, text)
            else:
                v = slots.get(off) or V('unk', None, ins.addr, text)
            regs[_reg(m.group(1))] = v
            continue
        m = STFP_RE.match(text)
        if m:
            off = _hex(m.group(3)) * (-1 if m.group(2) else 1)
            if off < 0 and _reg(m.group(1)) in regs:
                slots[off] = regs[_reg(m.group(1))]
            continue
        m = LOADFIELD_RE.match(text)
        if m:
            regs[int(m.group(1))] = V('field', text, ins.addr, text)
            continue
        m = REG_ANY_RE.match(text)
        if m:
            regs[int(m.group(1))] = V('unk', None, ins.addr, text)
            continue
        mm = None
        for r in [text] + raws:
            mm = SP_SPILL_RE.match(r)
            if mm:
                for g in mm.groups():
                    if g:
                        spill.append(_reg(g))
                break
        if mm:
            continue
        m = DEFOP_RE.match(text)
        if m and m.group(1) not in NODEF_OPS and not m.group(1).startswith('b.'):
            regs[int(m.group(2))] = V('unk', None, ins.addr, text)
            continue
        m = LDOTHER_RE.match(text)
        if m:
            regs[int(m.group(1))] = V('unk', None, ins.addr, text)
    return {'map_lits': map_lits, 'calls': calls, 'body_calls': body_calls, 'maps': arrays, 'method': method, 'method_addr': method_addr,
            'cmp_null': cmp_null}


def classify(val, width, rawtxt):
    """(value_kind, raw, value, width) for a tracked value stored in a map slot."""
    k = val.kind
    w = width if width in ('w', 'x') else None
    if k == 'imm':
        if w == 'w':
            if val.data % 2:
                return 'unknown', val.data, None, 'w'
            return 'const_smi', val.data, val.data // 2, 'w'
        if w == 'x':
            return 'const_int64', val.data, val.data, 'x'
        return 'unknown', val.data, None, w
    if k == 'box':
        return 'const_int64', val.data, val.data, 'x'
    if k == 'str':
        return 'const_string', val.data, val.data, None
    if k == 'bool':
        return 'const_bool', 'true' if val.data else 'false', val.data, None
    if k == 'param':
        return 'param', val.data, None, None
    if k == 'field':
        return 'field', val.text, None, None
    if k == 'map':
        return 'map', None, None, None
    if k == 'arr':
        return 'list', None, None, None
    if k == 'call':
        if val.data[0] in ('map', 'list'):
            return val.data[0], val.data[1], None, None
        return 'unknown', val.data[1], None, None
    if k == 'null':
        return 'unknown', 'null', None, None
    return 'unknown', val.text or None, None, None


def caller_body_fields(entry, callee_name):
    """Fields of the map literal built right before the first call to `callee_name`."""
    info = entry['info']
    call = info['calls'].get(callee_name)
    if call is None:
        return []
    before = [a for a in info['maps'] if a['kind'] == 'map' and not a['nested']
              and _hex(a['lit_addr']) < _hex(call)]
    if not before:
        return []
    last = max(before, key=lambda a: _hex(a['lit_addr']))
    out = fields_of(info, only=last)
    for f in out:
        f['source'] = 'caller'
        f['caller'] = entry['full'] + ' @' + entry['addr']
        f['call_addr'] = call
    return out


def fields_of(info, only=None):
    """Flat field list over the top-level map literals of one analysed function."""
    out = []
    maps = [a for a in info['maps'] if a['kind'] == 'map' and not a['nested']]
    if only is not None:
        maps = [only]
    for mi, arr in enumerate(maps):
        for idx in sorted(arr['slots']):
            if idx % 2:
                continue
            kval = arr['slots'][idx][0]
            if kval.kind != 'str':
                continue
            vslot = arr['slots'].get(idx + 1)
            if vslot is None:
                continue
            val, vaddr, width, rawtxt = vslot
            kind, raw, value, w = classify(val, width, rawtxt)
            f = {'key': kval.data, 'value_kind': kind, 'raw': raw, 'value': value,
                 'width': w, 'addr': kval.addr,
                 'evidence': '%s @%s' % (' '.join((rawtxt or '?').split()), vaddr)}
            if val.kind in ('map', 'arr'):
                sub = arrays_keys(info, val.data)
                if sub:
                    f['children'] = sub
            guard = None
            for caddr, target in info['cmp_null']:
                if _hex(caddr) < _hex(kval.addr) < _hex(target) \
                        and _hex(target) <= _hex(arr.get('lit_addr', '0x0')):
                    guard = caddr
                    break
            f['required'] = guard is None
            if guard:
                f['guard_addr'] = guard
            if len(maps) > 1:
                f['map'] = mi
            out.append(f)
        for key, val, caddr, sel in arr.get('extra', []):
            kind, raw, value, w = classify(val, None, None)
            f = {'key': key.data, 'value_kind': kind, 'raw': raw, 'value': value,
                 'width': w, 'addr': key.addr,
                 'evidence': '%s @%s (key stored by a call, selector not named)'
                             % (sel, caddr), 'via': 'call'}
            if val.kind in ('map', 'arr'):
                sub = arrays_keys(info, val.data)
                if sub:
                    f['children'] = sub
            guard = None
            for cmpaddr, target in info['cmp_null']:
                if _hex(cmpaddr) < _hex(key.addr) < _hex(target) <= _hex(caddr) + 4 \
                        or _hex(cmpaddr) < _hex(key.addr) < _hex(caddr) < _hex(target):
                    guard = cmpaddr
                    break
            f['required'] = guard is None
            if guard:
                f['guard_addr'] = guard
            if len(maps) > 1:
                f['map'] = mi
            out.append(f)
    return out


def arrays_keys(info, aid):
    arr = info['maps'][aid]
    return [arr['slots'][i][0].data for i in sorted(arr['slots'])
            if i % 2 == 0 and arr['slots'][i][0].kind == 'str']


def fromjson_classes(fn):
    out = []
    for ins in fn.instrs:
        m = FROMJSON_RE.match(ins.text)
        if m and m.group(1) not in out:
            out.append(m.group(1))
    return out


def scan_file(path, rel, want_addrs, want_callers):
    """One pass over one asm file.

    want_addrs: set of builder addresses; want_callers: set of function-name
    strings.  Returns (builders, callers): builders[addr] = analysis + 'fromjson'
    (own + closures); callers[name] = ordered classes (own + closures).
    """
    builders = {}
    callers = {}
    parents = None
    closure_cls = {}      # parent 'Class::func' -> classes
    with open(path, encoding='utf-8', errors='replace') as fh:
        parents = A.closure_parents(fh.read())
    for fn in A.iter_functions(path, rel):
        full = '%s::%s' % (fn.cls, fn.name)
        if fn.name == '<anonymous closure>':
            par = parents.get(fn.addr)
            if par:
                for c in fromjson_classes(fn):
                    lst = closure_cls.setdefault(par, [])
                    if c not in lst:
                        lst.append(c)
        if fn.addr in want_addrs:
            info = analyse_function(fn)
            info['fromjson'] = fromjson_classes(fn)
            info['full'] = full
            builders[fn.addr] = info
        if fn.name in want_callers:
            info = analyse_function(fn)
            callers.setdefault(fn.name, []).append(
                {'own': fromjson_classes(fn), 'full': full, 'addr': fn.addr, 'info': info})
    for info in builders.values():
        info['closure_fromjson'] = closure_cls.get(info['full'], [])
    for lst in callers.values():
        for c in lst:
            c['closure'] = closure_cls.get(c['full'], [])
    return builders, callers


def caller_name(entry):
    """'file.dart::name' -> (file, name); closures 'name' may carry an 'in' prefix."""
    f, _, n = entry.rpartition('::')
    if n.startswith('<anonymous closure> in '):
        n = n.split(' in ', 1)[1].split('::')[-1]
    return f, n


def models_index(models):
    idx = {}
    for row in models['rows']:
        idx.setdefault(row['class'], []).append(row)
    return idx


def resolve_model(cls, idx, here_dir):
    """(response_key, candidates) for a class name."""
    rows = idx.get(cls, [])
    if not rows:
        return None, []
    if len(rows) == 1:
        return rows[0]['key'], []
    same = [r for r in rows if os.path.dirname(r['dart_file']) == here_dir]
    if len(same) == 1:
        return same[0]['key'], []
    return None, sorted(r['key'] for r in rows)


def run(asm_root, endpoints, models, service=None, log=None):
    rows = [r for r in endpoints['rows']
            if service is None or r['url'].split('/')[1] == service]
    midx = models_index(models)
    want_b = {}      # file -> set(addr)
    want_c = {}      # file -> set(name)
    for r in rows:
        want_b.setdefault(r['dart_file'], set()).add(r['addr'])
        for c in r.get('callers') or []:
            f, n = caller_name(c)
            want_c.setdefault(f, set()).add(n)
    results_b = {}
    results_c = {}
    files = sorted(set(want_b) | set(want_c))
    for i, rel in enumerate(files):
        path = os.path.join(asm_root, rel)
        if not os.path.isfile(path):
            continue
        b, c = scan_file(path, rel, want_b.get(rel, set()), want_c.get(rel, set()))
        for a, info in b.items():
            results_b[(rel, a)] = info
        for n, info in c.items():
            results_c[(rel, n)] = info
        if log and i % 50 == 0:
            log('%d/%d files' % (i, len(files)))
    out = []
    for r in rows:
        info = results_b.get((r['dart_file'], r['addr']))
        rec = {'url': r['url'], 'service': r.get('service'),
               'builder': '%s::%s @%s' % (r['class'], r['function'], r['addr']),
               'dart_file': r['dart_file'],
               'sender': r.get('sender') or ('self' if r.get('role') == 'sender'
                                              else None),
               'method': None, 'method_addr': None, 'fields': [],
               'response_class': None, 'response_key': None,
               'response_candidates': [], 'response_source': None}
        if info is None:
            rec['note'] = 'builder function not found in asm'
            out.append(rec)
            continue
        rec['method'], rec['method_addr'] = info['method'], info['method_addr']
        rec['fields'] = fields_of(info)
        if not rec['fields']:
            for c in r.get('callers') or []:
                f, n = caller_name(c)
                for ent in results_c.get((f, n)) or []:
                    rec['fields'] = caller_body_fields(ent, r['function'])
                    if rec['fields']:
                        break
                if rec['fields']:
                    break
        if not rec['fields']:
            if info['map_lits']:
                rec['note'] = ('the builder only has empty or non-string-keyed map '
                               'literal(s); no body map in its direct callers')
            else:
                rec['note'] = ('no map literal in the builder and none before the call '
                               'in its direct callers')
            if info['body_calls']:
                rec['note'] += '; calls ' + ', '.join(info['body_calls'])
        own = list(info['fromjson'])
        for c in info['closure_fromjson']:
            if c not in own:
                own.append(c)
        here = os.path.dirname(r['dart_file'])
        cls = None
        if own:
            cls, src = own[0], 'builder'
            rec['response_classes'] = own
        else:
            cc = []
            for c in r.get('callers') or []:
                f, n = caller_name(c)
                for ent in results_c.get((f, n)) or []:
                    for k in ent['own'] + ent['closure']:
                        if k not in [x[0] for x in cc]:
                            cc.append((k, f))
            if len(cc) == 1:
                cls, src = cc[0][0], 'caller'
                here = os.path.dirname(cc[0][1])
            elif cc:
                rec['response_classes'] = [x[0] for x in cc]
                rec['response_source'] = 'caller-ambiguous'
        if cls:
            rec['response_class'] = cls
            rec['response_source'] = src
            rec['response_key'], rec['response_candidates'] = \
                resolve_model(cls, midx, here)
        out.append(rec)
    return out


def stats(recs):
    urls = {}
    for r in recs:
        urls.setdefault(r['url'], False)
        if any(f['value_kind'] != 'unknown' for f in r['fields']):
            urls[r['url']] = True
    hist = {}
    for r in recs:
        for f in r['fields']:
            hist[f['value_kind']] = hist.get(f['value_kind'], 0) + 1
    return {'rows': len(recs), 'urls': len(urls),
            'urls_with_classified_field': sum(urls.values()),
            'fields': sum(hist.values()), 'kinds': hist,
            'rows_with_response_class': sum(1 for r in recs if r['response_class']),
            'rows_with_response_key': sum(1 for r in recs if r['response_key'])}


def find_unknown_model_keys(recs, model_keys):
    return sorted({r['response_key'] for r in recs
                   if r.get('response_key') and r['response_key'] not in model_keys})


def check_file(path, models):
    with open(path, encoding='utf-8') as fh:
        recs = json.load(fh)['rows']
    bad = find_unknown_model_keys(recs, {r['key'] for r in models['rows']})
    for k in bad:
        print('unknown response_key: %s' % k)
    return 1 if bad else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('asm_root', nargs='?')
    ap.add_argument('--endpoints', default='data/endpoints.json')
    ap.add_argument('--models', default='data/models.json')
    ap.add_argument('--service')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--out')
    ap.add_argument('--check', action='store_true',
                    help='after an extraction (asm_root + --service/--all) or, alone, on an '
                         'existing --out: exit 1 when a response_key is not in models.json')
    a = ap.parse_args(argv)
    with open(a.models, encoding='utf-8') as fh:
        models = json.load(fh)
    extract = bool(a.asm_root and (a.service or a.all))
    if a.check and not extract:
        if not a.out:
            ap.error('--check needs --out (or an asm_root with --service/--all)')
        if not os.path.isfile(a.out):
            print('%s not found: run the extraction first' % a.out, file=sys.stderr)
            return 2
        return check_file(a.out, models)
    if not extract:
        ap.error('asm_root and --service or --all required')
    with open(a.endpoints, encoding='utf-8') as fh:
        endpoints = json.load(fh)
    recs = run(a.asm_root, endpoints, models, None if a.all else a.service,
               log=lambda s: print(s, file=sys.stderr))
    out = a.out or 'tools/out/request_fields_%s.json' % (a.service or 'all')
    A.write_json(out, 'tools/request_fields.py', endpoints.get('app_version'),
                 endpoints.get('snapshot'), recs)
    st = stats(recs)
    print(json.dumps(st, sort_keys=True))
    return check_file(out, models) if a.check else 0


if __name__ == '__main__':
    sys.exit(main())
