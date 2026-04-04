# Home Power Panel (A17B1)

> SOLIX Home Power Panel — gateway for SOLIX F3800 battery system
>
> **Product Code**: A17B1
> **Device Type**: `powerpanel` / `SolixDeviceType.POWERPANEL`
> **Site Type**: `t_4` (mapped to `SolixDeviceType.POWERPANEL`)
> **Virtual Capacity**: Inherits from A1790 (F3800) = 3840 Wh per unit
>
> **Relevant Issues**: [ha-anker-solix #480](https://github.com/thomluther/ha-anker-solix/issues/480), #447

## Communication Channels

| Channel | Support | Details |
|---------|---------|---------|
| **MQTT Status** | Read-only | JSON format via topic `{SN}/0505/a2` (not binary TLV) |
| **MQTT Commands** | None | Zero entries in `mqttcmdmap.py` — "Minimal-Command Device" |
| **BLE** | Minimal | Only Realtime Trigger (0x0057) + EV Charger BLE commands |
| **Cloud API** | **Primary** | 3 service layers (see below) |

**Key constraint**: HPP is controlled exclusively via Cloud API. MQTT delivers status only.
BLE is disabled when WiFi is active (see `feedback_ble_wifi_exclusion.md`).

## API Service Layers

The HPP uses **three separate Cloud API service prefixes**:

| Service | Purpose | Endpoint Count |
|---------|---------|---------------|
| `charging_energy_service/` | Energy data, configs, rate plans, firmware | 12+ |
| `charging_hes_svc/` | Device commands, station config, EV charger binding | 28+ |
| `charging_disaster_prepared/` | Backup/disaster mode control (auto + manual) | 5+ |

## MQTT Status Fields (_PP_JSON)

Topic: `{DEVICE_SN}/0505/a2` — JSON payload with abbreviated keys.

### Power Flow

| Key | Mapped Name | Unit | Notes |
|-----|-------------|------|-------|
| `bp` | `battery_power_signed` | W | Negative = charging (FACTOR: -1) |
| `pp` | `photovoltaic_power` | W | |
| `gp` | `grid_power_signed` | W | |
| `lp` | `home_demand` | W | |
| `p2lp` | `pv_to_home_power` | W | |
| `p2bp` | `pv_to_battery_power` | W | |
| `p2gp` | `pv_to_grid_power` | W | |
| `b2lp` | `battery_to_home_power` | W | |
| `b2gp` | `battery_to_grid_power` | W | |
| `g2bp` | `grid_to_battery_power` | W | |
| `g2lp` | `grid_to_home_power` | W | |

### State Fields

| Key | Mapped Name | Values |
|-----|-------------|--------|
| `soc` | `battery_soc` | 0-100% |
| `m` | `mode` | 0=off, 1=on, 2=auto |
| `gs` | `grid_status` | 0=offline, 1=online |
| `bs` | `battery_status` | 0=Standby, 1=Charging, 2=Discharging |
| `ps` | `plant_status` | 0=Off, 1=On-grid |
| `ws` | `working_status` | |
| `bc` | `pps_count` | Number of attached F3800 units |

### Battery Array (`bds`)

List of PPS (F3800) data dicts:
```json
[{"sn": "<pps_sn>", "soc": 61, "power": -1148, "error": 0}]
```

### Settings & Schedule

| Key | Mapped Name | Default | Notes |
|-----|-------------|---------|-------|
| `cp` | charge_percent_target | 40 | Battery reserve percentage |
| `rp` | rate_plan | [] | Schedule array |
| `dpp` | discharge_power_plan | [] | Discharge plan |
| `pu` | power_usage_mode | 0 | |

### Firmware & System

| Key | Name | Type |
|-----|------|------|
| `mv` | main_firmware_version | string |
| `mdv` | module_detail_version | string |
| `tv` | total_version | string |

### Diesel/Generator Extension

| Key | Name |
|-----|------|
| `hasDiesel` | Has diesel generator |
| `dieselState` | Diesel generator state |
| `o2lp` / `o2lpu` | Output2 load power / unit |
| `o2pp` / `o2ppu` | Output2 PV power / unit |

## Mode State (Home Power System)

| Value | Name | Description |
|-------|------|-------------|
| 0 | naStatus | N/A |
| 1 | selfUserState | Self-consumption |
| 2 | timeOfUserState | Time-of-use |
| 3 | manualBackupState | Manual backup active |
| 4 | automaticBackupState | Auto backup (weather) active |
| 5 | onlyBackupPower | Backup-only mode |
| 6 | manualGridOutage | Manual grid outage simulation |
| 7 | socCalibration | SOC calibration |
| 8 | physicalOffGrid | Physical off-grid |
| 9 | lowSolarInput | Low solar input |
| 10 | forcedRecharge | Forced recharge |

## EmsModeType (API values for device_command)

| Index | Name | API Value |
|-------|------|-----------|
| 0 | selfConsumption | 1 |
| 1 | manualPowerBackup | 4 |
| 2 | timeOfUse | 5 |
| 3 | onlyBackupPower | 8 |
| 4 | severeWeatherMode | 9 |
| 5 | offGrid | 10 |

## Backup/Disaster Mode Control

> Full flow analysis: `endpoints/charging_disaster_prepared.md`

### Two Independent Modes

| Mode | Trigger | API field | Time format |
|------|---------|-----------|-------------|
| **Auto Disaster** | Server-side weather alerts | `auto_disaster_switch` (bool) | Server-controlled |
| **Manual Disaster** | User picks time window | `manual_disaster_switch` (bool) + `manual_disaster_detail` | Unix timestamps |

Both can be active simultaneously.

### Cloud API Flow (what thomluther should implement)

**Enable manual backup**:
```json
POST /charging_disaster_prepared/set_site_device_disaster
{
  "type": "<device_type_int>",
  "identifier_id": "<site_id>",
  "manual_disaster_switch": true,
  "manual_disaster_detail": {
    "disaster_type": 4,
    "start_time": 1712160000,
    "end_time": 1712246400
  }
}
```

**Disable manual backup**:
```json
{
  "type": "...", "identifier_id": "...",
  "manual_disaster_switch": false
}
```

**Read current settings**:
```
GET /charging_disaster_prepared/get_site_device_disaster
→ DisasterSetting { auto_disaster_switch, manual_disaster_switch, disaster_details[] }
```

**Check feature support**:
```
GET /charging_disaster_prepared/get_support_func
→ SupportFunc { support_auto_disaster, support_country_code[] }
```

### Key Models (Cloud API — from device_disaster_model.dart)

**DisasterSetting** (size 0x30, extends ChangeNotifier):
```
auto_disaster_switch     bool    Auto disaster enabled
manual_disaster_switch   bool    Manual disaster enabled
disaster_details         list    Active events → List<DisasterEvent>
```

**DisasterStatus** (size 0x1c):
```
auto_disaster_status     int     Auto status (0 = inactive)
manual_disaster_status   int     Manual status (0 = inactive)
current_disaster_detail  object? → DisasterPrepareDetail (nullable)
```

**DisasterPrepareDetail**:
```
uuid            string   Event ID
event           string   Event name
event_key       string?  Event key
start_time      int      Unix timestamp
end_time        int      Unix timestamp
charging_time   int?     Charging duration
disaster_type   int      Type (4 = manual)
```

### BLE Battery Reserve Command

Separate from disaster system. Via BLE `sendA17B1Command()`:
- Command: `"scp"` [pp+0x757f8] (set cycle percent)
- Parameter: battery reserve value (0-100)
- Followed by `syncSiteConfig()` HTTP to persist
- BLE opcodes: 0x233 (response), 0x45a (dismiss)

## Device Command Control

### electricity_strategy (nested in device_command)

```json
{
  "electricity_strategy": {
    "conserve_percent": 20,
    "mode": 1,
    "isAuthorizeAIEms": false,
    "isEnableSmartMode": false
  }
}
```

### off_grid_switching (nested in device_command)

```json
{
  "off_grid_switching": {
    "off_grid_enable": 1,
    "off_grid_sensitivity": 3
  }
}
```

## EMS Strategy Modes

```
self_consumption, manual_backup, peak_shaving,
custom_mode, time_of_use, smart, dynamic, fixed
```

## Dart UI Pages (Blutter Decompilation)

| Page | Path | Purpose |
|------|------|---------|
| A17B1HomePage | `device/a17b1/device_home/` | Main device view |
| A17B1SystemPolicyLogic | `device/a17b1/system_policy/` | Backup/disaster strategy |
| A17B1ManualBackupPowerLogic | `device/a17b1/device_setting/manual_backup_power/` | Manual backup config |
| A17B1DeviceSettingLogic | `device/a17b1/device_setting/` | Device settings root |
| A17B1ElectricitySceneLogic | `device/a17b1/a17b1electricity_scene/` | Electricity management |
| A17B1FixedRateLogic | `device_setting/utility_rate_plan/fixed_rate/` | Fixed rate plan |
| A17B1SystemTestLogic | `device/a17b1/a17b1system_test/` | Diagnostics |
| A17B1FirmwareLogic | `device/a17b1/a17b1firmware/` | OTA updates |
| A17B1SelectDevicesLogic | `device/a17b1/a17b1select_devices/` | Device binding |
| ThirdAtsSetting | `device_setting/third_ats_setting/` | ATS configuration |

### Station-Level Pages

| Page | Path | Purpose |
|------|------|---------|
| A17b1StationLogic | `station/A17b1/` | Station overview |
| A17B1AutoDisasterMixin | `station/A17b1/` | Auto disaster handling |
| AutoDisasterSetting | `station/view/auto_disaster/` | Auto disaster config |
| ManualDisasterSetting | `station/view/auto_disaster/` | Manual disaster config |

## BLE Device Files

| File | Class | Purpose |
|------|-------|---------|
| `a17b1_anker_device.dart` | A17B1AnkerDevice | Core device abstraction |
| `a17b1_device_commands.dart` | A17B1DeviceCommands | Command parsing (static) |
| `a17b1_device_controller.dart` | A17B1DeviceController | Dual protocol: ZX BLE + MQTT |
| `mqtt_set_order_model.dart` | MqttSetOrderModel | MQTT command serialization |

### Command Architecture

- Dual protocol stack: `ZXCommandTransformer` (BLE) + `MqttCommandTransformer` (MQTT)
- `sendA17B1Command()` assembles: `{messageId, config, cmdId, data}`
- `handleMQTTDeviceResponse()` and `handleZXProtocolDeviceResponse()` for response handling

## Python API Implementation

### AnkerSolixPowerpanelApi (powerpanel.py, 1452 lines)

| Method | Lines | Purpose |
|--------|-------|---------|
| `_update_dev()` | 78-204 | Device data consolidation, A17B1→A1790 capacity mapping |
| `update_sites()` | 206-377 | Main site update, processes `powerpanel_list` |
| `update_site_details()` | 379-420 | Less-frequent detail updates |
| `update_device_energy()` | 422-494 | Energy statistics |
| `get_system_running_info()` | 518-581 | Cumulative runtime stats |
| `get_avg_power_from_energy()` | 583-858 | 5-min average power from multi-source energy |
| `energy_statistics()` | 860-921 | Core energy query (hes, solar, home, grid, pps, diesel) |
| `energy_daily()` | 923-1317 | Daily energy aggregation |
| `extract_energy()` | 1319-1452 | Energy extraction helper |

### API_CHARGING_ENDPOINTS (apitypes.py)

Currently implemented (12):
```python
"get_error_info", "get_system_running_info", "energy_statistics",
"get_rom_versions", "get_device_info", "get_wifi_info",
"get_installation_inspection", "get_utility_rate_plan",
"report_device_data", "get_configs", "get_sns", "get_monetary_units"
```

**Not implemented** (6 known):
```
sync_installation_inspection, sync_config, restart_peak_session,
preprocess_utility_rate_plan, ack_utility_rate_plan, adjust_station_price_unit
```

## Implementation Gaps (for ha-anker-solix)

### Critical for Issue #480

1. **`charging_disaster_prepared/` endpoints** — Entire service layer missing from Python API
2. **`charging_hes_svc/device_command`** — SET endpoint not implemented
3. **`charging_hes_svc/get_device_command`** — GET counterpart not implemented
4. **DisasterPreparednessInfo model** — Not defined in Python
5. **ElectricityStrategy model** — Not defined in Python
6. **OffGridSwitching model** — Not defined in Python

### Secondary Gaps

7. `charging_hes_svc/check_function` — Feature detection (auto_disaster support)
8. `charging_energy_service/get_configs` — param_types still unknown
9. `charging_hes_svc/get_station_config_and_status` — Station grid config
10. Disaster-prepare status/detail/quit endpoints
