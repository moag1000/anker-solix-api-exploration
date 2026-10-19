> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# statisticsPv

## Purpose

<!-- TODO -->

## Upstream name

`get_device_pv_statistics` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/charging_pv_svc/statisticsPv`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a5140/a5140charts/chart_http_reposity.dart @0x30363e4`
(literal also at 3 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | ? | ? | ? | `charging/ui/page/device/a5140/a5140charts/chart_http_reposity.dart @0x3036204` |
| `type` | ? | ? | ? | `charging/ui/page/device/a5140/a5140charts/chart_http_reposity.dart @0x3036204` |
| `start` | ? | ? | ? | `charging/ui/page/device/a5140/a5140charts/chart_http_reposity.dart @0x3036204` |
| `end` | ? | ? | ? | `charging/ui/page/device/a5140/a5140charts/chart_http_reposity.dart @0x3036204` |
| `version` | ? | ? | ? | `charging/ui/page/device/a5140/a5140charts/chart_http_reposity.dart @0x3036204` |
| `siteId` | ? | ? | ? | `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x2933314` |
| `dcPort` | ? | ? | ? | `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x2933314` |

Rows are the union over 4 senders; `source` is the first sender that sets the key.

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

- `charging/ui/page/device/a5140/a5140charts/chart_http_reposity.dart`: `getPvStatistics` @0x3036204 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/a5150/homePage/a5150_http_reposity.dart`: `getPvStatistics` @0x303d01c (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart`: `getSolarStatistics` @0x2933314 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/greenpower/charts/chart_http_repository.dart`: `getGreenPvStatistics` @0x23fec04 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
