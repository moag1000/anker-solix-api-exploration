> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# resend_active_email

## Purpose

Asks the server to send the account activation e-mail again; sent by the login screen (`LoginLogic::activeEmail`), the forgot-password screen (`ForgetPwdLogic::activeEmail`) and the verification screen (`VerificationLogic::_activeEmail`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/resend_active_email` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x2fb0100`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2fb00f8`, in `HttpRequestControllerImpl::sendVerifyEmailRequest` (`charging/http/http_request_repository_impl.dart @0x2fb004c`), sent through `encryptionRequestHttp` (`@0x2fb0128`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `email` | string | yes | `"<email>"` | `charging/http/http_request_repository_impl.dart @0x2fb00a0` (value store `@0x2fb00b0`) |

The value is a String: map literal with type arguments `<String, String>` (`@0x2fb00b4`).

## `param_type`/`cmd`

n/a

## Response model (link)

[`Result`](../../models/other.md#result), parsed by `Result.fromJson` at `charging/http/http_request_repository_impl.dart @0x2fb0264` in the success closure `@0x2fb01f8`.

## Response

(asm-traced) Top-level keys of `Result` (`data/models.json`, `charging::Result`): `code` (int?), `msg` (String?), `data` (unknown), `signature` (String?). The closure passes the parsed `Result` to the stored callback (`ClosureCall` `@0x2fb0280`).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "email": "<email>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

Codes compared in the failure closures of `LoginLogic::activeEmail` (`login_logic.dart`): 10005 (`@0x2fb0a04`, `@0x2fb0a7c`), 26053 (`@0x2fb0ae8`, `@0x2fb0af4`), 100053 (`@0x2fb0b60` x, `@0x2fb0b70` w), as listed in `data/errors.json`; the other two callers are forwarding closures. Meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `sendVerifyEmailRequest` @0x2fb004c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::sendVerifyEmailRequest`
- `charging/ui/page/account/forget_pwd/forget_pwd_logic.dart::activeEmail`
- `charging/ui/page/account/login/login_logic.dart::activeEmail`
- `charging/ui/page/account/privacy_policy/verification/verification_logic.dart::_activeEmail`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- How the two other callers (`ForgetPwdLogic::activeEmail`, `VerificationLogic::_activeEmail`) handle failures: their closures only forward to the sender and were not decoded further.
- Rate limits of the activation mail: only the code 100053 compare is known (`api/errors.md`). — reclassified: server (2026-10-20: rate limits are not visible in the app)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
