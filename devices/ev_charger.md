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

## MQTT

thomluther noted (Issue #271): EV Charger commands require **encoding type 2** with a 16-byte random seed. No dedicated EV MQTT command codes found in APK — commands flow through `evcharger_setting` parameter in HES `sendDeviceCommand`.

## What's needed from device owners

Per thomluther (Issue #322):
1. System exports as **owner account** (not shared)
2. EV charger must be **added to a system** (not standalone)
3. Vehicles should be configured
4. MQTT monitoring during charging sessions
