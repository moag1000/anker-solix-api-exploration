> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_site_detail

## Purpose

<!-- TODO -->

## Upstream name

`site_detail` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/site/get_site_detail`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x23f6a90`
(literal also at 2 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x28f4c38` |
| `path` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/rename_device/rename_device_controller.dart @0x47add6c` |
| `method` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/rename_device/rename_device_controller.dart @0x47add6c` |
| `param.site_id` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/rename_device/rename_device_controller.dart @0x47add6c` |

Rows are the union over 3 senders; `source` is the first sender that sets the key.

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

- `charging/http/http_request_repository_impl.dart`: `getGreenPPSSiteDetail` @0x28f4c38 (encryptionRequestHttp; encrypted: true); `getStationDetail` @0x23f69d8 (encryptionRequestHttp; encrypted: true)
- `flutter_charging_beginning/beginning/state_cards/rename_device/rename_device_controller.dart`: `<anonymous closure> in RenameSiteController::loadName` @0x47add6c (URL literal only, no `*Http*` call; sends in the same function (SDK `handle`))

Called from:

- `balcony/src/ae100/settings/ae100_remove_device_controller.dart::_checkDeviceBindSiteStatus`
- `charging/http/http_request_repository.dart::getGreenPPSSiteDetail`
- `charging/http/http_request_repository.dart::getStationDetail`
- `charging/ui/page/device/a1782/station/add_devices/a1782_add_devices_logic.dart::getUserDeviceList`
- `charging/ui/page/device/a17c0/select_station/select_station_logic.dart::getC0SeriesDevices`
- `charging/ui/page/device/a17c0/select_station/select_station_logic.dart::getCXSeriesDevices`
- `charging/ui/page/device/a17c5/ai_mode_condition/ai_mode_condition_logic.dart::getSmartPlugSetCount`
- `charging/ui/page/device/greenpower/recharge/recharge_logic.dart::getGreenPPSSite`
- `charging/ui/page/device/main/sitation_energy_mian/energy_pps/controller/energy_pps_controller.dart::getGreenPPSSite`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/add_devices/add_devices_logic.dart::getUserDeviceList`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/manage_devices/manage_devices_logic.dart::getSiteDevices`
- `charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart::getSolarAndPPSRes`
- `charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart::getStationInfo`
- `charging/ui/page/device/main/station_device_home/station_main_page/station_main_page_logic.dart::getGreenPPSSite`
- `charging/ui/page/device/main/station_device_home/station_set_time/station_set_time_logic.dart::getGreenPPSSite`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
