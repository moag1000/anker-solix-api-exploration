# JSON Request Examples per Endpoint

> Request payloads extracted from thomluther's Python code (marked **verified**)
> and supplemented with Blutter-decompiled parameters (marked *inferred*).
> Replace placeholder values (siteId, deviceSn, etc.) with actual IDs.

## Verified Requests (from thomluther's implementation)

### `check_upgrade_record`
`check_upgrade_record`

```json
{"type": recordType} if fromFile: resp = await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["check_upgrade_record"]}_{recordType}.json"
```

### `compatible_process`
`compatible_process`

```json
{"solarbank_sn": solarbankSn} if fromFile: resp = await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["compatible_process"]}_{solarbankSn}.json"
```

### `get_ai_ems_status`
`ai_ems_status`

```json
{"site_id": siteId} if fromFile: resp = await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["get_ai_ems_status"]}_{siteId}.json"
```

### `get_co2_ranking`
`co2_ranking`

```json
{"site_id": siteId} if fromFile: resp = await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["get_co2_ranking"]}_{siteId}.json"
```

### `get_cutoff`
`power_cutoff`

```json
{"site_id": siteId, "device_sn": deviceSn} if fromFile: # For file data, verify first if there is a modified file to be used for testing if not ( resp := await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["get_cutoff"]}_modified_{deviceSn}.json"
```

### `get_device_attributes`
`device_attrs`

```json
{"site_id": siteId, "device_sn": deviceSn} if fromFile: resp = await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["get_device_fittings"]}_{deviceSn}.json"
```

### `get_device_charge_order_stats`
`charge_order_stats`

```json
{"site_id": siteId} if deviceSn: data.update({"device_sn": deviceSn})
```

### `get_device_fittings`
`device_fittings`

```json
{"site_id": siteId, "device_sn": deviceSn} if fromFile: resp = await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["get_device_fittings"]}_{deviceSn}.json"
```

### `get_device_load`
`device_load`

```json
{"site_id": siteId, "device_sn": deviceSn} if fromFile: # For file data, verify first if there is a modified schedule to be used for testing if not ( resp := await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["get_device_load"]}_modified_{deviceSn}.json"
```

### `get_device_parm`
`device_parm`

```json
{"site_id": siteId, "param_type": paramType} if fromFile: # For file data, verify first if there is a modified schedule to be used for testing if not ( resp := await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["get_device_parm"]}_{paramType}_modified_{siteId}.json"
```

### `get_device_pv_price`
`device_pv_price`

```json
{"sn": deviceSn} if fromFile: # For file data, verify first if there is a modified file to be used for testing if not ( resp := await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["get_device_pv_price"]}_modified_{deviceSn}.json"
```

### `get_device_pv_statistics`
`device_pv_statistics`

```json
{"site_id": siteId} if deviceSn: data.update({"device_sn": deviceSn})
```

### `get_device_pv_status`
`device_pv_status`

```json
{"sns": sns} if fromFile: # combine status of each device file into single response for multiple devices resp = {}
```

### `get_device_pv_total_statistics`
`device_pv_total_statistics`

```json
{"sn": deviceSn} if fromFile: # For file data, verify first if there is a modified file to be used for testing if not ( resp := await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["get_device_pv_total_statistics"]}_modified_{deviceSn}.json"
```

### `get_dynamic_price_details`
`dynamic_price_details`

```json
{"site_id": str(siteId)} if decimals is not None: data["accuracy"] = decimals if fromFile: # For file data, verify first if there is a modified file to be used for testing if not ( resp := await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["get_site_price"]}_modified_{siteId}.json"
```

### `get_dynamic_price_providers`
`dynamic_price_providers`

```json
{"device_pn": model} if fromFile: resp = await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["get_dynamic_price_providers"]}_{model}.json"
```

### `get_ota_batch`
`ota_batch`

```json
{"site_id": siteId} if fromFile: resp = await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["wifi_list"]}_{siteId}.json"
```

### `get_ota_info`
`ota_info`

```json
{"solar_bank_sn": solarbankSn, "solar_sn": inverterSn} if fromFile: resp = await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["get_ota_info"]}_{solarbankSn or inverterSn}.json"
```

### `get_ota_update`
`ota_update`

```json
{"device_sn": deviceSn, "insert_sn": insertSn} if fromFile: resp = await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["get_ota_update"]}_{deviceSn}.json"
```

### `get_site_power_limit`
`power_limit`

```json
{"site_id": siteId} if fromFile: # For file data, verify first if there is a modified file to be used for testing if not ( resp := await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["get_site_power_limit"]}_modified_{siteId}.json"
```

### `get_site_price`
`price`

```json
{"site_id": str(siteId)} if decimals is not None: data["accuracy"] = decimals if fromFile: # For file data, verify first if there is a modified file to be used for testing if not ( resp := await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["get_site_price"]}_modified_{siteId}.json"
```

### `get_upgrade_record`
`upgrade_record`

```json
{"type": recordType} if fromFile: resp = await self.apisession.loadFromFile( Path( self.testDir() / f"{API_FILEPREFIXES["get_upgrade_record"]}_{recordType}_{deviceSn or siteId or recordType}.json"
```

### `home_load_chart`
`power_service/v1/site/get_home_load_chart`

```json
{"site_id": siteId} if deviceSn: data.update({"device_sn": deviceSn})
```

### `scene_info`
`scene`

```json
{"site_id": siteId} if fromFile: resp = await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["scene_info"]}_{siteId}.json"
```

### `set_auto_upgrade`
`power_service/v1/app/set_auto_upgrade`

```json
{"site_id": siteId} if fromFile: resp = await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["scene_info"]}_{siteId}.json"
```

### `set_cutoff`
`power_service/v1/app/compatible/set_power_cutoff`

```json
{"site_id": siteId, "device_sn": deviceSn} if fromFile: # For file data, verify first if there is a modified file to be used for testing if not ( resp := await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["get_cutoff"]}_modified_{deviceSn}.json"
```

### `set_device_load`
`power_service/v1/app/device/set_device_home_load`

```json
{} # get all SB1 in system that may share same schedule with device and update their schedule for sn in [ sn for sn, sb in self.devices.items() if sb.get("site_id") == siteId and sb.get("type") == SolixDeviceType.SOLARBANK.value and (sb.get("generation") or 0) <= 1 ]: self._update_dev(
```

### `set_device_parm`
`power_service/v1/site/set_site_device_param`

```json
{} # get all solarbanks that may share same schedule or are managed by a station dev_serials = { sn for sn, sb in self.devices.items() if sb.get("site_id") == siteId and sb.get("type") == SolixDeviceType.SOLARBANK.value and (sb.get("generation") or 0) >= 2 }
```

### `set_device_pv_price`
`charging_pv_svc/updateUserTieredElecPrice`

```json
{"sn": deviceSn} if fromFile: # For file data, verify first if there is a modified file to be used for testing if not ( resp := await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["get_device_pv_price"]}_modified_{deviceSn}.json"
```

### `site_detail`
`site_detail`

```json
{"site_id": siteId} if fromFile: resp = await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["site_detail"]}_{siteId}.json"
```

### `solar_info`
`solar_info`

```json
{"solarbank_sn": solarbankSn} if fromFile: resp = await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["solar_info"]}_{solarbankSn}.json"
```

### `update_site_price`
`power_service/v1/site/update_site_price`

```json
{"site_id": str(siteId)} if decimals is not None: data["accuracy"] = decimals if fromFile: # For file data, verify first if there is a modified file to be used for testing if not ( resp := await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["get_site_price"]}_modified_{siteId}.json"
```

### `wifi_list`
`wifi_list`

```json
{"site_id": siteId} if fromFile: resp = await self.apisession.loadFromFile( Path(self.testDir()) / f"{API_FILEPREFIXES["wifi_list"]}_{siteId}.json"
```

---

## Inferred Requests (from Blutter decompilation)

> These are parameter names found near API call sites. The actual JSON structure
> may differ. Field values are placeholders.

### `add_charging_mode`
Function: `addCustomChargeMode`

```json
{"device_sn": "...", "name": "...", "number": "...", "total_power": "...", "max_total_power": "...", "auto_exit": "...", "has_charge_protocol": "...", "power_settings": "..."}
```

### `add_feedback`
Function: `postFeedback`

```json
{"attachment_key_prefixs": "...", "device_name": "...", "product_number": "...", "device_sn": "...", "user_name": "...", "user_email": "...", "message_content": "...", "type": "..."}
```

### `add_manual_clock_screensavers`
Function: `addA2345CustomClockScreenSavers`

```json
{"sn": "...", "img_url": "...", "hash_code": "..."}
```

### `adjust_station_price_unit`
Function: `changePriceUnit`

```json
{"station_id": "...", "price_unit": "..."}
```

### `banners`
Function: `getBanners`

```json
{"region": "..."}
```

### `check_function`
Function: `checkFunction`

```json
{"station_id": "..."}
```

### `check_third_sn`
Function: `checkThirdSN`

```json
{"device_model": "...", "device_sn": "...", "brand_id": "..."}
```

### `confirm_permissions_settings`
Function: `getConfirmPermissionsSettingsApi`

```json
{"device_model": "...", "confirm_type": "..."}
```

### `create_site`
Function: `createSiteRequest`

```json
{"site_name": "...", "site_img": "...", "solar_list": "...", "pps_list": "...", "solarbank_list": "...", "home_backup_system_list": "...", "powerpanel_list": "...", "grid_list": "..."}
```

### `deal_share_data`
Function: `agreeOrRefuseVppDisclaimer`

```json
{"sn": "...", "action": "..."}
```

### `delete_charging_mode`
Function: `deleteCustomChargeMode`

```json
{"id": "..."}
```

### `delete_manual_clock_screensavers`
Function: `deleteA2345CustomClockScreenSavers`

```json
{"id": "..."}
```

### `device_command`
Function: `sendDeviceCommand`

```json
{"station_id": "...", "main_sn": "...", "time": "...", "electricity_strategy": "...", "add_diesel": "...", "screen_setting": "...", "utility_rate_plan": "...", "ack_peak_valley": "..."}
```

### `dst`
Function: `getDaylightSavingTime`

```json
{"city": "..."}
```

### `getPvStatus`
Function: `getPvStatus`

```json
{"sns": "..."}
```

### `get_addable_site_list`
Function: `getAddableSiteList`

```json
{"device_sn": "...", "device_model": "...", "device_model": "..."}
```

### `get_auto_disaster_prepare_detail`
Function: `getAutoDisasterPrepareDetail`

```json
{"station_id": "...", "unix": "...", "near_field": "..."}
```

### `get_auto_disaster_prepare_status`
Function: `getAutoDisasterPrepareStatus`

```json
{"station_id": "..."}
```

### `get_charging_device_identity_new_status`
Function: `getA2687StandardChargingDeviceModelIdentityStatus`

```json
{"device_sn": "...", "charging_device_identity_new_status": "..."}
```

### `get_charging_device_identity_status_default_true`
Function: `getA2345DeviceIdentityStatus`

```json
{"device_sn": "...", "status": "..."}
```

### `get_charging_mode_list`
Function: `getCustomChargeModeList`

```json
{"device_sn": "..."}
```

### `get_clock_screensavers`
Function: `getScreenSaversByCategory`

```json
{"product_code": "..."}
```

### `get_comb_addable_sites`
Function: `getDeviceJoinSiteList`

```json
{"devices": "..."}
```

### `get_compatible_process`
Function: `checkSolarForceUpdateState`

```json
{"solar_sn": "...", "solarbank_sn": "..."}
```

### `get_configs`
Function: `getSiteConfigs`

```json
{"station_id": "...", "param_types": "..."}
```

### `get_confirm_permissions`
Function: `getConfirmPermissionsApi`

```json
{"device_model": "..."}
```

### `get_day_power_data`
Function: `getDayPowerData`

```json
{"device_model": "...", "device_sn": "...", "date": "..."}
```

### `get_device_attrs`
Function: `getDeviceAttrs`

```json
{"device_sn": "...", "attributes": "...", "enable_0w_v2": "..."}
```

### `get_device_command`
Function: `getDeviceCommand`

```json
{"station_id": "...", "accuracy": "..."}
```

### `get_device_home_load`
Function: `getDeviceHomeLoadPort`

```json
{"device_sn": "..."}
```

### `get_device_income`
Function: `getTOUChartStatistics`

```json
{"device_sn": "...", "type": "...", "start_time": "..."}
```

### `get_device_infos`
Function: `getDeviceInfos`

```json
{"sns": "..."}
```

### `get_device_setting`
Function: `getCustomChargeModeSetting`

```json
{"device_sn": "...", "charging_mode_status": "...", "compatibility_status": "...", "charging_device_identity_status": "..."}
```

### `get_easter_egg_trigger_list`
Function: `getEasterEggRecord`

```json
{"device_sn": "..."}
```

### `get_error_infos`
Function: `getErrorInfos`

```json
{"sn_errors": "..."}
```

### `get_heat_pump_plan_json`
Function: `getHeatPumpTimePlan`

```json
{"heat_pump_plan": "..."}
```

### `get_installation`
Function: `getInstallationApi`

```json
{"solarbank_sn": "...", "site_id": "..."}
```

### `get_installation_inspection`
Function: `getInstallation`

```json
{"sn": "..."}
```

### `get_invited_list`
Function: `getInviteMember`

```json
{"site_id": "...", "status": "..."}
```

### `get_list`
Function: `getCurrencyGetList`

```json
{"counrty": "..."}
```

### `get_manual_clock_screensavers`
Function: `getA2345CustomClockScreenSavers`

```json
{"sn": "..."}
```

### `get_mes_device_info`
Function: `getDeviceLaserSn`

```json
{"device_sn": "..."}
```

### `get_message`
Function: `getMessage`

```json
{"last_time": "...", "device_sns": "...", "limit": "...", "message_type": "...", "last_msg_id": "..."}
```

### `get_ota_info`
Function: `getThirdOtaInfo`

```json
{"solar_bank_sn": "...", "solar_sn": "..."}
```

### `get_ota_update`
Function: `getThirdOtaStatus`

```json
{"device_sn": "...", "insert_sn": "..."}
```

### `get_popup`
Function: `queryA17Y0Popup`

```json
{"site_id": "..."}
```

### `get_port_remarks`
Function: `getPortRemarks`

```json
{"device_sn": "..."}
```

### `get_power_limit`
Function: `getSitePowerLimit`

```json
{"site_id": "..."}
```

### `get_power_range_support_protocols`
Function: `getPowerSupportProtocols`

```json
{"device_model": "..."}
```

### `get_protocol_status`
Function: `getA2687ProtocolAgreementStatus`

```json
{"device_sn": "..."}
```

### `get_relate_belong`
Function: `getDeviceBindInfo`

```json
{"device_sn": "..."}
```

### `get_relate_device_fittings`
Function: `getRelateAccessory`

```json
{"device_sn": "..."}
```

### `get_rom_versions`
Function: `checkFirmwareWifi`

```json
{"main_sn": "...", "device_rom_versions": "..."}
```

### `get_scen_info`
Function: `querySceneInfo`

```json
{"site_id": "..."}
```

### `get_schedule`
Function: `getSiteSchedule`

```json
{"site_id": "..."}
```

### `get_site_detail`
Function: `getStationDetail`

```json
{"site_id": "..."}
```

### `get_site_device_param`
Function: `getSafetySocParams`

```json
{"site_id": "...", "param_type": "..."}
```

### `get_site_price`
Function: `getSitePriceRequest`

```json
{"site_id": "...", "accuracy": "..."}
```

### `get_station_config_and_status`
Function: `getA5101StationConfigDetail`

```json
{"station_id": "..."}
```

### `get_status`
Function: `getAiModeStatusRequest`

```json
{"site_id": "..."}
```


---

## New Findings: Additional Parameters from Blutter

These parameters were found in the decompiled Dart code but are **not documented** in
thomluther's `apitypes.py`. Each entry shows what is currently known vs what Blutter adds.

### `get_device_attributes`
`power_service/v1/app/device/get_device_attrs`

Currently documented: `{"device_sn": "...", "attributes": ["rssi", "pv_power_limit", "legal_power_limit", "power_limit_option", "power_limit_option_real", "switch_0w"]}`

Blutter reveals an additional parameter:
```json
{"device_sn": "...", "attributes": [...], "enable_0w_v2": true}
```
Function: `getDeviceAttrs` — the `enable_0w_v2` flag likely enables the v2 version of the 0W output feature.

### `get_device_income`
`power_service/v1/app/device/get_device_income`

Currently documented: `{"device_sn": "...", "start_time": "..."}`

Blutter reveals additional parameters:
```json
{"device_sn": "...", "start_time": "...", "type": "..."}
```
Function: `getTOUChartStatistics` — the `type` parameter likely selects the chart data type (daily/weekly/monthly).

### `charger_get_device_setting`
`mini_power/v1/app/setting/get_device_setting`

Currently documented: `{"device_sn": "..."}`

Blutter reveals the expected response contains:
```json
{"charging_mode_status": "...", "compatibility_status": "...", "charging_device_identity_status": "..."}
```
Function: `getCustomChargeModeSetting` — these fields indicate available charger modes and compatibility state.

### `set_device_attributes` — Multiple usage patterns

The `set_device_attrs` endpoint (`power_service/v1/app/device/set_device_attrs`) is used by **9 different functions** in the app, each with a different payload structure:

#### Set power options
```json
{"device_sn": "...", "attributes": {...}, "enable_0w_v2": true}
```
Function: `setDevicePowerOptionsReq`

#### Set TOU electricity attributes
```json
{"device_sn": "...", "attributes": {...}, "pps_use_time": "..."}
```
Function: `setTouElectricAttrs`

#### Set currency
```json
{"device_sn": "...", "attributes": {...}, "currency": "..."}
```
Function: `getCurrencySetDeviceAttrs`

#### Set solar panel names
```json
{"device_sn": "...", "device_pn": "...", "attributes": {...}}
```
Function: `setSolarName` / `setPpsSolarName`

#### Set 0W feed-in grid switch
```json
{"device_sn": "...", "attributes": {...}, "switch_0w": 0}
```
Function: `setDeviceFeedGridSwitch`

#### Set PV power limit
```json
{"device_sn": "...", "attributes": {...}, "pv_power_limit": 800}
```
Function: `setDevicePvPowerOptionsReq`

#### Set location tag
```json
{"device_sn": "...", "attributes": {...}, "tag": "..."}
```
Function: `setLocationTag`

#### Set game/demo status
```json
{"device_sn": "...", "attributes": {...}, "init_status": "..."}
```
Function: `setDeviceGameStatus`

### `get_configs` (charging_energy_service)

Blutter reveals the `station_id` parameter name (thomluther documents it as `siteId`):
```json
{"station_id": "...", "param_types": [...]}
```
Function: `getSiteConfigs` — note: `station_id` vs `siteId` may be interchangeable.

---

## Constants and Enum Values (from APK)

### Peak/Valley Price Types
```json
{"peak": 1, "normal": 2, "valley": 3, "super_valley": 4}
```

### Usage Mode Types
```
self_consumption, manual_backup, peak_shaving, custom_mode,
time_of_use, use_time, smart, dynamic, fixed
```

### Day Types
```
weekday, weekend, everyday
```

### Schedule/Rate Plan Names
```
ai_ems, blend_plan, custom_rate_plan, manual_backup,
peak_sessions, peak_valley_prices, use_time
```

### Device Type Categories
```
solar_bank, solarbank, pps, hes, micro_inverter, ev_charger, generator
```

### All Known Product Codes (53 models)
```
A1340, A1341, A1722, A1723, A1725, A1726, A1727, A1728, A1729,
A1753, A1754, A1755, A1761, A1762, A1763, A1765,
A1770, A1771, A1772, A1780, A1780P, A1781, A1782, A1783, A1785,
A1790, A1790A, A1790B, A1790P, A1903,
A2345, A2687, A2693, A2693E1, A2693E2,
A5101, A5102, A5103, A5140, A5141, A5143, A5150, A5190, A5191, A5220, A5341, A5450,
A7320, AE100, AE1R0, AX170, AX1C0, AX1S0
```

---

## EV Charger Schedule Defaults (A5190)

```json
{
  "weekdayStartTime": "08:00",
  "weekdayEndTime": "22:00",
  "weekendStartTime": "08:00",
  "weekendEndTime": "22:00",
  "everyDaySwitch": false,
  "isSwitchOn": false,
  "chargingMode": "...",
  "regularCharge": "...",
  "smartChargeList": []
}
```

---

## Range Extender Strategy (A7320)

```json
{
  "strategySwitchOn": true,
  "strategyType": "bysoc|bytime",
  "bysocData": {"startSoc": 20, "targetSoc": 80},
  "bytimeData": {"startTime": "08:00", "targetSoc": 80},
  "unableExcuteStrategyReason": "...",
  "lastTaskResult": "...",
  "lastTaskExecusionTime": "...",
  "lastTaskFailReason": "..."
}
```

---

## EV Charger Control (A5190 prop_write_evcharger)

```json
{
  "rechargingPowerOutage": false,
  "plugAndChargeSwitch": false,
  "carChargerLockStatus": 0,
  "maximumCurrentLimit": 16,
  "delayStartSwitch": false,
  "lightBrightness": 100,
  "ledSwitch": true,
  "ledCloseStartTime": "22:00",
  "ledCloseEndTime": "06:00"
}
```

---

## Device Bind Request

`/app/devicerelation/relate_device`

```json
{
  "device_sn": "...",
  "product_code": "A17C0",
  "device_name": "Solarbank E1600",
  "bt_ble_id": "...",
  "bt_ble_mac": "...",
  "firmware_version": "...",
  "wifi_name": "...",
  "parent_device_sn": "...",
  "parent_device_pn": "..."
}
```

---

## Dynamic Price Response Fields

`/power_service/v1/dynamic_price/price_detail`

```json
{
  "release_time": "...",
  "today_avg_price": 0.15,
  "tomorrow_avg_price": 0.12,
  "today_price_trend": "...",
  "tomorrow_price_trend": "...",
  "batteryReserve": 10,
  "value": [...]
}
```

---

## akiot.cloud_api Bridge Format

The native AKIoT SDK uses this format to proxy cloud API calls through BLE/MQTT:

```json
{
  "method": "POST",
  "path": "/power_service/v1/site/get_site_device_param",
  "param": {"site_id": "...", "param_type": "18"}
}
```
Transport: `akiot.cloud_api` via `akiot.device.invoke_action`

---

## SceneInfo Key Feature Flags

From `get_scen_info` response — these boolean/status fields control UI behavior:

```json
{
  "manual_backup_mode": false,
  "exceed_power": "0",
  "peak_valley_mode": false,
  "heating": false,
  "shelly_meter": false,
  "support_p1_meter": false,
  "enable_parallel": false,
  "plug_switch_report": false,
  "show_third_party_pv_panel": false,
  "meter_self_testing": false,
  "power_limit_status": 0,
  "power_saving_mode": false,
  "third_party_pv_enable": false,
  "enable_aiems_v2": false,
  "grid_to_ev": false
}
```
