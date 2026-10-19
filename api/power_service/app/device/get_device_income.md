> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_device_income

## Purpose

<!-- TODO -->

## Upstream name

`get_device_income` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/app/device/get_device_income`, method: not extracted by the inventory <!-- TODO -->; string-only: `ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart @0x29fa1dc`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart @0x2eecbdc` |
| `type` | ? | ? | ? | `ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart @0x2eecbdc` |
| `start_time` | ? | ? | ? | `ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart @0x2eecbdc` |

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

- `ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart`: `getChartStatistics` @0x2eecbdc (encryptionRequestHttp; encrypted: true); `getTotalBenefit` @0x29fa084 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
