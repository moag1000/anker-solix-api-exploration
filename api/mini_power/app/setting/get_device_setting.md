> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_device_setting

## Purpose

<!-- TODO -->

## Upstream name

`charger_get_device_setting` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/mini_power/v1/app/setting/get_device_setting`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x28a7cf0`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x28a7c38` |

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

- `charging/http/http_request_repository_impl.dart`: `getCustomChargeModeSetting` @0x28a7c38 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getCustomChargeModeSetting`
- `charging/ui/page/device/a2345/a2345charging_model/a2345charging_model_logic.dart::getLaboratorySwitch`
- `charging/ui/page/device/a2345/a2345home/a2345home_logic.dart::getLaboratorySwitch`
- `charging/ui/page/device/a2345/a2345laboratory/a2345laboratory_logic.dart::getLaboratorySwitch`
- `charging/ui/page/device/a2345/a2345setting/a2345setting_logic.dart::getLaboratorySwitch`
- `charging/ui/page/device/a2687/a2687home/a2687_home_logic.dart::getLaboratorySwitch`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
