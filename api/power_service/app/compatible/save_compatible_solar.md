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

(asm-traced) `HttpRequestControllerImpl::saveCompatibleSolarApi` (`charging/http/http_request_repository_impl.dart @0x2753564`) receives the body as a parameter and builds none. The call has six call sites (`EZ1SelectModeLogic` twice, `SelectBrandLogic`, `SelectSolarPowerLogic`, `QrScannerLogic` twice); only `SelectBrandLogic` (`charging/ui/page/device/a17c0/select_brand/select_brand_logic.dart`) was read for the literal: it builds one literal of 5 pairs (raw `r2 = 20` at `@0x27532c8`, so 10 slots) with type arguments `<String, dynamic>` (`@0x275345c`) before the call at `@0x27534b4`.

| field | type | required | example | source |
|---|---|---|---|---|
| `brand_id` | ? | yes | ? | `charging/ui/page/device/a17c0/select_brand/select_brand_logic.dart @0x27532d4` (value: field of the logic object, `@0x27532e4`) |
| `solar_sn` | string | yes | | `charging/ui/page/device/a17c0/select_brand/select_brand_logic.dart @0x27532f0` (null check `cmp w1, NULL` `@0x2753300` replaces a null value) |
| `solar_brand` | ? | yes | ? | `charging/ui/page/device/a17c0/select_brand/select_brand_logic.dart @0x2753310` |
| `solar_model` | ? | yes | ? | `charging/ui/page/device/a17c0/select_brand/select_brand_logic.dart @0x2753350` (the constant string `"Others"` appears at `@0x275336c`) |
| `solarbank_sn` | ? | yes | ? | `charging/ui/page/device/a17c0/select_brand/select_brand_logic.dart @0x27533f0` (value from a device object field, `@0x2753428`) |

Typing, `"Others"` and the other call sites (asm-traced, `charging/ui/page/device/a17c0/select_brand/select_brand_logic.dart`): `solar_sn` is a value that is replaced by the String literal `""` when null (`cmp w1, NULL` `@0x2753300`, `r1 = ""` `@0x2753308`), so it is a string. `solar_model` is an Rx value compared by an equality call with the String literal `"Others"` (`@0x275336c`, call `@0x2753384`): when equal the literal `"Others"` itself is sent (`@0x2753390`), otherwise `field_7` of the selected model object (`@0x27533b8`) or null when no object is selected (`@0x27533b0`); so `"Others"` is the sentinel the model selector holds when the user picked no listed model. The other callers: `QrScannerLogic` (two call sites, closure `charging/ui/page/qr_Scanner/qr_scanner_logic.dart @0x33fb610` and `saveCompatibleSolar` `@0x33fb8dc`) and `SelectSolarPowerLogic.saveSelectSolarInfo` (`charging/ui/page/device/a17c0/select_solar_power/select_solar_power_logic.dart @0x3d73348`) load the same five key strings (`@0x33fb3d8`..`@0x33fb540`, `@0x33fb6dc`..`@0x33fb824`, `@0x3d73138`..`@0x3d73284`); the two call sites in `EZ1SelectModeLogic.next` (`charging/ui/page/device/a17c0/ez1_select_mode/ez1_select_mode_logic.dart @0x3d6506c`, `@0x3d65160`) load the key `solar_sn` (`@0x3d64f80`, `@0x3d64fb4`) and their other keys were not read.

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

- Types of `brand_id`, `solar_brand`, `solar_model` and `solarbank_sn`: fields or Rx values of UI logic objects (`charging/ui/page/device/a17c0/select_brand/select_brand_logic.dart @0x27532e4`, `@0x2753320`, `@0x2753428`) — attempted 2026-10-20 (two-hop not readable: the field declarations are not shown in the asm; `solar_sn` is typed (see Request). Header stays string-only)
- Server behaviour is not known from the app: this page states what the app builds and parses.
- The keys of the two `EZ1SelectModeLogic.next` call sites besides `solar_sn` (`charging/ui/page/device/a17c0/ez1_select_mode/ez1_select_mode_logic.dart @0x3d64f80`, `@0x3d64fb4`) — traced 2026-10-20: the other four call sites load the same five keys as `SelectBrandLogic` (see Request)

## Device-tested by

none
