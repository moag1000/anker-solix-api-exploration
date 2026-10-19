> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# GridCodeModel

## Purpose

Carries the grid code catalogue of a product: for each supported country the states with their grid codes and grid code names.

## Dart class + file

`GridCodeModel` (`fromJson @0x28f6e60`), `RegionCode` (`@0x28f7094`) and `RegionStateInfo` (`@0x28f7350`), file `base_service/bean/model/init_flow/grid_code_model.dart` (package `base_service`).

## Fields

Column `since`: `≤3.18.0` means the key is present in 3.18.0 (earlier versions not checked), `3.24.3` means first seen in 3.24.3. Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Nullability and Dart types come from `tools/model_fields.py` (`data/models.json`); `unknown` means the extractor could not resolve the element type.

### GridCodeModel

`fromJson` `grid_code_model.dart @0x28f6e60`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `product_code` | `String?` | yes | ≤3.18.0 | `grid_code_model.dart @0x28f6e80` |
| `region_codes` | `List` | no | ≤3.18.0 | `grid_code_model.dart @0x28f6f08` |

### RegionCode

`fromJson` `grid_code_model.dart @0x28f7094`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `country_code` | `String?` | yes | ≤3.18.0 | `grid_code_model.dart @0x28f70b4` |
| `country_name` | `String?` | yes | ≤3.18.0 | `grid_code_model.dart @0x28f713c` |
| `states` | `List` | no | ≤3.18.0 | `grid_code_model.dart @0x28f71c4` |

### RegionStateInfo

`fromJson` `grid_code_model.dart @0x28f7350`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `state_code` | `String?` | yes | ≤3.18.0 | `grid_code_model.dart @0x28f7370` |
| `state_name` | `String?` | yes | ≤3.18.0 | `grid_code_model.dart @0x28f73f8` |
| `grid_code` | `int?` | yes | ≤3.18.0 | `grid_code_model.dart @0x28f7480` |
| `country_name` | `String?` | yes | 3.24.3 | `grid_code_model.dart @0x28f7508` |
| `grid_code_name` | `String?` | yes | 3.24.3 | `grid_code_model.dart @0x28f7590` |
| `country_code` | `String?` | yes | 3.24.3 | `grid_code_model.dart @0x28f7618` |

The element type of `region_codes` is `RegionCode` and that of `states` is `RegionStateInfo` by name and file (the list parse was not traced).

## Produced by

[`platform_get_pn_region_code`](../api/power_service/v2/platform_get_pn_region_code.md): `GridCodeModel.fromJson` at `base_service/view/grid/grid_param_util.dart @0x28f649c` and `flutter_charging_beginning/.../power_plant_config_controller.dart @0x2b07498`; a cached copy is restored from storage in `base_service/utils/sp_helper.dart @0x2b080dc` and `charging/util/save/sp_util_impl.dart @0x2cbae14`.

## Consumed by

The grid pickers (`choose_grid_view.dart`, `choose_grid_view_v2.dart`) and the grid parameter setting pages; field-level use is not traced.

## Changed since 3.18.0

No key was added or removed between 3.18.0 and 3.24.3 (all keys `≤3.18.0`).

## Known unknowns

- Whether `RegionStateInfo.country_name` duplicates `RegionCode.country_name` is not known.
