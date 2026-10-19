> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# list_user_devices

## Purpose

<!-- TODO -->

## Upstream name

`user_devices` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/site/list_user_devices`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x23f43a4`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_models` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x23f42a4` |

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

- `charging/http/http_request_repository_impl.dart`: `getUserPPSDevice` @0x23f42a4 (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::getUserPPSDevice`, `charging/ui/page/device/a1782/station/add_devices/a1782_add_devices_logic.dart::getUserDeviceList`, `charging/ui/page/device/a17b1/a17b1select_devices/a17b1select_devices_logic.dart::_getUserDeviceList`, `charging/ui/page/device/a17c0/select_station/select_station_logic.dart::getUserDeviceList`, `charging/ui/page/device/main/sitation_energy_system/station_home_settings/add_devices/add_devices_logic.dart::deleteGroup`, `charging/ui/page/device/main/sitation_energy_system/station_home_settings/add_devices/add_devices_logic.dart::getUserDeviceList`, `charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart::getUserPPSDeviceList`, `charging/ui/page/device/main/station_device_home/station_main_page/station_main_page_logic.dart::getUserPPSDeviceList`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
