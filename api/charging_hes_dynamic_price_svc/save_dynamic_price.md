> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# save_dynamic_price

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_dynamic_price_svc/save_dynamic_price`, method: not extracted by the inventory <!-- TODO -->; string-only: `base_service/api_url.dart @0x2e82b4c`

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

- `base_service/api_url.dart`: `saveDynamicPrice` @0x2e82b34 (URL literal only, no `*Http*` call; sender found through callers: `ChargeDischargeSettingLogic::save` (`electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x41b469c`) via `ChargeDischargeSettingLogic::save` (`electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x41b469c`); also `ChargeDischargeSettingLogic_C5::save`, `CustomTimePeriodController::saveChargeTimes`, `ElectricityCompanySelectLogic::_switchToFlatpeakThenConfirm`, `ElectricityCompanySelectLogic::saveDynamicPrice`, `ElectricityPlaceConfirmPageLogic::save`)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
