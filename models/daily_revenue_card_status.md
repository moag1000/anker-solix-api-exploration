> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# DailyRevenueCardStatus

## Purpose

Carries the state of the "yesterday earnings" card of a micro-HES station: a status code, whether the price is dynamic, the revenue with currency and a link.

## Dart class + file

`DailyRevenueCardStatus` (`micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart`). `fromJson` addresses are under each class below.

## Fields

Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Dart types and nullability come from `tools/model_fields.py` (`data/models.json`); an "of `X`" note is the list element class read from the `<X>` type argument next to the key.

### DailyRevenueCardStatus

Answer of `daily_revenue_card/status`.

`fromJson` `yesterday_earning_tips_view.dart @0x27e8da0`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `status` | `int` | yes | 3.24.3 | `yesterday_earning_tips_view.dart @0x27e8dcc` |
| `is_dynamic` | `bool` | yes | 3.24.3 | `yesterday_earning_tips_view.dart @0x27e8e40` |
| `revenue` | `unknown` | yes | 3.24.3 | `yesterday_earning_tips_view.dart @0x27e8eb4` |
| `currency_unit` | `unknown` | yes | 3.24.3 | `yesterday_earning_tips_view.dart @0x27e8f2c` |
| `link_url` | `unknown` | yes | 3.24.3 | `yesterday_earning_tips_view.dart @0x27e8fa4` |
| `is_abnormal` | `false` | yes | 3.24.3 | `yesterday_earning_tips_view.dart @0x27e9018` |

## Produced by

- [`status`](../api/energy/daily_revenue_card/status.md): parsed with `DailyRevenueCardStatus.fromJson` (`micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart @0x27e8cc0`)

## Consumed by

`YesterdayEarningTipsLogic` and its view in the same file (`fetchCardStatus` success closure `@0x27e8c28`); field-level use is not traced.

## Changed since 3.18.0

The class is new in 3.24.3.

## Known unknowns

- The `status` codes, the unit of `revenue`, and what `is_abnormal` and `link_url` do on the card are not decoded; the extractor could not resolve the types of `revenue`, `currency_unit` and `link_url`.
