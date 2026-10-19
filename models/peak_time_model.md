> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# PeakTimeModel

## Purpose

Carries the peak-time plan of a site, as returned by `get_site_device_param` with `param_type` 2: the number of peak periods and the list of periods.

## Dart class + file

`charging/model/peak_time_model.dart` (package `charging`).

| class | role | method |
|---|---|---|
| `PeakTimeModel` | response object | `fromJson` `@0x28f1ab4`, `toJson` `@0x28f1974` |
| `Data` | element of `data` | `fromJson` `@0x28f1cd8`, `toJson` `@0x28f1858` |

## Fields

Column `since`: `≤3.18.0` means the key is present in 3.18.0 (3.18.0 `PeakTimeModel.fromJson` `@0x1df8d9c`, `Data.fromJson` `@0x1df8f98`; earlier versions not checked). Elements of `data` are parsed by the static closure `@0x28f1c88` with `Data.fromJson`.

### PeakTimeModel

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `peak_count` | `int?` | yes | ≤3.18.0 | `peak_time_model.dart @0x28f1ad8` |
| `data` | `List<Data>` (list built even when the key is missing) | no | ≤3.18.0 | `peak_time_model.dart @0x28f1b40` |

### Data

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `start_time` | `int?` | yes | ≤3.18.0 | `peak_time_model.dart @0x28f1d04` |
| `end_time` | `int?` | yes | ≤3.18.0 | `peak_time_model.dart @0x28f1d60` |
| `mode` | `int?` | yes | ≤3.18.0 | `peak_time_model.dart @0x28f1dbc` |
| `ext` | `int?` | yes | ≤3.18.0 | `peak_time_model.dart @0x28f1e14` |

`toJson` writes the same keys: `PeakTimeModel.toJson` `peak_count` `@0x28f19a4`, `data` `@0x28f19c0`; `Data.toJson` `start_time` `@0x28f1884`, `end_time` `@0x28f18a0`, `mode` `@0x28f18b8`, `ext` `@0x28f18d0`.

## Produced by

[`get_site_device_param`](../api/power_service/site/get_site_device_param.md) with `param_type` 2: `getSitePeakTimeDeviceParam` (`http_request_repository_impl.dart @0x28f1538`), success closure `@0x28f163c` (reads `param_data`, `jsonDecode` `@0x28f1760`, `PeakTimeModel.fromJson` `@0x28f178c`). The same plan is written, by the set callers, with a value whose class is not typed in the asm; the binding of that value to `PeakTimeModel` is inferred from this GET parse and is `string-only` (status tag of this page). Written with [`set_site_device_param`](../api/power_service/site/set_site_device_param.md) (`savePeakPlanNew`, `deletePeakPlan`; see [param_types.md](../api/param_types.md)).

## Consumed by

`getSitePeakTimeDevice` in `recharge_logic.dart` (`@0x28f1428`), `energy_pps_controller.dart` (`@0x2bda2c8`), `station_home_info_logic.dart` (`@0x2c1f718`) and `station_set_time_logic.dart` (`@0x30e0cd8`, the peak-plan editor). The field-level use is not traced.

## Changed since 3.18.0

No key added or removed in `PeakTimeModel` or `Data` (same four and two keys in 3.18.0).

## Known unknowns

- The meaning and value sets of `mode` and `ext`, and the unit of `start_time` / `end_time` (minutes, seconds or an index).
- Whether the value that the set callers serialize is a `PeakTimeModel` object (`string-only` inference, see [param_types.md](../api/param_types.md)).
