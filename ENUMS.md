# Enum Values and Constants

> Extracted from Blutter object pool (objs.txt) and decompiled Dart code.
> These are the actual values used internally by the Anker App.

## Device Types

### StationDeviceType
| Value | Name |
|-------|------|
| 0 | solarBank |
| 1 | pps |

### DeviceTypeEnum (Range Extender context)
| Value | Name |
|-------|------|
| 0 | undefined |
| 1 | oilMachine |
| 2 | pps |

### ChargingDeviceType
| Value | Name |
|-------|------|
| 0 | chargingPile |
| 1 | largeChargingDevice |
| 2 | mediumChargingDevice |
| 3 | smallChargingDevice |
| 4 | platformDevice |

### ReSystemDevicePnType
| Value | Name | Product Code |
|-------|------|-------------|
| 0 | generatorA7320 | A7320 |
| 1 | ppsA1782 | A1782 |
| 2 | ppsA1790 | A1790 |
| 3 | ppsA1790p | A1790P |

### ANKDeviceType (physical device)
| Value | Name |
|-------|------|
| 0 | phone |
| 1 | tablet |
| 2 | foldable |

## PV Types

### PvType
| Value | Name |
|-------|------|
| 0 | bodyPv |
| 1 | thirdPv |
| 2 | total |

## Battery / Temperature

### BatteryType
Extracted from AS200 settings: LFP (Lithium Iron Phosphate) and LA (Lead Acid)

### RESystemTemperatureUnitEnum
| Value | Name |
|-------|------|
| 0 | celsius |
| 1 | fahrenheit |

### RESystemDeviceLightEnum
| Value | Name |
|-------|------|
| 0 | on |
| 1 | off |

## Connection Status

### ReSystemConnectionStatus
| Value | Name |
|-------|------|
| 0 | loading |
| 1 | notNetworked |
| 2 | networkedOffline |
| 3 | networkedOnline |

### A17EXConnectStatus
| Value | Name |
|-------|------|
| 2 | DisConnected |

## Appliance Types (Smart Plug presets)

### ApplianceType
| Value | Name |
|-------|------|
| 0 | refrigerator |
| 1 | washingMachine |
| 2 | kettle |

## Pricing

### Peak/Valley Price Types
| Value | Name |
|-------|------|
| 1 | peak |
| 2 | normal |
| 3 | valley |
| 4 | super_valley |

### PricePlan
| Value | Name |
|-------|------|
| 1 | fixed |
| 2 | manualTou |

### Dynamic Price Providers
```
Nordpool, Tibber, Flatpeak, Octopus Energy
```

### Supported Countries
```
AT, AU, BE, CN, DE, ES, GB, IT, NL, NZ, PL, US, CA
```

## EMS Modes

### Usage Mode Types
| Value | Name |
|-------|------|
| 0 | unknown |
| 1 | smartmeter |
| 2 | smartplugs |
| 3 | manual |
| 4 | backup |
| 5 | use_time |
| 7 | smart |
| 8 | time_slot |

### EMS Strategy Modes
```
self_consumption, manual_backup, peak_shaving,
custom_mode, time_of_use, smart, dynamic, fixed
```

## Schedule Constants

```
ai_ems, blend_plan, custom_rate_plan, manual_backup,
peak_sessions, peak_valley_prices, use_time
```

### Day Types
```
weekday, weekend, everyday
```

## Disaster Preparedness Template

From object pool — hardcoded schedule template:
```json
[{"start": 1692201600, "end": 1692288000, "type": 1, "soc": 20}]
```

## Backup Mode (charging_disaster_prepared)

| Value | Name | Description |
|-------|------|-------------|
| 0 | AUTO | Weather-based automatic backup |
| 1 | MANUAL | User-defined time window |
| 4 | CLEAR | Disable/clear backup mode |

See `endpoints/charging_disaster_prepared.md` for full API documentation.

## Fault/Error Info Fields

From push notification and fault models:
```
failureCode, failureDesc, failureLevel, failureActualLevel,
failureTime, failureTimeUnix, failureType, handlingSuggestion,
stationId, sn, subSn, pn, compositeSystemId, allow_delete
```

## App Module List (complete feature inventory)

From log module registration:
```
a1903, a2693, analytics, anka_agent, as200, ats_ax170, ax1c0,
balcony, base_service, battery, ble, bluetooth, camera, charging,
charging_enode, common_view, data_sync, database, device_bind,
device_control, device_offline, device_share, device_unbind,
device_update, dynamic_price, electricity_module, electricity_price,
electricity_price_common, ev_charger, file_io, fixed_price,
flutter_ems, http, login, logout, memory, micro_hes, mqtt, network,
notification, oe_a7320, open_meteo, order, payment, performance,
push_service, sensor, third_device, timeslot, tou, tou_pct,
tracking, ui, websocket, wifi
```

## KV Config Model (per-device feature flags)

```
bindConfig, is_share, needCheckBind, needCheckOTA, needUserLogin,
otaConfig, otaLimitType, otaProgressTimeout, requires_bluetooth_pwd,
supportEthernet, support_dual_mode_online
```

---

## EMS Mode Type (with API values)

From objs.txt `EmsModeType` enum — the exact integer values sent to the API:

| Index | Name | API Value |
|-------|------|-----------|
| 0 | selfConsumption | 1 |
| 1 | manualPowerBackup | 4 |
| 2 | timeOfUse | 5 |
| 3 | onlyBackupPower | 8 |
| 4 | severeWeatherMode | 9 |
| 5 | offGrid | 10 |

## AI Mode Enum (with API values)

| Index | Name | API Value |
|-------|------|-----------|
| 0 | Default | 0 |
| 1 | SelfUse | 1 |
| 2 | ModeTypeAdd | 2 |
| 3 | ModeTypeCustom | 3 |
| 4 | ModeTypeManualBackup | 4 |
| 5 | ModeTypeUseTime | 5 |
| 6 | TOUDynamicPrice | 8 |
| 7 | ModeTypeAIEMS | 7 |

## Energy Flow Type (16-bit bitmask)

Each bit represents one energy flow direction:

| Bit | Hex | Name | Description |
|-----|-----|------|-------------|
| 0 | 0x0001 | pvToBattery | PV to battery |
| 1 | 0x0002 | pvToHome | PV to home |
| 2 | 0x0004 | pvToGrid | PV to grid |
| 3 | 0x0008 | thirdPvToBattery | 3rd-party PV to battery |
| 4 | 0x0010 | thirdPvToHome | 3rd-party PV to home |
| 5 | 0x0020 | thirdPvToGrid | 3rd-party PV to grid |
| 6 | 0x0040 | dcToBattery | DC generator to battery |
| 7 | 0x0080 | dcToHome | DC generator to home |
| 8 | 0x0100 | dcToGrid | DC generator to grid |
| 9 | 0x0200 | acToBattery | AC generator to battery |
| 10 | 0x0400 | acToHome | AC generator to home |
| 11 | 0x0800 | acToGrid | AC generator to grid |
| 12 | 0x1000 | gridToBattery | Grid to battery |
| 13 | 0x2000 | gridToHome | Grid to home |
| 14 | 0x4000 | batteryToHome | Battery to home |
| 15 | 0x8000 | batteryToDC | Battery to DC generator |

This maps to the `energy_flow_bits` field in SceneInfo.

## Mode State (SolarBank)

| Value | Name |
|-------|------|
| 0 | forcedRechargeState |
| 1 | sohCalibrationState |
| 2 | socCalibrationState |
| 3 | autoDisasterState |
| 4 | manualDisasterState |
| 5 | fastStopState |
| 6 | lowPowerState |
| 7 | defaultState |

## Mode State (Home Power System)

| Value | Name |
|-------|------|
| 0 | naStatus |
| 1 | selfUserState |
| 2 | timeOfUserState |
| 3 | manualBackupState |
| 4 | automaticBackupState |
| 5 | onlyBackupPower |
| 6 | manualGridOutage |
| 7 | socCalibration |
| 8 | physicalOffGrid |
| 9 | lowSolarInput |
| 10 | forcedRecharge |

## Generator Mode

| Value | Name |
|-------|------|
| 0 | silentDc |
| 1 | saveDc |
| 2 | fastDc |
| 3 | eco |
| 4 | turbo |
| 5 | exerciseAc |
| 6 | exerciseDc |

## PPS Work Status

| Value | Name |
|-------|------|
| 0 | idle |
| 1 | discharge |
| 2 | charge |
| 3 | sleep |
| 4 | shutdown |

## MQTT Command Type

| Value | Name |
|-------|------|
| 0 | normalCommand |
| 1 | otaCommand |
| 2 | a17y0OtaCommand |
| 4 | uploadLogCommand |
| 5 | remoteScanWifi |
| 6 | remoteSwitchWifi |
| 7 | unbindDevice |
| 8 | getDeviceBssid |

## BLE Command Status (response codes)

| Value | Name |
|-------|------|
| 0 | success |
| 1 | fail |
| 2 | accountVerifyFailed |
| 3 | timestampVerifyFailed |
| 4 | parameterVerifyFailed |
| 5 | noMoreData |
| 6 | lowPower |
| 7 | scanWifiFailed |
| 8 | wifiConnectFailedForWrongPwd |
| 9 | wifiConnectFailedForOtherReason |
| 10 | wifiActivateFailedForMissIp |
| 11 | wifiActivateFailedForCommFailed |
| 12 | crc32VerifyFailed |
| 13 | fireWarmVeriryFailed |
| 14 | needAuthentication |
| 15 | passwordWrongAuthenticationFailed |
| 16 | passwordRetryCountExceededAuthenticationFailed |
| 17 | unknown |

## Range Extender Strategy Type

| Value | Name |
|-------|------|
| 1 | bySoc |
| 2 | byTime |

## TOU Season/Period Template

From object pool — hardcoded TOU schedule template:
```json
[{
  "Sea": {"S": 1, "E": 3},
  "P1": [{"S": 0, "E": 8, "T": 1}, {"S": 8, "E": 16, "T": 2}, {"S": 16, "E": 24, "T": 3}],
  "P2": [...]
}]
```
Where S=start, E=end (hours or months), T=type (1=peak, 2=normal, 3=valley)

## IoT Device Product Codes (44 from DeviceConstant)

```
A1722, A1723, A1725, A1726, A1727, A1728, A1729, A1753, A1754, A1755,
A1761, A1762, A1763, A1765, A1771, A1772, A1780P, A1781, A1782, A1783,
A1785, A1790, A1790P, A17A3, A17A4, A17A5, A17B1, A17C0, A17C1, A17C2,
A17C3, A17C5, A17X7, A17X7US, A17X8, A17Y0, A2345, A2693, A7320, A91B2,
SHEM3, SHEMP3, SHPPS, AS100
```

Additional codes from message models:
```
A110A, A110B, A110G, A120J, A1340, A1341, A1770, A1780, A17A0, A17A1,
A17A2, A1903, A25X7, A2687, AE100, AS200
```

Total: **60 unique product codes**
