> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_system_device_time

## Purpose

Reads the current device time of a station for the manual backup power page (`ManualBackupPowerLogic::_getDeviceCurrentTime`; callers `retryGet` and `updateUiAndParams`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_system_device_time` (asm-traced): URL string at `charging/ui/page/device/a5101/setting/manual_backup_power/manual_backup_power_logic.dart @0x29734e8`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x29734e0`, in `ManualBackupPowerLogic::_getDeviceCurrentTime` (`charging/ui/page/device/a5101/setting/manual_backup_power/manual_backup_power_logic.dart @0x29733e8`), sent through `requestHttp` (`@0x2973510`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `ManualBackupPowerLogic::_getDeviceCurrentTime` (`charging/ui/page/device/a5101/setting/manual_backup_power/manual_backup_power_logic.dart`, call `@0x2973510`, argument list `@0x2973508`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `ManualBackupPowerLogic::_getDeviceCurrentTime` (`charging/ui/page/device/a5101/setting/manual_backup_power/manual_backup_power_logic.dart @0x297349c`, 1 key). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `StationId` | string | yes | `"<StationId>"` | `charging/ui/page/device/a5101/setting/manual_backup_power/manual_backup_power_logic.dart @0x2973488` |

## `param_type`/`cmd`

n/a

## Response model (link)

- `charging::ManualBackupTimeModel`, parsed by `ManualBackupTimeModel.fromJson` at `charging/ui/page/device/a5101/setting/manual_backup_power/manual_backup_power_logic.dart @0x2973610` (success closure `@0x29735d8`, `bl` target `[package:charging/model/a5101/manual_backup_time_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::ManualBackupTimeModel`): `deviceTime` (String?), `timeStamp` (int?), `timeLocation` (String?).

App side use (traced 2026-10-20): the success closure of `ManualBackupPowerLogic::_getDeviceCurrentTime` (`charging/ui/page/device/a5101/setting/manual_backup_power/manual_backup_power_logic.dart @0x29735d8`) logs the model with `jsonEncode` (`@0x2973638`), stores `timeLocation` (`field_f`, fallback `""`) in the logic field `field_af` (`@0x29736c4`) and calls `_calculateShowDateAndTime` (`@0x29736f4`) with `deviceTime` (`field_7`, fallback `""`) and `defaultTime: true`; `timeStamp` is not read. With `defaultTime` true that function applies a `parse` call (selector not named by Blutter) to the text (`@0x2972fa8`) and reads the date and time parts from the result; with it false it converts through `convertTimezoneToDateTime` with the stored `timeLocation` (`@0x297317c`, `@0x2973198`), so `timeLocation` is used as the zone name for that conversion.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "StationId": "<StationId>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a5101/setting/manual_backup_power/manual_backup_power_logic.dart`: `_getDeviceCurrentTime` @0x29733e8 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/device/a5101/setting/manual_backup_power/manual_backup_power_logic.dart::retryGet`
- `charging/ui/page/device/a5101/setting/manual_backup_power/manual_backup_power_logic.dart::updateUiAndParams`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The time zone and format of the returned time: only the parse was read. — traced 2026-10-20: narrowed, see Response (app side use); the text pattern accepted by the `parse` call at `manual_backup_power_logic.dart @0x2972fa8` is not named in the asm
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
