> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# energy_statistics

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_energy_service/energy_statistics`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x24390dc`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | ? | ? | ? | `charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x2438ee4` |
| `productCode` | ? | ? | ? | `charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x2438ee4` |
| `sourceType` | ? | ? | ? | `charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x2438ee4` |
| `dateType` | ? | ? | ? | `charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x2438ee4` |
| `start` | ? | ? | ? | `charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x2438ee4` |
| `end` | ? | ? | ? | `charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x2438ee4` |
| `global` | ? | ? | ? | `charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x2438ee4` |

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

- `charging/ui/page/station/mixin/station_chart_http_reposity.dart`: `getChartStatistics` @0x2438ee4 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
