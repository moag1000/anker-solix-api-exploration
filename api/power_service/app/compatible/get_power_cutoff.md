> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_power_cutoff

## Purpose

<!-- TODO -->

## Upstream name

`get_cutoff` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/app/compatible/get_power_cutoff`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x27507d4`
(literal also at 4 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x275072c` |

Rows are the union over 5 senders; `source` is the first sender that sets the key.

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

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
