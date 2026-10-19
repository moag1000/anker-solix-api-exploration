> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# resend_active_email

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/passport/resend_active_email`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x2fb0100`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `email` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x2fb004c` |

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

- `charging/http/http_request_repository_impl.dart`: `sendVerifyEmailRequest` @0x2fb004c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::sendVerifyEmailRequest`
- `charging/ui/page/account/forget_pwd/forget_pwd_logic.dart::activeEmail`
- `charging/ui/page/account/login/login_logic.dart::activeEmail`
- `charging/ui/page/account/privacy_policy/verification/verification_logic.dart::_activeEmail`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
