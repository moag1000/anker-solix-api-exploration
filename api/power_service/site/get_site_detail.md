> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_site_detail

## Purpose

Reads the device lists of a site: the station home, add/manage-devices, A17C0 select-station and PPS recharge logics call `getGreenPPSSiteDetail` and `getStationDetail`; the beginning flow reads it through the IoT kit (`RenameSiteController::loadName`).

## Upstream name

`site_detail` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/site/get_site_detail` (asm-traced) at the senders that load a `Method` object next to the URL string (pool entry `pp+0xa7e0`, `Method.post`):

- `HttpRequestControllerImpl::getGreenPPSSiteDetail` (`http_request_repository_impl.dart @0x28f4c38`): URL string `@0x28f4cec`, method object `Method.post` (`pp+0xa7e0`) `@0x28f4ce4`.
- `HttpRequestControllerImpl::getStationDetail` (`http_request_repository_impl.dart @0x23f69d8`): URL string `@0x23f6a90`, method object `Method.post` (`pp+0xa7e0`) `@0x23f6a88`.

The IoT-kit sender `RenameSiteController::<anonymous closure> in loadName` (`rename_device_controller.dart @0x47add6c`) puts the path (`@0x47addd0`, `"/power_service/v1/site/get_site_detail"`), the string literal `"POST"` (`@0x47adde8`) and a `param` map into a command map for `akIoTKitManager.handle` (`@0x47ade88`); the method there is a string literal, not a `Method` pool object.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

All three senders type their `site_id` map `<String, String>`, so the value is a String.

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | string | yes | `"<site_id>"` | key `charging/http/http_request_repository_impl.dart @0x28f4c8c`; `getGreenPPSSiteDetail` (`http_request_repository_impl.dart @0x28f4c38`): key `@0x28f4c8c`, store `@0x28f4c9c`, type arguments `@0x28f4ca0`; `getStationDetail` (`@0x23f69d8`): key `@0x23f6a30`, store `@0x23f6a40`, type arguments `@0x23f6a44`; IoT-kit sender: `param` map key `flutter_charging_beginning/beginning/state_cards/rename_device/rename_device_controller.dart @0x47ade0c`, store `@0x47ade24` (`field_f` of the controller), type arguments `@0x47ade28` |

## `param_type`/`cmd`

n/a

## Response model (link)

Per sender. `getGreenPPSSiteDetail`: `charging::GreenPPSSiteDetailModel` (`data/models.json` key; fields on [`models/energy.md`](../../../models/energy.md#greenppssitedetailmodel)), parsed in the success closure `http_request_repository_impl.dart @0x28f4d30` (`GreenPPSSiteDetailModel.fromJson`, then `jsonEncode` and `setGreenPPSSiteDetail`). `getStationDetail`: `charging::DeviceListModel` (`data/models.json` key; fields on [`models/device.md`](../../../models/device.md#devicelistmodel)), parsed in `@0x23f6ad4` (`DeviceListModel.fromJson` resolves to `charging/model/device_list_model.dart`). IoT-kit sender: not read (its result goes through `handle`).

## Response

Top-level keys of `GreenPPSSiteDetailModel` (from `data/models.json`): `site_info` (`SiteInfoModel`), `pps_list`, `solar_list`, `solarbank_list`, `powerpanel_list` (Lists). Top-level keys of `charging::DeviceListModel`: `site_info` (`SiteInfoModel`), `pps_list`, `solar_list`, `solarbank_list`, `combiner_box_list`, `solarbank_pps_list`, `combineBox_List`, `smartplug_list`, `hardware_list` and `grid_list` (`List<ManageDeviceModel>`), `charging_pile_list`, `home_backup_system_list`.

## Example request/response

Request, synthesized

```json
{"site_id": "<site_id>"}
```

Response keys: see Response; no capture.

## Errors seen

None traced. The builders pass the `postJML` failure template (`@0x226824c`); the callers' failure callbacks were not read. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getGreenPPSSiteDetail` @0x28f4c38 (encryptionRequestHttp; encrypted: true); `getStationDetail` @0x23f69d8 (encryptionRequestHttp; encrypted: true)
- `flutter_charging_beginning/beginning/state_cards/rename_device/rename_device_controller.dart`: `<anonymous closure> in RenameSiteController::loadName` @0x47add6c (URL literal only, no `*Http*` call; sends in the same function (`AKIoTKitManagerImpl::handle`); resolved from the URL literal at `flutter_charging_beginning/beginning/state_cards/rename_device/rename_device_controller.dart @0x47addd0` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

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

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta. `tools/out/diff_3.18.0_3.24.3.md` (changed params) lists `method`, `param.site_id` and `path` as added: these are the key names of the IoT-kit command map of `RenameSiteController::loadName`.

## Known unknowns

- The response handling of the IoT-kit sender (`loadName`): not read. Header stays string-only. — not traced 2026-10-20 in this pass (IoT-kit sender `loadName`); the reason given in the bullet stands
- Which sender each of the 15 callers uses was not mapped. — not traced 2026-10-20 in this pass (15 callers); the reason given in the bullet stands
- The element classes of the list keys in both models. — reclassified: server (not visible in the app: the models keep the lists untyped)

## Device-tested by

none
