> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# update_site_price

## Purpose

Saves the electricity price setup of a site: the TOU plan editors (`TOUPlanLogic::savePlan`, `TOUEditPreviewLogic::savePlan`, `TouHttpService::updateSitePrice`), the fixed-price page (`GeneralPriceSettingLogic::setFixedPrice`), the medium-charging plan helper (`ElectricityPricePlanApiHelper::saveMediumChargingPlan`) and two repository senders (`updateSitePriceRequest`, `postCloudSitePrice`) post it.

## Upstream name

`update_site_price` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/site/update_site_price` (asm-traced) at the senders that load a `Method` object next to the URL string (pool entry `pp+0xa7e0`, `Method.post`):

- `HttpRequestControllerImpl::postCloudSitePrice` (`http_request_repository_impl.dart @0x31e4050`): URL string `@0x31e40d0`, method object `Method.post` (`pp+0xa7e0`) `@0x31e40c8`.
- `HttpRequestControllerImpl::updateSitePriceRequest` (`http_request_repository_impl.dart @0x279e0cc`): URL string `@0x279e384`, method object `Method.post` (`pp+0xa7e0`) `@0x279e37c`.
- `ElectricityPricePlanApiHelper::saveMediumChargingPlan` (`electricity_price_plan_api_helper.dart @0x41a73e0`): URL string `@0x41a75d0`, method object `Method.post` (`pp+0xa7e0`) `@0x41a75c8`.
- `TOUPlanLogic::savePlan` (`tou_plan_logic.dart @0x31b88b4`): URL string `@0x31b8b14`, method object `Method.post` (`pp+0xa7e0`) `@0x31b8b0c`.
- `GeneralPriceSettingLogic::setFixedPrice` (`general_price_setting.dart @0x41a7afc`): URL string `@0x41a8044`, method object `Method.post` (`pp+0xa7e0`) `@0x41a803c`.
- `TouHttpService::updateSitePrice` (`tou_http_service.dart @0x4883d48`): URL string `@0x4883d7c`, method object `Method.post` (`pp+0xa7e0`) `@0x4883d94`.
- `TOUEditPreviewLogic::savePlan` (`tou_edit_preview_logic.dart @0x31de7dc`): URL string `@0x31dea04`, method object `Method.post` (`pp+0xa7e0`) `@0x31de9fc`.

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Seven senders with different key sets; the keys common to the senders that were read are listed.

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | yes | | `HttpRequestControllerImpl::updateSitePriceRequest` (`http_request_repository_impl.dart @0x279e0cc`): `<String, Object>` (`@0x279e338`), key `@0x279e134`, store `@0x279e144` (stack parameter); `ElectricityPricePlanApiHelper::saveMediumChargingPlan`, `TOUPlanLogic::savePlan`, `TOUEditPreviewLogic::savePlan`: `[]=` keys `@0x41a747c`, `@0x31b8964`, `@0x31de898`; `GeneralPriceSettingLogic::setFixedPrice` key `@0x41a7df0` (`field_7b` of the logic); `postCloudSitePrice`: the body is built by the caller `ConfirmPeakValleyLogic::setSitePrice` (`@0x3bc0dc8`), key `@0x3bc0e10` |
| `price` | ? | yes | | `updateSitePriceRequest`: key `@0x279e148`, double stored with `inline_Allocate_Double` `@0x279e180`; `[]=` keys in the TOU senders; `postCloudSitePrice` (caller `ConfirmPeakValleyLogic::setSitePrice`) key `@0x3bc0e64` (0.0) |
| `site_co2` | ? | yes | | `updateSitePriceRequest` key `@0x279e1ac` (double); TOU senders `[]=` keys `@0x41a7524`, `@0x31b8a20`, `@0x31de904`; `postCloudSitePrice` key `@0x3bc0e8c` |
| `site_price_unit` | ? | yes | | `updateSitePriceRequest` key `@0x279e210`; TOU senders `[]=` keys `@0x41a7578`, `@0x31b8a88`, `@0x31de96c`; `postCloudSitePrice` key `@0x3bc0e78` (empty string) |
| `price_type` | string | yes | `"use_time"` | `postCloudSitePrice` key `@0x3bc0ea0`, literal `@0x3bc0eac`; `setFixedPrice` literal `"fixed"` (key `@0x41a7ec0`, literal `@0x41a7ecc`); `updateSitePriceRequest` key `@0x279e248` takes a parameter |
| `current_mode` | int (unboxed, x) | yes | | `updateSitePriceRequest` key `@0x279e280`, `BoxInt64Instr` `@0x279e2b4` |
| `accuracy` | int (unboxed, x) | yes | | `updateSitePriceRequest` key `@0x279e2f0`, `BoxInt64Instr` `@0x279e2fc` |
| `use_time` | ? | optional | | `postCloudSitePrice` key `@0x3bc0eb8`; TOU senders `[]=` keys `@0x31b8abc`, `@0x31de9a4` |

`GeneralPriceSettingLogic::setFixedPrice` (`general_price_setting.dart @0x41a7afc`) builds several larger bodies for fixed and peak-valley prices (`peak_sessions`, `peak_valley_prices`, `fixed_price`, `currency`, `not_include_nem`, `utility_rate_plan`, `systemCode`, `main_sn`, `time`, `station_id`, `sell_price`) and also posts to `set_device_attrs` (`@0x41a7d84`) in the same function; only the send at `@0x41a8044` belongs to this URL, and which of the bodies it carries was not decoded.

## `param_type`/`cmd`

n/a

## Response model (link)

None resolved. `updateSitePriceRequest` passes the forwarding template `http_request_repository_impl.dart @0x261b9a0` and a failure closure `@0x279e3f8` that logs and calls `exeError()`; the TOU senders' callbacks (`tou_plan_logic.dart @0x31bb49c`, `tou_edit_preview_logic.dart @0x31df400`, `electricity_price_plan_api_helper.dart @0x41a7700`, `general_price_setting.dart @0x41a7970`) log `getSupportOption success` or `success: ` and navigate; none calls `fromJson` in the closures read.

## Response

No response key is read in the callbacks read.

## Example request/response

Request, synthesized (key set of `postCloudSitePrice`; types of the double fields unresolved)

```json
{"site_id": "<site_id>", "price": 0.0, "site_price_unit": "", "site_co2": 0.0, "price_type": "use_time", "use_time": "<use_time>"}
```

Response: none parsed in the callbacks read.

## Errors seen

One compare is traced: the `TOUEditPreviewLogic::savePlan` failure callback `tou_edit_preview_logic.dart @0x31df304` shows `settingFailed` and logs the code and the URL; no code compare was found. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `postCloudSitePrice` @0x31e4050 (encryptionRequestHttp; encrypted: true); `updateSitePriceRequest` @0x279e0cc (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/electricity_price_common/electricity_price_plan_api_helper.dart`: `saveMediumChargingPlan` @0x41a73e0 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart`: `getSaveDeviceEMSPrice` @0x249e420 (URL literal only, no `*Http*` call; sender `ElectricityUsageHelper::setDeviceEMSPriceArgument` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x249e2cc`), reached through callers `ElectricityUsageHelper::setDeviceEMSPriceArgument` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x249e2cc`); resolved from the URL literal at `electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x249e49c` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart`: `savePlan` @0x31b88b4 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart`: `setFixedPrice` @0x41a7afc (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/tou/impl_v2/service/tou_http_service.dart`: `updateSitePrice` @0x4883d48 (request; encrypted: default-true (requestHttp) — verify)
- `electricity_price/components/tou/page/tou_detail/view/tou_edit_preview_logic.dart`: `<anonymous closure> in TOUEditPreviewLogic::savePlan` @0x31df304 (URL literal only, no `*Http*` call; sends in the same function (`HttpServiceImpl::encryptionRequestHttp`); resolved from the URL literal at `electricity_price/components/tou/page/tou_detail/view/tou_edit_preview_logic.dart @0x31df3a4` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md)); `savePlan` @0x31de7dc (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/feature/peak_valley/confirm/confirm_peak_valley_logic.dart::setSitePrice`
- `charging/feature/utilitiy_rate_plan/dynamic_price/confirm/dynamic_price_confirm_logic.dart::save`
- `charging/feature/utilitiy_rate_plan/fixed_rate/fixed_rate_v2_logic.dart::save`
- `charging/feature/utilitiy_rate_plan/station_price_mode/station_price_mode_logic.dart::setSitePrice`
- `charging/http/http_request_repository.dart::postCloudSitePrice`
- `charging/http/http_request_repository.dart::updateSitePriceRequest`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/electricity_price/electricity_price_logic.dart::savePrice`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/utility_rate_plan/site_utility_rate_logic.dart::save`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/utility_rate_plan/site_utility_rate_plan_logic.dart::setTOUPrice`
- `charging/ui/page/device/main/station_device_home/station_price_setting/station_price_setting_logic.dart::savePrice`
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart::setDeviceEMSPriceArgument`
- `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart::clickSeasonItem`
- `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart::setFixedPriceV2`
- `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart::setTOU`
- `electricity_price/components/tou/impl_v2/repository/medium_tou_repository.dart::saveTouPlan`
- `electricity_price/components/tou/impl_v2/repository/platform_tou_repository.dart::saveTouPlan`
- `electricity_price/components/tou/page/tou_detail/view/tou_edit_preview_logic.dart::onDoneClick`
- `electricity_price/components/tou_pct/page/electricity_price_pad_preview/electricity_price_pad_preview_logic.dart::setSitePrice`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. `tools/out/diff_3.18.0_3.24.3.md` (changed params) lists ` salePrice.value.isEmpty:` and `fixedPrice.value.isEmpty:` as added: these are log-label strings inside `GeneralPriceSettingLogic::setFixedPrice` (`@0x41a80dc`, `@0x41a810c`), not request keys.

## Known unknowns

- Types of `site_id`, `price`, `site_co2`, `site_price_unit` and `price_type` in most senders (parameters and `[]=` values). Header stays string-only.
- Which body `setFixedPrice` sends to this URL (its function holds several bodies and two requests).
- `TouHttpService::updateSitePrice` (`tou_http_service.dart @0x4883d48`): body not read. `ElectricityPricePlanApiHelper::saveMediumChargingPlan` gets part of its body from the caller `GeneralPriceSettingLogic::setTOU` (`@0x41a68ac`: `device_sn`, `attributes`, `use_time`), also not decoded.
- Response handling was read only at the callback level; no model class is parsed there.

## Device-tested by

none
