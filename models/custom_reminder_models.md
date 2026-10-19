> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# Custom reminder models (Prime charger)

## Purpose

Carries the custom reminders of a small charging platform device (the Anker Prime charger display): one reminder with its schedule, and the list answer.

## Dart class + file

`CustomReminderItem` (`small_charging_platform/src/custom_reminder/model/custom_reminder_item.dart`); `CustomReminderListResponse` (`small_charging_platform/src/custom_reminder/model/custom_reminder_item.dart`). `fromJson` addresses are under each class below.

## Fields

Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Dart types and nullability come from `tools/model_fields.py` (`data/models.json`).

### CustomReminderItem

One reminder; also the shape sent to `set_reminder` (`toJson`).

`fromJson` `custom_reminder_item.dart @0x2a53530`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `id` | `unknown` | ? | 3.24.3 | `custom_reminder_item.dart @0x2a53564` |
| `device_sn` | `String?` | yes | 3.24.3 | `custom_reminder_item.dart @0x2a535b4` |
| `reminder_type` | `unknown` | ? | 3.24.3 | `custom_reminder_item.dart @0x2a53638` |
| `title` | `String?` | yes | 3.24.3 | `custom_reminder_item.dart @0x2a53688` |
| `image_url` | `String?` | yes | 3.24.3 | `custom_reminder_item.dart @0x2a53708` |
| `hash_code` | `String?` | yes | 3.24.3 | `custom_reminder_item.dart @0x2a5378c` |
| `cycle_type` | `unknown` | ? | 3.24.3 | `custom_reminder_item.dart @0x2a53810` |
| `repeat_week_mask` | `unknown` | ? | 3.24.3 | `custom_reminder_item.dart @0x2a53860` |
| `interval_hour` | `unknown` | ? | 3.24.3 | `custom_reminder_item.dart @0x2a538b0` |
| `status` | `unknown` | ? | 3.24.3 | `custom_reminder_item.dart @0x2a53900` |
| `start_time` | `unknown` | ? | 3.24.3 | `custom_reminder_item.dart @0x2a53950` |
| `end_time` | `unknown` | ? | 3.24.3 | `custom_reminder_item.dart @0x2a5399c` |

### CustomReminderListResponse

Answer of `get_reminder_list`: the reminders under one of three possible keys.

`fromJson` `custom_reminder_item.dart @0x2a5327c`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `items` | `unknown` | yes | 3.24.3 | `custom_reminder_item.dart @0x2a532b0` |
| `reminder_list` | `unknown` | yes | 3.24.3 | `custom_reminder_item.dart @0x2a532dc` |
| `list` | `List` of `CustomReminderItem` | no | 3.24.3 | `custom_reminder_item.dart @0x2a53304` |

## Produced by

- [`get_reminder_list`](../api/mini_power/app/reminder/get_reminder_list.md): `CustomReminderListResponse`
- [`set_reminder`](../api/mini_power/app/reminder/set_reminder.md): sends `CustomReminderItem.toJson` (12 keys, `custom_reminder_item.dart @0x2a53a68` to `@0x2a53b70`, the same names as the table)

## Consumed by

The reminder manager and editor of the `small_charging_platform` package (`CustomReminderManagerLogic`, `CustomReminderEditLogic`); field-level use is not traced.

## Changed since 3.18.0

Both classes are new in 3.24.3.

## Known unknowns

- `CustomReminderListResponse.fromJson` reads the keys `items`, `reminder_list` and `list` in that order and maps the first list found to `CustomReminderItem`; which key the server uses is not known (the extractor lists all three as keys).
- The values of `reminder_type`, `cycle_type`, `repeat_week_mask`, `interval_hour` and `status`, and the unit of `start_time`/`end_time`, are not decoded (the extractor could not resolve their types).
