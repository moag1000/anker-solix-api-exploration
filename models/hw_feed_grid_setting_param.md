> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# HwFeedGridSettingParam

## Purpose

Carries the hardware anti-backflow setting of a site, as read from and written to `get_site_device_param` / `set_site_device_param` with `param_type` 31.

## Dart class + file

`HwFeedGridSettingParam`, `settings/src/common/model/hw_feed_grid_setting_param.dart` (package `settings`), fromJson `@0x2aec2c4`, toJson `@0x2aebf64`. `fromJson` is a constructor body, so `data/models.json` does not list the class.

## Fields

Column `since`: the class is absent from the 3.18.0 asm, so every key is `3.24.3`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `anti_backflow_enable` | `int?` | yes | 3.24.3 | `hw_feed_grid_setting_param.dart @0x2aec2f0` |
| `anti_backflow_power` | `int?` | yes | 3.24.3 | `hw_feed_grid_setting_param.dart @0x2aec384` |

`toJson` writes the same keys (`@0x2aebfb0`, `@0x2aebfe0`).

## Produced by

[`get_site_device_param`](../api/power_service/site/get_site_device_param.md) with `param_type` 31: `getFeedGridParam` (`hardware_feed_grid_controller.dart @0x2aecf90`, closure `@0x2aed0ec`, `HwFeedGridSettingParam.fromJson` `@0x2aed2ac`). Written with [`set_site_device_param`](../api/power_service/site/set_site_device_param.md) (`updateByCloud`, `hardware_feed_grid_controller.dart @0x2aec054`, `toJson` call `@0x2aec130`; see [param_types.md](../api/param_types.md)).

## Consumed by

`HardwareFeedGridController` (`hardware_feed_grid_controller.dart`); field use is not traced.

## Changed since 3.18.0

New: the class and the `param_type` 31 requests do not exist in 3.18.0.

## Known unknowns

- The unit of `anti_backflow_power` and the value set of `anti_backflow_enable` (0/1 assumed, not shown).
- Which device or gateway the setting applies to.
