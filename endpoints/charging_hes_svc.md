# Charging Hes Svc

> 28 function calls, 28 unique endpoints

## `/charging_hes_svc/adjust_station_price_unit`

- **changePriceUnit**(`sn, action`)

## `/charging_hes_svc/check_function`

- **checkFunction**(`list`) → `CheckFunctionModel`

## `/charging_hes_svc/deal_share_data`

- **agreeOrRefuseVppDisclaimer**(`*(no params extracted)*`)

## `/charging_hes_svc/device_command`

- **sendDeviceCommand**(`*(no params extracted)*`)

## `/charging_hes_svc/get_aiems_profit`

- **queryLargeChargerAiEmsProfit**(`site_id`) → `LargeChargerAiEmsProfit`

## `/charging_hes_svc/get_auto_disaster_prepare_detail`

- **getAutoDisasterPrepareDetail**(`banner_id, handle_type`) → `AutoDisasterDetailModel`

## `/charging_hes_svc/get_auto_disaster_prepare_status`

- **getAutoDisasterPrepareStatus**(`*(no params extracted)*`) → `AutoDisasterPrepareStatusModel`

## `/charging_hes_svc/get_current_disaster_prepare_details`

- **getCurrentDisasterPrepareDetails**(`station_id, price_unit`) → `DisasterPrepareDetailsModel`

## `/charging_hes_svc/get_device_command`

- **getDeviceCommand**(`site_id, pps_list`) → `A5101DeviceCommandModel`

## `/charging_hes_svc/get_device_product_info`

- **getHesDeviceIcons**(`version`) → `HesProductsInfoModel`

## `/charging_hes_svc/get_heat_pump_plan_json`

- **getHeatPumpTimePlan**(`*(no params extracted)*`)

## `/charging_hes_svc/get_hes_dev_info`

- **getHesDeviceList**(`*(no params extracted)*`) → `A5101DeviceListModel`

## `/charging_hes_svc/get_install_info`

- **getDeviceInstallAddress**(`*(no params extracted)*`) → `A5101InstallAddressModel`

## `/charging_hes_svc/get_installer_info`

- **getInstallerInfo**(`current_version`) → `A5101InstallInformationModel`

## `/charging_hes_svc/get_station_config_and_status`

- **getA5101StationConfigDetail**(`site_id, param_type=20, cmd, param_data`) → `A5101StationGridConfigModel`

## `/charging_hes_svc/get_station_evchargers`

- **getX1BindChargerList**(`*(no params extracted)*`)

## `/charging_hes_svc/get_system_running_time`

- **getDeviceRunTime**(`*(no params extracted)*`)

## `/charging_hes_svc/get_user_bind_and_not_in_station_evchargers`

- **getX1BindUserUnbindChargerList**(`*(no params extracted)*`) → `A5101EvChargerListModel`

## `/charging_hes_svc/get_vpp_check_code`

- **getVppInfo**(`android, anker_power, param_types`) → `GdprLinkResponseModel`

## `/charging_hes_svc/get_vpp_service_policy_by_agg_user`

- **getVppDisclaimer**(`*(no params extracted)*`)

## `/charging_hes_svc/get_world_monetary_unit`

- **getPriceUnits**(`site_id, device_sn`)

## `/charging_hes_svc/quit_auto_disaster_prepare`

- **quitAutoDisasterPrepare**(`site_name, site_img, solar_list, pps_list, solarbank_list, home_backup_system_list, powerpanel_list, grid_list, solarbank_pps_list, smartplug_list, combiner_box_list, charging_pile_list`) → `AutoDisasterQuitPrepareModel`

## `/charging_hes_svc/restart_peak_session`

- **deleteAndRestartPeakValley**(`site_id, param_type, cmd, device_sn, parallel_type`)

## `/charging_hes_svc/set_station_evchargers`

- **bindUnX1Charger**(`station_id, main_sn, time, electricity_strategy, add_diesel, screen_setting, utility_rate_plan, ack_peak_valley, advanced_setting, heat_pump_setting, accuracy, cls_reset, off_grid_switching, evcharger_setting, version`)

## `/charging_hes_svc/update_hes_utility_rate_plan`

- **updatePeakAndValley**(`power_limit, limit, limit_real, site_id, param_type=19, cmd, param_data`)

## `/charging_hes_svc/update_wifi_config`

- **updateWiFiConfig**(`station_id, accuracy`)

## `/charging_hes_svc/user_event_alarm`

- **reportHesEvents**(`*(no params extracted)*`) → `A5101EventsSetModel`

## `/charging_hes_svc/user_fault_alarm`

- **sendDeviceReport**(`*(no params extracted)*`)

