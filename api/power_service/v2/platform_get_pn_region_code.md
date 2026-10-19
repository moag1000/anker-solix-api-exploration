> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# platform_get_pn_region_code

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v2/platform_get_pn_region_code`, method: not extracted by the inventory <!-- TODO -->; string-only: `base_service/view/grid/grid_param_util.dart @0x28f6080`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `product_code` | ? | ? | ? | `base_service/view/grid/grid_param_util.dart @0x28f5f1c` |
| `path` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/settings/power_plant_config_controller.dart @0x2b07c9c` |
| `method` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/settings/power_plant_config_controller.dart @0x2b07c9c` |
| `param` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/settings/power_plant_config_controller.dart @0x2b07c9c` |

Rows are the union over 2 senders; `source` is the first sender that sets the key.

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

- `base_service/view/grid/grid_param_util.dart`: `requestRegionCodes` @0x28f5f1c (encryptionRequestHttp; encrypted: true)
- `flutter_charging_beginning/beginning/state_cards/settings/power_plant_config_controller.dart`: `<anonymous closure> in PowerPlantConfigController::requestRegionCodes` @0x2b07c9c (URL literal only, no `*Http*` call)

Called from:

- `base_service/view/grid/choose_grid_view.dart::_fetchRegionCodes`
- `base_service/view/grid/choose_grid_view_v2.dart::_fetchRegionCodes`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/advanced_setting/grid_setting_logic.dart::_getGridSetting`
- `device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart::onReady`
- `settings/src/common/page/grid_param_setting/grid_param_setting_controller.dart::onReady`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
