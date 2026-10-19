> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_ota_update

## Purpose

<!-- TODO -->

## Upstream name

`get_ota_update` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/app/compatible/get_ota_update`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x33fbc84`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x33fbb74` |
| `insert_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x33fbb74` |

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

- `charging/http/http_request_repository_impl.dart`: `getThirdOtaStatus` @0x33fbb74 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getThirdOtaStatus`
- `charging/ui/page/device/a17c0/ez1_select_mode/ez1_select_mode_logic.dart::getOTAUpdateStatus`
- `charging/ui/page/device/a17c0/select_solar_power/select_solar_power_logic.dart::getThirdOtaStatusRes`
- `charging/ui/page/qr_Scanner/qr_scanner_logic.dart::getOTAUpdateStatus`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
