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

def _n(n, word='endpoint'):
    return '%d %s%s' % (n, word, '' if n == 1 else 's')


def ambiguous(c, v2_removed):
    """The ambiguous-prefix section; every count comes from the inventory."""
    g = lambda k: c.get(k, 0)  # noqa: E731
    return """## Ambiguous prefixes (resolved: all five are real services)

Checked on 2026-10-19 against the 3.24.3 asm (`blutter_output/asm`, grep only). Five prefixes looked ambiguous in the object-pool strings. The endpoint counts below are generated from `data/endpoints.json`; for the per-service pages see the service index above.

| prefix | Dart package paths of the same name | verdict |
|---|---|---|
| `smart_service` | none | real service: %s, sent through `encryptionRequestHttp`/`encryptionRequestHttpByGHttpRequest` in `anka_agent/http/` |
| `device_svc` | none | real service: %s, sent via `encryptionRequestHttp` |
| `privacy_service` | none | real service: %s (data export), sent via `encryptionRequestHttp` |
| `energy` | yes (`.../src/energy/model/...`) | real service: %s (`/energy/v1/...`). The package paths are unrelated Dart directories and are not endpoints |
| `site` | yes (`.../family/site/...`) | real service: %s (`/site/v1/...`). The package paths are unrelated Dart directories and are not endpoints |

Result: none of the five is only a Dart package path; every one has URL literals with a leading `/` that a `*Http*` sender uses, so all five are inventoried and have their own directory above. Related oddities, not errors: `v2/` holds %s of the form `/v2/anka/...` (the version segment comes first, so the URL prefix rule makes `v2` the service directory; %d removed in 3.24.3), and `ems/` (%s), `generator/` (%s) and `marketing/` (%s) are small services.
""" % (_n(g('smart_service')), _n(g('device_svc')), _n(g('privacy_service')),
       _n(g('energy')), _n(g('site')), _n(g('v2'), 'URL'), v2_removed,
       _n(g('ems')), _n(g('generator')), _n(g('marketing')))


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
        # links inside a Purpose line are relative to the page, not to the
        # index: keep the link text only (also strips '|' hazards).
        purpose = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', purpose).replace('|', '\\|')
    keys = sorted({r['upstream_key'] for r in rows if r.get('upstream_key')})
    removed = bool(rows) and all(r.get('removed_in') for r in rows)
    pool_only = bool(rows) and all(r.get('reference') == 'pool-only' for r in rows)
    # one of four values: removed / pool-only come from the inventory, the
    # others from the page itself (owner = a purpose without TODO)
    status = ('removed' if removed else 'pool-only' if pool_only else
              'skeleton' if skel or purpose == 'TODO' else 'owner')
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
    pages_on_disk = {}
    tally = {'owner': 0, 'skeleton': 0, 'pool-only': 0, 'removed': 0}
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
                status = ('skeleton' if skel or purpose == 'TODO' else 'owner') + \
                    ', not in `data/endpoints.json`'
                if skel:
                    purpose = 'TODO'
            nskel += bool(skel and url in by)
            tally[status.split(',')[0]] += 1
            L.append('| [`%s`](%s) | %s | %s | %s |' % (
                url, os.path.relpath(p, 'api/' + s), purpose, keys, status))
        L += ['', NOT_HERE.replace('../', '../../'), '']
        out[os.path.join(api, s, 'README.md')] = '\n'.join(L)
        summary.append((s, sum(1 for u, _ in svc[s] if u in by), nskel))
        pages_on_disk[s] = len(svc[s])
    total = sum(n for _, n, _ in summary)
    counts = {}
    for u in by:
        k = render_pages.endpoint_path(u).split('/')[1]
        counts[k] = counts.get(k, 0) + 1
    v2_removed = sum(1 for u, rs in by.items() if u.startswith('/v2/')
                     and all(r.get('removed_in') for r in rs))
    gone = sum(1 for u, rs in by.items() if all(r.get('removed_in') for r in rs))
    pool = sum(1 for u, rs in by.items()
               if all(r.get('reference') == 'pool-only' for r in rs))
    L = [HDR, '', '# API', '', INTRO, '', '## Service index', '',
         'One directory per URL prefix: %d distinct URLs (%d with a code reference '
         'in 3.24.3, %d only in the 3.24.3 object pool with no code reference, %d '
         'absent from 3.24.3 and only in 3.18.0). The pages column counts the pages '
         'on disk per service: one per URL plus hand-written pages that have no '
         'inventory row (%d in total). Skeleton pages are rendered from '
         '`data/endpoints.json` by `tools/render_pages.py`. Page status over all %d pages on disk (a page '
         'has exactly one status; `pool-only` and `removed` come from the '
         'inventory and take precedence over `skeleton`): `owner` %d, `skeleton` %d, '
         '`pool-only` %d, `removed` %d.' % (
             total, total - gone - pool, pool, gone,
             sum(pages_on_disk.values()) - total, sum(pages_on_disk.values()),
             tally['owner'], tally['skeleton'], tally['pool-only'], tally['removed']), '',
         '| service | pages | index |', '|---|---|---|']
    for n, c, _ in summary:
        L.append('| `%s/` | %d | [%s/README.md](%s/README.md) |' % (
            n, pages_on_disk[n], n, n))
    L += ['', ambiguous(counts, v2_removed), NOT_HERE, '']
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


def foreign_prose(old, new):
    """Non-table lines of an existing README that the generator does not emit."""
    keep = {l.strip() for l in new.splitlines() if l.strip() and not l.startswith('|')}
    return [l for l in old.splitlines()
            if l.strip() and not l.startswith('|') and l.strip() not in keep]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--endpoints', default='data/endpoints.json')
    ap.add_argument('--api', default='api')
    a = ap.parse_args(argv)
    with open(a.endpoints, encoding='utf-8') as fh:
        data = json.load(fh)
    out, summary = build(data, a.api)
    final, refused = {}, []
    for path, text in out.items():
        # api/README.md is generated end to end (its text may change with the
        # tool); the guard protects only the service READMEs that people extend
        if os.path.exists(path) and path != os.path.join(a.api, 'README.md'):
            with open(path, encoding='utf-8') as fh:
                old = fh.read()
            if KEEP_MARKER not in old and foreign_prose(old, text):
                refused.append(path)
        final[path] = keep_tail(path, text)
    if refused:
        for path in refused:
            sys.stderr.write('REFUSED: %s has hand-written prose and no "%s" marker; '
                             'add the marker above the hand-written part or move the '
                             'prose; nothing was written\n' % (path, KEEP_MARKER))
        return 1
    for path, text in final.items():
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(text)
    print('%d indexes, %d pages (%d skeletons)' % (
        len(out), sum(n for _, n, _ in summary), sum(k for _, _, k in summary)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
