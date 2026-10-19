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

## Produced by

[`get_self_check_record`](../api/devicecontrol/app/get_self_check_record.md): `SelfCheckRecordModel.fromJson` at `flutter_charging_beginning/beginning/state_cards/self_check/new_system_test_controller.dart @0x2aca808` and `self_check_fail_controller.dart @0x2ad317c`.

## Consumed by

The self-check result and self-check failure cards of the initial setup flow; field-level use is not traced.

## Changed since 3.18.0

The class is new in 3.24.3.

## Known unknowns

- The self-check status codes and the time format of `start_time` and `end_time` are not decoded.
