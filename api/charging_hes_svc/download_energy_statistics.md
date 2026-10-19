> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# download_energy_statistics

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/download_energy_statistics`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x301c558`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `start` | ? | ? | ? | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x301c460` |
| `end` | ? | ? | ? | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x301c460` |
| `productCode` | ? | ? | ? | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x301c460` |
| `dateType` | ? | ? | ? | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x301c460` |
| `siteId` | ? | ? | ? | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x301c460` |
| `sourceType` | ? | ? | ? | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x301c460` |

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

- `charging/ui/page/device/a5101/charts/chart_http_repository.dart`: `getDownloadEnergyStatistics` @0x301c460 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/util/demosite_util_impl.dart`: `DemoSiteUtilImpl` @0x4a33a6c (URL literal only, no `*Http*` call)

Called from:

- `charging/boostrap_impl.dart::DIInit`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
