# Charging Energy Service

> 11+ function calls, 10+ unique endpoints (expanded with pp.txt + powerpanel.py findings)
>
> **Source**: Regenerated from ENDPOINT_FIELDS.md (authoritative reference)
> + additional endpoints from powerpanel.py API implementation and Blutter pp.txt
>
> See also: `devices/home_power_panel.md` for full HPP device documentation

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

---

## Additional Endpoints (from powerpanel.py + pp.txt)

> These endpoints are implemented in `powerpanel.py` or found in pp.txt but
> were not in ENDPOINT_FIELDS.md extraction.

## `/charging_energy_service/get_system_running_info`

- **getSystemRunningInfo**(`site_id`)
- Implemented in `powerpanel.py` lines 518-581
- Response fields:
  ```
  connect_infos              dict    {<device_sn>: true/false}
  connected                  bool    System connectivity
  total_system_power_generation  float   Total generation (MWh)
  system_power_generation_unit   string  "MWh"
  save_carbon_footprint      float   Carbon saved (tons)
  save_carbon_unit            string  "t"
  total_system_savings        float   Total monetary savings
  system_savings_price_unit   string  "$"
  ```

## `/charging_energy_service/energy_statistics`

- **energyStatistics**(`siteId, rangeType, startDay, endDay, sourceType, isglobal?, productCode?`)
- Implemented in `powerpanel.py` lines 860-922
- `rangeType`: `"day"` | `"week"` | `"year"`
- `sourceType`: `"solar"` | `"hes"` | `"grid"` | `"home"` | `"pps"` | `"diesel"`

## `/charging_energy_service/get_error_infos`

- **getErrorInfos**(`sn_errors?`) → `ErrorInfosModel`
- Implemented in `powerpanel.py`

## `/charging_energy_service/report_device_data`

- **reportDeviceData**(`control?, data?`)
- `control`: 0 or 1

## `/charging_energy_service/get_sns`

- **getSns**(`main_sn, macs[]`)
- Maps attached PPS serial numbers to HPP
- Example: `{"main_sn": "POWERPANELSN", "macs": ["F38001MAC001", "F38002MAC002"]}`

## `/charging_energy_service/get_world_monetary_unit`

- **getWorldMonetaryUnit**(`*(params TBD)*`)

## `/charging_energy_service/adjust_station_price_unit`

- **adjustStationPriceUnit**(`*(params TBD)*`) [SET]

## `/charging_energy_service/restart_peak_session`

- **restartPeakSession**(`device_sn, home_load_data?`) [SET]
