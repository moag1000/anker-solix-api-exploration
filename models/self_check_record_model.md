> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# SelfCheckRecordModel

## Purpose

Carries the last self-check record of a system: the self-check status and its start and end time.

## Dart class + file

`SelfCheckRecordModel` (`fromJson @0x2aca934`), file `flutter_charging_beginning/beginning/state_cards/self_check/self_check_record_model.dart` (package `flutter_charging_beginning`).

## Fields

Column `since`: `≤3.18.0` means the key is present in 3.18.0 (earlier versions not checked), `3.24.3` means first seen in 3.24.3. Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Nullability and Dart types come from `tools/model_fields.py` (`data/models.json`); `unknown` means the extractor could not resolve the element type.

### SelfCheckRecordModel

`fromJson` `self_check_record_model.dart @0x2aca934`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `self_check_status` | `int?` | yes | 3.24.3 | `self_check_record_model.dart @0x2acaa6c` |
| `start_time` | `int?` | yes | 3.24.3 | `self_check_record_model.dart @0x2acaaf0` |
| `end_time` | `int?` | yes | 3.24.3 | `self_check_record_model.dart @0x2acab74` |

Status codes used by the app (traced 2026-10-20): after `SelfCheckRecordModel.fromJson` (`new_system_test_controller.dart @0x2aca808`) the controller compares `self_check_status` (record field at offset 0x7) with the tagged 2 (`cmp w1, #2`, `@0x2aca868`), so the value 1, and then sets the page state to `SelfCheckState.success` (pool `[pp+0xad560]`, `@0x2aca888`) and stores the record in the controller (`@0x2aca8b0`); with the tagged 6 (`cmp w1, #6`, `@0x2aca8d8`), so the value 3, it sets `SelfCheckState.failed` (pool `[pp+0xad588]`, `@0x2aca8f0`). Any other value changes neither state. The enum `SelfCheckState` has the members `start` 0, `checking` 1, `success` 2, `failed` 3, `skipped` 4, `complete` 5 and `failedAndNoSupportRetry` 6 as indices (object dump `@0x42026d1` to `@0x4202691`); these indices are not the wire codes (success is 1 on the wire and 2 as an index).

## Produced by

[`get_self_check_record`](../api/devicecontrol/app/get_self_check_record.md): `SelfCheckRecordModel.fromJson` at `flutter_charging_beginning/beginning/state_cards/self_check/new_system_test_controller.dart @0x2aca808` and `self_check_fail_controller.dart @0x2ad317c`.

## Consumed by

The self-check result and self-check failure cards of the initial setup flow; field-level use is not traced.

## Changed since 3.18.0

The class is new in 3.24.3.

## Known unknowns

- The time format of `start_time` and `end_time` and the status codes other than 1 and 3 are not decoded — traced 2026-10-20: `NewSystemTestController._fetchSelfCheckRecord` (`new_system_test_controller.dart`) reacts only to the values 1 and 3, see the paragraph before Produced by; no time conversion of the two fields was found in that function.
