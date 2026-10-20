> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# save_compatible_solar

## Purpose

Saves the third-party solar device (brand, model, serial number) that the user selected for a solar bank (callers `EZ1SelectModeLogic::next`, `SelectBrandLogic::saveSelectSolarInfo`, `SelectSolarPowerLogic::saveSelectSolarInfo`, `QrScannerLogic::checkDeviceSnCode`/`saveCompatibleSolar`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/compatible/save_compatible_solar` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x27535e8`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x27535e0`, in `HttpRequestControllerImpl::saveCompatibleSolarApi` (`charging/http/http_request_repository_impl.dart @0x2753564`), sent through `encryptionRequestHttp` (`@0x2753610`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) `HttpRequestControllerImpl::saveCompatibleSolarApi` (`charging/http/http_request_repository_impl.dart @0x2753564`) receives the body as a parameter and builds none. The call has six call sites (`EZ1SelectModeLogic` twice, `SelectBrandLogic`, `SelectSolarPowerLogic`, `QrScannerLogic` twice); only `SelectBrandLogic` was read: it builds one literal of 5 pairs (raw `r2 = 20` at `@0x27532c8`, so 10 slots) with type arguments `<String, dynamic>` (`@0x275345c`) before the call at `@0x27534b4`.

| field | type | required | example | source |
|---|---|---|---|---|
| `brand_id` | ? | yes | ? | `charging/ui/page/device/a17c0/select_brand/select_brand_logic.dart @0x27532d4` (value: field of the logic object, `@0x27532e4`) |
| `solar_sn` | ? | yes | ? | `charging/ui/page/device/a17c0/select_brand/select_brand_logic.dart @0x27532f0` (null check `cmp w1, NULL` `@0x2753300` replaces a null value) |
| `solar_brand` | ? | yes | ? | `charging/ui/page/device/a17c0/select_brand/select_brand_logic.dart @0x2753310` |
| `solar_model` | ? | yes | ? | `charging/ui/page/device/a17c0/select_brand/select_brand_logic.dart @0x2753350` (the constant string `"Others"` appears at `@0x275336c`) |
| `solarbank_sn` | ? | yes | ? | `charging/ui/page/device/a17c0/select_brand/select_brand_logic.dart @0x27533f0` (value from a device object field, `@0x2753428`) |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`SaveCompatibleSolarModel`](../../../../models/firmware.md#savecompatiblesolarmodel), parsed by `SaveCompatibleSolarModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x27536e0`

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `SaveCompatibleSolarModel` top-level keys (`data/models.json`, `charging::SaveCompatibleSolarModel`): `display_installation` (bool?), `install_mode` (int?), `solar_sn` (String?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "brand_id": "<?>",
  "solar_sn": "<?>",
  "solar_brand": "<?>",
  "solar_model": "<?>",
  "solarbank_sn": "<?>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `saveCompatibleSolarApi` @0x2753564 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::saveCompatibleSolarApi`
- `charging/ui/page/device/a17c0/ez1_select_mode/ez1_select_mode_logic.dart::next`
- `charging/ui/page/device/a17c0/select_brand/select_brand_logic.dart::saveSelectSolarInfo`
- `charging/ui/page/device/a17c0/select_solar_power/select_solar_power_logic.dart::saveSelectSolarInfo`
- `charging/ui/page/qr_Scanner/qr_scanner_logic.dart::checkDeviceSnCode`
- `charging/ui/page/qr_Scanner/qr_scanner_logic.dart::saveCompatibleSolar`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of all five keys: values are fields of UI logic objects and the literal is `<String, dynamic>`; the asm carries no field type.
- The bodies of the five other call sites (`EZ1SelectModeLogic` x2, `SelectSolarPowerLogic`, `QrScannerLogic` x2) were not read; they may send other keys.
- What `"Others"` stands for in `solar_model` (`@0x275336c`: a default when no model was picked; the branch was not decoded).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
