> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# DevicePowerConfigItem

## Purpose

Carries the power configuration of one device as returned by `get_devices_power_config`: the device serial and its configured input and output power.

## Dart class + file

`DevicePowerConfigItem` (`fromJson @0x2af2148`) and `InputPowerInfo` (`fromJson @0x2af2394`), file `settings/src/common/model/device_power_config.dart` (package `settings`).

## Fields

Column `since`: `≤3.18.0` means the key is present in 3.18.0 (earlier versions not checked), `3.24.3` means first seen in 3.24.3. Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Nullability and Dart types come from `tools/model_fields.py` (`data/models.json`); `unknown` means the extractor could not resolve the element type.

### DevicePowerConfigItem

`fromJson` `device_power_config.dart @0x2af2148`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `device_sn` | `String?` | yes | 3.24.3 | `device_power_config.dart @0x2af2168` |
| `config` | `unknown` | yes | 3.24.3 | `device_power_config.dart @0x2af21f0` |
| `output` | `OutputPowerInfo?` | yes | 3.24.3 | `device_power_config.dart @0x2af2248` |
| `input` | `InputPowerInfo?` | yes | 3.24.3 | `device_power_config.dart @0x2af22e8` |

### InputPowerInfo

`fromJson` `device_power_config.dart @0x2af2394`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `default_input_power` | `int?` | yes | 3.24.3 | `device_power_config.dart @0x2af23b4` |
| `max_input_power` | `int?` | yes | 3.24.3 | `device_power_config.dart @0x2af243c` |

## Produced by

[`get_devices_power_config`](../api/devicecontrol/get_devices_power_config.md): `DevicePowerConfigItem.fromJson` at `settings/src/sdk/util/grid_connect_util.dart @0x2af212c`.

## Consumed by

`grid_connect_util.dart` (the grid connection settings); field-level use is not traced.

## Changed since 3.18.0

Both classes are new in 3.24.3.

## Known unknowns

- The units and the meaning of `config`, `output` and `input` are not decoded beyond the Dart types.
