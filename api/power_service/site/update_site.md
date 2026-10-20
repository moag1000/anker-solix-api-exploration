> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# update_site

## Purpose

Renames a site: the rename pages call `updateSiteNameInfoRequest` (`A17B1SystemInfoLogic::renameDevice`, `A5101SystemInfoLogic::renameDevice`, `SystemInfoLogic::resetSiteName`, `StationHomeInfoLogic::renameSiteName`, `HomeCenterLogic::renameSiteName`), `StationNameViewModel::requestRenameStation` and `StationNameController::requestRenameStation`; the beginning flow sends the same URL through the IoT kit (`RenameSiteController::save`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/site/update_site` (asm-traced) at the senders that load a `Method` object next to the URL string (pool entry `pp+0xa7e0`, `Method.post`):

- `HttpRequestControllerImpl::updateSiteNameInfoRequest` (`http_request_repository_impl.dart @0x30c7640`): URL string `@0x30c76c0`, method object `Method.post` (`pp+0xa7e0`) `@0x30c76b8`.
- `StationNameViewModel::requestRenameStation` (`station_name_view_model.dart @0x2cb53ec`): URL string `@0x2cb55a8`, method object `Method.post` (`pp+0xa7e0`) `@0x2cb55a0`.
- `StationNameController::requestRenameStation` (`station_name_controller.dart @0x2cd3010`): URL string `@0x2cd312c`, method object `Method.post` (`pp+0xa7e0`) `@0x2cd3124`.

The fourth sender `RenameSiteController::<anonymous closure> in save` (`rename_device_controller.dart @0x47a6694`) goes through `akIoTKitManager.handle` with the command map `{path: "/power_service/v1/site/update_site" (`@0x47a66f4`), method: "POST" (string literal `@0x47a670c`), param: ...}`; the method here is a string literal, not a `Method` pool object.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

All map-literal senders type their maps `<String, String>` (or `<String, String?>`), so the values are Strings.

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | string | yes | `"<site_id>"` | key `station_name_view_model.dart @0x2cb54d8` in `StationNameViewModel::requestRenameStation` (function `@0x2cb53ec`): store `@0x2cb5518`, null default `""`, map type `@0x2cb5534`; `StationNameController::requestRenameStation` (`station_name_controller.dart @0x2cd3010`): key `@0x2cd305c`, store `@0x2cd30a4`, null default `""`, map type `@0x2cd30b8`; caller-built bodies for `updateSiteNameInfoRequest`: `a17b1/system_info/system_info_logic.dart` key `@0x3d4582c` (null default `""` `@0x3d4580c`), `station_home_settings/system_info/system_info_logic.dart` key `@0x3ecbe2c`, `station_home_info_logic.dart` key `@0x30c74bc`, `home_center_logic.dart` key `@0x405ea04` (typed `<String, String?>`) |
| `site_name` | string | yes | `"<site_name>"` | `StationNameViewModel`: key `device/src/station_setting/controller/common_station_name/station_name_view_model.dart @0x2cb551c`, store `@0x2cb5530`; `StationNameController`: key `station_name_controller.dart @0x2cd30a8`, store `@0x2cd30b4`; `a17b1` caller key `a17b1/system_info/system_info_logic.dart @0x3d45840`, store `@0x3d45850`; `station_home_info_logic.dart` key `@0x30c7514` (trimmed text, `trim()` `@0x30c7544` area), `home_center_logic.dart` key `@0x405ea68` |

The SDK sender `RenameSiteController::save` passes `param` from a closure-context field (`flutter_charging_beginning/beginning/state_cards/rename_device/rename_device_controller.dart @0x47a6728`); its keys and types were not read.

## `param_type`/`cmd`

n/a

## Response model (link)

None for the map-literal senders: `StationNameViewModel`'s success callback `station_name_view_model.dart @0x2cb5a20` and `StationNameController`'s `station_name_controller.dart @0x2cd3210` load no argument and call no `fromJson` (they update an Rx value and refresh the site list). Not read for `updateSiteNameInfoRequest` (its builder passes forwarding templates) and for the SDK sender.

## Response

No response key is read in the resolved callbacks.

## Example request/response

Request, synthesized (decrypted body of the typed senders)

```json
{"site_id": "<site_id>", "site_name": "<site_name>"}
```

Response: none parsed in the resolved callbacks.

## Errors seen

Both rename failure callbacks (`station_name_view_model.dart @0x2cb57c8` and `station_name_controller.dart @0x2cd3174`) compare the code with a 32-bit compare, raw 44200, so 22100 (`@0x2cb57f4`, `@0x2cd3190`) and show the text key `stationTips`. Meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `updateSiteNameInfoRequest` @0x30c7640 (encryptionRequestHttp; encrypted: true)
- `device/src/station_setting/controller/common_station_name/station_name_view_model.dart`: `requestRenameStation` @0x2cb53ec (encryptionRequestHttp; encrypted: true)
- `flutter_charging_beginning/beginning/state_cards/rename_device/rename_device_controller.dart`: `<anonymous closure> in RenameSiteController::save` @0x47a6694 (URL literal only, no `*Http*` call; sends in the same function (`AKIoTKitManagerImpl::handle`); resolved from the URL literal at `flutter_charging_beginning/beginning/state_cards/rename_device/rename_device_controller.dart @0x47a66f4` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `micro_hes/src/common_business/basic_station/basic_station_setting/component/general_setting/station_name_controller.dart`: `requestRenameStation` @0x2cd3010 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::updateSiteNameInfoRequest`
- `charging/ui/page/device/a17b1/system_info/system_info_logic.dart::renameDevice`
- `charging/ui/page/device/a5101/setting/system_info/system_info_logic.dart::renameDevice`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/system_info/system_info_logic.dart::resetSiteName`
- `charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart::renameSiteName`
- `charging/ui/page/user/share_site/home_center/home_center_logic.dart::renameSiteName`
- `device/src/station_setting/controller/common_station_name/station_name_controller.dart::renameStation`
- `micro_hes/src/common_business/basic_station/basic_station_setting/component/general_setting/station_name_controller.dart::renameStation`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. `tools/out/diff_3.18.0_3.24.3.md` (changed params) lists `method`, `param` and `path` as added and `combination_type` as removed. `path`, `method` and `param` are the key names of the IoT-kit sender's command map (`rename_device_controller.dart @0x47a66ec`..`@0x47a6718`). The map-literal senders read here carry `site_id` and `site_name`; the string `combination_type` occurs in 3.24.3 only in `station_command.dart`, `init_flow_command.dart` and `add_device_model.dart` (grep of the asm tree), not in a rename sender.

3.18.0 body with `combination_type` (read in the 3.18.0 tree `blutter_output/asm`, addresses without `@` because the checker reads only the 3.24.3 tree): `RenameDeviceController::save` (`flutter_charging_beginning/beginning/state_cards/rename_device/rename_device_controller.dart`, address 0x3730ca4) built a 3-pair `<String, Object>` literal with `site_id` (0x3730cb0), `site_name` (0x3730cc4) and `combination_type` (0x3730cd8, value computed through two null tests and `BoxInt64Instr` 0x3730cfc / 0x3730d30) and posted it to this URL (0x3730dbc). No sender in the 3.24.3 tree writes `combination_type` for this URL.

## Known unknowns

- The keys of the SDK sender (`RenameSiteController::save`): its `param` map is built outside the closure. — not traced 2026-10-20 in this pass (`RenameSiteController::save` param map); the reason given in the bullet stands
- Whether the callers of `updateSiteNameInfoRequest` read the answer: its callbacks are forwarded to the callers' closures, which were not read (header stays string-only). — not traced 2026-10-20 in this pass (callers of `updateSiteNameInfoRequest`); the reason given in the bullet stands
- Why `combination_type` was dropped: the 3.18.0 body was not opened for this page. — reclassified: server (not visible in the app: the sender is traced above and nothing in it says why the key was dropped)

## Device-tested by

none
