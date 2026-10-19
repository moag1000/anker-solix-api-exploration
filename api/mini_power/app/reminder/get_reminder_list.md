> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_reminder_list

## Purpose

Lists the custom reminders of a Prime-class charger (small charging platform), or fetches one reminder by id; the reminder manager, the editor's schedule-conflict check and the reminder image generator call it.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /mini_power/v1/app/reminder/get_reminder_list` (asm-traced). Sender: `CustomReminderCloudApi.getReminderList` (`small_charging_platform/src/custom_reminder/http/custom_reminder_cloud_api.dart @0x2a530b0`); the URL literal is loaded at `@0x2a531bc` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x2a531b4`).

## Encrypted?

Yes by wrapper (asm-traced): `getReminderList` calls `HttpServiceImpl.encryptionRequestHttp` (`small_charging_platform/src/custom_reminder/http/custom_reminder_cloud_api.dart @0x2a531e4`) with the named arguments `fail`, `showLoading` and `success` (`@0x2a531dc`) and without `needEncryption`, so the default `true` applies ([encryption.md](../../../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../../../encryption.md)); asm alone does not decide it.

## Request

Body is a `<String, int>` map: `{ "id": <id> }` when the optional named argument `id` is not null (`SetupParameters` `@0x2a530bc`, map `@0x2a53180`), otherwise an empty map (`@0x2a53190`).

| field | type | required | example | source |
|---|---|---|---|---|
| `id` | int | no | `7` | `custom_reminder_cloud_api.dart @0x2a53164`; value is the named argument `id` (`@0x2a53170`) |

Without `id` the answer is the list of the account's reminders (inferred from the optional key); the Prime charger's serial number is not sent here, the reminder items carry `device_sn` themselves.

## `param_type`/`cmd`

n/a

## Response model (link)

`CustomReminderListResponse` ([../../../../models/custom_reminder_models.md](../../../../models/custom_reminder_models.md#customreminderlistresponse)) with element class `CustomReminderItem`: the parser is `CustomReminderListResponse.fromJson` (`small_charging_platform/src/custom_reminder/model/custom_reminder_item.dart @0x2a5327c`).

## Response

`fromJson` reads the keys `items` (`@0x2a532b0`), `reminder_list` (`@0x2a532dc`) and `list` (`@0x2a53304`) and maps the first list it finds to `CustomReminderItem` objects (`@0x2a53414` to `@0x2a53458`). The success and failure closures of `getReminderList` are passed on to the caller (`@0x2a53204` closure).

| field | type | required | example | source |
|---|---|---|---|---|
| `items` / `reminder_list` / `list` | list of `CustomReminderItem` | no | `[ { "id": 7, "device_sn": "...", "title": "..." } ]` | `custom_reminder_item.dart @0x2a532b0`, `@0x2a532dc`, `@0x2a53304`; item keys on the [model page](../../../../models/custom_reminder_models.md#customreminderitem) |

## Example request/response

Request, synthesized

```json
{}
```

Request, synthesized (one reminder)

```json
{ "id": 7 }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `CustomReminderManagerLogic._fetchReminderListFromCloud` (`small_charging_platform/src/custom_reminder/custom_reminder_manager/custom_reminder_manager_logic.dart @0x2a53094`)
- `CustomReminderEditLogic._checkScheduleConflictBeforeSave` (`small_charging_platform/src/custom_reminder/custom_reminder_edit/custom_reminder_edit_logic.dart @0x3a83d90`)
- `ReminderImageGenerator._fetchFreshImageUrl` (`small_charging_platform/src/scp/utils/reminder_image_generator.dart @0x2a71af0`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0xa2e40`). since: 3.24.3.

## Known unknowns

- Whether the server filters the list by device (the app sends no `device_sn`) is not known.
- No response was captured; the answer key (`items`, `reminder_list` or `list`) is not known.

## Device-tested by

none
