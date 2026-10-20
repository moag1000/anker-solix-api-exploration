> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# S1S2ChargerSessionChartModel

## Purpose

Carries the charge-session chart of an S1/S2 device: the data trend (power and energy per period, split into AC, DC, charging, import and export), the totals and the units.

## Dart class + file

`S1S2ChargerSessionChartModel` (`fromJson @0x2993490`) with `DataTrend` (`fromJson @0x2993dd8`) and `PpsTotal` (`fromJson @0x2993920`), file `s1_s2/src/page/charge_sessions/model/charger_session_chart_model.dart` (package `s1_s2`).

## Fields

Column `since`: `≤3.18.0` means the key is present in 3.18.0 (earlier versions not checked), `3.24.3` means first seen in 3.24.3. Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Nullability and Dart types come from `tools/model_fields.py` (`data/models.json`); `unknown` means the extractor could not resolve the element type.

### S1S2ChargerSessionChartModel

`fromJson` `charger_session_chart_model.dart @0x2993490`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `data` | `String` | yes | 3.24.3 | `charger_session_chart_model.dart @0x29934cc` |
| `pps_total` | `PpsTotal?` | yes | 3.24.3 | `charger_session_chart_model.dart @0x29935e0` |
| `energy_unit` | `dynamic` (no type test between the key load and the store) | yes | 3.24.3 | `charger_session_chart_model.dart @0x299367c` |
| `power_unit` | `dynamic` (no type test between the key load and the store) | yes | 3.24.3 | `charger_session_chart_model.dart @0x2993700` |
| `update_time` | `dynamic` (no type test between the key load and the store) | yes | 3.24.3 | `charger_session_chart_model.dart @0x2993784` |
| `data_trend` | `List` of `DataTrend` (mapping closure allocated `@0x29938a0`, calls `DataTrend.fromJson`) | yes | 3.24.3 | `charger_session_chart_model.dart @0x2993808` |

### DataTrend

`fromJson` `charger_session_chart_model.dart @0x2993dd8`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `time` | `dynamic` (no type test between the key load and the store) | yes | 3.24.3 | `charger_session_chart_model.dart @0x2993df8` |
| `power` | `dynamic` (no type test between the key load and the store) | yes | 3.24.3 | `charger_session_chart_model.dart @0x2993e7c` |
| `import_energy` | `dynamic` (no type test between the key load and the store) | yes | 3.24.3 | `charger_session_chart_model.dart @0x2993f00` |
| `export_energy` | `dynamic` (no type test between the key load and the store) | yes | 3.24.3 | `charger_session_chart_model.dart @0x2993f84` |
| `ac_consume` | `dynamic` (no type test between the key load and the store) | not determined | 3.24.3 | `charger_session_chart_model.dart @0x2994008` |
| `dc_consume` | `dynamic` (no type test between the key load and the store) | not determined | 3.24.3 | `charger_session_chart_model.dart @0x299405c` |
| `ac_charging` | `dynamic` (no type test between the key load and the store) | not determined | 3.24.3 | `charger_session_chart_model.dart @0x29940b0` |
| `dc_charging` | `dynamic` (no type test between the key load and the store) | not determined | 3.24.3 | `charger_session_chart_model.dart @0x2994104` |
| `pv_input` | `dynamic` (no type test between the key load and the store) | not determined | 3.24.3 | `charger_session_chart_model.dart @0x2994158` |

### PpsTotal

`fromJson` `charger_session_chart_model.dart @0x2993920`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `ac_consume_total` | `dynamic` (no type test between the key load and the store) | yes | 3.24.3 | `charger_session_chart_model.dart @0x2993940` |
| `dc_consume_total` | `dynamic` (no type test between the key load and the store) | yes | 3.24.3 | `charger_session_chart_model.dart @0x29939c4` |
| `ac_charging_total` | `dynamic` (no type test between the key load and the store) | yes | 3.24.3 | `charger_session_chart_model.dart @0x2993a48` |
| `dc_charging_total` | `dynamic` (no type test between the key load and the store) | yes | 3.24.3 | `charger_session_chart_model.dart @0x2993acc` |
| `charging_total` | `dynamic` (no type test between the key load and the store) | yes | 3.24.3 | `charger_session_chart_model.dart @0x2993b50` |
| `consume_total` | `dynamic` (no type test between the key load and the store) | yes | 3.24.3 | `charger_session_chart_model.dart @0x2993bd4` |
| `pv_input_total` | `dynamic` (no type test between the key load and the store) | yes | 3.24.3 | `charger_session_chart_model.dart @0x2993c54` |

## Produced by

[`energy_analysis`](../api/power_service/v2/device/energy_analysis.md): `S1S2ChargerSessionChartModel.fromJson` is called in `S1S2ChargerChartHttpRepository._fetchFromServer` (`s1_s2/src/page/charge_sessions/repository/charger_chart_http_repository.dart @0x2991e24`).

## Consumed by

The S1/S2 charge-session chart page; `getChartTotalDimensionList` (`@0x2992d20`) reads the parsed object. Field-level use is not traced.

## Changed since 3.18.0

The whole class is new in 3.24.3.

## Known unknowns

- The unit semantics of `energy_unit` and `power_unit` are not decoded — traced 2026-10-20: both and all trend and total keys are read with no type test, so the app declares them as Dart `dynamic` (rows above); no literal unit text is bound to them in `getChartTotalDimensionList`.
- Which of the trend keys are filled for which chart type is not known.
