> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# SocSettingParam

## Purpose

Carries the state-of-charge limits of a site, as read from and written to `get_site_device_param` / `set_site_device_param` with `param_type` 27: charge limit, discharge limit, backup reserve and the SOC calibration switch.

## Dart class + file

`SocSettingParam` exists twice with the same keys: `soc/soc_setting/soc_setting_param.dart` (package `soc`, fromJson `@0x2afae64`, toJson `@0x2afa7a8`) and `device/src/station_setting/controller/station_soc_settings_v2/model/soc_setting_param.dart` (package `device`, fromJson `@0x3678460`). `data/models.json` does not list either, because `fromJson` is a constructor body (`_ SocSettingParam.fromJson`), not a `factory`.

## Fields

Column `since`: the class is absent from the 3.18.0 asm, so every key is `3.24.3`. Both copies read the same five keys in the same order; the table cites the `soc` package copy, the `device` copy is at `@0x367848c`, `@0x3678520`, `@0x36785b4`, `@0x3678648`, `@0x36786dc`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `charge_upper_limit` | `int?` | yes | 3.24.3 | `soc_setting_param.dart @0x2afae90` |
| `discharge_lower_limit` | `int?` | yes | 3.24.3 | `soc_setting_param.dart @0x2afaf24` |
| `backup_reserve_switch` | `int?` | yes | 3.24.3 | `soc_setting_param.dart @0x2afafb8` |
| `backup_reserve` | `int?` | yes | 3.24.3 | `soc_setting_param.dart @0x2afb04c` |
| `soc_calibration_enable` | `int?` | yes | 3.24.3 | `soc_setting_param.dart @0x2afb0e0` |

`toJson` writes the same five keys (`@0x2afa7f4`, `@0x2afa824`, `@0x2afa854`, `@0x2afa884`, `@0x2afa8b4`). In the closure `@0x45e76a8` of `SocSettingHandler.handle`, which builds the `SocSettingParam` (`@0x45e7738`) from a `SocLimitModel` and calls `_saveSocSetting`, the value stored into the `backup_reserve_switch` field (field 0xf, `@0x45e7768`) is derived from a bool of the model (`tst x1, #0x10`, `cset`, `lsl x2, x2, #1` at `@0x45e76fc` to `@0x45e7704`): raw 0 or 2, so 0 or 1.

## Produced by

[`get_site_device_param`](../api/power_service/site/get_site_device_param.md) with `param_type` 27: `getSocSetting` (`station_peak_shaving_controller.dart @0x2afab38`, closure `@0x2afac88`, `SocSettingParam.fromJson` `@0x2afadf8`) and `query` (`station_soc_data_source.dart @0x2afe7a0`, closure `@0x2afe92c`, `fromJson` `@0x2afeb00`). `fetchSocSetting` (`soc_command_capability_v2.dart @0x3677fc4`) sends the same request through the handler `akiot.cloud_api` and returns an `IoTAKResult`; the model parse of that path was not traced. Written with [`set_site_device_param`](../api/power_service/site/set_site_device_param.md) (`_saveSocSetting`; see [param_types.md](../api/param_types.md)).

## Consumed by

`StationPeakShavingController` (`station_peak_shaving_controller.dart`), `StationSocDataSource.query`, and the SOC settings v2 controller (`station_soc_settings_v2_controller.dart`); field-level use is not traced. The unrelated device capability class `SocSettings` (camelCase `chargeLimit`, `dischargeLimit`, `backupReserve`) is described in [soc_settings.md](soc_settings.md).

## Changed since 3.18.0

New: the class and the `param_type` 27 requests do not exist in 3.18.0.

## Known unknowns

- The units (percent) and ranges of the limits, and the meaning of `backup_reserve_switch` (0/1).
- Whether `fetchSocSetting` (cloud API handler) parses the response with this class.
