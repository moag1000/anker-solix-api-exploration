> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# del_reminder

## Purpose

Deletes one custom reminder of a Prime-class charger by id.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /mini_power/v1/app/reminder/del_reminder` (asm-traced). Sender: `CustomReminderCloudApi.deleteReminder` (`small_charging_platform/src/custom_reminder/http/custom_reminder_cloud_api.dart @0x2f2d794`); the URL literal is loaded at `@0x2f2d864` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x2f2d85c`).

## Encrypted?

Yes by wrapper (asm-traced): `deleteReminder` calls `HttpServiceImpl.encryptionRequestHttp` (`small_charging_platform/src/custom_reminder/http/custom_reminder_cloud_api.dart @0x2f2d88c`) with the named arguments `fail`, `showLoading` and `success` (`@0x2f2d884`) and without `needEncryption`, so the default `true` applies ([encryption.md](../../../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../../../encryption.md)); asm alone does not decide it.

## Request

Body is a `<String, int>` map of one pair (`r2 = 4`, `@0x2f2d7fc`).

| field | type | required | example | source |
|---|---|---|---|---|
| `id` | int | yes | `7` | `custom_reminder_cloud_api.dart @0x2f2d808`; the argument |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the answer is not parsed by this function.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "id": 7 }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `CustomReminderManagerLogic.deleteReminder` (`small_charging_platform/src/custom_reminder/custom_reminder_manager/custom_reminder_manager_logic.dart @0x2f2d77c`)
- `CustomReminderEditLogic._submitDeleteReminder` (`small_charging_platform/src/custom_reminder/custom_reminder_edit/custom_reminder_edit_logic.dart @0x3a7bc1c`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0xa2fc0`). since: 3.24.3.

## Known unknowns

- Whether deleting a reminder also removes it from the device is not traced (the device side is a separate BLE or MQTT command).

## Device-tested by

none
