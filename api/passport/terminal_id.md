> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# terminal_id

## Purpose

Asks the server for a terminal id (the app's anonymous client identity before login); the app stores it and sends it later as the `Openudid` header, as `X-Terminal-ID`, and to the IoT SDK as `terminalId`.

## Upstream name

`none` (no upstream name): `api/apitypes.py` has no key for this URL; it is listed in the upstream comment block of known passport URLs and the upstream library never calls it (upstream-confirmed as a known URL name only).

## Method+URL

`POST {base URL}/passport/terminal_id` (asm-traced): URL string `pp+0x4b370` at `charging/http/HttpEncryptionDecorator.dart @0x4867ec4`, joined to `RequestApi::currentBaseUrl` (`@0x4867ea4`) by string interpolation, so the call carries a full URL; method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x4868034`; the log line says `requestTerminalId post for url:` (`@0x4867f6c`). The function is `HttpEncryptionDecorator::requestTerminalId` (`@0x4867cd8`, work done in the closure `@0x4867d50`).

## Encrypted?

No by explicit choice (asm-traced): the interface call to `HttpRequest.request` (`@0x4868078`, descriptor `@0x4868070`) passes `needEncryption: false` and `needTerminalId: false` (`r30 = false` `@0x4868058`, `r16 = false` `@0x4868054` and `@0x4868060`), so the request cannot recurse into the terminal-id step and does not use the SDK path (see [../encryption.md](../encryption.md#terminal-id)).

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `gen_key` | String | yes | `""` | key `@0x4867fd4`, value is the empty string literal `@0x4867fe0` (map type `<String, String>`) |

## `param_type`/`cmd`

n/a

## Response model (link)

`TerminalId` (asm-traced, allocated at `HttpEncryptionDecorator.dart @0x486830c`); no `models/` page exists for it yet.

## Response

The success closure (`@0x4868188`) checks that the payload is a `Map<String, dynamic>` and reads one key.

| field | type | required | example | source |
|---|---|---|---|---|
| `terminal_id` | String | yes | `"<terminal id>"` | key read at `HttpEncryptionDecorator.dart @0x48682ac`; stored with `SpUtilImpl::setTerminalId` (`@0x48683ec`) |

Right after storing it, the closure waits for `isSDKInitialized` and, if the IoT SDK is not logged in, logs it in with the visitor secret (`AKIoTKitManagerImpl::loginIoTSDK`, `@0x4868514`), so a visitor session exists in the SDK before any account login. On failure (`@0x48680c8`, log `_requestTerminalId 11 for url: ... fail code = ...`) the closure completes with the empty string (`@0x4868160`).

## Example request/response

Request, synthesized

```json
{ "gen_key": "" }
```

Response, synthesized (shape only)

```json
{ "code": 0, "msg": "success!", "data": { "terminal_id": "<terminal id>" } }
```

## Errors seen

The code catalog is [errors.md](../errors.md). If no non-empty id results, `HttpEncryptionDecorator::request` logs `TerminalIdError` (`@0x4869380`) and calls the failure callback with code -101 and an empty message (raw `mov x16, #-0xca` at `@0x486933c` is passed as an argument, so it is a tagged Smi and the code is -101) instead of sending the original request.

## Callers in app

- `charging/http/HttpEncryptionDecorator.dart`: `requestTerminalId` @0x4867cd8. Called from `HttpEncryptionDecorator::request` (`@0x4869310`) when `needTerminalId` is true (default `true`, `@0x486921c`) and the account is not logged in (`SpUtilImpl::isLogin`, `@0x4869304`; the branch skips the call when it returns true, `@0x4869308`). A `BasicLock` serializes concurrent callers (`synchronized`, `@0x4867d34`); inside the lock an already stored non-empty id is returned without a request (`SpUtilImpl::getTerminalId`, `@0x4867dbc`, empty check `@0x4867dc8`).
- Consumers of the stored id: header `Openudid`, sent by `aiotPlatformRequestHttp` (`@0x260de6c`), `uploadDeviceToken` (`@0x27418d8`), `getAlexaLinkCodeRequest` (`@0x3bce938`, `@0x3bcea54`), `thirdLoginRequest` (`@0x3bd1a3c`), `iotLoginRequest` (`@0x3bd721c`), `verifyCodeLoginRequest` (`@0x3bd84d4`), all in `http_request_repository_impl.dart` (see [login](login.md#request), [third_party_login](third_party_login.md#request) for the two login bodies), header `X-Terminal-ID` on the plain path ([../auth.md](../auth.md#common-request-headers)), the SDK login map key `terminalId` ([../auth.md](../auth.md#token-lifecycle)), and the native login module (`ank_user_module_method_channel.dart`, `setOpenUdid`, string at `@0x26fd364`).

Clear-or-keep (traced 2026-10-20, app side): the logout cleanup only reads the stored id (`getTerminalId`, `charging/account/handlers/logout_handler.dart @0x38d6f5c`, used for `loadPersistedDeviceForUser` `@0x38d6f70`) and does not remove it. `removeTerminalId` is called at three sites only: `SplashLogic::onReady` (`charging/ui/page/account/splash/splash_logic.dart @0x293cf0c` and, after the log `terminalId is false`, `@0x293d008`) and `DemoSiteUtilImpl::exitDemo` (`charging/util/demosite_util_impl.dart @0x2741eac`). So a logout keeps the id; the app clears it on start-up in the two splash branches and when the demo site is left.

## Since/changed

3.18.0: present (3.18.0 `HttpEncryptionDecorator.dart`: URL string at `0x1b921bc`, key `gen_key` at `0x1b922d4`). 3.24.3: same URL and body key. since: ≤3.18.0.

## Known unknowns

- What the server derives the id from (the request carries no client data, only `gen_key: ""`) and whether it is stable per installation or per call.

## Device-tested by

none
