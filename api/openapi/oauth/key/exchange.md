> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# exchange

## Purpose

Starts the session-key negotiation for encrypted requests: the app posts its client public key material and the server answers with its own public key, from which the app derives and stores the session key and its identifier.

## Upstream name

`API_KEY_EXCHANGE` (module constant of `api/apitypes.py`, value `openapi/oauth/key/exchange`; not an `API_ENDPOINTS` key). Upstream-confirmed: `AnkerEncryptionHandler.perform_key_exchange` in `session.py` posts `{"client_public_key": ...}` to this URL and reads `data.server_public_key` from the answer.

## Method+URL

`POST /openapi/oauth/key/exchange` (asm-traced): URL string `pp+0xc3d70` at `charging/aiot/EncryptionUtilImpl.dart @0x4016f58`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x4016f50`, in `EncryptionUtilImpl::exchangeKey` (`@0x4016d54`). The call goes through `HttpBusinessImpl::requestHttp` (`@0x4016f8c`, the `HttpBusiness` static field is loaded at `@0x4016f0c`).

## Encrypted?

No (asm-traced): the call passes `needEncryption: false` (and `needTerminal: true`; `r16 = false` at `@0x4016f78`, `r30 = true` at `@0x4016f70`, descriptor `@0x4016f84`), as it must, because no session key exists yet. The decorator therefore sends it over the plain Dio path, with the encryption header names set by the app itself (see [../../../encryption.md](../../../encryption.md#key-exchange-endpoint)).

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `client_public_key` | String (Base64 text) | yes | `"<base64 text>"` | key at `EncryptionUtilImpl.dart @0x4016e88`; value is `Base64Codec.encode` output (`@0x4016e68`) derived from the client public key that `Encryption::getClientPublicKey` returns (`@0x4016e14`); how the value is produced is a scope note on [../../../encryption.md](../../../encryption.md#scope-note) |

Headers: the map from `EncryptionUtilImpl::commonHeaders` (`@0x4016ea4`); header names are listed in [../../../encryption.md](../../../encryption.md#request-headers-on-encrypted-calls). `exchangeKey` also reads `X-Key-Ident` from that map (`@0x4016ec8`, default empty string `@0x4016ee4`).

Skip rule: `exchangeKey` returns without a request when both a stored session key and a stored key identifier exist (`SpUtilImpl::getAeskey` `@0x4016dac`, `getIdentifyKey` `@0x4016db8`, `cbz` checks `@0x4016dcc` and `@0x4016dd4`); otherwise it removes both (`removeAesKey` `@0x4016de8`, `removeIdentifyKey` `@0x4016df4`) and starts over.

## `param_type`/`cmd`

n/a

## Response model (link)

None: the success closure only checks for a `Map<String, dynamic>` (`EncryptionUtilImpl.dart @0x401788c`) and hands it to `EncryptionUtilImpl::parse` (`@0x4017978`, call `@0x4017958`).

## Response

| field | type | required | example | source |
|---|---|---|---|---|
| `server_public_key` | String | yes | `"<base64 text>"` | key read in `parse` at `EncryptionUtilImpl.dart @0x40179c0`; upstream-confirmed (`session.py`, `data.server_public_key`) |

`parse` turns the server key into the session key and its identifier and persists them (`SpUtilImpl::saveAesKey` `@0x4017a94`, `saveIdentifyKey` `@0x4017aa4`). The derivation is a scope note, not documented here.

## Example request/response

Request, synthesized

```json
{ "client_public_key": "<base64 text>" }
```

Response, synthesized (shape only)

```json
{ "code": 0, "msg": "success!", "data": { "server_public_key": "<base64 text>" } }
```

## Errors seen

`api/errors.md` does not exist yet (Task 4.2). The failure closure of `exchangeKey` is not specific; generic transport codes are on [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). Upstream maps the server code 26070 to `ClientPublicKeyError` (upstream-confirmed, `errors.py`), which is the likely answer to a malformed client key; the app has no branch for it.

## Callers in app

- `charging/aiot/EncryptionUtilImpl.dart`: `exchangeKey` @0x4016d54 (`HttpBusinessImpl::requestHttp`).
- Called from `charging/ui/page/home/gdpr/gdpr_page_logic.dart::allow` (`@0x4016998`), which first resolves the regional host (`requestHostByRegion`, `@0x401697c`) and calls `exchangeKey` before it reads the user model (`@0x40169b8`). No other `bl` to `exchangeKey` exists in 3.24.3; the cached key material is also cleared on a region switch (`RegionSwitchHandler`, log `Encryption info cache cleared`, `region_switch_handler.dart @0x273c744`) and on logout (`SpUtilImpl::clearEncryptionInfo`).

## Since/changed

3.18.0: present, same URL string, body key, `needEncryption: false` descriptor (`EncryptionUtilImpl.dart` 3.18.0 `@0x311a47c`) and same header names. 3.24.3: unchanged. since: ≤3.18.0.

## Known unknowns

- What the SDK (native) does with the negotiated key: the app only stores it; the encrypted requests of the SDK path are built natively and were not analysed.
- Whether the native SDK performs its own key exchange: the Dart side has only this one caller.
- Server behavior on a repeated exchange with the same client key.

## Device-tested by

none recorded in this repository. Upstream library key exchange: `upstream-confirmed` (thomluther/anker-solix-api, `AnkerEncryptionHandler`, community-run).
