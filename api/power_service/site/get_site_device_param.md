> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_site_device_param

## Purpose

Reads one parameter set of a site: 36 app builders send `site_id` and a `param_type` that selects the set (power-limit, feed-grid, SOC, third-party PV, peak time, country code, and others); [param_types.md](../../param_types.md) owns the `param_type` values, the `cmd` values and the response model of each value.

## Upstream name

`get_device_parm` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/site/get_site_device_param` (asm-traced) at the senders that load a `Method` object next to the URL string (pool entry `pp+0xa7e0`, `Method.post`):

- `PowerUsageScenarioController::_checkPlatformHasSetTOUData` (`power_usage_scenario_controller.dart @0x37b1cc4`): URL string `@0x37b1dc8`, method object `Method.post` (`pp+0xa7e0`) `@0x37b1dc0`.
- `PowerUsageScenarioController::_fetchPowerLimits` (`power_usage_scenario_controller.dart @0x3564988`): URL string `@0x3564f28`, method object `Method.post` (`pp+0xa7e0`) `@0x3564f20`.
- `PowerUsageScenarioController::fetchESeriesFeedGridParams` (`power_usage_scenario_controller.dart @0x2a28750`): URL string `@0x2a28884`, method object `Method.post` (`pp+0xa7e0`) `@0x2a2887c`.
- `HttpRequestControllerImpl::get17C1SiteDeviceParam` (`http_request_repository_impl.dart @0x279d378`): URL string `@0x279d558`, method object `Method.post` (`pp+0xa7e0`) `@0x279d550`.
- `HttpRequestControllerImpl::getCombineBoxListData` (`http_request_repository_impl.dart @0x237a9e0`): URL string `@0x237aaac`, method object `Method.post` (`pp+0xa7e0`) `@0x237aaa4`.
- `HttpRequestControllerImpl::getSafetySocParams` (`http_request_repository_impl.dart @0x2377e5c`): URL string `@0x2377f64`, method object `Method.post` (`pp+0xa7e0`) `@0x2377f5c`.
- `HttpRequestControllerImpl::getSiteDeviceParam` (`http_request_repository_impl.dart @0x2896c30`): URL string `@0x2896d00`, method object `Method.post` (`pp+0xa7e0`) `@0x2896cf8`.
- `HttpRequestControllerImpl::getSiteEnablePeakDeviceParam` (`http_request_repository_impl.dart @0x28f215c`): URL string `@0x28f221c`, method object `Method.post` (`pp+0xa7e0`) `@0x28f2214`.
- `HttpRequestControllerImpl::getSiteGreenModeDeviceParam` (`http_request_repository_impl.dart @0x28f2c2c`): URL string `@0x28f2cec`, method object `Method.post` (`pp+0xa7e0`) `@0x28f2ce4`.
- `HttpRequestControllerImpl::getSiteLowerLimitDeviceParam` (`http_request_repository_impl.dart @0x28f2674`): URL string `@0x28f2734`, method object `Method.post` (`pp+0xa7e0`) `@0x28f272c`.
- `HttpRequestControllerImpl::getSitePeakTimeDeviceParam` (`http_request_repository_impl.dart @0x28f1538`): URL string `@0x28f15f8`, method object `Method.post` (`pp+0xa7e0`) `@0x28f15f0`.
- `HttpRequestControllerImpl::getStationCountryCode` (`http_request_repository_impl.dart @0x237eed8`): URL string `@0x237efa8`, method object `Method.post` (`pp+0xa7e0`) `@0x237efa0`.
- `HttpRequestControllerImpl::getThreePvParam` (`http_request_repository_impl.dart @0x237dc80`): URL string `@0x237dd60`, method object `Method.post` (`pp+0xa7e0`) `@0x237dd58`.
- `FeedGridNewController::getFeedGridParam` (`feed_network_limit_new_logic.dart @0x2aa8c90`): URL string `@0x2aa8dac`, method object `Method.post` (`pp+0xa7e0`) `@0x2aa8da4`.
- `SubLocationListController::getStationCountryCode` (`sub_location_list_controller.dart @0x38ecf1c`): URL string `@0x38ed00c`, method object `Method.post` (`pp+0xa7e0`) `@0x38ed004`.
- `ThirdPvLogic::_getThirdPvFromCloud` (`third_pv_logic.dart @0x35ee8f0`): URL string `@0x35eea14`, method object `Method.post` (`pp+0xa7e0`) `@0x35eea0c`.
- `TouHttpService::getSiteDeviceParam` (`tou_http_service.dart @0x4879544`): URL string `@0x48795c4`, method object `Method.post` (`pp+0xa7e0`) `@0x48795e0`.
- `PowerPlantConfigController::_getMeterTypeAsync` (`power_plant_config_controller.dart @0x3638f00`): URL string `@0x363907c`, method object `Method.post` (`pp+0xa7e0`) `@0x3639074`.
- `PowerPlantConfigController::getGatewayCurrentLimit` (`power_plant_config_controller.dart @0x3638a88`): URL string `@0x3638b8c`, method object `Method.post` (`pp+0xa7e0`) `@0x3638b84`.
- `PowerPlantConfigController::getThirdPv` (`power_plant_config_controller.dart @0x3637d84`): URL string `@0x3637e6c`, method object `Method.post` (`pp+0xa7e0`) `@0x3637e64`.
- `SystemConfigController::getThirdPv` (`system_config_controller.dart @0x364d850`): URL string `@0x364d924`, method object `Method.post` (`pp+0xa7e0`) `@0x364d91c`.
- `A17E2StationLogic::_getFeedGridConfig` (`a17e2_station_logic.dart @0x233e8c0`): URL string `@0x233eaa8`, method object `Method.post` (`pp+0xa7e0`) `@0x233eaa0`.
- `SystemA17E2FlowChartLogic::_fetchThirdPvConnectType` (`system_a17e2_flow_chart_logic.dart @0x3560e88`): URL string `@0x3560ff0`, method object `Method.post` (`pp+0xa7e0`) `@0x3560fe8`.
- `GatewayCurrentLimitMenuController::_loadCurrentLimit` (`gateway_current_limit_menu_controller.dart @0x36836d8`): URL string `@0x3683808`, method object `Method.post` (`pp+0xa7e0`) `@0x3683800`.
- `MonitoringDeviceMenuController::_loadCurrentMeterType` (`monitoring_device_menu_controller.dart @0x2cf3ae0`): URL string `@0x2cf3c10`, method object `Method.post` (`pp+0xa7e0`) `@0x2cf3c08`.
- `EvChargerSettingController::getSettingInfo` (`ev_charger_setting_controller.dart @0x2aed370`): URL string `@0x2aed490`, method object `Method.post` (`pp+0xa7e0`) `@0x2aed488`.
- `FeedGridController::getFeedGridParam` (`feed_grid_controller.dart @0x2aedeb8`): URL string `@0x2aedfe4`, method object `Method.post` (`pp+0xa7e0`) `@0x2aedfdc`.
- `HardwareFeedGridController::getFeedGridParam` (`hardware_feed_grid_controller.dart @0x2aecf90`): URL string `@0x2aed0a4`, method object `Method.post` (`pp+0xa7e0`) `@0x2aed09c`.
- `HeatPumpSettingController::getHeatPumpParam` (`heat_pump_setting_controller.dart @0x2af6630`): URL string `@0x2af6754`, method object `Method.post` (`pp+0xa7e0`) `@0x2af674c`.
- `StationAdvancedSettingController::_getGridOverloadAutoReduceSetting` (`station_advanced_setting_controller.dart @0x2a78b08`): URL string `@0x2a78c1c`, method object `Method.post` (`pp+0xa7e0`) `@0x2a78c14`.
- `StationPeakShavingController::getPeakShavingSetting` (`station_peak_shaving_controller.dart @0x2af9e24`): URL string `@0x2af9f80`, method object `Method.post` (`pp+0xa7e0`) `@0x2af9f78`.
- `StationPeakShavingController::getSocSetting` (`station_peak_shaving_controller.dart @0x2afab38`): URL string `@0x2afac4c`, method object `Method.post` (`pp+0xa7e0`) `@0x2afac44`.
- `GridConnectUtil::fetchSiteGridPowerList` (`grid_connect_util.dart @0x2af5dfc`): URL string `@0x2af5f58`, method object `Method.post` (`pp+0xa7e0`) `@0x2af5f50`.
- `GridConnectUtil::getGroupedOutputPowerSum` (`grid_connect_util.dart @0x2aee464`): URL string `@0x2aee5a0`, method object `Method.post` (`pp+0xa7e0`) `@0x2aee598`.
- `StationSocDataSource::query` (`station_soc_data_source.dart @0x2afe7a0`): URL string `@0x2afe8e4`, method object `Method.post` (`pp+0xa7e0`) `@0x2afe8dc`.
- `ElectricityUsageHelper::getCurEmsModeType` (`electricity_usage_helper.dart @0x292e1f4`): URL string `@0x292e3a0` without a `Method` object next to it; the method of this sender was not read.

Further senders reach the same URL without a `Method` pool object in the call setup: the IoT-kit sender `SocCommandCapabilityV2::fetchSocSetting` (`soc_command_capability_v2.dart @0x3677fc4`) puts the path string (`@0x36780b4`) and the string literal `"POST"` (`@0x36780cc`) into a command map for `akIoTKitManager.handle`, and the other URL-literal-only sites listed under Callers in app (`HttpHelper::getDataFromService` users) were not read.

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

All 36 listed builders build the body as a map literal (or `[]=` calls); the first two keys are the same everywhere. The values and the set of senders are not repeated here: the `param_type` strings and the `cmd` constants per sender are owned by [param_types.md](../../param_types.md).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | string | yes | `"<site_id>"` | in 29 builders the map is typed `<String, String>` or `<String, String?>` (so the value is a String), e.g. `fetchESeriesFeedGridParams` (`power_usage_scenario_controller.dart`, key `@0x2a287e4`, store `@0x2a287f4`, type arguments `@0x2a28810`) and `getSafetySocParams` (`http_request_repository_impl.dart`, key `@0x2377eec`, store `@0x2377efc`, type arguments `@0x2377f18`); the remaining 7 builders (`<String, Object>`, `<String, Object?>` or `<String, dynamic>`) store a parameter or field whose type was not read |
| `param_type` | string | yes | `"6"` | a string literal in 33 builders, e.g. `"6"` in `_checkPlatformHasSetTOUData` (key `@0x37b1d50`, literal `@0x37b1d5c`, store `@0x37b1d64`); in `get17C1SiteDeviceParam` (`@0x279d494`) and in `getSiteDeviceParam` (`@0x2896ca0`) the value is a parameter, type not read |
| `cmd` | int (Smi, w) | optional | | present in 5 builders only (`_checkPlatformHasSetTOUData` `ak_soft_ems/ems_list/power_usage_scenario_controller.dart @0x37b1d68`, `_fetchPowerLimits` `@0x3564ea4`, `get17C1SiteDeviceParam` `charging/http/http_request_repository_impl.dart @0x279d4a8`, `getThreePvParam` `@0x237dd00`, `TouHttpService::getSiteDeviceParam` `electricity_price/components/tou/impl_v2/service/tou_http_service.dart @0x487959c`); the constant is stored with `stur w16`; its value is owned by [param_types.md](../../param_types.md) |
| `device_sn` | string | optional | | `_fetchPowerLimits` (literal empty string, key `ak_soft_ems/ems_list/power_usage_scenario_controller.dart @0x3564eb8`, literal `@0x3564ec4`) and `get17C1SiteDeviceParam` (key `charging/http/http_request_repository_impl.dart @0x279d4bc`, null default `""`) |
| `parallel_type` | ? | optional | | `_fetchPowerLimits` (key `ak_soft_ems/ems_list/power_usage_scenario_controller.dart @0x3564ecc`) and `get17C1SiteDeviceParam` (key `charging/http/http_request_repository_impl.dart @0x279d4e8`); value not read |
| `path`, `method`, `param.site_id`, `param.param_type` | ? | | | keys of the IoT-kit command map of `fetchSocSetting` (`device/src/setting/controller/soc_settings_v2/soc_command_capability_v2.dart @0x36780ac`..`@0x36780e0`); `method` is the literal `"POST"`; the `param` map was not read |

`ElectricityUsageHelper::getCurEmsModeType` (`electricity_usage_helper.dart @0x292e1f4`) builds its body with `[]=` calls (`site_id` `@0x292e3d0`, `device_sn` `@0x292e448`, `station_id` `@0x292e4dc`) on a `<String, dynamic>` map; values were not read.

The earlier extractor rows `feed_switch`, `feed_times` and `feed_upper_limit` are not request keys: in `A17E2StationLogic::_getFeedGridConfig` (`a17e2_station_logic.dart @0x233e8c0`) they sit in a separate `<String, dynamic>` map (`@0x233e9d0`) stored into the closure context (`@0x233e9e0`) next to the request map `{site_id, param_type: "28"}` (`<String, String>`, `@0x233ea5c`).

## `param_type`/`cmd`

see `api/param_types.md`

param_type is a variable at this sender (traced by heuristic — verify against the callers in `data/param_types.json`).

## Response model (link)

Per sender; see [param_types.md](../../param_types.md) for the model of each `param_type`. Builder-side `fromJson` parses were read in the sender list: `SiteConsumptionStrategyModel`, `CombineBoxEntity`, `GetSiteDeviceParamResponse`, `SiteHomeLoadModel`, `PeakTimeModel`, `SiteDeviceParamData`, `FeedGridSettingParam`, `HwFeedGridSettingParam`, `HeatPumpParam`, `GridOverloadAutoReduceParam`, `PeakShavingSettingParam`, `SocSettingParam`, `AddDeviceModel` and `EmsModeModel` appear as `response_key` of single senders in `tools/out/request_fields_all.json`; 21 senders have no model attributed. These attributions were not re-read for this page.

## Response

The response fields depend on `param_type` and are owned by the model pages linked from [param_types.md](../../param_types.md).

## Example request/response

Request, synthesized (decrypted body of `getSafetySocParams`)

```json
{"site_id": "<site_id>", "param_type": "18"}
```

## Errors seen

None traced for this page as a whole; the senders' failure callbacks were not read. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `ak_soft_ems/ems_list/power_usage_scenario_controller.dart`: `_checkPlatformHasSetTOUData` @0x37b1cc4 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`); `_fetchPowerLimits` @0x3564988 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`); `fetchESeriesFeedGridParams` @0x2a28750 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `charging/http/http_request_repository_impl.dart`: `get17C1SiteDeviceParam` @0x279d378 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`); `getCombineBoxListData` @0x237a9e0 (requestHttp; encrypted: default-true (requestHttp) — verify, param_type/cmd: see `api/param_types.md`); `getSafetySocParams` @0x2377e5c (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`); `getSiteDeviceParam` @0x2896c30 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`); `getSiteEnablePeakDeviceParam` @0x28f215c (requestHttp; encrypted: default-true (requestHttp) — verify, param_type/cmd: see `api/param_types.md`); `getSiteGreenModeDeviceParam` @0x28f2c2c (requestHttp; encrypted: default-true (requestHttp) — verify, param_type/cmd: see `api/param_types.md`); `getSiteLowerLimitDeviceParam` @0x28f2674 (requestHttp; encrypted: default-true (requestHttp) — verify, param_type/cmd: see `api/param_types.md`); `getSitePeakTimeDeviceParam` @0x28f1538 (requestHttp; encrypted: default-true (requestHttp) — verify, param_type/cmd: see `api/param_types.md`); `getStationCountryCode` @0x237eed8 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`); `getThreePvParam` @0x237dc80 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/feed_network_limit_new/feed_network_limit_new_logic.dart`: `getFeedGridParam` @0x2aa8c90 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `device/src/setting/controller/location/sub_page/list/sub_location_list_controller.dart`: `getStationCountryCode` @0x38ecf1c (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `device/src/setting/controller/soc_settings_v2/soc_command_capability_v2.dart`: `fetchSocSetting` @0x3677fc4 (URL literal only, no `*Http*` call; sends in the same function (`AKIoTKitManagerImpl::handle`); resolved from the URL literal at `device/src/setting/controller/soc_settings_v2/soc_command_capability_v2.dart @0x36780b4` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `device/src/station_setting/controller/common_third_pv/page/third_pv_logic.dart`: `_getThirdPvFromCloud` @0x35ee8f0 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)
- `electricity_price/components/electricity_module/page/tou_and_timeslot_settings_detail_logic.dart`: `queryMediumChargingDeviceHasSetMode` @0x29b0b28 (URL literal only, no `*Http*` call; sender `HttpHelper::getDataFromService` (`electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bda38`) (HTTP helper wrapper), called from the same function; resolved from the URL literal at `electricity_price/components/electricity_module/page/tou_and_timeslot_settings_detail_logic.dart @0x29b0bf4` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `electricity_price/components/electricity_module/page/tou_and_timeslot_settings_poly_logic.dart`: `queryMediumChargingDeviceHasSetMode` @0x29b0c8c (URL literal only, no `*Http*` call; sender `HttpHelper::getDataFromService` (`electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bda38`) (HTTP helper wrapper), called from the same function; resolved from the URL literal at `electricity_price/components/electricity_module/page/tou_and_timeslot_settings_poly_logic.dart @0x29b0d54` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart`: `<anonymous closure> in ElectricityUsageHelper::getCurEmsModeType` @0x292e774 (URL literal only, no `*Http*` call; sends in the same function (`HttpServiceImpl::encryptionRequestHttp`); resolved from the URL literal at `electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x292e7a4` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md)); `<anonymous closure> in ElectricityUsageHelper::getManualSetTOUDetailWithUrl` @0x2c4fdfc (URL literal only, no `*Http*` call; sends in the same function (`HttpServiceImpl::encryptionRequestHttp`); resolved from the URL literal at `electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x2c4fedc` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md)); `assembleRemoteApiParametersWidthGetDetail` @0x2c4f694 (URL literal only, no `*Http*` call; no sender within 3 caller levels); `getCurEmsModeType` @0x292e1f4 (encryptionRequestHttp; encrypted: true); `getElectricityUsagePolicyUrl` @0x292e5e8 (URL literal only, no `*Http*` call; sender `ElectricityUsageHelper::getCurEmsModeType` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x292e1f4`), reached through callers `ElectricityUsageHelper::getCurEmsModeType` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x292e1f4`); resolved from the URL literal at `electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x292e628` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
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
- `electricity_price/components/tou/impl_v2/repository/medium_tou_repository.dart::getTouDetail`
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
- `settings/src/common/page/feed_grid/feed_grid_controller.dart::_resolveDefaultPower`
- `settings/src/common/page/feed_grid/feed_grid_controller.dart::onReady`
- `settings/src/common/page/grid_connected_settings/grid_connected_settings_controller.dart::_fetchSiteGridPowerParam`
- `settings/src/common/page/hardware_feed_grid/hardware_feed_grid_controller.dart::onReady`
- `settings/src/common/page/heat_pump/heat_pump_setting_controller.dart::onReady`
- `settings/src/common/page/station_advanced_setting/station_advanced_setting_controller.dart::onReady`
- `settings/src/common/station_page/station_peak_shaving/station_peak_shaving_controller.dart::onReady`
- `soc/soc_setting/soc_setting_logic.dart::_querySiteDeviceParam`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. `tools/out/diff_3.18.0_3.24.3.md` lists `feed_switch`, `feed_times`, `feed_upper_limit` and `method`, `param.param_type`, `param.site_id`, `path` as added keys and `param_type` values 24, 25, 27, 28, 29, 30, 31, 32, 34, 35, 37 as added. The `feed_*` keys are not request keys (see Request); `method`, `param.*` and `path` are the key names of the IoT-kit command map.

## Known unknowns

- Per-sender response handling: the model attributions of the extractor were not re-read here, and 21 of 36 senders have none. Header stays string-only. — traced 2026-10-20: not decoded in this pass (36 senders); the reason given in the bullet stands
- Types of `site_id` in the 7 builders whose map is `<String, Object>`, `<String, Object?>` or `<String, dynamic>`, and of `param_type` in `get17C1SiteDeviceParam` and `getSiteDeviceParam`. — attempted 2026-10-20 (two-hop not readable: seven builders with `<String, Object>` / `<String, Object?>` / `<String, dynamic>` maps; callers not followed in this pass. Header stays string-only)
- The URL-literal-only senders (`HttpHelper::getDataFromService` users, `ElectricityUsageHelper` closures) and `parallel_type` values were not read. — traced 2026-10-20: not decoded in this pass (URL-literal-only senders); the reason given in the bullet stands
- Whether the server accepts a missing `cmd` (most builders omit it): not derivable from the app.

## Device-tested by

none
