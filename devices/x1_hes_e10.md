# X1 HES / E10 Home Backup — A5101, A17E1, AX170

> **Priority**: P2 (High demand)
> [anker-solix-api #274](https://github.com/thomluther/anker-solix-api/issues/274) (E10, 80+ comments) |
> [anker-solix-api #162](https://github.com/thomluther/anker-solix-api/issues/162) (X1) |
> [ha-anker-solix PR #284](https://github.com/thomluther/anker-solix-api/pull/284) (AX170 mapping by nic-southern)

## Product Info

- **A5101** — X1 Power Module P6K (US), single-phase
- **A5102** — X1 Power Module 1P H(3.68-6)K (EU/AU)
- **A5103** — X1 Power Module 3P H(5-12)K (three-phase)
- **A17E1** — E10 Whole-Home Backup Module
- **AX170** — Power Dock (connects E10 modules + generator)
- **A7320** — Smart Generator 5500 (tri-fuel, pairs with E10)
- **A5220** — X1 Battery Module (5kWh LFP)
- All require certified installer. Owned by end users.

## MQTT Field Vocabulary — A5101DataCodeType

These are the internal field names from the APK `A5101DataCodeType` enum. Use as
**candidate names** when decoding MQTT binary messages with mqtt_monitor.

> These do NOT tell you which hex byte offset maps to which field — that requires
> live device testing. They tell you what fields **exist** in the app's data model.

### Power Flow
| Hex | Field Name | Notes |
|-----|-----------|-------|
| 0x14 | `pvLoadPower` | PV → Load |
| 0x15 | `pvGridPower` | PV → Grid |
| 0x16 | `batteryLoadPower` | Battery → Load |
| 0x17 | `batteryGridPower` | Battery → Grid |
| 0x18 | `gridBatteryPower` | Grid → Battery |
| 0x19 | `gridLoadPower` | Grid → Load |
| 0x38 | `dieselLoadPower` | Generator → Load |
| 0x39 | `dieselBatterPower` | Generator → Battery |

### Battery & SOC
| Hex | Field Name | Notes |
|-----|-----------|-------|
| 0x3a | `soc` | State of charge |
| 0x21 | `batteryReserve` | Reserve SOC setting |
| 0x5e | `minSoc` | Minimum SOC |
| 0x34 | `batState` | Battery state |

### Energy Totals
| Hex | Field Name | Notes |
|-----|-----------|-------|
| 0x11 | `dailyPowerGeneration` | |
| 0x12 | `totalPowerGeneration` | |

### Operating Modes
| Hex | Field Name | Notes |
|-----|-----------|-------|
| 0x10 | `backupMode` | Backup mode config |
| 0x22 | `shiftMode` | Energy shift mode |
| 0x23 | `gridCharging` | Grid charging enable |
| 0x46 | `workMode` | Current work mode |
| 0x47 | `manualBackupPowerEnable` | Manual backup enable |
| 0x28 | `manualBackupPower` | Manual backup power level |
| 0x81 | `x1AllowCharge` | X1 charge permission |

### Peak Shaving
| Hex | Field Name | Notes |
|-----|-----------|-------|
| 0x24 | `peakShaving` | Peak shaving enable |
| 0x25 | `peakShavingValue` | Peak shaving target |
| 0x4f | `a5103PeakShavingValue` | Three-phase variant |

### Grid
| Hex | Field Name | Notes |
|-----|-----------|-------|
| 0x07 | `gridStandardCode` | Grid code |
| 0x37 | `gridState` | Grid status |
| 0x49 | `realGridState` | Real-time grid state |
| 0x7b | `gridSensitivityEnable` | Grid sensitivity on/off |
| 0x7c | `gridSensitivity` | Sensitivity level |
| 0x7d | `softwarePowerExportLimitEnable` | Export limit on/off |
| 0x7e | `softwarePowerExportLimitInput` | Export limit value |

### Generator (A7320)
| Hex | Field Name | Notes |
|-----|-----------|-------|
| 0x29 | `onOrOffSwitch` | Generator on/off |
| 0x2a | `startUpSOC` | Start threshold |
| 0x2b | `closeSOC` | Stop threshold |
| 0x2c | `startUpProtection` | Protection delay |
| 0x2d | `controlMode` | Control mode |
| 0x2f | `generatorRatedPower` | Rated power |
| 0x61 | `dieselMode` | Diesel mode |
| 0x62-63 | `dieselNormalStartSOC/StopSOC` | Normal mode thresholds |
| 0x64-6a | `dieselQuiet*` | Quiet mode (enable, SOC, hours) |
| 0x6b-71 | `dieselMaintenance*` | Maintenance schedule |

### Heat Pump
| Hex | Field Name | Notes |
|-----|-----------|-------|
| 0x57 | `heatPumpSGEnable` | SG-Ready enable |
| 0x58 | `heatPumpWork` | Heat pump working state |
| 0x59 | `heatPumpActiveRatePower` | Active rated power |
| 0x5a | `heatPumpMode` | Operating mode |
| 0x5b | `heatPumpActiveTime` | Active time |
| 0x5c | `heatPumpStartingProtectionDelay` | Start protection |

### Disaster Preparedness / Storm Guard
| Hex | Field Name | Notes |
|-----|-----------|-------|
| 0x42 | `outageFrequency` | Outage frequency |
| 0x43 | `blackoutDuration` | Blackout duration |
| 0x44 | `autoDisaster` | Auto disaster enable |
| 0x45 | `autoDisasterData` | Auto disaster data |

### System / Device Management
| Hex | Field Name | Notes |
|-----|-----------|-------|
| 0x20 | `systemId` | System identifier |
| 0x33 | `systemPackNumber` | Number of battery packs |
| 0x3b | `getDeviceList` | Device list query |
| 0x55 | `supportFunction` | Capability flags |
| 0x56 | `supportFunction2` | Extended capabilities |
| 0x0d | `startScanDevice` | BLE device scan |

### Self-Check (Italy compliance)
| Hex | Field Name | Notes |
|-----|-----------|-------|
| 0x1a | `selfCheckResult` | Result |
| 0x1b | `selfCheckError` | Error code |
| 0x4a | `selfCheckEnable` | Enable |
| 0x4b | `selfCheckItemSelect` | Item selection |
| 0x4c | `selfCheckFaultClean` | Fault clear |
| 0x4d | `selfCheckStatus` | Current status |

## Related Files in This Repo

- [PARAM_DATA_STRUCTURES.md](../PARAM_DATA_STRUCTURES.md#disaster-preparedness) — Disaster mode payloads
- [PARAM_DATA_STRUCTURES.md](../PARAM_DATA_STRUCTURES.md#ax170-iot-action-payloads) — AX170 IoT actions
- [VALIDATION_MODEL.md](../VALIDATION_MODEL.md) — GET→SET flows for power limit, SOC, grid export
- [ENUMS.md](../ENUMS.md) — Product codes (A5101-A5103, A5220, A5341, A5450)
- [FIELD_TYPES.md](../FIELD_TYPES.md#feature-flags-sceneinfofeatureswitch) — Feature flags (enable_aiems_v2, grid_to_ev)
- [models/hes.md](../models/hes.md) — 14 HES response models
- [ENDPOINT_FIELDS.md](../ENDPOINT_FIELDS.md) — sendDeviceCommand, changePriceUnit, updateWiFiConfig
- [REQUIRED_FIELDS.md](../REQUIRED_FIELDS.md#charging_hes_svcdevice_command) — sendDeviceCommand required/optional

## API Endpoints

### HES Service (28 endpoints)
See [endpoints/charging_hes_svc.md](../endpoints/charging_hes_svc.md)

### Disaster Preparedness (5 endpoints)
See [endpoints/device_specific.md](../endpoints/device_specific.md#disaster-preparedness--storm-guard-endpoints-cross-device--p2)

### Device-Specific HES (25+ endpoints)
See [endpoints/device_specific.md](../endpoints/device_specific.md#hes--x1-endpoints-a5101--p2)

## Disaster Payload Structures (structurally inferred)

```json
// Manual disaster mode
{"type": 2, "identifier_id": "<siteid>", "manual_disaster_switch": 1,
 "start_time": "...", "end_time": "..."}

// Auto disaster mode
{"type": 2, "identifier_id": "<siteid>", "auto_disaster_switch": 1}

// Quit disaster mode
{"type": 2, "identifier_id": "<siteid>"}
```

## Response Models

See [models/hes.md](../models/hes.md) — 14 models including:
- `A5101DeviceCommandModel` (17 top-level fields, 4 levels deep nesting)
- `AutoDisasterPrepareStatusModel`
- `CheckFunctionModel` (capability flags)

## What's needed from device owners

Per thomluther:
1. **Owner account** system exports (shared accounts lack permissions)
2. MQTT monitoring with mqtt_monitor to validate field-to-hex mapping
3. Compare abbreviated MQTT field values with App display values
4. X1 uses JSON "trans" payloads with abbreviations — easier to decode than binary
