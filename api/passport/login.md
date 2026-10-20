> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# login

## Purpose

Logs a user in with e-mail and password: the app sends the e-mail, the encrypted password and its client public key, and the response carries the session token (`auth_token`) with the user profile.

## Upstream name

`API_LOGIN` (a module constant of `api/apitypes.py`, value `passport/login`; it is not an `API_ENDPOINTS` key). Upstream-confirmed: `session.py`, `AnkerSolixBaseSession.async_authenticate` posts to this URL.

## Method+URL

`POST /passport/login` (asm-traced): URL string `pp+0xdc610` at `charging/http/http_request_repository_impl.dart @0x3bd727c`, method object `Method.post` (pool entry `pp+0xa7e0`, `off_10: "post"`) at `@0x3bd7274`, in `HttpRequestControllerImpl::iotLoginRequest` (`@0x3bd7084`). Upstream posts to `{api_base}/passport/login` (upstream-confirmed).

## Encrypted?

The sender is `encryptionRequestHttp` (`@0x3bd72ac`) with `needEncryption` not passed, so it keeps the default `true` (`@0x226451c`, see [../encryption.md](../encryption.md#which-calls-are-encrypted)). Whether the request really goes through the encrypting SDK depends on a run-time test in `HttpEncryptionDecorator::request` (SDK login state), which asm alone does not decide. Independent of that, the password inside the body is always encrypted by the app before the request is built (see [../auth.md](../auth.md#password-encryption-at-login)). Upstream-confirmed: the library logs in with a plain JSON body, so the server accepts this call without payload encryption.

## Request

Body keys as built by `iotLoginRequest` (map literal of three pairs, the third value is itself a map). `Openudid` is not a body key: it is the only entry of the `header` argument (inventory skeleton listed it as a body field, which was wrong).

| field | type | required | example | source |
|---|---|---|---|---|
| `email` | String | yes | `"user@example.com"` | `http_request_repository_impl.dart @0x3bd716c`; argument of `iotLoginRequest`, passed by `LoginLogic::startLogin` (`login_logic.dart @0x3bd6fdc`) |
| `password` | String | yes | `"<encrypted password>"` | `@0x3bd7180`; `startLogin` first runs `StringExtensions.processPassword` (`login_logic.dart @0x3bd6eec`) and then `Encryption.loginPasswordECDH` (`@0x3bd6ef8`); if the encrypted password or the client public key is empty (`cbz`/`cbnz` on the string lengths, `@0x3bd6f10`, `@0x3bd6f1c`) it shows the generic network error (`commonNetWorkErrorFix`, `@0x3bd6f20`) and calls `Encryption.clearClientKeyPairs` (`@0x3bd6f4c`) without sending |
| `client_secret_info.public_key` | String | yes | `"<client public key>"` | map `client_secret_info` at `@0x3bd7194`, inner key `public_key` at `@0x3bd71ac`; value from `Encryption.getClientPublicKey` (`login_logic.dart @0x3bd6ea4`, empty string if null, `@0x3bd6ebc`) |

Header argument:

| header | carries | source |
|---|---|---|
| `Openudid` | the terminal id (`SpUtilImpl::getTerminalId`, see [terminal_id.md](terminal_id.md)) | key at `@0x3bd721c`, value from `@0x3bd70f8` |

Other call arguments: `showLoading: false` (`r30 = false`, `@0x3bd7294`; the app does show a loading dialog itself, `GetExtension.showLoading` at `@0x3bd7148`).

What upstream sends in addition (upstream-confirmed, `session.py`): the body keys `ab` (country id), `enc` (`0`), `time_zone` and `transaction`. The 3.24.3 `iotLoginRequest` has none of these four keys, and upstream sends no `Openudid` header. The server accepts the upstream form, so the four keys are not rejected; whether the app-style body without them is accepted by the server for every account is not tested here.

What `processPassword` (`validate_account_model.dart @0x2faf368`) does to the password is selected by the `EncType` argument (traced 2026-10-20): the instance `pp+0xc19d8` (`raw`, index 0, value `raw`) makes it return the string unchanged (compare `@0x2faf38c`, return `@0x2faf39c`); the instance `pp+0xc19e0` (`sha256`, index 1, value `sha2`) encodes the string as UTF-8 (`Utf8Encoder.convert` `@0x2faf3bc`), runs it through `_Sha256.convert` (`@0x2faf3cc`) and returns `toString` of the digest (`@0x2faf3d4`), the hex text of the SHA-256 hash; any other value returns the string unchanged. The login screen passes the `EncType` of the account, whose `enc_text` field comes from [validate_email](validate_email.md); the register, forgot-password, set-account-password and change-password screens pass the constant `pp+0xc19e0` (`sha256`): `register_logic.dart @0x3be22e8`, `forget_pwd_logic.dart @0x3bc88e0`, `account_set_password_logic.dart @0x4055474`, `user_change_password_logic.dart @0x4041dd4`, and a second register site in another closure (`charging/ui/page/account/register/register_logic.dart @0x3be2f9c`, also `sha256`). Callers that pass a variable (a `field_b` load, the `EncType` of the validated account) instead of a constant: the first change-password call (`user_change_password_logic.dart @0x4041da0`), `charging/ui/page/user/routerInfo/account_verification/account_verification_logic.dart @0x4055980`, `charging/ui/page/account/privacy_policy/verification/verification_logic.dart @0x2faece8` and `charging/ui/page/account/login/installer_login_logic.dart @0x3191f30`. Upstream sends the raw password with `enc: 0`.

Scope note: pre-processing named only; not described (vendor protection; decision pending with the repo owner).

Login entry (app side, traced 2026-10-20): the Dart `LoginLogic::startLogin` that sends this request is called from `LoginLogic::checkIsFormat` (`charging/ui/page/account/login/login_logic.dart @0x3bd6d6c`) on the Dart login page; the feature code of the app (35 call sites) calls `LoginHandler::startLoginFlow`, which starts the native `ank_user_module` container instead; a start without a login enters through the container (`SplashLogic::_navigatePage`); the evidence is on [../auth.md](../auth.md#login-endpoints).

## `param_type`/`cmd`

n/a

## Response model (link)

`IotUserModel` (asm-traced, `iot_user_model.dart`, parsed by `IotUserModel.fromJson` at `http_request_repository_impl.dart @0x3bd7420`); key list on the legacy page [../../models/account.md](../../models/account.md#iotusermodel). The meaning of the token-related keys is described in [../auth.md](../auth.md#token-lifecycle).

## Response

Wrapper keys read by `Result.fromJson` (`charging/model/result.dart`): `code` (`@0x2fb0548`), `msg` (`@0x2fb0574`), `data` (`@0x2fb05a4`), `signature` (`@0x2fb05d0`). A body `code` of 0 is success (`HttpEncryptionDecorator::_handler200`, `cbnz w0` on the tagged field, `HttpEncryptionDecorator.dart @0x486c708`; zero is zero under the Smi rule). `data` is the user model; its fields are on the model page.

| field | type | required | example | source |
|---|---|---|---|---|
| `code` | int | yes | `0` | `result.dart @0x2fb0548`; `HttpEncryptionDecorator.dart @0x486c708` |
| `msg` | String | yes | `"success!"` | `result.dart @0x2fb0574`; example text from the upstream capture in `session.py` (upstream-confirmed) |
| `data` | object | yes | see [../auth.md](../auth.md#token-lifecycle) | `result.dart @0x2fb05a4` |
| `signature` | String | no | `"<signature>"` | `result.dart @0x2fb05d0`; present on encrypted responses in the upstream capture (upstream-confirmed) |

## Example request/response

Request, synthesized (body as built by `iotLoginRequest`; the header `Openudid` is shown separately)

```json
{
  "email": "user@example.com",
  "password": "<encrypted password>",
  "client_secret_info": { "public_key": "<client public key>" }
}
```

Header, synthesized

```json
{ "Openudid": "<terminal id>" }
```

Response, synthesized (shape only; `<...>` marks values that are not shown here)

```json
{
  "code": 0,
  "msg": "success!",
  "data": { "auth_token": "<token>", "token_expires_at": 0, "user_id": "<user id>" }
}
```

## Errors seen

Catalog: [api/errors.md](../errors.md). Codes the login screen reacts to, from `LoginLogic::handleLoginFail` (`login_logic.dart @0x3bd2210`). All compares are 64-bit on an untagged int (`cmp x0, x17`), so the numbers are real:

| code | where | what the app shows (localization key, meaning taken from the key name) | upstream |
|---|---|---|---|
| 26108 | `@0x3bd22b8` | `errorAccountOrPassWord` | `InvalidCredentialsError` (upstream-confirmed, `errors.py`) |
| 26156 | `@0x3bd2780` | `errorAccountOrPassWord` or `loginEmailOrPwdIncorrect` | `InvalidCredentialsError` (upstream-confirmed) |
| 26105 | `@0x3bd234c` | `loginErrorNoVerified`, `loginErrorCheckEmailActivate`, `loginErrorResendVerification` (account not activated) | none |
| 26109 | `@0x3bd2450`, `@0x3bd2714` | `commonReset`/`commonCancel` dialog and `loginEmailOrPwdIncorrect` | none |
| 100053 | `@0x3bd24d4` | `loginErrorMaxLimit` | `RetryExceeded` (upstream-confirmed) |
| 10019 | `@0x3bd2544` | `loginErrorPwd`, `loginErrorFiveTimes` | none |
| 100056 | `@0x3bd25c0` | `loginErrorPwdReset` (offers a password reset) | none |
| 5000 | `@0x3bd2658` | `errorOccur` | none |
| 1000 | `@0x3bd26bc` (`cmp x0, #0x3e8`) | generic OK dialog | none |
| 26123 | `@0x3bd2324` | handled; branch target not resolved | none |

Transport-level codes (401, 461, 463, 26084, 26085) are handled before the login screen sees them; see [../encryption.md](../encryption.md#response-handling-and-error-codes). Upstream also maps 26070 to `ClientPublicKeyError`, a code the 3.24.3 login screen has no branch for.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `iotLoginRequest` @0x3bd7084 (`encryptionRequestHttp`, call at `@0x3bd72ac`).
- Called from `charging/http/http_request_repository.dart::iotLoginRequest` and `charging/ui/page/account/login/login_logic.dart::startLogin` (`@0x3bd6d88`, call at `@0x3bd6fdc`).
- Success closure `@0x3bd737c`: parses `IotUserModel` (`@0x3bd7420`), logs the SDK out (`AKIoTKitManagerImpl::loginOutTSDK`, `@0x3bd7460`) and logs it in again with the new user (`AKIoTKitManagerImpl::loginIoTSDK`, `@0x3bd7514`, named argument `userId`). Persisting the user model happens in `LoginLogic::handleLoginSuccess` (`@0x3bd2d84`, then `_loginSuccessAction` `@0x3bd3030`, `SpUtilImpl::updateIotUserInfo` `@0x3bd3434`).
- A second, native login screen exists (`ank_user_module`, platform channel method `startLogin`, `ank_user_module_method_channel.dart @0x26fc740`); which of the two is the active entry point in 3.24.3 is not decided here (see Known unknowns).

## Since/changed

3.18.0: present, same four request elements (`email`, `password`, `client_secret_info.public_key`, header `Openudid`; asm 3.18.0 `http_request_repository_impl.dart @0x2d28814` to `@0x2d288c4`). 3.24.3: unchanged. since: ≤3.18.0.

## Known unknowns

- Whether the login state that `SplashLogic` tests can already be true for a visitor session: see [../auth.md](../auth.md#login-endpoints) (traced 2026-10-20).
- Which transport path the login request takes at run time (SDK path or plain Dio path); depends on the SDK state, not decidable from asm.
- What the server returns for `26123` and when it returns `26109`.
- Whether the server requires `ab`, `time_zone`, `transaction` for accounts in non-default regions (upstream sends them, the app does not).

## Device-tested by

none recorded in this repository. Upstream library login with the body described in "What upstream sends in addition": `upstream-confirmed` (thomluther/anker-solix-api, community-run).
