> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_device_logging

## Purpose

Polls whether the device log that the user asked for has been uploaded; sent from a closure of `DeviceLogsLogic::_pollUploadState` (`charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x29224f0`) (asm-traced for the call site; the inventory lists no named caller).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/logging/get_device_logging` (asm-traced): URL string at `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x2922598`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2922590`, in `DeviceLogsLogic::<anonymous closure> in DeviceLogsLogic::_pollUploadState` (`charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x29224f0`), sent through `encryptionRequestHttp` (`@0x29225bc`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `upload_id` | string | yes | `"<upload_id>"` | `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x2922530` (value store `@0x2922548`) |

The value is a String: map literal with type arguments `<String, String>` (`charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x292254c`); it is read from a field of the polling state object (`@0x2922540`).

Source of `upload_id` (traced 2026-10-20, app side): the success closure of `_notifyServer` (`charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3134588`) builds the id itself by string interpolation (`_interpolate` `@0x3134638`) of three parts: a text derived from `field_13` of its context by a one-receiver selector (`GDT[cid_x0 + 0x2abf7]` `@0x31345d4`, not named by Blutter), the separator `" "` (`@0x3134604`) and an integer (`field_27` of the first context slot, boxed by `BoxInt64Instr` `@0x313461c`). The result is passed to `_saveWifiPending` (`@0x3134698`) and `_pollUploadState` (`@0x31346b4`), which keeps it as `field_13` of the poll context read for the request. So the id comes from the app, composed from the log task data, not from a server answer; what `field_13` and `field_27` hold is not decoded.

## `param_type`/`cmd`

n/a

## Response model (link)

no model: the success closure (`charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x2922814`) tests that the response is a `Map` (`@0x29228e8`) and reads the key `url` (key string `@0x292294c`, lookup `@0x2922968`) as `String?` (`@0x29229a4`). A non-empty `url` (`cbnz` `@0x29229b8`) leads to `_pushPollState` (`@0x29229f8`) and `_finishTask` (`@0x2922a24`); a missing or empty value, or a response that is not a map, calls `_recheckPoll` (`@0x2922930`, `@0x29229d8`) so the poll runs again.

## Response

(asm-traced) One key is read from the top level of the response: `url` (String, nullable). Whether it is the download link of the device log is inferred from the key name (string-only).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "upload_id": "<upload_id>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or its closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart`: `<anonymous closure> in DeviceLogsLogic::_pollUploadState` @0x29224f0 (encryptionRequestHttp; encrypted: true)

Poll rule (app side, traced 2026-10-20, `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart`): `_pollUploadState` (`@0x2921f38`..`@0x29220b8`) starts a one-shot `Timer` with a constant `Duration` of 6000000 microseconds (`pp+0x36d40`, `@0x29220b0`), that is 6 seconds, and `_recheckPoll` (`@0x292270c`) logs `deviceLog_pollCount=` with the count and `max=` (`@0x2922758`, `@0x2922780`), compares the count with 100 as an unboxed integer (`cmp x1, #0x64` `@0x29227b0`, branch `@0x29227b4`) and polls again below it (`_pollUploadState` `@0x29227c4`) or ends the task with `_finishTask` (`@0x29227f8`). So the app asks at most 100 times every 6 seconds, about ten minutes.

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The meaning of `url` (a link to the uploaded device log, by name only): not an app-side fact — reclassified: server (2026-10-20); the poll interval and the retry limit are in Callers in app.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
