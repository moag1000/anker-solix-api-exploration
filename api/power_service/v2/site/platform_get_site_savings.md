> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# platform_get_site_savings

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v2/site/platform_get_site_savings`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a17e2/benifits/a17e2_benifits_http_repository.dart @0x2a48244`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `charging/ui/page/device/a17e2/benifits/a17e2_benifits_http_repository.dart @0x2a47fd4` |
| `type` | ? | ? | ? | `charging/ui/page/device/a17e2/benifits/a17e2_benifits_http_repository.dart @0x2a47fd4` |
| `data_type` | ? | ? | ? | `charging/ui/page/device/a17e2/benifits/a17e2_benifits_http_repository.dart @0x2a47fd4` |
| `start_time` | ? | ? | ? | `charging/ui/page/device/a17e2/benifits/a17e2_benifits_http_repository.dart @0x2a47fd4` |

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

- `charging/ui/page/device/a17e2/benifits/a17e2_benifits_http_repository.dart`: `getChartStatistics` @0x2a47fd4 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `station_home/src/ui/shared/income/income_detail/income_detail_controller.dart`: `getChartStatistics` @0x2a43540 (request; encrypted: default-true (requestHttp) — verify)

Called from:

- `station_home/src/ui/shared/income/income_detail/income_detail_controller.dart::_executeChartDataRequest`
- `station_home/src/ui/shared/income/income_detail/income_detail_controller.dart::_updateCurrentMonthDataIfNeeded`

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
