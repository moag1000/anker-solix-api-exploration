> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# set_mode_sub_status

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/mini_power/v1/app/setting/set_mode_sub_status`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x38aa4f4`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x38aa3fc` |
| `mode` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x38aa3fc` |
| `protocol_key` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x38aa3fc` |
| `status` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x38aa3fc` |

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

- `charging/http/http_request_repository_impl.dart`: `setA2687ModeSubStatus` @0x38aa3fc (encryptionRequestHttp; encrypted: true)

Called from: `charging/ui/page/device/a2687/a2687setting/a2687_charge_mode/a2687_charge_mode_logic.dart::setModeSubStatus`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
