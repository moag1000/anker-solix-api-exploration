> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# SceneInfoModel

## Contents

1. [Purpose](#purpose)
2. [Dart class + file](#dart-class--file)
3. [Fields](#fields)
   - [SceneInfoModel](#sceneinfomodel)
   - [AiemsProfit](#aiemsprofit)
   - [BackupInfo](#backupinfo)
   - [BmsList](#bmslist)
   - [Branch](#branch)
   - [ChargingPileInfo](#chargingpileinfo)
   - [ChargingPileList](#chargingpilelist)
   - [DieselInfo](#dieselinfo)
   - [DieselList](#diesellist)
   - [FeatureSwitch](#featureswitch)
   - [FunctionSwitch](#functionswitch)
   - [GridInfo](#gridinfo)
   - [GridList](#gridlist)
   - [HardwareInfo](#hardwareinfo)
   - [HardwareItem](#hardwareitem)
   - [OffGridInfo](#offgridinfo)
   - [PvList](#pvlist)
   - [SmartPlugInfo](#smartpluginfo)
   - [SmartPlugList](#smartpluglist)
   - [SolarBankInfo](#solarbankinfo)
   - [SolarbankList](#solarbanklist)
4. [Produced by](#produced-by)
5. [Consumed by](#consumed-by)
6. [Changed since 3.18.0](#changed-since-3180)
7. [Known unknowns](#known-unknowns)

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

Element classes of the same file (keys in the sections below):

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

The keys of the element classes (copied from `data/models.json`, the same extractor output as the main table; `since` is its `3.18.0` comparison):

#### AiemsProfit

`fromJson` `scene_info_model.dart @0x2340ba0`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `unit` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2340bc0` |
| `aiems_profit_total` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2340c48` |
| `show_percentage` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2340cd0` |
| `aiems_self_use_diff` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2340d3c` |
| `percentage` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2340dc4` |

#### BackupInfo

`fromJson` `scene_info_model.dart @0x2346128`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `start_time` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2346148` |
| `end_time` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23461d0` |
| `full_time` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2346258` |

#### BmsList

`fromJson` `scene_info_model.dart @0x23479d0`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `bms_sn` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23479f0` |
| `temperature` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2347a78` |
| `charge_discharge` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2347b00` |
| `soc` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2347b88` |
| `heating_status` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2347c10` |

#### Branch

`fromJson` `scene_info_model.dart @0x2348008`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `icon_name` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x234803c` |
| `icon_url` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23480e0` |
| `remark` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2348180` |
| `name` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2348220` |
| `id` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23482bc` |
| `power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x234835c` |
| `merge_branche` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23483f8` |

#### ChargingPileInfo

`fromJson` `scene_info_model.dart @0x2340e6c`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `charging_pile_list` | `unknown` | yes | 3.24.3 | `scene_info_model.dart @0x2340ea8` |

#### ChargingPileList

`fromJson` `scene_info_model.dart @0x2341060`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `device_pn` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2341080` |
| `device_sn` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2341108` |
| `device_img` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2341190` |
| `bind_site_status` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2341218` |
| `device_name` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x23412a0` |
| `status` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2341328` |
| `charging_pile_power` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x23413b0` |
| `charging_pile_status` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x2341438` |
| `charging_pile_online` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x23414c0` |

#### DieselInfo

`fromJson` `scene_info_model.dart @0x2343dc8`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `diesel_list` | `unknown` | yes | ≤3.18.0 | `scene_info_model.dart @0x2343e04` |
| `total_diesel_power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2343ec8` |
| `third_party_diesel_power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2343f50` |
| `third_party_diesel_plugged` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2343fd8` |
| `third_party_diesel_mode` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2344044` |
| `total_diesel_remain_time` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23440cc` |
| `third_party_diesel_connect_type` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2344154` |
| `third_party_diesel_type` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23441dc` |
| `third_party_diesel_connected` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2344264` |

#### DieselList

`fromJson` `scene_info_model.dart @0x23443c8`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `device_pn` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23443e8` |
| `device_sn` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2344470` |
| `device_name` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23444f8` |
| `device_img` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2344580` |
| `diesel_power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2344608` |
| `bind_status` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2344690` |
| `mode` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2344718` |
| `fuel_type` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23447a0` |
| `remain_time` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2344828` |
| `bat_soc` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23448b0` |
| `is_plugged` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2344938` |
| `output_mode` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23449a4` |
| `fuel_level` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2344a2c` |
| `fuel_unit` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2344ab4` |
| `bat_is_charge` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2344b3c` |
| `status` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2344ba8` |
| `remain_electricity` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2344c30` |

#### FeatureSwitch

`fromJson` `scene_info_model.dart @0x2341574`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `multi_pv` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2341594` |
| `smart_plug` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2341600` |
| `micro_inverter_power_exceed` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x234166c` |
| `micro_inverter_output_exceed` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x23416d8` |
| `offgrid_with_micro_inverter_alert` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2341744` |
| `manual_backup_mode` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x23417b0` |
| `exceed_power` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x234181c` |
| `peak_valley_mode` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2341888` |
| `heating` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x23418f4` |
| `shelly_meter` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2341960` |
| `support_p1_meter` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x23419cc` |
| `0w_feed` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2341a34` |
| `0w_feed_v2` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2341a9c` |
| `enable_parallel` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2341b04` |
| `plug_switch_report` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2341b6c` |
| `show_third_party_pv_panel` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2341bd4` |
| `meter_self_testing` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2341c54` |
| `power_limit_status` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2341cd4` |
| `power_saving_mode` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2341d54` |
| `third_party_pv_enable` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2341dd4` |
| `enable_aiems_v2` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2341e54` |
| `grid_to_ev` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2341ed4` |
| `feed_in_time_segments` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2341f54` |
| `soc_enable` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2341fd4` |
| `backup_reserve_enable` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2342054` |
| `custom_rate_charge_enable` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x23420d4` |
| `backup_reserve_effective` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2342154` |
| `fault_platform` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x23421d8` |

#### FunctionSwitch

`fromJson` `scene_info_model.dart @0x23431cc`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `diesel_ac_output` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23431ec` |
| `diesel_connected` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2343258` |
| `grid_online` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23432c4` |
| `is_downgrade` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2343330` |
| `third_party_diesel_connected` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x234339c` |
| `third_party_pv_connected` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2343408` |
| `grid_available` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2343474` |
| `ct_available` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23434e0` |
| `sub_package_version_mismatch` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x234354c` |
| `diy_version_mismatch` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x23435b8` |
| `heating` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2343624` |
| `exceed_power` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2343690` |
| `soc_calibration` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23436fc` |
| `physical_grid` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2343768` |
| `meter_self_testing` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x23437d4` |
| `low_light_detection` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x234382c` |
| `wired_meter_connected` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2343898` |
| `is_greater_30v` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2343904` |
| `off_grid` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2343970` |
| `system_forced_charge` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23439dc` |
| `load_port_connected` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2343a48` |
| `third_party_pv_active` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2343ab4` |
| `is_ats` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2343b20` |
| `is_allow_ats_off_grid` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2343b8c` |
| `is_running_ats_off_grid` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2343bf8` |
| `temperature_unit` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2343c64` |
| `zero_net` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2343cd0` |
| `enable_self_test_fault_bits` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2343d3c` |

#### GridInfo

`fromJson` `scene_info_model.dart @0x2344ce4`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `grid_list` | `unknown` | yes | ≤3.18.0 | `scene_info_model.dart @0x2344d20` |
| `photovoltaic_to_grid_power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2344de4` |
| `grid_to_home_power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2344e6c` |
| `has_history_data` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2344ef4` |
| `is_show_grid` | `bool?` | yes | 3.24.3 | `scene_info_model.dart @0x2344f60` |

#### GridList

`fromJson` `scene_info_model.dart @0x23450c4`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `device_pn` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23450e4` |
| `device_sn` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x234516c` |
| `device_name` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23451f4` |
| `device_img` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x234527c` |
| `bind_site_status` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2345304` |
| `status` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x234538c` |
| `wireless_type` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2345414` |

#### HardwareInfo

`fromJson` `scene_info_model.dart @0x2340740`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `hardware_list` | `unknown` | yes | 3.24.3 | `scene_info_model.dart @0x234077c` |

#### HardwareItem

`fromJson` `scene_info_model.dart @0x2340934`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `device_pn` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2340954` |
| `device_sn` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x23409dc` |
| `hardware_type` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x2340a64` |
| `hardware_status` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x2340aec` |

#### OffGridInfo

`fromJson` `scene_info_model.dart @0x2342e48`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `off_grid_available_time` | `int` | yes | ≤3.18.0 | `scene_info_model.dart @0x2342e74` |
| `outage_date` | `int` | yes | ≤3.18.0 | `scene_info_model.dart @0x2342ee8` |
| `outage_duration` | `int` | yes | ≤3.18.0 | `scene_info_model.dart @0x2342f5c` |
| `back_up_duration_1` | `int` | yes | ≤3.18.0 | `scene_info_model.dart @0x2342fd0` |
| `back_up_duration_2` | `int` | yes | ≤3.18.0 | `scene_info_model.dart @0x2343044` |
| `off_grid_start_time` | `int` | yes | ≤3.18.0 | `scene_info_model.dart @0x23430b4` |

#### PvList

`fromJson` `scene_info_model.dart @0x2347d9c`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `pv_name` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2347dbc` |
| `pv_power` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2347e44` |

#### SmartPlugInfo

`fromJson` `scene_info_model.dart @0x234227c`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `total_power` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x23422b8` |
| `smart_plug_list` | `unknown` | yes | 3.24.3 | `scene_info_model.dart @0x2342340` |

#### SmartPlugList

`fromJson` `scene_info_model.dart @0x23424f8`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `device_pn` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2342518` |
| `device_sn` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x23425a0` |
| `device_img` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2342628` |
| `bind_site_status` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x23426b0` |
| `device_name` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2342738` |
| `tag` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x23427c0` |
| `status` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2342844` |
| `tag_img` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x23428cc` |
| `total_power` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2342954` |
| `current_power` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x23429dc` |
| `create_time` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x2342a64` |
| `err_code` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x2342aec` |
| `tag_alias` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2342b74` |
| `tag_id` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x2342bfc` |
| `type_tag` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2342c84` |
| `type_tag_id` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x2342d0c` |
| `type_tag_img` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2342d94` |

#### SolarBankInfo

`fromJson` `scene_info_model.dart @0x23454c8`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `solarbank_list` | `unknown` | yes | ≤3.18.0 | `scene_info_model.dart @0x2345504` |
| `total_charge_power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23455c8` |
| `power_unit` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2345650` |
| `charging_status` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23456d8` |
| `total_bat_soc` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2345760` |
| `total_bat_fcc` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x23457e8` |
| `total_bat_rc` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2345870` |
| `total_photovoltaic_power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23458f4` |
| `total_output_power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2345978` |
| `total_discharge_power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23459fc` |
| `is_display_data` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2345a80` |
| `to_home_load` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2345ae8` |
| `solar_power_1` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2345b6c` |
| `solar_power_2` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2345bf0` |
| `third_party_pv_power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2345c74` |
| `third_party_pv_connected` | `bool?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2345cf8` |
| `grid_to_battery_power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2345d60` |
| `pei_heating_power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2345de4` |
| `backup_info` | `BackupInfo?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2345e68` |
| `total_operating_power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2345efc` |
| `feeder_0w` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x2345f80` |
| `grid_port_input` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2346004` |
| `grid_port_output` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x234608c` |

#### SolarbankList

`fromJson` `scene_info_model.dart @0x23463e4`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `device_pn` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2346420` |
| `device_sn` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23464a8` |
| `device_name` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2346530` |
| `device_img` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23465b8` |
| `bat_soc` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2346640` |
| `bind_site_status` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23466c8` |
| `bat_charge_power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2346750` |
| `bat_discharge_power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23467d8` |
| `power_unit` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2346860` |
| `charging_status` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23468e8` |
| `status` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2346970` |
| `wireless_type` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x23469f8` |
| `photovoltaic_power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2346a80` |
| `output_power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2346b08` |
| `create_time` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2346b90` |
| `sub_package_num` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2346c18` |
| `max_battery_pack_num` | `int?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2346ca0` |
| `solar_power_1` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2346d28` |
| `solar_power_2` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2346db0` |
| `solar_name_1` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2346e38` |
| `solar_name_2` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2346ec0` |
| `pei_heating_power` | `String?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2346f48` |
| `function_switch` | `FunctionSwitch?` | yes | ≤3.18.0 | `scene_info_model.dart @0x2346fd0` |
| `pv_list` | `unknown` | yes | ≤3.18.0 | `scene_info_model.dart @0x234706c` |
| `bms_list` | `unknown` | yes | ≤3.18.0 | `scene_info_model.dart @0x234712c` |
| `offgrid_power` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x23471f0` |
| `offgrid_name` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2347278` |
| `load_port_power` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2347300` |
| `load_port_name` | `String?` | yes | 3.24.3 | `scene_info_model.dart @0x2347388` |
| `load_port_switch` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x2347410` |
| `load_port_auto` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x2347498` |
| `load_port_mode` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x2347520` |
| `load_port_status` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x23475a8` |
| `bat_temperature` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x2347630` |
| `phase` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x23476b8` |
| `self_test_status` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x2347740` |
| `install_method` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x23477c8` |
| `enwg_status` | `int?` | yes | 3.24.3 | `scene_info_model.dart @0x2347850` |

The table shows some keys twice (`branch_info`, `branch_list`, `other_load_power`): the extractor records one row per read site; the `fromJson` reads those keys in more than one branch.

## Produced by

[`platform_get_site_scene`](../api/power_service/v2/site/platform_get_site_scene.md): `SceneInfoModel.fromJson` at `micro_hes/src/a17e2/station/home/base_station_logic.dart @0x2348a88`. The class is also used for the V1 site scene of the IoT kit (not described here).

## Consumed by

The micro HES (A17E2) station home (`base_station_logic.dart`); field-level use is not traced.

## Changed since 3.18.0

Keys with `since` 3.24.3 are new: `ems_mode_power`, `ct2_self_test_status`, `self_test_fault_bits`, `switch_0w`, `style_id`, `smart_plug_info`, `feature_switch`, `charging_pile_info`, `aiems_profit`, `heat_pump_connected`, `custom_charging_type`, `is_show_pv`, `price_level`, `hardware_info`, `grid_ov_auto_reduce_capability`, `reason_code`; the element classes `AiemsProfit`, `ChargingPileInfo`, `ChargingPileList`, `FeatureSwitch`, `HardwareInfo`, `HardwareItem`, `SmartPlugInfo` and `SmartPlugList` are new.

## Known unknowns

- The value domains of the many integer keys are only partly decoded: `power_site_type` takes the values of [enums, power_site_type](../reference/enums.md#power_site_type-upstream-solixsitetype) and `ems_mode` the wire values of `EmsModeType` ([enums](../reference/enums.md#energy-mode-and-price-enums)); `use_time_type`, `style_id`, `custom_charging_type`, `price_level`, `reason_code` and the other integer keys have no enum in the asm that was bound to them — traced 2026-10-20: not traced per key.
