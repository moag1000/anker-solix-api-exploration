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

(asm-traced) `HttpRequestControllerImpl::getInstallationApi` (`charging/http/http_request_repository_impl.dart @0x23f2d64`) starts with an empty map literal (`THR::empty_array`, `@0x23f2dbc`). Two steps run one after the other: first, when the first parameter is not null (`cmp w0, NULL` `@0x23f2dc8`), the map becomes `{solarbank_sn: <parameter>}` (key `@0x23f2ddc`); then, when the second parameter is not null (`cmp w1, NULL` `@0x23f2e0c`) and its comparison with the empty string (`r16 = ""` `@0x23f2e1c`, equality call `@0x23f2e2c`) is false, the map is replaced by a new literal `{site_id: <parameter>}` (key `@0x23f2e44`, `Map._fromLiteral` `@0x23f2e5c`); `tbz w0, #4` `@0x23f2e30` skips this second step when the comparison is true (the second parameter equals the empty string). So the body carries `site_id` alone when the second parameter is non-null and not empty, else `solarbank_sn` alone when the first parameter is non-null, else the empty map. The type-argument loads of these literals are not visible in the asm text.

| field | type | required | example | source |
|---|---|---|---|---|
| `solarbank_sn` | ? | optional (first parameter not null, guard `@0x23f2dc8`; dropped when `site_id` is sent) | ? | `charging/http/http_request_repository_impl.dart @0x23f2ddc` |
| `site_id` | string | optional (second parameter not null and not the empty string, guards `@0x23f2e0c`, `@0x23f2e30`; it replaces `solarbank_sn`) | | `charging/http/http_request_repository_impl.dart @0x23f2e44` |

Callers and typing (asm-traced; the parameters are named `deviceSn` and `siteId` in the callers' call descriptors): `ez1_current_mode_logic.dart @0x40ae0a8` and `a17c0setting_logic.dart @0x344db4c` (both `getInstallationReq`) pass `deviceSn` and `siteId`; `ez1_select_mode_logic.dart @0x344f2f4` passes `deviceSn` only; `station_setting_logic.dart @0x2903a08` passes `siteId` only; `StationMainPageLogic.goSelectMode` (`charging/ui/page/device/main/station_device_home/station_main_page/station_main_page_logic.dart @0x23f2b9c`) and `StationHomeInfoLogic.goSelectMode` (`charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart @0x2c20cc0`) pass `siteId` only (with `showLoading`). The type of `site_id` is read at the first of these: `field_7` of an Rx `.value`, replaced by the String literal `""` when null (`station_main_page_logic.dart @0x23f2b68`), so it is a string. `solarbank_sn` is passed as `field_6b` of an Rx `.value` in the callers that send `deviceSn` (`ez1_current_mode_logic.dart @0x40ae078`) and has no declared type in the asm.

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

- Type of `solarbank_sn`: `field_6b` of an Rx `.value` in the callers that send it (`charging/ui/page/device/a17c0/ez1_current_mode/ez1_current_mode_logic.dart @0x40ae078`) — attempted 2026-10-20 (two-hop not readable: the field declaration is not shown in the asm. Header stays string-only)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
