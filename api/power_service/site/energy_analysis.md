> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# energy_analysis

## Purpose

<!-- TODO -->

## Upstream name

`energy_analysis` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/site/energy_analysis`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a1782/station/station_main_page/chart/chart_http_repository.dart @0x2370ff8`
(literal also at 2 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `charging/ui/page/device/a1782/station/station_main_page/chart/chart_http_repository.dart @0x2370b5c` |
| `type` | ? | ? | ? | `charging/ui/page/device/a1782/station/station_main_page/chart/chart_http_repository.dart @0x2370b5c` |
| `device_sn` | ? | ? | ? | `charging/ui/page/device/a1782/station/station_main_page/chart/chart_http_repository.dart @0x2370b5c` |
| `device_type` | ? | ? | ? | `charging/ui/page/device/a1782/station/station_main_page/chart/chart_http_repository.dart @0x2370b5c` |
| `start_time` | ? | ? | ? | `charging/ui/page/device/a1782/station/station_main_page/chart/chart_http_repository.dart @0x2370b5c` |
| `end_time` | ? | ? | ? | `charging/ui/page/device/a1782/station/station_main_page/chart/chart_http_repository.dart @0x2370b5c` |
| `phase` | ? | ? | ? | `charging/ui/page/device/a1782/station/station_main_page/chart/chart_http_repository.dart @0x2370b5c` |
| `enable_third_party_pv` | ? | ? | ? | `common_view/charts/station_chart_http_reposity.dart @0x230db24` |

Rows are the union over 3 senders; `source` is the first sender that sets the key.

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

- `charging/ui/page/device/a1782/station/station_main_page/chart/chart_http_repository.dart`: `getChartStatistics` @0x2370b5c (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/ui/page/device/greenpower/charts/chart_http_repository.dart`: `getGreenPPsStatistics` @0x23ff9fc (encryptionRequestHttp; encrypted: true)
- `common_view/charts/station_chart_http_reposity.dart`: `getStationEnergyStatistics` @0x230db24 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
