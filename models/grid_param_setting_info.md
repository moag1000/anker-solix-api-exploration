> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# GridParamSettingInfo

## Purpose

Carries the grid code (grid standard) settings of a product: product code, country, grid code and name, the enabled parameters and the advanced parameter template and values; it is both the response of `platform_get_user_region_param` and the basis of the document sent to `platform_set_user_region_param`.

## Dart class + file

`GridParamSettingInfo` and its element classes, file `settings/src/common/model/grid_param_setting_info.dart` (package `settings`, `GridParamSettingInfo.fromJson @0x28f7e98`). The package `device` holds an identical copy in `device/src/station_setting/controller/common_grid_param/model/grid_param_setting_info.dart` (`fromJson` addresses: `GridParamSettingInfo @0x2a5154c`, `GridProtectParam @0x2a5031c`, `GridScheduleParam @0x2a5121c`, `ParamInfos @0x2a50620`, `Range @0x2a50fc0`, `ScopeValue @0x2a50d4c`); the key lists of both copies are the same (compared programmatically).

## Fields

Column `since`: `≤3.18.0` means the key is present in 3.18.0 (earlier versions not checked), `3.24.3` means first seen in 3.24.3. Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Nullability and Dart types come from `tools/model_fields.py` (`data/models.json`); `unknown` means the extractor could not resolve the element type.

### GridParamSettingInfo

`fromJson` `grid_param_setting_info.dart @0x28f7e98`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `product_code` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x28f7eb8` |
| `identifier_id` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x28f7f40` |
| `country_code` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x28f7fc8` |
| `grid_code` | `int?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x28f8050` |
| `grid_code_name` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x28f80d8` |
| `enable_params` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x28f8160` |
| `advanced_params_template` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x28f81e8` |
| `advanced_params_setting` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x28f8270` |

### GridProtectParam

`fromJson` `grid_param_setting_info.dart @0x29e5994`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `category` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x29e59d0` |
| `paramInfos` | `unknown` | yes | 3.24.3 | `grid_param_setting_info.dart @0x29e5a54` |
| `categoryType` | `int?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x29e5b18` |

### GridScheduleParam

`fromJson` `grid_param_setting_info.dart @0x28f7a30`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `dredRcrRrcr` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x28f7a50` |
| `enwg` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x28f7ad8` |
| `epo` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x28f7b60` |
| `clsInput` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x28f7be8` |
| `clsOutput` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x28f7c70` |

### ParamInfos

`fromJson` `grid_param_setting_info.dart @0x29e5c98`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `site` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x29e5cb8` |
| `unit` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x29e5d40` |
| `dataName` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x29e5dc8` |
| `describe` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x29e5e50` |
| `isSelected` | `int?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x29e5ed8` |
| `scopeValue` | `ScopeValue?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x29e5f5c` |
| `actualValue` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x29e5ff8` |
| `coefficient` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x29e6080` |
| `abbreviation` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x29e6108` |
| `defaultValue` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x29e6190` |
| `abbreviationFieldTag` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x29e6218` |
| `fullNameInEnglish` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x29e62a0` |
| `abbreviationFieldType` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x29e6328` |

### ScopeValue

`fromJson` `grid_param_setting_info.dart @0x29e63c4`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `type` | `int?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x29e63e4` |
| `range` | `Range?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x29e6468` |
| `property` | `unknown` | not determined | 3.24.3 | `grid_param_setting_info.dart @0x29e6504` |
| `fixedValue` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x29e6550` |
| `selectValue` | `unknown` | not determined | 3.24.3 | `grid_param_setting_info.dart @0x29e65d8` |

### Range

`fromJson` `grid_param_setting_info.dart @0x29e6638`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `max` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x29e6658` |
| `min` | `String?` | yes | 3.24.3 | `grid_param_setting_info.dart @0x29e66e0` |

## Produced by

[`platform_get_user_region_param`](../api/power_service/v2/platform_get_user_region_param.md): `GridParamSettingInfo.fromJson` is called in the success closures of `GridParamSettingController.getGridSetting` (`device/.../grid_param_setting_controller.dart @0x2a4f934`, `settings/.../grid_param_setting_controller.dart @0x29e4e88`), `GridSettingLogic._getGridSetting` (`charging/.../grid_setting_logic.dart @0x28f5d80`) and the protect page (`grid_protect_setting_controller.dart @0x361706c`). The sibling write is [`platform_set_user_region_param`](../api/power_service/v2/platform_set_user_region_param.md).

## Consumed by

The grid parameter setting pages and the grid protection setting page (`grid_param_setting_controller.dart`, `grid_protect_setting_controller.dart`); field-level use is not traced.

## Changed since 3.18.0

The whole class family is new in 3.24.3.

## Known unknowns

- The meaning of the keys of `ParamInfos` (13 keys, mostly limits) and of `GridScheduleParam` is not documented here; the table lists the Dart types only.
- Which products return `advanced_params_template` is not known.
