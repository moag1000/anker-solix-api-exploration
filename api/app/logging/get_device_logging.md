> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_device_logging

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/app/logging/get_device_logging`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x2922598`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `upload_id` | ? | ? | ? | `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x29224f0` |

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

- `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart`: `<anonymous closure> in DeviceLogsLogic::_pollUploadState` @0x29224f0 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
