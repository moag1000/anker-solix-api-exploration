> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_charging_mode_list

## Purpose

<!-- TODO -->

## Upstream name

`charger_get_charging_modes` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/mini_power/v1/app/charging/get_charging_mode_list`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x26c1398`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x26c12e0` |

Rows are the union over 2 senders; `source` is the first sender that sets the key.

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

- `charging/http/http_request_repository_impl.dart`: `getCustomChargeModeList` @0x26c12e0 (encryptionRequestHttp; encrypted: true)
- `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart`: `getCustomChargeModeList` @0x2afb74c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getCustomChargeModeList`
- `charging/ui/page/device/a2345/a2345charging_model/a2345charging_model_logic.dart::getCustomChargeModelList`
- `charging/ui/page/device/a2345/a2345custom_charging_mode/a2345custom_charging_mode_logic.dart::_getCustomChargeModeListByCloud`
- `charging/ui/page/device/a2687/a2687setting/a2687_charge_mode/a2687_charge_mode_logic.dart::getCustomChargeModelList`
- `charging/ui/page/device/a2687/a2687setting/a2687_charge_mode/a2687_custom_charge_mode/a2687_custom_charge_mode_logic.dart::_getCustomChargeModeListByCloud`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
