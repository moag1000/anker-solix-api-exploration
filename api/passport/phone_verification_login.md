> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# phone_verification_login

## Purpose

Logs in with a phone number and an SMS code; sent by `LoginLogic::verifyCodeLogin` (`charging/ui/page/account/login/login_logic.dart`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/phone_verification_login` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3bd8534`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3bd852c`, in `HttpRequestControllerImpl::verifyCodeLoginRequest` (`charging/http/http_request_repository_impl.dart @0x3bd833c`), sent through `encryptionRequestHttp` (`@0x3bd8564`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `phone_number` | string | yes |  | `charging/http/http_request_repository_impl.dart @0x3bd8424` (value store `@0x3bd8434`) |
| `verify_code` | string | yes |  | `charging/http/http_request_repository_impl.dart @0x3bd8438` (value store `@0x3bd8448`) |
| `client_secret_info` | object | yes | `{"public_key": "<public_key>"}` | `charging/http/http_request_repository_impl.dart @0x3bd844c` (value store `@0x3bd848c`) |

The body map literal has type arguments `<String, Object>` (`@0x3bd84b0`), which is not evidence of a value type, so the scalar types stay `?`. `client_secret_info` is a nested map literal `<String, String>` (`@0x3bd8478`) with the key `public_key` (`@0x3bd8464`), value from a parameter. A second map literal `<String, String>` (`@0x3bd84e8`) holds the key `Openudid` (`@0x3bd84d4`) with the value of `getTerminalId` (`@0x3bd83b0`); it is passed as the `header` named argument (`@0x3bd855c`), so it is a request header, not a body field.

Caller values (traced 2026-10-20, app side): the login page calls `LoginLogic::verifyCodeLogin` with the text of two logic fields, `field_83` (`charging/ui/page/account/login/login_view.dart @0x3bd6220`..`@0x3bd6230`) and `field_87` (`@0x3bd624c`..`@0x3bd625c`), each read through the chain `field_27` then `field_7`, and the route string `"/userMainPage"` or `"/home"` (`@0x3bd6284`, `@0x3bd6328`; `LoginSuggestPage` calls it too, `login_suggest_view.dart @0x3bdb984`). The logic constructor creates both fields as `TextEditingController` objects (`charging/ui/page/account/login/login_logic.dart @0x40f96d4`..`@0x40f96f0` and `@0x40f9710`..`@0x40f972c`), and on such a controller that chain is `value.text`, a String (`flutter/src/widgets/editable_text.dart @0x2573d7c`, as on [register](register.md)). `verifyCodeLogin` keeps the two values in its context and passes them to `verifyCodeLoginRequest` after `prepareLogin`, `checkInputFormat` and `checkIsRegister` (`login_logic.dart @0x3bd7fbc`, `@0x3bd7fc4`, `@0x3bd8078`, call `@0x3bd82a0`). So `phone_number` and `verify_code` are the strings typed in the login form.

## `param_type`/`cmd`

n/a

## Response model (link)

[`IotUserModel`](../../models/account.md#iotusermodel) (`data/models.json`, `charging::IotUserModel`), parsed by `IotUserModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x3bd86d8` in the success closure `@0x3bd8634` (the call target is `#0x22016cc` in `charging/model/iot_user_model.dart`).

## Response

(asm-traced) Top-level keys of `charging::IotUserModel` (`data/models.json`): `ab_code`, `auth_token`, `avatar`, `country_code`, `domain`, `email`, `fa_info`, `geo_key`, `mac_addr`, `nick_name`, `params`, `phone`, `phone_number`, `phone_code`, `privilege`, `server_secret_info`, `public_key`, `token_expires_at`, `token_id`, `trust_list`, `user_id`, `freeze_status`. After the parse the closure logs the SDK out (`loginOutTSDK` `@0x3bd8718`) and logs in again (`loginIoTSDK` `@0x3bd87cc`); the credential roles of the response fields are described in `auth.md`, not repeated here.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "phone_number": "<phone_number>",
  "verify_code": "<verify_code>",
  "client_secret_info": {}
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced in the caller `LoginLogic::verifyCodeLogin`: no numeric error code is compared in it or in the sender's closures read for this page. Code meanings are owned by `api/errors.md`.

Failure path (traced 2026-10-20, app side): the failure closure of `LoginLogic::verifyCodeLogin` (`charging/ui/page/account/login/login_logic.dart @0x3bd8a10`, signature `(int, String)`) calls `loginReport` (`@0x3bd8a50`) and `handleLoginFail` (`@0x3bd8a74`); the codes that `handleLoginFail` (`@0x3bd2210`) compares are listed with their meanings in [errors.md](../errors.md), which owns them.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `verifyCodeLoginRequest` @0x3bd833c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::verifyCodeLoginRequest`
- `charging/ui/page/account/login/login_logic.dart::verifyCodeLogin`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
