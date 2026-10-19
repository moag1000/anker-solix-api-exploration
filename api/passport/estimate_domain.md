> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# estimate_domain

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/passport/estimate_domain`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x27408ac`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `ab` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x274080c` |
| `mode` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x274080c` |

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

- `charging/http/http_request_repository_impl.dart`: `getRegionHostRequest` @0x274080c (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/account/handlers/region_switch_handler.dart::_getRegionHostAsync`
- `charging/http/http_request_repository.dart::getRegionHostRequest`
- `charging/ui/page/account/region/region_logic.dart::showConfirmDialog`
- `charging/ui/page/account/splash/splash_logic.dart::requestHostByRegion`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
