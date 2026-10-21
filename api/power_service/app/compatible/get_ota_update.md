> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_ota_update

## Purpose

Reads the OTA update status of a third-party solar device during EZ1 mode selection, solar power selection and QR scanning (callers `EZ1SelectModeLogic::getOTAUpdateStatus`, `SelectSolarPowerLogic::getThirdOtaStatusRes`, `QrScannerLogic::getOTAUpdateStatus`; builder `getThirdOtaStatus`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`get_ota_update` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/compatible/get_ota_update` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x33fbc84`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x33fbc7c`, in `HttpRequestControllerImpl::getThirdOtaStatus` (`charging/http/http_request_repository_impl.dart @0x33fbb74`), sent through `encryptionRequestHttp` (`@0x33fbcac`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) One map literal of 2 pairs (`AllocateArray` raw `r2 = 8` at `@0x33fbbc4`, so 4 slots) with type arguments `<String, dynamic>` (`@0x33fbbf4`); `install_mode` is added afterwards when a numeric parameter is non-zero (`cbz x2` `@0x33fbc0c`, key `@0x33fbc38`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x33fbbcc` |
| `insert_sn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x33fbbe0` |
| `install_mode` | int (unboxed, x) | optional (added only when the parameter at `cbz x2` is non-zero, guard `@0x33fbc0c`) | | `charging/http/http_request_repository_impl.dart @0x33fbc38` |

Typing (asm-traced): the value of `install_mode` is the unboxed integer parameter tested by `cbz x2` (`@0x33fbc0c`); it is boxed by `BoxInt64Instr` (`@0x33fbc10`) and inserted with the map `[]=` call under the key at `@0x33fbc38` (`charging/http/http_request_repository_impl.dart`). Callers: `EZ1SelectModeLogic.getOTAUpdateStatus` (`charging/ui/page/device/a17c0/ez1_select_mode/ez1_select_mode_logic.dart @0x3d65740`) passes the named argument `installMode`, an unboxed integer field of the logic read at `@0x3d656e4` and boxed at `@0x3d656e8`; `SelectSolarPowerLogic.getThirdOtaStatusRes` (`charging/ui/page/device/a17c0/select_solar_power/select_solar_power_logic.dart @0x3d7376c`) and `QrScannerLogic.getOTAUpdateStatus` (`charging/ui/page/qr_Scanner/qr_scanner_logic.dart @0x33fbaac`) pass no named argument, so the default 0 applies and `install_mode` is not sent.

## `param_type`/`cmd`

n/a

## Response model (link)

- [`OTAUpdateStatus`](../../../../models/firmware.md#otaupdatestatus), parsed by `OTAUpdateStatus.fromJson` at `charging/http/http_request_repository_impl.dart @0x33fbd00`

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `OTAUpdateStatus` top-level keys (`data/models.json`, `charging::OTAUpdateStatus`): `is_ota_update` (bool?), `need_retry` (bool?), `retry_interval` (int?), `device_list` (List), `available` (bool?), `need_installation` (bool?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<?>",
  "insert_sn": "<?>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getThirdOtaStatus` @0x33fbb74 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getThirdOtaStatus`
- `charging/ui/page/device/a17c0/ez1_select_mode/ez1_select_mode_logic.dart::getOTAUpdateStatus`
- `charging/ui/page/device/a17c0/select_solar_power/select_solar_power_logic.dart::getThirdOtaStatusRes`
- `charging/ui/page/qr_Scanner/qr_scanner_logic.dart::getOTAUpdateStatus`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `device_sn` and `insert_sn`: parameters of the builder (`charging/http/http_request_repository_impl.dart @0x33fbbd8`, `@0x33fbbec`) — attempted 2026-10-20 (two-hop not readable: the callers read them through field and dispatch-table reads with no declared type in the asm (`charging/ui/page/qr_Scanner/qr_scanner_logic.dart @0x33fba68`). Header stays string-only)
- Server behaviour is not known from the app: this page states what the app builds and parses.
- Which values the integer `install_mode` field of `EZ1SelectModeLogic` (`charging/ui/page/device/a17c0/ez1_select_mode/ez1_select_mode_logic.dart @0x3d656e4`) takes: it is set elsewhere — traced 2026-10-20: the other two callers send no `install_mode`

## Device-tested by

none
