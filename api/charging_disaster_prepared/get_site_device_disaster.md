> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_site_device_disaster

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_disaster_prepared/get_site_device_disaster`, method: not extracted by the inventory <!-- TODO -->; string-only: `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart @0x35614c0`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `type` | ? | ? | ? | `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart @0x3561310` |
| `identifier_id` | ? | ? | ? | `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart @0x3561310` |

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

- `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart`: `_fetchDisasterSetting` @0x3561310 (encryptionRequestHttp; encrypted: true)

Called from:

- `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart::_setupEventBusListener`
- `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart::onInit`

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
