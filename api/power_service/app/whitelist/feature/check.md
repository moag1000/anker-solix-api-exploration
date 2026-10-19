> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# check

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/whitelist/feature/check`, method: not extracted by the inventory <!-- TODO -->; string-only: `ak_soft_ems/ems_list/power_usage_scenario_controller.dart @0x35662f8`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `feature_code` | ? | ? | ? | `ak_soft_ems/ems_list/power_usage_scenario_controller.dart @0x3565f9c` |
| `product_code` | ? | ? | ? | `ak_soft_ems/ems_list/power_usage_scenario_controller.dart @0x3565f9c` |

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

- `ak_soft_ems/ems_list/power_usage_scenario_controller.dart`: `checkFeatureVisibility` @0x3565f9c (encryptionRequestHttp; encrypted: true)
- `charging/http/http_request_repository_impl.dart`: `getWhiteListStatusRes` @0x26ffad4 (encryptionRequestHttp; encrypted: true)

Called from: `ak_soft_ems/ems_list/power_usage_scenario_controller.dart::_updateFeatureVisibility`, `charging/http/http_request_repository.dart::getWhiteListStatusRes`, `charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart::_requestEvChargerWhiteList`, `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/power_usage_scenario_logic.dart::getWhiteListStatus`, `charging/ui/page/user/main/user_main_page_logic.dart::_getWhileList`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
