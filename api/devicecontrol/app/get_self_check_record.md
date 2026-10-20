> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_self_check_record

## Purpose

Reads the last self-check record of a device in a system (status, start and end time); the self-check result and failure cards of the initial setup flow use it.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /devicecontrol/v1/app/get_self_check_record` (asm-traced). Two senders, both named `_fetchSelfCheckRecord`: in `NewSystemTestController` (`flutter_charging_beginning/beginning/state_cards/self_check/new_system_test_controller.dart @0x2aca588`; URL literal `@0x2aca6d8`, `Method.post` pool entry `pp+0xa7e0`, `@0x2aca6d0`) and in `SelfCheckFailController` (`flutter_charging_beginning/beginning/state_cards/self_check/self_check_fail_controller.dart @0x2ad2f1c`; URL `@0x2ad306c`, `Method.post` `@0x2ad3064`).

## Encrypted?

`encryptionRequestHttp` (`flutter_charging_beginning/beginning/state_cards/self_check/new_system_test_controller.dart @0x2aca700`, `self_check_fail_controller.dart @0x2ad3090`) without `needEncryption`, so the default `true` applies ([which calls are encrypted](../../encryption.md#which-calls-are-encrypted)); whether the call goes through the SDK is decided at run time. The first sender turns the loading overlay on (`r30 = true`, `@0x2aca6e8`).

## Request

Map literal with two string pairs, `<String, String>`, identical in both senders.

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | String | yes | `"<site id>"` | `flutter_charging_beginning/beginning/state_cards/self_check/new_system_test_controller.dart @0x2aca5f8` (value: object field at offset 0x4b, `@0x2aca608`); `self_check_fail_controller.dart @0x2ad2f8c` |
| `device_sn` | String | yes | `"<device sn>"` | `@0x2aca614` (value: a getter on the object field at offset 0x47, empty string if null, `@0x2aca620` to `@0x2aca65c`); `@0x2ad2fa8` |

## `param_type`/`cmd`

n/a

## Response model (link)

`SelfCheckRecordModel` ([../../../models/self_check_record_model.md](../../../models/self_check_record_model.md)), `fromJson` called at `flutter_charging_beginning/beginning/state_cards/self_check/new_system_test_controller.dart @0x2aca808` (success closure `@0x2aca7d0`) and `self_check_fail_controller.dart @0x2ad317c`.

## Response

All fields live in the model page (wrapper `code`, `msg`, `data` as in [encryption.md](../../encryption.md#response-handling-and-error-codes)). The failure closures only log `_fetchSelfCheckRecord fail` (`new_system_test_controller.dart @0x2aca760`).

## Example request/response

Request, synthesized

```json
{ "site_id": "<site id>", "device_sn": "<device sn>" }
```

Response: no captured response; the key list is on the model page.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or logs it; the shared transport codes are in [encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- `NewSystemTestController._fetchSelfCheckRecord` (`flutter_charging_beginning/beginning/state_cards/self_check/new_system_test_controller.dart @0x2aca588`), called from `onReady`: the new-system test (self-check) card of the initial setup flow (package `flutter_charging_beginning`).
- `SelfCheckFailController._fetchSelfCheckRecord` (`flutter_charging_beginning/beginning/state_cards/self_check/self_check_fail_controller.dart @0x2ad2f1c`), called from `onReady`: the self-check failure card of the same flow.

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 pool as a code-referenced URL; see the inventory row `since`). 3.24.3: present (new). since: 3.24.3. `SelfCheckRecordModel` is new in 3.24.3.

## Known unknowns

- The value domains of `self_check_status` and the time format of `start_time` and `end_time` are not decoded (the report call [self_check_report](self_check_report.md) sends integers for the times). — reclassified: device test row 157 (2026-10-20: status values and time format come from the stored report of the device self check)
- Server behaviour is not known.

## Device-tested by

none
