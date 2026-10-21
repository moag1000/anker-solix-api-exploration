> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# validate_email

## Purpose

Checks an e-mail address against the account server (registered or not, password empty or not, encrypted text); sent by the login, forgot-password, verification, change-password and router-info screens (`LoginLogic::checkIsRegister`, `::checkIsPwdEmpty`, `::login`, `ForgetPwdLogic::checkIsRegister`, `UserChangePasswordLogic::changePassword`, others in the call chain of `data/endpoints.json`) (asm-traced for the call chain; the meaning of the answer is read from the model keys, string-only for the key names).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/validate_email` (asm-traced): three senders use the same URL and the method object `Method.post` (pool entry `pp+0xa7e0`):

- `HttpRequestControllerImpl::checkIsRegisterRequest` (`charging/http/http_request_repository_impl.dart @0x3bc84c0`): URL string at `@0x3bc85c0`, method object at `@0x3bc85b8`, sent through `encryptionRequestHttp` (`@0x3bc85e8`).
- `HttpRequestControllerImpl::validateAccountRequest` (`charging/http/http_request_repository_impl.dart @0x2915640`): URL string at `@0x29156f8`, method object at `@0x29156f0`, sent through `encryptionRequestHttp` (`@0x2915720`).
- `checkIsRegisterRequest` (static function in `charging/ui/page/account/login/installer_login_logic.dart @0x31921c0`): URL string at `@0x31922e4`, method object at `@0x31922dc`, sent through `encryptionRequestHttp` (`@0x319230c`) of an `HttpService` obtained with `getService` (`@0x3192268`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `email` | string | yes | `"<email>"` | `charging/http/http_request_repository_impl.dart @0x3bc8560` (value store `@0x3bc8570`) |

All three senders store the one key `email` in a map literal with type arguments `<String, String>` (`charging/http/http_request_repository_impl.dart @0x3bc8574`, `@0x29156ac`; `charging/ui/page/account/login/installer_login_logic.dart @0x3192298`); the source column is the first sender.

## `param_type`/`cmd`

n/a

## Response model (link)

[`ValidateAccountModel`](../../models/account.md#validateaccountmodel), parsed by `ValidateAccountModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x3bc86c8` (closure `@0x3bc867c`) and at `@0x2915844` (closure `@0x29157f8`), call target `#0x29158bc` in `charging/model/validate_account_model.dart`, applied to the response value cast to `Map<String, dynamic>` (`@0x3bc86bc`, `@0x291582c`). The third sender takes `success` and `fail` callbacks from its caller and its parse was not read.

## Response

(asm-traced for the first two senders) Top-level keys of `ValidateAccountModel` (`data/models.json`, `charging::ValidateAccountModel`): `result` (bool), `enc_text` (String?), `status` (String?), `pass_empty` (bool). The first sender completes a `Future<ValidateAccountModel?>` with the model (`complete` `@0x3bc871c`); the second passes it to the stored callback (`ClosureCall` `@0x2915898`).

Values of `enc_text` (app side, traced 2026-10-20, `charging/model/validate_account_model.dart`): `ValidateAccountModel.fromJson` passes the key to `EncType.fromValue` (call `@0x29159b0`), which runs `firstWhere` over the two enum instances (`@0x2915cec`; the list `[raw, sha256]`, pool `pp+0xc1aa8`) with the shared predicate closure `base_service/enum/charging_pn.dart @0x22caf60` (it compares the `value` string of the instance with the argument by `==`, `@0x22caf88`..`@0x22caf9c`) and the fallback closure `@0x2915d04`, which returns the instance `raw` (`pp+0xc19d8`). The value strings of the instances are `"raw"` (`raw`) and `"sha2"` (`sha256`) (`pp+0xc19d8`, `pp+0xc19e0`), so the app understands `enc_text` = `"raw"` or `"sha2"` and treats any other text as `raw`; what `processPassword` does for each is on [login.md](login.md#request). The value format of `status` was not read.

Third sender (traced 2026-10-20): the success closure of `checkIsRegisterRequest` in `charging/ui/page/account/login/installer_login_logic.dart` (`@0x319238c`, argument `Object?`) casts the value to `Map<String, dynamic>` (`@0x31923c0`), parses it with `ValidateAccountModel.fromJson` (`@0x31923d8`) and completes the `Future<ValidateAccountModel?>` (`complete` `@0x31923f8`); its failure closure (`@0x319233c`, `(int, String)`) calls `completeError` (`@0x3192370`). So the third sender parses the same model as the first two and compares no code.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "email": "<email>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `checkIsRegisterRequest` @0x3bc84c0 (encryptionRequestHttp; encrypted: true); `validateAccountRequest` @0x2915640 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/account/login/installer_login_logic.dart`: `checkIsRegisterRequest` @0x31921c0 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::checkIsRegisterRequest`
- `charging/http/http_request_repository.dart::validateAccountRequest`
- `charging/ui/page/account/forget_pwd/forget_pwd_logic.dart::checkIsRegister`
- `charging/ui/page/account/login/login_logic.dart::checkIsPwdEmpty`
- `charging/ui/page/account/login/login_logic.dart::checkIsRegister`
- `charging/ui/page/account/login/login_logic.dart::login`
- `charging/ui/page/account/privacy_policy/verification/verification_logic.dart::passwordVerify`
- `charging/ui/page/user/accountSetting/account_setting_page_logic.dart::checkIsPwdEmpty`
- `charging/ui/page/user/changePassword/user_change_password_logic.dart::changePassword`
- `charging/ui/page/user/routerInfo/account_verification/account_verification_logic.dart::confirmChangePwd`
- `charging/ui/page/user/routerInfo/router_info_logic.dart::checkIsPwdEmpty`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What `status` carries (a `String?` in the model): only the `enc_text` chain was followed on 2026-10-20 (its values are in Response), the readers of `status` were not looked up.
- Error codes: none compared in the callers read (`login_logic.dart`, `forget_pwd_logic.dart`, and others). — traced 2026-10-20: no sender compares a code (the failure closures call `completeError`, see Response); the callers receive the Future, and their `then`/error handling (`LoginLogic::checkIsRegister` `login_logic.dart @0x3bd69bc`, `ForgetPwdLogic::checkIsRegister` `forget_pwd_logic.dart @0x3bc8430`, `InstallerLoginLogic::verifyInstallerAccountPwd` `installer_login_logic.dart @0x3191ea8`) was not decoded for codes
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
