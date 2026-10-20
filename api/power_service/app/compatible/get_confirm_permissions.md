> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_confirm_permissions

## Purpose

Reads the permission-confirmation state of a device model during Wi-Fi set-up (callers `HttpRequestControllerImpl::getConfirmPermissionsApi` from `ZXConfigWifiSuccessLogic::done`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/compatible/get_confirm_permissions` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x26f8c9c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x26f8c94`, in `HttpRequestControllerImpl::getConfirmPermissionsApi` (`charging/http/http_request_repository_impl.dart @0x26f8bf4`), sent through `encryptionRequestHttp` (`@0x26f8cc4`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) The body is one map literal of 1 pair (`AllocateArray`, raw `r2 = 4` at `@0x26f8c34`, so 2 slots) with type arguments `<String, String>` at `@0x26f8c50`, so every value is typed in the literal; all keys are stored unconditionally.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_model` | string | yes | `"<device_model>"` | `charging/http/http_request_repository_impl.dart @0x26f8c3c` |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`ConfirmModel`](../../../../models/products.md#confirmmodel), parsed by `ConfirmModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x26f8d18`

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `ConfirmModel` top-level keys (`data/models.json`, `charging::ConfirmModel`): `is_confirm` (int?), `confirm_type` (String?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_model": "<device_model>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getConfirmPermissionsApi` @0x26f8bf4 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getConfirmPermissionsApi`
- `charging/ui/page/device/connect/zx_config_wifi_success/zx_config_wifi_succees_logic.dart::done`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which `device_model` values the caller passes (parameter `@0x26f8c3c`).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
