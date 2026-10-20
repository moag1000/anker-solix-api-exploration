> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# Encryption of API requests

This page documents the encrypted request path of the app for interoperability: which calls take it, the headers on them and where each value comes from, how the session key is negotiated, how a request is signed, how nonce and timestamp enter the signature, what an encrypted body looks like on the wire, and a minimal sequence for a library that wants to talk to the cloud with its own account. It owns the rule for reading the `encrypted` flag of `data/endpoints.json`. Login, token and common headers are on [auth.md](auth.md); the step trace is [../flows/encrypted_request.md](../flows/encrypted_request.md). Tags and the Smi rule: [../METHODOLOGY.md](../METHODOLOGY.md).

Scope: the application-layer encryption is signing, replay protection and payload confidentiality on top of TLS; it is not an account login. The account login and password encryption stay on [auth.md](auth.md) and are not extended here. On the cloud and wire path Dart only invokes the cryptographic primitives through the platform channel `encryption` (pool `pp+0x36800`: `getExchangedAesKey`, `hMacEncrypt`, `aesCbcEncrypt`, `aesCbcDecrypt`, `getClientPublicKey`) and, for ordinary encrypted calls, hands the whole request to the IoT SDK (channel `ak_iot_kit_flutter`, pool `pp+0xc468`). That the primitives themselves (ECDH, HKDF, HMAC, AES-CBC) run in native code is inferred from the method names, not traced. Dart does AES-CBC itself only for local storage, via the `encrypt` package (`AesHelper`, [Local-info key](#local-info-key-not-part-of-the-wire-protocol)). The native libraries are out of scope, so this page documents what Dart passes to the primitives (inputs, order, separators) and marks what the primitives do internally as a known unknown. One value is deliberately given by role and location only: the app-embedded preset key (see [Session key and key identifier](#session-key-and-key-identifier)).

## Contents

- [Purpose](#purpose)
- [Which calls are encrypted](#which-calls-are-encrypted)
- [Request headers on encrypted calls](#request-headers-on-encrypted-calls)
- [Key-exchange endpoint](#key-exchange-endpoint)
- [Session key and key identifier](#session-key-and-key-identifier)
- [Request signing](#request-signing)
- [Nonce and timestamp](#nonce-and-timestamp)
- [Payload encryption and response decryption](#payload-encryption-and-response-decryption)
- [Local-info key (not part of the wire protocol)](#local-info-key-not-part-of-the-wire-protocol)
- [For library implementers](#for-library-implementers)
- [Terminal id](#terminal-id)
- [Response handling and error codes](#response-handling-and-error-codes)
- [Where it is implemented](#where-it-is-implemented)
- [Scope note](#scope-note)
- [Changed since 3.18.0](#changed-since-3180)
- [Known unknowns](#known-unknowns)
- [Device-tested by](#device-tested-by)

## Purpose

Lets a reader of the endpoint pages answer: "is this call encrypted, and what does that change for a client?" The short answer, detailed below: the flag in the inventory records which wrapper function a sender calls, not what travels on the wire; the wire form is decided at run time by `HttpEncryptionDecorator::request`, and encrypted calls are performed by the IoT SDK (native), not by Dart code.

## Which calls are encrypted

There are three call paths (asm-traced). Every named HTTP wrapper of the app ends in one of them.

| path | what it is | when |
|---|---|---|
| A. decorator, SDK path | `HttpEncryptionDecorator::request` hands the call to `HttpEncryptionDecorator::_handlerHttpBySdk` (`charging/http/HttpEncryptionDecorator.dart @0x4869874`), which calls `AkIotKitFlutter::handle` (`@0x4869d14`) with the identifier `akiot.cloud_api` (`@0x4869d0c`) and a map `path`, `method`, `param`, `header` (`@0x4869b9c`, `@0x4869c20`, `@0x4869c60`, `@0x4869c9c`); the SDK sends the request natively | all three tests below pass |
| B. decorator, plain path | `HttpRequestImpl::request` (`charging/http/http_request_impl.dart @0x486cee4`, called at `HttpEncryptionDecorator.dart @0x4869700`, log `use anker app url = ` `@0x486961c`): a normal Dio request, JSON body, headers from `_headerToken` ([auth.md](auth.md#common-request-headers)). `HttpRequestImpl::request` accepts a `needEncryption` argument but never reads it (`@0x486d094`) | any test fails |
| C. direct SDK | some senders call the SDK handler themselves with the same identifier (`akiot.cloud_api`) and no `*Http*` wrapper: `AkNetwork::requestHttp`, `StationApiClient::request`, `ScheduleNetwork::_requestHttp`, the `AKIotEVChargeCommand` and AX170 command maps and a few direct `handle` calls. The list with the addresses is owned by [sdk_senders.md](sdk_senders.md#path-c-sender-list) | always; the decorator is not involved |

The three tests in `HttpEncryptionDecorator::request` (`@0x4868ff4`), in the order the code checks them (all `asm-traced`):

1. The SDK reports a logged-in state: `AkIotKitFlutter::isLogin` (`@0x48694f0`), compared with `true` (`@0x4869504`). This is the SDK's own state, which can already be true for a visitor session before any account login ([auth.md](auth.md#token-lifecycle)).
2. `needEncryption` is true. The parameter defaults to `true` (`@0x48691bc`); `false` jumps to the plain path (`tbnz` at `@0x4869510`).
3. The request URL passes a string predicate against `RequestApi::currentBaseUrl` (interface call `@0x4869544`; the selector is not named by Blutter). My reading: the URL must belong to the current API base URL, so calls with `useBaseUrl: false` (foreign hosts) would go the plain path; the exact predicate is a known unknown.

Before these tests (and independent of them), a call that needs a terminal id (`needTerminalId`, default `true`, `@0x486921c`) and has no account login first requests one ([terminal id](#terminal-id)).

Method mapping on the SDK path (`_handlerHttpBySdk`): the `Method` enum index is turned into the string `GET` for 0 (`cmp x2, #0`, `@0x4869974`, string `@0x486997c`), `DELETE` for 2 (`cmp x2, #2`, `@0x4869990`, string `@0x48699a0`) and `PUT` for 3 (boxed compare with raw 6, `cmp w0, #6`, `@0x48699b8`, tagged, so 3; string `@0x48699c0`); every other index, including 1 (`post`), falls to `POST` (`@0x48699d0`). The pool shows `get` as 0 (`pp+0x340e8`) and `post` as 1 (`pp+0xa7e0`); 2 as `delete` and 3 as `put` follow from this mapping and from the order of the pool map `Map<Method, String>` (get, post, delete, put, patch, head; `pp+0x48ad0`), which also suggests `patch` 4 and `head` 5 (not proven by a compare). Those two would be sent as `POST` on this path.

### How the wrappers reach the paths

Rows are `sender` rows of `data/endpoints.json` (610 of the 764 rows; the other 154 are URL-provider rows; for the command-map functions of `AKIotEVChargeCommand` and the AX170 command the sender is traced in the same function (38 cloud sends in `AKIotEVChargeCommand`, [sdk_senders.md](sdk_senders.md)), the flag just cannot say so). `encrypted: true` = the wrapper name contains `encryptionRequestHttp` (448 rows); "note" rows (162) call a plain `requestHttp`/`request` wrapper; `false` rows (154) are URL providers, for which the flag means "encryption not determined" (no `*Http*` call in the same function). Counts regenerated on 2026-10-19 after the inventory learned URL literals without a leading slash; before that the file had 709 rows (598 sender, 449 true, 149 note, 111 url_provider). The true count fell by one (449 to 448) because one row left the file, not because a flag flipped: the 3.18.0-only row `setRemainPluginStatus` (`charging/http/http_request_repository_impl.dart @0x3097764`, `encryptionRequestHttp`, URL `/power_service/v1/site/set_device_feature`) is no longer emitted, since 3.24.3 still holds that URL as the slashless literal `power_service/v1/site/set_device_feature` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x396035c`, a `url_provider` row).

| wrapper (callee name in the inventory) | next hop (asm-traced unless marked) | path | rows true / note |
|---|---|---|---|
| `HttpRequestControllerImpl::encryptionRequestHttp` (`http_request_repository_impl.dart @0x2264510`) | forwards all arguments, `needEncryption` default true (`@0x226451c`), to `HttpRequestControllerImpl::requestHttp` (`@0x2264924`) | A | 198 / 0 |
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
| `AkNetwork::requestHttp` | `AKIoTKitManagerImpl::handle` (addresses: [sdk_senders.md](sdk_senders.md#path-c-sender-list)) | C | 0 / 26 |
| `StationApiClient::request` | `AkIotKitFlutter::handle` (addresses: [sdk_senders.md](sdk_senders.md#path-c-sender-list)) | C | 0 / 5 |
| `ScheduleNetwork::_requestHttp` | `AKIoTKitManagerImpl::handle` (addresses: [sdk_senders.md](sdk_senders.md#path-c-sender-list)) | C | 0 / 5 |
| `AKIotEVChargeCommand` and AX170 command maps | `AKIoTKitManagerImpl::handle`, in the same function as the URL literal | C | 0 / 0 (url_provider rows, see below) |
| total | | | 448 / 162 |

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

1. If the sender is on path C (the list is in [sdk_senders.md](sdk_senders.md#path-c-sender-list); the 36 counted rows are the `AkNetwork`, `StationApiClient` and `ScheduleNetwork` rows): the SDK sends it, whatever the flag says. **36 rows** (all in the 162 "note" rows).
2. Else, if the sender passes `needEncryption: false` (table above): plain path, **3 rows** (`logOutRequest` is in the 448 "true" rows, `getRegionHostRequest` and `exchangeKey` in the 162 "note" rows).
3. Else (default `needEncryption: true`): the call takes the SDK path whenever the SDK is logged in (visitor sessions count) and the URL passes the base-URL predicate, otherwise the plain path. **571 rows** = 447 "true" rows + 124 "note" rows. Of them, 36 rows go through mixin stubs whose asm is not available (13 + 23); their target is inferred.

Check: 36 + 3 + 571 = 610 sender rows; the 154 `false` rows are URL-provider rows: the flag is not applicable to them, encryption is not determined by the flag (the command-map rows are path C, see [sdk_senders.md](sdk_senders.md#path-c-sender-list)); 79 of those rows, 75 distinct URLs, have no sender row at all).

The reading for a client author: for a logged-in app session almost every ordinary call (571 of 610 sender rows) is an SDK call. The server also accepts plain calls for the endpoints the upstream library uses: the library keeps payload encryption off by default (`session.py`, `self.encrypt_payload: bool = False`, upstream-confirmed) and has an experimental encrypted mode for the same endpoints. Which endpoints reject a plain call is not recorded in this repository.

## Request headers on encrypted calls

Each header with the derivation of its value. Dart builds this set in `EncryptionUtilImpl::commonHeaders` (`charging/aiot/EncryptionUtilImpl.dart @0x4016fbc`) and uses it for the key-exchange request (plain Dio path, merged with the ordinary identity headers of [auth.md](auth.md#common-request-headers)). Requests on the SDK path get their encryption headers natively; for those the names come from the upstream capture of an app request (`session.py` comment block, upstream-confirmed), and the derivations below are the Dart ones, which the SDK is expected to share (same names, same upstream sizes: a 32-hex-character nonce, key identifier and 64-hex-character signature; the sharing itself is not traced).

| header | value and derivation | Dart (`commonHeaders`) | upstream capture |
|---|---|---|---|
| `X-Encryption-Info` | the constant `algo_ecdh` | `@0x40170a8`, value `@0x40170b0` | `x-encryption-info: algo_ecdh` (upstream-confirmed) |
| `X-Replay-Info` | the constant `replay` | `@0x401702c`, value `@0x4017034` | `x-replay-info: replay` (upstream-confirmed) |
| `X-Request-Ts` | Unix time in whole seconds as decimal text: `getTimeStamp` ([Nonce and timestamp](#nonce-and-timestamp)); read once per request and reused for the signature | call `@0x4016ff0`, key `@0x401705c` | `x-request-ts` (10-digit seconds, upstream-confirmed) |
| `X-Request-Once` | per-request nonce: lowercase MD5 hex of `<epoch milliseconds>+<random double in [0,1)>`: `getRequestOnce` ([Nonce and timestamp](#nonce-and-timestamp)) | call `@0x4016ffc`, key `@0x4017084` | `x-request-once`, 32 hex characters (upstream-confirmed) |
| `X-Key-Ident` | identifier of the negotiated key: the `currentIdentifyKey` text from `SharedPreferences`; if none is stored it is created on first read as one more `getRequestOnce` value and stored ([Session key and key identifier](#session-key-and-key-identifier)) | `getIdentifyKey` call `@0x40170dc`, key `@0x40170f8` | `x-key-ident`, 32 hex characters (upstream-confirmed) |
| `X-Signature` | lowercase hex of `hMacEncrypt(key, "<ts>+<once>+<body text>")` with `key` = `getAesKey()` for the key exchange (as traced; the SDK path for ordinary calls is not traced) ([Request signing](#request-signing)) | `getAesKey` call `@0x4017110`, `getSignature` call `@0x4017128`, key `@0x4017150` | `x-signature`, 64 hex characters (upstream-confirmed) |
| `X-App-Key` | the empty string | `@0x40171cc`, value `@0x40171d4` | `x-app-key: ` (upstream-confirmed) |
| `App-name` | the constant `anker_power` | `@0x40171a0`, value `@0x40171a8` | `app-name: anker_power` (upstream-confirmed) |
| `Content-Type` | `application/json` in the Dart key-exchange request | `@0x4017174`, value `@0x401717c` | `text/plain` on encrypted API calls (the body is base64 text), `application/json` on the key exchange (upstream-confirmed) |
| `X-Auth-TS` | not in `commonHeaders`. On the plain path `_headerToken` adds the current time in seconds when there is no `gtoken` ([auth.md](auth.md#common-request-headers)); the upstream key-exchange request always sends it, with the same value it embeds in its client key | n/a | `x-auth-ts` (upstream-confirmed) |

The ordinary identity headers (`X-Auth-Token`, `gtoken`, `App-Version`, `Language`, `Timezone`, `Country`, ...) are on [auth.md](auth.md#common-request-headers). Header names are case-insensitive on the wire. The body of an encrypted call is one base64 text (next sections); the answer is JSON with `signature`, `msg`, `code`, `trace_id` and an encrypted text in `data` (upstream capture).

## Key-exchange endpoint

`POST /openapi/oauth/key/exchange` with the body key `client_public_key`; the answer carries `server_public_key`. The page [openapi/oauth/key/exchange.md](openapi/oauth/key/exchange.md) owns the body, the skip rule, the callers and the response handling; this section owns how the values are built. The exchange is sent with `needEncryption: false` (plain Dio path), because no session key exists yet (`exchangeKey`, `EncryptionUtilImpl.dart @0x4016d54`, descriptor `@0x4016f84`). Tag: asm-traced unless marked.

Request side, in the order `exchangeKey` runs (all calls through the `encryption` channel):

1. Skip if both `currentAesKey` and `currentIdentifyKey` are stored (`@0x4016dac` to `@0x4016dd4`); otherwise remove both (`@0x4016de8`, `@0x4016df4`).
2. `Encryption::getClientPublicKey` (`@0x4016e14`, channel method `getClientPublicKey`, `encryption_method_channel.dart @0x2faf454`): Dart receives a String. By the method name the native side presumably creates the client key pair and keeps the private key (inferred, not shown in Dart). Its exact text format is native and not visible in Dart. (`clearClientKeyPairs`, `@0x3bd75ac`, discards the pair; only the login screen calls it.)
3. `Encryption::aesCbcEncrypt(key = getPresetKey(), data = <client public key text>)` (`@0x4016e40`, `@0x4016e50`; channel map `data`, `key`, `@0x401772c` to `@0x401774c`). The result is a byte list; Dart base64-encodes it (`Base64Codec.encode`, `@0x4016e68`) and stores that text as `client_public_key` (key string `@0x4016e88`). So the client public key never travels in the clear: it travels encrypted under the app-embedded preset key. This differs from the upstream experimental handler, which sends the key in clear form (`AnkerEncryptionHandler._generate_client_key`, a 16-byte timestamp, a marker byte and the uncompressed point, base64; its class docstring says the encrypted mode "does not work yet").
4. `commonHeaders(<the base64 client_public_key text>)` (`@0x4016ea4`) builds the header map ([headers table](#request-headers-on-encrypted-calls)). The text passed in is the third component of the signature, so the exchange request is signed over exactly the `client_public_key` string it sends. `getAesKey` returns the preset key here, because the stored key was removed in step 1 ([Session key and key identifier](#session-key-and-key-identifier)).
5. `exchangeKey` reads the `X-Key-Ident` entry of that map (`@0x4016ec8`, default empty string `@0x4016ee4`) and keeps it in the closure context for step 8; the request goes out through `HttpBusinessImpl::requestHttp` (`@0x4016f8c`).

Response side, `EncryptionUtilImpl::parse(keyIdent, response)` (`@0x4017978`, called from the success closure `@0x401788c` at `@0x4017958`):

6. Read `server_public_key` from the response `data` map (`@0x40179c0`; upstream-confirmed name). The response `signature` field is checked in `_handler200` before the closure runs ([Request signing](#request-signing)).
7. `Encryption::aesCbcDecrypt(data = <server_public_key text>, key = getPresetKey())` (`@0x4017a1c`, `@0x4017a2c`; channel map `@0x4017d74` to `@0x4017d8c`), then the byte list is UTF-8 decoded with `allowMalformed: true` (`Utf8Codec::decode`, `@0x4017a50`). So the server public key is also encrypted under the preset key on the wire, and the decrypted value is text.
8. `Encryption::getExchangedAesKey(key = <that text>)` (`@0x4017a64`; channel method name loaded at `@0x4017c8c`, wrapper `@0x4017c28`, map key `key`) returns the session key as a String. Dart stores it with `SpUtilImpl::saveAesKey` (`@0x4017a94`, preference `currentAesKey`) and stores the key identifier from step 5 with `saveIdentifyKey` (`@0x4017aa4`, preference `currentIdentifyKey`).

ECDH and curve: the shared-secret computation and the key derivation behind `getExchangedAesKey` are presumably native inside the `encryption` channel (inferred). The only value Dart passes to `getExchangedAesKey` is the decrypted server text under the map key `key`; no shared secret or private key is passed in Dart. That the native side performs ECDH with the key pair of `getClientPublicKey` and derives the session key is inferred from the method names, not shown in Dart. The curve is NIST P-256 (secp256r1) for the library's login ECDH (`session.py`, `ec.SECP256R1()`, server key as an uncompressed point; upstream-confirmed) and for its experimental key-exchange handler (`AnkerEncryptionHandler`, `ec.SECP256R1()`); that the native cloud key exchange uses the same curve is an inference from those two, not a trace. `Encryption::computeEcdhWithPublicKey` (`@0x484b850`) exists but is called only by the BLE conferrers (`ecdh_confer.dart @0x484b120`, `secure_ecdh_confer.dart @0x484cc48`), not by the cloud path. Which hash, salt and info the native derivation uses is a known unknown; the upstream experimental handler tries HKDF-SHA256 with `info = b"ecdh handshake"` and no salt (`derive_shared_key`), an unconfirmed hypothesis (its docstring marks the whole class as not working).

The key identifier is not derived from the key: it is a client-generated random-looking value (next section), which the server associates with the derived key.

## Session key and key identifier

Tag: asm-traced unless marked.

- **Which key is in use.** `EncryptionUtilImpl::getAesKey` (`@0x401741c`) returns the stored `currentAesKey` (`SpUtilImpl::getAeskey`, `sp_util_impl.dart @0x2dbb5c8`) when it is not empty, otherwise `getPresetKey()` (`@0x4017464`). So the preset key is the HMAC key of the key-exchange request, and the exchanged session key is the HMAC key of every later request. The same function is used when the app checks a response signature (`HttpRequestManager::validateSignature`, `charging/util/manager/http_manager.dart @0x486cb88`).
- **Preset key (`getPresetKey`, `@0x2dbb554`).** Role: an app-embedded constant that is the shared secret of the first leg of the exchange: it encrypts the client public key, decrypts the server public key and keys the HMAC of the exchange request. It is a 32-character hex string and the function returns one of two values by the server environment (`serverEnv`, static field `0x1bb4`): the pool string at `pp+0x35b70` for the Env instance `mp` (index 2 as printed in the pool dump, `pp+0x8420`, compare `@0x2dbb590`), and the pool string at `pp+0x35b78` for every other environment (`@0x2dbb5ac`). `getServerEnv` (`charging/main_env.dart @0x4a3d188`) returns that `mp` instance unconditionally, so a normal build uses the first one. The same static field (offset 0x1bb4) is the `serverEnv` that `MqttServe._getDemoSiteConfig` compares to pick the MQTT broker and certificate set ([mqtt/envelope.md](../mqtt/envelope.md#which-certificate-set-and-broker-host-the-app-picks-new-read-2026-10-20)); this is the one place that states which value a normal build holds. A library reads the current value from its own copy of the APK at that pool offset; it is not written on this page. The app passes the same value to the native SDK as the `presetKey` entry of its login map (`getSDKLoginParams`, `charging/impl/device_serviceImpl.dart @0x481dd50`; `AkIotKitFlutter::loginAnkerCloud`, [auth.md](auth.md#token-lifecycle)), so the SDK holds it too.
- **How the preset key is handed to the primitives.** As a String, in the `key` slot of `aesCbcEncrypt`, `aesCbcDecrypt` and `hMacEncrypt`. Whether the native side uses the 32 characters as 32 text bytes (AES-256) or hex-decodes them to 16 bytes (AES-128) is not visible in Dart (known unknown).
- **Session key.** The String returned by `getExchangedAesKey`, saved as `currentAesKey` (preference key at `sp_util_impl.dart @0x4017ba0`). Its format (hex, base64, raw) and size are native; it is used as the `key` String of `hMacEncrypt` and, by inference, of the payload cipher. How it is derived from the ECDH secret is native (see [Key-exchange endpoint](#key-exchange-endpoint)); `getAesKey` is the only name in Dart that mentions "AES key" for it, and the Dart side does no HKDF for it. The only Dart-visible `HKDF` call belongs to the unrelated [local-info key](#local-info-key-not-part-of-the-wire-protocol).
- **Key identifier.** `SpUtilImpl::getIdentifyKey` (`@0x40177b0`) reads the preference `currentIdentifyKey` (`@0x4017800`, `@0x4017818`); if the preference does not exist it calls `getRequestOnce()` (`@0x401784c`), stores the result as `currentIdentifyKey` (`setString`, `@0x4017864`) and returns it. After `removeIdentifyKey` (`@0x273c86c`) the next `commonHeaders` call therefore creates a fresh identifier, which the exchange request carries in `X-Key-Ident` and `parse` stores again (`saveIdentifyKey`, `@0x4017ac4`). It is a client-chosen handle, not a hash of the key.
- **Lifetime.** Both preferences are removed by `SpUtilImpl::clearEncryptionInfo` (`@0x273c814`, on logout and region switch). There is no timer or refresh in Dart; the 463 handling is on [Response handling and error codes](#response-handling-and-error-codes).

## Request signing

`EncryptionUtilImpl::getSignature(body, key, once, ts)` (`@0x4017200`). Tag: asm-traced for the input string and the primitive's name and argument order; the algorithm behind the name is native.

Input string, byte for byte as Dart builds it with two string interpolations, each over a 3-element array (`AllocateArray` with raw length 6 at `@0x4017254` and `@0x4017284`, tagged, so 3 elements by the Smi rule): first `ts + "+" + once` (`@0x4017260` to `@0x40172a8`, interpolation `@0x401727c`), then `<that> + "+" + body` (interpolation `@0x40172b0`). The separator is the pool string `"+"` (`pp+0x3210`, `@0x4017268` and `@0x401729c`). So:

```
signature_input = ts + "+" + once + "+" + body_text
```

- `ts`: the `X-Request-Ts` value, decimal seconds text.
- `once`: the `X-Request-Once` value, 32 hex characters.
- `body_text`: for the key-exchange request, the exact `client_public_key` base64 string (`@0x4016ea4`, argument of `commonHeaders`, `@0x4017128`). For ordinary encrypted calls the SDK signs natively; by analogy with the exchange the signed text is the body text as sent (the base64 of IV plus ciphertext), but that is an inference. No separator or newline other than `+` appears, and nothing else (method, path, headers, key identifier) enters the input in the Dart implementation. The upstream experimental handler signs a different string (`ts`, `once`, key identifier and `json.dumps(data)` concatenated without separators, plain SHA-256); it is marked as not working and does not match the app.

Primitive: `Encryption::hMacEncrypt(key, data)` (`encryption.dart @0x40172ec`, channel method `hMacEncrypt`, `encryption_method_channel.dart @0x401735c`, map `data` then `key`, `@0x401739c` to `@0x40173bc`), called at `@0x40172c8` with `key = getAesKey()` and `data = signature_input` as Strings. It returns a byte list; `CmdUtil::bytesToHexString` (`cmd_util.dart @0x21d4e88`, called at `@0x40172dc`) turns it into the header text: each byte as radix-16 text, a leading `0` added when the text is shorter than 2 characters (`cmp x2, #2` at `@0x21d4f74`), so two lowercase hex characters per byte. The hash inside "hMac" is native. The upstream capture shows a 64-hex-character signature (upstream-confirmed), which is 32 bytes and consistent with HMAC-SHA-256; that is the length-based reading, not a traced algorithm name. 3.18.0 builds the signature identically (same two interpolations with `"+"` at `pp+0x2ca0` and `hMacEncrypt`, `EncryptionUtilImpl.dart` 3.18.0 `@0x1b938e8`, `@0x1b9391c`, `@0x1b93948`).

Response signature (Dart side): `_handler200` (`HttpEncryptionDecorator.dart @0x486c680`) calls `HttpRequestManager::validateSignature(headers, result)` (`@0x486c75c`) only when the body `code` is 0 and the parsed `Result` carries a `signature` field (`@0x486c708`, null check `@0x486c718`; `Result` fields `code`, `msg`, `data`, `signature`, `charging/model/result.dart`). `validateSignature` (`http_manager.dart @0x486c99c`) reads `X-Request-Ts` (`@0x486ca0c`) and `X-Request-Once` (`@0x486ca44`) from the header map it is given, takes `data["server_public_key"]` as the text (`@0x486cad4`, empty string if absent), recomputes `getSignature(text, getAesKey(), once, ts)` (`@0x486cb88`, `@0x486cba0`) and compares it with the received `signature` (`@0x486cbc4`). So for the key-exchange response the signature is the same HMAC over `ts + "+" + once + "+" + <server_public_key text as received, still encrypted>`, keyed with `getAesKey()` at that moment, which is still the preset key. A mismatch yields code 463 ([Response handling and error codes](#response-handling-and-error-codes)). Which header map is passed in (the request headers the app sent, which matches the use of its own `ts` and `once`, or the response headers) is not decoded. For ordinary SDK responses the check happens natively.

## Nonce and timestamp

Tag: asm-traced.

- **Timestamp** (`getTimeStamp`, `@0x40175dc`): `DateTime` from `_getCurrentMicros` (`@0x4017608`), `toUtc` (`@0x4017624`), then two integer divisions by 1000 (microseconds to milliseconds to seconds, `sdiv` at `@0x4017644` and `@0x4017648`, divisor `mov x0, #0x3e8` at `@0x401763c`, an unboxed value so raw is real), interpolated as decimal text (`_interpolateSingle`, `@0x4017664`). The sign test at `@0x401762c` with `999` at `@0x4017630` is Dart's floor-division adjustment for negative values and never applies to current times. Result: Unix seconds, for example 10 digits. App side: the app maps HTTP status 461 to a device-time hint ([Response handling and error codes](#response-handling-and-error-codes)). Whether the server rejects a request for a timestamp far from its clock, and with what tolerance, is not known here; the tolerance is not in the app.
- **Nonce** (`getRequestOnce`, `@0x4017488`): the same `_getCurrentMicros` and `toUtc`, one division by 1000 (`@0x40174e8`, `@0x40174ec`, `@0x40174f0`) giving epoch milliseconds, then the interpolation `"<ms>" + "+" + "<Random().nextDouble()>"` (array of 3 elements, `@0x4017524` to `@0x4017580`; `Random()` at `@0x40174fc`, `nextDouble` at `@0x401754c`; the double is printed in Dart's default shortest form), and finally `StringUtil::md5Str` (`@0x40175b4`; `string_util.dart @0x3ea1c2c` is UTF-8 encode, MD5, `Digest.toString`, which is lowercase hex). The result is 32 lowercase hex characters. The server cannot verify the randomness; it is a replay-protection value, so a library may generate any fresh 32-hex value, but using the app's construction is the safest match. How the server stores used values (window length) is not in the app.
- **Roles.** `X-Request-Ts` and `X-Request-Once` are sent as headers and are the first two components of the signature input; together with the `X-Replay-Info: replay` marker they let the server reject a repeated or stale request. The same `getRequestOnce` function also creates the key identifier ([Session key and key identifier](#session-key-and-key-identifier)).

## Payload encryption and response decryption

What Dart shows and what it does not. Tag: asm-traced for the first two points; upstream-confirmed (capture) for the wire shape.

- On the cloud request path Dart never encrypts or decrypts an API body. The plain path (`HttpRequestImpl::request`) sends JSON and ignores `needEncryption` ([Which calls are encrypted](#which-calls-are-encrypted)); the SDK path hands the SDK the `path`, `method`, `param` (the request data as a map) and `header` map and returns an already decrypted `data` ([Response handling and error codes](#response-handling-and-error-codes)). The cipher of the SDK is native.
- The only Dart-visible uses of the `encryption` channel cipher calls on the cloud path are the two in the key exchange (client key encrypted, server key decrypted, both with the preset key).
- Wire shape of an encrypted call (the upstream capture of an app request, `session.py` comment block, upstream-confirmed; the decoding that follows is mine, from that one sample): `POST` with `content-type: text/plain` and the body being one base64 text; the response is JSON whose `data` is a base64 text and which carries a `signature`. Decoding the captured request body shows 80 bytes: the first 16 bytes are ASCII digits, a 13-digit millisecond time followed by `000`, whose leading 10 digits equal the captured `x-request-ts`; the remaining 64 bytes are a whole number of AES blocks. The captured response `data` also decodes to 80 bytes with a non-textual first 16 bytes. This fits `base64( IV(16 bytes) || AES-CBC ciphertext )`, with the IV for a request being a 16-character text derived from the current time. The upstream experimental decryptor assumes exactly this layout, splitting the first 16 bytes as IV, AES-CBC with the session key, PKCS#7 unpadding (`AnkerEncryptionHandler.decryptApiData`; marked as not working because key and headers were not known). The same layout fits the key-exchange blob: upstream reads its first 16 bytes as a timestamp (`_generate_client_key`), which is what an IV of this kind looks like. The reading is one captured sample, not a device test.
- AES-CBC itself is named by the channel method `aesCbcEncrypt` / `aesCbcDecrypt` and by upstream; the padding and the IV generation rule are native (known unknown). The login password path of the library, which works against real accounts, uses AES-256-CBC with PKCS#7 padding and the first 16 bytes of the key as IV (`session.py` `_encryptApiData`, upstream-confirmed), but that is the login ECDH path (`loginPasswordECDH`), not this one.
- JSON body: the plaintext is the same JSON object the plain path would send; the upstream capture is of `get_device_attrs`. Whether the SDK serializes it with particular spacing is not known.

## Local-info key (not part of the wire protocol)

`getLocalInfoAeskey` / `newLocalInfoAesKey` do not belong to the request protocol and do not use the preset key. They protect locally stored user information (`SpUtilImpl` readers and writers call `encryptLocalInfo` and `decryptLocalInfo`, for example `sp_util_impl.dart @0x21d466c`, `@0x273b3d4`). Tag: asm-traced.

- `newLocalInfoAesKey` (`EncryptionUtilImpl.dart @0x49dde44`) generates a per-install key: `ts = getTimeStamp()` (`@0x49dde70`), `info = md5Str(ts)` (`@0x49dde7c`), then the channel call `HKDF(data = ts, info = info)` (`Encryption::HKDF`, `@0x49dde94`; channel map keys `data` and `info`, `encryption_method_channel.dart @0x49de04c`, `@0x49de05c`). The byte list is turned into hex text (`@0x49ddea8`) and stored in the platform keychain (`FlutterKeychain::put`, `@0x49ddee8`). Hash, salt and length of the HKDF are native.
- `getLocalInfoAeskey` (`@0x49de0d0`) reads that value from the keychain (`FlutterKeychain::get`, `@0x49de0f8`); if it is missing it removes the stored user info (`removeIotUserInfo`, `@0x49de128`) and generates a new key. At startup `injection_init.dart @0x49dd8f0` or `@0x49dd920` puts the result into the static field `0x2044`, which `encryptLocalInfo` (`@0x273b7d4`) and `decryptLocalInfo` (`@0x21d4938`) read and slice into key and IV bytes for `AesHelper::aesCbcEncrypt` / `aesCbcDecrypt` (`charging/ble_zx/helper/aes_helper.dart @0x273b8b4`, `@0x21d4a3c`), which use the Dart `encrypt` package with AES mode `cbc` (pool `pp+0xe5c8`, name `cbc`) and require a 16-byte IV (`cmp w0, #0x20` on a tagged length, `@0x2274adc`, so 16; error text `Initialization vector must be 16 bytes long`). Unlike the preset key, this key is not an embedded constant: there is no 32-hex literal in `getLocalInfoAeskey`. The slicing arguments (`@0x273b824` to `@0x273b868`) did not reconcile with the 16-byte check and are left in Known unknowns.

## For library implementers

Minimal sequence to produce a valid encrypted request for one's own account, as far as the app code determines it. It reuses the library's existing ECDH code in `session.py` (`self._private_key = ec.generate_private_key(ec.SECP256R1())`, `_shared_key`, `_encryptApiData`, upstream-confirmed) as the starting point for the key pair and the AES-CBC helper, and `AnkerEncryptionHandler` in the same file as the skeleton for the exchange request. Field-level pseudocode; steps tagged T are traced in the app (only the exchange-path inputs and orders), N depend on a native primitive, `capture` comes from the single upstream capture, and `inferred` is extrapolated; everything but T must be validated against the server.

```
0. login as today (auth_token, gtoken, geo_key); nothing here changes the login.        [T]
1. preset = <32-hex value read from your own copy of the APK, pool offset pp+0x35b70>   [T, location only]
2. key_ident = md5hex(str(now_ms) + "+" + str(random.random()))      # any fresh 32-hex value
   once     = md5hex(str(now_ms) + "+" + str(random.random()))
   ts       = str(int(time.time()))                                                     [T]
3. client_key_text = text form of your own P-256 public key                              [N: format of
                                                                                          getClientPublicKey]
   client_public_key = b64( [IV16 ||] AES_CBC(key=preset, data=client_key_text) )       [T: encrypt+base64 order; IV16 prefix = [capture/upstream], N cipher]
   sig = hex( HMAC(key=preset, ts + "+" + once + "+" + client_public_key) )              [T input @0x4017200, N hash]
   POST /openapi/oauth/key/exchange, JSON {"client_public_key": client_public_key},
   headers: X-Encryption-Info: algo_ecdh, X-Replay-Info: replay, X-Request-Ts: ts,
            X-Request-Once: once, X-Key-Ident: key_ident, X-Signature: sig,
            X-App-Key: "", App-name: anker_power + the ordinary identity headers         [T]
4. server_text = utf8( AES_CBC_decrypt(key=preset, data=b64decode(data.server_public_key)) )   [T: decrypt+UTF-8 order; IV16 prefix [inferred], N cipher]
   session_key = derive(ECDH(your_private_key, server_text))                              [N, inferred from method names]
   store session_key and key_ident together                                              [T]
5. every later call: ts, once fresh;
   body  = b64( IV16 || AES_CBC(key=session_key, data=json_text) )   [IV16 layout: capture, one sample; AES-CBC under the session key: inferred, SDK path not traced]
   sig   = hex( HMAC(key=session_key, ts + "+" + once + "+" + body) )                     [inferred by analogy with the exchange; SDK, not traced]
   headers as in step 3 with X-Key-Ident = key_ident, X-Signature = sig,
   Content-Type: text/plain, body as raw text                                             [capture]
6. [inferred; extrapolated from the traced exchange-response check] response: JSON; check signature = hex(HMAC(session_key, ts + "+" + once + "+" + data)) (the app does this for the exchange response with
   data = server_public_key); then b64decode(data), IV = first 16 bytes, AES-CBC decrypt.
   HTTP 461 = clock skew, 463 or a bad response signature = renegotiate the key.
```

What is still open before this is a working client (none of it is `device-tested`): the text format `getClientPublicKey` returns, the session-key derivation behind `getExchangedAesKey`, the HMAC hash, how the 32-hex preset string and the session key are turned into cipher key bytes, the padding and the IV rule. Each is a candidate to test against the server with the library's experimental mode; the candidates in upstream's `AnkerEncryptionHandler` (HKDF-SHA256 with `info = b"ecdh handshake"`, PKCS#7, IV as the first 16 bytes) are consistent with the capture but were not confirmed by upstream either.

## Terminal id

`POST {base URL}/passport/terminal_id` owned by [passport/terminal_id.md](passport/terminal_id.md). It is requested by `HttpEncryptionDecorator::request` (`@0x4869310`) for any call with `needTerminalId` (default true) while no account is logged in, once (an `HttpEncryptionDecorator` lock serializes callers, a stored id is reused). It is not in `commonHeaders` (Dart); whether the native SDK includes it in its headers is unknown. The app sends it as `Openudid` on the calls listed on that page, as `X-Terminal-ID` on the plain path when there is no `gtoken`, and to the SDK as `terminalId`.

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

What the app does per code: 461 and 463 are reported to the caller as failures (461 with a hint that the device time may be wrong). 463 also stands for a failed response signature check in `_handler200`, after which the log says the key must be renegotiated; no automatic `exchangeKey` call follows in that function (the only `exchangeKey` caller is the privacy-policy page). 401 (as HTTP status with body code 401 or 26085) and the SDK codes 401/26085 lead to a forced logout with scene `tokenExpired`; 26084 leads to scene `kickedOut` (`_handler401 @0x486b2bc`, [auth.md](auth.md#token-lifecycle)). `_getErrorMsg` (`@0x486bd64`) maps SDK-side error values to three localization keys, `netWorkError`, `requestTimeout` and `errorOccur`; the numeric tests compare against large negative constants that were not decoded (Known unknowns). Login-screen codes (26108, 26105, 100053, ...) are on [passport/login.md](passport/login.md#errors-seen). The catalog (catalog: [api/errors.md](errors.md); upstream maps 401/403 to `AuthorizationError`, 26084 to `TokenKickedOutError` and others in `api/errors.py` (upstream-confirmed).

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

Added rows for the construction (function names, file `@0xADDR`):

| area | file | functions |
|---|---|---|
| key store | `charging/util/save/sp_util_impl.dart` | `getAeskey` (`@0x2dbb5c8`), `saveAesKey` (`@0x4017b44`), `removeAesKey` (`@0x273c8e0`), `getIdentifyKey` (`@0x40177b0`), `saveIdentifyKey` (`@0x4017ac4`), `removeIdentifyKey` (`@0x273c86c`), `clearEncryptionInfo` (`@0x273c814`); preference names `currentAesKey`, `currentIdentifyKey` |
| response signature check | `charging/util/manager/http_manager.dart` | `HttpRequestManager::validateSignature` (`@0x486c99c`) |
| response model | `charging/model/result.dart` | `Result.fromJson` (`@0x2fb02a4`): `code`, `msg`, `data`, `signature` |
| string helpers | `charging/util/string_util.dart`, `charging/util/cmd_util.dart` | `StringUtil::md5Str` (`@0x3ea1c2c`), `CmdUtil::bytesToHexString` (`@0x21d4e88`), `CmdUtil::hexStringToBytes` (`@0x22014a4`) |

What stays in Dart and what is forwarded: Dart picks the path, builds the request map, assembles the key-exchange header map (timestamp, nonce, constants, key identifier from storage), builds the signature input string, decides which key is used (stored session key or the preset key), and stores the results (`SpUtilImpl` keys). Every cryptographic primitive is a platform channel call (`encryption` channel, pool entry `pp+0x36800`, name `encryption`): `getClientPublicKey`, `aesCbcEncrypt`, `aesCbcDecrypt`, `getExchangedAesKey`, `hMacEncrypt`, `HKDF`, `loginPasswordECDH`, `computeEcdhWithPublicKey`, `clearClientKeyPairs`. The SDK path forwards the entire request, including header building, signing, encryption and decryption, to the native SDK (channel `ak_iot_kit_flutter`, pool entry `pp+0xc468`). A native library named `libecc-encryption.so` ships in the 3.24.3 APK (`arm64-v8a`); that it backs the `encryption` channel is plausible but was not traced (no native analysis).

## Scope note

What this page covers: the construction visible in Dart (string inputs, their order and separators, which function stores what, which primitive receives which argument) and the wire facts of the upstream capture. What it does not cover: the inside of the native primitives (listed in [Known unknowns](#known-unknowns)), the account login and its password encryption ([auth.md](auth.md#password-encryption-at-login)), and the visitor token. The app-embedded preset key (`getPresetKey`, [Session key and key identifier](#session-key-and-key-identifier)) is given by role and by its pool offsets only; a library reads the current value from its own copy of the APK at that offset. The upstream library (thomluther/anker-solix-api, `session.py`, `AnkerEncryptionHandler`) is public; where this page differs from its experimental handler, the difference is stated in the section concerned.

## Changed since 3.18.0

Compared with the 3.18.0 asm: the decorator layout, `needEncryption` default (`true`), the path decision, `EncryptionUtilImpl` (same function names, `exchangeKey` with `needEncryption: false` at 3.18.0 `@0x311a47c`, header names `X-Replay-Info`, `X-Encryption-Info`, `X-Key-Ident`, `X-Request-Once`, `X-Request-Ts`, `X-Signature`), the `terminal_id` step and the 401/463 handling are all present in 3.18.0. The construction is unchanged too: in 3.18.0 `getSignature` builds the same two interpolations with `"+"` and calls `hMacEncrypt` (`@0x1b938e8`, `@0x1b9391c`, `@0x1b93948`), `getRequestOnce` has the same shape (one division by 1000, `Random.nextDouble`, `md5Str`, `@0x311a748` to `@0x311a80c`), `exchangeKey` encrypts the client key with `getPresetKey` (`@0x311a338`, `@0x311a348`) and `parse` decrypts the server key with it, calls `getExchangedAesKey` and saves key and identifier (`@0x311ac60` to `@0x311ace8`), and `getAesKey` falls back to `getPresetKey` (`@0x1b93bc8`). New in 3.24.3: the 461 branch of `handleStatusCode` and its message key `mismatchTimeAndNetworkCheck`, the function `_handleSdkError`, a Dio observability interceptor (`NetworkObservabilityInterceptor`) and net-performance logging on the SDK path (`logNetPerf`, `@0x486ae74`; `logNetPerf` is absent from the 3.18.0 pool and asm, present in `charging/ume/network_monitor/` in 3.24.3), and more direct SDK callers (`akiot.cloud_api` in 19 Dart files against 6). No header name or endpoint of the encrypted path changed. Whether the preset key value itself changed between the versions was not compared.

## Known unknowns

- How the native SDK builds its encrypted requests and which headers it adds (only the upstream capture is known); in particular which text it signs for ordinary calls (the exchange signs the `client_public_key` string; the same rule for ordinary bodies is an analogy).
- The format of the text `getClientPublicKey` returns, and what `getExchangedAesKey` does with the decrypted server text: curve (P-256 is inferred from upstream), KDF (hash, salt, info, length) and the format of the returned session key. The Dart side has no HKDF for it.
- Which hash `hMacEncrypt` uses (a 64-hex-character result suggests SHA-256 but the name is not in Dart) and how the String keys (preset key, session key) are turned into bytes (text or hex-decoded). — reclassified: device test row 152 (traced 2026-10-20: Dart only calls the platform channel method `hMacEncrypt` with two strings (pool `pp+0x36800`); the hash and the key-to-bytes step run in native code, which has no Blutter asm)
- The AES-CBC details of the `encryption` channel: key size, padding, and the IV rule (the capture suggests an IV prefix of 16 bytes holding a millisecond time as ASCII digits for requests; one sample).
- Which header map `validateSignature` receives (`_handler200` argument) and whether the SDK validates ordinary response signatures the same way. — traced 2026-10-20: `_handler200` calls `validateSignature` (`HttpEncryptionDecorator.dart @0x486c75c`) with its first argument, replaced by an empty `<String, dynamic>` map when null (`@0x486c730`..`@0x486c748`), and the response model (`@0x486c758`); the SDK-callback closure `(dynamic, int?, Result?)` calls `_handler200` with five stack arguments (`@0x486c5d0`..`@0x486c5e0`), the first of them stored as `NULL`, so which of the two header sources feeds the call was not decided and whether the SDK validates ordinary responses stays open
- Server tolerances: clock window for `X-Request-Ts`, how long a `X-Request-Once` is remembered, and whether the key identifier or key expires server side.
- Whether the preset key value differs between app versions or between the two server environments in practice, and whether the native SDK holds the same value as `getPresetKey` (it is handed the `presetKey` map entry, so very likely).
- The byte slicing of the local-info key (`sublist` arguments raw 32/0 and 64/16 at `EncryptionUtilImpl.dart @0x273b824` to `@0x273b868`, same at `@0x21d4988` to `@0x21d49cc`): read with the Smi rule they give ranges 0..16 and 8..32 that do not match the 16-byte IV check in `AesHelper` (`@0x2274adc`); not resolved. It is not part of the wire protocol. — traced 2026-10-20: re-read at `charging/aiot/EncryptionUtilImpl.dart @0x273b824`..`@0x273b870`: the first call passes raw 0 and raw 32, the second raw 16 and raw 64, through a dynamic `GDT[cid_x0 + 0x3b69f]` call whose selector Blutter does not name, and the two results go to `aesCbcEncrypt` as its second and third argument (`@0x273b89c`); under the Smi rule the ranges are 0..16 and 8..32, read as unboxed 0..32 and 16..64, and neither pair gives the 16-byte IV that `AesHelper` demands, so the tagging of the arguments cannot be decided from the asm
- Which endpoints the server rejects when sent plain; the inventory cannot tell.
- The 36 rows behind mixin stubs (`HttpRequestMixin` applications) are inferred to follow path A; their asm is not emitted by Blutter. — traced 2026-10-20: the class `HttpRequestMixin` is empty in the asm (`charging/http/http_request_mixin.dart` holds only `Debouncer::run` `@0x230f7f0` and the class header), and its named arguments (`cacheKey`, `loopSeconds`, `debounceMills`, `isLogResponse`, `showDefaultError`) occur in no emitted function body, so the stub bodies cannot be read and the rows stay inferred
- The selector of the URL predicate in `request` (`@0x4869544`) and the exact meaning of its result for relative paths. — traced 2026-10-20: the same dynamic call `GDT[cid_x0 + -0x1000]` with one String argument is used in `Api.init` to test the package name against `"anker.pros"` (`base_service/api_url.dart @0x49ce9cc`) and in `HttpEncryptionDecorator::successCallback` with `currentBaseUrl()` (`charging/http/HttpEncryptionDecorator.dart @0x486c1e0`); Blutter does not name the selector, and the dispatch-table file needed to resolve it is not part of the dump
- The thresholds of `_getErrorMsg` are decoded on [errors.md](errors.md#user-visible-message) (the three client sentinels and their message keys, traced 2026-10-20); the producers of the sentinels are not traced there.
- Whether an SDK request also needs the visitor/terminal id to be present, and what the SDK does on 461 or 463 beyond reporting them.
- Whether the native SDK includes the terminal id in its request headers (the Dart `commonHeaders` does not). — reclassified: device test row 152 (traced 2026-10-20: the headers of SDK calls are added natively, `AkIotKitFlutter::handle` passes only `path`, `method`, `param` and `header` (`ak_iot_kit_flutter/src/ak_iot_kit_flutter.dart @0x21c3d8c`))
- Whether `libecc-encryption.so` implements the `encryption` channel (no native analysis). — reclassified: device test row 152 (traced 2026-10-20: the Dart side only names the channel `encryption`; the native library is outside the Blutter asm)

## Device-tested by

Upstream library (thomluther/anker-solix-api): key exchange and an encrypted `get_device_attrs`-style request against the EU server work in its experimental encrypted mode; plain requests work in the default mode (`upstream-confirmed`). No named client version, device PN, firmware or date is recorded here, so nothing is `device-tested`.
