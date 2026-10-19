"""Render page skeletons from the generated JSON (prose is left for humans).

Usage:
  python3 -I tools/render_pages.py [--endpoints data/endpoints.json] \
      [--models data/models.json] [--out tools/out/pages] [--date YYYY-MM-DD]

Writes `<out>/api/<service>/.../<last_segment>.md` per endpoint URL (template
docs/templates/endpoint.md) and `<out>/models/<snake_class>.md` per model
(docs/templates/model.md).  It never writes into api/ or models/ of the repo;
copy a skeleton over by hand once its prose has been written.  Every skeleton
carries `Confidence: string-only`, because nothing here is traced by a human.
"""
import argparse
import datetime
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

TODO = '<!-- TODO -->'
VERSION_SEG = re.compile(r'^v\d+$')


def _clean(seg):
    return re.sub(r'[^a-z0-9_]+', '_', seg.lower()).strip('_') or 'x'


def endpoint_path(url, keep_version=False):
    segs = [s for s in url.split('/') if s]
    service, last = _clean(segs[0]), _clean(segs[-1])
    mid = [s for s in segs[1:-1] if keep_version or not VERSION_SEG.match(s)]
    return '/'.join(['api', service] + [_clean(m) for m in mid] + [last + '.md'])


def snake(name):
    s = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s).lower().replace('$', '_')


def _base(dart_file):
    return dart_file.rsplit('/', 1)[-1]


def header(date, owner='this page'):
    return ('> Verified against: App 3.24.3 · Date: %s · '
            'Confidence: string-only · Owner page: %s' % (date, owner))


def _yn(v):
    return {True: 'yes', False: 'no', None: 'unknown'}[v]


def render_endpoint(rows, date=None, version='3.24.3'):
    date = date or datetime.date.today().isoformat()
    first = rows[0]
    url = first['url']
    last = url.rsplit('/', 1)[-1]
    L = [header(date), '', '# %s' % last, '', '## Purpose', '', TODO, '',
         '## Upstream name', '']
    keys = sorted({r['upstream_key'] for r in rows if r.get('upstream_key')})
    if keys:
        L.append('%s in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).'
                 % ', '.join('`%s`' % k for k in keys))
    else:
        L.append('`none` (no upstream name)')
    L += ['', '## Method+URL', '',
          '`%s` (method: %s), string-only: `%s @%s`' % (
              url, TODO, _base(first['dart_file']), first['url_addr']), '',
          '## Encrypted?', '']
    enc = sorted({r['encrypted'] for r in rows})
    senders = [r for r in rows if r['role'] == 'sender']
    if True in enc and False in enc:
        L.append('Mixed across callers, see the per-sender list below; scheme in '
                 '`api/encryption.md`.')
    elif enc == [True]:
        L.append('Yes, see `api/encryption.md`.')
    else:
        L.append('No encryption helper seen at the sender; see `api/encryption.md` '
                 'and the notes below. %s' % TODO)
    for r in senders:
        note = ' (%s)' % r['encryption_note'] if r.get('encryption_note') else ''
        L.append('- `%s` calls %s at `%s @%s`%s' % (
            r['function'], ', '.join('`%s`' % c for c in r['http_callees']),
            _base(r['dart_file']), r['addr'], note))
    L += ['', '## Request', '']
    shown = [r for r in rows if r['params'] or r['envelope']]
    if not shown:
        L += ['No request keys found by the extractor. %s' % TODO, '']
    for r in shown:
        src = '%s @%s' % (_base(r['dart_file']), r['addr'])
        L.append('### Sender `%s` (%s)' % (r['function'], src))
        L.append('')
        if r['param_data_is_json']:
            L.append('The sender wraps these keys in `param_data` as a JSON string '
                     '(`jsonEncode`); outer keys: %s.' % ', '.join(
                         '`%s`' % k for k in r['envelope']))
            L.append('')
        L += ['| field | type | required | example | source |', '|---|---|---|---|---|']
        for p in r['params'] or r['envelope']:
            L.append('| `%s` | ? | ? | ? | `%s` |' % (p, src))
        L.append('')
    L += ['## `param_type`/`cmd`', '']
    if any(r['param_type'] or r['cmd'] is not None for r in rows):
        L.append('see `api/param_types.md`')
        if any(r.get('param_type_source') == 'variable' for r in rows):
            L.append('')
            L.append('param_type is a variable at this sender (traced by heuristic '
                     '\u2014 verify against the callers in `data/param_types.json`).')
    else:
        L.append('n/a')
    L += ['', '## Response model (link)', '', TODO, '', '## Response', '', TODO, '',
          '## Example request/response', '', TODO, '', '## Errors seen', '',
          '`api/errors.md`: %s' % TODO, '', '## Callers in app', '']
    seen = set()
    for r in rows:
        for c in r['callers']:
            if c not in seen:
                seen.add(c)
                L.append('- `%s` (calls `%s`)' % (c, r['function']))
    for r in rows:
        if r['role'] == 'url_provider':
            L.append('- `%s @%s` holds the URL literal only (no `*Http*` call in '
                     'that function)' % (r['dart_file'], r['addr']))
    if not seen and not any(r['role'] == 'url_provider' for r in rows):
        L.append('No callers found by the extractor.')
    L += ['', '## Since/changed', '']
    sinces = sorted({r['since'] for r in rows if r.get('since')})
    if any(r.get('removed_in') for r in rows):
        L.append('3.18.0: present. 3.24.3: absent (removed).')
    elif sinces == [version]:
        L.append('3.18.0: absent. 3.24.3: present (new).')
    else:
        L.append('3.18.0: present. 3.24.3: present. %s (compare params in '
                 '`tools/out/diff_3.18.0_3.24.3.md`)' % TODO)
    L += ['', '## Known unknowns', '', '- %s' % TODO, '', '## Device-tested by', '',
          'none', '']
    return '\n'.join(L)


def render_model(row, date=None, version='3.24.3'):
    date = date or datetime.date.today().isoformat()
    cls = row['class']
    base = _base(row['dart_file'])
    L = [header(date), '', '# %s' % cls, '', '## Purpose', '', TODO, '',
         '## Dart class + file', '',
         '`%s`, `%s`, fromJson `@%s`' % (cls, row['dart_file'], row['from_json_addr']),
         '', '## Fields', '',
         '| JSON key | Dart type | nullable | since | source |', '|---|---|---|---|---|']
    for f in row['fields']:
        L.append('| `%s` | `%s` | %s | %s | `%s @%s` |' % (
            f['json_key'], f['dart_type'], _yn(f['nullable']),
            f.get('since') or '?', base, f['key_addr']))
    L += ['', '## Produced by', '', TODO, '', '## Consumed by', '', TODO, '',
          '## Changed since 3.18.0', '']
    if row.get('since') == version:
        L.append('- class is new in %s' % version)
    else:
        new = [f['json_key'] for f in row['fields'] if f.get('since') == version]
        for k in new:
            L.append('- added: `%s`' % k)
        for k in row.get('removed_keys', []):
            L.append('- removed: `%s`' % k)
        if not new and not row.get('removed_keys'):
            L.append('- no key added or removed (types not compared)')
    L += ['', '## Known unknowns', '', '- %s' % TODO, '']
    return '\n'.join(L)


REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def out_allowed(out, repo):
    """True only if `out` resolves to <repo>/tools/out or below (component-wise)."""
    from pathlib import Path
    root = Path(repo).resolve() / 'tools' / 'out'
    target = Path(out).resolve()
    return target == root or root in target.parents


def _load(path):
    with open(path, encoding='utf-8') as fh:
        return json.load(fh)


def render_all(endpoints, models, out, date=None):
    n_ep = n_md = 0
    by_url = {}
    for r in endpoints['rows']:
        if r.get('removed_in'):
            continue
        by_url.setdefault(r['url'], []).append(r)
    paths = {}
    for url in by_url:
        paths.setdefault(endpoint_path(url), []).append(url)
    for path, urls in sorted(paths.items()):
        for url in urls:
            p = path if len(urls) == 1 else endpoint_path(url, keep_version=True)
            _write(os.path.join(out, p), render_endpoint(by_url[url], date))
            n_ep += 1
    mrows = [r for r in models['rows'] if not r.get('removed_in')]
    count = {}
    for r in mrows:
        count[r['class']] = count.get(r['class'], 0) + 1
    used = set()
    for r in mrows:
        name = snake(r['class'])
        if count[r['class']] > 1:
            name += '__' + _clean(_base(r['dart_file']).rsplit('.', 1)[0])
        base_name, n = name, 1
        while name in used:  # same class and file stem in different dirs
            n += 1
            name = '%s_%d' % (base_name, n)
        used.add(name)
        _write(os.path.join(out, 'models', name + '.md'), render_model(r, date))
        n_md += 1
    return n_ep, n_md


def _write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(text)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--endpoints', default='data/endpoints.json')
    ap.add_argument('--models', default='data/models.json')
    ap.add_argument('--out', default='tools/out/pages')
    ap.add_argument('--date')
    a = ap.parse_args(argv)
    if not out_allowed(a.out, REPO):
        print('refusing --out %s: output must be inside %s'
              % (a.out, os.path.join(REPO, 'tools', 'out')), file=sys.stderr)
        return 2
    n_ep, n_md = render_all(_load(a.endpoints), _load(a.models), a.out, a.date)
    print('%d endpoint pages, %d model pages -> %s' % (n_ep, n_md, a.out))
    return 0


if __name__ == '__main__':
    sys.exit(main())
