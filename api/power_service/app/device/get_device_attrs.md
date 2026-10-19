> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_device_attrs

## Purpose

<!-- TODO -->

## Upstream name

`get_device_attributes` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/app/device/get_device_attrs`, method: not extracted by the inventory <!-- TODO -->; string-only: `ak_soft_ems/util/timezone_util.dart @0x22ba254`
(literal also at 23 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart @0x2a3ebd0` |
| `attributes` | ? | ? | ? | `ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart @0x2a3ebd0` |
| `enable_0w_v2` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x239ec40` |
| `site_id` | ? | ? | ? | `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart @0x2c49144` |
| `accuracy` | ? | ? | ? | `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart @0x2c49144` |
| `ems_data` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a4974` |
| `station_id` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a4974` |
| `not_include_nem` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a4974` |
| `currency` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a4974` |

Rows are the union over 6 senders; `source` is the first sender that sets the key.

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

- `ak_soft_ems/util/timezone_util.dart`: `getDeviceTimezone` @0x22ba090 (URL literal only, no `*Http*` call)
- `ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart`: `getTouElectricAttrs` @0x2a3ebd0 (encryptionRequestHttp; encrypted: true)
- `as200/src/page/home/as200_home_logic.dart`: `_getLowLoadAutoShutdownTimeout` @0x29f088c (encryptionRequestHttp; encrypted: true)
- `charging/http/http_request_repository_impl.dart`: `getDeviceAttrs` @0x239ec40 (encryptionRequestHttp; encrypted: true); `getDeviceAttrsInfo` @0x2384088 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart`: `<anonymous closure> in ElectricityUsageHelper::getPriceType` @0x35f72e8 (URL literal only, no `*Http*` call); `getPriceType` @0x35f70c8 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/electricity_price_common/tou_auto_preview/tou_auto_price_pkg_result_logic.dart`: `_getDevicePriceUnit` @0x31acd90 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart`: `getDataFromAPi` @0x2c49144 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart`: `<anonymous closure> in GeneralPriceSettingLogic::getDevicePriceType` @0x29a4e04 (URL literal only, no `*Http*` call); `_getDevicePriceUnit` @0x2a799d0 (encryptionRequestHttp; encrypted: true); `getDevicePriceType` @0x29a4974 (encryptionRequestHttp; encrypted: true); `getPriceTypeUrl` @0x29a4d20 (URL literal only, no `*Http*` call)
- `ev_charger/src/ev_charger/page/home/schedule_charge/network/%20schedule_network.dart`: `_getDeviceAttrs` @0x2851084 (_requestHttp; encrypted: default-true (requestHttp) — verify)
- `micro_hes/src/a17ex/home/components/electricity_price/a17ex_electricity_price_logic.dart`: `_fetchDeviceCurrency` @0x35fe644 (encryptionRequestHttp; encrypted: true)
- `micro_hes/src/common_business/basic_station/module/system_flow/common/energy_system_cover_helper.dart`: `getSolarPvNameMode` @0x2c8d5a0 (encryptionRequestHttp; encrypted: true)
- `settings/src/common/menu_controller/equipment_feed_power_menu_controller.dart`: `getMenuVisible` @0x3691b40 (encryptionRequestHttp; encrypted: true)
- `settings/src/common/menu_controller/feed_grid_menu_controller.dart`: `getMenuVisible` @0x367a224 (encryptionRequestHttp; encrypted: true)
- `settings/src/common/page/feed_grid/feed_grid_controller.dart`: `getDeviceAttrs` @0x2aed8b0 (encryptionRequestHttp; encrypted: true)
- `settings/src/common/page/hardware_feed_grid/hardware_feed_grid_controller.dart`: `getDeviceAttrs` @0x2aeb688 (encryptionRequestHttp; encrypted: true)
- `settings/src/common/page/load_port_setting/load_port_settings_controller.dart`: `getLoadPortConfig` @0x2af7c04 (encryptionRequestHttp; encrypted: true); `getLoadPortName` @0x2af9188 (encryptionRequestHttp; encrypted: true)
- `settings/src/sdk/util/load_port_util.dart`: `updateLoadPortSetting` @0x3291ac0 (encryptionRequestHttp; encrypted: true)
- `settings/src/service/site_settings_service_impl.dart`: `_getDeviceFeedAttributes` @0x3515784 (encryptionRequestHttp; encrypted: true)

Called from: `as200/src/page/home/as200_home_logic.dart::onReady`, `charging/ble/device/anker_device_delegate_impl.dart::a17C1JumpToBleSuccessPage`, `charging/common_bussiness/currency/app_currency_process_list_controller.dart::getDeciceGetCurrency`, `charging/feature/backup_power/back_power_logic.dart::getTimeZone`, `charging/http/http_request_repository.dart::getDeviceAttrs`, `charging/http/http_request_repository.dart::getDeviceAttrsInfo`, `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::_preloadDeviceAttrs`, `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::getMicorLimitData`, `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::getWifiSignal`, `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::onInit`, `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart::_updateGridConnectedInput`, `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart::getPowerLimitList`, `charging/ui/page/device/a17x7/a17x7home/a17x7home_logic.dart::getWifiSignal`, `charging/ui/page/device/a17x8/a17x8home/a17x8home_logic.dart::_getTimingLimit`, `charging/ui/page/device/a17x8/a17x8home/a17x8home_logic.dart::getWifiSignal`, `charging/ui/page/device/a17x8/a17x8scene_start/a17x8scene_start_logic.dart::getLocationTagList`, `charging/ui/page/device/a17x8/space_setup/space_setup_controller.dart::getList`, `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::getSiteInfo`, `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/power_usage_scenario_logic.dart::getTimeZone`, `electricity_price/components/electricity_module/electricity_price_serviceImpl.dart::getPriceType`, `electricity_price/components/electricity_price_common/tou_auto_preview/tou_auto_price_pkg_result_logic.dart::goToReSelectPlan`, `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart::parserRouterInfo`, `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart::updateData`, `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart::changePriceType`, `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart::getDevicePriceType`, `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart::onReady`, `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart::setFixedPriceV2`, `micro_hes/src/a17ex/home/components/electricity_price/a17ex_electricity_price_logic.dart::_initializeDeviceIfAvailable`, `micro_hes/src/common_business/basic_station/dialog/multiple_pv_data.dart::_requestSolarPvNames`, `settings/src/common/menu_controller/equipment_feed_power_menu_controller.dart::onInit`, `settings/src/common/menu_controller/feed_grid_menu_controller.dart::onInit`, `settings/src/common/page/feed_grid/feed_grid_controller.dart::onReady`, `settings/src/common/page/hardware_feed_grid/hardware_feed_grid_controller.dart::onReady`, `settings/src/common/page/load_port_setting/load_port_settings_controller.dart::switchPort`, `settings/src/service/site_settings_service_impl.dart::_sendDefaultParameters`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
