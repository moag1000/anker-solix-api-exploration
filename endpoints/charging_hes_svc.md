# Charging Hes Svc

> 28 function calls, 28 unique endpoints
>
> **Source**: Regenerated from ENDPOINT_FIELDS.md (authoritative reference)

## `/charging_hes_svc/adjust_station_price_unit`

- **changePriceUnit**(`station_id?, price_unit`)

## `/charging_hes_svc/check_function`

- **checkFunction**(`station_id?`) → `CheckFunctionModel`

## `/charging_hes_svc/deal_share_data`

- **agreeOrRefuseVppDisclaimer**(`sn?, action`)

## `/charging_hes_svc/device_command`

- **sendDeviceCommand**(`station_id?, main_sn, time, electricity_strategy?, add_diesel?, screen_setting?, utility_rate_plan?, ack_peak_valley?, advanced_setting, heat_pump_setting?, accuracy?, cls_reset, off_grid_switching, evcharger_setting?, version?`)

## `/charging_hes_svc/get_aiems_profit`

- **queryLargeChargerAiEmsProfit**(`*(none extracted)*`) → `LargeChargerAiEmsProfit`

## `/charging_hes_svc/get_auto_disaster_prepare_detail`

- **getAutoDisasterPrepareDetail**(`station_id?, unix, near_field?`) → `AutoDisasterDetailModel`

## `/charging_hes_svc/get_auto_disaster_prepare_status`

- **getAutoDisasterPrepareStatus**(`station_id?`) → `AutoDisasterPrepareStatusModel`

## `/charging_hes_svc/get_current_disaster_prepare_details`

- **getCurrentDisasterPrepareDetails**(`*(none extracted)*`) → `DisasterPrepareDetailsModel`

## `/charging_hes_svc/get_device_command`

- **getDeviceCommand**(`station_id?, accuracy`) → `A5101DeviceCommandModel`

## `/charging_hes_svc/get_device_product_info`

- **getHesDeviceIcons**(`*(none extracted)*`) → `HesProductsInfoModel`

## `/charging_hes_svc/get_heat_pump_plan_json`

- **getHeatPumpTimePlan**(`heat_pump_plan?`)

## `/charging_hes_svc/get_hes_dev_info`

- **getHesDeviceList**(`*(none extracted)*`) → `A5101DeviceListModel`

## `/charging_hes_svc/get_install_info`

- **getDeviceInstallAddress**(`*(none extracted)*`) → `A5101InstallAddressModel`

## `/charging_hes_svc/get_installer_info`

- **getInstallerInfo**(`*(none extracted)*`) → `A5101InstallInformationModel`

## `/charging_hes_svc/get_station_config_and_status`

- **getA5101StationConfigDetail**(`station_id?`) → `A5101StationGridConfigModel`

## `/charging_hes_svc/get_station_evchargers`

- **getX1BindChargerList**(`station_id?`)

## `/charging_hes_svc/get_system_running_time`

- **getDeviceRunTime**(`station_id?`)

## `/charging_hes_svc/get_user_bind_and_not_in_station_evchargers`

- **getX1BindUserUnbindChargerList**(`*(none extracted)*`) → `A5101EvChargerListModel`

## `/charging_hes_svc/get_vpp_check_code`

- **getVppInfo**(`station_id?, get_code, current_version`) → `VppInfoModel`

## `/charging_hes_svc/get_vpp_service_policy_by_agg_user`

- **getVppDisclaimer**(`current_version?`)

## `/charging_hes_svc/get_world_monetary_unit`

- **getPriceUnits**(`station_id?`)

## `/charging_hes_svc/quit_auto_disaster_prepare`

- **quitAutoDisasterPrepare**(`station_id?, unix, far_field?`) → `AutoDisasterQuitPrepareModel`

## `/charging_hes_svc/restart_peak_session`

- **deleteAndRestartPeakValley**(`station_id?, far_field_model`)

## `/charging_hes_svc/set_station_evchargers`

- **bindUnX1Charger**(`stationId?, evChargers, deleteFlag?, forceBindFlag?`)
  - ⚠️ Uses **camelCase** field names

## `/charging_hes_svc/update_hes_utility_rate_plan`

- **updatePeakAndValley**(`siteId?, peakValleyPriceSeason`)
  - ⚠️ Uses **camelCase** field names
  - This is a HES-specific endpoint, NOT a `set_site_device_param` wrapper

## `/charging_hes_svc/update_wifi_config`

- **updateWiFiConfig**(`ssid?, sn, rssi, encryption`)

## `/charging_hes_svc/user_event_alarm`

- **reportHesEvents**(`station_id?, pn, language, event`) → `A5101EventsSetModel`

## `/charging_hes_svc/user_fault_alarm`

- **sendDeviceReport**(`station_id?`)
