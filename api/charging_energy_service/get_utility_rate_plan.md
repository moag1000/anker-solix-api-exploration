> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_utility_rate_plan

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_energy_service/get_utility_rate_plan`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart @0x28bbdd8`
(literal also at 2 more site(s) in `data/endpoints.json`)

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

- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart`: `_getRatePlanDataByStation` @0x28bbca4 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/a17b1_utility_rate_plan_logic.dart`: `_getRatePlanData` @0x293842c (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart`: `_getSystemPolicySetting` @0x288cf18 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart::_getSiteConfig`
- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart::didPopNext`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/a17b1_utility_rate_plan_logic.dart::onReady`
- `charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart::didPopNext`
- `charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart::requestSiteConfig`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
