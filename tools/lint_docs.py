"""Repo-wide documentation linter and link checker.

Usage (from the repo root):
  python3 -I tools/lint_docs.py [--rule NAME[,NAME]] [--summary] [--json] [--warn-only] [--strict] [--root DIR]

Rules (each finding is printed as `path:line: ERROR|WARN rule: message`):
  header                      status header on the first non-blank line of every fact page
  sections                    H2 (endpoint/model/flow/device) or H3/H4 (mqtt/ble) order matches docs/templates
  uncited-int                 integer >= 2 in a table row without `@0xADDR`, an `objs.txt Obj!Class@id` citation or a row tag
  tag-overclaim               `asm-traced` sentence or `Tag: asm-traced` section that says presumably/likely/inferred/not traced/assumed (--strict: also warns on @0x rows under an asm-traced header)
  inferred-as-traced-sequence a `[T]` traced-step line that says the same words
  todo-purpose  (warning)     `## Purpose` is `<!-- TODO -->` (grouped per service in text output)
  links                       relative link or #anchor does not resolve
  length                      > 600 lines error; > 150 lines without a Contents heading warning
  dup-payload                 identical ```json block on more than one page
  secret                      a 32+ hex run outside docs/audit
  owner-cmd                   numeric cmd value outside api/param_types.md

Exit 1 when any error is reported. `--warn-only` runs only the warning rules and exits 0.
Old root docs listed in the migration map of docs/STRUCTURE.md that still lack a status
header (legacy, bannered later) and headerless pages under docs/archive/ are exempt from every rule except `links`. Standard library only.
"""
import argparse
import collections
import hashlib
import json
import os
import re
import sys
from urllib.parse import unquote

TAGS = ('asm-traced', 'string-only', 'upstream-confirmed', 'device-tested')
SEP = ' \u00b7 '


def valid_header(line):
    """`> Verified against: App 3.24.3 · Date: D · (Confidence: tag | Page type: x) · Owner page: p`.

    Segments after the date may come in any order (some pages add `Page type:` next to
    `Confidence:`); a tag may be followed by a parenthetical scope note."""
    seg = line.split(SEP)
    if len(seg) < 4 or seg[0] != '> Verified against: App 3.24.3':
        return False
    if not re.match(r'^Date: \d{4}-\d{2}-\d{2}$', seg[1]):
        return False
    rest = seg[2:]
    conf = [x for x in rest if x.startswith('Confidence:')]
    ptype = [x for x in rest if x.startswith('Page type:')]
    owner = [x for x in rest if x.startswith('Owner page:') and len(x) > 12]
    if not owner or not (conf or ptype) or len(conf) > 1:
        return False
    if len(rest) != len(conf) + len(ptype) + len(owner):
        return False
    return not conf or re.match(r'^Confidence: (%s)( \(.*\))?$' % '|'.join(TAGS), conf[0]) is not None


RULES = ('header', 'sections', 'uncited-int', 'tag-overclaim', 'inferred-as-traced-sequence',
         'todo-purpose', 'links', 'length', 'dup-payload', 'secret', 'owner-cmd')
SOFT = ('todo-purpose', 'length')
SKIP_DIRS = {'.git', '.superpowers', 'out', '__pycache__', 'easter_eggs', 'node_modules'}
HEADER_DIRS = ('api', 'models', 'flows', 'devices', 'mqtt', 'ble', 'reference')
# non-command pages under mqtt/ and ble/ (template does not apply)
PROTOCOL_PAGES = {'README.md', 'envelope.md', 'protocol.md', 'handshake.md'}
OVERCLAIM = re.compile(r'\b(presumably|likely|inferred|not traced|assumed)\b', re.I)
ROW_TAG = re.compile(r'upstream-confirmed|device-tested|string-only|untagged by design', re.I)
FENCE = re.compile(r'^\s*(```|~~~)')


class Finding:
    def __init__(self, rule, severity, path, line, msg, text=''):
        self.rule, self.severity, self.path, self.line = rule, severity, path, line
        self.msg, self.text = msg, text

    def as_dict(self):
        return {'rule': self.rule, 'severity': self.severity, 'path': self.path,
                'line': self.line, 'message': self.msg}


class Page:
    def __init__(self, root, rel):
        self.rel = rel
        self.legacy = False       # headerless page of the migration map: link check only
        with open(os.path.join(root, rel), encoding='utf-8') as fh:
            self.lines = fh.read().split('\n')
        self.fenced = []          # per line: True inside a fence (fence lines included)
        inside = False
        for ln in self.lines:
            f = bool(FENCE.match(ln))
            self.fenced.append(inside or f)
            if f:
                inside = not inside
        self.headings = []        # (line_no, level, text) outside fences
        for i, ln in enumerate(self.lines):
            m = re.match(r'^(#{1,6})\s+(.*?)\s*#*\s*$', ln)
            if m and not self.fenced[i]:
                self.headings.append((i + 1, len(m.group(1)), m.group(2)))

    @property
    def first(self):
        for i, ln in enumerate(self.lines):
            if ln.strip():
                return i, ln.strip()
        return 0, ''

    def has_header(self):
        return valid_header(self.first[1])

    def section(self, level, title):
        """Body lines (index, text) of the first heading `title` at `level`."""
        for k, (ln, lv, tx) in enumerate(self.headings):
            if lv == level and tx == title:
                end = len(self.lines)
                for ln2, lv2, _ in self.headings[k + 1:]:
                    if lv2 <= level:
                        end = ln2 - 1
                        break
                return [(i, self.lines[i]) for i in range(ln, end)]
        return None


def slug(text):
    t = re.sub(r'<[^>]+>', '', text).strip().lower()
    t = re.sub(r'[^\w\- ]', '', t)
    return t.replace(' ', '-')


def anchors(page):
    seen, out = collections.Counter(), set()
    for _, _, tx in page.headings:
        s = slug(tx)
        out.add(s if not seen[s] else '%s-%d' % (s, seen[s]))
        seen[s] += 1
    for ln in page.lines:
        out.update(re.findall(r'\b(?:id|name)="([^"]+)"', ln))
    return out


def legacy_paths(root):
    """Old paths of the migration map in docs/STRUCTURE.md."""
    path = os.path.join(root, 'docs', 'STRUCTURE.md')
    out = set()
    if not os.path.exists(path):
        return out
    on = False
    with open(path, encoding='utf-8') as fh:
        for ln in fh:
            if ln.startswith('## '):
                on = ln.strip() == '## Migration map'
            m = re.match(r'^\|\s*`([^`]+\.md)`\s*\|', ln)
            if on and m:
                out.add(m.group(1))
    return out


def collect(root):
    legacy = legacy_paths(root)
    pages = []
    for dp, dns, fns in os.walk(root):
        dns[:] = sorted(d for d in dns if d not in SKIP_DIRS and not d.startswith('.venv'))
        for f in sorted(fns):
            if not f.endswith('.md'):
                continue
            rel = os.path.relpath(os.path.join(dp, f), root).replace(os.sep, '/')
            pg = Page(root, rel)
            # docs/archive/ holds superseded 3.18.0 pages kept for provenance: link check only
            pg.legacy = (rel in legacy or rel.startswith('docs/archive/')) and not pg.has_header()
            pages.append(pg)
    return pages


def parse_template(root, name, level):
    """Headings of `level` before the second H1 of docs/templates/<name>.md."""
    path = os.path.join(root, 'docs', 'templates', name)
    if not os.path.exists(path):
        return None
    pg = Page(root, 'docs/templates/' + name)
    out, h1 = [], 0
    for _, lv, tx in pg.headings:
        if lv == 1:
            h1 += 1
            if h1 == 2:
                break
        elif lv == level and h1 == 1:
            out.append(tx)
    return out


def page_type(rel):
    parts = rel.split('/')
    base = parts[-1]
    if base == 'README.md':
        return None
    if parts[0] == 'api' and len(parts) >= 3:
        return 'endpoint'
    if parts[0] == 'models':
        return 'model'
    if parts[0] == 'flows':
        return 'flow'
    if parts[0] == 'devices':
        return 'device'
    if parts[0] in ('mqtt', 'ble') and base not in PROTOCOL_PAGES:
        return parts[0]
    return None


def is_fact_page(pg):
    """Header carries `Confidence:` or a `Page type:` other than guidance."""
    h = pg.first[1]
    if 'Confidence:' in h:
        return True
    m = re.search(r'Page type: ([^\u00b7]+)', h)
    return bool(m) and not m.group(1).strip().lower().startswith('guidance')


def in_header_scope(rel):
    parts = rel.split('/')
    if len(parts) == 1:
        return rel in ('METHODOLOGY.md', 'GLOSSARY.md')
    if parts[0] in HEADER_DIRS:
        return True
    return parts[0] == 'docs' and (len(parts) == 2 or parts[1] == 'audit')


# ---------------------------------------------------------------- rules

def rule_header(pg, ctx):
    if not in_header_scope(pg.rel):
        return
    i, txt = pg.first
    if not pg.has_header():
        yield i + 1, 'first non-blank line is not a valid status header (App 3.24.3, date, one of 4 tags or Page type, Owner page)', txt


def subsequence_problem(want, have):
    missing = [w for w in want if w not in have]
    if missing:
        return 'missing section(s): ' + ', '.join(missing)
    order = [h for h in have if h in want]
    if order != want:
        return 'sections out of order: found %s, expected %s' % (order, want)
    return None


def rule_sections(pg, ctx):
    pt = page_type(pg.rel)
    if not pt:
        return
    if pt in ('endpoint', 'model', 'flow', 'device'):
        want = ctx.template(pt + '.md', 2)
        if want is None:
            return
        have = [t for _, lv, t in pg.headings if lv == 2]
        if pt == 'model' and not have:
            return
        prob = subsequence_problem(want, have)
        if prob:
            yield 1, prob, ''
        return
    want = ctx.template(pt + '_command.md', 4)
    if want is None:
        return
    h3 = [(ln, k) for k, (ln, lv, _) in enumerate(pg.headings) if lv == 3]
    if not h3:
        yield 1, 'no ### command sections', ''
    for ln, k in h3:
        have = []
        for ln2, lv2, tx2 in pg.headings[k + 1:]:
            if lv2 <= 3:
                break
            if lv2 == 4:
                have.append(tx2)
        prob = subsequence_problem(want, have)
        if prob:
            yield ln, 'command "%s": %s' % (pg.headings[k][2], prob), ''


INT = re.compile(r'(?<![\w.#/@+-])\d+(?![\w])')
ROW_STRIP = [
    re.compile(r'@0x[0-9a-fA-F]+'), re.compile(r'\b0x[0-9a-fA-F]+'),
    re.compile(r'\]\([^)]*\)'), re.compile(r'https?://\S+'),
    re.compile(r'\d+(?:\.\d+)+'), re.compile(r'\b20\d\d-\d\d(?:-\d\d)?\b'),
    re.compile(r'\.dart:\d+(?::\d+)?'), re.compile(r'\b[Ll]ines? \d+(?:\s*(?:-|to|–)\s*\d+)?'),
    re.compile(r'\bL\d+\b'),
]


UNTAGGED_SECTIONS = ('Known unknowns', 'Device-tested by')   # untagged by design (templates)
COUNT_COL = re.compile(r'\b(?:counts?|rows|calls|total)\b', re.I)
ID_COL = re.compile(r'^`?param_type`?$', re.I)    # param_type ids are string literals
COUNT_NOUN = re.compile(r'\b\d+\s+(?:sends|senders|calls|call sites|functions|endpoints|pages|files|rows)\b', re.I)
STEP_REF = re.compile(r'\b[Ss]teps? \d+(?:\s*(?:-|to|and)\s*\d+)?')


def cells(row):
    return [c.strip() for c in row.strip().strip('|').split('|')]


# Object-dump citation (Blutter objs.txt): `objs.txt Obj!<Class>@<hexid>`; `@0x…` stays asm-only.
OBJ_CITE = re.compile(r'objs\.txt Obj![A-Za-z_][A-Za-z0-9_<>, ?]*@[0-9a-f]+')


def rule_uncited_int(pg, ctx):
    # Fact pages only (see is_fact_page). Audit tables cite through their raw/decoded
    # columns. Cells of a count column (never the first) and of a `param_type` id column are
    # tool-derived tallies / string literals, not decoded immediates.
    if pg.rel.startswith(('docs/audit/', 'docs/templates/')) or not is_fact_page(pg):
        return
    sec_exempt, in_table, skip_cols = False, False, set()
    heads = {ln: tx for ln, _, tx in pg.headings}
    for i, ln in enumerate(pg.lines):
        if (i + 1) in heads:
            sec_exempt = heads[i + 1] in UNTAGGED_SECTIONS
        elif re.match(r'^Tag:\s*untagged by design', ln.strip()):
            sec_exempt = True
        s = ln.strip()
        if pg.fenced[i] or not s.startswith('|'):
            in_table = False
            continue
        if not in_table:
            in_table = True
            skip_cols = {k for k, h in enumerate(cells(s))
                         if ID_COL.match(h) or (k > 0 and COUNT_COL.search(h))}
        if sec_exempt or re.match(r'^\|[\s:|-]+\|?$', s):
            continue
        if re.search(r'@0x[0-9a-fA-F]+', s) or ROW_TAG.search(s) or OBJ_CITE.search(s):
            continue
        t = ' | '.join(c for k, c in enumerate(cells(s)) if k not in skip_cols)
        for r in ROW_STRIP + [COUNT_NOUN, STEP_REF]:
            t = r.sub(' ', t)
        bad = [m.group(0) for m in INT.finditer(t) if int(m.group(0)) >= 2]
        if bad:
            yield i + 1, 'integer(s) %s in a table row without an @0x citation or a row tag' % ', '.join(bad), ln


def units(pg):
    """Paragraphs, table rows and list items as (first_line_no, text) outside fences."""
    cur, start = [], 0
    for i, ln in enumerate(pg.lines):
        s = ln.strip()
        if pg.fenced[i] or not s or s.startswith('#'):
            if cur:
                yield start + 1, ' '.join(cur)
                cur = []
            continue
        if s.startswith('|') or re.match(r'^([-*+]|\d+\.)\s', s):
            if cur:
                yield start + 1, ' '.join(cur)
                cur = []
            yield i + 1, s
            continue
        if not cur:
            start = i
        cur.append(s)
    if cur:
        yield start + 1, ' '.join(cur)


# "X is not traced" / "(..., not traced)" states a limit of the evidence; it claims nothing
SCOPE_LIMIT = re.compile(r'(?:\b(?:is|are|was|were|remains?|stays?) not traced\b|,\s*not traced\)|\(not traced\))', re.I)


def overclaim_word(text):
    m = OVERCLAIM.search(SCOPE_LIMIT.sub(' ', text))
    return m.group(0) if m else None


def rule_tag_overclaim(pg, ctx):
    """A sentence (cells of a table row are split into sentences too) that carries `asm-traced` and also hedges."""
    first = pg.first[0] + 1
    for ln, txt in units(pg):
        if ln == first or 'asm-traced' not in txt:
            continue
        pieces = [x for c in (txt.split('|') if txt.startswith('|') else [txt])
                  for x in re.split(r'(?<=[.;!?])\s+', c)]
        for sent in pieces:
            w = overclaim_word(sent) if 'asm-traced' in sent else None
            if w:
                yield ln, 'asm-traced claim says "%s": use string-only or drop the word' % w, txt[:120]
                break
    for k, (ln, lv, tx) in enumerate(pg.headings):
        body = pg.section(lv, tx) or []
        tagged = 'asm-traced' in tx or any(re.match(r'^Tag:\s*asm-traced\b', t.strip()) for _, t in body[:4])
        if not tagged:
            continue
        for i, line in body:
            w = overclaim_word(line) if not pg.fenced[i] else None
            if w:
                yield i + 1, 'section "%s" is tagged asm-traced but says "%s"' % (tx, w), line


def rule_traced_seq(pg, ctx):
    for i, ln in enumerate(pg.lines):
        if re.search(r'\[T[\] ]', ln):
            m = OVERCLAIM.search(ln)
            if m:
                yield i + 1, 'traced [T] line says "%s"' % m.group(0), ln


def rule_todo_purpose(pg, ctx):
    if page_type(pg.rel) not in ('endpoint', 'model'):
        return
    body = pg.section(2, 'Purpose')
    if body is not None and any(t.strip() == '<!-- TODO -->' for _, t in body):
        yield 1, 'Purpose is a TODO skeleton', ''


LINK = re.compile(r'!?\[[^\]]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)')


def rule_links(pg, ctx):
    base = os.path.dirname(pg.rel)
    for i, ln in enumerate(pg.lines):
        if pg.fenced[i]:
            continue
        t = re.sub(r'`[^`]*`', '', ln)
        for m in LINK.finditer(t):
            tgt = m.group(1).strip('<>')
            if re.match(r'^[a-z][a-z0-9+.-]*:', tgt, re.I) or tgt.startswith('//'):
                continue
            file_part, _, anc = tgt.partition('#')
            file_part = unquote(file_part)
            if file_part:
                full = os.path.normpath(os.path.join(ctx.root, base, file_part))
                if not os.path.exists(full):
                    yield i + 1, 'link target not found: %s' % tgt, ln
                    continue
                rel = os.path.relpath(full, ctx.root).replace(os.sep, '/')
                tp = ctx.page(rel) if full.endswith('.md') else None
            else:
                tp = pg
            if anc and tp is not None and unquote(anc).lower() not in anchors(tp):
                yield i + 1, 'anchor not found: %s' % tgt, ln


def rule_length(pg, ctx):
    n = len(pg.lines) - (1 if pg.lines and pg.lines[-1] == '' else 0)
    if n > 600 and not pg.rel.startswith('docs/audit/'):
        yield 1, '%d lines (limit 600)' % n, ''
    elif n > 600:
        yield 1, '%d lines (frozen audit table, limit not enforced)' % n, ''
    elif n > 150 and not any(re.match(r'(contents|table of contents|toc)$', t, re.I)
                             for _, _, t in pg.headings):
        yield 1, '%d lines without a Contents section' % n, ''


def norm_json(block):
    try:
        return json.dumps(json.loads(block), sort_keys=True)
    except ValueError:
        return re.sub(r'\s+', '', block)


# the generic success envelope with an empty data member is not a payload fact
ENVELOPE = re.compile(r'^\{"code": ?0, ?"data": ?(\{\}|\[\]|null), ?"msg": ?"success"\}$')


def in_section(pg, idx, title):
    """True when the line `idx` (0-based) lies under the H2 `title`."""
    h2 = [tx for ln, lv, tx in pg.headings if lv == 2 and ln <= idx + 1]
    return bool(h2) and h2[-1] == title


def rule_dup_payload(pg, ctx):
    if pg.rel.startswith(('docs/templates/', 'docs/audit/')):
        return
    i = 0
    while i < len(pg.lines):
        if re.match(r'^\s*```json\b', pg.lines[i]):
            j = i + 1
            while j < len(pg.lines) and not FENCE.match(pg.lines[j]):
                j += 1
            norm = norm_json('\n'.join(pg.lines[i + 1:j]))
            if len(norm) >= 30 and not ENVELOPE.match(norm):
                owned = page_type(pg.rel) == 'endpoint' and in_section(pg, i, 'Example request/response')
                ctx.blocks[hashlib.sha1(norm.encode()).hexdigest()].append((pg.rel, i + 1, owned))
            i = j
        i += 1
    return ()


def finish_dup(ctx):
    # Every endpoint page owns the request/response example in its own `Example
    # request/response` section, so identical shapes there (two endpoints taking
    # `{"vehicle_id": ...}`) are not copies; a copy anywhere else is.
    for locs in ctx.blocks.values():
        pages = sorted({p for p, _, _ in locs})
        if len(pages) > 1 and not all(o for _, _, o in locs):
            for p, ln, _ in locs:
                others = ', '.join(x for x in pages if x != p)
                yield p, ln, 'identical json block also on: %s (single source)' % others


def rule_secret(pg, ctx):
    if pg.rel.startswith(('docs/audit/', 'data/')):
        return
    for i, ln in enumerate(pg.lines):
        m = re.search(r'[0-9a-fA-F]{32,}', ln)
        # public build identifiers (sha256 of the XAPK, Dart snapshot hash): keyword right
        # next to the run and a 32/40/64 length
        if m and len(m.group(0)) in (32, 40, 64) and re.search(
                r'(sha256|sha1|md5|snapshot|checksum)\W{0,12}$', ln[:m.start()], re.I):
            continue
        if m:
            yield i + 1, '32+ hex run (%d chars) outside docs/audit: possible secret' % len(m.group(0)), ''


CMD = re.compile(r'"cmd"\s*:\s*\d+|\bcmd`?\s*=\s*\d+|\bcmd`?\s+\d+\b', re.I)


def rule_owner_cmd(pg, ctx):
    # Fact pages only. Exempt: the owner page; docs/audit (frozen records of the old values,
    # including wrong ones); plans and issue notes (no header); a line carrying the marker
    # `<!-- lint: owner-cmd example -->` (METHODOLOGY's worked Smi example).
    if pg.rel == 'api/param_types.md' or pg.rel.startswith('docs/audit/') or not is_fact_page(pg):
        return
    for i, ln in enumerate(pg.lines):
        m = CMD.search(ln)
        if m and 'lint: owner-cmd example' not in ln:
            yield i + 1, 'numeric cmd value "%s" belongs on api/param_types.md' % m.group(0), ln


PAGE_RULES = {
    'header': rule_header, 'sections': rule_sections, 'uncited-int': rule_uncited_int,
    'tag-overclaim': rule_tag_overclaim, 'inferred-as-traced-sequence': rule_traced_seq,
    'todo-purpose': rule_todo_purpose, 'links': rule_links, 'length': rule_length,
    'dup-payload': rule_dup_payload, 'secret': rule_secret, 'owner-cmd': rule_owner_cmd,
}


class Ctx:
    def __init__(self, root, pages):
        self.root = root
        self.pages = {p.rel: p for p in pages}
        self.blocks = collections.defaultdict(list)
        self._tpl = {}
        self._extra = {}

    def template(self, name, level):
        if (name, level) not in self._tpl:
            self._tpl[(name, level)] = parse_template(self.root, name, level)
        return self._tpl[(name, level)]

    def page(self, rel):
        if rel in self.pages:
            return self.pages[rel]
        if rel not in self._extra:
            self._extra[rel] = Page(self.root, rel)
        return self._extra[rel]


def strict_hedges(pg):
    """--strict: hedge words in table rows that cite `@0x` under an asm-traced page header."""
    if 'Confidence: asm-traced' not in pg.first[1]:
        return
    for i, ln in enumerate(pg.lines):
        s = ln.strip()
        if not pg.fenced[i] and s.startswith('|') and re.search(r'@0x[0-9a-fA-F]+', s):
            w = overclaim_word(s)
            if w:
                yield i + 1, 'row cites @0x under an asm-traced header and says "%s"' % w, ln


def lint_repo(root, rules=None, strict=False):
    rules = list(rules or RULES)
    pages = collect(root)
    ctx = Ctx(root, pages)
    out = []
    for pg in pages:
        # a headerless legacy page is exempt from every rule except the link check
        for name in rules:
            if pg.legacy and name != 'links':
                continue
            for res in PAGE_RULES[name](pg, ctx) or ():
                ln, msg, text = res
                sev = 'warning' if (name == 'todo-purpose' or (name == 'length' and '(limit 600)' not in msg)) else 'error'
                out.append(Finding(name, sev, pg.rel, ln, msg, text))
    if strict and 'tag-overclaim' in rules:
        seen = {(f.path, f.line) for f in out if f.rule == 'tag-overclaim'}
        for pg in pages:
            for ln, msg, text in strict_hedges(pg):
                if (pg.rel, ln) not in seen:
                    out.append(Finding('tag-overclaim', 'warning', pg.rel, ln, msg, text))
    if 'dup-payload' in rules:
        for p, ln, msg in finish_dup(ctx):
            out.append(Finding('dup-payload', 'error', p, ln, msg))
    out.sort(key=lambda f: (f.path, f.line, f.rule))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--rule', help='comma-separated rule names (default: all)')
    ap.add_argument('--summary', action='store_true', help='print counts per rule only')
    ap.add_argument('--json', action='store_true', help='machine output')
    ap.add_argument('--strict', action='store_true', help='also warn on hedge words in @0x rows under an asm-traced header')
    ap.add_argument('--warn-only', action='store_true', help='run only the warning rules, exit 0')
    ap.add_argument('--root', default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    a = ap.parse_args(argv)
    rules = a.rule.split(',') if a.rule else list(RULES)
    bad = [r for r in rules if r not in RULES]
    if bad:
        print('unknown rule(s): %s (known: %s)' % (', '.join(bad), ', '.join(RULES)), file=sys.stderr)
        return 2
    if a.warn_only:
        rules = [r for r in rules if r in SOFT]
    found = lint_repo(a.root, rules, strict=a.strict)
    if a.warn_only:
        found = [f for f in found if f.severity == 'warning']
    errors = [f for f in found if f.severity == 'error']
    if a.json:
        print(json.dumps([f.as_dict() for f in found], indent=1))
    elif a.summary:
        for r in rules:
            e = sum(1 for f in found if f.rule == r and f.severity == 'error')
            w = sum(1 for f in found if f.rule == r and f.severity == 'warning')
            print('%-30s errors %4d  warnings %4d' % (r, e, w))
        print('%-30s errors %4d  warnings %4d' % ('TOTAL', len(errors), len(found) - len(errors)))
    else:
        todo = collections.Counter()
        for f in found:
            if f.rule == 'todo-purpose':
                parts = f.path.split('/')
                todo[parts[1] if parts[0] == 'api' else parts[0]] += 1
                continue
            print('%s:%d: %s %s: %s' % (f.path, f.line, 'ERROR' if f.severity == 'error' else 'WARN', f.rule, f.msg))
        for svc, n in sorted(todo.items()):
            print('WARN todo-purpose: %s: %d skeleton Purpose section(s)' % (svc, n))
        print('%d error(s), %d warning(s)' % (len(errors), len(found) - len(errors)))
    return 0 if a.warn_only else (1 if errors else 0)


if __name__ == '__main__':
    sys.exit(main())
