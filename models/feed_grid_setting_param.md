> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# FeedGridSettingParam

## Purpose

Carries the grid feed-in setting of a site in two variants: the settings-package class for `param_type` 28 (feed switch, upper limit, 0 W feeder, cached power, time windows) and the class of the new feed-limit page for `param_type` 18 (`switch_0w`, `feed-in_power_limit`, time windows).

## Dart class + file

Both variants are named `FeedGridSettingParam` and both define a nested `FeedTimes`; they are different classes in different files. `fromJson` is a constructor body (`_ X.fromJson`), so `data/models.json` does not list them.

| class | file | method |
|---|---|---|
| `FeedGridSettingParam` (28) | `settings/src/common/model/feed_grid_setting_param.dart` | `fromJson` `@0x2282d64`, `toJson` `@0x228330c` |
| `FeedTimes` (28) | same file | `fromJson` `@0x22831bc` |
| `FeedGridSettingParam` (18) | `charging/ui/page/device/main/sitation_energy_system/station_home_settings/feed_network_limit_new/feed_grid_setting_param_new.dart` | `fromJson` `@0x2aa98b8`, `toJson` `@0x2aa92dc` |
| `FeedTimes` (18) | same file | `fromJson` `@0x2aa9be4` |

## Fields

Column `since`: neither file has a counterpart in the 3.18.0 asm (no class of these names), so every key is `3.24.3`.

### FeedGridSettingParam (`param_type` 28, `feed_grid_setting_param.dart`)

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `feed_switch` | `int?` | yes | 3.24.3 | `feed_grid_setting_param.dart @0x2282da8` |
| `feed_upper_limit` | `int?` | yes | 3.24.3 | `feed_grid_setting_param.dart @0x2282e3c` |
| `feeder_0w` | `int?` | yes | 3.24.3 | `feed_grid_setting_param.dart @0x2282ed0` |
| `cached_power` | `int?` | yes | 3.24.3 | `feed_grid_setting_param.dart @0x2282f64` |
| `feed_times` | `List<FeedTimes>` (element type not read from a cast) | not determined | 3.24.3 | `feed_grid_setting_param.dart @0x2282ff8` |

`FeedTimes` (28): `start_time` (`int?`, `@0x22831dc`), `end_time` (`int?`, `@0x2283264`). `toJson` writes `feed_switch` `@0x2283358`, `feed_upper_limit` `@0x2283388`, `feeder_0w` `@0x22833b8`, `cached_power` `@0x22833e8`, `feed_times` `@0x2283468`.

### FeedGridSettingParam (`param_type` 18, `feed_grid_setting_param_new.dart`)

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `switch_0w` | `int?` | yes | 3.24.3 | `feed_grid_setting_param_new.dart @0x2aa98fc` |
| `feed-in_power_limit` | `int?` | yes | 3.24.3 | `feed_grid_setting_param_new.dart @0x2aa9990` |
| `feed_times` | `List<FeedTimes>` (element type not read from a cast) | not determined | 3.24.3 | `feed_grid_setting_param_new.dart @0x2aa9a24` |

`FeedTimes` (18): `start_time` (`int?`, `@0x2aa9c04`), `end_time` (`int?`, `@0x2aa9c88`). `toJson` writes `switch_0w` `@0x2aa9328`, `feed-in_power_limit` `@0x2aa9358`, `feed_times` `@0x2aa93d8`. The three keys are also keys of `SiteDeviceParamData` ([get_site_device_param_response.md](get_site_device_param_response.md)).

## Produced by

[`get_site_device_param`](../api/power_service/site/get_site_device_param.md): `param_type` 28 by `FeedGridController.getFeedGridParam` (`feed_grid_controller.dart @0x2aedeb8`; `FeedGridSettingParam.fromJson` `@0x2aeddcc` and `@0x2aee264`); `param_type` 18 by `getFeedGridParam` of the new page (`feed_network_limit_new_logic.dart @0x2aa8c90`, closure `@0x2aa8df4`, `fromJson` `@0x2aa8ff4`). Written with [`set_site_device_param`](../api/power_service/site/set_site_device_param.md): 28 by `FeedGridController.updateByCloud` (`feed_grid_controller.dart @0x2287430`, `toJson` call `@0x2287504`), 18 by `updateByCloud` of the new page (`feed_network_limit_new_logic.dart @0x2aa90fc`, `toJson` call `@0x2aa91d4`). See [param_types.md](../api/param_types.md).

## Consumed by

`FeedGridController` (`feed_grid_controller.dart`) and `FeedNetworkLimitNewLogic` (`feed_network_limit_new_logic.dart`); field use is not traced. The a17e2 station logic does not use this class: it reads and updates the same `param_type` 28 map as a plain `Map` (`_getFeedGridConfig` `@0x233e8c0`, `updateFeeder0w` `@0x233e6bc`).

## Changed since 3.18.0

New: both classes and the `param_type` 28 requests do not exist in 3.18.0. `param_type` 18 existed (the old page uses `SiteDeviceParamData` and `FeedNetWorkLimitEntity`, see [feed_net_work_limit_entity.md](feed_net_work_limit_entity.md)).

## Known unknowns

- The meaning and units of `feed_switch`, `feeder_0w`, `cached_power` and the time-window values.
- Whether the settings variant (28) and the new-page variant (18) address the same device setting through two different server types.
