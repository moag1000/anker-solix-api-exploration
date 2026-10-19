> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_utility_rate_plans

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/get_utility_rate_plans`, method: not extracted by the inventory <!-- TODO -->; string-only: `base_service/api_url.dart @0x24a5d70`

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

- `base_service/api_url.dart`: `getHesUtilityRatePlans` @0x24a5d58 (URL literal only, no `*Http*` call; sender `ElectricityPlaceConfirmPageLogic::_getUtilityRatePlan` (`electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29abe94`), reached through callers `ElectricityPlaceConfirmPageLogic::_getUtilityRatePlan` (`electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29abe94`); other senders: `ElectricityUsageHelper::getCurEmsModeType`, `ElectricityUsageHelper::getManualSetTOUDetailWithUrl`, `EmsAiModeConditionLogic::_getLargeUtilityRatePlan`, `GeneralPriceSettingLogic::getDevicePriceType`, `SmartModeLogic::_getUtilityRatePlan`; resolved from the URL literal at `base_service/api_url.dart @0x24a5d70` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
