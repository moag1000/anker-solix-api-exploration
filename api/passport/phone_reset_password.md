> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

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
| `phone_number` | string | yes |  | `charging/http/http_request_repository_impl.dart @0x3bc8a2c` (value store `@0x3bc8a3c`) |
| `verify_code` | string | yes |  | `charging/http/http_request_repository_impl.dart @0x3bc8a40` (value store `@0x3bc8a50`) |
| `password` | string | yes |  | `charging/http/http_request_repository_impl.dart @0x3bc8a54` (value store `@0x3bc8a64`) |
| `client_secret_info` | object | yes | `{"public_key": "<public_key>"}` | `charging/http/http_request_repository_impl.dart @0x3bc8a68` (value store `@0x3bc8aa8`) |

The map literal has type arguments `<String, Object>` (`charging/http/http_request_repository_impl.dart @0x3bc8acc`), which is not evidence of a value type; the scalar types come from the caller (see below). `client_secret_info` is a nested map literal `<String, String>` (`charging/http/http_request_repository_impl.dart @0x3bc8a94`) with the key `public_key` (`@0x3bc8a80`), value from a parameter (the caller `charging/ui/page/account/forget_pwd/forget_pwd_logic.dart` loads `getClientPublicKey`, `@0x3bc8880`).

Password processing (app side, traced 2026-10-20): `ForgetPwdLogic::startResetPwd` passes the constant `EncType` `pp+0xc19e0` (`sha256`, `charging/ui/page/account/forget_pwd/forget_pwd_logic.dart @0x3bc88e0`, call `@0x3bc88e8`), so `processPassword` returns the SHA-256 hex text of the UTF-8 password; the branches are described on [login.md](login.md#request).

Types (app side, traced 2026-10-20, `charging/ui/page/account/forget_pwd/forget_pwd_logic.dart`): `ForgetPwdLogic::startResetPwd` reads `phone_number` and `verify_code` from two text controllers (`field_5b` `@0x3bc88ac`..`@0x3bc88bc` and `field_5f` `@0x3bc88f8`..`@0x3bc8908`; the logic creates the fields `field_5b`, `field_5f` and `field_63` as `TextEditingController` objects, `@0x40f90c8`, `@0x40f9104`, `@0x40f9140`) through the chain `field_27` then `field_7`, which on a `TextEditingController` is `value.text` (`flutter/src/widgets/editable_text.dart`, getter `selection` `@0x2573d7c` reads the same `field_27` as the `TextEditingValue`), a `String`; the third value is the result of `processPassword` on `field_63` (see above), the hex text of a SHA-256 digest, a string. So the three scalar keys are strings.

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
  "client_secret_info": {
    "public_key": "<public_key>"
  }
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

- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
