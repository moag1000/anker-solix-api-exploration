> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# preprocess_utility_rate_plan

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_energy_service/preprocess_utility_rate_plan`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x3d038e0`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `peak_sessions` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3d0377c` |
| `id` | ? | ? | ? | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f658` |
| `buy` | ? | ? | ? | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f658` |
| `energy_unit` | ? | ? | ? | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f658` |
| `start_time_period` | ? | ? | ? | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f658` |
| `end_time_period` | ? | ? | ? | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f658` |
| `peak_type` | ? | ? | ? | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f658` |
| `day_type` | ? | ? | ? | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f658` |
| `mode` | ? | ? | ? | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f658` |

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

- `charging/http/http_request_repository_impl.dart`: `dealUtilityRatePlanData` @0x3d0377c (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart`: `savePlanPrice` @0x3d3f658 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::dealUtilityRatePlanData`
- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart::sendPeakValleyData`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley_price_diff_secondary_edit/a17b1_peak_valley_price_diff_secondary_edit_logic.dart::sendPeakValleyData`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart::save`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
