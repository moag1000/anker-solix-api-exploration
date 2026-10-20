> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# update_profile

## Purpose

Changes the nick name or the phone number in the account settings (`AccountSettingPageLogic::changeNickname`, `::changePhoneNumber`); `LanguageLogic::updateLanguage` also calls the sender (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/update_profile` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x403b5b4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x403b5ac`, in `HttpRequestControllerImpl::updateUserProfileRequest` (`charging/http/http_request_repository_impl.dart @0x403b524`), sent through `encryptionRequestHttp` (`@0x403b5dc`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The sender builds no body: it forwards the map it receives (`HttpRequestControllerImpl::updateUserProfileRequest`, `charging/http/http_request_repository_impl.dart @0x403b524`). The body is built in the callers, one key per call:

| field | type | required | example | source |
|---|---|---|---|---|
| `phone_number` | string | yes (in the `changePhoneNumber` call) | `"<phone_number>"` | `charging/ui/page/user/accountSetting/account_setting_page_logic.dart @0x403b428` (value store `@0x403b458`, map literal `<String, String>` `@0x403b45c`, value from a text field) |
| `nick_name` | string | yes (in the `changeNickname` call) | `"<nick_name>"` | `charging/ui/page/user/accountSetting/account_setting_page_logic.dart @0x403c930` (value store `@0x403c96c`, map literal `<String, String>` `@0x403c990`, value passed through `trim` `@0x403c964`) |

`LanguageLogic::updateLanguage` calls the sender with the empty string instead of a map (`charging/ui/page/user/language/language_logic.dart @0x404ff3c`); the language is not a body key in the code read.

## `param_type`/`cmd`

n/a

## Response model (link)

[`UserModel`](../../models/account.md#usermodel), parsed by `UserModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x403b664` in the success closure `@0x403b5f8` (call target `#0x34e6fd8`, `charging/model/user_model.dart`).

## Response

(asm-traced) Top-level keys of `UserModel` (`data/models.json`, `charging::UserModel`): `email` (String?), `phone_number` (String?), `nick_name` (String?), `phone` (String?), `avatar` (String?), `country` (String?), `promo_email` (bool?), `access_token` (String?), `id` (int?). The closure logs `login result: ` and passes the model to the stored callback (`ClosureCall` `@0x403b680`).

## Example request/response

Request, synthesized (decrypted body as built by `changeNickname`; `<...>` is a placeholder, not a captured value)

```json
{
  "nick_name": "<nick_name>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `updateUserProfileRequest` @0x403b524 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::updateUserProfileRequest`
- `charging/ui/page/user/accountSetting/account_setting_page_logic.dart::changeNickname`
- `charging/ui/page/user/accountSetting/account_setting_page_logic.dart::changePhoneNumber`
- `charging/ui/page/user/language/language_logic.dart::updateLanguage`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- How the language change is sent: `updateLanguage` passes `""` as the body argument (`@0x404ff3c`); the language is probably carried in a request header, not read here.
- Whether other callers send further profile keys (for example `avatar` or `country`): only the two callers above build a map.
- Value rules for `nick_name` (the dialog passes `maxLength` 40, `account_setting_page_logic.dart @0x403c834`) and the phone number: server side checks are not visible.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
