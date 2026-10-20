> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# phone_verification_code

## Purpose

Requests an SMS verification code for a phone number; sent by the login, register, forgot-password and bind-phone screens (`LoginLogic`, `RegisterLogic`, `ForgetPwdLogic`, `BindPhoneNumberLogic`, each `sendVerifyCode`), which pass the literal `kind` values `"login"` (`charging/ui/page/account/login/login_logic.dart @0x3bd9e90`), `"regist"` (`charging/ui/page/account/register/register_logic.dart @0x3be5674`), `"forget_pass"` (`charging/ui/page/account/forget_pwd/forget_pwd_logic.dart @0x3bcbb7c`) and `"third_binding_phone"` (`charging/ui/page/account/bind_phone_number/bind_phone_number_logic.dart @0x3bc56d8`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/phone_verification_code` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3bc5818`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3bc5810`, in `HttpRequestControllerImpl::sendVerifyCodeRequest` (`charging/http/http_request_repository_impl.dart @0x3bc5750`), sent through `encryptionRequestHttp` (`@0x3bc5840`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `phone_number` | string | yes | `"<phone_number>"` | `charging/http/http_request_repository_impl.dart @0x3bc57a8` (value store `@0x3bc57b8`) |
| `kind` | string | yes | `"login"`, `"regist"`, `"forget_pass"` or `"third_binding_phone"` (constants in the four callers; the sender stores a parameter) | `charging/http/http_request_repository_impl.dart @0x3bc57bc` (value store `@0x3bc57c8`) |

Both values are Strings: map literal with type arguments `<String, String>` (`@0x3bc57cc`).

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced for the sender and the login caller): the success closure (`charging/http/http_request_repository_impl.dart @0x3bc585c`) logs `sendVerifyCode success: ` with the response value and passes it unchanged to the stored callback (`ClosureCall` `@0x3bc58d0`); no `fromJson`. The login screen's callback (`login_logic.dart @0x3bda100`) ignores the value and starts the countdown (`_startCountdown` `@0x3bda12c`); the callbacks of the other three screens were not read.

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "phone_number": "<phone_number>",
  "kind": "<kind>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

Codes compared in the login screen's failure closure (`login_logic.dart @0x3bd9eb8`): 26008 (`@0x3bd9efc` x, `@0x3bd9f08` w), 26124 (`@0x3bd9ef0`, `@0x3bd9f40`), 26125 (`@0x3bd9fcc`), 100053 (`@0x3bda02c` x, `@0x3bda03c` w), as listed in `data/errors.json`; the closures of the other three screens were not read. Meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `sendVerifyCodeRequest` @0x3bc5750 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::sendVerifyCodeRequest`
- `charging/ui/page/account/bind_phone_number/bind_phone_number_logic.dart::sendVerifyCode`
- `charging/ui/page/account/forget_pwd/forget_pwd_logic.dart::sendVerifyCode`
- `charging/ui/page/account/login/login_logic.dart::sendVerifyCode`
- `charging/ui/page/account/register/register_logic.dart::sendVerifyCode`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Whether the callbacks of the register, forgot-password and bind-phone screens also ignore the response (only the login callback was read).
- The server's rate limit and code lifetime: not visible in the app; `api/errors.md` lists the retry-limit code 100053.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
