> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_price_company

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_dynamic_price_svc/get_price_company`, method: not extracted by the inventory <!-- TODO -->; string-only: `base_service/api_url.dart @0x27bde50`

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

- `base_service/api_url.dart`: `getPriceCompany` @0x27bde38 (URL literal only, no `*Http*` call; sender `HttpHelper::getDataFromService` (`electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bda38`) (HTTP helper wrapper), called from `ChargeDischargeSettingLogic::getDynamicPriceCompany` (`electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x29b6424`); also through `ChargeDischargeSettingLogic_C5::getDynamicPriceCompany`, `DynamicPriceDetailInfoViewState::getDynamicPriceCompany`, `ElectricityCompanySelectLogic::getDynamicPriceCompany`, `ElectricityPriceProviderLogic::getDynamicPriceCompany`, `ElectricityPriceServiceImpl::_supportAutoTou`; other senders: `PowerUsageScenarioController::_requestDynamicPriceCompany`, `PowerUsageScenarioController::getDynamicPriceCompany`, `PowerUsageScenarioLogic::_requestDynamicPriceCompany`, `SystemPolicyLogic::_getDynamicPriceCompany`; resolved from the URL literal at `base_service/api_url.dart @0x27bde50` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
