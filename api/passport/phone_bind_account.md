> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# phone_bind_account

## Purpose

Binds a phone number to the account after a login with Apple or WeChat; sent by `BindPhoneNumberLogic::bindPhoneNumberWithApple` and `::bindPhoneNumberWithWechat` with the literal `third_party` values `"apple"` (`charging/ui/page/account/bind_phone_number/bind_phone_number_logic.dart @0x3bc2ef4`) and `"wechat"` (`@0x3bc4620`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/phone_bind_account` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3bc313c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3bc3134`, in `HttpRequestControllerImpl::bindPhoneNumberRequest` (`charging/http/http_request_repository_impl.dart @0x3bc2f9c`), sent through `encryptionRequestHttp` (`@0x3bc3164`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `phone_number` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3bc3000` (value store `@0x3bc3010`) |
| `verify_code` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3bc3014` (value store `@0x3bc3024`) |
| `access_token` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3bc3028` (value store `@0x3bc3038`) |
| `third_party` | ? | yes | `"apple"` or `"wechat"` (constants in the two callers) | `charging/http/http_request_repository_impl.dart @0x3bc303c` (value store `@0x3bc304c`) |
| `client_secret_info` | object | yes | `{"public_key": "<public_key>"}` | `charging/http/http_request_repository_impl.dart @0x3bc3050` (value store `@0x3bc3090`) |
| `open_id` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3bc30b8` (value store `@0x3bc30cc`) |

The map literal has type arguments `<String, Object?>` (`@0x3bc30f0`), which is not evidence of a value type, so the scalar types stay `?`. `client_secret_info` is a nested map literal `<String, String?>` (`@0x3bc307c`) with the key `public_key` (`@0x3bc3068`); its value is a parameter, not a constant. `open_id` is stored like the others (`@0x3bc30cc`); the `tbz`/`b.eq` pairs after the array stores (`@0x3bc3098`, `@0x3bc30d4`) are write-barrier checks, not value guards.

## `param_type`/`cmd`

n/a

## Response model (link)

[`IotUserModel`](../../models/account.md#iotusermodel) (`data/models.json`, `charging::IotUserModel`), parsed by `IotUserModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x3bc32c0` in the success closure `@0x3bc31fc` (the call target is `#0x22016cc` in `charging/model/iot_user_model.dart`). The Apple caller closure parses the same class again (`charging/ui/page/account/bind_phone_number/bind_phone_number_logic.dart @0x3bc3830`).

## Response

(asm-traced) Top-level keys of `charging::IotUserModel` (`data/models.json`): `ab_code`, `auth_token`, `avatar`, `country_code`, `domain`, `email`, `fa_info`, `geo_key`, `mac_addr`, `nick_name`, `params`, `phone`, `phone_number`, `phone_code`, `privilege`, `server_secret_info`, `public_key`, `token_expires_at`, `token_id`, `trust_list`, `user_id`, `freeze_status`. When the parsed model carries a non-empty token field and a non-empty value in the second checked field (`@0x3bc32d4`..`@0x3bc32f4`), the sender logs the SDK out (`loginOutTSDK` `@0x3bc3310`) and logs in again (`loginIoTSDK` `@0x3bc33bc`).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "phone_number": "<phone_number>",
  "verify_code": "<verify_code>",
  "access_token": "<access_token>",
  "third_party": "<third_party>",
  "client_secret_info": {},
  "open_id": "<open_id>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

Codes compared in the callers' failure closures (`bindPhoneNumberWithApple`, `bindPhoneNumberWithWechat`): 1000, 5000, 26123, 100053 (Apple: `@0x3bc372c`, `@0x3bc36c8`, `@0x3bc362c`, `@0x3bc3654`; WeChat: `@0x3bc4794`, `@0x3bc4730`, `@0x3bc4694`, `@0x3bc46bc`), as listed in `data/errors.json`. Meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `bindPhoneNumberRequest` @0x3bc2f9c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::bindPhoneNumberRequest`
- `charging/ui/page/account/bind_phone_number/bind_phone_number_logic.dart::bindPhoneNumberWithApple`
- `charging/ui/page/account/bind_phone_number/bind_phone_number_logic.dart::bindPhoneNumberWithWechat`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `phone_number`, `verify_code`, `access_token`, `open_id`: parameters of the sender stored into a `<String, Object?>` literal; the callers pass fields read from state (`@0x3bc2e7c`..`@0x3bc2ec0`) whose types were not read.
- What the callers pass for `open_id` (the field is stored without a null guard, but its content for an Apple login was not decoded).
- What the two secret-bearing fields of the response (`auth_token`, `server_secret_info`) are used for after the re-login: the roles are described in `api/auth.md`; they are not repeated here.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
