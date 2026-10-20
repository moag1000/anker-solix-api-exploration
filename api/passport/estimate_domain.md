> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# estimate_domain

## Purpose

Asks the account server for the API host of the user's region; sent by `HttpRequestControllerImpl::getRegionHostRequest` for `RegionSwitchHandler::_getRegionHostAsync`, `RegionLogic::showConfirmDialog` and `SplashLogic::requestHostByRegion` (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/estimate_domain` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x27408ac`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x274093c`, in `HttpRequestControllerImpl::getRegionHostRequest` (`charging/http/http_request_repository_impl.dart @0x274080c`), sent through `requestHttp` (`@0x274097c`).

The URL literal is appended to a base URL: `getLocalHostByRegion` (`@0x27408a8`) returns the host and the `+` operator joins it with the literal (`@0x27408b8`), so this request goes to a regional host, not to the usual base URL; the call passes the named arguments `fail`, `needEncryption`, `needTerminal`, `showLoading`, `useBaseUrl` (`@0x2740974`) with `false` loaded at `@0x2740958`, `@0x2740964` and `@0x2740968`; which argument carries which `false` was not decoded.

## Encrypted?

encrypted: `false` (asm-traced): the sender passes `needEncryption` explicitly in the named arguments (`charging/http/http_request_repository_impl.dart @0x2740974`, list `fail`, `needEncryption`, `needTerminal`, `showLoading`, `useBaseUrl`); by the slot indices in that list the value is the `false` loaded at `charging/http/http_request_repository_impl.dart @0x2740964`, as it is for `needTerminal` and `showLoading`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `ab` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x27408cc` (value store `@0x27408e4`) |
| `mode` | int (Smi, w) | yes | `1` | `charging/http/http_request_repository_impl.dart @0x27408e8` (value store `@0x27408f8`) |

The map literal has type arguments `<String, Object>` (`@0x27408fc`), which is not evidence of a value type. `mode` is the Smi raw 2 stored with a 32-bit store (`@0x27408f4`, `@0x27408f8`), so 1. `ab` is read from a field of an object held by the sender (`LoadField r1 = r2->field_13`, `@0x27408dc`).

## `param_type`/`cmd`

n/a

## Response model (link)

[`RegionHostModel`](../../models/other.md#regionhostmodel), parsed by `RegionHostModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x2740b40` in the success closure `@0x2740a6c`, applied to the value of the response key `data` (`"data"` loaded at `@0x2740b08`, map lookup `@0x2740b0c`).

## Response

(asm-traced) Top-level keys of `RegionHostModel` (`data/models.json`, `charging::RegionHostModel`): `domain` (String?), `is_same_region` (bool?). The closure then compares `is_same_region` with `true` (`@0x2740b54`) and calls `handleRegionHostModel` (`@0x2740b74`).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "ab": "<ab>",
  "mode": 1
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or its closures. The failure closure (`@0x274099c`) logs the code and falls back to `getPrivacyPolicyData` (`@0x2740a1c`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getRegionHostRequest` @0x274080c (requestHttp; encrypted: false, `needEncryption` passed explicitly)

Called from:

- `charging/account/handlers/region_switch_handler.dart::_getRegionHostAsync`
- `charging/http/http_request_repository.dart::getRegionHostRequest`
- `charging/ui/page/account/region/region_logic.dart::showConfirmDialog`
- `charging/ui/page/account/splash/splash_logic.dart::requestHostByRegion`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The type of `ab`: it is a field of an object (`charging/http/http_request_repository_impl.dart @0x27408dc`), no type is read at the store.
- Which of the named arguments of `requestHttp` (`charging/http/http_request_repository_impl.dart @0x2740974`) is `needEncryption`: the `Encrypted?` section keeps the inventory flag; the three `false` loads were not assigned to names.
- The `domain` value format and how `handleRegionHostModel` uses it were not read here.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
