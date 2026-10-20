> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# forget_password

## Purpose

Sends the password-reset e-mail to the address typed on the forgot-password screen; sent by `ForgetPwdLogic::requestForgetPwdApi` (`charging/ui/page/account/forget_pwd/forget_pwd_logic.dart @0x3bc9d74`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/forget_password` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3bc9f98`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3bc9f90`, in `HttpRequestControllerImpl::sendForgetPwdEmailRequest` (`charging/http/http_request_repository_impl.dart @0x3bc9ee4`), sent through `encryptionRequestHttp` (`@0x3bc9fc0`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `email` | string | yes | `"<email>"` | `charging/http/http_request_repository_impl.dart @0x3bc9f38` (value store `@0x3bc9f48`) |

The value is a String: map literal with type arguments `<String, String>` (`@0x3bc9f4c`).

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closure (`charging/http/http_request_repository_impl.dart @0x3bc8b60`) applies a dynamic call to the response value (`@0x3bc8bb0`, selector not named by Blutter) and passes the result to the stored callback (`ClosureCall` `@0x3bc8bcc`); the caller's success closure (`forget_pwd_logic.dart @0x3bca28c`, argument type `String`) only logs it (`exeSuccess` `@0x3bca2d4`) and shows the dialog `forgetPwdEmailHasSent` (`@0x3bca2f8`). No `fromJson` is applied.

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "email": "<email>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

Codes compared in the failure closure of `requestForgetPwdApi` (`forget_pwd_logic.dart @0x3bc9fdc`): 10005 (`@0x3bca020` x, `@0x3bca02c` w), 26105 (`@0x3bca014`, `@0x3bca098`), 26106 (`@0x3bca138`), 100053 (`@0x3bca1a4` x, `@0x3bca1b4` w), as listed in `data/errors.json`. Meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `sendForgetPwdEmailRequest` @0x3bc9ee4 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::sendForgetPwdEmailRequest`
- `charging/ui/page/account/forget_pwd/forget_pwd_logic.dart::requestForgetPwdApi`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the server answers on success: the app never reads the body (see Response model).
- Whether the reset link expires and how long: not visible in the app. — reclassified: server (2026-10-20: link lifetime is not visible in the app)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
