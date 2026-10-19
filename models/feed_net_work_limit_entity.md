> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# FeedNetWorkLimitEntity

## Purpose

Holds the feed-in limit state that the old feed-limit page shows and caches locally; it is a UI-side entity, not a server response, and it is built from a `GetSiteDeviceParamResponse`.

## Dart class + file

`FeedNetWorkLimitEntity`, `charging/ui/page/device/main/sitation_energy_system/station_home_settings/feed_network_limit/feed_network_limit_logic.dart` (package `charging`). `fromJson` `@0x34b03bc`, `fromJsonString` `@0x34b0258` (decodes a JSON string and calls `fromJson` at `@0x34b02bc`), `toJsonString` `@0x28f9440`, `copy` (`@0x3fb30ac`).

## Fields

Column `since`: `≤3.18.0` means the key is present in 3.18.0 (earlier versions not checked). The keys are camelCase because the object is stored locally as JSON text, not sent to the cloud.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `feedTimes` | `List<FeedTimes>` (element type not read from a cast) | not determined | 3.24.3 | `feed_network_limit_logic.dart @0x34b03ec` |
| `isSwithOpen` | `bool?` | yes | ≤3.18.0 | `feed_network_limit_logic.dart @0x34b04c0` |
| `isLimitChecked` | `bool?` | yes | ≤3.18.0 | `feed_network_limit_logic.dart @0x34b0548` |
| `currentvalue` | `String?` | yes | ≤3.18.0 | `feed_network_limit_logic.dart @0x34b05d0` |

## Produced by

Not an endpoint response. `FeedNetworkLimitLogic.getFeedLimitStatus` (`@0x28f8a44`) builds the entity (`@0x28f8d94`) from the parsed [`GetSiteDeviceParamResponse`](get_site_device_param_response.md) of [`get_site_device_param`](../api/power_service/site/get_site_device_param.md) with `param_type` 18 and stores it with `toJsonString` (`@0x28f8e44`) through `saveFeedNetLimitSwitchStatus` (`@0x28f8e54`). `onInit` (`@0x34aff18`) restores it with `fromJsonString` (`@0x34b0084`).

## Consumed by

The old feed-limit page itself (`FeedNetworkLimitLogic`, `feed_network_limit_logic.dart`); `showOpenLimitDialog` (`@0x3fb43e8`, allocations `@0x3fb4528`, `@0x3fb4588`) and a dialog closure (`@0x3fb47b0`) create modified copies. The new feed-limit page uses a different class, see [feed_grid_setting_param.md](feed_grid_setting_param.md).

## Changed since 3.18.0

Added key: `feedTimes` (the list of feed-in time windows). The other three keys exist in 3.18.0.

## Known unknowns

- Where the cached JSON string is stored (the `saveFeedNetLimitSwitchStatus` target) and when it is read back.
- Whether the old page is still reachable in 3.24.3 now that `feed_network_limit_new` exists.
