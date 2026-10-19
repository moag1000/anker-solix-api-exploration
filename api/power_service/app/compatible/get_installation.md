> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_installation

## Purpose

<!-- TODO -->

## Upstream name

`get_installation` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/app/compatible/get_installation`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x23f2ea4`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `solarbank_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x23f2d64` |
| `site_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x23f2d64` |

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

- `charging/http/http_request_repository_impl.dart`: `getInstallationApi` @0x23f2d64 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getInstallationApi`
- `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart::getInstallationReq`
- `charging/ui/page/device/a17c0/ez1_current_mode/ez1_current_mode_logic.dart::getInstallationReq`
- `charging/ui/page/device/a17c0/ez1_select_mode/ez1_select_mode_logic.dart::getInstallationReq`
- `charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart::goSelectMode`
- `charging/ui/page/device/main/station_device_home/station_main_page/station_main_page_logic.dart::goSelectMode`
- `charging/ui/page/device/main/station_device_home/station_setting/station_setting_logic.dart::getInstallationReq`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
