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
