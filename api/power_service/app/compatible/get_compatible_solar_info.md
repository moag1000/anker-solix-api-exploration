> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_compatible_solar_info

## Purpose

<!-- TODO -->

## Upstream name

`solar_info` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/app/compatible/get_compatible_solar_info`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x2750af4`
(literal also at 2 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `solarbank_sn` | ? | ? | ? | `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x2750a4c` |

Rows are the union over 3 senders; `source` is the first sender that sets the key.

## `param_type`/`cmd`

n/a

## Response model (link)

<!-- TODO -->

## Response

<!-- TODO -->

## Example request/response

<!-- TODO -->

## Errors seen

`api/errors.md`: <!-- TODO -->

## Callers in app

- `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart`: `requestSolarBankInfo` @0x2750a4c (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/a5140/a5140home/a5140home_logic.dart`: `getA17C0Info` @0x34ced84 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart`: `getSolarBankParticleData` @0x244350c (encryptionRequestHttp; encrypted: true)

Called from: `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart::requestInfo`, `charging/ui/page/device/a5140/a5140home/a5140home_logic.dart::onInit`, `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::getDeviceList`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
