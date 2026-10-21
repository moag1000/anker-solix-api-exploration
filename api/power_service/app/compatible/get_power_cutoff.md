> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_power_cutoff

## Purpose

Reads the discharge cut-off (SoC) settings of an A17C0/A17C1 solar bank for the settings pages, the A17C1 home preload and the device main page (callers `A17c0settingLogic::requestInfo`, `A17C1homeLogic::_preloadSettingsData`, `A17C1SettingLogic::requestInfo`, `DeviceMainLogic::getSolarBankParticleData`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`get_cutoff` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/compatible/get_power_cutoff` (asm-traced): URL string at `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x27507d4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x27507cc`, in `A17c0settingLogic::requestSoc` (`charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x275072c`), sent through `encryptionRequestHttp` (`@0x27507f8`).

Same URL and method object in the other sender(s) read:

- `POST /power_service/v1/app/compatible/get_power_cutoff` (asm-traced): URL string at `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart @0x286532c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2865324`, in `A17C1homeLogic::_preloadSocList` (`charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart @0x2865208`), sent through `encryptionRequestHttp` (`@0x2865350`).
- `POST /power_service/v1/app/compatible/get_power_cutoff` (asm-traced): URL string at `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart @0x2620938`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2620930`, in `A17C1homeLogic::onMessageDispatch` (`charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart @0x261fce8`), sent through `encryptionRequestHttp` (`@0x262095c`).
- `POST /power_service/v1/app/compatible/get_power_cutoff` (asm-traced): URL string at `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3454204`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x34541fc`, in `A17C1SettingLogic::requestSoc` (`charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3454154`), sent through `encryptionRequestHttp` (`@0x3454228`).
- `POST /power_service/v1/app/compatible/get_power_cutoff` (asm-traced): URL string at `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x24443f4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x24443ec`, in `DeviceMainLogic::requestSoc` (`charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x244434c`), sent through `encryptionRequestHttp` (`@0x2444418`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) Five senders, each with a one-pair `<String, String>` literal (type arguments `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x2750788`, `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart @0x28652e0`, `@0x26208ec`, `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x34541b8`, `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x24443a8`) and the key `device_sn`; the value is a parameter or a field of the device object.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x2750774`; `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart @0x28652a4`, `@0x26208b0`; `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x34541a4`; `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x2444394` |

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::SocModel` (`data/models.json` key; no models page) as a list under the key `power_cutoff_data`: all five success closures read the string literal `"power_cutoff_data"` and map the entries with the type argument `<SocModel>` (the list `map` closure is the shared closure `@0x24446e4` in `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart`, which calls `SocModel.fromJson` at `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x244470c`; literal/type-argument addresses: `@0x27508b4`/`@0x27509b8` in `a17c0setting_logic.dart`, `@0x2865418`/`@0x2865528` and `@0x26348b4`/`@0x26349b8` in `a17c1home_logic.dart`, `@0x34542e8`/`@0x34543ec` in `a17c1setting_logic.dart`, `@0x244454c`/`@0x2444650` in `device_main_logic.dart`). `A17C1SettingLogic::requestSoc` also constructs a `NewSocParamModel` (`charging::NewSocParamModel`) inside the same closure (`@0x3454244`).

`NewSocParamModel` in `A17C1SettingLogic.requestSoc` (asm-traced): the success closure (`charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3454244`) passes the mapped `SocModel` list to the stored callback (`ClosureCall` `@0x3454458`) and builds the `NewSocParamModel` separately, by `NewSocParamModel.fromJson` applied to the whole response object (`@0x3454478`), then hands it to `updateWithNewSocValue` (`@0x345448c`); it is not derived from the `SocModel` list.

## Response

(asm-traced) `SocModel` top-level keys (`data/models.json`): `id` (int?), `is_selected` (int?), `output_cutoff_data` (int?), `lowpower_input_data` (int?), `input_cutoff_data` (int?). `NewSocParamModel` keys: `power_cutoff_data` (unknown), `charge_upper_limit` (int?), `discharge_lower_limit` (int?), `backup_reserve` (int?), `cmd_type` (int?), `backup_reserve_switch` (int?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart`: `requestSoc` @0x275072c (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart`: `_preloadSocList` @0x2865208 (encryptionRequestHttp; encrypted: true); `onMessageDispatch` @0x261fce8 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart`: `requestSoc` @0x3454154 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart`: `requestSoc` @0x244434c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart::requestInfo`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::_preloadSettingsData`
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart::requestInfo`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::getSolarBankParticleData`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which device types answer with which cut-off entries (server data; the app queries by `device_sn` only).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
