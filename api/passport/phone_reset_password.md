> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# phone_reset_password

## Purpose

Resets the password with a phone number and an SMS code; sent by `ForgetPwdLogic::startResetPwd` (`charging/ui/page/account/forget_pwd/forget_pwd_logic.dart @0x3bc8838`), which first passes the new password through `StringExtensions.processPassword` with an `EncType` (`@0x3bc88e8`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/phone_reset_password` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3bc8b1c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3bc8b14`, in `HttpRequestControllerImpl::sendForgetPwdPhoneRequest` (`charging/http/http_request_repository_impl.dart @0x3bc89cc`), sent through `encryptionRequestHttp` (`@0x3bc8b44`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `phone_number` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3bc8a2c` (value store `@0x3bc8a3c`) |
| `verify_code` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3bc8a40` (value store `@0x3bc8a50`) |
| `password` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3bc8a54` (value store `@0x3bc8a64`) |
| `client_secret_info` | object | yes | `{"public_key": "<public_key>"}` | `charging/http/http_request_repository_impl.dart @0x3bc8a68` (value store `@0x3bc8aa8`) |

The map literal has type arguments `<String, Object>` (`charging/http/http_request_repository_impl.dart @0x3bc8acc`), which is not evidence of a value type, so the scalar types stay `?`. `client_secret_info` is a nested map literal `<String, String>` (`charging/http/http_request_repository_impl.dart @0x3bc8a94`) with the key `public_key` (`@0x3bc8a80`), value from a parameter (the caller `charging/ui/page/account/forget_pwd/forget_pwd_logic.dart` loads `getClientPublicKey`, `@0x3bc8880`).

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closure (`charging/http/http_request_repository_impl.dart @0x3bc8b60`, shared with `forget_password`) applies a dynamic call to the response value (`@0x3bc8bb0`) and passes the result to the stored callback; the caller's success closure (`forget_pwd_logic.dart @0x3bc920c`, argument type `String`) only logs it (`exeSuccess` `@0x3bc9264`) and shows the dialog `passWordResetSuccess` (`@0x3bc9288`).

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "phone_number": "<phone_number>",
  "verify_code": "<verify_code>",
  "password": "<password>",
  "client_secret_info": {}
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

Codes compared in the failure closure of `startResetPwd` (`forget_pwd_logic.dart @0x3bc8bf0`): 26105 (`@0x3bc8c28`), 26123 (`@0x3bc8cbc`), 100053 (`@0x3bc8ce8`), as listed in `data/errors.json`. Meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `sendForgetPwdPhoneRequest` @0x3bc89cc (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::sendForgetPwdPhoneRequest`
- `charging/ui/page/account/forget_pwd/forget_pwd_logic.dart::startResetPwd`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `phone_number`, `verify_code` and `password`: parameters of the sender stored into a `<String, Object>` literal; the caller reads text fields (`@0x3bc88bc`..`@0x3bc8908`) whose element type was not read.
- What `processPassword` with the `EncType` instance does to the password (hashing or encryption scheme): not read here.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
