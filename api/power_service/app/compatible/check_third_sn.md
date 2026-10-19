> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# check_third_sn

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/compatible/check_third_sn`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x33fa5cc`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_model` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x33fa4e8` |
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x33fa4e8` |
| `brand_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x33fa4e8` |

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

- `charging/http/http_request_repository_impl.dart`: `checkThirdSN` @0x33fa4e8 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::checkThirdSN`
- `charging/ui/page/qr_Scanner/qr_scanner_logic.dart::checkDeviceSnCode`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
