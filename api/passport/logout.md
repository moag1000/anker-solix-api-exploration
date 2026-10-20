> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# logout

## Purpose

Tells the server that the session of the current user ends; the app sends an empty body and then clears its stored encryption information and all local user data.

## Upstream name

`none` (no upstream name): `api/apitypes.py` has no key for this URL and the upstream library never logs out; the URL is only in the upstream list of known passport URLs.

## Method+URL

`POST /passport/logout` (asm-traced): URL string `pp+0xbb090` at `charging/http/http_request_repository_impl.dart @0x38d66ac`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x38d66a4`, in `HttpRequestControllerImpl::logOutRequest` (`@0x38d65c0`).

## Encrypted?

No by explicit choice (asm-traced): `logOutRequest` calls `encryptionRequestHttp` with `needEncryption: false` (`r30 = false` stored into the argument slot of `needEncryption`, `@0x38d66c8`; call descriptor `@0x38d66d8`, call `@0x38d66e0`). With that flag the decorator skips the SDK path and sends the request over the plain Dio path (see [../encryption.md](../encryption.md#which-calls-are-encrypted)). The inventory flag `encrypted: true` for this row only records that the wrapper is called `encryptionRequestHttp`; it does not describe the transport.

## Request

The data argument is an empty map (`Map._fromLiteral` with `THR::empty_array`, `@0x38d6620`). No header argument.

| field | type | required | example | source |
|---|---|---|---|---|
| (none) | | | `{}` | `http_request_repository_impl.dart @0x38d6620` |

The common request headers (token and client information) are added by the transport, see [../auth.md](../auth.md#common-request-headers).

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the success closure parses the wrapper only (`Result.fromJson`, `http_request_repository_impl.dart @0x38d6800`).

## Response

| field | type | required | example | source |
|---|---|---|---|---|
| (wrapper `code`/`msg`) | | | | `Result.fromJson` at `@0x38d6800`; no field is read afterwards |

After a successful answer the closure calls `SpUtilImpl::clearEncryptionInfo` (`@0x38d6848`), which removes the stored session key material (`api/encryption.md` lists where it is set). The failure closure (`@0x38d66fc`) only logs `---> log out failed, code: ..., msg: ...`.

## Example request/response

Request, synthesized

```json
{}
```

Response, synthesized: the standard wrapper (`code`, `msg`, `data`), see [login](login.md#response).

## Errors seen

The code catalog is [errors.md](../errors.md). No logout-specific code branch exists; the failure closure logs code and message and calls the failure callback of the caller.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `logOutRequest` @0x38d65c0.
- Called from `charging/account/handlers/logout_handler.dart::performLogoutWithRequest` (`@0x38d63dc`, call to the controller at `@0x38d64c4`; the log line says "Starting logout flow (with server request) - scene: manual") and `charging/http/http_request_repository.dart::logOutRequest`.
- After the request, the handler runs `LogoutHandler::_performCoreCleanup` (`@0x38d6bcc`, called at `@0x38d68c0`) and the native module logout (`AnkUserModule` `logout`, `@0x38d68d0`). The cleanup, among other things, removes the stored user model (`SpUtilImpl::removeIotUserInfo`, `@0x38d6e94`), clears the encryption info (`@0x38d6ef4`), disconnects MQTT (`MqttServe::clearAndDisconnect`, `@0x38d705c`) and BLE (`BleManager::disconnect`, `@0x38d701c`) and logs the IoT SDK out (`AKIoTKitManagerImpl::loginOutTSDK`, `@0x38d7140`).
- Forced logouts after token errors do not send this request; they call `LogoutHandler::performLogout` directly (see [../auth.md](../auth.md#token-lifecycle)).

## Since/changed

3.18.0: present (`http_request_repository_impl.dart`, 3.18.0 `@0x2347db8`, descriptor with `needEncryption` at `@0x2347de4`, `r30 = false` at `@0x2347dd4`). 3.24.3: unchanged. since: ≤3.18.0.

## Known unknowns

- Whether the server invalidates the token on this call (the app clears its own copy either way).
- Whether `_performCoreCleanup` runs when the request fails: the order of the closures in `performLogoutWithRequest` was not traced to that level. — traced 2026-10-20: `performLogoutWithRequest` (`charging/account/handlers/logout_handler.dart @0x38d63dc`) passes the closure that runs `_performCoreCleanup` as the named argument `complete` (argument descriptor `@0x38d64bc`, closure `@0x38d6870`, call `@0x38d64c4`); `logOutRequest` forwards `complete` to `requestHttp` (`charging/http/http_request_repository_impl.dart @0x38d66d8`, descriptor name `complete`) next to its own success closure `@0x38d67b8` and failure closure `@0x38d66fc`. Whether `requestHttp` calls `complete` after a failed request is decided in code outside the app asm tree, so the failure case is not readable

## Device-tested by

none
