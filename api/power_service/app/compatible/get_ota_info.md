> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_ota_info

## Purpose

Reads the OTA information of a third-party solar device that is attached to a solar bank (builder `getThirdOtaInfo`; no UI caller is recorded in `data/endpoints.json`, so the purpose is inferred from the builder name, string-only).

## Upstream name

`get_ota_info` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/compatible/get_ota_info` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x36c7e54`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x36c7e4c`, in `HttpRequestControllerImpl::getThirdOtaInfo` (`charging/http/http_request_repository_impl.dart @0x36c7d88`), sent through `encryptionRequestHttp` (`@0x36c7e74`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) The body is one map literal of 2 pairs (`AllocateArray`, raw `r2 = 8` at `@0x36c7dd8`, so 4 slots) with type arguments `<String, String>` at `@0x36c7e08`, so every value is typed in the literal; all keys are stored unconditionally.

| field | type | required | example | source |
|---|---|---|---|---|
| `solar_bank_sn` | string | yes | `"<solar_bank_sn>"` | `charging/http/http_request_repository_impl.dart @0x36c7de0` |
| `solar_sn` | string | yes | `"<solar_sn>"` | `charging/http/http_request_repository_impl.dart @0x36c7df4` |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`ThirdOtaInfoModel`](../../../../models/firmware.md#thirdotainfomodel), parsed by `ThirdOtaInfoModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x36c7f7c`

## Response

(asm-traced) All keys belong to the model page; this endpoint adds no wrapper fields of its own in the code read.

- `ThirdOtaInfoModel` top-level keys (`data/models.json`, `charging::ThirdOtaInfoModel`): `ota_status` (int?), `current_version` (String?), `timestamp` (int?), `version_type` (int?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "solar_bank_sn": "<solar_bank_sn>",
  "solar_sn": "<solar_sn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getThirdOtaInfo` @0x36c7d88 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getThirdOtaInfo`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- No UI caller is recorded for `getThirdOtaInfo` in `data/endpoints.json`.
- The error text in the failure closure reads "checkSolarForceUpdateState failed" (`@0x36c7e90` closure), a copied string; it does not name this call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
