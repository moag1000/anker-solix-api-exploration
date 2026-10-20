> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# delete_site_devices

## Purpose

Removes devices from a site: `RemoveStationDevicesLogic::deleteSiteDevice`, `AddDevicesLogic::deleteGroup`, `ManageDevicesLogic::deleteSiteDevice`, `StationHomeInfoLogic` (delete-PPS closure) and `SiteLogic::_deleteGroupDevices` build the body and call `deleteSitePPSRequest`.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/site/delete_site_devices` (asm-traced): URL string at `http_request_repository_impl.dart @0x30c5f30`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x30c5f28`, in `HttpRequestControllerImpl::deleteSitePPSRequest` (`http_request_repository_impl.dart @0x30c5eb0`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The builder `deleteSitePPSRequest` (`http_request_repository_impl.dart @0x30c5eb0`) has no map literal; the five callers build the body, with different key sets.

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | yes | | all five callers: `remove_station_devices_logic.dart` key `@0x3450a64`, store `@0x3450a84`; `add_devices_logic.dart` key `@0x3fa089c`, store `@0x3fa08e0` (empty-string default); `manage_devices_logic.dart` `[]=` key `@0x3fbcc60`; `station_home_info_logic.dart` key `@0x30c5cb4`; `site_logic.dart` key `@0x3fa1528`, store `@0x3fa1570` (empty-string default) |
| `device_sn` | list | yes | | key `@0x3450a88` (`remove_station_devices_logic.dart`, store `@0x3450a98`); `add_devices_logic.dart` key `@0x3fa0904`; `manage_devices_logic.dart` `[]=` key `@0x3fbccbc`; `station_home_info_logic.dart` key `@0x30c5d0c`; `site_logic.dart` key `@0x3fa1594`; the lists are built as growable lists (`_GrowableList`) |
| `hardware_info` | ? | optional | | `manage_devices_logic.dart` `[]=` key `@0x3fbccec`, added when a list parameter has elements (`cbz` `@0x3fbccd8`) |

## `param_type`/`cmd`

n/a

## Response model (link)

None for most callers: the success callbacks of `remove_station_devices_logic.dart @0x3450b00`, `station_home_info_logic.dart @0x30c5f74` load no argument. The two delete-group callers parse the response map by key: `add_devices_logic.dart @0x3fa0a00` and `site_logic.dart @0x3fa0d30` read the key `del_device_infos` (a list) and each element's `device_sn`; `manage_devices_logic.dart @0x3fbd7f8` reads other keys (`update_user_power_limit`). No model class is parsed (no `fromJson` call in these callbacks).

## Response

Keys read by the callers: `del_device_infos` (list of maps with `device_sn`), `update_user_power_limit` (read by `manage_devices_logic.dart @0x3fbd7f8`): the callback checks the key for null (`cmp w0, NULL` `@0x3fbd840`) and compares the value with the boolean `true` through an equality call (`r16 = true` `@0x3fbd8ac`, `tbnz w0, #4` `@0x3fbd8c4`), so the app treats it as a bool flag and continues only when it is `true`.

## Example request/response

Request, synthesized (key set of `site_logic.dart`; types of `site_id` unresolved)

```json
{"site_id": "<site_id>", "device_sn": ["<device_sn>"]}
```

Response keys: see Response; no capture.

## Errors seen

None traced. The `manage_devices_logic.dart @0x3fbd7f8` callback has a 64-bit compare with 16189 (`@0x3fbd9a0`) that is a class-id test, not an error code; the other callbacks show shared dialogs. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `deleteSitePPSRequest` @0x30c5eb0 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::deleteSitePPSRequest`
- `charging/ui/page/device/a17c0/remove_station_devices/remove_station_devices_logic.dart::deleteSiteDevice`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/add_devices/add_devices_logic.dart::deleteGroup`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/manage_devices/manage_devices_logic.dart::deleteSiteDevice`
- `charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart::deleteSitePPS`
- `charging/ui/page/green_energy/site/site_logic.dart::_deleteGroupDevices`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- Type of `site_id` in all callers and the full key set of the `manage_devices_logic.dart` variant (it also sends `hardware_info`, and logs `isOnlyDeleteC0` and `selectedDeleteDeviceSNList` strings in the same function). Header stays string-only.
- Whether `device_sn` elements are always Strings: the lists are built dynamically. — traced 2026-10-20: two callers build the list with the type argument `<String>` (`AddDevicesLogic.deleteGroup`, `charging/ui/page/device/main/sitation_energy_system/station_home_settings/add_devices/add_devices_logic.dart @0x3fa09e4`, and `SiteLogic._deleteGroupDevices`, `charging/ui/page/green_energy/site/site_logic.dart @0x3fa167c`); the other three callers (`charging/ui/page/device/a17c0/remove_station_devices/remove_station_devices_logic.dart @0x3450ae4`, `charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart @0x30c5da0`, `charging/ui/page/device/main/sitation_energy_system/station_home_settings/manage_devices/manage_devices_logic.dart @0x3fbcd34`) were not checked for element types

## Device-tested by

none
