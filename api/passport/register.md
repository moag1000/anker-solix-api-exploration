> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# register

## Purpose

Registers an account with an e-mail address and a password; sent by `RegisterLogic::register` (`charging/ui/page/account/register/register_logic.dart`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/register` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3be24d4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3be24cc`, in `HttpRequestControllerImpl::registerRequest` (`charging/http/http_request_repository_impl.dart @0x3be23dc`), sent through `encryptionRequestHttp` (`@0x3be24fc`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `email` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3be2438` (value store `@0x3be2448`) |
| `password` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3be244c` (value store `@0x3be245c`) |
| `is_subscribe` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3be2460` (value store `@0x3be2470`) |
| `country_code` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3be2474` (value store `@0x3be2484`) |

The body map literal has type arguments `<String, Object>` (`@0x3be2488`), which is not evidence of a value type, so the scalar types stay `?`.

## `param_type`/`cmd`

n/a

## Response model (link)

[`UserModel`](../../models/account.md#usermodel), parsed by `UserModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x3be2550` in the success closure `@0x3be2518` (call target `#0x34e6fd8`, `charging/model/user_model.dart`).

## Response

(asm-traced) Top-level keys of `UserModel` (`data/models.json`, `charging::UserModel`): `email` (String?), `phone_number` (String?), `nick_name` (String?), `phone` (String?), `avatar` (String?), `country` (String?), `promo_email` (bool?), `access_token` (String?), `id` (int?). The closure passes the model to the stored callback (`ClosureCall` `@0x3be256c`).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "email": "<email>",
  "password": "<password>",
  "is_subscribe": "<is_subscribe>",
  "country_code": "<country_code>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

Codes compared in the failure closures of `register` (`register_logic.dart`): 1000 (`@0x3be2a14`), 2001 (`@0x3be2838`), 4007 (`@0x3be28e4`), 5000 (`@0x3be29b0`), 10005 (`@0x3be2a6c`), 26114 (`@0x3be2788`), 100053 (`@0x3be293c`), as listed in `data/errors.json`. Meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `registerRequest` @0x3be23dc (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::registerRequest`
- `charging/ui/page/account/register/register_logic.dart::register`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `email`, `password`, `is_subscribe`, `country_code`: parameters of the sender stored into a `<String, Object>` literal; the caller's values were not typed.
- Whether the password is sent in clear or processed first (the forgot-password caller applies `StringExtensions.processPassword`; the `register` caller was not checked for it).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
