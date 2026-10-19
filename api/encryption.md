> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# Encryption of API requests

This page gives an interoperability overview of the encrypted request path of the app: which calls take it, which header names appear on them, how the session key is negotiated at the level of endpoints, and how the transport reports errors. It owns the rule for reading the `encrypted` flag of `data/endpoints.json`. Login, token and common headers are on [auth.md](auth.md); the step trace is [../flows/encrypted_request.md](../flows/encrypted_request.md). Tags and the Smi rule: [../METHODOLOGY.md](../METHODOLOGY.md).

Scope note: this page intentionally does not document how signatures and keys are computed, the values the app embeds, or any step-by-step reproduction of the encryption (vendor protection; decision pending with the repo owner). It names endpoints, header names, function names, error codes and the rule for "is this call encrypted". Where a section would go deeper, a one-line scope note says so.

## Purpose

Lets a reader of the endpoint pages answer: "is this call encrypted, and what does that change for a client?" The short answer, detailed below: the flag in the inventory records which wrapper function a sender calls, not what travels on the wire; the wire form is decided at run time by `HttpEncryptionDecorator::request`, and encrypted calls are performed by the IoT SDK (native), not by Dart code.

## Which calls are encrypted

There are three call paths (asm-traced). Every named HTTP wrapper of the app ends in one of them.

| path | what it is | when |
|---|---|---|
| A. decorator, SDK path | `HttpEncryptionDecorator::request` hands the call to `HttpEncryptionDecorator::_handlerHttpBySdk` (`charging/http/HttpEncryptionDecorator.dart @0x4869874`), which calls `AkIotKitFlutter::handle` (`@0x4869d14`) with the identifier `akiot.cloud_api` (`@0x4869d0c`) and a map `path`, `method`, `param`, `header` (`@0x4869b9c`, `@0x4869c20`, `@0x4869c60`, `@0x4869c9c`); the SDK sends the request natively | all three tests below pass |
| B. decorator, plain path | `HttpRequestImpl::request` (`charging/http/http_request_impl.dart @0x486cee4`, called at `HttpEncryptionDecorator.dart @0x4869700`, log `use anker app url = ` `@0x486961c`): a normal Dio request, JSON body, headers from `_headerToken` ([auth.md](auth.md#common-request-headers)). `HttpRequestImpl::request` accepts a `needEncryption` argument but never reads it (`@0x486d094`) | any test fails |
| C. direct SDK | some senders call the SDK handler themselves with the same identifier: `AkNetwork::requestHttp` (`base_service/util/ak_util/src/ak_network.dart @0x21c3444`, via `AKIoTKitManagerImpl::handle`, `@0x21c3544`), `StationApiClient::request` (`station_home/src/http/station_api_client.dart @0x2a4435c`, via `AkIotKitFlutter::handle`, `@0x2a444c0`), `ScheduleNetwork::_requestHttp` (`ev_charger/.../schedule_network.dart @0x284f6d0`, via `AKIoTKitManagerImpl::handle`, `@0x284f790`) | always; the decorator is not involved |

The three tests in `HttpEncryptionDecorator::request` (`@0x4868ff4`), in the order the code checks them (all `asm-traced`):

1. The SDK reports a logged-in state: `AkIotKitFlutter::isLogin` (`@0x48694f0`), compared with `true` (`@0x4869504`). This is the SDK's own state, which can already be true for a visitor session before any account login ([auth.md](auth.md#token-lifecycle)).
2. `needEncryption` is true. The parameter defaults to `true` (`@0x48691bc`); `false` jumps to the plain path (`tbnz` at `@0x4869510`).
3. The request URL passes a string predicate against `RequestApi::currentBaseUrl` (interface call `@0x4869544`; the selector is not named by Blutter). My reading: the URL must belong to the current API base URL, so calls with `useBaseUrl: false` (foreign hosts) would go the plain path; the exact predicate is a known unknown.

Before these tests (and independent of them), a call that needs a terminal id (`needTerminalId`, default `true`, `@0x486921c`) and has no account login first requests one ([terminal id](#terminal-id)).

Method mapping on the SDK path (`_handlerHttpBySdk`): the `Method` enum index is turned into the string `GET` for 0 (`cmp x2, #0`, `@0x4869974`, string `@0x486997c`), `DELETE` for 2 (`cmp x2, #2`, `@0x4869990`, string `@0x48699a0`) and `PUT` for 3 (boxed compare with raw 6, `cmp w0, #6`, `@0x48699b8`, tagged, so 3; string `@0x48699c0`); every other index, including 1 (`post`), falls to `POST` (`@0x48699d0`). The pool shows `get` as 0 (`pp+0x340e8`) and `post` as 1 (`pp+0xa7e0`); 2 as `delete` and 3 as `put` follow from this mapping and from the order of the pool map `Map<Method, String>` (get, post, delete, put, patch, head; `pp+0x48ad0`), which also suggests `patch` 4 and `head` 5 (not proven by a compare). Those two would be sent as `POST` on this path.

### How the wrappers reach the paths

Rows are `sender` rows of `data/endpoints.json` (598 of the 709 rows; the other 111 are URL-provider rows without a traced sender). `encrypted: true` = the wrapper name contains `encryptionRequestHttp` (449 rows); "note" rows (149) call a plain `requestHttp`/`request` wrapper; `false` rows (111) are URL providers.

| wrapper (callee name in the inventory) | next hop (asm-traced unless marked) | path | rows true / note |
|---|---|---|---|
| `HttpRequestControllerImpl::encryptionRequestHttp` (`http_request_repository_impl.dart @0x2264510`) | forwards all arguments, `needEncryption` default true (`@0x226451c`), to `HttpRequestControllerImpl::requestHttp` (`@0x2264924`) | A | 199 / 0 |
| `HttpRequestControllerImpl::requestHttp` (`@0x2264938`) | checks `isDemoBlockPath` (`@0x2264df0`), logs, then calls the static `HttpRequest` (an `IHttpRequest`, set to a `HttpEncryptionDecorator` around a `HttpRequestImpl` in `charging/boostrap_impl.dart @0x49e0218`, `@0x49e0220`, `@0x49e0288`) with `needEncryption` and `needTerminalId` (`@0x2265018`) | A | 0 / 59 + 1 |
| `HttpServiceImpl::encryptionRequestHttp` (`charging/impl/http_service_impl.dart @0x2284214`) | calls `HttpRequestControllerImpl::encryptionRequestHttp` (`@0x2284520`) | A | 197 / 0 |
| `HttpServiceImpl::encryptionRequestHttpByGHttpRequest` (`@0x2737114`) | forwards to `HttpRequestControllerImpl::encryptionRequestHttp` (`@0x2737230`; the object is the global `gHttpRequest`, static field `0x1094`, `@0x27371cc`) | A | 14 / 0 |
| `BaseGetController::encryptionRequestHttp` (`charging/base/get/getx_controller.dart @0x231e3e4`) | calls `HttpRequestControllerImpl::encryptionRequestHttp` (`@0x231e8a0`) | A | 20 / 0 |
| `BaseGetController::requestHttp` (`@0x230eaa8`) | calls `HttpRequestControllerImpl::requestHttp` (`@0x230ef1c`), no `needEncryption` | A | 0 / 29 |
| `HttpBusinessImpl::encryptionRequestHttp` (`http_business_impl.dart @0x2618680`) | calls `HttpBusinessImpl::requestHttp` (`@0x26187b8`) | A | 6 / 0 |
| `HttpBusinessImpl::requestHttp` (`@0x239ba88`) | `needEncryption` default true (`@0x239bc0c`); calls the static `HttpRequest` with `needTerminalId: true` and `cancelDuplicatedRequest: false` (`@0x239bdac`, `@0x239bdb8`, call `@0x239bdd0`) | A | 0 / 4 + 1 |
| `HttpHelper::request` (`electricity_price/.../http_helper.dart`) | calls `HttpServiceImpl::encryptionRequestHttp` (`@0x2c146c8`, `@0x27bdbc8`, `@0x4393190`) | A | 0 / 7 |
| `HttpRequestControllerImpl::aiotPlatformRequestHttp` (`@0x260dde0`) | calls `HttpRequestControllerImpl::requestHttp` (`@0x260df68`) | A | 0 / 2 |
| mixin applications of `HttpRequestMixin` (`_MixinApplication313&...`, `_MixinApplication417&...`, `_FamilyMainHttpReposity&...`) | no asm: Blutter does not emit `dart:mixin_deduplication` code. `HttpRequestMixin` is declared as `extends BaseGetController` (`charging/http/http_request_mixin.dart`, class header), so the likely target is `BaseGetController` (not traced) | A (inferred) | 13 / 23 |
| `AkNetwork::requestHttp` | `AKIoTKitManagerImpl::handle` (`@0x21c3544`) | C | 0 / 16 |
| `StationApiClient::request` | `AkIotKitFlutter::handle` (`@0x2a444c0`) | C | 0 / 5 |
| `ScheduleNetwork::_requestHttp` | `AKIoTKitManagerImpl::handle` (`@0x284f790`) | C | 0 / 2 |
| total | | | 449 / 149 |

Senders that pass `needEncryption` explicitly (the call descriptors that name it; values decoded from the argument slots, tag asm-traced):

| sender | file `@0xADDR` of the descriptor | value | what it is |
|---|---|---|---|
| `EncryptionUtilImpl::exchangeKey` | `charging/aiot/EncryptionUtilImpl.dart @0x4016f84` | false | `POST /openapi/oauth/key/exchange` ([page](openapi/oauth/key/exchange.md)) |
| `HttpRequestControllerImpl::logOutRequest` | `charging/http/http_request_repository_impl.dart @0x38d66d8` | false | `POST /passport/logout` ([page](passport/logout.md)) |
| `HttpRequestControllerImpl::getRegionHostRequest` | `http_request_repository_impl.dart @0x2740974` | false (also `needTerminal: false`, `useBaseUrl: false`) | `/passport/estimate_domain` |
| `HttpEncryptionDecorator::requestTerminalId` | `HttpEncryptionDecorator.dart @0x4868070` | false (also `needTerminalId: false`) | `POST /passport/terminal_id` ([page](passport/terminal_id.md)) |
| `HdfsManager::uploadAppEventToHDFS` | `charging/hdfs/hdfs_manager.dart @0x224e994` | false | event upload; calls `IHttpRequest.request` directly, not in the inventory |
| `CommonLocation::request` | `charging/feature/common_location/common_location.dart @0x2cbdf40` | true | location lookup; calls `IHttpRequest.request` directly, not in the inventory |

### Rule and resulting counts

The flag `encrypted` does not say "encrypted on the wire". Read each sender row with this rule instead:

1. If the sender is on path C (`AkNetwork`, `StationApiClient`, `ScheduleNetwork`): the SDK sends it, whatever the flag says. **23 rows** (all in the 149 "note" rows).
2. Else, if the sender passes `needEncryption: false` (table above): plain path, **3 rows** (`logOutRequest` is in the 449 "true" rows, `getRegionHostRequest` and `exchangeKey` in the 149 "note" rows).
3. Else (default `needEncryption: true`): the call takes the SDK path whenever the SDK is logged in (visitor sessions count) and the URL passes the base-URL predicate, otherwise the plain path. **572 rows** = 448 "true" rows + 124 "note" rows. Of them, 36 rows go through mixin stubs whose asm is not available (13 + 23); their target is inferred.

Check: 23 + 3 + 572 = 598 sender rows; the 111 `false` rows are URL-provider rows: the flag is not applicable to them (45 of those rows, 41 distinct URLs, have no sender row at all).

The reading for a client author: for a logged-in app session almost every ordinary call (572 of 598 sender rows) is an SDK call. The server also accepts plain calls for the endpoints the upstream library uses: the library keeps payload encryption off by default (`session.py`, `self.encrypt_payload: bool = False`, upstream-confirmed) and has an experimental encrypted mode for the same endpoints. Which endpoints reject a plain call is not recorded in this repository.

## Request headers on encrypted calls

Header names only; each line is a meaning, not a value rule. Dart builds this set in `EncryptionUtilImpl::commonHeaders` (`charging/aiot/EncryptionUtilImpl.dart @0x4016fbc`) and uses it for the key-exchange request. Requests on the SDK path get their encryption headers natively, so for those the names below come from the upstream capture of an app request (`session.py` comment block, upstream-confirmed); the two sets use the same names.

| header | meaning | app (Dart) | upstream capture |
|---|---|---|---|
| `X-Encryption-Info` | marks the scheme; the constant `algo_ecdh` | `@0x40170a8`, value `@0x40170b0` | `x-encryption-info: algo_ecdh` |
| `X-Replay-Info` | replay-protection marker; the constant `replay` | `@0x401702c`, value `@0x4017034` | `x-replay-info: replay` |
| `X-Request-Ts` | request timestamp in seconds (the app's 461 message blames the device clock, see below); built by `getTimeStamp` (`@0x40175dc`: the microsecond clock `_getCurrentMicros` divided by 1000 twice, `sdiv` at `@0x4017644` and `@0x4017648`, constant `r0 = 1000` at `@0x401763c` used in arithmetic, so raw equals real: 1000) | `@0x401705c` | `x-request-ts` |
| `X-Request-Once` | a per-request unique value (replay protection); built by `getRequestOnce` (`@0x4017488`) | `@0x4017084` | `x-request-once` |
| `X-Key-Ident` | identifier of the negotiated session key; read from storage by `getIdentifyKey` (`@0x40170dc`) | `@0x40170f8` | `x-key-ident` |
| `X-Signature` | request signature, built by `getSignature` (`@0x4017200`) | `@0x4017150` | `x-signature` |
| `X-App-Key` | the empty string | `@0x40171cc`, value `@0x40171d4` | `x-app-key: ` |
| `App-name` | the constant `anker_power` | `@0x40171a0`, value `@0x40171a8` | `app-name: anker_power` |
| `Content-Type` | `application/json` in the Dart key-exchange request | `@0x4017174`, value `@0x401717c` | `text/plain` on encrypted API calls (the body is an encrypted text), `application/json` on the key exchange |
| `X-Auth-TS` | authentication timestamp, only in the upstream key-exchange request | not in `commonHeaders` | `x-auth-ts` |

The ordinary identity headers (`X-Auth-Token`, `gtoken`, `App-Name`, `App-Version`, `Language`, `Timezone`, `Country`, ...) are on [auth.md](auth.md#common-request-headers). On an encrypted call the upstream capture shows the body as encrypted text and the response as `signature`, `msg`, `code`, `trace_id`, `data` with an encrypted `data` (upstream-confirmed); the encryption of body and response is a scope note.

Scope note: intentionally not documented here (vendor protection; decision pending with the repo owner): what goes into `X-Signature`, `X-Key-Ident` and `X-Request-Once`, and how the body and response are encrypted.

## Key-exchange endpoint

`POST /openapi/oauth/key/exchange` with the body key `client_public_key`; the answer carries `server_public_key`. The page [openapi/oauth/key/exchange.md](openapi/oauth/key/exchange.md) owns the body, the skip rule (a stored key and identifier mean no new exchange), the callers (`GdprPageLogic::allow`, `gdpr_page_logic.dart @0x4016998`) and the answer handling (`EncryptionUtilImpl::parse`, `@0x4017978`, which stores the derived key and its identifier with `SpUtilImpl::saveAesKey` and `saveIdentifyKey`). The exchange itself is sent with `needEncryption: false`. The stored keys are removed on logout (`clearEncryptionInfo`) and when the region changes. The server code 26070 is mapped upstream to `ClientPublicKeyError` (upstream-confirmed).

Scope note: intentionally not documented here (vendor protection; decision pending with the repo owner): how `client_public_key` is formed and how the answer becomes the session key.

## Terminal id

`POST {base URL}/passport/terminal_id` with the body key `gen_key` (empty string), owned by [passport/terminal_id.md](passport/terminal_id.md). It is requested by `HttpEncryptionDecorator::request` (`@0x4869310`) for any call with `needTerminalId` (default true) while no account is logged in, once (an `HttpEncryptionDecorator` lock serializes callers, a stored id is reused). It is not part of the signature headers; it travels as `Openudid` on login calls, as `X-Terminal-ID` on the plain path when there is no `gtoken`, and to the SDK as `terminalId`.

## Response handling and error codes

`HttpEncryptionDecorator` (`charging/http/HttpEncryptionDecorator.dart`) handles responses of both paths. The SDK returns an `AKIoTResult` that the app converts (`IoTAKResult.fromAKIoTResult`, `@0x486aa78`) and whose `data` it JSON-decodes (`@0x486ab9c`, `decode` `@0x486ac18`): the decryption has already happened natively. On error the closure calls `_handleSdkError` (`@0x486ad18`). On the plain path, `successCallback`/`failCallback` closures call `_handleResponse` (`@0x486c2dc`, builds a `Result` with `Result.fromJson`) and `handleStatusCode`.

Codes seen (Smi rule applied; "raw" is the immediate in the asm, "width" tells whether the compare or store is on a tagged 32-bit value or an untagged 64-bit one):

| meaning | where (`HttpEncryptionDecorator.dart`) | raw | width | real |
|---|---|---|---|---|
| HTTP status 401 | `handleStatusCode` `cmp w1, #0x322`, `@0x486b0d4` | 0x322 = 802 | tagged | 401, goes to `_handler401` |
| HTTP status 463 | `cmp w1, #0x39e`, `@0x486b100`; second compare `cmp w0, #0x39e`, `@0x486b108` | 0x39e = 926 | tagged | 463; log `request fail for url: ... with 463 other code` (`@0x486b158`), failure callback |
| HTTP status 461 | `cmp w1, #0x39a`, `@0x486b1ac` | 0x39a = 922 | tagged | 461; log `request fail for url: ... with 461 timestamp error, device time may be incorrect` (`@0x486b1d8`) |
| code handed to the failure callback for 461 | `r30 = 922`, `@0x486b210`, passed as an argument | 922 | tagged | 461; message is the server message or, if empty, the localization key `RS.mismatchTimeAndNetworkCheck` (`@0x486b204`) |
| no result model (content type error) | `r2 = -100`, `@0x486b074`, then `BoxInt64Instr` | -100 | untagged | -100, log `content type error` (`@0x486b058`) |
| other HTTP status | log `request fail for url: ... with other code` (`@0x486b258`) | n/a | n/a | passed through |
| signature check failed | `_handler200`: `r16 = 926` passed as an argument, `@0x486c808`, after `HttpRequestManager::validateSignature` returned false (`@0x486c75c`, compare `@0x486c770`); log `签名校验不通过，需要重新协商key` ("signature check failed, key must be renegotiated", my translation, `@0x486c7ec`) | 926 | tagged | 463 |
| body `code` of the answer | `_handler200`: `cbnz w0` on the tagged `code` field, `@0x486c708` | 0 | tagged | 0 = success; any other value is logged (`http error: body code is not iot success code`, `@0x486c8a4`) and passed to the failure callback with the body message (`code` defaults to 0 if null, `@0x486c914`) |
| terminal id missing | `request`: `mov x16, #-0xca` passed as an argument, `@0x486933c` | -202 | tagged | -101 (log `TerminalIdError`, `@0x4869380`) |
| token expired (SDK or HTTP 401 body) | `_handleSdkError` `cmp x0, #0x191`, `@0x486af08`; `_handler401` `@0x486b304` | 0x191 = 401 | untagged | 401 |
| token expired | `mov x17, #0x65e5`, `@0x486af10`, `@0x486b30c` | 0x65e5 | untagged | 26085 |
| logged in elsewhere (kicked out) | `mov x17, #0x65e4`, `@0x486af1c`, `@0x486b3d0` | 0x65e4 | untagged | 26084 |

What the app does per code: 461 and 463 are reported to the caller as failures (461 with a hint that the device time may be wrong). 463 also stands for a failed response signature check in `_handler200`, after which the log says the key must be renegotiated; no automatic `exchangeKey` call follows in that function (the only `exchangeKey` caller is the privacy-policy page). 401 (as HTTP status with body code 401 or 26085) and the SDK codes 401/26085 lead to a forced logout with scene `tokenExpired`; 26084 leads to scene `kickedOut` (`_handler401 @0x486b2bc`, [auth.md](auth.md#token-lifecycle)). `_getErrorMsg` (`@0x486bd64`) maps SDK-side error values to three localization keys, `netWorkError`, `requestTimeout` and `errorOccur`; the numeric tests compare against large negative constants that were not decoded (Known unknowns). Login-screen codes (26108, 26105, 100053, ...) are on [passport/login.md](passport/login.md#errors-seen). The catalog `api/errors.md` is created by Task 4.2; upstream maps 401/403 to `AuthorizationError`, 26084 to `TokenKickedOutError` and others in `api/errors.py` (upstream-confirmed).

## Where it is implemented

Function names only, with the file and address of the function.

| area | file | functions |
|---|---|---|
| wrappers | `charging/http/http_request_repository_impl.dart` | `encryptionRequestHttp` (`@0x2264510`), `requestHttp` (`@0x2264938`) |
| decorator | `charging/http/HttpEncryptionDecorator.dart` | `request` (`@0x4868ff4`), `requestTerminalId` (`@0x4867cd8`), `_handlerHttpBySdk` (`@0x4869874`), `_convertToMap` (`@0x4869dc0`), `_deepConvertMap` (`@0x486a1a8`), `_deepConvertList` (`@0x486a62c`), `_handleSdkError` (`@0x486aed0`), `handleStatusCode` (`@0x486afc0`), `_handler401` (`@0x486b2bc`), `_getErrorMsg` (`@0x486bd64`), `_handleResponse` (`@0x486c2dc`), `_handler200` (`@0x486c680`) |
| plain transport | `charging/http/http_request_impl.dart` | `HttpRequestImpl::request` (`@0x486cee4`), `createInstance` (`@0x4868a00`), `_headerToken` (`@0x486d610`) |
| encryption utility | `charging/aiot/EncryptionUtilImpl.dart` | `decryptLocalInfo` (`@0x21d4938`), `encryptLocalInfo` (`@0x273b7d4`), `getPresetKey` (`@0x2dbb554`), `exchangeKey` (`@0x4016d54`), `commonHeaders` (`@0x4016fbc`), `getSignature` (`@0x4017200`), `getAesKey` (`@0x401741c`), `getRequestOnce` (`@0x4017488`), `getTimeStamp` (`@0x40175dc`), `parse` (`@0x4017978`), `newLocalInfoAesKey` (`@0x49dde44`), `getLocalInfoAeskey` (`@0x49de0d0`) |
| crypto primitives (platform channel `encryption`) | `encryption/encryption.dart`, `encryption/encryption_method_channel.dart` | `loginPasswordECDH`, `getClientPublicKey`, `clearClientKeyPairs`, `hMacEncrypt`, `aesCbcEncrypt`, `getExchangedAesKey`, `aesCbcDecrypt`, `computeEcdhWithPublicKey`, `HKDF`; forwarders at `@0x2faf228`, `@0x2faf454`, `@0x3bd75ac`, `@0x401735c`, `@0x40176ec`, `@0x4017c28`, `@0x4017d34`, `@0x484b8b4`, `@0x49de00c` |
| SDK bridge (platform channel `ak_iot_kit_flutter`) | `ak_iot_kit_flutter/src/ak_iot_kit_flutter.dart` | `handle` (`@0x21c3d8c`: method `handle` with `identifier` and `param`), `loginAnkerCloud` (`@0x273dcac`), `logout` (`@0x273e7c0`), `isLogin` (`@0x273e8dc`), `updateConfig`, `initSDK` |

What stays in Dart and what is forwarded: Dart picks the path, builds the request map, assembles the key-exchange header map (timestamp, per-request value, constants, key identifier from storage) and stores the results (`SpUtilImpl` keys). Every cryptographic primitive is a platform channel call (`encryption` channel, pool entry `pp+0x36800`, name `encryption`); the SDK path forwards the entire request, including header building, signing, encryption and decryption, to the native SDK (channel `ak_iot_kit_flutter`, pool entry `pp+0xc468`). A native library named `libecc-encryption.so` ships in the 3.24.3 APK (`arm64-v8a`); that it backs the `encryption` channel is plausible but was not traced (no native analysis).

## Scope note

Not documented on this page, on purpose (vendor protection; decision pending with the repo owner): the construction of `X-Signature`, `X-Key-Ident` and `X-Request-Once`; the cipher, key-derivation and hash parameters; the keys and constants the app embeds (two 32-character hex constants exist in `EncryptionUtilImpl`; their publication is a decision for the repo owner); how `client_public_key` and the session key are formed; the format of encrypted bodies and responses; the visitor token. The upstream library (thomluther/anker-solix-api, `session.py`, `AnkerEncryptionHandler`) is public and implements an encrypted mode; this repository does not restate it.

## Changed since 3.18.0

Compared with the 3.18.0 asm: the decorator layout, `needEncryption` default (`true`), the path decision, `EncryptionUtilImpl` (same function names, `exchangeKey` with `needEncryption: false` at 3.18.0 `@0x311a47c`, header names `X-Replay-Info`, `X-Encryption-Info`, `X-Key-Ident`, `X-Request-Once`, `X-Request-Ts`, `X-Signature`), the `terminal_id` step and the 401/463 handling are all present in 3.18.0. New in 3.24.3: the 461 branch of `handleStatusCode` and its message key `mismatchTimeAndNetworkCheck`, the function `_handleSdkError`, a Dio observability interceptor (`NetworkObservabilityInterceptor`) and net-performance logging on the SDK path (`logNetPerf`, `@0x486ae74`; `logNetPerf` is absent from the 3.18.0 pool and asm, present in `charging/ume/network_monitor/` in 3.24.3), and more direct SDK callers (`akiot.cloud_api` in 19 Dart files against 6). No header name or endpoint of the encrypted path changed.

## Known unknowns

- How the native SDK builds its encrypted requests and which headers it adds (only the upstream capture is known).
- Which endpoints the server rejects when sent plain; the inventory cannot tell.
- The 36 rows behind mixin stubs (`HttpRequestMixin` applications) are inferred to follow path A; their asm is not emitted by Blutter.
- The selector of the URL predicate in `request` (`@0x4869544`) and the exact meaning of its result for relative paths.
- The numeric thresholds in `_getErrorMsg` (`@0x486bd64`).
- Whether an SDK request also needs the visitor/terminal id to be present, and what the SDK does on 461 or 463 beyond reporting them.
- Whether `libecc-encryption.so` implements the `encryption` channel (no native analysis).

## Device-tested by

Upstream library (thomluther/anker-solix-api): key exchange and an encrypted `get_device_attrs`-style request against the EU server work in its experimental encrypted mode; plain requests work in the default mode (`upstream-confirmed`). No named client version, device PN, firmware or date is recorded here, so nothing is `device-tested`.
