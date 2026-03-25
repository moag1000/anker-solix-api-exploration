# Validation Model — How the Anker App determines allowed values

> The Anker App does NOT hardcode validation ranges. It queries the server for
> device-specific limits and builds UI controls dynamically from the response.
> This document describes the query→validate→set flow for each setting category.
>
> **Sources:** Blutter decompilation of controller/logic Dart files (for API/BLE flows),
> mqtt_monitor sessions on A17C1 FW 1.0.6.10 and A17X8 FW 0.0.2.7 (for verified MQTT commands).
> Settings marked "Verified" were confirmed with real device traffic.

## General Pattern

```
1. GET endpoint  →  Response with min/max/step/options fields
2. UI built from response values (slider range, picker options)
3. User changes value (constrained by UI)
4. SET endpoint  ←  New value sent to server
```

Developers implementing controls must follow the same pattern:
**always query limits first**, then validate user input against the response.

---

## Power Limit Settings

### Query: `get_power_limit` (param_type=16)
**Response model:** `StationPowerLimitModel`

| Response Field | Purpose |
|---------------|---------|
| `min` | Minimum allowed power (W) |
| `max` | Maximum allowed power (W) |
| `step` | Step size for slider (W) |
| `init_step` | Initial step size |
| `legal_limit` | Legal limit for region |
| `legal_power_limit` | Legal power limit (W) |
| `region_power_limit` | Region-specific limit |
| `power_limit_option` | Available power options |
| `power_limit_option_real` | Actual applicable options |
| `acInputLimit` | AC input limit |
| `supportAcLimit` | Whether AC limit is supported |
| `parallel_type` | Parallel system type |
| `exceed_alarm` | Exceed alarm threshold |

### Set: `set_site_device_param` (param_type=19)
**Function:** `setSiteDevicePowerLimit`
**Params:** `site_id, param_type=19, cmd, param_data`

### App Flow (from `station_power_limit_logic.dart`)
```
1. getSitePowerLimit()  →  StationPowerLimitModel
2. UI slider: min=model.min, max=model.max, step=model.step
3. Legal warning if value > model.legal_power_limit
4. setSiteDevicePowerLimit()  ←  new limit value
```

---

## Home Load / Output Power Settings

### Query: `get_device_home_load`
**Response model:** `A17C1DeviceHomeLoadData` / `SiteHomeLoadModel`

| Response Field | Purpose |
|---------------|---------|
| `min_load` | Minimum home load (W) |
| `max_load` | Maximum home load (W) |
| `step` | Step size (W) |
| `current_home_load` | Current setting |
| `default_home_load` | Default value |
| `default_charge_priority` | Default charge priority (%) |
| `schedule_mode` | Current schedule mode |
| `last_select_mode` | Last selected mode |
| `parallel_home_load` | Parallel system load |
| `parallel_display` | Whether parallel display is shown |
| `advancedModeMinLoad` | Min load in advanced mode |
| `ranges` | Time slot ranges with per-slot settings |

### Set: `set_device_home_load`
**Params:** `device_sn, mode_type, custom_rate_plan, home_load_data`

### App Flow (from `a17c1home_logic.dart` / `energy_home_controller.dart`)
```
1. get17C1DeviceHomeLoadPort()  →  A17C1DeviceHomeLoadData
2. UI slider: min=model.min_load, max=model.max_load, step=model.step
3. Schedule editor: ranges with start_time, end_time, power, charge_priority
4. set17C1DeviceHomeLoadRes()  ←  updated schedule
```

---

## SOC Reserve / Battery Reserve

### Query: `get_site_device_param` (param_type=18)
**Function:** `getSafetySocParams`
**Response:** `param_data` JSON containing:

| Response Field | Purpose |
|---------------|---------|
| `soc_list` | List of SOC options: `[{id, is_selected, soc}]` |
| `switch_0w` | 0W switch status |
| `enable_0w` | 0W feature enabled |
| `enable_0w_change` | Whether 0W can be changed |
| `feed-in_power_limit` | Feed-in power limit |

### Set: `set_site_device_param` (param_type=18)
**Function:** `setSafetySocParams`

### Additional: `get_device_attrs` for per-device SOC
**Response model:** `DevicePowerLimit`

| Response Field | Purpose |
|---------------|---------|
| `min` | Minimum SOC (%) |
| `max` | Maximum SOC (%) |
| `step` | Step size (%) |
| `feeder0w` | 0W feeder status |
| `switch_0w` | 0W switch |
| `ip_region` | IP region |
| `regulation_code` | Regulation code |

### App Flow (from `soc_setting_controller.dart`)
```
1. getSafetySocParams()  →  soc_list with available SOC options
2. UI shows soc_list options (e.g., 5% and 10%)
3. User selects new SOC reserve
4. setSafetySocParams()  ←  updated soc_list with is_selected
```

---

## Usage Mode / Energy Mode

### Query: `get_site_device_param` (param_type depends on device)
**Functions:**
- param_type=1: `getSiteGreenModeDeviceParam` — Green mode
- param_type=2: `getSitePeakTimeDeviceParam` — Peak/valley
- param_type=3: `getSiteEnablePeakDeviceParam` — Peak shaving
- param_type=5: `getSiteLowerLimitDeviceParam` — Lower limit

**Response model:** `SiteConsumptionStrategyModel`

| Response Field | Purpose |
|---------------|---------|
| `mode_type` | Current mode |
| `min_load` | Minimum load for this mode |
| `max_load` | Maximum load for this mode |
| `step` | Step size |
| `reserved_soc` | Reserved SOC for this mode |
| `custom_rate_plan` | Custom rate plan definition |
| `blend_plan` | Blend plan (smart plug mode) |
| `data_auth` | Data authorization flag |
| `exceed_alarm` | Exceed alarm setting |
| `ai_ems` | AI EMS configuration |

### Set: `set_site_device_param`
**Function:** `set17C1SiteDeviceParam`
**Also via MQTT:** Command `005e` (usage_mode + schedule, see PR #283)

### App Flow (from `power_usage_scenario_logic.dart`)
```
1. get17C1SiteDeviceParam()  →  SiteConsumptionStrategyModel per mode
2. getAiModeStatusRequest()  →  AiModeStatusModel (AI EMS state)
3. UI shows available modes with their constraints
4. set17C1SiteDeviceParam()  ←  new mode + schedule
```

---

## Country Code / Grid Code

### Query: `get_site_device_param` (param_type=20)
**Function:** `getStationCountryCode`

### Set: `set_site_device_param` (param_type=20)
**Function:** `setStationCountryCode`

---

## Third-Party PV

### Query: `get_site_device_param` (param_type=26)
**Function:** `getThreePvParam`
**Response:** `param_data` containing `third_part_pv_setting`, `show_third_party_pv_panel`

### Set: `set_site_device_param` (param_type=26)
**Function:** `setThreePvInstallSwitch`

---

## EV Charger Max Current

### App Flow (from `max_charge_controller.dart`)
```
1. Read ev_max_current from device info
2. UI slider constrained by device rated current
3. Set via MQTT or API
```

Tracked fields: `ev_max_current`, `ev_event_duration`, `ev_entrance`, `ev_is_success`

---

## Dynamic Price / TOU

### Query: `dynamic_price/support_option`
**Function:** `getDynamicPriceSupportOption`
**Params:** `site_id`

### Query: `dynamic_price/price_detail`
**Function:** `getDynamicPriceDetail`
**Response model:** `DynamicPriceDetailModel`

| Response Field | Purpose |
|---------------|---------|
| `time` | Time points |
| `price` | Price values |
| `currency` | Currency |
| `todayAvgPrice` | Today average price |
| `todayPriceTrend` | Today price trend |
| `tomorrowAvgPrice` | Tomorrow average |
| `tomorrowPriceTrend` | Tomorrow trend |

### Set: `set_site_device_param` with electricity_strategy
**Function:** `setDynamicPrice`
**Params:** `device_sn, mode, protocol_key, status`

---

## Disaster Preparedness / Storm Guard

### Query: `check_function`
**Response model:** `CheckFunctionModel`

| Response Field | Purpose |
|---------------|---------|
| `auto_disaster` | Auto disaster supported |
| `support` | General support flags |
| `ems_disable` | EMS disabled flag |
| `peak_shaving` | Peak shaving supported |

### Query: `get_auto_disaster_prepare_status`
**Response model:** `AutoDisasterPrepareStatusModel`
**Fields:** `code, disasterPrepareStatus, events, targetPage`

### Set: Manual disaster via API
**Params:** `identifier_id, type, disaster_type, manual_disaster_switch, start_time, end_time`

---

---

## MQTT-Only Settings (Solarbank A17C0-C5)

These settings are controlled **exclusively via MQTT** commands, not through the cloud API.
The validation values come from the device's status messages (0405/0408).

**Important:** MQTT command numbers are **device-specific**. The same command number can have
different meanings on different devices. For example, `0068` is the LED command on A17C1 but
`CMD_SB_INVERTER_TYPE` on A17C0. Similarly, `005e` is `CMD_SB_USAGE_MODE` on Solarbanks but
`CMD_AC_FAST_CHARGE_SWITCH` on PPS devices. Always check `mqttmap.py` for the device-specific
mapping under the correct model key.

### LED / Light Mode
| | Details |
|---|---|
| **MQTT cmd** | `0068` (A17C1 — on A17C0 this is inverter type!) |
| **Fields** | a2=`light_mode` (0=normal, 1=mood), a3=`light_off_switch` (0=on, 1=off) |
| **Status** | 0405 fields d2, e1 |
| **BLE action** | `action_set_ambient_light_switch` |
| **Verified** | A17C1 FW 1.0.6.10 (mqtt_monitor 2026-03-25) |

### Temperature Unit
| | Details |
|---|---|
| **MQTT cmd** | `0050` |
| **Fields** | a2=`temp_unit` (0=Celsius, 1=Fahrenheit) |
| **Status** | 0405 field a9 |
| **BLE action** | `action_set_temperature_type` |
| **Verified** | A17C1 FW 1.0.6.10 |

### Power Cutoff Thresholds
| | Details |
|---|---|
| **MQTT cmd** | `0067` |
| **Fields** | a2=`output_cutoff` (5\|10), a3=`lowpower_input` (4\|5), a4=`input_cutoff` (5\|10) |
| **Status** | 0405 fields b4, b5, b6 |
| **Options** | Fixed: output/input=[5,10], lowpower follows output (5→4, 10→5) |
| **Verified** | A17C1 FW 1.0.6.10 |

### Max Load (direct)
| | Details |
|---|---|
| **MQTT cmd** | `0080` (from app), `005a` (from cloud) |
| **Fields** | a2=`max_load` (W), a3=`max_load_type` (0=manual, 3=auto/parallel) |
| **Status** | 0405 field c2 |
| **Options** | Depends on `get_power_limit` response: Single=[350,600,800,1000], Multi=[1200,2400,3600,4800] |
| **Verified** | A17C1 FW 1.0.6.10 |

### Usage Mode + Schedule
| | Details |
|---|---|
| **MQTT cmd** | `005e` (A17C1 Solarbank — on PPS devices this is `CMD_AC_FAST_CHARGE_SWITCH`!) |
| **Fields** | a2=`usage_mode` (1=SmartHome, 3=Volleinspeisung, ...), a3=`schedule_enabled`, a4-be=7 weekday slots |
| **Slot format** | 8 bytes LE: start_min(2B):end_min(2B):home_load_W(2B):charge_priority(2B) |
| **Also via API** | `set_site_device_param` with mode-specific param_type |
| **Verified** | A17C1 FW 1.0.6.10, modes 1+3 |

### Grid Export
| | Details |
|---|---|
| **MQTT cmd** | `0080` (command group: max_load + grid_export) |
| **Fields** | a5=`off_grid_enable?`, a6=`disable_grid_export` (0=allow, 1=disable), a9=`grid_export_limit` |
| **Status** | 0405 field fb (bitmask 0x01) |
| **Also via API** | `set_device_attrs` with `pv_power_limit` attribute |

### AC Input Limit
| | Details |
|---|---|
| **MQTT cmd** | (part of device control, msg type varies) |
| **BLE action** | `action_set_ac_params` |
| **Status** | 0405 field: `ac_input_power?` |

### PV Power Limit
| | Details |
|---|---|
| **API** | `set_device_attrs` with `pv_power_limit` attribute |
| **Validation** | From `get_device_attrs` response: `pv_power_limit`, `legal_power_limit` |

### Device Timeout
| | Details |
|---|---|
| **MQTT cmd** | Device-specific command |
| **Status** | 0405 fields vary |

---

## MQTT-Only Settings (SmartPlug A17X8)

### Plug Switch
| | Details |
|---|---|
| **MQTT cmd** | `007a` |
| **Fields** | a2=`switch` (0=OFF, 1=ON) |
| **Status** | 0405 field a4 (`ac_output_power_switch`) |
| **Verified** | A17X8 FW 0.0.2.7 |

### Plug Schedule
| | Details |
|---|---|
| **MQTT cmd** | `007c` |
| **Fields** | a2=`action` (0=delete, 1=create, 2=modify), a3=`slot` (1-x), a4=`enabled` (0/1), a5=`time` (min:hour), a6=`switch` (0=OFF, 1=ON), a7=`weekdays` (day numbers 1=Mon..7=Sun, variable length) |
| **Options** | a2=[0,1,2], a4=[0,1], a6=[0,1], a7=1-7 per byte |
| **Verified** | A17X8 FW 0.0.2.7, 4 sessions |

### Plug Timer / Countdown
| | Details |
|---|---|
| **MQTT cmd** | `007e` |
| **Fields** | a2=`toggle_switch` (0=cancel, 1=start, 2=pause, 3=resume), a3=`delay_time` (3 bytes LE, seconds), a4=`back_switch`, a5=`back_delay_time` |
| **Status** | 0405 field ad (8 bytes: delay_time[3B] + setting[1B] + status[1B] + elapsed[3B]) |
| **Status values** | status: 0=off, 2=paused, 3=running |
| **Verified** | A17X8 FW 0.0.2.7, pause/resume confirmed |

---

## BLE/IoT SDK Actions (A5101/X1, AX170, A17E1)

These settings use the `akiot.device.invoke_action` or `akiot.device.write_property` path.

### Backup Strategy (AX170)
| | Details |
|---|---|
| **BLE action** | `action_set_backup_strategy` |
| **File** | ax170_command.dart |

### Branch Circuit Config (AX170)
| | Details |
|---|---|
| **BLE action** | `action_set_custom_branch` |
| **File** | ax170_command.dart |

### Connection Sensitivity (AX170)
| | Details |
|---|---|
| **BLE action** | `action_set_connection_sensitivity` |
| **File** | ax170_command.dart |

### Generator / Oil Machine Params
| | Details |
|---|---|
| **BLE actions** | `action_set_oil_machine_params` (A17E1), `action_set_standby_oil_machine_params` (AX170), `action_set_third_oil_params` (A17E1), `action_set_third_oil_AX170`, `action_set_third_oil_type` |

### Heat Pump
| | Details |
|---|---|
| **API** | `set_station_evchargers` with `heat_pump_setting` param |
| **BLE action** | None found (API-only for heat pump) |
| **Fields** | `heat_pump_mode`, `heat_pump_manual_enable`, `heat_pump_min_running_time`, `heat_pump_min_launch_time`, `heat_pump_power` |

### Electricity Price / Grid Code
| | Details |
|---|---|
| **BLE action** | `action_set_electricity_price_and_unit` (A17E1) |
| **BLE action** | `action_set_power_limit_country_code` (init flow) |
| **BLE action** | `action_set_biggest_frequency` (AX170) |

### Distribution Box / Grid Config
| | Details |
|---|---|
| **BLE action** | `action_set_distribution_box` |
| **BLE action** | `action_set_system_self_check` |

### Off-Grid Port Switch (A17E1)
| | Details |
|---|---|
| **BLE action** | `action_set_offline_port_switch`, `action_set_offline_port_switch_memory` |

---

## BLE/IoT SDK Actions (EV Charger A5190)

### Load Balancing
| | Details |
|---|---|
| **BLE action** | `prop_write_load_balancing` |
| **Fields** | `loadBalancingSwitch`, `loadBalancingMainBreakerCurrent`, `maximumCurrentLimit` |

### Green Energy Priority
| | Details |
|---|---|
| **BLE action** | `prop_write_green_energy_priority` |
| **Fields** | `greenEnergyPrioritySwitch`, `greenEnergyPriorityChargingMode`, `greenEnergyPriorityMinOutputCurrent` |

### RFID
| | Details |
|---|---|
| **BLE actions** | `prop_read_rfid`, `prop_write_rfid`, `prop_write_by_evcharger_rfid` |

### OCPP
| | Details |
|---|---|
| **BLE actions** | `prop_read_ocpp_info`, `prop_write_ocpp_info` |

### EV Charger General Config
| | Details |
|---|---|
| **BLE action** | `prop_write_evcharger` |
| **BLE action** | `action_set_schedule` (schedule_ble.dart, ev_charge_command.dart) |

---

## BLE/IoT SDK Actions (PPS / Charger)

### AC/DC/Car Port Params (A1782 PPS)
| | Details |
|---|---|
| **BLE actions** | `action_set_ac_params`, `action_set_bms_params`, `action_set_car_charger_params` |
| **BLE action** | `action_set_tou_system_params`, `action_set_cycle_charging_power` |

### Screen / Display (A2345/A2687)
| | Details |
|---|---|
| **BLE actions** | `action_set_screen_saver_params`, `action_set_screen_off_time`, `action_set_screen_orientation`, `action_set_lcd_backlight_brightness` |

### Charging Protocol (A2687)
| | Details |
|---|---|
| **BLE actions** | `action_set_charging_protocol`, `action_set_charging_fixed_protocol`, `action_set_laboratory_charging_protocol`, `action_set_laboratory_function_switch` |

### DC Port Control (A2687)
| | Details |
|---|---|
| **BLE actions** | `action_set_dc_port_switch`, `action_set_dc_port_countdown` |

### Custom Mode (A2687)
| | Details |
|---|---|
| **BLE actions** | `action_set_custom_mode_delete`, `action_set_custom_mode_switch_type` |

### Charging Schedule (A2693)
| | Details |
|---|---|
| **BLE actions** | `action_set_charging_schedule`, `action_get_charging_schedule` |

### Sleep Mode (A25X7)
| | Details |
|---|---|
| **BLE action** | `action_set_sleep_mode` |

### Gyroscope (A2687)
| | Details |
|---|---|
| **BLE action** | `action_set_gyroscope_switch` |

### Tomato Timer
| | Details |
|---|---|
| **BLE action** | `action_set_tomato_time` |

---

---

## BLE Settings (AS200 Car Charger)

All AS200 settings use a single BLE action `action_set_system_params` with different param keys.

### Temperature Unit
| | Details |
|---|---|
| **BLE action** | `action_set_system_params` |
| **Param** | `{temperatureUnit: <int>}` |

### Shutdown / Standby
| | Details |
|---|---|
| **BLE action** | `action_set_system_params` |
| **Params** | `shutdownStatus` (bool), `shutdownTimeout` (int), `shutdownTimeoutV2` (int), `neverShutdown` (bool) |

### Work Mode
| | Details |
|---|---|
| **BLE action** | `action_set_system_params` |
| **Param** | `{currentWorkMode: <int>}` |

### Power On/Off
| | Details |
|---|---|
| **BLE action** | `action_set_system_params` |
| **Param** | `{powerSwitch: <bool>}` |

### Power & Output Voltage
| | Details |
|---|---|
| **BLE action** | `action_set_system_params` |
| **Params** | `{reverseModePower|chargingModePower: <int>, powerOutVoltage: <int>}` — key depends on work mode |

### Scene / Battery Config
| | Details |
|---|---|
| **BLE action** | `action_set_system_params` |
| **Params** | `batteryType` (int), `batteryVoltageType` (int), `powerUnlock` (int), `lowLoadAutoShutdownTimeout` (int) |

---

## BLE + API Settings (A7320 Generator / Range Extender)

A7320 uses **both** BLE property writes (22 commands) and cloud HTTP API (18 endpoints).

### BLE Settings (via `writeProperty`)

| Setting | BLE Property | Params |
|---------|-------------|--------|
| Screen timeout | `screen_off_time` | timeout value |
| Atmosphere light brightness | `a7320_atmosphere_lights_hrightness` | brightness level |
| Factory reset | `restore_factory_settings` | — |
| Manual exercise start | `manual_workout_start` | exercise params |
| Oil reminder | `remaining_oil_reminder` | remaining value |
| Automatic exercise | `automatic_exercise` | schedule params |
| AC timed shutdown | `timed_shutdown_ac` | timeout |
| AC cancel shutdown | `timed_shutdown_cancel_ac` | — |
| Engine operation control | `engine_operation_control` | control params |
| Gas volume monitoring | `gas_volume_monitoring_switch` | on/off |
| LPG tank remaining | `weight_full_LPG_tank_remaining` | fullTank, remaining, source, typeEngine |
| LPG delete | `added_LPG_delete` | GAS |
| LPG sensor add | `added_LPG_sensor` | sensor params |
| Calendar reminder | `calendar_expiration_reminde` | setTime, setWeek, setMonth, resetSameTime |
| Maintenance update | `maintenance_update` | update data |
| Periodic counter | `periodic_counterr` | counter value |
| Unit of measurement | `unit_of_measurement` | unit |
| Engine operation mode | `oil_engine_operation_mode` | mode |
| Stop engine | `stop_engine` | — |

### Cloud API — Maintenance

| Endpoint | Params |
|----------|--------|
| `set_oil_consumption_reminder_plan` | `device_sn, interval_period_month, interval_period_week` |
| `set_oil_consumption_reminder_switch` | `device_sn, oil_consumption_reminder_switch` |
| `set_oil_machine_exercise_plan` | `device_sn, effective_mode, automatic_exercise, manual_exercise` |
| `start_oil_machine_exercise` | `device_sn, execution_time, execution_result` |
| `set_parts_maintenance_plan` | `device_sn, parts_maintenance_items` |
| `set_maintain_parts_notice_switch` | `device_sn, notice_switch` |
| `set_maintain_parts_ignore_reminders` | `device_sn, item_id, item_name, ignore_reminders` |
| `batch_maintain_oil_engine_parts` | `device_sn, maintenance_items: [{item_id, item_name, description}]` |

### Cloud API — Range Extender System

| Endpoint | Params |
|----------|--------|
| `add_extender_system` | `device_list` |
| `del_extender_system` | `extender_system_id` |
| `set_extender_system_name` | `extender_system_id, extender_system_name` |
| `update_extender_system_strategy` | `extender_system_id, extender_system_params` |
| `batch_add_extender_system_device` | `extender_system_id, device_list` |
| `batch_del_extender_system_device` | `extender_system_id, device_sn_list` |
| `get_strategy_last_record` | `extender_system_id, strategy_type` |

### Strategy Model Fields
```
oilEngineSystemStatus, oilEngineStartCondition,
oilEngineStartSoc, oilEngineStartTime, oilEngineTargetSoc,
oilEngineWorkModeList: [{workMode, startTime, end_time}],
transactionId
```

---

## Summary: Which endpoints to call BEFORE setting a value

| Setting Category | GET first | Response tells you | SET method |
|-----------------|-----------|-------------------|------------|
| Power limit | `get_power_limit`(16) | min, max, step, legal_limit | `set_site_device_param`(19) |
| Home load | `get_device_home_load` | min_load, max_load, step | `set_device_home_load` |
| SOC reserve | `get_site_device_param`(18) | soc_list (available options) | `set_site_device_param`(18) |
| Usage mode | `get_site_device_param`(1-6) | mode constraints, min/max_load | `set_site_device_param` / MQTT `005e` |
| Country code | `get_site_device_param`(20) | current country | `set_site_device_param`(20) |
| 3rd-party PV | `get_site_device_param`(26) | pv_setting flags | `set_site_device_param`(26) |
| Peak shaving | `get_site_device_param`(3) | enable status | `set_site_device_param` |
| Dynamic price | `dynamic_price/support_option` | supported options | `setDynamicPrice` |
| Disaster prep | `check_function` | feature support flags | API set commands |
| LED mode | MQTT status 0405 | current mode | MQTT `0068` |
| Temp unit | MQTT status 0405 | current setting | MQTT `0050` |
| Cutoff | MQTT status 0405 | current values | MQTT `0067` |
| Max load (direct) | `get_power_limit` | power_limit_option | MQTT `0080` |
| Grid export | MQTT status 0405 | current flag | MQTT `0080` (a5/a6) |
| PV limit | `get_device_attrs` | pv_power_limit, legal | `set_device_attrs` |
| Plug switch | MQTT status 0405 | a4 switch state | MQTT `007a` |
| Plug schedule | (none — create directly) | — | MQTT `007c` |
| Plug timer | (none — set directly) | — | MQTT `007e` |
| EV load balance | BLE prop_read | current config | BLE `prop_write_load_balancing` |
| EV green energy | BLE prop_read | current config | BLE `prop_write_green_energy_priority` |
| EV RFID | BLE prop_read | card list | BLE `prop_write_rfid` |
| Generator params | BLE prop_read | current config | BLE `action_set_oil_machine_params` |
| Backup strategy | (via station config) | branch priorities | BLE `action_set_backup_strategy` |
| Heat pump | (via station config) | mode, timing | API `set_station_evchargers` |
| Screen/Display | BLE prop_read | brightness, timeout | BLE `action_set_screen_*` |
| AC/DC ports (PPS) | BLE prop_read | switch states | BLE `action_set_ac/bms/car_params` |
| AS200 work mode | BLE device info | current mode | BLE `action_set_system_params` |
| AS200 power config | BLE device info | mode power, voltage | BLE `action_set_system_params` |
| AS200 shutdown | BLE device info | timeout, never flag | BLE `action_set_system_params` |
| A7320 engine control | BLE device info | engine status | BLE `writeProperty(engine_operation_control)` |
| A7320 exercise/maint | API `get_device_exercise_details` | schedule, logs | API `set_oil_machine_exercise_plan` |
| A7320 oil reminder | API `get_oil_consumption_reminder_plan_details` | interval | API `set_oil_consumption_reminder_plan` |
| A7320 RE strategy | API `get_strategy_last_record` | strategy_type, SOC | API `update_extender_system_strategy` |
