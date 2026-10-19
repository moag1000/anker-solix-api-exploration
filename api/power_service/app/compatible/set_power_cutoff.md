> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# set_power_cutoff

## Purpose

<!-- TODO -->

## Upstream name

`set_cutoff` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/app/compatible/set_power_cutoff`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x3d60a14`
(literal also at 3 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x3d60820` |
| `cutoff_data_id` | ? | ? | ? | `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x3d60820` |
| `charge_upper_limit` | ? | ? | ? | `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d95764` |
| `discharge_lower_limit` | ? | ? | ? | `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d95764` |
| `backup_reserve` | ? | ? | ? | `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d95764` |
| `backup_reserve_switch` | ? | ? | ? | `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d95764` |
| `cmd_type` | ? | ? | ? | `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d95764` |

Rows are the union over 4 senders; `source` is the first sender that sets the key.

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

- `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart`: `requestToSetSoc` @0x3d60820 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart`: `_dealWithBleResponse` @0x263087c (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart`: `requestNewSetSoc` @0x3d95764 (encryptionRequestHttp; encrypted: true); `requestToSetSoc` @0x3d94c6c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart::showSocDialog`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::onMessageDispatch`
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart::onTapSafetySoC`
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart::showSocDialog`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
