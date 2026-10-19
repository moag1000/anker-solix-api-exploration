"""Check the asm citations of documentation pages against a Blutter asm tree.

Usage: python3 -I tools/check_citations.py <asm_root> <page.md> [page.md ...]

1. Address check: every `@0xADDR` on a line is looked up in the Dart file(s)
   named earlier on the same line (else the last file named on a previous
   line); a MISSING report means the address is in none of them. A file name
   that only appears in a later sentence makes a false positive, so read each
   report before acting on it.
2. Key check: for a table row whose first cell is a backticked identifier and
   whose last cell cites an address, the decoded instruction at the first
   cited address must contain the quoted key (`"key"`).
Output: MISSING / KEY? lines and a summary line. Exit code 1 when any KEY?.
"""
import os
import re
import sys

DEC = re.compile(r'^\s+//\s+(0x[0-9a-f]+): (.*)$')
FILE = re.compile(r'[\w%][\w/%.]*\.dart')


class Tree:
    def __init__(self, root):
        self.root = root
        self.idx = {}
        for dp, _, fns in os.walk(root):
            for f in fns:
                if f.endswith('.dart'):
                    self.idx.setdefault(f, []).append(os.path.join(dp, f))
        self.cache = {}

    def resolve(self, token):
        b = os.path.basename(token.replace('%20', ' ').strip())
        if b in self.idx:
            return self.idx[b]
        hit = [k for k in self.idx if k.endswith(b)]
        return self.idx[hit[0]] if hit else []

    def addrs(self, path):
        if path not in self.cache:
            d = {}
            with open(path, encoding='utf-8', errors='replace') as fh:
                for line in fh:
                    m = DEC.match(line)
                    if m:
                        d.setdefault(m.group(1), m.group(2))
                    m = re.match(r'^\s+// \*\* addr: (0x[0-9a-f]+)', line)
                    if m:
                        d.setdefault(m.group(1), 'FUNC')
            self.cache[path] = d
        return self.cache[path]


def check_page(tree, page):
    missing, badkeys, rows = [], [], 0
    recent = []
    with open(page, encoding='utf-8') as fh:
        lines = fh.read().split('\n')
    for ln, line in enumerate(lines, 1):
        files = [f for f in (tree.resolve(m.group(0)) for m in FILE.finditer(line)) if f]
        if files:
            recent = files
        for m in re.finditer(r'@(0x[0-9a-f]+)', line):
            before = [f for f in (tree.resolve(x.group(0))
                                  for x in FILE.finditer(line[:m.start()])) if f]
            cand = {p for f in (before or recent) for p in f} | {p for f in recent for p in f}
            if not any(m.group(1) in tree.addrs(p) for p in cand):
                missing.append((page, ln, m.group(1)))
        if line.startswith('|'):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            k = re.match(r'^`([A-Za-z_]\w*)`$', cells[0]) if len(cells) >= 5 else None
            a = re.search(r'@(0x[0-9a-f]+)', cells[-1]) if k else None
            if a:
                fl = [f for f in (tree.resolve(x.group(0)) for x in FILE.finditer(cells[-1])) if f] or recent
                cand = {p for f in fl for p in f} | {p for f in recent for p in f}
                rows += 1
                if not any(a.group(1) in tree.addrs(p)
                           and '"%s"' % k.group(1) in tree.addrs(p)[a.group(1)] for p in cand):
                    badkeys.append((page, ln, k.group(1), a.group(1)))
    return missing, badkeys, rows


def main(argv=None):
    a = sys.argv[1:] if argv is None else argv
    if len(a) < 2:
        print(__doc__)
        return 2
    tree = Tree(a[0])
    tm = tb = tr = 0
    for page in a[1:]:
        m, b, r = check_page(tree, page)
        for x in m:
            print('MISSING %s line %d %s' % x)
        for x in b:
            print('KEY? %s line %d %s %s' % x)
        tm, tb, tr = tm + len(m), tb + len(b), tr + r
    print('pages %d, missing %d, key rows %d, bad keys %d' % (len(a) - 1, tm, tr, tb))
    return 1 if tb else 0


if __name__ == '__main__':
    sys.exit(main())
