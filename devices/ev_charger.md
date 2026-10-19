> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Page type: device · Owner page: this page

# EV Charger V1 — A5190 / A5191

Row numbers ("audit row N") count the table rows of [../docs/audit/devices.md](../docs/audit/devices.md) from the top; this page consumes rows 51 to 74. Method, tags and the Smi rule: [../METHODOLOGY.md](../METHODOLOGY.md). All code sites are in `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` unless another file is named.

## PN, marketing name, generation/family

- `A5190`: APK-internal product code. `A5191`: shipping product, SOLIX V1 Smart EV Charger, 11 to 22 kW, EU. Consumer wallbox sold on ankersolix.com EU. Supports WiFi, RS-485 (Modbus), BLE and phase auto-switching. Source: old page and upstream issues [ha-anker-solix #322](https://github.com/thomluther/ha-anker-solix/issues/322) and [anker-solix-api #271](https://github.com/thomluther/anker-solix-api/issues/271) (upstream-confirmed; audit row 74 NOT-FROM-ASM). Product codes: [../reference/enums.md](../reference/enums.md).

## Features matrix

| feature | API (link) | MQTT (link) | BLE / IoT kit (link) | device-tested? |
|---|---|---|---|---|
| start, stop, skip delay, boost | none | unknown | `action_control_charging` property write, flow [ev_charger_start_charging](../flows/ev_charger_start_charging.md), values [ChargeControlType](../models/ev_charger_device_models.md#chargecontroltype-ev-charger-command-value) | no |
| device settings (`prop_write_evcharger`) | none | unknown; candidate tags below | [iot_kit_channels](../reference/iot_kit_channels.md), [sdk_senders](../api/sdk_senders.md) | no |
| load balancing, green energy priority | none | unknown; candidate tags below | same | no |
| charging schedule | none | unknown | `action_set_schedule` (invokeAction) | no |
| OCPP, RFID | `get_ocpp_info` and device-card endpoints, see [device_specific](../endpoints/device_specific.md#ev-charger-endpoints-a5190--p2) | unknown | same | no |
| Modbus TCP switch | none | unknown (upstream has `b7`, `modbus_switch`) | [modbus](modbus.md#ev-charger-modbus-tcp-device-properties) | no |
| vehicles, sessions, groups, sharing | 42 endpoints in nine groups, see below | none | none | no |

## API endpoint groups

The old page counted 35 endpoints; its own sub-lists add up to 42 (11, 8, 3, 5, 2, 2, 5, 4, 2) and [../endpoints/device_specific.md](../endpoints/device_specific.md#ev-charger-endpoints-a5190--p2) has 42 endpoint lines in the EV charger section (audit rows 51 to 54, prose counts). Groups: Vehicle Management 11, Charging Sessions 8, RFID 3, Groups 5, OCPP 2, Security 2, Sharing 5, HES Integration 4, Faults 2. Per-endpoint payloads: the pages under [../api/power_service/app/](../api/README.md) (for example [add_vehicle](../api/power_service/app/vehicle/add_vehicle.md)); the old per-endpoint tables are removed here. The HES binding body uses camelCase keys (`stationId`, `evChargers`, `deleteFlag`, `forceBindFlag`), see [../endpoints/device_specific.md](../endpoints/device_specific.md) and [set_station_evchargers](../api/charging_hes_svc/set_station_evchargers.md).

## MQTT/BLE Command → TLV Tag → APK Field Name Mapping

The Dart code passes field names to the IoT kit; the framework maps them to wire tags below the Dart layer, so the app names no tag (audit row 59). The names and values below are asm facts; the tag column is a candidate table at the end of this section.

### IoT-kit actions and property writes

Tag: asm-traced.

- `prop_write_evcharger`: `rechargingPowerOutage`, `plugAndChargeSwitch`, `carChargerLockStatus` (`ev_charge_command.dart` `setCarChargerLockStatus` @0x2cdf80c), `maximumCurrentLimit` (`setMaximumCurrentLimit` @0x2ce0b20, name literal @0x2ce0b18), `delayStartSwitch`, `lightBrightness`, `ledSwitch`, `ledCloseStartTime`, `ledCloseEndTime`, `modbusTcpSwitch`, `ioDetectionSwitch`, `ioDetectionType`, `ioDetectionMaxCurrent`, `initSettings`.
- `prop_write_load_balancing`: `loadBalancingSwitch`, `loadBalancingMainBreakerCurrent`, `loadBalancingConnectedType`, `loadBalancingConnectionMode`, `loadBalancingConnectedId`, `maximumCurrentLimit`.
- `prop_write_green_energy_priority`: `greenEnergyPrioritySwitch`, `greenEnergyPriorityChargingMode`, `greenEnergyPriorityMinOutputCurrent`, `greenEnergyPriorityConnectedType`, `greenEnergyPriorityConnectionMode`, `greenEnergyPriorityThreePhaseSwitch`, `greenEnergyPriorityConnectedId`.
- `prop_write_ocpp_info` (`ev_charge_command.dart` `writeOcppServerInfo` @0x3973df0): seven key/value pairs, `ocppName`, `ocppIconPath`, `ocppAddress`, `ocppType`, `ocppCbid`, `ocppAuthorizationKey`, `ocppCertificatePath` (raw 28 before `AllocateArray`, 28 / 2 = 14 slots = 7 pairs; audit row 70). `prop_read_ocpp_info`, `prop_read_rfid` and `prop_write_rfid` also exist (old page).
- `action_control_charging` goes through `writeProperty`, not `invokeAction` (`ev_charge_command.dart` `setControlType` @0x39447d4; `ak_iot_kit_manager_impl.dart` `writeProperty` @0x228fec8, channel `akiot.device.write_property` @0x228ff28; audit row 72). `action_set_schedule` (`schedule_ble.dart` @0x39685f8) and `action_restart_device` (`basic_command.dart` @0x2ce2b54) use `invokeAction`. Others in the old table: `action_rcd_test`, `action_disconnect_function` (field `disconnectFunction`), `prop_write_by_evcharger_rfid`.

### Values the app writes

| APK field | value | tag |
|---|---|---|
| `controlType` | 1 start, 2 stop, 3 skip delay, 4 boost, owner [ChargeControlType](../models/ev_charger_device_models.md#chargecontroltype-ev-charger-command-value) (pool object `off_14`, `ev_charge_command.dart` `setControlType` @0x3944780 to @0x39447b4; audit rows 55 to 58) | asm-traced |
| `carChargerLockStatus` | 1 unlocked, 2 locked (raw 2 and 4 before tagging, `ev_charge_command.dart` `setCarChargerLockStatus` @0x2cdf80c to @0x2cdf81c; audit row 60). "Bit-shifted" in the old page described the Smi tagging, not a protocol shift | asm-traced |
| `modbusTcpSwitch` | 0 off, 1 on, passed as is (`ev_charge_command.dart` `setModbusTcpSwitch` @0x3972f84; the `lsl x2,x1,#1` is Smi tagging; audit row 64) | asm-traced |
| `initSettings` | 1 (init complete); raw 2 stored with `stur w` into the map slot of `ev_charge_command.dart` `setMaximumCurrentAndCompleteInit` @0x3981730, key literal @0x398172c; the same builder also writes `maximumCurrentLimit` @0x398170c (audit row 65) | asm-traced |
| `maximumCurrentLimit` | the int argument unchanged, no divisor and no range check in the builder (`ev_charge_command.dart` `setMaximumCurrentLimit` @0x2ce0b20; audit row 62). Upstream's range is 6 A up to the rated limit (32 A) in 1 A steps (`mqttmap.py` line 5870 comment) | asm-traced for "unchanged", upstream-confirmed for the range |
| `lightBrightness` | 0 to 100 percent in 10 percent steps (upstream `CMD_EV_LIGHT_BRIGHTNESS`, `mqttcmdmap.py` line 1101 comment; audit row 63) | upstream-confirmed |
| `loadBalancingMainBreakerCurrent` | 10 to 500 A in 1 A steps (upstream `CMD_MAIN_BREAKER_LIMIT`, `mqttmap.py` line 5905 comment; audit row 67) | upstream-confirmed |
| `greenEnergyPriorityChargingMode` | 0 solar plus grid, 1 solar only (upstream `set_solar_evcharge_mode`, `mqttcmdmap.py` line 1274 comment; audit row 66) | upstream-confirmed |

### Candidate table (old page's guesses, not traced)

Tag: untagged by design (candidate mapping, not a fact). Group `0100` entries are the ones upstream lists as fields `a3` to `b7` (`mqttmap.py` lines 5855 to 5866); the others are the old page's guesses.

| APK field | candidate tag | upstream name |
|---|---|---|
| `controlType` | a2 (upstream: a4 of `0105`) | `ev_charger_mode` |
| `carChargerLockStatus` | a3 | `plug_lock_switch` |
| `plugAndChargeSwitch` | a4 | `ev_auto_start_switch` |
| `maximumCurrentLimit` | a8 | `ev_max_charge_current` |
| `lightBrightness` | aa | `light_brightness` |
| `rechargingPowerOutage` | ac | `ev_auto_charge_restart_switch` |
| `delayStartSwitch` | ad | `ev_random_delay_switch` |
| `ledSwitch`, `ledCloseStartTime`, `ledCloseEndTime` | b4, b5, b6 | `light_off_schedule` |
| `modbusTcpSwitch` | b7 | `modbus_switch` |
| `greenEnergyPriority*` | a2 to a8 (a5, a6 guessed) | `solar_evcharge_*`, `auto_phase_switch` |
| `loadBalancing*` | a2 to a6 (a3 to a5 guessed) | `load_balance_*`, `main_breaker_limit` |
| `schedChargeSwitch`, weekday and weekend hours | a2 to a6 (a3 to a6 guessed) | `ev_schedule_switch`, `ev_week_*` |

## Since/changed

| value | old page (3.18.0 reading) | 3.24.3 | audit row |
|---|---|---|---|
| `modbusTcpSwitch` | "0=off, 1=on (left-shifted by 1)" | 0 or 1 as passed; the shift is Dart tagging (`setModbusTcpSwitch` @0x3972f84 in `ev_charge_command.dart`) | 64 (WRONG) |
| `initSettings` | "2 = init complete" | 1 (raw 2 is the tagged Smi, `setMaximumCurrentAndCompleteInit` @0x3981730 in `ev_charge_command.dart`) | 65 (WRONG) |
| `action_control_charging` route | `invokeAction` | `writeProperty` (`setControlType` @0x39447d4 in `ev_charge_command.dart`) | 72 (WRONG) |
| endpoint count | 35 | 42 (sum of the nine groups) | 51 (count note; untagged by design, prose count) |

## Known firmware notes

- No firmware is recorded for any statement on this page. The 3.24.3 app is the only evidence for the field names; behavior per firmware is unknown.

## Known unknowns

Tag: untagged by design (no API fact).

- The TLV tags below are inferred by correlating the APK field names with upstream's mapping; the app's Dart code never names a tag, so no asm site can confirm them (audit row 59 UNVERIFIABLE).
- Value ranges whose value comes from the caller and was not traced: `plugAndChargeSwitch`, `rechargingPowerOutage`, `delayStartSwitch` (old page: 0 off, 1 on; audit row 61), green energy minimum current (old page 6 to 16 A, upstream says up to the rated limit), phase mode (1 one phase, 3 three phase) and the 16-byte device serial fields (audit rows 66, 67), `schedChargeSwitch` (old page "1 on, 2 off, inverted"; audit row 68), `chargerMode` ("0 default", audit row 69).
- The "encoding type 2 with a 16-byte random seed" for `action_control_charging` and `device_power_mode` (restart) is not visible in the Dart code: no `encoding_type` and no `device_power_mode` string was found; the restart in the app is `action_restart_device` (audit row 71).
- Whether `carChargerLockStatus` 1 and 2 mean unlocked and locked as the audit reads them: upstream labels `plug_lock_switch` "On (1), Off (2)" (`mqttcmdmap.py` line 1063 comment).
- Which tag carries the charge command: the old page said `a2` for `controlType`; upstream binds `ev_charger_mode_select` to field `a4` of opcode `0105` (`mqttmap.py` line 5882). Open.
- Test requests: [../docs/DEVICE_TEST_BACKLOG.md](../docs/DEVICE_TEST_BACKLOG.md).

### What's needed from device owners

Tag: untagged by design (no API fact). Per upstream issue 322:

1. System exports as owner account (shared accounts lack permissions).
2. The EV charger must be added to a system (not standalone), and vehicles configured.
3. MQTT monitoring during charging sessions.
4. The field to tag mapping above can be checked by changing one setting and watching which TLV tag changes in mqtt_monitor.

## Device-tested by

none
