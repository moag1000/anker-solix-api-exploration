> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# AX170 branch icon models

## Purpose

Carries the icon catalogue for the custom branch circuits of an AX170 (ATS) system: icon categories, each with a list of named icon URLs.

## Dart class + file

`BranchIconModel` (`ats_ax170/src/ats_ax170/branch_circuit/data/branch_circuit_data.dart`); `BranchIconInfo` (`ats_ax170/src/ats_ax170/branch_circuit/data/branch_circuit_data.dart`). `fromJson` addresses are under each class below.

## Fields

Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Dart types and nullability come from `tools/model_fields.py` (`data/models.json`).

### BranchIconModel

Answer element of `get_custom_branch_icon`: one icon category.

`fromJson` `branch_circuit_data.dart @0x27d6064`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `icon_category` | `String?` | yes | ≤3.18.0 | `branch_circuit_data.dart @0x27d6090` |
| `icon_infos` | `List<BranchIconInfo>` of `BranchIconInfo` | no | ≤3.18.0 | `branch_circuit_data.dart @0x27d60ec` |

### BranchIconInfo

One icon (name and URL) in `BranchIconModel.icon_infos`.

`fromJson` `branch_circuit_data.dart @0x27d6514`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `name` | `String?` | yes | ≤3.18.0 | `branch_circuit_data.dart @0x27d6540` |
| `url` | `String?` | yes | ≤3.18.0 | `branch_circuit_data.dart @0x27d65b0` |

### BranchCircuitModel

A branch circuit record of the same file (name, icon, relay and power state). It is not part of the icon-catalogue answer; the page lists it because the file holds it. Its producer was not traced here.

`fromJson` `branch_circuit_data.dart @0x2336cac`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `id` | `int?` | yes | ≤3.18.0 | `branch_circuit_data.dart @0x2336cd8` |
| `name` | `String?` | yes | ≤3.18.0 | `branch_circuit_data.dart @0x2336d4c` |
| `remark` | `String?` | yes | ≤3.18.0 | `branch_circuit_data.dart @0x2336dc0` |
| `icon_url` | `String?` | yes | ≤3.18.0 | `branch_circuit_data.dart @0x2336e38` |
| `icon_name` | `String?` | yes | ≤3.18.0 | `branch_circuit_data.dart @0x2336eb0` |
| `defaultName` | `String?` | yes | ≤3.18.0 | `branch_circuit_data.dart @0x2336f28` |
| `defaultImg` | `String?` | yes | ≤3.18.0 | `branch_circuit_data.dart @0x2336fa0` |
| `defaultOffImg` | `String?` | yes | ≤3.18.0 | `branch_circuit_data.dart @0x2337018` |
| `merge_branche` | `int?` | yes | ≤3.18.0 | `branch_circuit_data.dart @0x2337090` |
| `isInitialData` | `bool?` | yes | ≤3.18.0 | `branch_circuit_data.dart @0x2337104` |
| `switchOn` | `bool?` | yes | ≤3.18.0 | `branch_circuit_data.dart @0x2337178` |
| `local` | `bool?` | yes | ≤3.18.0 | `branch_circuit_data.dart @0x23371ec` |
| `isCharging` | `bool?` | yes | ≤3.18.0 | `branch_circuit_data.dart @0x2337260` |
| `power` | `int?` | yes | ≤3.18.0 | `branch_circuit_data.dart @0x23372d4` |
| `combinedRelayStatus` | `bool?` | yes | ≤3.18.0 | `branch_circuit_data.dart @0x2337348` |
| `relayOverloadStatus` | `bool?` | yes | ≤3.18.0 | `branch_circuit_data.dart @0x23373b8` |

## Produced by

- [`get_custom_branch_icon`](../api/power_service/v2/app/get_custom_branch_icon.md): the data list holds `BranchIconModel` elements (mapping closure `custom_branch_controller.dart @0x27d6014`, `BranchIconModel.fromJson` call `@0x27d604c`).

## Consumed by

`CustomBranchController.getBranchIcons` (`ats_ax170/src/ats_ax170/branch_circuit/pages/custom_branch/custom_branch_controller.dart @0x27d5b0c`), the custom-branch editor of the AX170 branch circuit pages; field-level use is not traced.

## Changed since 3.18.0

Both classes are present in 3.18.0 (`since` column); no key is new in 3.24.3.

## Known unknowns

- Whether `icon_url` values (and `url` here) point to PNG or SVG images and from which host is not known.
