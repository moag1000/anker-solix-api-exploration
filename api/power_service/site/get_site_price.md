> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_site_price

## Purpose

Reads the electricity price of a site: the AI-mode condition logic, the power-usage scenario controller, the electricity usage helper, the TOU plan logic and the general price setting logic send `site_id` and `accuracy` through seven senders.

## Upstream name

`get_site_price` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/site/get_site_price` (asm-traced) at the senders that load a `Method` object next to the URL string (pool entry `pp+0xa7e0`, `Method.post`):

- `EmsAiModeConditionLogic::getSitePrice` (`ems_ai_mode_condition_logic.dart @0x2a30408`): URL string `@0x2a304ec`, method object `Method.post` (`pp+0xa7e0`) `@0x2a304e4`.
- `PowerUsageScenarioController::_fetchSitePriceUnit` (`power_usage_scenario_controller.dart @0x37af378`): URL string `@0x37af464`, method object `Method.post` (`pp+0xa7e0`) `@0x37af45c`.
- `PowerUsageScenarioController::getSitePrice` (`power_usage_scenario_controller.dart @0x2a2783c`): URL string `@0x2a27950`, method object `Method.post` (`pp+0xa7e0`) `@0x2a27948`.
- `HttpRequestControllerImpl::getSitePriceRequest` (`http_request_repository_impl.dart @0x23a1180`): URL string `@0x23a1284`, method object `Method.post` (`pp+0xa7e0`) `@0x23a127c`.
- `ElectricityUsageHelper::fetchSitePriceUnit` (`electricity_usage_helper.dart @0x2c5ebc0`): URL string `@0x2c5ecbc`, method object `Method.post` (`pp+0xa7e0`) `@0x2c5ecb4`.
- `TOUPlanLogic::getDataFromAPi` (`tou_plan_logic.dart @0x2c49144`): URL string `@0x2c4928c` without a `Method` object next to it; the method of this sender was not read.
- `GeneralPriceSettingLogic::getDevicePriceType` (`general_price_setting.dart @0x29a4974`): URL string `@0x29a4a48` without a `Method` object next to it; the method of this sender was not read.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Five senders send exactly `site_id` and `accuracy`; two senders add more keys.

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | yes |  | key `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a30470`; `EmsAiModeConditionLogic::getSitePrice` (`ems_ai_mode_condition_logic.dart @0x2a30408`): `<String, Object>` (`@0x2a304a0`), key `@0x2a30470`, store `@0x2a30488`; `PowerUsageScenarioController::_fetchSitePriceUnit` (`power_usage_scenario_controller.dart @0x37af378`): `<String, Object?>` (`@0x37af418`), key `@0x37af3f0`, store `@0x37af400`; `PowerUsageScenarioController::getSitePrice` (`@0x2a2783c`): `<String, Object>` (`@0x2a27904`), key `@0x2a278d4`, store `@0x2a278ec`; `HttpRequestControllerImpl::getSitePriceRequest` (`http_request_repository_impl.dart @0x23a1180`): `<String, Object>` (`@0x23a1238`), key `@0x23a1210`, store `@0x23a1220`; `ElectricityUsageHelper::fetchSitePriceUnit` (`electricity_usage_helper.dart @0x2c5ebc0`): `<String, Object?>` (`@0x2c5ec70`), key `@0x2c5ec44`, store `@0x2c5ec54` |
| `accuracy` | int (Smi, w) | yes | `5` | key `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a3048c`; constant in four senders: `mov` + `stur w`, tagged, so 5 (`@0x2a30498`/`@0x2a3049c`, `ak_soft_ems/ems_list/power_usage_scenario_controller.dart @0x37af410`/`@0x37af414`, `@0x2a278fc`/`@0x2a27900`, `charging/http/http_request_repository_impl.dart @0x23a1230`/`@0x23a1234`) |
| `accuracy` | int (Smi, w) | yes | | `ElectricityUsageHelper::fetchSitePriceUnit`: key `electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x2c5ec58`, `lsl x, x, #1` `@0x2c5ec68` Smi-tags the unboxed parameter, store `@0x2c5ec6c` |

`TOUPlanLogic::getDataFromAPi` (`tou_plan_logic.dart @0x2c49144`: `site_id` `@0x2c492c8`, `accuracy` constant 5 `@0x2c492d8`/`@0x2c492dc`, `price_type` the string `"use_time"` `@0x2c494a8`, `[]=` keys `device_sn`, `station_id`, `attributes`) and `GeneralPriceSettingLogic::getDevicePriceType` (`general_price_setting.dart @0x29a4974`: several `<String, Object?>` maps with `site_id`, `accuracy`, `device_sn`, `attributes`, `station_id`, `not_include_nem`, `currency`) build larger bodies; their URL literals (`@0x2c4928c`, `@0x29a4a48`) have no `Method` object next to them and their value types were not read.

## `param_type`/`cmd`

n/a

## Response model (link)

Per sender. `SitePriceModel` (`data/models.json` keys `ak_soft_ems::SitePriceModel` and `charging::SitePriceModel`; fields on [`models/pricing.md`](../../../models/pricing.md#sitepricemodel)): parsed in `ems_ai_mode_condition_logic.dart @0x2a30534` and `power_usage_scenario_controller.dart @0x2a27ae4` (both resolve to `ak_soft_ems/model/site_price_model.dart`) and in `http_request_repository_impl.dart @0x23a1384` (resolves to `charging/model/site_price_model.dart`). The unit-fetching senders pass forwarding templates to callers that were not read; `TOUPlanLogic` and `GeneralPriceSettingLogic` parse in closures that compare many class ids and were not decoded.

## Response

Top-level keys of the model (from `data/models.json`): `site_id` (String), `price` (num), `site_co2` (num), `site_price_unit` (String), `current_mode` (int), `price_type` (String), `use_time` (`PeakValleyParamData`), `dynamic_price` (`DynamicPriceParamData`).

## Example request/response

Request, synthesized (decrypted body of `getSitePriceRequest`; type of `site_id` unresolved)

```json
{"site_id": "<site_id>", "accuracy": 5}
```

Response keys: see Response; no capture.

## Errors seen

None traced. The failure callbacks `power_usage_scenario_controller.dart @0x2a27998` and `http_request_repository_impl.dart @0x23a12c8` log the code and message; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart`: `getSitePrice` @0x2a30408 (encryptionRequestHttp; encrypted: true)
- `ak_soft_ems/ems_list/power_usage_scenario_controller.dart`: `_fetchSitePriceUnit` @0x37af378 (encryptionRequestHttp; encrypted: true); `getSitePrice` @0x2a2783c (encryptionRequestHttp; encrypted: true)
- `charging/http/http_request_repository_impl.dart`: `getSitePriceRequest` @0x23a1180 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart`: `<anonymous closure> in ElectricityUsageHelper::getPriceType` @0x35f72e8 (URL literal only, no `*Http*` call; sends in the same function (`HttpServiceImpl::encryptionRequestHttp`); resolved from the URL literal at `electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x35f7690` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md)); `fetchSitePriceUnit` @0x2c5ebc0 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart`: `<anonymous closure> in TOUPlanLogic::getDataFromAPi` @0x2c49658 (URL literal only, no `*Http*` call; no sender within 3 caller levels); `getDataFromAPi` @0x2c49144 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart`: `<anonymous closure> in GeneralPriceSettingLogic::getDevicePriceType` @0x29a4e04 (URL literal only, no `*Http*` call; sends in the same function (`HttpServiceImpl::encryptionRequestHttp`); resolved from the URL literal at `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a5a20` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md)); `getDevicePriceType` @0x29a4974 (encryptionRequestHttp; encrypted: true); `getPriceTypeUrl` @0x29a4d20 (URL literal only, no `*Http*` call; sender `GeneralPriceSettingLogic::getDevicePriceType` (`electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a4974`), reached through callers `GeneralPriceSettingLogic::getDevicePriceType` (`electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a4974`); resolved from the URL literal at `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a4d88` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

Called from:

- `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart::onReady`
- `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart::refreshPagePurely`
- `ak_soft_ems/ems_list/power_usage_scenario_controller.dart::onReady`
- `ak_soft_ems/ems_list/power_usage_scenario_controller.dart::requestSitePriceType`
- `ak_soft_ems/ems_list/power_usage_scenario_page.dart::didPopNext`
- `charging/feature/utilitiy_rate_plan/station_price_mode/station_price_mode_logic.dart::getSitePrice`
- `charging/http/http_request_repository.dart::getSitePriceRequest`
- `charging/ui/page/device/a1782/station/electricity_scene/a1782_electricity_scene_logic.dart::getCurrency`
- `charging/ui/page/device/a1782/station/setting/menu_controller/electricity_price_controller.dart::onTapMenu`
- `charging/ui/page/device/a1782/station/system_policy/a1782_system_policy_logic.dart::getCurrency`
- `charging/ui/page/device/a17c5/ai_mode_condition/ai_mode_condition_logic.dart::getSitePrice`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::getAiModeStatus`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/electricity_price/electricity_price_logic.dart::getSitePrice`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/power_usage_scenario_logic.dart::getPriceType`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/power_usage_scenario_logic.dart::getSitePrice`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/station_home_settings_logic.dart::getPriceType`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/utility_rate_plan/site_utility_rate_plan_logic.dart::getSitePrice`
- `charging/ui/page/device/main/station_device_home/station_price_setting/station_price_setting_logic.dart::getSitePrice`
- `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart::parserRouterInfo`
- `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart::updateData`
- `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart::getDevicePriceType`
- `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart::onReady`
- `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart::setFixedPriceV2`
- `electricity_price/components/tou/page/tou_result_view/tou_result/tou_result_logic.dart::onReady`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta. The model `SitePriceModel` is `≤3.18.0` (`charging`) and 3.24.3 (`ak_soft_ems`) in `data/models.json`.

## Known unknowns

- Types of `site_id` in the five simple senders (all maps are `<String, Object>` or `<String, Object?>`). Header stays string-only. — attempted 2026-10-20 (two-hop not readable: five simple senders with `<String, Object>` maps; callers not followed in this pass. Header stays string-only)
- The two larger senders (`TOUPlanLogic::getDataFromAPi`, `GeneralPriceSettingLogic::getDevicePriceType`): method object, value types and response parsing were not read. — not traced 2026-10-20 in this pass (`TOUPlanLogic::getDataFromAPi`, `GeneralPriceSettingLogic::getDevicePriceType`); the reason given in the bullet stands
- What `accuracy` selects (the app sends 5 or a parameter): server side.

## Device-tested by

none
