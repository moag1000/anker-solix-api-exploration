> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_ota_info

## Purpose

Reads the OTA information of a third-party solar device that is attached to a solar bank (builder `getThirdOtaInfo`; the wrapper has no call site in the asm (see Callers in app), so the purpose is inferred from the builder name, string-only).

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

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

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

none traced: no numeric error code is compared in the sender or the closures read for this page. The failure closure (`charging/http/http_request_repository_impl.dart @0x36c7e90`) logs the text "checkSolarForceUpdateState failed", which is a copied string and does not name this call. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getThirdOtaInfo` @0x36c7d88 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getThirdOtaInfo`

No direct call site of the wrapper `HttpRequestController::getThirdOtaInfo` (`charging/http/http_request_repository.dart @0x36c7d34`) exists in the asm tree: a search for its call target address and for the function name found nothing outside the two repository files (2026-10-20); the app may reach it through a dispatch-table call, which Blutter does not name.

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
