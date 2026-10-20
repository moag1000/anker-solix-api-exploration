> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# check_third_sn

## Purpose

Checks the serial number of a scanned third-party solar device against the compatible-device list (caller `QrScannerLogic::checkDeviceSnCode`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/compatible/check_third_sn` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x33fa5cc`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x33fa5c4`, in `HttpRequestControllerImpl::checkThirdSN` (`charging/http/http_request_repository_impl.dart @0x33fa4e8`), sent through `encryptionRequestHttp` (`@0x33fa5ec`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) The body is one map literal of 3 pairs (`AllocateArray`, raw `r2 = 12` at `@0x33fa53c`, so 6 slots) with type arguments `<String, String>` at `@0x33fa580`, so every value is typed in the literal; all keys are stored unconditionally.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_model` | string | yes | `"<device_model>"` | `charging/http/http_request_repository_impl.dart @0x33fa544` |
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_request_repository_impl.dart @0x33fa558` |
| `brand_id` | string | yes | `"<brand_id>"` | `charging/http/http_request_repository_impl.dart @0x33fa56c` |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`OTAUpdateStatus`](../../../../models/firmware.md#otaupdatestatus), parsed by `OTAUpdateStatus.fromJson` at `charging/http/http_request_repository_impl.dart @0x33fa640`

## Response

(asm-traced) All keys belong to the model page; this endpoint adds no wrapper fields of its own in the code read.

- `OTAUpdateStatus` top-level keys (`data/models.json`, `charging::OTAUpdateStatus`): `is_ota_update` (bool?), `need_retry` (bool?), `retry_interval` (int?), `device_list` (List), `available` (bool?), `need_installation` (bool?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_model": "<device_model>",
  "device_sn": "<device_sn>",
  "brand_id": "<brand_id>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `checkThirdSN` @0x33fa4e8 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::checkThirdSN`
- `charging/ui/page/qr_Scanner/qr_scanner_logic.dart::checkDeviceSnCode`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which values of `device_model` and `brand_id` the scanner passes: the three values are parameters of the builder (`@0x33fa544`, `@0x33fa558`, `@0x33fa56c`) and the caller was not decoded for their content.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
