> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_compatible_solar_info

## Purpose

Reads the third-party solar device (brand, model, version, OTA state) attached to an A17C0 solar bank for its settings page, the A5140 home and the device list (callers `A17c0settingLogic::requestInfo`, `A5140homeController::onInit`, `DeviceMainLogic::getDeviceList`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`solar_info` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/compatible/get_compatible_solar_info` (asm-traced): URL string at `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x2750af4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2750aec`, in `A17c0settingLogic::requestSolarBankInfo` (`charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x2750a4c`), sent through `encryptionRequestHttp` (`@0x2750b18`).

Same URL and method object in the other sender(s) read:

- `POST /power_service/v1/app/compatible/get_compatible_solar_info` (asm-traced): URL string at `charging/ui/page/device/a5140/a5140home/a5140home_logic.dart @0x34cf05c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x34cf054`, in `A5140homeController::getA17C0Info` (`charging/ui/page/device/a5140/a5140home/a5140home_logic.dart @0x34ced84`), sent through `encryptionRequestHttp` (`@0x34cf080`).
- `POST /power_service/v1/app/compatible/get_compatible_solar_info` (asm-traced): URL string at `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x24437b8`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x24437b0`, in `DeviceMainLogic::getSolarBankParticleData` (`charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x244350c`), sent through `encryptionRequestHttp` (`@0x24437dc`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) Three senders, each with one `<String, String>` literal and one key: `A17c0settingLogic::requestSolarBankInfo` (`charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x2750a4c`, type arguments `@0x2750aa8`), `A5140homeController::getA17C0Info` (`charging/ui/page/device/a5140/a5140home/a5140home_logic.dart @0x34ced84`, `@0x34cf010`) and `DeviceMainLogic::getSolarBankParticleData` (`charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x244350c`, `@0x244376c`). The value is a field of the solar-bank device object in the two latter senders and a parameter in the first.

| field | type | required | example | source |
|---|---|---|---|---|
| `solarbank_sn` | string | yes | `"<solarbank_sn>"` | `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x2750a94` (`A17c0settingLogic`), `charging/ui/page/device/a5140/a5140home/a5140home_logic.dart @0x34ceffc`, `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x2443758` |

## `param_type`/`cmd`

n/a

## Response model (link)

`charging/model/check_solar_force_update_model::SolarInfo` (`data/models.json` key; no models page): all three senders pass the closure `@0x2443b28` (`charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart`), which builds it with `SolarInfo.fromJson` (`@0x2443b60`, target `charging/model/check_solar_force_update_model.dart @0x2443ba0`).

## Response

(asm-traced) `SolarInfo` top-level keys (`data/models.json`): `solar_sn` (String?), `solar_brand` (String?), `solar_model` (String?), `model_img` (String?), `version` (String?), `brand_id` (String?), `ota_status` (int?), `solar_model_name` (String?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "solarbank_sn": "<solarbank_sn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart`: `requestSolarBankInfo` @0x2750a4c (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/a5140/a5140home/a5140home_logic.dart`: `getA17C0Info` @0x34ced84 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart`: `getSolarBankParticleData` @0x244350c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart::requestInfo`
- `charging/ui/page/device/a5140/a5140home/a5140home_logic.dart::onInit`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::getDeviceList`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What each of the three senders does with the `SolarInfo` after the shared closure returns it: all three allocate the same closure (`charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x2750abc`, `charging/ui/page/device/a5140/a5140home/a5140home_logic.dart @0x34cf024`, `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x2443780`), so each parses the received object with `SolarInfo.fromJson`; their handling of the result was not read
- Which device types the three callers query (the `A5140` sender gates on firmware `"1.3.5"` `@0x34cedf8`; the `DeviceMainLogic` sender gates on the `"A17C0"` pn `@0x2443618`).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
