# Home Energy System (A5101/X1) & Home Power Panel (A17B1) — Response Models

> 14+ models (expanded with nested structures from Blutter decompilation)

## A5101DeviceCommandModel

Source: `model/a5101/a5101_device_command_model.dart`

### Top-Level Fields (GET response from `get_device_command`)

```
conserve_percent       int     Battery conservation percentage (0-100)
day_type               string  "weekday" | "weekend" | "everyday"
evcharger_enable       bool    EV charger enabled
last_select_mode       int     Last selected operation mode
main_sn                string  Main device serial number
off_grid_enable        bool    Off-grid mode enabled
radar                  bool    Radar/proximity sensor control
scanning_switch        bool    Scanning switch enabled
soc                    int     State of charge (0-100)
template_id            string  Schedule template ID
```

### Full SET Request (to `device_command`)

28 parameters allocated (60-element array), key fields:

```
station_id             string  Station identifier
main_sn                string  Main device serial number
time                   string  Timestamp (auto-generated if null)
electricity_strategy   object  → ElectricityStrategy
add_diesel             object  → A5101Diesel
screen_setting         object  Screen settings
utility_rate_plan      object  → UtilityRatePlan
ack_peak_valley        int     Acknowledge peak/valley config
advanced_setting       object  → AdvancedSetting (required)
heat_pump_setting      object  → HeatPumpModel
accuracy               int     Fixed value: 10
cls_reset              string  CLS reset flag (required)
off_grid_switching     object  → OffGridSwitching (required)
evcharger_setting      object  EV charger settings
version                string  API version ("1.0.0")
```

### Additional Response Fields (from fromJson parsing)

```
time_zone              string  Timezone string
cls_status             int     CLS status
price_source_type      int     Price source type
price_source_sub_type  int     Price source sub-type
history_schedule_mode  object  → HistoryScheduleMode
```

### Nested: ElectricityStrategy

```json
{
  "conserve_percent": 20,
  "mode": 1,
  "isAuthorizeAIEms": false,
  "isEnableSmartMode": false
}
```

Mode values map to EmsModeType:
| Value | Name |
|-------|------|
| 1 | selfConsumption |
| 4 | manualPowerBackup |
| 5 | timeOfUse |
| 8 | onlyBackupPower |
| 9 | severeWeatherMode |
| 10 | offGrid |

### Nested: OffGridSwitching

```json
{
  "off_grid_enable": 1,
  "off_grid_sensitivity": 3
}
```

### Nested: HeatPumpModel

```json
{
  "add_or_delete_heat_pump": null,
  "heat_pump_state": 0,
  "heat_pump_power": 0,
  "heat_pump_mode": "auto",
  "heat_pump_plan": {},
  "heat_pump_manual_enable": false,
  "heat_pump_min_launch_time": 0,
  "heat_pump_min_running_time": 0
}
```

### Nested: AdvancedSetting

```json
{
  "arc_fault_circuit_interrupter": null,
  "rapid_shutdown": null,
  "respons_enabled_device": null,
  "ripple_control": null
}
```

## A5101DeviceListModel

Source: `model/a5101/a5101_device_list_model/a5101_device_list_model.dart`

*(no fields extracted)*

## A5101EvChargerListModel

Source: `model/a5101/a5101_ev_charger_list_model.dart`

```
deviceSn, evChargers, userBindEvChargersCount
```

## A5101EventsSetModel

Source: `model/a5101/auto_disaster_prepare_status_model.dart`

```
code
```

## A5101InstallAddressModel

Source: `ui/page/device/a5101/setting/install_address/a5101_install_address_model.dart`

```
installLocation
```

## A5101InstallInformationModel

Source: `ui/page/device/a5101/setting/install_information/a5101_install_information_model.dart`

```
companyName
```

## A5101StationGridConfigModel

Source: `model/a5101/a5101_station_grid_config_model.dart`

```
afci                   object  Arc Fault Circuit Interrupter
  config               object  AFCI configuration
  status               object  AFCI status
rsd                    object  Residual current device
  config               object  RSD configuration
  status               object  RSD status
dred                   object  DRED configuration/status
rcr                    object  RCR configuration/status
```

## AutoDisasterDetailModel

Source: `model/a5101/auto_disaster_detail_model.dart`

```
uuid                   string  Unique disaster event ID
event                  string  Disaster event type
start                  int     Event start time (unix timestamp)
end                    int     Event end time (unix timestamp)
isErrorData            bool    Error data flag
```

## AutoDisasterPrepareStatusModel

Source: `model/a5101/auto_disaster_prepare_status_model.dart`

```
code                   int     Status code
```

## AutoDisasterQuitPrepareModel

Source: `model/a5101/auto_disaster_quit_prepare_model.dart`

```
success
```

## CheckFunctionModel

Source: `model/a5101/check_function_model.dart`

```
auto_disaster          bool    Auto disaster feature enabled
net_energy_meter       bool    Net energy meter support
peak_shaving           bool    Peak shaving available
ems_disable            bool    EMS can be disabled
soft2                  list    Soft2 feature flag (list of int)
smartModeInfo          object  → SmartModeInfo
support                object  Support details
```

## DisasterPrepareDetailsModel

Source: `model/a5101/disaster_prepare_details_model.dart`

```
start_time             int     Preparation start time (unix timestamp)
autoDisasterInfoList   list    List of AutoDisasterDetailModel objects
```

## HesProductsInfoModel

Source: `model/a5101/hes_products_info_model.dart`

```
category
```

## VppInfoModel

Source: `ui/page/device/a5101/setting/vpp/vpp_info_model.dart`

```
lastVersion, name, vppEnable
```

