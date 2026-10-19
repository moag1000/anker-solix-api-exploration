> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# delete_charging_mode

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/mini_power/v1/app/charging/delete_charging_mode`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x26c4004`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x26c3f3c` |

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

- `charging/http/http_request_repository_impl.dart`: `deleteCustomChargeMode` @0x26c3f3c (encryptionRequestHttp; encrypted: true)
- `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart`: `deleteCustomChargeMode` @0x3a9f464 (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::deleteCustomChargeMode`, `charging/ui/page/device/a2345/a2345custom_charging_mode/a2345custom_charging_mode_logic.dart::_deleteCustomChargeModeByCloud`, `charging/ui/page/device/a2687/a2687setting/a2687_charge_mode/a2687_custom_charge_mode/a2687_custom_charge_mode_logic.dart::_deleteCustomChargeModeByCloud`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
