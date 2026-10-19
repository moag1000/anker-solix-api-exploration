> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

Removed in 3.24.3 — present in 3.18.0 only

# get_port_protocol_status

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/mini_power/v1/app/setting/get_port_protocol_status`, method: not extracted by the inventory <!-- TODO -->; string-only: `small_charging_platform/src/custom_protocol/device_online_listener.dart @0x34d2a24`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `small_charging_platform/src/custom_protocol/device_online_listener.dart @0x34d2934` |
| `version` | ? | ? | ? | `small_charging_platform/src/custom_protocol/device_online_listener.dart @0x34d2934` |

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

- `small_charging_platform/src/custom_protocol/device_online_listener.dart`: `getPortProtocolStatus` @0x34d2934 (encryptionRequestHttp; encrypted: true)
- `small_charging_platform/src/custom_protocol/page/custom_protocol_manager_logic.dart`: `getPortProtocolStatus` @0x27a00a4 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: absent (removed). since: ≤3.18.0.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
