> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_wifi_info_list

## Purpose

<!-- TODO -->

## Upstream name

`wifi_list` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/site/get_wifi_info_list`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x2385100`
(literal also at 5 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `device/src/station_setting/controller/common_station_wifi/page/device_wifi_info_setting_controller.dart @0x29e6fd0` |

Rows are the union over 5 senders; `source` is the first sender that sets the key.

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

- `charging/http/http_request_repository_impl.dart`: `getSiteWifiInfoRequest` @0x238507c (encryptionRequestHttp; encrypted: true)
- `device/src/station_setting/controller/common_station_wifi/page/device_wifi_info_setting_controller.dart`: `fetchDeviceWifiInfo` @0x29e6fd0 (encryptionRequestHttp; encrypted: true)
- `device/src/station_setting/controller/common_station_wifi/page/wifi_management_controller.dart`: `fetchDeviceWifiInfo` @0x29eb244 (encryptionRequestHttp; encrypted: true)
- `flutter_charging_beginning/beginning/state_cards/add_devices/select_power_device/select_power_device_controller.dart`: `_fetchSiteWifiSignal` @0x29ecfb4 (encryptionRequestHttp; encrypted: true)
- `micro_hes/src/a17ex/station_setting/device_wifi_info_controller.dart`: `fetchDeviceWifiInfo` @0x29ec464 (encryptionRequestHttp; encrypted: true)
- `micro_hes/src/common_business/basic_station/module/navigation_bar/basic_station_navigation_bar_logic.dart`: `getSiteWifiInfo` @0x27db43c (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::getSiteWifiInfoRequest`, `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::getSiteWifiInfo`, `charging/ui/page/device/main/sitation_energy_system/station_home_settings/system_wifi_info/system_wifi_info_logic.dart::getSiteWifiInfo`, `charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart::getSiteWifiInfo`, `device/src/station_setting/controller/common_station_wifi/page/device_wifi_info_setting_controller.dart::_syncStatePageOnDone`, `device/src/station_setting/controller/common_station_wifi/page/device_wifi_info_setting_controller.dart::onReady`, `device/src/station_setting/controller/common_station_wifi/page/wifi_management_controller.dart::_syncStatePageOnDone`, `device/src/station_setting/controller/common_station_wifi/page/wifi_management_controller.dart::onReady`, `device/src/station_setting/controller/common_station_wifi/page/wifi_management_page.dart::didPopNext`, `flutter_charging_beginning/beginning/state_cards/add_devices/select_power_device/select_power_device_controller.dart::_startWifiRefresh`, `micro_hes/src/a17e2/station/home/base_station_logic.dart::_updateWeakWifiInfo`, `micro_hes/src/a17ex/station_setting/device_wifi_info_controller.dart::_syncStatePageOnDone`, `micro_hes/src/a17ex/station_setting/device_wifi_info_controller.dart::onReady`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
