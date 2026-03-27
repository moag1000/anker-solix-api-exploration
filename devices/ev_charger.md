# EV Charger V1 — A5190 / A5191

> **Priority**: P2 (High demand) — actively requested in upstream Issues
> [ha-anker-solix #322](https://github.com/thomluther/ha-anker-solix/issues/322) |
> [anker-solix-api #271](https://github.com/thomluther/anker-solix-api/issues/271)

## Product Info

- **A5190** — APK internal code
- **A5191** — Shipping product (SOLIX V1 Smart EV Charger, 11-22kW, EU)
- Consumer wallbox, sold on ankersolix.com EU
- Supports: WiFi, 485 (Modbus), BLE, phase auto-switching

## API Endpoints (35)

Full list in [endpoints/device_specific.md](../endpoints/device_specific.md#ev-charger-endpoints-a5190--p2)

### Vehicle Management (11)
| Endpoint | Function | Key Params |
|----------|----------|-----------|
| `/power_service/v1/app/vehicle/get_vehicle_list` | getEvList | |
| `/power_service/v1/app/vehicle/add_vehicle` | addEv | `user_vehicle_info` |
| `/power_service/v1/app/vehicle/delete_vehicle` | deleteEv | `vehicle_id` |
| `/power_service/v1/app/vehicle/set_default` | setDefaultEv | `vehicle_id` |
| `/power_service/v1/app/vehicle/get_vehicle_detail` | getEvDetail | `vehicle_id` |
| `/power_service/v1/app/vehicle/update_vehicle` | updateEv | |
| `/power_service/v1/app/vehicle/set_charging_vehicle` | setChargingVehicle | `vehicle_id` |
| `/power_service/v1/app/get_brand_list` | getEvBrandList | |
| `/power_service/v1/app/get_model_list` | getEvVersionList | |
| `/power_service/v1/app/get_model_years` | getEvYearList | |
| `/power_service/v1/app/get_models` | getEvModelList | |

### Charging Sessions (8)
| Endpoint | Function | Key Params |
|----------|----------|-----------|
| `.../order/get_charging_order_list` | getChargeSessions | `order_status` |
| `.../order/get_charging_order_detail` | getSessionsDetail | |
| `.../order/get_charge_order_stats_list` | getChargerSessionOrderList | `order_status` |
| `.../order/get_charge_order_stats` | getChargeSessionChartModel | |
| `.../order/get_charging_order_sec_preview` | getSessionsOrderSecPreview | `order_id` |
| `.../order/get_charging_order_sec_detail` | getSessionsOrderSecDetail | `order_id` |
| `.../order/export_charge_order` | fetchExportChargeOrderUrl | |
| `.../order/delete_charging_order` | deleteChargingSession | `order_id` |

### RFID (3), Groups (5), OCPP (2), Security (2), Sharing (5), HES Integration (4), Faults (2)

See [device_specific.md](../endpoints/device_specific.md#ev-charger-endpoints-a5190--p2) for full list.

## BLE Actions (from APK decompilation)

| Action | Fields |
|--------|--------|
| `prop_write_evcharger` | `rechargingPowerOutage, plugAndChargeSwitch, carChargerLockStatus, maximumCurrentLimit, delayStartSwitch, lightBrightness, ledSwitch, ledCloseStartTime, ledCloseEndTime` |
| `prop_write_load_balancing` | `loadBalancingSwitch, loadBalancingMainBreakerCurrent, maximumCurrentLimit` |
| `prop_write_green_energy_priority` | `greenEnergyPrioritySwitch, greenEnergyPriorityChargingMode, greenEnergyPriorityMinOutputCurrent` |
| `prop_read_rfid` / `prop_write_rfid` | RFID card management |
| `prop_read_ocpp_info` / `prop_write_ocpp_info` | OCPP configuration |
| `action_set_schedule` | Charging schedule via BLE |

## Related Files in This Repo

- [PARAM_DATA_STRUCTURES.md](../PARAM_DATA_STRUCTURES.md#ev-charger-operations) — Driving plan, RFID, smart charging payloads
- [VALIDATION_MODEL.md](../VALIDATION_MODEL.md) — BLE action fields for load balancing, green energy priority
- [ENUMS.md](../ENUMS.md) — Product codes, charging device types
- [JSON_EXAMPLES.md](../JSON_EXAMPLES.md) — Schedule defaults, control settings
- [models/hes.md](../models/hes.md) — A5101EvChargerListModel, A5101DeviceCommandModel
- [ENDPOINT_FIELDS.md](../ENDPOINT_FIELDS.md) — bindUnX1Charger (camelCase), sendDeviceCommand
- [REQUIRED_FIELDS.md](../REQUIRED_FIELDS.md#charging_hes_svcset_station_evchargers) — bindUnX1Charger required/optional

## Data Structures (structurally inferred)

### Smart Charging — Driving Plan
```json
{"driving_plan": [{"vehicleId": "...", "targetSoc": 80, "departureTime": "08:00",
  "everyday": false, "weekday": true, "weekend": false}]}
```

### RFID Card
```json
{"device_sn": "...", "card_number": "...", "alias_name": "..."}
```

### HES Binding (camelCase!)
```json
{"stationId": "...", "evChargers": [...], "deleteFlag": false, "forceBindFlag": false}
```

### Push Notification Config
```json
{"disturb_scenes": {"start_charging": true, "stop_charging": true,
  "paused_charging": true, "paused_car_charging": true,
  "restore_charging": true, "smart_charging": true, "boost_charging": true}}
```

## MQTT/BLE Command → TLV Tag → APK Field Name Mapping

Cross-referenced from APK decompilation (field names) + upstream mqttcmdmap.py (TLV tags).
The IoT framework maps `prop_write_*` field names to TLV tags at the protocol layer.

> **Confidence**: Tag assignments are inferred by correlating the APK field names with
> thomluther's device-tested TLV mappings. Fields marked "?" need device verification.

### Charge Control (encoding_type=2, via `action_control_charging`)

| APK Field | TLV Tag | Values | Upstream Name |
|-----------|---------|--------|---------------|
| `controlType` | a2 | 1=Start, 2=Stop, 3=SkipDelay, 4=Boost | `ev_charger_mode` |

### Device Settings (via `prop_write_evcharger`)

| APK Field | TLV Tag | Type/Range | Upstream Name |
|-----------|---------|-----------|---------------|
| `carChargerLockStatus` | a3 | 1=off, 2=on (bit-shifted) | `plug_lock_switch` |
| `plugAndChargeSwitch` | a4 | 0=off, 1=on | `ev_auto_start_switch` |
| `maximumCurrentLimit` | a8 | 6-32A (int, divider 0.1) | `ev_max_charge_current` |
| `lightBrightness` | aa | 0-100% | `light_brightness` |
| `rechargingPowerOutage` | ac | 0=off, 1=on | `ev_auto_charge_restart_switch` |
| `delayStartSwitch` | ad | 0=off, 1=on | `ev_random_delay_switch` |
| `ledSwitch` | b4 | on/off | `light_off_schedule` (switch) |
| `ledCloseStartTime` | b5 | "HH:MM" | `light_off_schedule` (start) |
| `ledCloseEndTime` | b6 | "HH:MM" | `light_off_schedule` (end) |
| `modbusTcpSwitch` | b7 | 0=off, 1=on (left-shifted by 1) | `modbus_switch` |
| `ioDetectionSwitch` | ? | 0=off, 1=on | **NEW — not in upstream** |
| `ioDetectionType` | ? | int | **NEW — digital input type** |
| `ioDetectionMaxCurrent` | ? | int (A) | **NEW — digital input max current** |
| `initSettings` | ? | 2 = init complete | **NEW — init completion flag** |

### Solar Charging / Green Energy Priority (via `prop_write_green_energy_priority`)

| APK Field | TLV Tag | Notes | Upstream Name |
|-----------|---------|-------|---------------|
| `greenEnergyPrioritySwitch` | a2 | on/off | `solar_evcharge_switch` |
| `greenEnergyPriorityChargingMode` | a3 | 0=solar+grid, 1=solar only | `solar_evcharge_mode` |
| `greenEnergyPriorityMinOutputCurrent` | a4 | 6-16A | `solar_evcharge_min_current` |
| `greenEnergyPriorityConnectedType` | a5? | phase mode (1=1P, 3=3P) | `phase_operating_mode?` |
| `greenEnergyPriorityConnectionMode` | a6? | monitoring mode | `solar_evcharge_monitoring_mode?` |
| `greenEnergyPriorityThreePhaseSwitch` | a7 | auto phase switch | `auto_phase_switch` |
| `greenEnergyPriorityConnectedId` | a8 | device SN (16 bytes) | `solar_evcharge_monitor_device` |

### Load Balancing (via `prop_write_load_balancing`)

| APK Field | TLV Tag | Notes | Upstream Name |
|-----------|---------|-------|---------------|
| `loadBalancingSwitch` | a2 | on/off | `load_balance_switch` |
| `loadBalancingMainBreakerCurrent` | a3? | 10-500A | `main_breaker_limit` |
| `loadBalancingConnectedType` | a4? | — | `load_balance_setting_d5?` |
| `loadBalancingConnectionMode` | a5? | — | `load_balance_setting_d6?` |
| `loadBalancingConnectedId` | a6 | device SN (16 bytes) | `load_balance_monitor_device` |

### Schedule (via `action_set_schedule`)

| APK Field | TLV Tag | Notes | Upstream Name |
|-----------|---------|-------|---------------|
| `schedChargeSwitch` | a2 | 1=on, 2=off (inverted!) | `ev_schedule_switch` |
| `chargerMode` | ? | 0 = default | — |
| `weekdayStartHour/Min` | a3? | HH:MM split | `ev_week_start_time` |
| `weekdayEndHour/Min` | a4? | HH:MM split | `ev_week_end_time` |
| `weekendStartHour/Min` | a5? | HH:MM split | `ev_weekend_start_time` |
| `weekendEndHour/Min` | a6? | HH:MM split | `ev_weekend_end_time` |
| `everyDaySwitch` | ? | same weekday/weekend | — |

### Other Actions

| Action | Property ID | Fields |
|--------|------------|--------|
| RCD Test | `action_rcd_test` | (none — trigger only) |
| Disconnect | `action_disconnect_function` | `disconnectFunction` — **NEW** |
| OCPP Config | `prop_write_ocpp_info` | `ocppName` + 6 more fields |
| RFID Write | `prop_write_rfid` | card data |
| RFID Read | `prop_write_by_evcharger_rfid` | — |

### Key Insight: encoding_type 2

Only `action_control_charging` (start/stop/boost) and `device_power_mode` (restart) use
encoding type 2 with 16-byte random seed. All other commands use standard encoding.
The APK routes these through `invokeAction` (not `writeProperty`), which is a different
code path in the IoT framework.

## What's needed from device owners

Per thomluther (Issue #322):
1. System exports as **owner account** (not shared)
2. EV charger must be **added to a system** (not standalone)
3. Vehicles should be configured
4. MQTT monitoring during charging sessions
5. The field→tag mapping above can be **quickly verified** by changing one setting
   and checking which TLV tag changes in mqtt_monitor
