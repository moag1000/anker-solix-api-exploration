> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Page type: device · Owner page: this page

# X1 HES / E10 Home Backup — A5101, A17E1, AX170

## Contents

1. [PN, marketing name, generation/family](#pn-marketing-name-generationfamily)
2. [Features matrix](#features-matrix)
3. [A5101DataCodeType vocabulary](#a5101datacodetype-vocabulary)
4. [API endpoints](#api-endpoints)
5. [Disaster payloads](#disaster-payloads)
6. [Response models](#response-models)
7. [Since/changed](#sincechanged)
8. [Known firmware notes](#known-firmware-notes)
9. [Known unknowns](#known-unknowns)
10. [Device-tested by](#device-tested-by)

Row numbers ("audit row N") count the table rows of [../docs/audit/devices.md](../docs/audit/devices.md) from the top; this page consumes rows 123 to 193. Method, tags and the Smi rule: [../METHODOLOGY.md](../METHODOLOGY.md). Payloads, command fields and wire codes live on the owner pages linked below.

## PN, marketing name, generation/family

| PN | marketing name | note |
|---|---|---|
| `A5101` | X1 Power Module P6K (US) | single-phase; untagged by design (product name) |
| `A5102` | X1 Power Module 1P H(3.68-6)K (EU/AU) | untagged by design (product name) |
| `A5103` | X1 Power Module 3P H(5-12)K | three-phase; untagged by design (product name) |
| `A17E1` | E10 Whole-Home Backup Module | untagged by design (product name) |
| `AX170` | Power Dock | connects E10 modules and a generator; untagged by design (product name) |
| `A7320` | Smart Generator 5500 | tri-fuel, pairs with E10; untagged by design (product name) |
| `A5220` | X1 Battery Module (5 kWh LFP) | untagged by design (product name) |

Names, ratings and the priority label come from the old page and upstream issues [anker-solix-api #274](https://github.com/thomluther/anker-solix-api/issues/274) (E10, more than 80 comments), [#162](https://github.com/thomluther/anker-solix-api/issues/162) (X1) and [PR #284](https://github.com/thomluther/anker-solix-api/pull/284) (AX170 mapping); they are product facts, not asm facts (audit row 193 NOT-FROM-ASM). All products require a certified installer and are owned by end users. Product codes: [../reference/enums.md](../reference/enums.md).

## Features matrix

| feature | API (link) | MQTT (link) | BLE (link) | device-tested? |
|---|---|---|---|---|
| status (JSON "trans" payload with abbreviated keys) | [get_hes_dev_info](../api/charging_hes_svc/get_hes_dev_info.md) and the energy endpoints | [JSON status](../mqtt/a5101.md#json-status-trans-payload) | none | no |
| work mode, battery reserve, storm guard | [device_command](../api/charging_hes_svc/device_command.md); flows [a5101_work_mode_change](../flows/a5101_work_mode_change.md), [a5101_battery_reserve](../flows/a5101_battery_reserve.md), [a5101_storm_guard](../flows/a5101_storm_guard.md) | [data code maps](../mqtt/a5101.md#data-code-maps-setdatacodemap-and-getdatacodemap) | [ble/a5101.md](../ble/a5101.md) | no |
| disaster preparedness | [charging_disaster_prepared](../api/charging_disaster_prepared/README.md) | [0115 sendAutoDisasterDataCmd](../mqtt/a5101.md) (upstream-confirmed owner page) | [ble/a5101.md](../ble/a5101.md) | no |
| generator, heat pump, peak shaving, self-check | [device_command](../api/charging_hes_svc/device_command.md) | data codes below | [ble/a5101.md](../ble/a5101.md) | no |

## A5101DataCodeType vocabulary

Tag: asm-traced. The enum `A5101DataCodeType` has 133 members ([../mqtt/a5101.md](../mqtt/a5101.md#data-code-maps-setdatacodemap-and-getdatacodemap)). The names are the app's internal field names; use them as candidate names when decoding. The old tables headed their number column "Hex" and read like codes: those numbers are the enum index (`off_8` of the pool object), not the code sent or received. The wire code is a different 2-byte key in `setDataCodeMap` and `getDataCodeMap` of `charging/ble/device/A5101/a5101_commands.dart` (audit row 123, WRONG framing; the per-row values are audit rows 124 to 186, OK as enum indices). The 25 members whose codes are already in the owner page are not repeated: `pvLoadPower`, `batteryLoadPower`, `gridBatteryPower`, `gridLoadPower`, `dieselLoadPower`, `dieselBatterPower`, `soc`, `batteryReserve`, `minSoc`, `backupMode`, `workMode`, `manualBackupPower`, `x1AllowCharge`, `peakShaving`, `gridStandardCode`, `gridSensitivityEnable`, `gridSensitivity`, `softwarePowerExportLimitEnable`, `softwarePowerExportLimitInput`, `heatPumpSGEnable`, `outageFrequency`, `blackoutDuration`, `autoDisaster`, `supportFunction` and `selfCheckError`. The `diesel*` family (17 codes) is owned by the same page; the old page listed `dieselMode` at index 0x61 with normal, quiet and maintenance sub-ranges (0x62 to 0x71).

### Power flow

| enum index | field | wire code | map | site in `a5101_commands.dart` |
|---|---|---|---|---|
| 0x15 | `pvGridPower` | `0x0038` | get and set | @0x3b8912c, @0x3b8afe0 |
| 0x17 | `batteryGridPower` | `0x003e` | get and set | @0x3b891b4, @0x3b8b068 |

### Battery and SOC

| enum index | field | wire code | map | site in `a5101_commands.dart` |
|---|---|---|---|---|
| 0x34 | `batState` | `0x0002` | get and set | @0x3b89a4c, @0x3b8b76c |

### Energy totals

| enum index | field | wire code | map | site in `a5101_commands.dart` |
|---|---|---|---|---|
| 0x11 | `dailyPowerGeneration` | `0x0064` | get and set | @0x3b89060, @0x3b8aed0 |
| 0x12 | `totalPowerGeneration` | `0x0086` | get and set | @0x3b890a4, @0x3b8af14 |

### Operating modes

| enum index | field | wire code | map | site in `a5101_commands.dart` |
|---|---|---|---|---|
| 0x22 | `shiftMode` | `0x0000` | set | @0x3b89464 |
| 0x23 | `gridCharging` | `0x0003` | set | @0x3b894b8 |
| 0x47 | `manualBackupPowerEnable` | `0x0005` | set | @0x3b89cec |

### Peak shaving

| enum index | field | wire code | map | site in `a5101_commands.dart` |
|---|---|---|---|---|
| 0x25 | `peakShavingValue` | `0x0007` | get and set | @0x3b89560, @0x3b8b328 |
| 0x4f | `a5103PeakShavingValue` | `0x0028` | set | @0x3b89e90 |

### Grid

| enum index | field | wire code | map | site in `a5101_commands.dart` |
|---|---|---|---|---|
| 0x37 | `gridState` | `0x0003` | get | @0x3b8b910 |
| 0x49 | `realGridState` | `0x0010` | get | @0x3b8bda8 |

### Generator (A7320)

| enum index | field | wire code | map | site in `a5101_commands.dart` |
|---|---|---|---|---|
| 0x29 | `onOrOffSwitch` | `0x000c` | get and set | @0x3b896b0, @0x3b8b478 |
| 0x2a | `startUpSOC` | `0x000d` | set | @0x3b89704 |
| 0x2b | `closeSOC` | `0x000e` | get and set | @0x3b89758, @0x3b8b4cc |
| 0x2c | `startUpProtection` | `0x0010` | get and set | @0x3b897ac, @0x3b8b520 |
| 0x2d | `controlMode` | `0x0011` | get and set | @0x3b89800, @0x3b8b574 |
| 0x2f | `generatorRatedPower` | `0x0013` | get and set | @0x3b898a8, @0x3b8b61c |

### Heat pump

| enum index | field | wire code | map | site in `a5101_commands.dart` |
|---|---|---|---|---|
| 0x58 | `heatPumpWork` | `0x003a` | set | @0x3b89f38 |
| 0x59 | `heatPumpActiveRatePower` | `0x003b` | set | @0x3b89f8c |
| 0x5a | `heatPumpMode` | `0x003c` | set | @0x3b89fe0 |
| 0x5b | `heatPumpActiveTime` | `0x003e` | set | @0x3b8a034 |
| 0x5c | `heatPumpStartingProtectionDelay` | `0x003f` | set | @0x3b8a088 |

### Disaster preparedness / storm guard

| enum index | field | wire code | map | site in `a5101_commands.dart` |
|---|---|---|---|---|
| 0x45 | `autoDisasterData` | `0xf012` | get and set | @0x3b89c98, @0x3b8bd00 |

### System / device management

| enum index | field | wire code | map | site in `a5101_commands.dart` |
|---|---|---|---|---|
| 0x20 | `systemId` | `0xf00b` | get and set | @0x3b893d4, @0x3b8b288 |
| 0x33 | `systemPackNumber` | `0xe000` | get and set | @0x3b899f8, @0x3b8b718 |
| 0x3b | `getDeviceList` | `0xf002` | get and set | @0x3b89bf0, @0x3b8ba0c |
| 0x56 | `supportFunction2` | `0x0158` | get | @0x3b8c198 |
| 0x0d | `startScanDevice` | `0xf002` | get and set | @0x3b88f50, @0x3b8adc0 |

### Self-check (Italy compliance)

| enum index | field | wire code | map | site in `a5101_commands.dart` |
|---|---|---|---|---|
| 0x1a | `selfCheckResult` | `0x0136` | get and set | @0x3b89280, @0x3b8b134 |
| 0x4a | `selfCheckEnable` | `0x0261` | get and set | @0x3b89d40, @0x3b8be50 |
| 0x4b | `selfCheckItemSelect` | `0x0262` | get and set | @0x3b89d94, @0x3b8bea4 |
| 0x4c | `selfCheckFaultClean` | `0x0263` | get and set | @0x3b89de8, @0x3b8bef8 |
| 0x4d | `selfCheckStatus` | `0x014f` | get | @0x3b8bf4c |

## API endpoints

The old counts ("HES Service 28", "Disaster Preparedness 5", "Device-Specific HES 25+") were prose counts and are removed (audit row 187); the old endpoint files list 50 path headings for `charging_hes_svc`, 31 endpoint lines in the HES / X1 section of `device_specific.md` and 6 in the disaster section. Current pages: [api/charging_hes_svc](../api/charging_hes_svc/README.md), [api/charging_disaster_prepared](../api/charging_disaster_prepared/README.md), and the owner pages above replace the deleted lists `endpoints/charging_hes_svc.md` and `endpoints/device_specific.md`.

## Disaster payloads

The three request shapes of the old page (manual, auto, quit) are not repeated; the 3.24.3 values of the manual request are owned by the section "Manual request values (3.24.3)" of [home_power_panel.md](home_power_panel.md#manual-request-values-3243) and the endpoint pages above. What changed for the X1 page:

- `manual_disaster_switch` is the JSON boolean `true` in the manual request, not the integer 1 (`manual_power_backup_logic.dart` @0x25ecd50; audit row 189, WRONG).
- `type` is 1 or 2 (`manual_power_backup_logic.dart` @0x25ecd1c to @0x25ecd28); the old example's 2 is one of the two possible values (the `"type": 2` row of the X1 section of the audit, OK).
- `auto_disaster_switch` in a request: no request map with this key exists in 3.24.3, only read sites (audit row 190, UNVERIFIABLE).

## Response models

[../models/hes.md](../models/hes.md) holds 14 HES models, every class of which exists in the 3.24.3 asm (audit row 192, prose count confirmed by the heading count). `A5101DeviceCommandModel` (class size 0x54) has 19 field slots and its `toJson` writes 19 keys (`a5101_device_command_model.dart` `toJson` @0x277d908; audit row 191); the old "17 top-level fields" is corrected. Other models: `AutoDisasterPrepareStatusModel`, `CheckFunctionModel` (capability flags).

## Since/changed

| item | old page (3.18.0 reading) | 3.24.3 |
|---|---|---|
| numbers in the vocabulary tables | "Hex" codes | enum indices; wire codes in the tables above and in the owner page |
| `manual_disaster_switch` in the manual request | `1` | `true` (bool), `manual_power_backup_logic.dart` @0x25ecd50 |
| `A5101DeviceCommandModel` top-level fields | 17 | 19 (`toJson` @0x277d908 in `a5101_device_command_model.dart`); untagged by design (product name) |
| endpoint counts | 28, 5, 25+ | 50 path headings, 6 disaster lines, 31 HES / X1 lines in the old endpoint files (prose counts; untagged by design) |

## Known firmware notes

- No firmware is recorded for any statement on this page.

`auto_disaster_switch` in requests (checked 2026-10-20): the key string occurs at only two places in the whole dump, both in `DisasterSetting.fromJson` (`base_service/ak_iot_kit/business/basic/model/device_disaster_model.dart @0x2a2bd84` and `charging/ui/page/station/mixin/auto_disaster.dart @0x46c4a30`), so the app reads it from answers and never builds a request body with it in 3.24.3 (audit row 190).

## Known unknowns

Tag: untagged by design (no API fact).

- Which wire code maps to which field is asm-traced (tables above), but what each field means on the device needs a live capture; the vocabulary tells what fields exist, not their units or scales.
- Wire codes of the `diesel*` family and the A5103 variants: the 17 `diesel*` codes (`0x02be` to `0x02cd` and `0x02d1`) are in [../mqtt/a5101.md](../mqtt/a5101.md#data-code-maps-setdatacodemap-and-getdatacodemap); the A5103 variants are not separated there.
- Needed from device owners (per upstream): system exports as owner account (shared accounts lack permissions); MQTT monitoring with mqtt_monitor to validate the field to code mapping; comparing abbreviated MQTT values with the app display. X1 uses JSON "trans" payloads with abbreviations, which are easier to decode than binary. Open requests: [../docs/DEVICE_TEST_BACKLOG.md](../docs/DEVICE_TEST_BACKLOG.md).

## Device-tested by

none
