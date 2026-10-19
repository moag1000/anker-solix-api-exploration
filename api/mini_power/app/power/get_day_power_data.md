> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_day_power_data

## Purpose

<!-- TODO -->

## Upstream name

`charger_get_statistics` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/mini_power/v1/app/power/get_day_power_data`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x28a8538`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_model` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x28a8454` |
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x28a8454` |
| `date` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x28a8454` |

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

- `charging/http/http_request_repository_impl.dart`: `getDayPowerData` @0x28a8454 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getDayPowerData`
- `charging/impl/http_service_impl.dart::getDayPowerData`
- `charging/ui/page/device/a2345/a2345power_curve/a2345power_curve_logic.dart::_getPowerCurveData`
- `charging/ui/page/device/a91b2/a91b2power_curve/a91b2power_curve_logic.dart::_getPowerCurveData`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
