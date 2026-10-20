> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_installation

## Purpose

Reads the installation (solar integration) mode that is saved for a solar bank or a site, for the A17C0 settings, the EZ1 mode pages and the station main page (callers `A17c0settingLogic::getInstallationReq`, `EZ1CurrentModeLogic::getInstallationReq`, `EZ1SelectModeLogic::getInstallationReq`, `StationMainPageLogic::goSelectMode`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`get_installation` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/compatible/get_installation` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x23f2ea4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x23f2e9c`, in `HttpRequestControllerImpl::getInstallationApi` (`charging/http/http_request_repository_impl.dart @0x23f2d64`), sent through `encryptionRequestHttp` (`@0x23f2ecc`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) `HttpRequestControllerImpl::getInstallationApi` (`charging/http/http_request_repository_impl.dart @0x23f2d64`) starts with an empty map literal (`THR::empty_array`, `@0x23f2dbc`) and replaces it by one of two one-pair literals: `{solarbank_sn: <parameter>}` when the first parameter is not null (`cmp w0, NULL` `@0x23f2dc8`, key `@0x23f2ddc`), else `{site_id: <parameter>}` when the second parameter is not null and a comparison with the empty string is false (`cmp w1, NULL` `@0x23f2e0c`, `r16 = ""` `@0x23f2e1c`, `tbz w0, #4` `@0x23f2e30` skips the insertion when the comparison is true, key `@0x23f2e44`); else the empty map is sent. The type-argument loads of these literals are not visible in the asm text.

| field | type | required | example | source |
|---|---|---|---|---|
| `solarbank_sn` | ? | optional (first parameter not null, guard `@0x23f2dc8`) | ? | `charging/http/http_request_repository_impl.dart @0x23f2ddc` |
| `site_id` | ? | optional (second parameter not null, guard `@0x23f2e0c`) | ? | `charging/http/http_request_repository_impl.dart @0x23f2e44` |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`SaveCompatibleSolarModel`](../../../../models/firmware.md#savecompatiblesolarmodel), parsed by `SaveCompatibleSolarModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x23f2f20`

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `SaveCompatibleSolarModel` top-level keys (`data/models.json`, `charging::SaveCompatibleSolarModel`): `display_installation` (bool?), `install_mode` (int?), `solar_sn` (String?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "solarbank_sn": "<?>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint). Alternative request bodies: `{"site_id": "<?>"}` or `{}`.

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getInstallationApi` @0x23f2d64 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getInstallationApi`
- `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart::getInstallationReq`
- `charging/ui/page/device/a17c0/ez1_current_mode/ez1_current_mode_logic.dart::getInstallationReq`
- `charging/ui/page/device/a17c0/ez1_select_mode/ez1_select_mode_logic.dart::getInstallationReq`
- `charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart::goSelectMode`
- `charging/ui/page/device/main/station_device_home/station_main_page/station_main_page_logic.dart::goSelectMode`
- `charging/ui/page/device/main/station_device_home/station_setting/station_setting_logic.dart::getInstallationReq`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `solarbank_sn` and `site_id` (parameters; the literal type arguments are not shown in the asm).
- Which of the two keys each caller sets. The `site_id` branch also tests the second parameter against the empty string (`r16 = ""` `@0x23f2e1c`, `tbz w0, #4` `@0x23f2e30` skips the insertion when the test is true); the compared operand was not attributed to a parameter name.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
