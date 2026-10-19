> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_mi_layout

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/get_mi_layout`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x2931220`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | ? | ? | ? | `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x2931054` |
| `type` | ? | ? | ? | `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x2931054` |
| `start` | ? | ? | ? | `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x2931054` |
| `end` | ? | ? | ? | `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x2931054` |

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

- `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart`: `getSolarMiLayout` @0x2931054 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
