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


def _clean(seg):
    return re.sub(r'[^a-z0-9_]+', '_', seg.lower()).strip('_') or 'x'


ENVELOPE_NOISE = {'url', 'method', 'useWebsocket', 'isAIotEnv'}


def is_noise_key(k, envelope=False):
    """Extractor noise.  Local-variable fragments (trailing `:`, `.isEmpty`,
    leading space) are noise anywhere; the transport names url/method/
    useWebsocket/isAIotEnv are noise only in `envelope` (in `params` they are
    real request keys)."""
    if k.endswith(':') or '.isEmpty' in k or k.startswith(' '):
        return True
    return envelope and k in ENVELOPE_NOISE


def request_keys(r):
    """Request keys of one row: params if any, else envelope; noise removed."""
    if r['params']:
        return [k for k in r['params'] if not is_noise_key(k)]
    return [k for k in r['envelope'] if not is_noise_key(k, envelope=True)]


def endpoint_path(url):
    """`v1` (the default API version) is dropped; any other version segment
    (v2, v3, ...) is kept.  The first segment is the service directory."""

    segs = [s for s in url.split('/') if s]
    service, last = _clean(segs[0]), _clean(segs[-1])
    mid = [s for s in segs[1:-1] if s != 'v1']
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


def _enc_state(r):
    """Per-row encrypted value as written on the page."""
    if r['role'] != 'sender':
        return 'unknown (URL literal only, no `*Http*` call)'
    if r['encrypted']:
        return 'true'
    if r.get('encryption_note'):
        return 'default-true (requestHttp) — verify'
    return 'false'


def _sender_note(r):
    """Result of the caller walk (`sender`, `sender_via`, `resolution`)."""
    if r.get('sender'):
        if not r.get('sender_via'):
            return '; sends in the same function (SDK `handle`): `%s`' % r['sender']
        note = '; sender found through callers: `%s` via %s' % (
            r['sender'], ' -> '.join('`%s`' % v for v in r['sender_via']))
        if r.get('sender_also'):
            note += '; also %s' % ', '.join('`%s`' % v for v in r['sender_also'])
        return note
    if r.get('resolution') == 'mixin-gap':
        return ('; caller walk enters a deduplicated mixin function absent from '
                'the dump (UNCONFIRMED)')
    if r.get('resolution') == 'unresolved':
        return '; no sender within 3 caller levels'
    return ''


def _is_removed(rows):
    return all(r.get('removed_in') for r in rows)


def _is_pool_only(rows):
    return all(r.get('reference') == 'pool-only' for r in rows)


def render_endpoint(rows, date=None, version='3.24.3'):
    """One skeleton for ALL rows (senders and URL providers) of one URL."""
    date = date or datetime.date.today().isoformat()
    first = rows[0]
    url = first['url']
    last = url.rsplit('/', 1)[-1]
    removed = _is_removed(rows)
    L = [header(date), '']
    pool_only = _is_pool_only(rows)
    if removed:
        L += ['Removed in %s — present in 3.18.0 only' % version, '']
    elif pool_only:
        L += ['%s: string present in the object pool, no code reference found '
              '(present in 3.18.0 with a sender)' % version, '']
    L += ['# %s' % last, '', '## Purpose', '', TODO, '', '## Upstream name', '']
    keys = sorted({r['upstream_key'] for r in rows if r.get('upstream_key')})
    if keys:
        L.append('%s in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).'
                 % ', '.join('`%s`' % k for k in keys))
    else:
        L.append('`none` (no upstream name)')
    addrs = sorted({(r['dart_file'], r['url_addr']) for r in rows})
    L += ['', '## Method+URL', '',
          '`%s`, method: not extracted by the inventory %s; string-only: `%s @%s`'
          % (url, TODO, addrs[0][0], addrs[0][1])]
    if len(addrs) > 1:
        L.append('(literal also at %d more site(s) in `data/endpoints.json`)'
                 % (len(addrs) - 1))
    senders = [r for r in rows if r['role'] == 'sender']
    L += ['', '## Encrypted?', '']
    states = sorted({_enc_state(r) for r in (senders or rows)})
    L.append('encrypted: %s. Scheme and header rules: `api/encryption.md`; '
             'per-sender values are in "Callers in app".'
             % ' / '.join('`%s`' % x if x in ('true', 'false') else '"%s"' % x
                          for x in states))
    L += ['', '## Request', '']
    shown = [r for r in rows if request_keys(r)]
    if not shown:
        L += ['No request keys found by the extractor. %s' % TODO, '']
    else:
        env = sorted({k for r in shown if r['param_data_is_json']
                      for k in r['envelope']
                      if not is_noise_key(k, envelope=True)})
        if env:
            L += ['Some senders wrap these keys in `param_data` as a JSON string '
                  '(`jsonEncode`); outer keys: %s.' % ', '.join(
                      '`%s`' % k for k in env), '']
        L += ['| field | type | required | example | source |',
              '|---|---|---|---|---|']
        seen_p = set()
        for r in shown:
            src = '%s @%s' % (r['dart_file'], r['addr'])
            for p in request_keys(r):
                if p not in seen_p:
                    seen_p.add(p)
                    L.append('| `%s` | ? | ? | ? | `%s` |' % (p, src))
        if len(shown) > 1:
            L += ['', 'Rows are the union over %d senders; `source` is the first '
                  'sender that sets the key.' % len(shown)]
        L.append('')
    L += ['## `param_type`/`cmd`', '']
    if any(r['param_type'] or r['cmd'] is not None for r in rows):
        L.append('see `api/param_types.md`')
        if any(r.get('param_type_source') == 'variable' for r in rows):
            L.append('')
            L.append('param_type is a variable at this sender (traced by heuristic '
                     '— verify against the callers in `data/param_types.json`).')
    else:
        L.append('n/a')
    L += ['', '## Response model (link)', '', TODO, '', '## Response', '', TODO, '',
          '## Example request/response', '', TODO, '', '## Errors seen', '',
          '`api/errors.md`: %s' % TODO, '', '## Callers in app', '']
    by_file = {}
    for r in rows:
        by_file.setdefault(r['dart_file'], []).append(r)
    for f, rs in sorted(by_file.items()):
        parts = []
        for r in rs:
            if r['role'] == 'sender':
                pt = ', param_type/cmd: see `api/param_types.md`' if (
                    r['param_type'] or r['cmd'] is not None) else ''
                parts.append('`%s` @%s (%s; encrypted: %s%s)' % (
                    r['function'], r['addr'],
                    ', '.join(c.split('::')[-1] for c in r['http_callees']),
                    _enc_state(r), pt))
            else:
                parts.append('`%s` @%s (URL literal only, no `*Http*` call%s)'
                             % (r['function'], r['addr'], _sender_note(r)))
        L.append('- `%s`: %s' % (f, '; '.join(parts)))
    ui = sorted({c for r in rows for c in r['callers']})
    if ui:
        L += ['', 'Called from:', ''] + ['- `%s`' % c for c in ui]
    L += ['', '## Since/changed', '']
    sinces = sorted({r['since'] for r in rows if r.get('since')})
    if removed:
        L.append('3.18.0: present. 3.24.3: absent (removed). since: %s.'
                 % ', '.join(sinces))
    elif pool_only:
        L.append('3.18.0: present. %s: string present in the object pool, no code '
                 'reference found. since: %s.' % (version, ', '.join(sinces)))
    elif sinces == [version]:
        L.append('3.18.0: absent. 3.24.3: present (new). since: %s.' % version)
    else:
        L.append('3.18.0: present. 3.24.3: present. since: %s. %s (compare params in '
                 '`tools/out/diff_3.18.0_3.24.3.md`)' % (', '.join(sinces), TODO))
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
        by_url.setdefault(r['url'], []).append(r)
    seen = {}
    for url in sorted(by_url):
        p = endpoint_path(url)
        if p in seen:
            raise ValueError('path collision: %s and %s -> %s' % (seen[p], url, p))
        seen[p] = url
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
