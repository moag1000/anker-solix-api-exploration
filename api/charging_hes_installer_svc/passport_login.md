> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# passport_login

## Purpose

Verifies the e-mail and password of an installer account in the identity-authentication dialog: the app sends the e-mail, the encrypted password and its client public key and only learns whether the check succeeded (no token is stored from the answer).

## Upstream name

`none` (no upstream name). The consumer login is `API_LOGIN` (`passport/login`, [../passport/login.md](../passport/login.md)); this installer twin has no upstream constant.

## Method+URL

`POST /charging_hes_installer_svc/passport_login` (asm-traced): the URL is a literal at `charging/ui/page/account/login/installer_login_logic.dart @0x3192110` in `verifyInstallerAccountPwd` (`@0x3191e48`, a top-level function, `async`), method object `Method.post` (pool entry `pp+0xa7e0`, `@0x3192108`). Unlike most pages of this service there is no `isProApp` selector, so the flag-based dormancy of the other URLs does not apply: the call is sent by the identity dialog, which consumer settings pages open without an `isProApp` test (see Callers); whether it is reached in `com.anker.charging` is not determined.

## Encrypted?

Yes by wrapper (asm-traced): `HttpService.encryptionRequestHttp` (`charging/ui/page/account/login/installer_login_logic.dart @0x3192138`) with a `header` argument and without `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../encryption.md#which-calls-are-encrypted)). The password inside the body is encrypted by the app independently of that flag, as for the consumer login ([../auth.md](../auth.md#password-encryption-at-login)). Whether the call goes through the SDK is decided at run time.

## Request

Before this call the function runs `checkIsRegisterRequest(email)` (`@0x3191ea8`), a `POST /passport/validate_email` with body `{"email": <email>}` (`@0x31922e4`, `showLoading: true`), see [../passport/validate_email.md](../passport/validate_email.md); its answer supplies the account's `EncType`, which `StringExtensions.processPassword` (`@0x3191f30`) uses. The login body then is a map literal of four pairs, `<String, Object>` (`r2 = 16`, `@0x3191f54`; the third value is itself a map):

| field | type | required | example | source |
|---|---|---|---|---|
| `email` | String | yes | `"installer@example.com"` | `charging/ui/page/account/login/installer_login_logic.dart @0x3191f64`; value is the first argument of `verifyInstallerAccountPwd`, passed by `installerLogin`, which reads the two input texts from the dialog state (`identity_auth_view.dart @0x3191db8` to `@0x3191dec`); that the first is the e-mail and the second the password follows from the argument order |
| `password` | String | yes | `"<encrypted password>"` | `@0x3191f78`; result of `Encryption.loginPasswordECDH` (`@0x3191f40`) applied to `processPassword(...)`; the scheme is not described here (vendor protection, see [../encryption.md](../encryption.md#scope-note)) |
| `client_secret_info.public_key` | String | yes | `"<client public key>"` | map `client_secret_info` at `@0x3191f8c`, inner key `public_key` at `@0x3191fa4`; value from `Encryption.getClientPublicKey` (`@0x3191ec4`), empty string if null (`@0x3191edc`) |
| `support_anker_login` | int | yes | `1` | `@0x3191ff4`; raw `2` (`@0x3192000`) stored with `stur w16` (`@0x3192004`), Smi, so 1 (`tools/smi.py`: `2 → stur w → 1`) |

Headers (named argument `header`, `<String, String>` literal, `r2 = 8`, `@0x3192048`):

| header | carries | source |
|---|---|---|
| `Openudid` | the terminal id (`SpUtilImpl::getTerminalId`, see [../passport/terminal_id.md](../passport/terminal_id.md)) | key `@0x3192058`, value from `@0x319207c` |
| `App-Name` | the constant `anker_pros` | key `@0x31920ac`, value `@0x31920b8` |

The consumer login body has no `support_anker_login` and sends no `App-Name` header (compare [../passport/login.md](../passport/login.md#request)).

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model is parsed.

## Response

No response field is read (asm-traced). The success closure (`@0x3192444`, defined in `custom_charge_cloud_api.dart` and shared by identical code) takes a `Map<String, dynamic>`, ignores it and calls the caller's callback with `true` (`@0x3192470`). The failure closure (`HttpRequestControllerImpl::getInstallation` closure `@0x2375ad8`, shared) forwards the code and message to the callback (`ClosureCall` `@0x2375b14`). In particular, no token or profile from the answer is stored here; the wrapper envelope is as in [../encryption.md](../encryption.md#response-handling-and-error-codes).

## Example request/response

Request, synthesized

```json
{ "email": "installer@example.com", "password": "<encrypted password>", "client_secret_info": { "public_key": "<client public key>" }, "support_anker_login": 1 }
```

Headers: `Openudid: <terminal id>`, `App-Name: anker_pros`. Response: no captured response; no field is read.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or shows a toast; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../errors.md). The login-screen codes of [../passport/login.md](../passport/login.md#errors-seen) are not confirmed for this endpoint.

## Callers in app

- `verifyInstallerAccountPwd` (`charging/ui/page/account/login/installer_login_logic.dart @0x3191e48`), called by `_IdentityAuthViewState.installerLogin` (`device/src/widgets/identity_auth_view.dart @0x3191d1c`, call `@0x3191e24`) and by the identical copy in `settings/src/common/component/identity_auth_view.dart` (`installerLogin @0x3192e6c`, call `@0x3192f74`). UI: the identity-authentication dialog (`IdentityAuthView`), which has an e-mail and a password field and shows a loading overlay (`showLoading`, `@0x3191d8c`) while the call runs. On success the dialog closes and returns the integer 1 (`GetNavigation.back<int>(result: 1)`, raw `2` at `settings/src/common/component/identity_auth_view.dart @0x3192e3c`, a tagged argument).
- `IdentityAuthView` is opened, without an `isProApp` test, from the consumer settings pages `settings/src/common/menu_controller/grid_param_menu_controller.dart @0x2cd5db8` and `charging/ui/page/device/main/sitation_energy_system/station_home_settings/advanced_setting/advanced_setting_logic.dart @0x3fabd84` (both load an `Instance_IdentityAuthView`; no `isProApp` test near them).

## Since/changed

3.18.0: absent (the 3.18.0 pool has neither an `installer_svc` string nor `anker_pros`; the consumer login `/passport/login` is a different endpoint). 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- Server behaviour is not known: whether the answer sets a session, and what the installer server does with `support_anker_login`.
- Whether the dialog really sends this installer URL in the consumer build (the sender has no flag test) and what the server answers to a consumer account is not known.
- The numeric error codes of this endpoint are not known.

## Device-tested by

none
