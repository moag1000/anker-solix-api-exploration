> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# update_site

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/site/update_site`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x30c76c0`
(literal also at 3 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `device/src/station_setting/controller/common_station_name/station_name_view_model.dart @0x2cb53ec` |
| `site_name` | ? | ? | ? | `device/src/station_setting/controller/common_station_name/station_name_view_model.dart @0x2cb53ec` |
| `path` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/rename_device/rename_device_controller.dart @0x47a6694` |
| `method` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/rename_device/rename_device_controller.dart @0x47a6694` |
| `param` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/rename_device/rename_device_controller.dart @0x47a6694` |

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

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
