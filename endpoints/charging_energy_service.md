# Charging Energy Service

> 13 function calls, 13 unique endpoints

## `/charging_energy_service/ack_utility_rate_plan`

- **ackUtilityRatePlanData**(`sn, page, errors`)

## `/charging_energy_service/adjust_station_price_unit`

- **changeA17B1PriceUnit**(`*(no params extracted)*`)

## `/charging_energy_service/get_configs`

- **getSiteConfigs**(`business_type, identifier_type, identifier_id`)

## `/charging_energy_service/get_device_infos`

- **getDeviceInfos**(`main_sn, device_rom_versions`) → `DeviceInfosModel`

## `/charging_energy_service/get_error_infos`

- **getErrorInfos**(`*(no params extracted)*`) → `ErrorInfosModel`

## `/charging_energy_service/get_installation_inspection`

- **getInstallation**(`site_id, param_type=18`) → `SceneInfo`

## `/charging_energy_service/get_rom_versions`

- **checkFirmwareWifi**(`solar_sn, solarbank_sn`) → `FirmwareUpdateModel`

## `/charging_energy_service/get_wifi_info`

- **getWifiInfoOf17B1**(`*(no params extracted)*`) → `WifiInfoModel`

## `/charging_energy_service/get_world_monetary_unit`

- **getA17B1PriceUnits**(`*(no params extracted)*`)

## `/charging_energy_service/preprocess_utility_rate_plan`

- **dealUtilityRatePlanData**(`device_sn, attributes, switch_0w`)

## `/charging_energy_service/restart_peak_session`

- **restartPeakSession**(`device_sn, home_load_data`)

## `/charging_energy_service/sync_config`

- **syncSiteConfig**(`*(no params extracted)*`)

## `/charging_energy_service/sync_installation_inspection`

- **syncInstallation**(`sn_errors`)

