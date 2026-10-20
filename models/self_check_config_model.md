> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# SelfCheckConfigItem

## Purpose

Carries one entry of the cloud self-check configuration: a check id, its type, title, text and image, shown on the self-check and self-check-failure screens of the initial setup.

## Dart class + file

`SelfCheckConfigItem` (`flutter_charging_beginning/beginning/state_cards/self_check/self_check_config_model.dart`). `fromJson` addresses are under each class below.

## Fields

Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Dart types and nullability come from `tools/model_fields.py` (`data/models.json`); an "of `X`" note is the list element class read from the `<X>` type argument next to the key.

### SelfCheckConfigItem

One entry of the answer of `get_self_check_config`.

`fromJson` `self_check_config_model.dart @0x2ad23f0`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `checkId` | `int?` | yes | 3.24.3 | `self_check_config_model.dart @0x2ad2410` |
| `content` | `String?` | yes | 3.24.3 | `self_check_config_model.dart @0x2ad2498` |
| `imageUrl` | `String?` | yes | 3.24.3 | `self_check_config_model.dart @0x2ad2520` |
| `checkType` | `int?` | yes | 3.24.3 | `self_check_config_model.dart @0x2ad25a4` |
| `title` | `String?` | yes | 3.24.3 | `self_check_config_model.dart @0x2ad262c` |

Wrapper `SelfCheckConfigModel.fromJson` (traced 2026-10-20, `self_check_config_model.dart @0x2ad1404`): the argument is the answer itself, not a key of an object. A non-empty `String` is decoded with `JsonCodec.decode` first (class-id test `@0x2ad143c` to `@0x2ad1444`, decode `@0x2ad145c`); when the value is then a `List` (`InstanceOf` `@0x2ad1518`) its elements are mapped through the closure `@0x2ad1544` that builds `SelfCheckConfigItem` (type argument `@0x2ad1558`, `toList` `@0x2ad159c`) and stored in the model's single field (`@0x2ad15b4`); any other value leaves the field unset.

## Produced by

- [`get_self_check_config`](../api/device_svc/get_self_check_config.md): `SelfCheckConfigModel.fromJson` (`flutter_charging_beginning/beginning/state_cards/self_check/self_check_config_model.dart @0x2ad1404`) maps the answer to a list of `SelfCheckConfigItem` (type argument `@0x2ad1558`); the wrapper class `SelfCheckConfigModel` itself has no JSON key in `data/models.json`.

## Consumed by

`SelfCheckController` and `SelfCheckFailController` of the initial setup flow; field-level use is not traced.

## Changed since 3.18.0

The class is new in 3.24.3.

## Known unknowns

- The meaning of `checkType` and the relation of `checkId` to the failure codes (see [self_check_report](../api/devicecontrol/app/self_check_report.md)) are not decoded. — traced 2026-10-20: not traced; no enum for `checkType` is in the object dump (class names searched).
