> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# platform_set_user_region_param

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v2/platform_set_user_region_param`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/main/sitation_energy_system/station_home_settings/advanced_setting/grid_setting_logic.dart @0x3facb54`
(literal also at 4 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `path` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/settings/system_config/system_config_controller.dart @0x32558c0` |
| `method` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/settings/system_config/system_config_controller.dart @0x32558c0` |
| `param` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/settings/system_config/system_config_controller.dart @0x32558c0` |

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

- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/advanced_setting/grid_setting_logic.dart`: `_setEnwgSwitch` @0x3fac850 (encryptionRequestHttp; encrypted: true)
- `device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart`: `updateCloudSetting` @0x47c84f0 (encryptionRequestHttp; encrypted: true)
- `flutter_charging_beginning/beginning/state_cards/settings/system_config/system_config_controller.dart`: `<anonymous closure> in SystemConfigController::updateCountryCodeByCloud` @0x32558c0 (URL literal only, no `*Http*` call)
- `settings/src/common/page/grid_param_setting/grid_param_setting_controller.dart`: `updateCloudSetting` @0x3a57130 (encryptionRequestHttp; encrypted: true)
- `settings/src/common/page/grid_param_setting/grid_protect_setting_controller.dart`: `saveProtectParam` @0x3a59ff0 (encryptionRequestHttp; encrypted: true)

Called from: `charging/ui/page/device/main/sitation_energy_system/station_home_settings/advanced_setting/grid_setting_logic.dart::onEnwg14aSwitchChanged`, `device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart::setGridInfo`, `settings/src/common/page/grid_param_setting/grid_param_setting_controller.dart::setGridInfo`, `settings/src/common/page/grid_param_setting/grid_protect_setting_controller.dart::handleSave`

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
