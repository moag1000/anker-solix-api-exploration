> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# MeterEnergyAnalysisModel

## Purpose

Carries the history chart document of the AE1X0 meter: the data trend, the import and export energy of the selected period and the lifetime import and export totals, per phase.

## Dart class + file

`MeterEnergyAnalysisModel` (`fromJson @0x2ca3574`) and its element class `ChartDataPoint` (`fromJson @0x2ca4230`), file `third_device/src/module/ae1x0/history/widget/meter_energy_analysis_model.dart` (package `third_device`).

## Fields

Column `since`: `≤3.18.0` means the key is present in 3.18.0 (earlier versions not checked), `3.24.3` means first seen in 3.24.3. Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Nullability and Dart types come from `tools/model_fields.py` (`data/models.json`); `unknown` means the extractor could not resolve the element type.

### MeterEnergyAnalysisModel

`fromJson` `meter_energy_analysis_model.dart @0x2ca3574`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `data_trend` | `List<ChartDataPoint>` | no | 3.24.3 | `meter_energy_analysis_model.dart @0x2ca3594` |
| `period_export` | `String?` | yes | 3.24.3 | `meter_energy_analysis_model.dart @0x2ca37cc` |
| `period_import` | `String?` | yes | 3.24.3 | `meter_energy_analysis_model.dart @0x2ca3854` |
| `lifetime_total_export` | `String?` | yes | 3.24.3 | `meter_energy_analysis_model.dart @0x2ca38dc` |
| `lifetime_l1_export` | `String?` | yes | 3.24.3 | `meter_energy_analysis_model.dart @0x2ca3964` |
| `lifetime_l2_export` | `String?` | yes | 3.24.3 | `meter_energy_analysis_model.dart @0x2ca39ec` |
| `lifetime_l3_export` | `String?` | yes | 3.24.3 | `meter_energy_analysis_model.dart @0x2ca3a74` |
| `lifetime_total_import` | `String?` | yes | 3.24.3 | `meter_energy_analysis_model.dart @0x2ca3afc` |
| `lifetime_l1_import` | `String?` | yes | 3.24.3 | `meter_energy_analysis_model.dart @0x2ca3b84` |
| `lifetime_l2_import` | `String?` | yes | 3.24.3 | `meter_energy_analysis_model.dart @0x2ca3c0c` |
| `lifetime_l3_import` | `String?` | yes | 3.24.3 | `meter_energy_analysis_model.dart @0x2ca3c94` |

### ChartDataPoint

`fromJson` `meter_energy_analysis_model.dart @0x2ca4230`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `time` | `String?` | yes | 3.24.3 | `meter_energy_analysis_model.dart @0x2ca4250` |
| `power` | `String?` | yes | 3.24.3 | `meter_energy_analysis_model.dart @0x2ca42d8` |
| `import_energy` | `String?` | yes | 3.24.3 | `meter_energy_analysis_model.dart @0x2ca4360` |
| `export_energy` | `String?` | yes | 3.24.3 | `meter_energy_analysis_model.dart @0x2ca43e8` |

The element type of `data_trend` is probably `ChartDataPoint` (inference from the file; the list parse was not traced).

## Produced by

[`energy_analysis`](../api/power_service/v2/device/energy_analysis.md): `MeterEnergyAnalysisModel.fromJson` is called in the success closure of `Ae1x0MeterChartLogic.requestChartData` (`third_device/src/module/ae1x0/history/widget/meter_chart_logic.dart @0x2ca2fc8`, closure `@0x2ca2f10`).

## Consumed by

The AE1X0 history page (`meter_chart_logic.dart`, `meter_chart_widget.dart`); field-level use is not traced.

## Changed since 3.18.0

The whole class is new in 3.24.3 (`since` 3.24.3 on every key).

## Known unknowns

- The unit and meaning of `period_export`, `period_import` and the lifetime values (kWh versus Wh, strings versus numbers) are not decoded here beyond the Dart type. — traced 2026-10-20: all of these values and the four `ChartDataPoint` values are `String?` in the model (table above). The only unit labels in the history files (`third_device/src/module/ae1x0/history/`) are the localization keys `unitKWh` and `unitW` in `widget/meter_chart_widget.dart`; the page `ae1x0_history_page.dart` has only the title keys `dataHistoryAe1x0`, `energyStorageExportAe1x0`, `energyStorageImportAe1x0`, `lifetime` and `total`. So the app shows kWh and W labels; which of the model values carries which label was not followed to the field loads.
