> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# sync_config

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_energy_service/sync_config`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x2678754`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys found by the extractor. <!-- TODO -->

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

- `charging/http/http_request_repository_impl.dart`: `syncSiteConfig` @0x2678638 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::syncSiteConfig`
- `charging/ui/page/device/a1782/station/electricity_scene/a1782_electricity_scene_logic.dart::setBatteryReserve`
- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart::_getRatePlanDataByStation`
- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart::setBatteryReserve`
- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart::updateMode`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley_price_diff_secondary_edit/a17b1_peak_valley_price_diff_secondary_edit_logic.dart::ackUtilityRatePlan`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley_price_diff_secondary_edit/a17b1_peak_valley_price_diff_secondary_edit_logic.dart::setMode`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/a17b1_utility_rate_plan_logic.dart::_fixedRateSuccess`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/a17b1_utility_rate_plan_logic.dart::setMode`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart::setMode`
- `charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart::setBatteryReserve`
- `charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart::updateMode`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
