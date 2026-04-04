# Charging Hes Svc

> 28+ function calls, 28+ unique endpoints (expanded with pp.txt discoveries)
>
> **Source**: Regenerated from ENDPOINT_FIELDS.md (authoritative reference)
> + additional endpoints from Blutter pp.txt string pool
>
> See also: `charging_disaster_prepared.md` for the separate disaster/backup API layer

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

---

## Additional Endpoints (from pp.txt string pool)

> These endpoints were found in the Blutter object pool but not in ENDPOINT_FIELDS.md.
> Parameter details are incomplete.

## `/charging_hes_svc/check_update`

- **checkUpdate**(`*(params TBD)*`)

## `/charging_hes_svc/download_energy_statistics`

- **downloadEnergyStatistics**(`*(params TBD)*`)

## `/charging_hes_svc/get_back_up_history`

- **getBackUpHistory**(`*(params TBD)*`)
  - Likely returns backup event history for HPP/HES devices

## `/charging_hes_svc/get_device_card_list`

- **getDeviceCardList**(`*(params TBD)*`)

## `/charging_hes_svc/get_device_pn_info`

- **getDevicePnInfo**(`*(params TBD)*`)

## `/charging_hes_svc/get_conn_net_tips`

- **getConnNetTips**(`*(params TBD)*`)

## `/charging_hes_svc/get_wifi_info`

- **getWifiInfo**(`*(params TBD)*`)

## `/charging_hes_svc/cancel_pop`

- **cancelPop**(`*(params TBD)*`)

## `/charging_hes_svc/get_site_mi_list`

- **getSiteMiList**(`*(params TBD)*`)
  - Likely returns microinverter list for station

## `/charging_hes_svc/get_user_fault_info`

- **getUserFaultInfo**(`*(params TBD)*`)

## `/charging_hes_svc/report_device_data`

- **reportDeviceData**(`*(params TBD)*`)

## `/charging_hes_svc/update_device_info_by_app`

- **updateDeviceInfoByApp**(`*(params TBD)*`) [SET]

## `/charging_hes_svc/upload_device_status`

- **uploadDeviceStatus**(`*(params TBD)*`) [SET]

## `/charging_hes_svc/get_energy_statistics`

- **getEnergyStatistics**(`*(params TBD)*`)

## `/charging_hes_svc/get_system_running_info`

- **getSystemRunningInfo**(`*(params TBD)*`)

## `/charging_hes_svc/sync_back_up_history`

- **syncBackUpHistory**(`*(params TBD)*`) [SET]
  - Synchronizes backup history data

## `/charging_hes_svc/enable_aiems_mode`

- **enableAiemsMode**(`*(params TBD)*`) [SET]
  - Enables AI EMS mode for station

## `/charging_hes_svc/get_history_setting`

- **getHistorySetting**(`*(params TBD)*`)

## `/charging_hes_svc/get_device_self_check`

- **getDeviceSelfCheck**(`*(params TBD)*`)

## `/charging_hes_svc/get_electric_utility_and_electric_plan_list`

- **getElectricUtilityAndElectricPlanList**(`*(params TBD)*`)

## `/charging_hes_svc/get_external_device_config`

- **getExternalDeviceConfig**(`*(params TBD)*`)

## `/charging_hes_svc/get_device_card_details`

- **getDeviceCardDetails**(`*(params TBD)*`)

---

## Related pp.txt String Constants

### Backup/Manual Mode Keys
```
manual_backup, manual_backup_mode, backup_info, backup_power,
backup_history, backupMode, backupHistoryReq, backupHistoryRes,
backupHistoryList
```

### Off-Grid Keys
```
off_grid, off_grid_enable, off_grid_sensitivity, off_grid_info,
off_grid_available_time, off_grid_start_time, is_off_grid
```

### Heat Pump Keys
```
heat_pump_setting, add_or_delete_heat_pump, heat_pump_state,
heat_pump_power, heat_pump_mode, heat_pump_plan,
heat_pump_manual_enable, heat_pump_min_launch_time,
heat_pump_min_running_time, heat_pump_plan_json
```
