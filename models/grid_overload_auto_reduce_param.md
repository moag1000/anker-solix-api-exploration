> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# GridOverloadAutoReduceParam

## Purpose

Carries the grid overload auto-reduce switch of a site, as read from and written to `get_site_device_param` / `set_site_device_param` with `param_type` 37.

## Dart class + file

`GridOverloadAutoReduceParam`, `settings/src/common/model/grid_overload_auto_reduce_param.dart` (package `settings`), fromJson `@0x2a78ea8`, toJson `@0x2a78fc8`. `fromJson` is a constructor body, so `data/models.json` does not list the class.

## Fields

Column `since`: the class is absent from the 3.18.0 asm, so the key is `3.24.3`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `grid_ov_auto_load_cut_enable` | `int?` | yes | 3.24.3 | `grid_overload_auto_reduce_param.dart @0x2a78ed4` |

`toJson` writes the same key (`@0x2a79014`).

## Produced by

[`get_site_device_param`](../api/power_service/site/get_site_device_param.md) with `param_type` 37: `_getGridOverloadAutoReduceSetting` (`station_advanced_setting_controller.dart @0x2a78b08`, closure `@0x2a78c60`, `GridOverloadAutoReduceParam.fromJson` `@0x2a78df4`). Written with [`set_site_device_param`](../api/power_service/site/set_site_device_param.md) (`_setGridOverloadAutoReduceSetting`, `@0x376fb50`, `toJson` call `@0x376fd04`; see [param_types.md](../api/param_types.md)).

## Consumed by

`StationAdvancedSettingController` (`station_advanced_setting_controller.dart`); field use is not traced.

## Changed since 3.18.0

New: the class and the `param_type` 37 requests do not exist in 3.18.0.

## Known unknowns

- The value set of `grid_ov_auto_load_cut_enable` (0/1 assumed, not shown) and what the cut does on the device.
