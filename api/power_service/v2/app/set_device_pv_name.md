> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# set_device_pv_name

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v2/app/set_device_pv_name`, method: not extracted by the inventory <!-- TODO -->; string-only: `ats_ax170/src/ats_ax170/page/station/system_ax170_flow_chart_controller.dart @0x2f3adbc`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `ats_ax170/src/ats_ax170/page/station/system_ax170_flow_chart_controller.dart @0x2f3ac50` |
| `pv_key` | ? | ? | ? | `ats_ax170/src/ats_ax170/page/station/system_ax170_flow_chart_controller.dart @0x2f3ac50` |
| `pv_name` | ? | ? | ? | `ats_ax170/src/ats_ax170/page/station/system_ax170_flow_chart_controller.dart @0x2f3ac50` |

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

- `ats_ax170/src/ats_ax170/page/station/system_ax170_flow_chart_controller.dart`: `requestRenamePV` @0x2f3ac50 (encryptionRequestHttp; encrypted: true)

Called from:

- `ats_ax170/src/ats_ax170/page/station/system_ax170_flow_chart.dart::_editPvName`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
