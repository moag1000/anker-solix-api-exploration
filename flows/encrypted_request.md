> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# Encrypted request

How an ordinary cloud call of the app travels from the page that triggers it to the decoded answer, at the level of endpoints and function names. This page links to the owners of every fact and copies none. Scope note: intentionally not documented here (vendor protection; decision pending with the repo owner): signature and key computation, embedded values, and step-by-step reproduction of the encryption; see [../api/encryption.md](../api/encryption.md#scope-note).

## Trigger (UI action)

Any user action or page start that calls a sender function of the app. Example used for the citations: opening the station power limit page, whose `_getStationPowerLimit` sends `get_power_limit` through `encryptionRequestHttp` (`station_power_limit_logic.dart @0x28cac9c`, see [system_output_limit.md](system_output_limit.md)). Tag: asm-traced.

## Preconditions

- A session key and key identifier are stored, from the one-time key exchange at the privacy-policy step (`gdpr_page_logic.dart @0x4016998`, [exchange](../api/openapi/oauth/key/exchange.md)); without them `exchangeKey` would run again, with them it returns early.
- A terminal id exists, or is requested in step 3 ([terminal_id](../api/passport/terminal_id.md)).
- The IoT SDK is logged in: as a visitor after startup or as the user after login ([auth.md](../api/auth.md#token-lifecycle)). If it is not, the call falls to the plain path (step 9).
- Cloud path only; this flow makes no BLE or MQTT call (BLE is not a live fallback for it).

## Steps

| # | actor | action | owner page link | asm citation |
|---|---|---|---|---|
| 1 | app | A page logic calls a sender wrapper (`encryptionRequestHttp` or `requestHttp` of `HttpServiceImpl`, `BaseGetController`, `HttpBusinessImpl` or the controller). | [encryption.md](../api/encryption.md#how-the-wrappers-reach-the-paths) | `station_power_limit_logic.dart @0x28cac9c` |
| 2 | app | `HttpRequestControllerImpl::encryptionRequestHttp` forwards to `requestHttp`, which stops if `isDemoBlockPath`, logs `request URL ==============> ...` and calls the static `HttpRequest` (the `HttpEncryptionDecorator`) with `needEncryption` (default true) and `needTerminalId`. | [encryption.md](../api/encryption.md#how-the-wrappers-reach-the-paths) | `http_request_repository_impl.dart @0x2264924`, `@0x2264df0`, `@0x2265018` |
| 3 | app | `HttpEncryptionDecorator::request`: if `needTerminalId` and no account login, call `requestTerminalId` (a stored id is reused; a missing id ends the call with code -101). | [terminal_id](../api/passport/terminal_id.md) | `HttpEncryptionDecorator.dart @0x4869310`, `@0x486933c` |
| 4 | cloud | Only on the first call: `POST /passport/terminal_id` answers with `terminal_id`; the app stores it and, if the SDK is not logged in, logs it in as a visitor. | [terminal_id](../api/passport/terminal_id.md#response) | `HttpEncryptionDecorator.dart @0x48682ac`, `@0x4868514` |
| 5 | app | Adds the header `X-Biz-Func: demosite` in demo-site mode. | [auth.md](../api/auth.md#common-request-headers) | `HttpEncryptionDecorator.dart @0x486942c` |
| 6 | app | Decides the path: SDK logged in (`AkIotKitFlutter::isLogin`), `needEncryption` true, URL passes a string predicate against the current base URL. | [encryption.md](../api/encryption.md#which-calls-are-encrypted) | `HttpEncryptionDecorator.dart @0x48694f0`, `@0x4869510`, `@0x4869544` |
| 7 | app | SDK path: `_handlerHttpBySdk` maps the method to `GET`, `POST`, `PUT` or `DELETE`, builds `path` (URL without the base URL and the slash), `method`, `param`, `header` and calls the SDK handler `akiot.cloud_api` over the channel `ak_iot_kit_flutter`. | [encryption.md](../api/encryption.md#which-calls-are-encrypted) | `HttpEncryptionDecorator.dart @0x4869874`, `@0x4869d0c`, `@0x4869d14` |
| 8 | cloud | The SDK sends the request natively with the encryption headers (`X-Encryption-Info`, `X-Replay-Info`, `X-Request-Ts`, `X-Request-Once`, `X-Key-Ident`, `X-Signature`, plus the identity headers); the answer is an encrypted body with a `signature` field. How this is built is not traced. | [encryption.md](../api/encryption.md#request-headers-on-encrypted-calls) | upstream-confirmed (`session.py` capture of an app request and response) |
| 9 | app | Plain path (any test in step 6 failed, or `needEncryption` is false): `HttpRequestImpl::request` checks connectivity, builds the headers with `_headerToken` and sends JSON with Dio. | [auth.md](../api/auth.md#common-request-headers) | `http_request_impl.dart @0x486d150`, `@0x486d1ec`, `@0x486d3cc` |
| 10 | app | SDK path answer: the SDK result is converted to an `IoTAKResult` and its `data` JSON-decoded (already decrypted natively); an error result goes to `_handleSdkError`. | [encryption.md](../api/encryption.md#response-handling-and-error-codes) | `HttpEncryptionDecorator.dart @0x486aa78`, `@0x486ac18`, `@0x486ad18` |
| 11 | app | `_handler200`: body `code` 0 is success and the success callback gets the data; if the signature check fails the failure callback gets 463; any other body code goes to the failure callback with its message. | [encryption.md](../api/encryption.md#response-handling-and-error-codes) | `HttpEncryptionDecorator.dart @0x486c708`, `@0x486c75c`, `@0x486c808` |
| 12 | app | The caller's success closure parses the model, for example `StationPowerLimitModel` for the example call. | [get_power_limit](../api/power_service/site/get_power_limit.md) | `http_request_repository_impl.dart @0x23790e0` |

## Side effects

- A terminal id is stored on first use (`SpUtilImpl::setTerminalId`), and an SDK visitor login may happen (`loginIoTSDK`).
- Request and response metadata is recorded for network monitoring and SDK calls are logged with a net-performance record tagged `SDK` (`logNetPerf`, `HttpEncryptionDecorator.dart @0x486ae6c`, `@0x486ae74`).
- Token errors trigger a forced logout that clears user data, keys and connections ([logout](../api/passport/logout.md), [auth.md](../api/auth.md#token-lifecycle)).
- The stored session key and identifier are removed on logout and on a region switch.

## Timing (delays/polling)

No polling and no retry loop on this path. Timeouts exist only for the plain path (Dio `BaseOptions`, `http_request_impl.dart @0x4868a88`): connect and send timeout 15 s (shared constant duration `pp+0x2a740`, pool value 15,000,000 microseconds), receive timeout 10 s (`Duration` built with the raw constant 10,000,000, `mov x0, #0x9680` + `movk x0, #0x98, lsl #16`, `@0x4868a34`, stored with a 64-bit `stur x0` at `@0x4868a40`, unboxed, so 10,000,000 microseconds). The SDK path timeouts are inside the native SDK and unknown. Duplicate calls are only cancelled when a sender sets `cancelDuplicatedRequest`; the wrappers default it to false (`HttpBusinessImpl::requestHttp` passes false, `@0x239bdb8`).

## Failure paths

- No network: the plain path stops before sending and reports `commonNetWorkErrorFix` (`http_request_impl.dart @0x486d150`, `@0x486d174`).
- Terminal id missing: code -101, request not sent ([terminal_id](../api/passport/terminal_id.md#errors-seen)).
- HTTP 461: failure callback with code 461 and a hint that the device time may be wrong (`HttpEncryptionDecorator.dart @0x486b1ac`, `@0x486b210`).
- HTTP 463, or a failed response signature check: failure callback with 463; the log says the key must be renegotiated, but no renegotiation is started there (`@0x486b100`, `@0x486c808`).
- HTTP 401 or the SDK codes 401, 26085, 26084: forced logout, scene `tokenExpired` or `kickedOut` (`_handler401 @0x486b2bc`).
- Content type error (no parsable result): code -100 (`@0x486b074`).
- The catalog of codes is `api/errors.md` (not yet written, Task 4.2); the codes seen so far are in [encryption.md](../api/encryption.md#response-handling-and-error-codes).

## Known unknowns

- What the native SDK does between step 7 and step 10 (headers, signing, encryption, retries, timeouts).
- Whether the SDK renegotiates the key by itself after 463.
- How mixin-based senders (36 inventory rows) reach the wrappers; their asm is not emitted.
- Whether a visitor SDK session is enough for the SDK path to accept calls that need an account.
