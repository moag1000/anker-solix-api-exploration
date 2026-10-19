"""Smi rule decoder (METHODOLOGY.md, "Smi rule").

Usage: python3 -I tools/smi.py <asm_file> <addr> [--dump]

Finds the instruction at <addr> (e.g. 0x43558c4), reads the raw immediate of
`mov xN, #imm` and the first following store of that register:
  stur/str wN (32-bit, tagged Smi)  -> value = imm / 2
  stur/str xN (64-bit, unboxed)     -> value = imm
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

MOV_RE = re.compile(r'^mov\s+[xw](\d+),\s+#(0x[0-9a-f]+|\d+)\b')
STORE_RE = re.compile(r'^(stur|str|stp)\s+([wx])(\d+)(?:,\s+([wx])(\d+))?,')
DECODED_RE = re.compile(r'^\s+// (0x[0-9a-f]+): ')
RAW_RE = re.compile(r'^\s+//\s{5}(0x[0-9a-f]+): (.*?)\s*$')


def decode_following(reg, imm, raw_lines):
    """Apply the Smi rule: raw_lines are the raw mnemonic lines after the mov."""
    for line in raw_lines:
        m = STORE_RE.match(line)
        if not m:
            continue
        kind, width, r1, width2, r2 = m.groups()
        if int(r1) == reg:
            w = width
        elif r2 is not None and int(r2) == reg:
            w = width2
        else:
            continue
        if w == 'w':
            return {'store': kind, 'width': 'w',
                    'value': imm // 2, 'odd': imm % 2 == 1}
        return {'store': kind, 'width': 'x', 'value': imm, 'odd': False}
    return {'store': None, 'width': None, 'value': None, 'odd': False}


def raw_after(path, addr, count=6):
    """Return the `count` raw lines starting at the instruction at addr."""
    out = []
    found = False
    with open(path, encoding='utf-8', errors='replace') as fh:
        for line in fh:
            if not found:
                m = DECODED_RE.match(line)
                if m and m.group(1) == addr:
                    found = True
                continue
            m = RAW_RE.match(line)
            if m:
                out.append((m.group(1), m.group(2)))
                if len(out) >= count:
                    break
    if not found:
        raise KeyError('address %s not found in %s' % (addr, path))
    return out


def smi_at(path, addr):
    raws = raw_after(path, addr)
    mov = MOV_RE.match(raws[0][1]) if raws else None
    res = {'addr': addr, 'raw': None, 'store': None, 'width': None,
           'value': None, 'odd': False, 'dump': raws}
    if not mov:
        return res
    reg = int(mov.group(1))
    imm = int(mov.group(2), 0)
    res['raw'] = imm
    res.update(decode_following(reg, imm, [r for _, r in raws[1:]]))
    return res


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('asm_file')
    ap.add_argument('addr')
    ap.add_argument('--dump', action='store_true',
                    help='print the 6 raw lines after the address')
    a = ap.parse_args(argv)
    r = smi_at(a.asm_file, a.addr)
    if a.dump:
        for ad, raw in r['dump']:
            print('  %s: %s' % (ad, raw))
    if r['raw'] is None:
        print('%s: no `mov xN, #imm` at this address (not an immediate)' % a.addr)
        return 1
    if r['store'] is None:
        print('%s: %d -> no store of the register within 6 raw lines; '
              'check by eye (--dump)' % (a.addr, r['raw']))
        return 1
    note = '  (ODD raw value in a tagged slot: re-check)' if r['odd'] else ''
    print('%d → %s %s → %d%s' % (r['raw'], r['store'], r['width'],
                                         r['value'], note))
    return 0


if __name__ == '__main__':
    sys.exit(main())
