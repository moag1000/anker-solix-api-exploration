> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_site_device_param

## Purpose

<!-- TODO -->

## Upstream name

`get_device_parm` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/site/get_site_device_param`, method: not extracted by the inventory <!-- TODO -->; string-only: `ak_soft_ems/ems_list/power_usage_scenario_controller.dart @0x2a28884`
(literal also at 42 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `ak_soft_ems/ems_list/power_usage_scenario_controller.dart @0x37b1cc4` |
| `param_type` | ? | ? | ? | `ak_soft_ems/ems_list/power_usage_scenario_controller.dart @0x37b1cc4` |
| `cmd` | ? | ? | ? | `ak_soft_ems/ems_list/power_usage_scenario_controller.dart @0x37b1cc4` |
| `device_sn` | ? | ? | ? | `ak_soft_ems/ems_list/power_usage_scenario_controller.dart @0x3564988` |
| `parallel_type` | ? | ? | ? | `ak_soft_ems/ems_list/power_usage_scenario_controller.dart @0x3564988` |
| `path` | ? | ? | ? | `device/src/setting/controller/soc_settings_v2/soc_command_capability_v2.dart @0x3677fc4` |
| `param.site_id` | ? | ? | ? | `device/src/setting/controller/soc_settings_v2/soc_command_capability_v2.dart @0x3677fc4` |
| `param.param_type` | ? | ? | ? | `device/src/setting/controller/soc_settings_v2/soc_command_capability_v2.dart @0x3677fc4` |
| `feed_switch` | ? | ? | ? | `micro_hes/src/a17e2/station/home/a17e2_station_logic.dart @0x233e8c0` |
| `feed_times` | ? | ? | ? | `micro_hes/src/a17e2/station/home/a17e2_station_logic.dart @0x233e8c0` |
| `feed_upper_limit` | ? | ? | ? | `micro_hes/src/a17e2/station/home/a17e2_station_logic.dart @0x233e8c0` |

Rows are the union over 38 senders; `source` is the first sender that sets the key.

## `param_type`/`cmd`

see `api/param_types.md`

param_type is a variable at this sender (traced by heuristic — verify against the callers in `data/param_types.json`).

## Response model (link)

<!-- TODO -->

## Response

<!-- TODO -->

## Example request/response

<!-- TODO -->

## Errors seen

`api/errors.md`: <!-- TODO -->

## Callers in app

- `ak_soft_ems/ems_list/power_usage_scenario_controller.dart`: `_checkPlatformHasSetTOUData` @0x37b1cc4 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`); `_fetchPowerLimits` @0x3564988 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`); `fetchESeriesFeedGridParams` @0x2a28750 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `charging/http/http_request_repository_impl.dart`: `get17C1SiteDeviceParam` @0x279d378 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`); `getCombineBoxListData` @0x237a9e0 (requestHttp; encrypted: default-true (requestHttp) — verify, param_type/cmd: see `api/param_types.md`); `getSafetySocParams` @0x2377e5c (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`); `getSiteDeviceParam` @0x2896c30 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`); `getSiteEnablePeakDeviceParam` @0x28f215c (requestHttp; encrypted: default-true (requestHttp) — verify, param_type/cmd: see `api/param_types.md`); `getSiteGreenModeDeviceParam` @0x28f2c2c (requestHttp; encrypted: default-true (requestHttp) — verify, param_type/cmd: see `api/param_types.md`); `getSiteLowerLimitDeviceParam` @0x28f2674 (requestHttp; encrypted: default-true (requestHttp) — verify, param_type/cmd: see `api/param_types.md`); `getSitePeakTimeDeviceParam` @0x28f1538 (requestHttp; encrypted: default-true (requestHttp) — verify, param_type/cmd: see `api/param_types.md`); `getStationCountryCode` @0x237eed8 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`); `getThreePvParam` @0x237dc80 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/feed_network_limit_new/feed_network_limit_new_logic.dart`: `getFeedGridParam` @0x2aa8c90 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `device/src/setting/controller/location/sub_page/list/sub_location_list_controller.dart`: `getStationCountryCode` @0x38ecf1c (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `device/src/setting/controller/soc_settings_v2/soc_command_capability_v2.dart`: `fetchSocSetting` @0x3677fc4 (URL literal only, no `*Http*` call)
- `device/src/station_setting/controller/common_third_pv/page/third_pv_logic.dart`: `_getThirdPvFromCloud` @0x35ee8f0 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `electricity_price/components/electricity_module/page/tou_and_timeslot_settings_detail_logic.dart`: `queryMediumChargingDeviceHasSetMode` @0x29b0b28 (URL literal only, no `*Http*` call)
- `electricity_price/components/electricity_module/page/tou_and_timeslot_settings_poly_logic.dart`: `queryMediumChargingDeviceHasSetMode` @0x29b0c8c (URL literal only, no `*Http*` call)
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart`: `<anonymous closure> in ElectricityUsageHelper::getCurEmsModeType` @0x292e774 (URL literal only, no `*Http*` call); `<anonymous closure> in ElectricityUsageHelper::getManualSetTOUDetailWithUrl` @0x2c4fdfc (URL literal only, no `*Http*` call); `assembleRemoteApiParametersWidthGetDetail` @0x2c4f694 (URL literal only, no `*Http*` call); `getCurEmsModeType` @0x292e1f4 (encryptionRequestHttp; encrypted: true); `getElectricityUsagePolicyUrl` @0x292e5e8 (URL literal only, no `*Http*` call)
- `electricity_price/components/tou/impl_v2/service/tou_http_service.dart`: `getSiteDeviceParam` @0x4879544 (request; encrypted: default-true (requestHttp) — verify, param_type/cmd: see `api/param_types.md`)
- `flutter_charging_beginning/beginning/state_cards/settings/power_plant_config_controller.dart`: `_getMeterTypeAsync` @0x3638f00 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`); `getGatewayCurrentLimit` @0x3638a88 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`); `getThirdPv` @0x3637d84 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `flutter_charging_beginning/beginning/state_cards/settings/system_config/system_config_controller.dart`: `getThirdPv` @0x364d850 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `micro_hes/src/a17e2/station/home/a17e2_station_logic.dart`: `_getFeedGridConfig` @0x233e8c0 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart`: `_fetchThirdPvConnectType` @0x3560e88 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `settings/src/common/menu_controller/gateway_current_limit_menu_controller.dart`: `_loadCurrentLimit` @0x36836d8 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `settings/src/common/menu_controller/monitoring_device_menu_controller.dart`: `_loadCurrentMeterType` @0x2cf3ae0 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `settings/src/common/page/ev_charger/ev_charger_setting_controller.dart`: `getSettingInfo` @0x2aed370 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `settings/src/common/page/feed_grid/feed_grid_controller.dart`: `getFeedGridParam` @0x2aedeb8 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `settings/src/common/page/hardware_feed_grid/hardware_feed_grid_controller.dart`: `getFeedGridParam` @0x2aecf90 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `settings/src/common/page/heat_pump/heat_pump_setting_controller.dart`: `getHeatPumpParam` @0x2af6630 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `settings/src/common/page/station_advanced_setting/station_advanced_setting_controller.dart`: `_getGridOverloadAutoReduceSetting` @0x2a78b08 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `settings/src/common/station_page/station_peak_shaving/station_peak_shaving_controller.dart`: `getPeakShavingSetting` @0x2af9e24 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`); `getSocSetting` @0x2afab38 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `settings/src/sdk/util/grid_connect_util.dart`: `fetchSiteGridPowerList` @0x2af5dfc (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`); `getGroupedOutputPowerSum` @0x2aee464 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `soc/soc_setting/station_soc_data_source.dart`: `query` @0x2afe7a0 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)

Called from:

- `ak_soft_ems/ems_list/power_usage_scenario_controller.dart::handleItemToggle`
- `ak_soft_ems/ems_list/power_usage_scenario_controller.dart::onInit`
- `ak_soft_ems/ems_list/power_usage_scenario_controller.dart::onReady`
- `charging/http/http_request_repository.dart::get17C1SiteDeviceParam`
- `charging/http/http_request_repository.dart::getCombineBoxListData`
- `charging/http/http_request_repository.dart::getSafetySocParams`
- `charging/http/http_request_repository.dart::getSiteDeviceParam`
- `charging/http/http_request_repository.dart::getSiteEnablePeakDeviceParam`
- `charging/http/http_request_repository.dart::getSiteGreenModeDeviceParam`
- `charging/http/http_request_repository.dart::getSiteLowerLimitDeviceParam`
- `charging/http/http_request_repository.dart::getSitePeakTimeDeviceParam`
- `charging/http/http_request_repository.dart::getStationCountryCode`
- `charging/impl/http_service_impl.dart::get17C1SiteDeviceParam`
- `charging/ui/page/device/a1782/a1782_setting/locale_settings/locale_settings_list_controller.dart::LocaleSettingsListController`
- `charging/ui/page/device/a1782/station/electricity_scene/a1782_electricity_scene_logic.dart::_getSiteConfig`
- `charging/ui/page/device/a1782/station/electricity_scene/a1782_electricity_scene_logic.dart::next`
- `charging/ui/page/device/a1782/station/setting/menu_controller/station_locale_settings_controller.dart::getStationLocale`
- `charging/ui/page/device/a1782/station/system_policy/a1782_system_policy_logic.dart::_getSystemPolicySetting`
- `charging/ui/page/device/a1782/station/system_policy/a1782_system_policy_logic.dart::setBatteryReserve`
- `charging/ui/page/device/a1782/station/system_policy/a1782_system_policy_logic.dart::setMode`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::setSelfUseMode`
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart::getCombinerBoxInfo`
- `charging/ui/page/device/a17c1/energy_plan/energy_plan_logic.dart::getHomeLoadSiteParam`
- `charging/ui/page/device/a17c1/open_process/open_process_logic.dart::getSiteHomeLoad`
- `charging/ui/page/device/a17c1/open_process/open_process_logic.dart::mainDeviceJoin`
- `charging/ui/page/device/a17c5/ai_mode_condition/ai_mode_condition_logic.dart::getSiteDataAuth`
- `charging/ui/page/device/greenpower/recharge/recharge_logic.dart::getSiteDeviceParamData`
- `charging/ui/page/device/greenpower/recharge/recharge_logic.dart::getSiteEnablePeak`
- `charging/ui/page/device/greenpower/recharge/recharge_logic.dart::getSiteGreenMode`
- `charging/ui/page/device/greenpower/recharge/recharge_logic.dart::getSiteLowerLimit`
- `charging/ui/page/device/greenpower/recharge/recharge_logic.dart::getSitePeakTimeDevice`
- `charging/ui/page/device/main/sitation_energy_mian/energy_home/controller/energy_home_controller.dart::getHomeLoadSiteDeviceParam`
- `charging/ui/page/device/main/sitation_energy_mian/energy_home/controller/energy_home_controller.dart::getSiteHomeLoadData`
- `charging/ui/page/device/main/sitation_energy_mian/energy_pps/controller/energy_pps_controller.dart::getSiteEnablePeak`
- `charging/ui/page/device/main/sitation_energy_mian/energy_pps/controller/energy_pps_controller.dart::getSiteGreenMode`
- `charging/ui/page/device/main/sitation_energy_mian/energy_pps/controller/energy_pps_controller.dart::getSiteLowerLimit`
- `charging/ui/page/device/main/sitation_energy_mian/energy_pps/controller/energy_pps_controller.dart::getSitePeakTimeDevice`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::_updateSafetySocStatus`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::checkIfNeedShowSetLocaleDialog`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::fetchThirdPvSetting`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::getSiteHomeLoad`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::getSiteInfo`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::hasAE100FeederStatusChange`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::updateEquipmentFeedNetworkStatus`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/add_devices_progress/add_devices_progress_logic.dart::emetySiteSitePramar`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/add_devices_progress/add_devices_progress_logic.dart::multiAddDevices`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/chargers_management/chargers_manage_logic.dart::getInitSwitchStatus`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/feed_network_limit/feed_network_limit_logic.dart::getFeedLimitStatus`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/feed_network_limit_new/feed_network_limit_new_logic.dart::onReady`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/manage_devices/manage_devices_logic.dart::getCombineBoxList`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/merge_system_energy/merge_system_energy_plan_logic.dart::getHomeLoadSiteParam`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/power_usage_scenario_logic.dart::_getMinCutoffPowerBySiteId`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/power_usage_scenario_logic.dart::_refreshScheduleModeStatus`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/power_usage_scenario_logic.dart::getHomeLoadSiteParam`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/power_usage_scenario_logic.dart::getSiteDataAuth`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/station_home_settings_logic.dart::updateSafetySocAndFeedNetworkStatus`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/utility_rate_plan/site_utility_rate_plan_logic.dart::getSiteTOUParams`
- `charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart::getSiteEnablePeak`
- `charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart::getSiteGreenMode`
- `charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart::getSiteLowerLimit`
- `charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart::getSitePeakTimeDevice`
- `charging/ui/page/device/main/station_device_home/station_set_time/station_set_time_logic.dart::getSiteGreenMode`
- `charging/ui/page/device/main/station_device_home/station_set_time/station_set_time_logic.dart::getSitePeakTimeDevice`
- `device/src/setting/controller/location/sub_page/list/sub_location_list_controller.dart::SubLocationListController`
- `device/src/station_setting/controller/common_third_pv/page/third_pv_logic.dart::_loadCurrentPvType`
- `device/src/station_setting/controller/station_soc_settings_v2/station_soc_settings_v2_controller.dart::getSocSetting`
- `electricity_price/components/electricity_module/electricity_price_serviceImpl.dart::getCurEmsModeType`
- `electricity_price/components/electricity_module/page/tou_and_timeslot_settings_detail_logic.dart::onReady`
- `electricity_price/components/electricity_module/page/tou_and_timeslot_settings_poly_logic.dart::onReady`
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart::getCurEmsModeType`
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart::getManualSetTOUDetail`
- `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart::onReady`
- `flutter_charging_beginning/beginning/state_cards/settings/power_plant_config_controller.dart::checkATSInstalled`
- `flutter_charging_beginning/beginning/state_cards/settings/power_plant_config_controller.dart::onInit`
- `flutter_charging_beginning/beginning/state_cards/settings/system_config/system_config_controller.dart::onInit`
- `micro_hes/src/a17e2/station/home/a17e2_station_logic.dart::updateFeeder0w`
- `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart::_setupEventBusListener`
- `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart::onInit`
- `settings/src/common/menu_controller/gateway_current_limit_menu_controller.dart::onInit`
- `settings/src/common/menu_controller/monitoring_device_menu_controller.dart::_navigateToMonitoringDevicePage`
- `settings/src/common/menu_controller/monitoring_device_menu_controller.dart::onInit`
- `settings/src/common/page/ev_charger/ev_charger_setting_controller.dart::onReady`
- `settings/src/common/page/feed_grid/feed_grid_controller.dart::onReady`
- `settings/src/common/page/hardware_feed_grid/hardware_feed_grid_controller.dart::onReady`
- `settings/src/common/page/heat_pump/heat_pump_setting_controller.dart::onReady`
- `settings/src/common/page/station_advanced_setting/station_advanced_setting_controller.dart::onReady`
- `settings/src/common/station_page/station_peak_shaving/station_peak_shaving_controller.dart::onReady`
- `soc/soc_setting/soc_setting_logic.dart::_querySiteDeviceParam`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
