> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# PeakShavingSettingParam

## Purpose

Carries the peak shaving setting of a site, as read from and written to `get_site_device_param` / `set_site_device_param` with `param_type` 30: the switch, the upper limit and the reserved SOC.

## Dart class + file

`PeakShavingSettingParam`, `settings/src/common/model/peak_shaving_setting_param.dart` (package `settings`), fromJson `@0x2afa92c`, toJson `@0x2afa668`. `fromJson` is a constructor body, so `data/models.json` does not list the class.

## Fields

Column `since`: the class is absent from the 3.18.0 asm, so every key is `3.24.3`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `peak_shaving_switch` | `int?` | yes | 3.24.3 | `peak_shaving_setting_param.dart @0x2afa958` |
| `peak_shaving_upper_limit` | `int?` | yes | 3.24.3 | `peak_shaving_setting_param.dart @0x2afa9ec` |
| `peak_shaving_soc` | `int?` | yes | 3.24.3 | `peak_shaving_setting_param.dart @0x2afaa80` |

`toJson` writes the same keys (`@0x2afa6b4`, `@0x2afa6e4`, `@0x2afa714`).

## Produced by

[`get_site_device_param`](../api/power_service/site/get_site_device_param.md) with `param_type` 30: `getPeakShavingSetting` (`station_peak_shaving_controller.dart @0x2af9e24`, closure `@0x2af9fc4`, `PeakShavingSettingParam.fromJson` `@0x2afa194`). Written with [`set_site_device_param`](../api/power_service/site/set_site_device_param.md) (`updatePeakShavingSetting`, `@0x3a6d9cc`, `toJson` call `@0x3a6da90`; see [param_types.md](../api/param_types.md)).

## Consumed by

`StationPeakShavingController` and `station_peak_shaving_page.dart` (call `@0x3a6e20c`); field use is not traced.

## Changed since 3.18.0

New: the class and the `param_type` 30 requests do not exist in 3.18.0.

## Known unknowns

- The units of `peak_shaving_upper_limit` and `peak_shaving_soc` and the value set of `peak_shaving_switch`.
