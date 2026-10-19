"""Write api/README.md and api/<service>/README.md from data/endpoints.json and the pages on disk.

Usage (repo root):
  python3 -I tools/service_index.py [--endpoints data/endpoints.json] [--api api]

Page paths follow render_pages.endpoint_path.  A page counts as a skeleton while
it still has `Confidence: string-only` and at least five `<!-- TODO -->` markers;
for every other page the purpose column is the first line under "## Purpose".
The output is a pure function of the JSON and the files, so a second run changes
nothing.  Standard library only.
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render_pages  # noqa: E402

DATE = '2026-10-19'
HDR = ('> Verified against: App 3.24.3 · Date: %s · Page type: guidance '
       '(no API facts) · Owner page: this page' % DATE)

INTRO = (
    "This directory holds one page per cloud endpoint, grouped by service (the "
    "first URL segment after the host), plus the cross-cutting pages "
    "`param_types.md`, `errors.md`, `auth.md`, `encryption.md` and "
    "`sdk_senders.md` (the direct SDK senders several endpoint groups share). "
    "An endpoint "
    "page is the single owner of that endpoint's request parameters, response "
    "payload and confidence tags. Paths follow the naming rule in "
    "[../docs/STRUCTURE.md](../docs/STRUCTURE.md#naming-conventions): `v1` is "
    "dropped from the path, any other version segment is kept.")

AMBIGUOUS = """## Ambiguous prefixes (resolved: all five are real services)

Checked on 2026-10-19 against the 3.24.3 asm (`blutter_output/asm`, grep only). Five prefixes looked ambiguous in the object-pool strings:

| prefix | URL literals (`"/<prefix>/...`) | Dart package paths | verdict |
|---|---|---|---|
| `smart_service` | 13 | none | real service: 13 endpoints, sent through `encryptionRequestHttp`/`encryptionRequestHttpByGHttpRequest` in `anka_agent/http/` |
| `device_svc` | 3 | none | real service: 3 endpoints, sent via `encryptionRequestHttp` |
| `privacy_service` | 2 | none | real service: 2 endpoints (data export), sent via `encryptionRequestHttp` |
| `energy` | 4 | 6 (`.../src/energy/model/...`) | real service: 4 endpoints (`/energy/v1/...`). The package paths are unrelated Dart directories and are not endpoints |
| `site` | 2 | 12 (`.../family/site/...`) | real service: 2 endpoints (`/site/v1/...`). The package paths are unrelated Dart directories and are not endpoints |

Result: none of the five is only a Dart package path; every one has URL literals with a leading `/` that a `*Http*` sender uses, so all five are inventoried and have their own directory above. Related oddities, not errors: `v2/` holds four `/v2/anka/...` URLs (the version segment comes first, so the URL prefix rule makes `v2` the service directory; the four rows are URL literals with no traced sender, one of them removed in 3.24.3), and `ems/`, `generator/` and `marketing/` hold one endpoint each.
"""

NOT_HERE = ("Not here: MQTT or BLE facts (see [../mqtt/README.md](../mqtt/README.md), "
            "[../ble/README.md](../ble/README.md)), step-by-step flows "
            "([../flows/README.md](../flows/README.md)); ownership rules are in "
            "[../docs/STRUCTURE.md](../docs/STRUCTURE.md).")


def page_info(path, rows):
    txt = open(path, encoding='utf-8').read()
    conf = re.search(r'Confidence: ([a-z-]+)', txt.splitlines()[0]).group(1)
    skel = conf == 'string-only' and txt.count('<!-- TODO -->') >= 5
    purpose = 'TODO'
    if not skel:
        m = re.search(r'## Purpose\n\n(.*?)\n', txt)
        purpose = m.group(1) if m else 'TODO'
    keys = sorted({r['upstream_key'] for r in rows if r.get('upstream_key')})
    removed = all(r.get('removed_in') for r in rows)
    pool_only = all(r.get('reference') == 'pool-only' for r in rows)
    status = ('removed in 3.24.3, ' if removed else
              'pool-only in 3.24.3, ' if pool_only else '') + (
        'skeleton' if skel else 'hand-written')
    return skel, purpose, ', '.join('`%s`' % k for k in keys) or '-', status


def build(endpoints, api):
    by = {}
    for r in endpoints['rows']:
        by.setdefault(r['url'], []).append(r)
    svc = {}
    covered = set()
    for url in sorted(by):
        p = render_pages.endpoint_path(url)  # api/<service>/.../<name>.md
        covered.add(p)
        svc.setdefault(p.split('/')[1], []).append((url, p))
    # pages on disk with no inventory row (hand-added, e.g. a URL the app never
    # sends) keep their row; the url shown is the page path without `.md`
    for service in sorted(os.listdir(api)):
        top = os.path.join(api, service)
        if not os.path.isdir(top):
            continue
        for dirpath, _, files in os.walk(top):
            for f in sorted(files):
                if not f.endswith('.md') or f == 'README.md':
                    continue
                rel = os.path.relpath(os.path.join(dirpath, f), api)
                p = 'api/' + rel.replace(os.sep, '/')
                if p in covered:
                    continue
                url = '/' + p[len('api/'):-len('.md')]
                svc.setdefault(service, []).append((url, p))
    out = {}
    summary = []
    for s in sorted(svc):
        L = [HDR, '', '# %s' % s, '',
             'Service index for the URL prefix `/%s/`. Each endpoint page is the '
             'single owner of its request, response and tags; a skeleton page '
             '(status "skeleton", purpose TODO) carries only what '
             '`data/endpoints.json` knows and has `Confidence: string-only` until '
             'a human reads the asm. Upstream keys are `API_ENDPOINTS` keys of '
             '`api/apitypes.py`.' % s, '',
             '| endpoint | purpose | upstream key | status |', '|---|---|---|---|']
        nskel = 0
        for url, p in sorted(svc[s], key=lambda x: x[1]):
            disk = os.path.join(api, os.path.relpath(p, 'api'))
            if url in by:
                skel, purpose, keys, status = page_info(disk, by[url])
            else:
                skel, purpose, keys, status = page_info(disk, [])
                status = 'hand-written, not in `data/endpoints.json`'
                if skel:
                    status = 'skeleton, not in `data/endpoints.json`'
                    purpose = 'TODO'
            nskel += bool(skel and url in by)
            L.append('| [`%s`](%s) | %s | %s | %s |' % (
                url, os.path.relpath(p, 'api/' + s), purpose, keys, status))
        L += ['', NOT_HERE.replace('../', '../../'), '']
        out[os.path.join(api, s, 'README.md')] = '\n'.join(L)
        summary.append((s, sum(1 for u, _ in svc[s] if u in by), nskel))
    total = sum(n for _, n, _ in summary)
    gone = sum(1 for u, rs in by.items() if all(r.get('removed_in') for r in rs))
    pool = sum(1 for u, rs in by.items()
               if all(r.get('reference') == 'pool-only' for r in rs))
    L = [HDR, '', '# API', '', INTRO, '', '## Service index', '',
         'One directory per URL prefix: %d distinct URLs (%d with a code reference '
         'in 3.24.3, %d only in the 3.24.3 object pool with no code reference, %d '
         'absent from 3.24.3 and only in 3.18.0). Counts include hand-written pages; all other pages are '
         'skeletons rendered from `data/endpoints.json` by '
         '`tools/render_pages.py`.' % (total, total - gone - pool, pool, gone), '',
         '| service | pages | index |', '|---|---|---|']
    for n, c, _ in summary:
        L.append('| `%s/` | %d | [%s/README.md](%s/README.md) |' % (n, c, n, n))
    L += ['', AMBIGUOUS, NOT_HERE, '']
    out[os.path.join(api, 'README.md')] = '\n'.join(L)
    return out, summary


KEEP_MARKER = '<!-- hand-written below: kept by tools/service_index.py -->'


def keep_tail(path, text):
    """Append the hand-written part of an existing README (from KEEP_MARKER on)."""
    if os.path.exists(path):
        with open(path, encoding='utf-8') as fh:
            old = fh.read()
        i = old.find(KEEP_MARKER)
        if i >= 0:
            return text.rstrip('\n') + '\n\n' + old[i:]
    return text


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--endpoints', default='data/endpoints.json')
    ap.add_argument('--api', default='api')
    a = ap.parse_args(argv)
    with open(a.endpoints, encoding='utf-8') as fh:
        data = json.load(fh)
    out, summary = build(data, a.api)
    for path, text in out.items():
        text = keep_tail(path, text)
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(text)
    print('%d indexes, %d pages (%d skeletons)' % (
        len(out), sum(n for _, n, _ in summary), sum(k for _, _, k in summary)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
