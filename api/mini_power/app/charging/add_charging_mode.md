> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# add_charging_mode

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/mini_power/v1/app/charging/add_charging_mode`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x38b75d4`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x38b7458` |
| `name` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x38b7458` |
| `number` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x38b7458` |
| `total_power` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x38b7458` |
| `max_total_power` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x38b7458` |
| `auto_exit` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x38b7458` |
| `has_charge_protocol` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x38b7458` |
| `power_settings` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x38b7458` |

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

- `charging/http/http_request_repository_impl.dart`: `addCustomChargeMode` @0x38b7458 (encryptionRequestHttp; encrypted: true)
- `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart`: `addCustomChargeMode` @0x3aa5e14 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::addCustomChargeMode`
- `charging/ui/page/device/a2345/a2345CNcustom_charging_edit/a2345CNcustom_charging_edit_logic.dart::_addCustomChargeModeToCloud`
- `charging/ui/page/device/a2345/a2345CNcustom_charging_edit/a2345CNcustom_platfrom_charging_edit_logic.dart::_addCustomChargeModeToCloud`
- `charging/ui/page/device/a2345/a2345custom_charging_edit/a2345custom_charging_edit_logic.dart::_addCustomChargeModeToCloud`
- `charging/ui/page/device/a2687/a2687setting/a2687_charge_mode/a2687_custom_charge_edit/a2687_custom_charge_edit_logic.dart::_addCustomChargeModeToCloud`
- `charging/ui/page/device/a2687/a2687setting/a2687_charge_mode/a2687_custom_charge_edit/a2687_custom_platform_charge_edit_logic.dart::_addCustomChargeModeToCloud`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
