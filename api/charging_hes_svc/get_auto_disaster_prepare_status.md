> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_auto_disaster_prepare_status

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/get_auto_disaster_prepare_status`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x34b6cac`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x34b6ba0` |

## `param_type`/`cmd`

n/a

## Response model (link)

<!-- TODO -->

## Response

<!-- TODO -->

## Example request/response

<!-- TODO -->

## Errors seen

`api/errors.md`: <!-- TODO -->

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getAutoDisasterPrepareStatus` @0x34b6ba0 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/util/demosite_util_impl.dart`: `DemoSiteUtilImpl` @0x4a33a6c (URL literal only, no `*Http*` call)

Called from:

- `charging/boostrap_impl.dart::DIInit`
- `charging/http/http_request_repository.dart::getAutoDisasterPrepareStatus`
- `charging/ui/page/family/auto_disaster/auto_disaster_tips_logic.dart::_getNetAutoDisasterPrepareStatus`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
