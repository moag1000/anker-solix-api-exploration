> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_compatible_process

## Purpose

<!-- TODO -->

## Upstream name

`compatible_process` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/app/compatible/get_compatible_process`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x26735ac`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `solar_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x26734ec` |
| `solarbank_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x26734ec` |

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

- `charging/http/http_request_repository_impl.dart`: `checkSolarForceUpdateState` @0x26734ec (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::checkSolarForceUpdateState`, `charging/ui/page/device/a17c0/a17c0home/a17c0home_logic.dart::checkSolarForceUpdate`, `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart::checkSolarForceUpdate`, `charging/ui/page/device/connect/zx_config_wifi_success/zx_config_wifi_succees_logic.dart::checkSolarForceUpdate`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
