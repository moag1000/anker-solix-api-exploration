# Charging Energy Service

> 11 function calls, 10 unique endpoints
>
> **Source**: Regenerated from ENDPOINT_FIELDS.md (authoritative reference)

## `/charging_energy_service/get_configs`

- **getSiteConfigs**(`station_id?, param_types`)

## `/charging_energy_service/get_device_infos`

- **getDeviceInfos**(`sns?`) → `DeviceInfosModel`

## `/charging_energy_service/get_error_infos`

- **getErrorInfos**(`sn_errors?`) → `ErrorInfosModel`

## `/charging_energy_service/get_installation_inspection`

- **getInstallation**(`sn?`) → `SceneInfo`

## `/charging_energy_service/get_rom_versions`

- **checkFirmwareWifi**(`main_sn?, device_rom_versions`) → `FirmwareUpdateModel`

## `/charging_energy_service/get_wifi_info`

- **getWifiInfoOf17B1**(`sn?`) → `WifiInfoModel`

## `/charging_energy_service/preprocess_utility_rate_plan`

- **dealUtilityRatePlanData**(`peak_sessions?`)

## `/charging_energy_service/sync_installation_inspection`

- **syncInstallation**(`sn?, page, errors`)

## `/charging_energy_service/ack_utility_rate_plan`

- **ackUtilityRatePlanData**(`*(no params in ENDPOINT_FIELDS.md)*`)

## `/charging_energy_service/sync_config`

- **syncSiteConfig**(`*(no params in ENDPOINT_FIELDS.md)*`)
