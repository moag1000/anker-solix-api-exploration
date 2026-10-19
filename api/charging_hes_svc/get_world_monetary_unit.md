> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_world_monetary_unit

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/get_world_monetary_unit`, method: not extracted by the inventory <!-- TODO -->; string-only: `base_service/api_url.dart @0x29ae8f4`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `countryCodes` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x28e9994` |
| `areaCodes` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x28e9994` |
| `siteId` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x28e9994` |

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

- `base_service/api_url.dart`: `getPriceUnitsConfig` @0x29ae8dc (URL literal only, no `*Http*` call; sender found through callers: `ElectricityUsageHelper::getPriceUnits` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x29ae3f4`) via `ElectricityUsageHelper::getPriceUnits` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x29ae3f4`))
- `charging/http/http_request_repository_impl.dart`: `getPriceUnits` @0x28e9994 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getPriceUnits`
- `charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart::_getCurrency`
- `charging/ui/page/device/a5101/setting/peaksAndValleys/peaks_valleys_logic.dart::fetchPriceUnits`
- `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::getCurrency`
- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart::getCurrency`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
