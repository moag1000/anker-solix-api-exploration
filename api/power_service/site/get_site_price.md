> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_site_price

## Purpose

<!-- TODO -->

## Upstream name

`get_site_price` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/site/get_site_price`, method: not extracted by the inventory <!-- TODO -->; string-only: `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a304ec`
(literal also at 10 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a30408` |
| `accuracy` | ? | ? | ? | `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a30408` |
| `ems_data` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a4974` |
| `station_id` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a4974` |
| `not_include_nem` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a4974` |
| `currency` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a4974` |

Rows are the union over 7 senders; `source` is the first sender that sets the key.

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

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
