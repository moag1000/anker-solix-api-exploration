> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# SceneInfoModel

## Purpose

Carries the scene (energy flow) document of a site as the IoT kit sees it: solarbank, backup, grid, diesel, smart plug and charging pile information, power values, the feature switches and the hardware list.

## Dart class + file

`SceneInfoModel` (`fromJson @0x233f13c`), file `base_service/ak_iot_kit/business/basic/model/scene_info_model.dart` (package `base_service`). The same file holds 20 element classes, listed below with their `fromJson` address and key count; their keys are not expanded on this page.

## Fields

Column `since`: `≤3.18.0` means the key is present in 3.18.0 (earlier versions not checked), `3.24.3` means first seen in 3.24.3. Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Nullability and Dart types come from `tools/model_fields.py` (`data/models.json`); `unknown` means the extractor could not resolve the element type.

### SceneInfoModel

`fromJson` `scene_info_model.dart @0x233f13c`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `solarbank_info` | `SolarBankInfo?` | yes | ≤3.18.0 | `scene_info_model.dart @0x233f180` |
| `home_backup_system_info` | `SolarBankInfo?` | yes | ≤3.18.0 | `scene_info_model.dart @0x233f21c` |
| `grid_info` | `GridInfo?` | yes | ≤3.18.0 | `scene_info_model.dart @0x233f2b8` |
| `diesel_info` | `DieselInfo?` | yes | ≤3.18.0 | `scene_info_model.dart @0x233f354` |
| `home_load_power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x233f3f0` |
| `ems_mode` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x233f478` |
| `ems_mode_power` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x233f500` |
| `error_code` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x233f588` |
| `function_switch` | `FunctionSwitch` | no | ≤3.18.0 | `scene_info_model.dart @0x233f62c` |
| `site_id` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x233f790` |
| `self_test_status` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x233f818` |
| `ct2_self_test_status` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x233f8a0` |
| `init_status` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x233f928` |
| `use_time_type` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x233f9b0` |
| `energy_flow_bits` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x233fa38` |
| `self_test_fault_bits` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x233fac0` |
| `off_grid_info` | `OffGridInfo?` | yes | ≤3.18.0 | `scene_info_model.dart @0x233fb48` |
| `power_site_type` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x233fbf4` |
| `switch_0w` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x233fc7c` |
| `style_id` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x233fd04` |
| `smart_plug_info` | `SmartPlugInfo?` | yes | 3.24.3 | `scene_info_model.dart @0x233fd8c` |
| `feature_switch` | `FeatureSwitch?` | yes | 3.24.3 | `scene_info_model.dart @0x233fe28` |
| `charging_pile_info` | `ChargingPileInfo?` | yes | 3.24.3 | `scene_info_model.dart @0x233fec4` |
| `aiems_profit` | `AiemsProfit?` | yes | 3.24.3 | `scene_info_model.dart @0x233ff60` |
| `branch_info` | `unknown` | yes | ≤3.18.0 | `scene_info_model.dart @0x233fffc` |
| `other_load_power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2340050` |
| `branch_info` | `unknown` | not determined | ≤3.18.0 | `scene_info_model.dart @0x23400f0` |
| `ats_load_power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2340114` |
| `branch_info` | `unknown` | not determined | ≤3.18.0 | `scene_info_model.dart @0x23401b4` |
| `branch_list` | `unknown` | yes | ≤3.18.0 | `scene_info_model.dart @0x23401d8` |
| `branch_info` | `unknown` | not determined | ≤3.18.0 | `scene_info_model.dart @0x234023c` |
| `branch_list` | `unknown` | not determined | ≤3.18.0 | `scene_info_model.dart @0x2340260` |
| `heat_pump_connected` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x23402c0` |
| `other_load_power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x234032c` |
| `custom_charging_type` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x23403b4` |
| `is_show_pv` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x234043c` |
| `price_level` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x23404a8` |
| `hardware_info` | `HardwareInfo?` | yes | 3.24.3 | `scene_info_model.dart @0x2340530` |
| `grid_ov_auto_reduce_capability` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x23405cc` |
| `reason_code` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x2340654` |

Element classes of the same file (keys not expanded here):

| class | `fromJson` | keys | since (first key) |
|---|---|---|---|
| `AiemsProfit` | `fromJson @0x2340ba0` | 5 | 3.24.3 |
| `BackupInfo` | `fromJson @0x2346128` | 3 | ≤3.18.0 |
| `BmsList` | `fromJson @0x23479d0` | 5 | ≤3.18.0 |
| `Branch` | `fromJson @0x2348008` | 7 | ≤3.18.0 |
| `ChargingPileInfo` | `fromJson @0x2340e6c` | 1 | 3.24.3 |
| `ChargingPileList` | `fromJson @0x2341060` | 9 | 3.24.3 |
| `DieselInfo` | `fromJson @0x2343dc8` | 9 | ≤3.18.0 |
| `DieselList` | `fromJson @0x23443c8` | 17 | ≤3.18.0 |
| `FeatureSwitch` | `fromJson @0x2341574` | 28 | 3.24.3 |
| `FunctionSwitch` | `fromJson @0x23431cc` | 28 | ≤3.18.0 |
| `GridInfo` | `fromJson @0x2344ce4` | 5 | ≤3.18.0 |
| `GridList` | `fromJson @0x23450c4` | 7 | ≤3.18.0 |
| `HardwareInfo` | `fromJson @0x2340740` | 1 | 3.24.3 |
| `HardwareItem` | `fromJson @0x2340934` | 4 | 3.24.3 |
| `OffGridInfo` | `fromJson @0x2342e48` | 6 | ≤3.18.0 |
| `PvList` | `fromJson @0x2347d9c` | 2 | ≤3.18.0 |
| `SmartPlugInfo` | `fromJson @0x234227c` | 2 | 3.24.3 |
| `SmartPlugList` | `fromJson @0x23424f8` | 17 | 3.24.3 |
| `SolarBankInfo` | `fromJson @0x23454c8` | 23 | ≤3.18.0 |
| `SolarbankList` | `fromJson @0x23463e4` | 38 | ≤3.18.0 |

The table shows some keys twice (`branch_info`, `branch_list`, `other_load_power`): the extractor records one row per read site; the `fromJson` reads those keys in more than one branch.

## Produced by

[`platform_get_site_scene`](../api/power_service/v2/site/platform_get_site_scene.md): `SceneInfoModel.fromJson` at `micro_hes/src/a17e2/station/home/base_station_logic.dart @0x2348a88`. The class is also used for the V1 site scene of the IoT kit (not described here).

## Consumed by

The micro HES (A17E2) station home (`base_station_logic.dart`); field-level use is not traced.

## Changed since 3.18.0

Keys with `since` 3.24.3 are new: `ems_mode_power`, `ct2_self_test_status`, `self_test_fault_bits`, `switch_0w`, `style_id`, `smart_plug_info`, `feature_switch`, `charging_pile_info`, `aiems_profit`, `heat_pump_connected`, `custom_charging_type`, `is_show_pv`, `price_level`, `hardware_info`, `grid_ov_auto_reduce_capability`, `reason_code`; the element classes `AiemsProfit`, `ChargingPileInfo`, `ChargingPileList`, `FeatureSwitch`, `HardwareInfo`, `HardwareItem`, `SmartPlugInfo` and `SmartPlugList` are new.

## Known unknowns

- The keys of the 20 element classes are in `data/models.json` but not described here.
- The value domains of the many integer keys (`ems_mode`, `use_time_type`, `power_site_type`, ...) are not decoded.
