"""Validate the four machine-readable exports in data/ against small inline schemas.

Usage (repo root):
  python3 -I tools/schema_check.py [--repo .] [--check]

Checks data/endpoints.json, data/models.json, data/param_types.json and
data/errors.json: the envelope (`generated_by`, `app_version`, `snapshot`, `rows`),
the field names and types of every row (and of the nested model fields), fields
that no schema knows (so a new key cannot ship undocumented), duplicate model
keys, and that all four files carry the same `app_version` and `snapshot`.
Prints one line per violation.  Exit code is 0 unless --check is given and a
violation was found.  The tool never writes anything.  Standard library only.

The schemas below are the contract documented in data/README.md; change both
together.  A type is one of: str, int, bool, list, dict, none (JSON null);
a tuple means "any of".  `list:str` is a list whose items are all strings.
"""
import argparse
import json
import os
import sys

STR, INT, BOOL, LIST, DICT, NONE = 'str', 'int', 'bool', 'list', 'dict', 'none'
LIST_STR = 'list:str'

ENVELOPE = {'generated_by': STR, 'app_version': STR, 'snapshot': STR, 'rows': LIST}

ENDPOINT_REQUIRED = {
    'addr': STR, 'callers': LIST_STR, 'class': STR, 'cmd': (INT, NONE),
    'cmd_addr': (STR, NONE), 'cmd_note': (STR, NONE), 'cmd_raw': (INT, NONE),
    'dart_file': STR, 'encrypted': BOOL, 'encryption_note': (STR, NONE),
    'envelope': LIST_STR, 'function': STR, 'http_callees': LIST_STR,
    'param_data_is_json': BOOL, 'param_type': (STR, NONE),
    'param_type_source': (STR, NONE), 'params': LIST_STR, 'role': STR, 'service': STR,
    'since': STR, 'upstream_key': (STR, NONE), 'url': STR, 'url_addr': STR,
}
ENDPOINT_OPTIONAL = {
    'reference': STR, 'removed_in': STR, 'resolution': STR,
    'sender': STR, 'sender_file': STR, 'sender_kind': STR, 'sender_wrapper': STR,
    'sender_via': LIST_STR, 'sender_via_files': LIST_STR, 'sender_also': LIST_STR,
    'sender_via_also': LIST,
}

MODEL_FIELD = {
    'dart_type': STR, 'json_key': STR, 'key_addr': STR,
    'nullable': (BOOL, NONE), 'since': (STR, NONE),
}
MODEL_REQUIRED = {
    'key': STR, 'class': STR, 'dart_file': STR, 'fields': 'rows:model_field',
    'from_json_addr': STR, 'removed_keys': LIST_STR, 'since': STR,
}
MODEL_OPTIONAL = {'removed_in': STR}

PARAM_TYPE_REQUIRED = {
    'cmd': (INT, NONE), 'cmd_addr': (STR, NONE), 'cmd_by_function': DICT,
    'cmd_get': (INT, NONE), 'cmd_get_addr': (STR, NONE), 'cmd_get_raw': (INT, NONE),
    'cmd_raw': (INT, NONE), 'cmd_set': (INT, NONE), 'cmd_set_addr': (STR, NONE),
    'cmd_set_raw': (INT, NONE), 'dart_files': LIST_STR, 'function_sources': DICT,
    'get_function': LIST_STR, 'get_model': (STR, NONE), 'keys': LIST,
    'name': (STR, NONE), 'param_type': STR, 'param_type_source': STR,
    'set_function': LIST_STR, 'traced_from': LIST, 'unresolved': LIST,
}

# errors.json rows come from three sources; only code, kind, source and tag are common.
ERROR_REQUIRED = {'code': INT, 'kind': STR, 'source': STR, 'tag': STR}
ERROR_OPTIONAL = {
    'addr': STR, 'branch': (STR, NONE), 'file': STR, 'form': STR, 'function': STR,
    'function_addr': STR, 'odd_raw': BOOL, 'raw': INT, 'strings': LIST_STR, 'width': STR,
    'base': STR, 'class_line': INT, 'line': INT, 'message': STR, 'name': STR,
    'context': STR, 'endpoint': STR, 'reported': STR, 'reported_by': STR, 'url': STR,
}

SCHEMAS = {
    'endpoints': (ENDPOINT_REQUIRED, ENDPOINT_OPTIONAL),
    'models': (MODEL_REQUIRED, MODEL_OPTIONAL),
    'param_types': (PARAM_TYPE_REQUIRED, {}),
    'errors': (ERROR_REQUIRED, ERROR_OPTIONAL),
}
FILES = tuple(SCHEMAS)


def _is(value, t):
    if t == STR:
        return isinstance(value, str)
    if t == INT:
        return isinstance(value, int) and not isinstance(value, bool)
    if t == BOOL:
        return isinstance(value, bool)
    if t == LIST:
        return isinstance(value, list)
    if t == DICT:
        return isinstance(value, dict)
    if t == NONE:
        return value is None
    if t == LIST_STR:
        return isinstance(value, list) and all(isinstance(i, str) for i in value)
    raise ValueError('unknown type %r' % (t,))


def _type_ok(value, spec):
    if spec == 'rows:model_field':
        return isinstance(value, list)
    return any(_is(value, t) for t in (spec if isinstance(spec, tuple) else (spec,)))


def _name(spec):
    return '|'.join(spec) if isinstance(spec, tuple) else spec


def _check_obj(obj, where, required, optional):
    out = []
    if not isinstance(obj, dict):
        return ['%s: not an object' % where]
    for k, spec in required.items():
        if k not in obj:
            out.append('%s: missing field `%s`' % (where, k))
        elif not _type_ok(obj[k], spec):
            out.append('%s: field `%s` must be %s, got %s'
                       % (where, k, _name(spec), type(obj[k]).__name__))
    for k, v in obj.items():
        if k in required:
            continue
        if k not in optional:
            out.append('%s: unknown field `%s`' % (where, k))
        elif not _type_ok(v, optional[k]):
            out.append('%s: field `%s` must be %s, got %s'
                       % (where, k, _name(optional[k]), type(v).__name__))
    return out


def check_doc(name, doc):
    """Return a list of violation strings for one parsed export (name without .json)."""
    required, optional = SCHEMAS[name]
    out = _check_obj(doc, name, ENVELOPE, {})
    rows = doc.get('rows') if isinstance(doc, dict) else None
    if not isinstance(rows, list):
        return out
    seen = {}
    for i, r in enumerate(rows):
        where = '%s rows[%d]' % (name, i)
        out += _check_obj(r, where, required, optional)
        if not isinstance(r, dict):
            continue
        if name == 'models':
            for j, f in enumerate(r.get('fields') or []):
                out += _check_obj(f, '%s fields[%d]' % (where, j), MODEL_FIELD, {})
            key = r.get('key')
            if isinstance(key, str):
                if not key.endswith('::' + str(r.get('class'))):
                    out.append('%s: `key` %r does not end with `::<class>`' % (where, key))
                if key in seen:
                    out.append('%s: duplicate key %r (first at rows[%d])'
                               % (where, key, seen[key]))
                seen.setdefault(key, i)
    return out


def check_repo(repo):
    """Validate every export under <repo>/data; return all violation strings."""
    out, envelopes = [], {}
    for n in FILES:
        path = os.path.join(repo, 'data', n + '.json')
        if not os.path.isfile(path):
            out.append('%s.json: file missing' % n)
            continue
        try:
            with open(path, encoding='utf-8') as fh:
                doc = json.load(fh)
        except (OSError, ValueError) as e:
            out.append('%s.json: not valid JSON (%s)' % (n, e))
            continue
        out += check_doc(n, doc)
        if isinstance(doc, dict):
            envelopes[n] = doc
    for k in ('app_version', 'snapshot'):
        vals = {n: d.get(k) for n, d in envelopes.items()}
        if len({json.dumps(v) for v in vals.values()}) > 1:
            out.append('%s differs between files: %s' % (
                k, ', '.join('%s=%r' % kv for kv in sorted(vals.items()))))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--repo', default='.')
    ap.add_argument('--check', action='store_true',
                    help='exit 1 when any violation is found')
    a = ap.parse_args(argv)
    v = check_repo(a.repo)
    for line in v:
        print(line)
    print('%d violation(s) in data/*.json' % len(v))
    return 1 if (a.check and v) else 0


if __name__ == '__main__':
    sys.exit(main())
