"""Streaming parser for Blutter asm text (read-only, standard library only).

One asm file is plain text.  This module yields functions with their decoded
instruction comments (`// 0xADDR: text`) and the raw lines belonging to each
instruction (`//     0xADDR: mnemonic operands ; comment`).
"""
import os
import re

CLASS_RE = re.compile(r'^(?:abstract )?class ([^\s<{]+)')
ADDR_LINE_RE = re.compile(r'^\s+// \*\* addr: (0x[0-9a-f]+)')
DECODED_RE = re.compile(r'^    // (0x[0-9a-f]+): (.*?)\s*$')
RAW_RE = re.compile(r'^    //     (0x[0-9a-f]+): (.*?)\s*$')
CALLEE_RE = re.compile(r'\bbl\s+#0x[0-9a-f]+\s+; \[([^\]]*)\] (\S+)')
CLOSURE_REF_RE = re.compile(
    r'AnonymousClosure: \((0x[0-9a-f]+)\), in \[[^\]]*\] (\S+) \(0x[0-9a-f]+\)')
URL_LIT_RE = re.compile(r'^(r\d+) = "(/[^"]*)"$')
# URL literals without the leading slash ("devicecontrol/v1/app/..."): accepted only
# when the first segment is a known service prefix or the string starts with
# "<name>/v<N>/".  Dart package paths ("charging_platform/...") stay out.
SERVICE_PREFIXES = (
    'power_service', 'charging_hes_svc', 'charging_hes_installer_svc',
    'charging_hes_third_party_service_svc', 'charging_energy_service',
    'charging_hes_dynamic_price_svc', 'charging_pv_svc', 'charging_imsg_svc',
    'charging_common_svc', 'charging_disaster_prepared', 'devicecontrol',
    'generator', 'smart_service', 'device_svc', 'energy', 'site', 'marketing',
    'ems', 'privacy_service', 'mini_power', 'app', 'passport', 'openapi', 'v2')
URL_NOSLASH_RE = re.compile(
    r'^(r\d+) = "((?:(?:%s)/|[a-z_]+/v[0-9]+/)[^"]*)"$' % '|'.join(SERVICE_PREFIXES))
URL_PRECHECK_RE = re.compile(
    r'= "(?:/|(?:%s)/|[a-z_]+/v[0-9]+/)' % '|'.join(SERVICE_PREFIXES))


def url_literal(text):
    """Return (register, url) for a URL literal instruction text, else None.

    The url is stored with a leading slash whether or not the literal had one.
    """
    m = URL_LIT_RE.match(text)
    if m:
        return m.group(1), m.group(2)
    m = URL_NOSLASH_RE.match(text)
    if m:
        return m.group(1), '/' + m.group(2)
    return None


class Instr:
    __slots__ = ('addr', 'text', 'raw')

    def __init__(self, addr, text):
        self.addr = addr
        self.text = text
        self.raw = []


class Func:
    __slots__ = ('cls', 'name', 'header', 'addr', 'instrs', 'file')

    def __init__(self, cls, header, file):
        self.cls = cls
        self.header = header
        self.file = file
        self.name = func_name(header)
        self.addr = None
        self.instrs = []

    def callees(self):
        """Yield (instr, lib, 'Class::method') for every bl with a symbol."""
        for ins in self.instrs:
            for r in ins.raw:
                m = CALLEE_RE.search(r)
                if m:
                    yield ins, m.group(1), m.group(2)


def func_name(header):
    h = header.strip()
    prefix = h[:h.index('(')] if '(' in h else h
    prefix = prefix.rstrip()
    if prefix.endswith('<anonymous closure>'):
        return '<anonymous closure>'
    name = prefix.rsplit(None, 1)[-1] if prefix else h
    return re.sub(r'<.*>$', '', name)


def is_header(line):
    return (line.startswith('  ') and not line.startswith('   ')
            and not line.startswith('  //') and not line.startswith('  }')
            and '(' in line and line.rstrip().endswith('{'))


def iter_functions(path, rel=None):
    """Yield Func objects for one asm file, streaming line by line."""
    rel = rel or os.path.basename(path)
    cls = None
    fn = None
    ins = None
    prev = ''
    with open(path, encoding='utf-8', errors='replace') as fh:
        for line in fh:
            if line[0] in 'ca' and (line.startswith('class ')
                                    or line.startswith('abstract class ')):
                m = CLASS_RE.match(line)
                cls = m.group(1) if m else None
                continue
            if fn is None:
                if is_header(line):
                    fn = Func(cls, line, rel)
                    ins = None
                elif ADDR_LINE_RE.match(line) and prev.startswith('  ') \
                        and '(' in prev:
                    # fallback anchor: `// ** addr:` follows every header
                    fn = Func(cls, prev, rel)
                    fn.addr = ADDR_LINE_RE.match(line).group(1)
                    ins = None
                prev = line
                continue
            if line.startswith('  }'):
                yield fn
                fn = None
                continue
            if not line.startswith('    //'):
                continue
            if fn.addr is None:
                m = ADDR_LINE_RE.match(line)
                if m:
                    fn.addr = m.group(1)
                    continue
            m = RAW_RE.match(line)
            if m:
                if ins is not None:
                    ins.raw.append(m.group(2))
                continue
            m = DECODED_RE.match(line)
            if m:
                ins = Instr(m.group(1), m.group(2))
                fn.instrs.append(ins)
    if fn is not None:
        yield fn


def iter_dart_files(root):
    """Yield (abs_path, rel_path) for every file in the asm tree, sorted."""
    out = []
    for dp, dn, fns in os.walk(root):
        dn.sort()
        for f in fns:
            p = os.path.join(dp, f)
            out.append((p, os.path.relpath(p, root)))
    out.sort(key=lambda x: x[1])
    return out


def file_contains(path, needles):
    """Cheap pre-check: does the file contain any of the substrings?"""
    with open(path, encoding='utf-8', errors='replace') as fh:
        text = fh.read()
    return any(n in text for n in needles), text


def closure_parents(text):
    """Map closure address -> enclosing 'Class::function' (same file)."""
    return {m.group(1): m.group(2) for m in CLOSURE_REF_RE.finditer(text)}


SNAPSHOT_3_24_3 = '78da37fed6bf1489361a312568249f3f'
DEFAULT_NEW_ROOT = os.environ.get(
    'ANKER_ASM_NEW', '/Users/michaelbanda/Nextcloud/www/untitled1/ankerAPK/'
    'v3.24.3/blutter_output/asm')
DEFAULT_OLD_ROOT = os.environ.get(
    'ANKER_ASM_OLD', '/Users/michaelbanda/Nextcloud/www/untitled1/ankerAPK/'
    'blutter_output/asm')
DEFAULT_UPSTREAM = os.environ.get(
    'ANKER_UPSTREAM', '/Users/michaelbanda/Nextcloud/www/untitled1/ankerAPK/'
    'anker-solix-api/api/apitypes.py')
ALL_CALLEE_RE = re.compile(r'\bbl\s+#0x[0-9a-f]+\s+; \[[^\]]*\] (\S+)')


def load_upstream(path):
    """Parse apitypes.py with ast (never imported or executed).

    Returns (api_endpoints {key: url-without-leading-slash},
             parm_types {value: ENUM_NAME}).
    """
    import ast
    with open(path, encoding='utf-8') as fh:
        tree = ast.parse(fh.read())
    endpoints, parm = {}, {}
    for node in tree.body:
        target = None
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            target = node.target.id
        elif (isinstance(node, ast.Assign) and len(node.targets) == 1
              and isinstance(node.targets[0], ast.Name)):
            target = node.targets[0].id
        if target == 'API_ENDPOINTS' and isinstance(node.value, ast.Dict):
            for k, v in zip(node.value.keys, node.value.values):
                if isinstance(k, ast.Constant) and isinstance(v, ast.Constant):
                    endpoints[k.value] = v.value
        if isinstance(node, ast.ClassDef) and node.name == 'SolixParmType':
            for st in node.body:
                if (isinstance(st, ast.Assign) and isinstance(st.value, ast.Constant)
                        and isinstance(st.targets[0], ast.Name)):
                    parm[str(st.value.value)] = st.targets[0].id
    return endpoints, parm


def write_json(path, generated_by, app_version, snapshot, rows):
    import json
    doc = {'generated_by': generated_by, 'app_version': app_version,
           'snapshot': snapshot, 'rows': rows}
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as fh:
        json.dump(doc, fh, indent=2, sort_keys=True, ensure_ascii=False)
        fh.write('\n')

# an instruction that clearly starts a new statement (used to bound key lookups)
ASSIGN_KEY_BREAK = re.compile(r'^r\d+ = (?:AllocateArray|Map\._fromLiteral|StackOverflow)')
