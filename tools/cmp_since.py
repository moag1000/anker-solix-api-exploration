"""Compare the literals of the same Dart functions in two Blutter asm trees.

Usage: python3 -I tools/cmp_since.py <old_asm_root> <new_asm_root> <relpath.dart> [function ...]

For every function (all functions of the file when none is named) the ordered
sequence of decoded literals (strings, integers, `<type>` arguments of
`rN = ...` instructions) is compared. Output per function: `same`, `DIFF`,
`new` (only in the new tree) or `absent` (only in the old tree); with named
functions a DIFF also prints both sequences.

Limit: only literals are compared. A changed branch condition, a changed call
target or a reordered argument that keeps the literal sequence is NOT seen, so
`same` means "no literal difference found", not "unchanged".
"""
import re
import sys

HDR = re.compile(r'^  \S.*\{$')
NAME = re.compile(r'(\S+?)\(')
LIT = re.compile(r'^\s+// 0x[0-9a-f]+: r\d+ = ("[^"]*"|<[^>]*>|-?\d+)\s*$')


def literals(path):
    """Return {function name: [literals]} for one asm file (None if missing)."""
    try:
        fh = open(path, encoding='utf-8', errors='replace')
    except OSError:
        return None
    out, cur = {}, None
    with fh:
        for line in fh:
            line = line.rstrip('\n')
            if HDR.match(line):
                m = NAME.search(line)
                cur = m.group(1) if m else line.strip()
                out.setdefault(cur, [])
                continue
            if cur is None:
                continue
            m = LIT.match(line)
            if m:
                out[cur].append(m.group(1))
    return out


def compare(old_path, new_path, names=None):
    old, new = literals(old_path), literals(new_path)
    if old is None or new is None:
        raise FileNotFoundError('missing asm file: %s' % (old_path if old is None else new_path))
    res = {}
    for n in (names or sorted(new)):
        if n not in new:
            res[n] = ('absent' if n in old else 'unknown', None, None)
        elif n not in old:
            res[n] = ('new', None, new[n])
        else:
            res[n] = ('same' if old[n] == new[n] else 'DIFF', old[n], new[n])
    return res


def main(argv=None):
    a = sys.argv[1:] if argv is None else argv
    if len(a) < 3:
        print(__doc__)
        return 2
    old_root, new_root, rel = a[:3]
    res = compare(old_root.rstrip('/') + '/' + rel, new_root.rstrip('/') + '/' + rel, a[3:])
    for n, (st, o, nw) in res.items():
        print(n, st)
        if st == 'DIFF' and a[3:]:
            print('  old:', o)
            print('  new:', nw)
    return 0


if __name__ == '__main__':
    sys.exit(main())
