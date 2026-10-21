> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# list_user_devices

## Purpose

Lists the devices of a user that can be added to a site, filtered by device model: the device-selection logics of the A1782, A17B1 and A17C0 pages, `AddDevicesLogic` (`getUserDeviceList`, `deleteGroup`) and the station home logics call `getUserPPSDevice`.

## Upstream name

`user_devices` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/site/list_user_devices` (asm-traced): URL string at `http_request_repository_impl.dart @0x23f43a4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x23f439c`, in `HttpRequestControllerImpl::getUserPPSDevice` (`http_request_repository_impl.dart @0x23f42a4`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is a 1-pair map literal typed `<String, List<String>>` (type arguments `@0x23f4354`) built in `getUserPPSDevice` (`http_request_repository_impl.dart @0x23f42a4`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_models` | list | yes | `["<device_model>"]` | key `@0x23f4300`, value store `@0x23f4330`; a null parameter (`cmp w1, NULL` `@0x23f4310`) is replaced by an empty `<String>` growable list (`_GrowableList` `@0x23f4320`); the map type says the elements are Strings |

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::UserSiteDevicePPSModel` (`data/models.json` key; fields on [`models/connectivity.md`](../../../models/connectivity.md#usersitedeviceppsmodel)), parsed in the builder's success closure `http_request_repository_impl.dart @0x23f43e8` by `UserSiteDevicePPSModel.fromJson`.

## Response

Top-level keys of the model (from `data/models.json`): `pps_list`, `solarbank_list`, `solarbank_pps_list`, `solar_list`, `powerpanel_list`, `smartplug_list`, `combiner_box_list`, `charging_pile_list` (Lists), `hardware_list` and `grid_list` (`List<SiteDeviceModel>`).

## Example request/response

Request, synthesized (decrypted body as built by `getUserPPSDevice`)

```json
{"device_models": ["<device_model>"]}
```

Response keys: see Response; no capture.

## Errors seen

None traced: the builder passes the `postJML` failure template (`@0x226824c`) to the callers' failure callbacks, which were not read. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getUserPPSDevice` @0x23f42a4 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getUserPPSDevice`
- `charging/ui/page/device/a1782/station/add_devices/a1782_add_devices_logic.dart::getUserDeviceList`
- `charging/ui/page/device/a17b1/a17b1select_devices/a17b1select_devices_logic.dart::_getUserDeviceList`
- `charging/ui/page/device/a17c0/select_station/select_station_logic.dart::getUserDeviceList`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/add_devices/add_devices_logic.dart::deleteGroup`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/add_devices/add_devices_logic.dart::getUserDeviceList`
- `charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart::getUserPPSDeviceList`
- `charging/ui/page/device/main/station_device_home/station_main_page/station_main_page_logic.dart::getUserPPSDeviceList`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta. The model `UserSiteDevicePPSModel` is `≤3.18.0` in `data/models.json`.

## Known unknowns

- Which device models each caller sends: the list is a parameter; the nine callers were not followed. — traced 2026-10-20: three callers pass the model list as the named argument `productCodeList` (`A1782AddDevicesLogic.getUserDeviceList`, `charging/ui/page/device/a1782/station/add_devices/a1782_add_devices_logic.dart @0x28b97b4`; `A17B1SelectDevicesLogic._getUserDeviceList` `charging/ui/page/device/a17b1/a17b1select_devices/a17b1select_devices_logic.dart @0x28b3364`; `AddDevicesLogic.getUserDeviceList` `charging/ui/page/device/main/sitation_energy_system/station_home_settings/add_devices/add_devices_logic.dart @0x349a740`) or none; the list contents were not followed
- Whether an empty `device_models` list (the null fallback) returns all devices: server behaviour, not derivable from the app.
- Failure handling in the callers was not read. — traced 2026-10-20: the call sites pass no `fail` closure among their named arguments: `A1782AddDevicesLogic.getUserDeviceList` (`charging/ui/page/device/a1782/station/add_devices/a1782_add_devices_logic.dart @0x28b97bc`): named arguments `productCodeList`, `showLoading`; `A17B1SelectDevicesLogic._getUserDeviceList` (`charging/ui/page/device/a17b1/a17b1select_devices/a17b1select_devices_logic.dart @0x28b336c`): named arguments `productCodeList`; `SelectStationLogic.getUserDeviceList` (`charging/ui/page/device/a17c0/select_station/select_station_logic.dart @0x28c2b2c`): named arguments `showLoading`; `StationMainPageLogic.getUserPPSDeviceList` (`charging/ui/page/device/main/station_device_home/station_main_page/station_main_page_logic.dart @0x23f41a4`): named arguments `showLoading`; `StationHomeInfoLogic.getUserPPSDeviceList` (`charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart @0x2c1fcd0`): no named argument; `AddDevicesLogic.getUserDeviceList` (`charging/ui/page/device/main/sitation_energy_system/station_home_settings/add_devices/add_devices_logic.dart @0x349a748`): named arguments `productCodeList`, `showLoading`; `AddDevicesLogic.Null <anonymous closure>` (`charging/ui/page/device/main/sitation_energy_system/station_home_settings/add_devices/add_devices_logic.dart @0x3fa0cbc`): no named argument. Failure then falls to the callee's default or to the awaiting code, neither of which was read

## Device-tested by

none
