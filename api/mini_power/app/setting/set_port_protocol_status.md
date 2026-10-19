> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

3.24.3: string present in the object pool, no code reference found (present in 3.18.0 with a sender)

# set_port_protocol_status

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/mini_power/v1/app/setting/set_port_protocol_status`, method: not extracted by the inventory <!-- TODO -->; string-only: `small_charging_platform/src/custom_protocol/page/custom_protocol_manager_logic.dart @0x246df28`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `small_charging_platform/src/custom_protocol/page/custom_protocol_manager_logic.dart @0x246dd88` |
| `version` | ? | ? | ? | `small_charging_platform/src/custom_protocol/page/custom_protocol_manager_logic.dart @0x246dd88` |
| `type` | ? | ? | ? | `small_charging_platform/src/custom_protocol/page/custom_protocol_manager_logic.dart @0x246dd88` |
| `port_list` | ? | ? | ? | `small_charging_platform/src/custom_protocol/page/custom_protocol_manager_logic.dart @0x246dd88` |

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

- `small_charging_platform/src/custom_protocol/page/custom_protocol_manager_logic.dart`: `setPortProtocolStatus` @0x246dd88 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: string present in the object pool, no code reference found. since: ≤3.18.0.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
