> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# HeatPumpParam

## Purpose

Carries the heat-pump control setting of a site, as read from `get_site_device_param` with `param_type` 24: the switch and three numeric limits.

## Dart class + file

`settings/src/common/model/heat_pump_param.dart` (package `settings`). Both classes write `fromJson` as a constructor body (`_ X.fromJson`), not as a `factory`, so `data/models.json` does not list them.

| class | role | method |
|---|---|---|
| `HeatPumpParam` | wrapper `{site_id, params}` | `fromJson` `@0x2af7300`, `toJson` `@0x2af6fbc` |
| `Params` | the decoded `param_data` | `fromJson` `@0x2af747c`, `toJson` `@0x2af70c4` |

## Fields

Column `since`: both classes are absent from the 3.18.0 asm (no class of these names), so every key is `3.24.3`.

### HeatPumpParam

The app builds the wrapper map itself: the GET closure wraps the decoded `param_data` as `{"site_id": <site>, "params": <decoded map>}` (`@0x2af6a34`, `@0x2af6a50`) before calling `fromJson`. `site_id` is therefore not a server key.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `site_id` | `String?` | yes | 3.24.3 | `heat_pump_param.dart @0x2af732c` |
| `params` | `Params` | no | 3.24.3 | `heat_pump_param.dart @0x2af73c0` |

### Params

These four keys are also the `param_data` keys of the set call (`Params.toJson`: `enabled` `@0x2af7110`, `activate_power` `@0x2af713c`, `min_interval` `@0x2af716c`, `min_running_time` `@0x2af719c`); `setHeatPump` builds its own map with the same four keys (see [param_types.md](../api/param_types.md)).

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `enabled` | `bool?` | yes | 3.24.3 | `heat_pump_param.dart @0x2af749c` |
| `activate_power` | `int?` | yes | 3.24.3 | `heat_pump_param.dart @0x2af7500` |
| `min_interval` | `int?` | yes | 3.24.3 | `heat_pump_param.dart @0x2af7584` |
| `min_running_time` | `int?` | yes | 3.24.3 | `heat_pump_param.dart @0x2af7608` |

## Produced by

[`get_site_device_param`](../api/power_service/site/get_site_device_param.md) with `param_type` 24: `HeatPumpSettingController.getHeatPumpParam` (`heat_pump_setting_controller.dart @0x2af6630`), success closure `@0x2af687c` (`param_data` `@0x2af696c`, `jsonDecode` `@0x2af69e0`, `HeatPumpParam.fromJson` `@0x2af6a88`). An empty `param_data` becomes `{"enabled": false}` (`@0x2af69c4`). Written with [`set_site_device_param`](../api/power_service/site/set_site_device_param.md) (`setHeatPump`, `heat_pump_setting_controller.dart @0x3a5e8d4`).

## Consumed by

The heat pump settings page (`HeatPumpSettingController`, `heat_pump_setting_controller.dart`): after parsing, the closure applies `fixedActivatePower` (`@0x2af6af8`), `fixedMinRunningTime` (`@0x2af6b68`) and `fixedMinInterval` (`@0x2af6be0`) to the values and rebuilds the model (`@0x2af6e80`). `setHeatPump` (`@0x3a5e8d4`) parses the typed values with `tryParse` and clamps them (`clamp` calls `@0x3a5e960` and `@0x3a5ea00`); the bounds were not decoded.

Fallback values when the switch is off (traced 2026-10-20): `setHeatPump` (`heat_pump_setting_controller.dart @0x3a5e8d4`) takes `activate_power`, `min_running_time` and `min_interval` from the parsed and clamped page values when `enabled` is true (`ArrayLoad` at `@0x3a5eb38`), and from three controller fields when it is false: `field_47` (`@0x3a5eb5c`), `field_4f` (`@0x3a5eba8`) and `field_57` (`@0x3a5ebe0`). The controller initialiser sets these three 64-bit fields to the raw values 500, 5 and 5 (`@0x370be98` to `@0x370beb8`, unboxed, so real values): the fallbacks are the page defaults 500 for `activate_power` and 5 for `min_running_time` and `min_interval`. The units of the three numbers are not stated in the asm.

## Changed since 3.18.0

New: both classes and the `param_type` 24 requests do not exist in 3.18.0 (see [param_types.md](../api/param_types.md#changed-since-3180)).

## Known unknowns

- The units and valid ranges of `activate_power`, `min_running_time` and `min_interval`, and the clamp bounds used by `setHeatPump`.
