> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# ElectricityPriceModel

## Contents

1. [Purpose](#purpose)
1. [Dart class + file](#dart-class--file)
1. [Fields](#fields)
1. [Produced by](#produced-by)
1. [Consumed by](#consumed-by)
1. [Changed since 3.18.0](#changed-since-3180)
1. [Known unknowns](#known-unknowns)

## Purpose

Carries the electricity price data of a site for one provider: either a time-of-use price table with seasons, or dynamic hourly prices for today and tomorrow, as returned by `get_price`.

## Dart class + file

`ElectricityPriceModel` and its element classes, file `ak_soft_contract/src/energy/model/electricity_price_model.dart` (package `ak_soft_contract`). `ElectricityPriceModel.fromJson` is at `@0x255111c`. Classes with the same names exist in other Dart files (`charging/feature/utilitiy_rate_plan/dynamic_price/model/dynamic_price_model.dart`, `electricity_price_common/timeslot_model/electricity_price_model.dart`); they are different classes and are not described here.

## Fields

Column `since`: `≤3.18.0` means the key is present in 3.18.0 (earlier versions not checked). Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Nullability and Dart types come from `tools/model_fields.py` (`data/models.json`); `unknown` means the extractor could not resolve the list or map element type.

### ElectricityPriceModel

`fromJson` `electricity_price_model.dart @0x255111c`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `companyName` | `String?` | yes | ≤3.18.0 | `electricity_price_model.dart @0x255113c` |
| `touPrice` | `TouPrice?` | yes | ≤3.18.0 | `electricity_price_model.dart @0x25511c4` |
| `dynamicPrice` | `DynamicPrice?` | yes | ≤3.18.0 | `electricity_price_model.dart @0x2551260` |

### TouPrice

`fromJson` `electricity_price_model.dart @0x2553a38`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `peakValleyPriceSeasons` | `unknown` | yes | ≤3.18.0 | `electricity_price_model.dart @0x2553a74` |
| `currency` | `String?` | yes | ≤3.18.0 | `electricity_price_model.dart @0x2553b38` |

### PeakValleyPriceSeasons

`fromJson` `electricity_price_model.dart @0x25541b4`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `sessionStart` | `int?` | yes | ≤3.18.0 | `electricity_price_model.dart @0x25541f0` |
| `sessionEnd` | `int?` | yes | ≤3.18.0 | `electricity_price_model.dart @0x2554278` |
| `peakValleyPrices` | `unknown` | yes | ≤3.18.0 | `electricity_price_model.dart @0x2554300` |

### PeakValleyPrices

`fromJson` `electricity_price_model.dart @0x25544b8`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `from` | `String?` | yes | 3.24.3 | `electricity_price_model.dart @0x25544d8` |
| `to` | `String?` | yes | 3.24.3 | `electricity_price_model.dart @0x255455c` |
| `sellPrice` | `double?` | yes | 3.24.3 | `electricity_price_model.dart @0x25545e0` |
| `buyPrice` | `double?` | yes | 3.24.3 | `electricity_price_model.dart @0x25546fc` |
| `type` | `int?` | yes | 3.24.3 | `electricity_price_model.dart @0x2554818` |
| `dayType` | `int?` | yes | 3.24.3 | `electricity_price_model.dart @0x255489c` |

### DynamicPrice

`fromJson` `electricity_price_model.dart @0x2551dc0`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `releaseTime` | `String?` | yes | 3.24.3 | `electricity_price_model.dart @0x2551de0` |
| `todayPrices` | `PricesParent?` | yes | 3.24.3 | `electricity_price_model.dart @0x2551e64` |
| `tomorrowPrices` | `PricesParent?` | yes | 3.24.3 | `electricity_price_model.dart @0x2551ef8` |
| `currency` | `String?` | yes | 3.24.3 | `electricity_price_model.dart @0x2551f8c` |
| `interval` | `int?` | yes | 3.24.3 | `electricity_price_model.dart @0x2552010` |
| `dynamicPriceParam` | `DynamicPriceParam?` | yes | 3.24.3 | `electricity_price_model.dart @0x2552094` |
| `needReconfigure` | `bool?` | yes | 3.24.3 | `electricity_price_model.dart @0x2552128` |

### DynamicPriceParam

`fromJson` `electricity_price_model.dart @0x25521a4`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `chargeTime` | `unknown` | yes | ≤3.18.0 | `electricity_price_model.dart @0x25521e0` |
| `chargeSoc` | `int?` | yes | ≤3.18.0 | `electricity_price_model.dart @0x25522a4` |
| `chargeSum` | `int?` | yes | ≤3.18.0 | `electricity_price_model.dart @0x255232c` |
| `dischargeTime` | `unknown` | yes | ≤3.18.0 | `electricity_price_model.dart @0x25523b4` |
| `dischargeSum` | `int?` | yes | ≤3.18.0 | `electricity_price_model.dart @0x2552478` |
| `batteryExport` | `bool?` | yes | ≤3.18.0 | `electricity_price_model.dart @0x2552500` |
| `countryCode` | `String?` | yes | ≤3.18.0 | `electricity_price_model.dart @0x255256c` |

### PricesParent

`fromJson` `electricity_price_model.dart @0x2552924`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `prices` | `unknown` | yes | ≤3.18.0 | `electricity_price_model.dart @0x2552960` |
| `buyRealPrice` | `unknown` | yes | ≤3.18.0 | `electricity_price_model.dart @0x2552a14` |
| `sellRealPrice` | `unknown` | yes | ≤3.18.0 | `electricity_price_model.dart @0x2552ac8` |
| `day` | `String?` | yes | ≤3.18.0 | `electricity_price_model.dart @0x2552b80` |
| `changeDst` | `bool?` | yes | ≤3.18.0 | `electricity_price_model.dart @0x2552c04` |
| `isManual` | `bool?` | yes | ≤3.18.0 | `electricity_price_model.dart @0x2552c70` |
| `dst` | `String?` | yes | ≤3.18.0 | `electricity_price_model.dart @0x2552cdc` |

### Prices

`fromJson` `electricity_price_model.dart @0x2553398`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `buyPrice` | `double?` | yes | 3.24.3 | `electricity_price_model.dart @0x25533c0` |
| `sellPrice` | `double?` | yes | 3.24.3 | `electricity_price_model.dart @0x25534dc` |
| `start` | `String?` | yes | 3.24.3 | `electricity_price_model.dart @0x25535f8` |
| `end` | `String?` | yes | 3.24.3 | `electricity_price_model.dart @0x255367c` |
| `startUnix` | `int?` | yes | 3.24.3 | `electricity_price_model.dart @0x2553700` |
| `endUnix` | `int?` | yes | 3.24.3 | `electricity_price_model.dart @0x2553788` |
| `type` | `int?` | yes | 3.24.3 | `electricity_price_model.dart @0x2553810` |
| `canSelect` | `bool?` | yes | 3.24.3 | `electricity_price_model.dart @0x2553894` |
| `zone` | `String?` | yes | 3.24.3 | `electricity_price_model.dart @0x2553900` |
| `manual` | `bool` | yes | 3.24.3 | `electricity_price_model.dart @0x2553988` |

### BuyRealPrice

`fromJson` `electricity_price_model.dart @0x2552e5c`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `price` | `double?` | yes | ≤3.18.0 | `electricity_price_model.dart @0x2552e7c` |
| `start` | `String?` | yes | ≤3.18.0 | `electricity_price_model.dart @0x2552f98` |
| `end` | `String?` | yes | ≤3.18.0 | `electricity_price_model.dart @0x255301c` |
| `startUnix` | `int?` | yes | ≤3.18.0 | `electricity_price_model.dart @0x25530a0` |
| `endUnix` | `int?` | yes | ≤3.18.0 | `electricity_price_model.dart @0x2553128` |

### ChargeTime

`fromJson` `electricity_price_model.dart @0x25526ec`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `start` | `String?` | yes | ≤3.18.0 | `electricity_price_model.dart @0x255270c` |
| `end` | `String?` | yes | ≤3.18.0 | `electricity_price_model.dart @0x2552790` |

`ChargeTime` (`start`, `end`) is the probable element type of `DynamicPriceParam.chargeTime` and `dischargeTime`; that mapping is an inference from the class name, the list parse was not traced. The same holds for `PricesParent.prices` (probably `Prices`), `buyRealPrice` / `sellRealPrice` (probably `BuyRealPrice`) and `TouPrice.peakValleyPriceSeasons` (probably `PeakValleyPriceSeasons`).

## Produced by

[`get_price`](../api/charging_hes_installer_svc/get_price.md): `ElectricityPriceModel.fromJson` is called in the success closure of every sender listed on that page: `dynamic_price_detail_info_view.dart @0x27d1dcc`, `dynameic_price_detail_info_view_c5.dart @0x27d04ac`, `tou_auto_price_pkg_result_logic.dart @0x2c48c7c`, `charge_discharge_setting_logic.dart @0x29b5488`, `charge_discharge_setting_logic_c5.dart @0x29b41e4`, `timeslot_preview_logic.dart @0x2c56230`, `timeslot_preview_poly_logic.dart @0x2c5283c`, `power_usage_scenario_controller.dart @0x2550a50`, `system_policy_logic.dart @0x28ec3b4`, `power_usage_scenario_logic.dart @0x28a2214`.

## Consumed by

The parsed object is read by the same files (price preview pages and the charge/discharge time-slot settings pages). Field-level use is not traced.

## Changed since 3.18.0

Keys with `since` 3.24.3 are new: all of `DynamicPrice` (the class is new in this file, `@0x2551dc0`; `releaseTime`, `todayPrices`, `tomorrowPrices`, `currency`, `interval`, `dynamicPriceParam`, `needReconfigure`), all of `Prices` (`@0x2553398`) and all of `PeakValleyPrices` (`@0x25544b8`). `ElectricityPriceModel`, `TouPrice`, `PricesParent`, `BuyRealPrice`, `DynamicPriceParam`, `ChargeTime` and `PeakValleyPriceSeasons` exist in 3.18.0. Because the 3.18.0 file used other names for the same data, whether the wire format changed or only the Dart class was renamed is not decided.

## Known unknowns

- The list element types listed as `unknown` were not resolved (see the note below the tables).
- The unit and rounding of `buyPrice` / `sellPrice` (double) and the meaning of `type`, `dayType` and `canSelect` are not documented; no captured response exists.
