> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# shelly_ctrl_device

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/shelly_ctrl_device`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x3073dec`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3073d34` |
| `op_type` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3073d34` |
| `value` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3073d34` |

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

- `charging/http/http_request_repository_impl.dart`: `changeShellyDeviceStatus` @0x3073d34 (encryptionRequestHttp; encrypted: true)
- `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart`: `changeShellyDeviceStatus` @0x3291774 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::changeShellyDeviceStatus`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::changeShellyPlugSwitch`
- `charging/ui/page/device/third_party_device/shelly/shellyhome/shellyhome_logic.dart::changeShellyPlugSwitch`
- `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart::homeLoadSwitchChanged`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
