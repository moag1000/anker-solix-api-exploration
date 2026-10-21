> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# phone_verification_regist

## Purpose

Registers an account with a phone number, an SMS code and a password; sent by `RegisterLogic::startRegister` (`charging/ui/page/account/register/register_logic.dart`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/phone_verification_regist` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3be3240`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3be3238`, in `HttpRequestControllerImpl::verifyCodeRegisterRequest` (`charging/http/http_request_repository_impl.dart @0x3be30a0`), sent through `encryptionRequestHttp` (`@0x3be3268`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `phone_number` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3be3104` (value store `@0x3be3114`) |
| `verify_code` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3be3118` (value store `@0x3be3128`) |
| `password` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3be312c` (value store `@0x3be313c`) |
| `client_secret_info` | object | yes | `{"public_key": "<public_key>"}` | `charging/http/http_request_repository_impl.dart @0x3be3140` (value store `@0x3be3180`) |
| `is_subscribe` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3be31a8` (value store `@0x3be31b8`) |
| `country_code` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3be31bc` (value store `@0x3be31d0`) |

The body map literal has type arguments `<String, Object>` (`@0x3be31f4`), which is not evidence of a value type, so the scalar types stay `?`. `client_secret_info` is a nested map literal `<String, String>` (`@0x3be316c`) with the key `public_key` (`@0x3be3158`), value from a parameter. The `tbz`/`b.eq` pairs after the array stores (`@0x3be3188`, `@0x3be31d8`) are write-barrier checks, not value guards.

## `param_type`/`cmd`

n/a

## Response model (link)

[`UserModel`](../../models/account.md#usermodel), parsed by `UserModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x3be336c` in the success closure `@0x3be3334` (call target `#0x34e6fd8`, `charging/model/user_model.dart`).

## Response

(asm-traced) Top-level keys of `UserModel` (`data/models.json`, `charging::UserModel`): `email` (String?), `phone_number` (String?), `nick_name` (String?), `phone` (String?), `avatar` (String?), `country` (String?), `promo_email` (bool?), `access_token` (String?), `id` (int?). The closure logs `register success ` and passes the model to the stored callback (`ClosureCall` `@0x3be33bc`).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "phone_number": "<phone_number>",
  "verify_code": "<verify_code>",
  "password": "<password>",
  "client_secret_info": {},
  "is_subscribe": "<is_subscribe>",
  "country_code": "<country_code>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

Codes compared in the failure closures of `startRegister` (`register_logic.dart`): 1000 (`@0x3be361c`), 4007 (`@0x3be34ec`), 5000 (`@0x3be35b8`), 26114 (`@0x3be343c`), 26123 (`@0x3be3414`), 100053 (`@0x3be3544`), as listed in `data/errors.json`. Meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `verifyCodeRegisterRequest` @0x3be30a0 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::verifyCodeRegisterRequest`
- `charging/ui/page/account/register/register_logic.dart::startRegister`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `phone_number`, `verify_code`, `password`, `is_subscribe`, `country_code`: parameters of the sender stored into a `<String, Object>` literal; the caller's values were not typed. — attempted 2026-10-20 (two-hop not readable: `startRegister` (`charging/ui/page/account/register/register_logic.dart @0x3be3020`) pass slots or fields of their own frames; no literal or declared type in the argument setups)
- What `is_subscribe` means on the server (e-mail or SMS marketing opt-in): inferred from the name only.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
