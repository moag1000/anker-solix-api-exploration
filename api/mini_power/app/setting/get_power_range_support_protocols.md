> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_power_range_support_protocols

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/mini_power/v1/app/setting/get_power_range_support_protocols`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x3472f74`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_model` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3472ea8` |
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3472ea8` |

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

- `charging/http/http_request_repository_impl.dart`: `getPowerSupportProtocols` @0x3472ea8 (encryptionRequestHttp; encrypted: true)
- `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart`: `getPowerSupportProtocols` @0x2afcf10 (encryptionRequestHttp; encrypted: true)

Called from: `charging/ui/page/device/a2345/a2345home/a2345home_logic.dart::getRangeProtocols`, `charging/ui/page/device/a2687/a2687home/a2687_home_logic.dart::getRangeProtocols`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
