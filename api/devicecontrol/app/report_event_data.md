> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# report_event_data

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/devicecontrol/v1/app/report_event_data`, method: not extracted by the inventory <!-- TODO -->; string-only: `business_common/msg/device_fault_manager.dart @0x24127f0`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `business_common/msg/device_fault_manager.dart @0x2412574` |
| `product_code` | ? | ? | ? | `business_common/msg/device_fault_manager.dart @0x2412574` |
| `pn_payload` | ? | ? | ? | `business_common/msg/device_fault_manager.dart @0x2412574` |
| `report_time` | ? | ? | ? | `business_common/msg/device_fault_manager.dart @0x2412574` |

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

- `business_common/msg/device_fault_manager.dart`: `_reportEventToServer` @0x2412574 (encryptionRequestHttp; encrypted: true)

Called from: `business_common/msg/device_fault_manager.dart::_handleEventReport425`

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
