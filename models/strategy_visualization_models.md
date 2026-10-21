> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# AI EMS strategy visualization models

## Purpose

Carries the answer of the AI EMS strategy visualization: the planned energy chart (solar, battery, home load, grid per period with the strategy type), the current strategy and the price chart (buy and sell prices).

## Dart class + file

`StrategyVisualizationDetail` (`ak_soft_ems/aiems/models/strategy_visualization_model.dart`); `EnergyChartDataPoint` (`ak_soft_ems/aiems/models/strategy_visualization_model.dart`); `PriceChartData` (`ak_soft_ems/aiems/models/strategy_visualization_model.dart`); `PriceDataPoint` (`ak_soft_ems/aiems/models/strategy_visualization_model.dart`). `fromJson` addresses are under each class below.

## Fields

Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Dart types and nullability come from `tools/model_fields.py` (`data/models.json`); an "of `X`" note is the list element class read from the `<X>` type argument next to the key.

### StrategyVisualizationDetail

Answer of `strategy/visualization`.

`fromJson` `strategy_visualization_model.dart @0x24a43a8`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `energy_chart_data` | `List<EnergyChartDataPoint>` (the key read is not type-tested in place; the list is built with the type argument `<EnergyChartDataPoint>` `@0x24a465c`, the `List` check `@0x24a45f8` and the mapping closure `@0x24a4648` that calls `EnergyChartDataPoint.fromJson` `@0x24a4dc0`) | yes | 3.24.3 | `strategy_visualization_model.dart @0x24a43d4` |
| `current_strategy` | `Map?` | yes | 3.24.3 | `strategy_visualization_model.dart @0x24a441c` |
| `price_unit` | `String` | yes | 3.24.3 | `strategy_visualization_model.dart @0x24a44c4` |
| `energy_unit` | `String` | yes | 3.24.3 | `strategy_visualization_model.dart @0x24a4540` |
| `price_chart_data` | `PriceChartData?` | yes | 3.24.3 | `strategy_visualization_model.dart @0x24a46e0` |

### EnergyChartDataPoint

One period of the planned energy chart (element of `energy_chart_data`).

`fromJson` `strategy_visualization_model.dart @0x24a4dd8`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `start_time` | `String` | yes | 3.24.3 | `strategy_visualization_model.dart @0x24a4e04` |
| `end_time` | `String` | yes | 3.24.3 | `strategy_visualization_model.dart @0x24a4e7c` |
| `solar_energy` | `unknown` | yes | 3.24.3 | `strategy_visualization_model.dart @0x24a4ef4` |
| `battery_energy` | `unknown` | yes | 3.24.3 | `strategy_visualization_model.dart @0x24a4f4c` |
| `home_load` | `unknown` | yes | 3.24.3 | `strategy_visualization_model.dart @0x24a4fa4` |
| `grid_energy` | `unknown` | yes | 3.24.3 | `strategy_visualization_model.dart @0x24a4ffc` |
| `data_period` | `int` | yes | 3.24.3 | `strategy_visualization_model.dart @0x24a5054` |
| `battery_soc` | `unknown` | yes | 3.24.3 | `strategy_visualization_model.dart @0x24a50c8` |
| `battery_status` | `unknown` | yes | 3.24.3 | `strategy_visualization_model.dart @0x24a5120` |
| `strategy_type` | `int` | yes | 3.24.3 | `strategy_visualization_model.dart @0x24a5178` |
| `strategy_detail_values` | `List?` | yes | 3.24.3 | `strategy_visualization_model.dart @0x24a51dc` |
| `strategy_detail_description` | `String` | yes | 3.24.3 | `strategy_visualization_model.dart @0x24a5294` |

### PriceChartData

Buy and sell price series.

`fromJson` `strategy_visualization_model.dart @0x24a4798`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `buy_real_prices` | `List` | no | 3.24.3 | `strategy_visualization_model.dart @0x24a47c4` |
| `sell_real_prices` | `List<PriceDataPoint>` | no | 3.24.3 | `strategy_visualization_model.dart @0x24a486c` |

### PriceDataPoint

One price point.

`fromJson` `strategy_visualization_model.dart @0x24a4b54`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `price` | `unknown` | yes | 3.24.3 | `strategy_visualization_model.dart @0x24a4b80` |
| `start` | `String` | yes | 3.24.3 | `strategy_visualization_model.dart @0x24a4bd8` |
| `end` | `String` | yes | 3.24.3 | `strategy_visualization_model.dart @0x24a4c4c` |
| `data_period` | `int` | yes | 3.24.3 | `strategy_visualization_model.dart @0x24a4cac` |

## Produced by

- [`visualization`](../api/ems/strategy/visualization.md): `StrategyVisualizationDetail` (`StrategyVisualizationDetail.fromJson`, `ak_soft_ems/aiems/models/strategy_visualization_model.dart @0x24a43a8`)

## Consumed by

`AiEmsStrategyController._fetchStrategyData` (`ak_soft_ems/aiems/aiems_strategy_controller.dart @0x363cfa8`) and the system policy page of the A5101 (`SystemPolicyLogic.fetchAndUpdateSmartModeSubtitle`); field-level use is not traced.

## Changed since 3.18.0

All classes are new in 3.24.3.

## Known unknowns

- The units are given by `energy_unit` and `price_unit` in the answer; the value formats of `solar_energy`, `battery_energy`, `home_load`, `grid_energy`, `battery_soc`, `battery_status` and `price` are `unknown` for the extractor.
- `current_strategy` is a free map (`Map?`, `@0x24a4440`): its keys are not read here, and `strategy_type`/`strategy_detail_values` are not decoded — traced 2026-10-20: the string keys `strategy_detail_values` and `strategy_detail_description` are loaded in no file other than this model (grep over the asm root: 1 file each), so no code reads them from `current_strategy` by name; `strategy_type` occurs in other models (range extender, schedule), none of them a reader of this map; reads by field offset on `EnergyChartDataPoint` were not followed.
