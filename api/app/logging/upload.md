> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# upload

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/app/logging/upload`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133e68`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `url` | ? | ? | ? | `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133b80` |
| `source` | ? | ? | ? | `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133b80` |
| `logging_time` | ? | ? | ? | `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133b80` |
| `level` | ? | ? | ? | `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133b80` |
| `os` | ? | ? | ? | `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133b80` |
| `version` | ? | ? | ? | `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133b80` |
| `app_version` | ? | ? | ? | `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133b80` |
| `related_device_sn` | ? | ? | ? | `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133b80` |
| `device_sn` | ? | ? | ? | `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133b80` |

Rows are the union over 2 senders; `source` is the first sender that sets the key.

## `param_type`/`cmd`

n/a

## Response model (link)

<!-- TODO -->

## Response

<!-- TODO -->

## Example request/response

<!-- TODO -->

## Errors seen

`api/errors.md`: <!-- TODO -->

## Callers in app

- `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart`: `_notifyServer` @0x3133b80 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/user/upload_log/upload_log_logic.dart`: `uploadLogURL` @0x46b62e0 (encryptionRequestHttp; encrypted: true)

Called from: `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart::_putFile`, `charging/ui/page/user/upload_log/upload_log_logic.dart::uploadAppLogData`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
