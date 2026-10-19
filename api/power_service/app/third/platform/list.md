> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# list

## Purpose

<!-- TODO -->

## Upstream name

`get_third_platforms` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/app/third/platform/list`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x26192fc`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `app_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x2619228` |

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

- `charging/http/http_request_repository_impl.dart`: `getThirdPartyPlatformList` @0x2619228 (encryptionRequestHttp; encrypted: true)
- `flutter_charging_beginning/beginning/state_cards/add_devices/platform_appoint_add_device/platform_appoint_add_device_controller.dart`: `getThirdPartyPlatformList` @0x24e60d8 (URL literal only, no `*Http*` call)

Called from: `charging/http/http_request_repository.dart::getThirdPartyPlatformList`, `charging/ui/page/device/connect/scan_logic.dart::onInit`, `charging/ui/page/device/connect/third_party_platform_list/third_party_platform_list_logic.dart::requestThirdPartyPlatformList`, `charging/ui/page/device/main/sitation_energy_system/scan_appoint_device/scan_appoint_device_logic.dart::onInit`, `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::_initLogic`, `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::onMessageDispatch`, `flutter_charging_beginning/beginning/state_cards/add_devices/platform_appoint_add_device/platform_appoint_add_device_controller.dart::afterPermissionEnable`, `flutter_charging_beginning/beginning/state_cards/add_devices/platform_appoint_add_device/platform_appoint_add_device_controller.dart::onInit`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
