> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# IncomeDetailModel and A17e2BenifitsModel

## Purpose

Carries the savings (income) statistics of a site: the solar/grid self-sufficiency split, the trend values per period, the total with its unit and the list of years; the same layout exists in two Dart classes.

## Dart class + file

`IncomeDetailModel` (`fromJson @0x2a43778`, file `station_home/src/domain/model/income_detail_model.dart`, package `station_home`) and `A17e2BenifitsModel` (`fromJson @0x2a48a00`, file `charging/model/a17e2/a17e2_benifits_model/a17e2_benifits_model.dart`, package `charging`), each with its own copies of `SelfSufRateInfo` and `Trends`. The key lists are identical; the only difference is the nullability of `self_suf_rate_info` (non-null in `IncomeDetailModel`, nullable in `A17e2BenifitsModel`).

## Fields

Column `since`: `≤3.18.0` means the key is present in 3.18.0 (earlier versions not checked), `3.24.3` means first seen in 3.24.3. Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Nullability and Dart types come from `tools/model_fields.py` (`data/models.json`); `unknown` means the extractor could not resolve the element type.

### IncomeDetailModel

`fromJson` `income_detail_model.dart @0x2a43778`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `self_suf_rate_info` | `SelfSufRateInfo` | no | 3.24.3 | `income_detail_model.dart @0x2a4379c` |
| `trends` | `List?` | yes | 3.24.3 | `income_detail_model.dart @0x2a4383c` |
| `total` | `String?` | yes | 3.24.3 | `income_detail_model.dart @0x2a43944` |
| `unit` | `String?` | yes | 3.24.3 | `income_detail_model.dart @0x2a439b0` |
| `years` | `List?` | yes | 3.24.3 | `income_detail_model.dart @0x2a43a1c` |

### SelfSufRateInfo

`fromJson` `income_detail_model.dart @0x2a43ff8`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `solar` | `String?` | yes | 3.24.3 | `income_detail_model.dart @0x2a44024` |
| `grid` | `String?` | yes | 3.24.3 | `income_detail_model.dart @0x2a44080` |

### Trends

`fromJson` `income_detail_model.dart @0x2a441e8`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `time` | `String?` | yes | 3.24.3 | `income_detail_model.dart @0x2a44214` |
| `value` | `String?` | yes | 3.24.3 | `income_detail_model.dart @0x2a44274` |
| `rods` | `List?` | yes | 3.24.3 | `income_detail_model.dart @0x2a442cc` |

The `A17e2BenifitsModel` copy has the same keys at other addresses:

### A17e2BenifitsModel

`fromJson` `a17e2_benifits_model.dart @0x2a48a00`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `self_suf_rate_info` | `SelfSufRateInfo?` | yes | 3.24.3 | `a17e2_benifits_model.dart @0x2a48a2c` |
| `trends` | `List?` | yes | 3.24.3 | `a17e2_benifits_model.dart @0x2a48ab8` |
| `total` | `String?` | yes | 3.24.3 | `a17e2_benifits_model.dart @0x2a48bb0` |
| `unit` | `String?` | yes | 3.24.3 | `a17e2_benifits_model.dart @0x2a48c10` |
| `years` | `List?` | yes | 3.24.3 | `a17e2_benifits_model.dart @0x2a48c6c` |

## Produced by

[`platform_get_site_savings`](../api/power_service/v2/site/platform_get_site_savings.md): `IncomeDetailModel.fromJson` at `station_home/src/ui/shared/income/income_detail/income_detail_controller.dart @0x2a436f8`; `A17e2BenifitsModel.fromJson` at `charging/ui/page/device/a17e2/benifits/a17e2_benifits_http_repository.dart @0x2a48598`.

## Consumed by

The income detail page of the station home and the A17E2 benefits page; field-level use is not traced.

## Changed since 3.18.0

The whole class family is new in 3.24.3.

## Known unknowns

- The element types of `trends`, `rods` and `years` (`List?`) are not resolved.
- The unit semantics of `total` and `unit` (currency or energy) are not decoded.
