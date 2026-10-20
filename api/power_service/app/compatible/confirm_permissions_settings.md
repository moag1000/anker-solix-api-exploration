> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# confirm_permissions_settings

## Purpose

Reads the brand list for a confirm type (permission confirmation) when the user selects a solar brand or opens the solar-bank particle data (callers `SelectBrandLogic::getConfirmPermissionsSettings`, `DeviceMainLogic::getSolarBankParticleData`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/compatible/confirm_permissions_settings` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x2444f8c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2444f84`, in `HttpRequestControllerImpl::getConfirmPermissionsSettingsApi` (`charging/http/http_request_repository_impl.dart @0x2444ebc`), sent through `encryptionRequestHttp` (`@0x2444fb4`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) The body is one map literal of 2 pairs (`AllocateArray`, raw `r2 = 8` at `@0x2444f0c`, so 4 slots) with type arguments `<String, String>` at `@0x2444f40`, so every value is typed in the literal; all keys are stored unconditionally.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_model` | string | yes | `"A17C0"` | `charging/http/http_request_repository_impl.dart @0x2444f14` |
| `confirm_type` | string | yes | `"<confirm_type>"` | `charging/http/http_request_repository_impl.dart @0x2444f2c` |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`BrandModel`](../../../../models/products.md#brandmodel), parsed by `BrandModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x2445120`

## Response

(asm-traced) The success closure (`charging/http/http_request_repository_impl.dart @0x2444fd0`) reads the key `brand_list` (string literal `@0x244501c`) and builds `BrandModel` objects with `BrandModel.fromJson` (`@0x2445120`).

| field | type | required | example | source |
|---|---|---|---|---|
| `brand_list` | list of `BrandModel` | optional | `[...]` | `charging/http/http_request_repository_impl.dart @0x244501c` |

(asm-traced) All keys belong to the model page; this endpoint adds no wrapper fields of its own in the code read.

- `BrandModel` top-level keys (`data/models.json`, `charging::BrandModel`): `brand_id` (String?), `brand_name` (String?), `brand_img` (String?), `model_list` (List).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_model": "A17C0",
  "confirm_type": "<confirm_type>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getConfirmPermissionsSettingsApi` @0x2444ebc (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getConfirmPermissionsSettingsApi`
- `charging/ui/page/device/a17c0/select_brand/select_brand_logic.dart::getConfirmPermissionsSettings`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::getSolarBankParticleData`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What `confirm_type` selects: it is a parameter (`@0x2444f2c`); the two callers were not decoded for its value.
- Whether the `brand_list` entries are mapped one by one (the loop body was not decoded; only the `BrandModel.fromJson` call is read).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
