> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# DevicePowerConfigItem

## Purpose

Carries the power configuration of one device as returned by `get_devices_power_config`: the device serial and its configured input and output power.

## Dart class + file

`DevicePowerConfigItem` (`fromJson @0x2af2148`) and `InputPowerInfo` (`fromJson @0x2af2394`), file `settings/src/common/model/device_power_config.dart` (package `settings`); `OutputPowerInfo` (`fromJson @0x2af24e4`), file `settings/src/common/model/output_power_info.dart` (package `settings`).

## Fields

Column `since`: `≤3.18.0` means the key is present in 3.18.0 (earlier versions not checked), `3.24.3` means first seen in 3.24.3. Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Nullability and Dart types come from `tools/model_fields.py` (`data/models.json`); `unknown` means the extractor could not resolve the element type.

### DevicePowerConfigItem

`fromJson` `device_power_config.dart @0x2af2148`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `device_sn` | `String?` | yes | 3.24.3 | `device_power_config.dart @0x2af2168` |
| `config` | container map (not stored itself): `fromJson` tests it for null (`@0x2af2214`) and reads `output` and `input` from it, not from the item (receiver at `@0x2af2250`) | yes | 3.24.3 | `device_power_config.dart @0x2af21f0` |
| `output` | `OutputPowerInfo?` | yes | 3.24.3 | `device_power_config.dart @0x2af2248` |
| `input` | `InputPowerInfo?` | yes | 3.24.3 | `device_power_config.dart @0x2af22e8` |

### InputPowerInfo

`fromJson` `device_power_config.dart @0x2af2394`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `default_input_power` | `int?` | yes | 3.24.3 | `device_power_config.dart @0x2af23b4` |
| `max_input_power` | `int?` | yes | 3.24.3 | `device_power_config.dart @0x2af243c` |

### OutputPowerInfo

`fromJson` `output_power_info.dart @0x2af24e4`. The three `unlock_*` keys have the same names as keys of `StationPowerLimitModel`; their semantics are owned by [station_power_limit.md](station_power_limit.md) and are not repeated here (whether the device-level and the station-level values mean the same is not verified).

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `max_output_power` | `int?` | yes | 3.24.3 | `output_power_info.dart @0x2af2504` |
| `legal_limit` | `int?` | yes | 3.24.3 | `output_power_info.dart @0x2af258c` |
| `default_output_power` | `int?` | yes | 3.24.3 | `output_power_info.dart @0x2af2614` |
| `unlock_default_power_type` | `int?` | yes | 3.24.3 | `output_power_info.dart @0x2af269c` |
| `unlock_pop_content` | `String?` | yes | 3.24.3 | `output_power_info.dart @0x2af2724` |
| `unlock_pop_image` | `String?` | yes | 3.24.3 | `output_power_info.dart @0x2af27ac` |

## Produced by

[`get_devices_power_config`](../api/devicecontrol/get_devices_power_config.md): `DevicePowerConfigItem.fromJson` at `settings/src/sdk/util/grid_connect_util.dart @0x2af212c`.

## Consumed by

`grid_connect_util.dart` (the grid connection settings); field-level use is not traced.

## Changed since 3.18.0

Both classes are new in 3.24.3.

## Known unknowns

- The units of the power values in `output` and `input` and their meaning beyond the names are not decoded — traced 2026-10-20: the structure is decoded (`config` is the map that holds `output` and `input`, see the `config` row); no unit string was found in `device_power_config.dart` or `output_power_info.dart`.
