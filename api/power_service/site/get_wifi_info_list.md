> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_wifi_info_list

## Purpose

Reads the WiFi info of a site's devices: the station WiFi settings pages (`DeviceWifiInfoSettingController`, `WifiManagementController`, `DeviceWifiInfoController`), the add-device flow (`SelectPowerDeviceController::_fetchSiteWifiSignal`), the basic-station navigation bar and the repository `getSiteWifiInfoRequest` send `site_id`.

## Upstream name

`wifi_list` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/site/get_wifi_info_list` (asm-traced) at the senders that load a `Method` object next to the URL string (pool entry `pp+0xa7e0`, `Method.post`):

- `HttpRequestControllerImpl::getSiteWifiInfoRequest` (`http_request_repository_impl.dart @0x238507c`): URL string `@0x2385100`, method object `Method.post` (`pp+0xa7e0`) `@0x23850f8`.
- `DeviceWifiInfoSettingController::fetchDeviceWifiInfo` (`device_wifi_info_setting_controller.dart @0x29e6fd0`): URL string `@0x29e70a8`, method object `Method.post` (`pp+0xa7e0`) `@0x29e70a0`.
- `WifiManagementController::fetchDeviceWifiInfo` (`wifi_management_controller.dart @0x29eb244`): URL string `@0x29eb31c`, method object `Method.post` (`pp+0xa7e0`) `@0x29eb314`.
- `SelectPowerDeviceController::_fetchSiteWifiSignal` (`select_power_device_controller.dart @0x29ecfb4`): URL string `@0x29ed090`, method object `Method.post` (`pp+0xa7e0`) `@0x29ed088`.
- `DeviceWifiInfoController::fetchDeviceWifiInfo` (`device_wifi_info_controller.dart @0x29ec464`): URL string `@0x29ec53c`, method object `Method.post` (`pp+0xa7e0`) `@0x29ec534`.
- `BasicStationNavigationBarLogic::getSiteWifiInfo` (`basic_station_navigation_bar_logic.dart @0x27db43c`): URL string `@0x27db61c`, method object `Method.post` (`pp+0xa7e0`) `@0x27db614`.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Six senders; each sends `site_id` only.

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | string | yes | `"<site_id>"` | key `device/src/station_setting/controller/common_station_wifi/page/device_wifi_info_setting_controller.dart @0x29e7040`; typed maps: `DeviceWifiInfoSettingController::fetchDeviceWifiInfo` (`device/src/station_setting/controller/common_station_wifi/page/device_wifi_info_setting_controller.dart @0x29e6fd0`): `<String, String>` (`@0x29e705c`), key `@0x29e7040`, store `@0x29e7058`; `WifiManagementController::fetchDeviceWifiInfo` (`device/src/station_setting/controller/common_station_wifi/page/wifi_management_controller.dart @0x29eb244`): `<String, String>` (`@0x29eb2d0`), key `@0x29eb2b4`, store `@0x29eb2cc`; `SelectPowerDeviceController::_fetchSiteWifiSignal` (`flutter_charging_beginning/beginning/state_cards/add_devices/select_power_device/select_power_device_controller.dart @0x29ecfb4`): `<String, String>` (`@0x29ed058`), key `@0x29ed03c`, store `@0x29ed054`; `DeviceWifiInfoController::fetchDeviceWifiInfo` (`micro_hes/src/a17ex/station_setting/device_wifi_info_controller.dart @0x29ec464`): `<String, String>` (`@0x29ec4f0`), key `@0x29ec4d4`, store `@0x29ec4ec`; `BasicStationNavigationBarLogic::getSiteWifiInfo` (`micro_hes/src/common_business/basic_station/module/navigation_bar/basic_station_navigation_bar_logic.dart @0x27db43c`): `<String, String?>` (`@0x27db5cc`), key `@0x27db528`, store `@0x27db5a8` |
| `site_id` | ? | yes |  | key `charging/http/http_request_repository_impl.dart @0x238c818`; `HttpRequestControllerImpl::getSiteWifiInfoRequest` (`http_request_repository_impl.dart @0x238507c`): key `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart @0x2384f24`, store `@0x2384f50` (`field_7` of an Rx value); the map literal carries no printed type arguments |

## `param_type`/`cmd`

n/a

## Response model (link)

Per sender. `getSiteWifiInfoRequest`: `SiteWifiInfoModel` from `charging/model/site_wifi_info_model.dart` (`data/models.json` key `charging::SiteWifiInfoModel`; fields on [`models/connectivity.md`](../../../models/connectivity.md#sitewifiinfomodel)), parsed in `http_request_repository_impl.dart @0x2385144`. `WifiManagementController` (`device/src/station_setting/controller/common_station_wifi/page/wifi_management_controller.dart @0x29e7c70`), `SelectPowerDeviceController` (`flutter_charging_beginning/beginning/state_cards/add_devices/select_power_device/select_power_device_controller.dart @0x29ed0cc`) and `BasicStationNavigationBarLogic` (`micro_hes/src/common_business/basic_station/module/navigation_bar/basic_station_navigation_bar_logic.dart @0x27db714`): `base_service::SiteWifiInfoModel` (`base_service/bean/model/init_flow/site_wifi_info_model.dart`, `data/models.json` key). `DeviceWifiInfoSettingController` (`device/src/station_setting/controller/common_station_wifi/page/device_wifi_info_setting_controller.dart @0x29e71f4`) and `DeviceWifiInfoController` (`micro_hes/src/a17ex/station_setting/device_wifi_info_controller.dart @0x29eb474`): no model class; they read the key `wifi_info_list` (`@0x29e72e0`).

## Response

Top-level keys of both `SiteWifiInfoModel` classes (from `data/models.json`): `wifi_info_list` (List) and `hardware_list` (List).

## Example request/response

Request, synthesized

```json
{"site_id": "<site_id>"}
```

Response keys: see Response; no capture.

## Errors seen

None traced. The failure callbacks of the controllers log `"load data failed: "` and hide the loading; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getSiteWifiInfoRequest` @0x238507c (encryptionRequestHttp; encrypted: true)
- `device/src/station_setting/controller/common_station_wifi/page/device_wifi_info_setting_controller.dart`: `fetchDeviceWifiInfo` @0x29e6fd0 (encryptionRequestHttp; encrypted: true)
- `device/src/station_setting/controller/common_station_wifi/page/wifi_management_controller.dart`: `fetchDeviceWifiInfo` @0x29eb244 (encryptionRequestHttp; encrypted: true)
- `flutter_charging_beginning/beginning/state_cards/add_devices/select_power_device/select_power_device_controller.dart`: `_fetchSiteWifiSignal` @0x29ecfb4 (encryptionRequestHttp; encrypted: true)
- `micro_hes/src/a17ex/station_setting/device_wifi_info_controller.dart`: `fetchDeviceWifiInfo` @0x29ec464 (encryptionRequestHttp; encrypted: true)
- `micro_hes/src/common_business/basic_station/module/navigation_bar/basic_station_navigation_bar_logic.dart`: `getSiteWifiInfo` @0x27db43c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getSiteWifiInfoRequest`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::getSiteWifiInfo`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/system_wifi_info/system_wifi_info_logic.dart::getSiteWifiInfo`
- `charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart::getSiteWifiInfo`
- `device/src/station_setting/controller/common_station_wifi/page/device_wifi_info_setting_controller.dart::_syncStatePageOnDone`
- `device/src/station_setting/controller/common_station_wifi/page/device_wifi_info_setting_controller.dart::onReady`
- `device/src/station_setting/controller/common_station_wifi/page/wifi_management_controller.dart::_syncStatePageOnDone`
- `device/src/station_setting/controller/common_station_wifi/page/wifi_management_controller.dart::onReady`
- `device/src/station_setting/controller/common_station_wifi/page/wifi_management_page.dart::didPopNext`
- `flutter_charging_beginning/beginning/state_cards/add_devices/select_power_device/select_power_device_controller.dart::_startWifiRefresh`
- `micro_hes/src/a17e2/station/home/base_station_logic.dart::_updateWeakWifiInfo`
- `micro_hes/src/a17ex/station_setting/device_wifi_info_controller.dart::_syncStatePageOnDone`
- `micro_hes/src/a17ex/station_setting/device_wifi_info_controller.dart::onReady`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- Type of `site_id` in `getSiteWifiInfoRequest` (Rx field with no printed map type). Header stays string-only. — attempted 2026-10-20 (two-hop not readable: the three callers (`StationHomeInfoLogic.getSiteWifiInfo`, `StationEnergySystemLogic.getSiteWifiInfo`, `SystemWifiInfoLogic.getSiteWifiInfo`) read an Rx field with no default or declared type. Header stays string-only)
- Why two `SiteWifiInfoModel` classes (charging and base_service) read the same answer. — reclassified: server (the reason for two model classes is not recorded in the app)
- The element structure of `wifi_info_list` and `hardware_list`.

## Device-tested by

none
