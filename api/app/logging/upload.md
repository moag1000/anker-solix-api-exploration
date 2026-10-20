> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# upload

## Purpose

Tells the server that a log file has been uploaded to storage and gives its URL; sent by `DeviceLogsLogic::_notifyServer` (device logs, called from `_putFile`) and `UploadLogLogic::uploadLogURL` (app log, called from `uploadAppLogData`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/logging/upload` (asm-traced): URL string at `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133e68`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3133e60`, in `DeviceLogsLogic::_notifyServer` (`charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133b80`), sent through `encryptionRequestHttp` (`@0x3133e8c`).

Same URL in the other sender(s) read:

- `POST /app/logging/upload` (asm-traced): URL string at `charging/ui/page/user/upload_log/upload_log_logic.dart @0x46b6520`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x46b6518`, in `UploadLogLogic::uploadLogURL` (`charging/ui/page/user/upload_log/upload_log_logic.dart @0x46b62e0`), sent through `encryptionRequestHttp` (`@0x46b6544`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `url` | ? | yes | ? | `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133c90` (value store `@0x3133ca8`) |
| `source` | string | yes | `"app"` | `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133cac` (value store `@0x3133cbc`) |
| `logging_time` | int (unboxed, x) | yes | ? | `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133cc0` (value store `@0x3133cec`) |
| `level` | string | yes | `"info"` | `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133d10` (value store `@0x3133d24`) |
| `os` | string | yes | `"android"` | `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133d28` (value store `@0x3133d38`) |
| `version` | string | yes | `"<version>"` | `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133d3c` (value store `@0x3133d50`) |
| `app_version` | string | yes | `"<app_version>"` | `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133d74` (value store `@0x3133d88`) |
| `related_device_sn` | ? | yes | ? | `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133dac` (value store `@0x3133dc0`) |
| `device_sn` | ? | yes | ? | `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133de4` (value store `@0x3133df8`) |

Union over the two senders; the table lists the keys of `DeviceLogsLogic::_notifyServer` (`charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133b80`, map literal `<String, Object?>` `@0x3133e1c`), which is not evidence of a value type. `UploadLogLogic::uploadLogURL` (`charging/ui/page/user/upload_log/upload_log_logic.dart @0x46b62e0`, map literal `<String, dynamic>` `@0x46b64d8`) sends the same keys except `related_device_sn` and `device_sn`. `logging_time` is boxed by `BoxInt64Instr` (`@0x3133cd4`, `@0x46b6400`), so it is an unboxed int (in `uploadLogURL` the value is the current time in milliseconds computed with `sdiv`). `source` is `"app"`, `level` `"info"` and `os` `"android"` in both senders (constants; no platform test was found in the senders). `version` and `app_version` are awaited results of `systemVersion` and `appVersion` (`@0x3133c6c`, `@0x3133c58`); both functions declare `InitAsync() -> Future<String>` (`charging/util/device_util.dart @0x225093c` and `@0x224ee44`), so both values are strings (one-hop evidence).

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closures never read their response argument; `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133ef4` calls the stored callback (`ClosureCall` `@0x3133f2c`) and `charging/ui/page/user/upload_log/upload_log_logic.dart @0x46b662c` deletes the uploaded file, cuts the log file and records the upload time (`_deleteUploadFile` `@0x46b666c`, `cutUploadLogFile` `@0x46b668c`, `eventTrackUploadLogInfo` `@0x46b6728`). No `fromJson`.

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "url": "<url>",
  "source": "app",
  "logging_time": "<logging_time>",
  "level": "info",
  "os": "android",
  "version": "<version>",
  "app_version": "<app_version>",
  "related_device_sn": "<related_device_sn>",
  "device_sn": "<device_sn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or its closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart`: `_notifyServer` @0x3133b80 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/user/upload_log/upload_log_logic.dart`: `uploadLogURL` @0x46b62e0 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart::_putFile`
- `charging/ui/page/user/upload_log/upload_log_logic.dart::uploadAppLogData`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `url` (a field in `_notifyServer`, a parameter in `uploadLogURL`), `related_device_sn` and `device_sn` (parameters of `_notifyServer`): no declared type was read at the callers.
- Whether `source: "app"` and `os: "android"` are replaced on iOS: no branch was found in the senders. — reclassified: device test row 161 (2026-10-20: the workspace holds the Android build only, so an iOS branch cannot be checked here)
- How the failure path works: `uploadLogURL` calls `uploadLogFail` (`charging/ui/page/user/upload_log/upload_log_logic.dart @0x46b6568`); the failure closures were not decoded.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
