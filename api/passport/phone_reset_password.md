> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# phone_reset_password

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/passport/phone_reset_password`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x3bc8b1c`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `phone_number` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bc89cc` |
| `verify_code` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bc89cc` |
| `password` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bc89cc` |
| `client_secret_info.public_key` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bc89cc` |

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

- `charging/http/http_request_repository_impl.dart`: `sendForgetPwdPhoneRequest` @0x3bc89cc (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::sendForgetPwdPhoneRequest`
- `charging/ui/page/account/forget_pwd/forget_pwd_logic.dart::startResetPwd`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
