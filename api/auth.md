> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# Authentication

This page owns how an app session starts, what identifies it on every request, and how it ends: the login endpoints, the common request headers, the token lifecycle and the name of the password mechanism. Request bodies live on the endpoint pages linked below; the encrypted request path (key exchange, encryption headers, error codes of the transport) lives on [encryption.md](encryption.md). Tags and the Smi rule are defined in [../METHODOLOGY.md](../METHODOLOGY.md).

Scope note: request signing, session key and payload encryption are documented on [encryption.md](encryption.md). This page does not extend the account login and its password encryption (see [Password encryption at login](#password-encryption-at-login)).

## Purpose

Describes, for someone who writes a client against the same cloud: which URLs start a session (and which of them carry the encrypted password), which headers the app sends on ordinary requests and where each comes from, where the session token comes from and how it is stored, passed on to the IoT SDK, expired and cleared, and how the app's password step relates to what the upstream library already does.

## Login endpoints

All four senders use `Method.post` (pool entry `pp+0xa7e0`, `off_10: "post"`). Request body keys are deliberately omitted from this table: they live on the owner pages linked in the second column (single source), so check there for them. "Wrapper default" means the sender calls an `encryptionRequestHttp` wrapper without `needEncryption`, so the default `true` applies and the real transport is decided at run time as described in [encryption.md](encryption.md#which-calls-are-encrypted). Tag for every row: asm-traced.

| endpoint | owner page | sender (function, `file.dart @0xADDR`) | transport flag | upstream key |
|---|---|---|---|---|
| `/passport/login` | [passport/login.md](passport/login.md) | `HttpRequestControllerImpl::iotLoginRequest`, `http_request_repository_impl.dart @0x3bd7084` (URL `@0x3bd727c`) | wrapper default | `API_LOGIN` (constant) |
| `/passport/third_party_login` | [passport/third_party_login.md](passport/third_party_login.md) | `thirdLoginRequest`, `http_request_repository_impl.dart @0x3bd1858` (URL `@0x3bd1a9c`) | wrapper default | none |
| `/passport/phone_verification_login` | [passport/phone_verification_login.md](passport/phone_verification_login.md) (skeleton) | `verifyCodeLoginRequest`, `http_request_repository_impl.dart @0x3bd833c` (URL `@0x3bd8534`) | wrapper default | none (listed as a known URL upstream) |
| `/charging_hes_installer_svc/passport_login` | [charging_hes_installer_svc/passport_login.md](charging_hes_installer_svc/passport_login.md) (skeleton) | `verifyInstallerAccountPwd`, `installer_login_logic.dart @0x3191e48` (URL `@0x3192110`) | `HttpServiceImpl::encryptionRequestHttp` | none |

Related endpoints, not login themselves: [passport/validate_email.md](passport/validate_email.md) (account check; its `enc_text` selects the password pre-processing, see [login.md](passport/login.md#request)), [passport/terminal_id.md](passport/terminal_id.md) (anonymous client id, requested before any login), [passport/logout.md](passport/logout.md) (sent with `needEncryption: false`), [openapi/oauth/key/exchange.md](openapi/oauth/key/exchange.md) (session key negotiation), [passport/estimate_domain.md](passport/estimate_domain.md) (region host lookup, sent with `needEncryption: false`, `needTerminal: false` and `useBaseUrl: false`, `http_request_repository_impl.dart @0x2740974`).

The app also contains a native login container (`ank_user_module`, platform channel method `startLogin`, `ank_user_module_method_channel.dart @0x26fc740`) whose result is a `UserData` object with `token`, `tokenExpiresAt`, `userId`, `geoKey`, `abCode`, `apCloudUserId` (key strings at `ank_user_module/models/user_data.dart @0x26fbc64` to `@0x26fc258`). It is not an HTTP interface and is not described further; see Known unknowns.

## Common request headers

Built for the plain Dio path by `HttpRequestImpl::_headerToken` (`charging/http/http_request_impl.dart @0x486d610`). Header names are case-insensitive on the wire; the spelling below is the one in the app. On the SDK path the Dart side only hands over the caller's own `header` map, and the SDK adds its headers natively (not visible in asm); the headers the upstream capture shows on encrypted calls are listed in [encryption.md](encryption.md#request-headers-on-encrypted-calls). Tag for the Dart-built rows: asm-traced; the last column also gives the upstream view where one exists.

| header | what it carries | where it comes from | when | upstream |
|---|---|---|---|---|
| `Model-Type` | the constant `PHONE` | strings at `@0x486d6fc`, `@0x486d708` | always | `model-type` is `DESKTOP` in the library (`API_HEADERS`, upstream-confirmed) |
| `Timezone` | local time zone as a GMT offset text | `DeviceUtil::getCurrentTimeIdGMT`, `@0x486d640` | always | `timezone`, format `GMT+01:00` (upstream-confirmed, `session.py`) |
| `Os-Type` | the constant `android` | `@0x486d728`, `@0x486d734` | always | `os-type: android` (upstream-confirmed) |
| `Os-Version` | OS version | `DeviceUtil::systemVersion`, `@0x486d6c0` | empty string unless `SpUtilImpl::isLogin` (`@0x486d6b8`) | not sent |
| `Phone-Model` | device model | `DeviceUtil::phoneModel`, `@0x486d694` | empty string unless logged in (`@0x486d68c`) | not sent |
| `App-Version` | app version string (run-time value of the package info, `3.24.3` for this build; not a literal) | `DeviceUtil::appVersion`, `@0x486d654` | always | commented out in the library (`API_HEADERS`) |
| `Country` | region/country code, default `US` | `DeviceUtil::getCurrentRegion`, `@0x486d78c`, default at `@0x486d7a0` | always | `country` (upstream-confirmed) |
| `Language` | UI language, mapped through a constant map of 78 entries (`_ConstMap len:78`) | `LocaleOptions::getDefault`, `@0x486d7e8`, map lookup `@0x486d800` | always | the capture in `session.py` shows `language: en` |
| `App-Name` | the constant `anker_power` | `@0x486d83c`, `@0x486d848` | always | `app-name: anker_power` (upstream-confirmed) |
| `X-Auth-Token` | the session token | `StringUtil::httpHeaderToken`, `@0x486d864` (`string_util.dart @0x2935fb4`): the `auth_token` field of the stored user model, or a visitor token (`defaultAutoToken`, `@0x2936024`) when no user model is stored | always | `x-auth-token` = login `auth_token` (upstream-confirmed) |
| `X-App-Key` | the empty string | `@0x486d894`, `@0x486d8a0` | always | `x-app-key: ` empty (upstream capture) |
| `gtoken` | an identifier derived from the user id of the stored user model | key `@0x486d92c`; input read from the user model field that holds `user_id` (`@0x486d8e8`) | when a user model with that field exists | `gtoken`, derived from `user_id` of the login response (upstream-confirmed, `session.py`, `_gtoken`) |
| `X-Terminal-ID` | the stored terminal id | `SpUtilImpl::getTerminalId`, `@0x486d960`; key `@0x486d974` | only when there is no `gtoken` | not sent |
| `X-Auth-TS` | the current time in seconds | `StringUtil::currentTimeSecond`, `@0x486d668`; key `@0x486d988` | only when there is no `gtoken` | `x-auth-ts` appears in the key-exchange request of the library |
| `X-Biz-Func` | the constant `demosite` | `@0x486d9dc`, `@0x486d9e4`; also added by `HttpEncryptionDecorator::request` (`@0x486942c`) | only in demo-site mode | not sent |
| `Content-Type` | `application/json` | Dio `BaseOptions`, `http_request_impl.dart @0x4868a5c` | always on this path | `content-type: application/json` |
| `Openudid` | the terminal id | passed per call as the `header` argument by 7 senders (key sites): `aiotPlatformRequestHttp` (`@0x260de6c`), `uploadDeviceToken` (`@0x27418d8`), `getAlexaLinkCodeRequest` (`@0x3bce938`, `@0x3bcea54`), `thirdLoginRequest` (`@0x3bd1a3c`), `iotLoginRequest` (`@0x3bd721c`), `verifyCodeLoginRequest` (`@0x3bd84d4`), all in `http_request_repository_impl.dart`; the installer login `verifyInstallerAccountPwd` also has the string (`installer_login_logic.dart @0x3192058`), whether as header or body key not decoded | only on those calls, not on ordinary requests | not sent |

Scope note: intentionally not documented here (vendor protection; decision pending with the repo owner): how the visitor token behind `X-Auth-Token` is formed when nobody is logged in.

Names that are not headers: the pool strings `app_version`, `country_code` and `timezone` exist, but they are keys of other maps (log upload, location, webview parameters), not of this header map; `appName`, `modelType`, `appVersion` are keys of the Anka agent parameter list (`ai_chat_controller.dart @0x35ca6ec`) and the SDK configuration, not HTTP headers. The 3.24.3 header names are therefore the hyphenated ones in the table.

## Token lifecycle

Tag: asm-traced unless a row says otherwise.

1. **Origin.** The session token is the `auth_token` of the login response. `IotUserModel` (`charging/model/iot_user_model.dart`) carries, among others, `auth_token` (`@0x220251c`), `token_expires_at` (`@0x220286c`), `token_id` (`@0x220289c`), `user_id` (`@0x220294c`), `geo_key` (`@0x2202654`), `domain` (`@0x22025ac`), `ab_code` (`@0x22024ec`), `country_code` (`@0x220257c`) and `server_secret_info` with a nested `public_key` (`@0x220283c`, `@0x2201fa4`); key list on the legacy page [../models/account.md](../models/account.md#iotusermodel). Upstream (`session.py`) reads `auth_token`, `token_expires_at`, `user_id`, `nick_name` from the same response and also `geo_key` and `ap_cloud_user_id` (upstream-confirmed).
2. **Storage in the app.** After a successful login, `LoginLogic::handleLoginSuccess` (`login_logic.dart @0x3bd2d84`) calls `_loginSuccessAction` (`@0x3bd3030`), which stores the model with `SpUtilImpl::updateIotUserInfo` (`@0x3bd3434`) and sets the last login time (`@0x3bd34b8`). `SpUtilImpl::getUserModel` is the reader used by the header builder above.
3. **Hand-over to the IoT SDK.** The success closure of `iotLoginRequest` parses the model (`http_request_repository_impl.dart @0x3bd7420`), logs the SDK out (`AKIoTKitManagerImpl::loginOutTSDK`, `@0x3bd7460`) and logs it in as the user (`AKIoTKitManagerImpl::loginIoTSDK`, `@0x3bd7514`). That runs `LoginManager::loginIoTSDK` (`base_service/ak_iot_kit/login_manager.dart @0x273d204`, which queues concurrent logins: log `Login in progress, waiting for completion`, `@0x273d288`) and `_loginIoTSDK` (`@0x273d6b4`), ending in `AkIotKitFlutter::loginAnkerCloud` (`ak_iot_kit_flutter.dart @0x273dcac`, call at `login_manager.dart @0x273dae4`). `loginAnkerCloud` invokes the platform channel method `loginAnkerCloud` (`@0x273de90`, `@0x273dea4`) on the channel `ak_iot_kit_flutter` with a map whose keys are `authToken`, `presetKey`, `appDomain`, `deviceDomain`, `countyCode` (sic), `language`, `appVersion`, `featureConfig`, `isGuestLogin`, `userId`, `terminalId` (`@0x273dd4c` to `@0x273de70`). The value behind `presetKey` is the app-embedded preset key, described by role and pool offset on [encryption.md](encryption.md#session-key-and-key-identifier); a library reads it from its own copy of the APK.
4. **Visitor session before any account.** Without an account, `HttpEncryptionDecorator::request` first obtains a terminal id ([terminal_id.md](passport/terminal_id.md)) and logs the SDK in with the visitor secret (`loginIoTSDK`, `HttpEncryptionDecorator.dart @0x4867e44`, `@0x4868514`). The splash page and the privacy-policy page also call `loginIoTSDK` (`splash_logic.dart @0x296eba0`, `gdpr_page_logic.dart @0x4016b34`). This is why `AkIotKitFlutter::isLogin` can be true before an account login (see [encryption.md](encryption.md#which-calls-are-encrypted)).
5. **Expiry and invalidation.** `HttpEncryptionDecorator::_handler401` (`@0x486b2bc`) runs when the HTTP status is 401 or when the SDK reports one of three codes (`_handleSdkError`, `@0x486aed0`). With code 401 or 26085 it logs `token 过期` ("token expired", `@0x486b328`) and calls `LogoutHandler::performLogout` with scene `tokenExpired` (`@0x486b3c8`); with code 26084 it logs `账号在其他地方登录` ("account logged in elsewhere", `@0x486b3ec`) and logs out with scene `kickedOut` (`@0x486b51c`); any other code is passed to the failure callback (`401 other code`, `@0x486b534`). Upstream maps 26084 to `TokenKickedOutError` (upstream-confirmed, `errors.py`) and re-logs in when the token has less than 60 seconds left (`session.py`, upstream-confirmed). The numbers and their decoding are in the integer notes below.
6. **No client-side refresh found.** `token_expires_at` is parsed (`iot_user_model.dart @0x2202044`, and `login_handler.dart @0x274167c` for the native login result) but no reader that compares it with the clock and no refresh request was found by grep over the 3.24.3 asm. The app reacts to the server's answer instead (previous row). A negative grep result, not a proof.
7. **Clearing.** Manual logout sends [logout](passport/logout.md) and then `_performCoreCleanup` (`logout_handler.dart @0x38d6bcc`): stored user model (`removeIotUserInfo`, `@0x38d6e94`), encryption info (`clearEncryptionInfo`, `@0x38d6ef4`), MQTT and BLE connections, and the SDK session (`loginOutTSDK`, `@0x38d7140`). The scenes of `LogoutScene` are `manual` 0, `tokenExpired` 1, `kickedOut` 2, `deleteAccount` 3, `freezeAccount` 4, `passwordChanged` 5 (pool entries `pp+0xbb050`, `pp+0x4b500`, `pp+0x4b518`, `pp+0xc2430`, `pp+0xc22e0`, `pp+0xc2528`, shown as plain ints by the pool dump, cross-checked against `Method.get` 0 / `Method.post` 1 in the same format).
8. **`get_token_by_userid` is not the session token.** [power_service/app/get_token_by_userid.md](power_service/app/get_token_by_userid.md) (upstream key `get_token_by_userid`, `POST /power_service/v1/app/get_token_by_userid`, body key `user_id`, `http_request_repository_impl.dart @0x3f2e004`, `@0x3f2e064`) returns a `token` (`@0x3f2e0e4`). Its only traced caller is `ThirdPartyPlatformListLogic::navigateToShellyPage` (`third_party_platform_list_logic.dart @0x3f2de88`, call `@0x3f2df34`), whose success closure appends the token to a Shelly H5 page URL as `?token=` (`@0x3f2e284`) and opens the page `/thirdPartyPlatFormH5` (`@0x3f2e380`). So it is a token for the third-party (Shelly) page; the upstream question mark in `apitypes.py` ("is that the token to be used to query shelly status?") is consistent with this but not proven for Shelly's own API.

Integer notes (Smi rule, [../METHODOLOGY.md](../METHODOLOGY.md#smi-rule-reading-numbers-from-blutter-output)): the codes 401, 26085, 26084 in `_handler401` and `_handleSdkError` are compared as `cmp x0, #0x191` and `cmp x0, x17` with `x17 = 0x65e5` / `0x65e4` on an untagged 64-bit int (`@0x486af08` to `@0x486af1c`, `@0x486b304` to `@0x486b3d0`), so raw equals real: 401, 26085, 26084. The full integer table of the transport codes is in [encryption.md](encryption.md#response-handling-and-error-codes).

## Password encryption at login

Mechanism as upstream describes it (upstream-confirmed, `session.py`, comments at the class header and in `async_authenticate`): the client creates an ECDH key pair, derives a shared secret with the server's public key, and sends the password encrypted with AES-256-CBC under that secret; the client public key travels in `client_secret_info.public_key` (body key owned by [login.md](passport/login.md#request)). The library sends `enc: 0` with the login body.

How the app's names line up (asm-traced, names only): the login screen calls `Encryption::getClientPublicKey` (`login_logic.dart @0x3bd6ea4`) and `Encryption::loginPasswordECDH` (`@0x3bd6ef8`), and `Encryption::clearClientKeyPairs` (`@0x3bd6f4c`) when the step fails. These are forwarders to the platform channel `encryption` (`encryption/encryption_method_channel.dart`: `loginPasswordECDH @0x2faf228`, `getClientPublicKey @0x2faf454`, `clearClientKeyPairs @0x3bd75ac`; channel pool entry `pp+0x36800`), so the work happens natively. The other functions of that package are listed on [encryption.md](encryption.md#where-it-is-implemented). The names `loginPasswordECDH` and `aesCbcEncrypt` fit the ECDH plus AES-CBC mechanism upstream names; whether `loginPasswordECDH` uses exactly that combination internally is not visible in Dart and is a name-level match only. Before the call, `StringExtensions.processPassword` applies the account's `EncType` (`raw` or `sha256`; `validate_account_model.dart @0x2faf368`, see [login.md](passport/login.md#request)).

Scope note: intentionally not documented here (vendor protection; decision pending with the repo owner): the key and secret handling, the cipher parameters and any reproduction recipe.

## Changed since 3.18.0

Compared with the 3.18.0 asm (`ankerAPK/blutter_output`), by identical pool strings and function layouts:

- Login bodies, `Openudid` header, `needEncryption: false` on logout and key exchange, the header names of `_headerToken`, the SDK login map keys, the `401`/`26085`/`26084` handling and the `terminal_id` request are unchanged (all strings present once in both pools; `iotLoginRequest` keys at 3.18.0 `http_request_repository_impl.dart @0x2d28814` to `@0x2d288c4`).
- New in 3.24.3: a branch for HTTP status 461 in `handleStatusCode` (3.18.0 has only the 401 and 463 compares), the function `_handleSdkError` (routes SDK error codes into `_handler401`), the localization key `mismatchTimeAndNetworkCheck` for the 461 message, `cold_start_handler.dart` (push-notification cold start, not auth), and a network-observability interceptor in the Dio setup. The string `akiot.cloud_api` is referenced from 19 Dart files in 3.24.3 against 6 in 3.18.0 (more callers use the SDK path directly; counts by `grep -l`).

## Known unknowns

- Which login entry is the default in 3.24.3: the Dart `LoginLogic::startLogin` (HTTP `/passport/login`) or the native `ank_user_module` container; both exist in both versions.
- `/passport/external_login` is only a string ([passport/external_login.md](passport/external_login.md)); no sender, body or response is known.
- Whether the login request itself goes over the SDK path or the Dio path at run time.
- What the native SDK sends as headers on its requests (beyond the upstream capture) and how it holds the token.
- The server contract for `ab`, `enc`, `time_zone`, `transaction` (sent by upstream, not by the app).
- The exact difference between the visitor token and the user token on the wire.

## Device-tested by

Upstream library (thomluther/anker-solix-api, `AnkerSolixBaseSession`): password login with the ECDH-encrypted password, token and `gtoken` headers on later requests, and re-login before expiry work against real accounts: `upstream-confirmed`. No named client version, device or date is recorded in this repository, so nothing here is `device-tested`.
