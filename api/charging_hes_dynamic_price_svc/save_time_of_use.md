> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# save_time_of_use

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_dynamic_price_svc/save_time_of_use`, method: not extracted by the inventory <!-- TODO -->; string-only: `base_service/api_url.dart @0x2e82420`

## Encrypted?

encrypted: "unknown (URL literal only, no `*Http*` call)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

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

- `base_service/api_url.dart`: `saveAutoTou` @0x2e82408 (URL literal only, no `*Http*` call; sender found through callers: `GeneralPriceSettingLogic::setTOU` (`electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a68ac`) via `ElectricityPricePlanApiHelper::changeToTouPlan` (`electricity_price/components/electricity_price_common/electricity_price_plan_api_helper.dart @0x31a9fdc`) -> `GeneralPriceSettingLogic::setTOU` (`electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a68ac`))

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
