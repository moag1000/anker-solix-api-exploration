> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# phone_bind_account

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/passport/phone_bind_account`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x3bc313c`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `phone_number` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bc2f9c` |
| `verify_code` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bc2f9c` |
| `access_token` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bc2f9c` |
| `third_party` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bc2f9c` |
| `client_secret_info.public_key` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bc2f9c` |
| `open_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bc2f9c` |

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

- `charging/http/http_request_repository_impl.dart`: `bindPhoneNumberRequest` @0x3bc2f9c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::bindPhoneNumberRequest`
- `charging/ui/page/account/bind_phone_number/bind_phone_number_logic.dart::bindPhoneNumberWithApple`
- `charging/ui/page/account/bind_phone_number/bind_phone_number_logic.dart::bindPhoneNumberWithWechat`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
