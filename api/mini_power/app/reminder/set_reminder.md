> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# set_reminder

## Purpose

Creates or changes one custom reminder of a Prime-class charger (title, image, schedule, status); the reminder editor saves with it and the manager toggles a reminder's status with it.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /mini_power/v1/app/reminder/set_reminder` (asm-traced). Sender: `CustomReminderCloudApi.setReminder` (`small_charging_platform/src/custom_reminder/http/custom_reminder_cloud_api.dart @0x3a84718`); the URL literal is loaded at `@0x3a847ac` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x3a847a4`).

## Encrypted?

Yes by wrapper (asm-traced): `setReminder` calls `HttpServiceImpl.encryptionRequestHttp` (`small_charging_platform/src/custom_reminder/http/custom_reminder_cloud_api.dart @0x3a847d4`) with the named arguments `fail`, `showLoading` and `success` (`@0x3a847cc`) and without `needEncryption`, so the default `true` applies ([encryption.md](../../../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../../../encryption.md)); asm alone does not decide it.

## Request

Body is `CustomReminderItem.toJson()` of the first argument (`toJson` call `@0x3a84780`); the keys are those of the model (`custom_reminder_item.dart @0x2a53a68` to `@0x2a53b70`):

| field | type | required | example | source |
|---|---|---|---|---|
| `id` | int | no (new reminder) | `7` | `custom_reminder_item.dart @0x2a53a68` |
| `device_sn` | String? | yes | `<device sn>` | `custom_reminder_item.dart @0x2a53a84` |
| `reminder_type` | int? | yes | `1` | `custom_reminder_item.dart @0x2a53a9c`; meaning not decoded |
| `title` | String? | yes | `Medication` | `custom_reminder_item.dart @0x2a53ab4` |
| `image_url` | String? | no | `https://...` | `custom_reminder_item.dart @0x2a53ac8` |
| `hash_code` | String? | no | `<hash>` | `custom_reminder_item.dart @0x2a53ae0` |
| `cycle_type` | int? | yes | `1` | `custom_reminder_item.dart @0x2a53af8`; meaning not decoded |
| `repeat_week_mask` | int? | no | `127` | `custom_reminder_item.dart @0x2a53b10`; probably a weekday bit mask (inferred from the name) |
| `interval_hour` | int? | no | `2` | `custom_reminder_item.dart @0x2a53b28` |
| `status` | int? | yes | `1` | `custom_reminder_item.dart @0x2a53b40`; the manager sets it when it toggles a reminder |
| `start_time` | int? | yes | `28800` | `custom_reminder_item.dart @0x2a53b58`; unit not decoded |
| `end_time` | int? | no | `64800` | `custom_reminder_item.dart @0x2a53b70`; unit not decoded |

The types and example values come from the extractor (`unknown`) and are placeholders; only the key names are asm-traced. The `showLoading` flag is `false` (`@0x3a847bc`).

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the answer is not parsed by this function; the success closure comes from the caller.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "id": 7, "device_sn": "<device sn>", "reminder_type": 1, "title": "Medication", "image_url": "", "hash_code": "", "cycle_type": 1, "repeat_week_mask": 127, "interval_hour": 2, "status": 1, "start_time": 28800, "end_time": 64800 }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `CustomReminderManagerLogic.toggleReminderStatus` (`small_charging_platform/src/custom_reminder/custom_reminder_manager/custom_reminder_manager_logic.dart @0x3a8cce0`)
- `CustomReminderEditLogic._startCloudSave` (`small_charging_platform/src/custom_reminder/custom_reminder_edit/custom_reminder_edit_logic.dart @0x3a84620`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0xa2f78`). since: 3.24.3.

## Known unknowns

- The meaning and range of `reminder_type`, `cycle_type`, `repeat_week_mask`, `interval_hour` and `status` and the time unit are not decoded.
- Whether a missing `id` creates a reminder (and the answer returns the new id) is inferred, not traced.

## Device-tested by

none
