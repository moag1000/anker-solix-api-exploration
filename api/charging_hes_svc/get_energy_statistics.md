> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_energy_statistics

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/get_energy_statistics`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x23e5a10`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | ? | ? | ? | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x23e5710` |
| `productCode` | ? | ? | ? | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x23e5710` |
| `sourceType` | ? | ? | ? | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x23e5710` |
| `dateType` | ? | ? | ? | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x23e5710` |
| `start` | ? | ? | ? | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x23e5710` |
| `end` | ? | ? | ? | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x23e5710` |
| `global` | ? | ? | ? | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x23e5710` |

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

- `charging/ui/page/device/a5101/charts/chart_http_repository.dart`: `getChartStatistics` @0x23e5710 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
