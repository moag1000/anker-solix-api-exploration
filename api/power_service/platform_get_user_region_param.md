> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# platform_get_user_region_param

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v2/platform_get_user_region_param`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/main/sitation_energy_system/station_home_settings/advanced_setting/grid_setting_logic.dart @0x28f5cf8`
(literal also at 5 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `product_code` | ? | ? | ? | `device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart @0x2a4f638` |
| `identifier_id` | ? | ? | ? | `device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart @0x2a4f638` |
| `scenario_type` | ? | ? | ? | `device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart @0x2a4f638` |
| `grid_code_name` | ? | ? | ? | `device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart @0x2a4f638` |
| `country_code` | ? | ? | ? | `device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart @0x2a4f638` |
| `grid_code` | ? | ? | ? | `device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart @0x2a4f638` |
| `path` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/settings/system_config/system_config_controller.dart @0x3256434` |
| `method` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/settings/system_config/system_config_controller.dart @0x3256434` |
| `param` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/settings/system_config/system_config_controller.dart @0x3256434` |

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

- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/advanced_setting/grid_setting_logic.dart`: `_getGridSetting` @0x28f5bb8 (encryptionRequestHttp; encrypted: true)
- `device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart`: `<anonymous closure> in GridParamSettingController::showGridPicker` @0x390d94c (encryptionRequestHttp; encrypted: true); `getGridSetting` @0x2a4f638 (encryptionRequestHttp; encrypted: true)
- `flutter_charging_beginning/beginning/state_cards/settings/system_config/system_config_controller.dart`: `<anonymous closure> in SystemConfigController::updateCountryCodeByCloud` @0x3256434 (URL literal only, no `*Http*` call)
- `settings/src/common/page/grid_param_setting/grid_param_setting_controller.dart`: `<anonymous closure> in GridParamSettingController::showGridPicker` @0x3a58b94 (encryptionRequestHttp; encrypted: true); `getGridSetting` @0x29e4b8c (encryptionRequestHttp; encrypted: true)

Called from: `charging/ui/page/device/main/sitation_energy_system/station_home_settings/advanced_setting/grid_setting_logic.dart::onReady`, `device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart::_watchGridCode`, `device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart::onReady`, `device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart::showGridPicker`, `settings/src/common/page/grid_param_setting/grid_param_setting_controller.dart::onReady`, `settings/src/common/page/grid_param_setting/grid_param_setting_controller.dart::showGridPicker`

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
