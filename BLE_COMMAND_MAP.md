# BLE/MQTT Command Map — Static Cross-Reference

> **New methodology (2026-03-28)**: This mapping was produced by cross-referencing
> decompiled APK command builder functions (field order + Dart Smi constants) with
> thomluther's device-tested TLV tag assignments in `mqttcmdmap.py`.
>
> **Validation**: 5/5 exact matches on device-confirmed commands (A17X8 007a/007c/007e,
> A17C1 005e/0080). Field type correlation confirmed: `intToList()`→ui, `intToList3()`→var(3),
> `intToList4()`→var(4). Dart Smi encoding: assembly constant >> 1 = hex tag value.
>
> **Confidence levels**:
> - **CONFIRMED** — matches upstream mqttcmdmap.py (community-tested)
> - **NEW** — found in APK but not in upstream (needs device verification)
> - **?** — tag assignment inferred from field order (needs verification)

---

## A17C1 / A17C2 / A17C3 / A17C5 — Solarbank 2/3

> A17C5 (Solarbank 3) reuses `A17C1DeviceController` — confirmed in device_factory_impl.dart

| Opcode | APK Function | Tags → Fields | Status |
|--------|-------------|---------------|--------|
| **0050** | `setTempUnit` | a2: temp_unit (0=C, 1=F) | CONFIRMED |
| **005e** | `setBackPower` | a2: usage_mode, a3: flag?, a4: charge_switch, a6: start_ts(u32), a7: end_ts(u32), fd: timestamp | CONFIRMED |
| **005e** | `setTacticsTime` | a2-bb: 30 schedule slot tags, fd: timestamp | CONFIRMED (full schedule) |
| **005e** | `setPeakValley` | a2: mode, a3: flag, fd: timestamp | CONFIRMED |
| **005a** | `setMaxLoad` | a2: max_load(u16), a3: max_load_type | CONFIRMED |
| **0067** | `setSoc` | a2: output_cutoff, a3: lowpower_input, a4: input_cutoff | CONFIRMED |
| **0068** | `setDeviceLightMode` | a2: light_mode, a3: light_off_switch | CONFIRMED |
| **0073** | `setOffGridSwitch` | a2: ac_socket_switch (0=off, 1=on) | CONFIRMED (A17C5) |
| **0080** | `setDevicePowerLimit` | a2-a8: grid export + power limit fields (u16) | CONFIRMED |
| **009a** | `setSleepingTime` | a2: timeout_min (divider 30) | CONFIRMED (A17C5) |
| **0057** | `remoteConfigWifi` | a2: trigger, a3: ?(u32) | CONFIRMED |
| **0040** | (status request) | (no payload) | CONFIRMED |
| **0071** | `setElectricityPrice` | a2: price(u32), a3: ?(var) | **NEW** |
| **0069** | `hourPerMinute` | (params unclear) | **NEW** |
| **005f** | `setDeviceSelfTest` | a2: enable, a3: ? | **NEW** |
| **0081** | `setDeviceMicroPowerLimit` | a2: limit(u16) | **NEW** |
| **0082** | (init command) | (inline) | **NEW** |
| **006a** | (peak/valley day data) | (GET request) | **NEW** |

---

## A17X8 — Smart Plug

| Opcode | APK Function | Tags → Fields | Status |
|--------|-------------|---------------|--------|
| **007a** | `setRelaySwitchCmd` | a2: switch (0=off, 1=on) | CONFIRMED |
| **007c** | `setTimingCmd` | a2: action(0=del/1=create/2=mod), a3: slot, a4: enabled, a5: time(min:hour), a6: switch, a7: weekdays(var len, 1=Mon..7=Sun) | CONFIRMED |
| **007e** | `setCountdownCmd` | a2: toggle_switch(0=cancel/1=start/2=pause/3=resume), a3: delay(3 bytes LE), a4: back_switch, a5: back_delay(3 bytes) | CONFIRMED |
| **007f** | (timer request) | (no payload) | CONFIRMED |
| **0079** | `setMomenryPortSwitch` | a2: switch? | **NEW** — momentary/memory mode |
| **007b** | `setCountdownCmd` (alt) | (shares tags with 007e) | **NEW** — countdown variant |
| **007d** | (request) | (no payload) | **NEW** — unknown query |

---

## A17C0 — Solarbank Gen 1

| Opcode | APK Function | Tags → Fields | Status |
|--------|-------------|---------------|--------|
| **0050** | `setTempUnit` | a2: temp_unit | CONFIRMED |
| **005e** | `setDischargeTime` | a2: mode, a3: schedule_data | CONFIRMED |
| **0067** | `setSoc` | a2: output_cutoff, a3: lowpower_input, a4: input_cutoff | CONFIRMED |
| **0068** | `setMicroInversionModel` | a2-a9: brand, model, min/max load | CONFIRMED |
| **0071** | `setElectricityPrice` | a2: price(u32), a3: ?(var) | **NEW** |

---

## A172X / A176X / A178X — Portable Power Stations (PPS)

| Opcode | APK Function | Tags → Fields | Status |
|--------|-------------|---------------|--------|
| **004a** | `setAcSwitch` | a2: switch (0=off, 1=on) | CONFIRMED |
| **004b** | `setCarSwitch` | a2: switch | CONFIRMED |
| **004c** | `setLcdLight` | a2: brightness (0=off,1=low,2=med,3=high) | CONFIRMED |
| **004d** | `setAcFrequency` | a2: freq | CONFIRMED |
| **004e** | `setEnergyMode` | a2: mode | CONFIRMED |
| **004f** | `setAmbientLight` | a2: mode (0=off,1-4) | CONFIRMED |
| **0050** | `setTempUnit` | a2: unit | CONFIRMED |
| **0052** | `setScreenSwitch` | a2: switch | CONFIRMED |
| **0043** | `setCarCountDownTime` | a2: seconds(u32) | CONFIRMED |
| **0044** | `setAcChargePower` | a2: watts(u16) | CONFIRMED |
| **0045** | `setDeviceWaitTime` | a2: minutes(u16) | CONFIRMED |
| **0046** | `setDeviceScreenTime` | a2: seconds(u16) | CONFIRMED |
| **0076** | `setCarPortSavingMode` | a2: mode (0=smart, 1=normal) | CONFIRMED |
| **0077** | `setAcOutputSmartMode` | a2: mode (0=smart, 1=normal) | CONFIRMED |
| **0079** | `setMomenryPortSwitch` | a2: switch | **NEW** for PPS |
| **0075** | `setPullLightWaitTime` | a2: time(u16) | **NEW** |
| **0091** | `setLocale` | (inline) | **NEW** (A1790 only) |

---

## A1790 — F3800 (with expansion batteries + generator)

Inherits all PPS commands above, plus:

| Opcode | APK Function | Tags → Fields | Status |
|--------|-------------|---------------|--------|
| **0078** | `setThirdATSData` | a2-a5: generator params(u16), fe: timestamp(u24) | **NEW** |
| **005f** | `setBMSSubBatteryPowerSwitch` | a2: battery_id, a3: switch, a4: ? | **NEW** |
| **0060** | `setBMSSubBatteryLightSwitch` | a2: battery_id, a3: switch, a4: ? | **NEW** |

---

## A5190 / A5191 — EV Charger V1

See [devices/ev_charger.md](devices/ev_charger.md#mqttble-command--tlv-tag--apk-field-name-mapping) for full mapping.

Uses IoT SDK `prop_write_*` / `invokeAction` abstraction — TLV tags assigned by framework.
Only `action_control_charging` (start/stop/boost) uses encoding_type=2.

---

## A5101 — X1 HES (Home Energy System)

> **Different protocol**: Uses attribute-ID (att_id) system via `BleWritePayloadHelper`,
> NOT TLV command opcodes. Data serialized as JSON strings, not binary TLV.

| Function | Protocol | Notes |
|----------|----------|-------|
| `sendPeakAndValleyCmd` | att_id + JSON | Peak/valley schedule |
| `sendHeatPumpTimePlanCmd` | att_id + JSON | **NEW** — heat pump schedule |
| `sendAutoDisasterData` | opcode **002d** | Auto disaster/backup |
| `getAtsAndMiFault` | att_id | ATS + micro-inverter fault query |
| `getBackupHistoryListReq` | att_id | Backup history |
| `getOtaSocData` | att_id | OTA SOC data |
| `getDeviceVersion` | opcode **0030** | Version query |

The **entire** A5101 BLE command set is unmapped in upstream.

---

## A17A0 / A17A3-A5 — EverFrost Cooler (entirely unmapped)

| Opcode | APK Function | Tags | Notes |
|--------|-------------|------|-------|
| — | `setBox0Switch` | a2 | Compartment 0 on/off |
| — | `setBox0Temp` | a3 | Compartment 0 temperature |
| — | `setBox1Switch` | a4 | Compartment 1 on/off |
| — | `setBox1Temp` | a5 | Compartment 1 temperature |
| — | `setTemperatureUnit` | e1 | Celsius/Fahrenheit |
| — | `setVoltageProtection` | cd | Low voltage protection |
| **004c** | `setLcdBrightness` | cf | LCD brightness |
| **0081** | `setBox0Mode` | (inline) | Compartment mode |
| **0082** | `setScreenAlwaysOn` | (inline) | Screen always-on |
| — | `setSingleBoxTemp` | d3 | Single-zone temp |
| — | `setDoubleBoxRTemp` | d7 | Right zone temp |
| — | `setDoubleBoxLTemp` | dd | Left zone temp |

P4 priority — minimal community demand.

---

## A2345 / A91B2 — Prime Charger / Charging Station (partially mapped)

| Opcode | APK Function | Tags | Status |
|--------|-------------|------|--------|
| — | `setChargingMode` | a2, a3?, a4? | **NEW** |
| — | `setDCPortCountdownTask` | a2, a3(u32) | **NEW** |
| — | `setDCRelaySwitch` | a2, a3 | **NEW** |
| — | `setACPortCountdownTask` (A91B2) | a2, a3(u32) | **NEW** |
| — | `setACRelaySwitch` (A91B2) | a2, a3 | **NEW** |
| — | `setUFCSSwitch` | a2 | **NEW** — USB Fast Charge |
| — | `setButtonRotateDirection` | a2 | **NEW** |
| — | `setScreenSaverSwitchAndTheme` | a2-a7? | **NEW** |
| — | `setClockFormat` (A91B2) | a2 | **NEW** |

P3 priority — niche but requested.

---

# STATUS Message Fields (Receive Direction)

> Devices periodically send status messages (0405 type). These are the fields
> the app reads from those messages. Extracted from `parseDeviceAllInfo` and
> MQTT model `fromJson` methods in the decompiled code.

---

## A17B1 — Solarbank 2 System JSON Keys (MQTT status)

The A17B1 uses **JSON** (not binary TLV) for MQTT status messages.
These abbreviated keys are what mqtt_monitor shows — now with full names.

### Core Power Fields
| Key | Full Name | Type | Default |
|-----|-----------|------|---------|
| `soc` | State of Charge | int | — |
| `pp` | PV (Solar) Power | int | 0 |
| `bp` | Battery Power | int | 0 |
| `gp` | Grid Power | int | 0 |
| `lp` | Load Power | int | 0 |
| `op` | Output Power | int? | null |
| `ep` | Export Power | int | 0 |
| `ppu` | PV Power Unit | str | — |
| `bpu` | Battery Power Unit | str | — |
| `gpu` | Grid Power Unit | str | — |
| `lpu` | Load Power Unit | str | — |
| `opu` | Output Power Unit | str | — |

### State Fields
| Key | Full Name | Type | Default |
|-----|-----------|------|---------|
| `ws` | WiFi Signal | int | 0 |
| `bs` | Battery State | int | — |
| `gs` | Grid Status | int | 0 |
| `ps` | PV Status | int | 0 |
| `m` | Mode | int | 2 |
| `os` | Online State | bool | false |
| `ts` | Timer/Schedule State | bool | false |

### Energy Flow (nested in `dataFlow` object)
| Key | Full Name |
|-----|-----------|
| `p2bp` | PV → Battery Power |
| `p2lp` | PV → Load Power |
| `p2gp` | PV → Grid Power |
| `b2lp` | Battery → Load Power |
| `b2gp` | Battery → Grid Power |
| `g2bp` | Grid → Battery Power |
| `g2lp` | Grid → Load Power |
| `mpp` | Micro-Inverter PV Power |

### Settings & Totals
| Key | Full Name | Type | Default |
|-----|-----------|------|---------|
| `cp` | Charge Percentage Target | int | 40 |
| `pu` | Power Usage Mode | int | 0 |
| `tu` | Time Update / Timestamp | int | 0 |
| `b1t` | Battery 1 Temperature | int | 0 |
| `mps` | Micro Power Setting | int | 0 |
| `tpp` | Total PV Production | int | 0 |
| `tgp` | Total Grid Power | int | 0 |
| `tlp` | Total Load Power | int | 0 |
| `tsp` | Total Solar Production | int | 0 |
| `dps` | Discharge Power Setting | int | 0 |
| `dpct` | Discharge Percent | int | 0 |
| `inmt` | Inverter Max Throughput | int? | null |
| `gmp` | Grid Max Power | int? | null |
| `scfg` | System Configuration | int? | null |

### Version & System
| Key | Full Name | Type |
|-----|-----------|------|
| `mv` | Main Firmware Version | str |
| `mdv` | Module Detail Version | str |
| `tv` | Total Version | str |
| `acc` | Account/Access Code | str? |
| `rp` | Rate Plan (schedule array) | list |
| `dpp` | Discharge Power Plan | list |

### Battery Array (in `bds` list)
| Key | Full Name |
|-----|-----------|
| `sn` | Battery Serial Number |
| `name` | Battery Name |
| `soc` | Battery SOC |
| `power` | Battery Power |
| `error` | Error Code |
| `related` | Related Device |

### Diesel/Generator Extension
| Key | Full Name |
|-----|-----------|
| `hasDiesel` | Has Diesel Generator |
| `dieselState` | Diesel Generator State |
| `o2lp` / `o2lpu` | Output2 Load Power / Unit |
| `o2pp` / `o2ppu` | Output2 PV Power / Unit |

---

## A5101 — X1 HES MQTT Status Fields

The X1 system uses **JSON "trans" payloads** (not binary TLV).

### Core Power Fields
| Key | Full Name | Unit Key |
|-----|-----------|----------|
| `pvPower` | PV Power | `pvEnergyUnit` |
| `batPower` | Battery Power | `batEnergyUnit` |
| `gridPower` | Grid Power | `gridEnergyUnit` |
| `loadPower` | Load Power | `loadEnergyUnit` |
| `dieselPower` | Diesel/Generator Power | `dieselPowerUnit` |
| `evChargerAllPower` | EV Charger Total Power | — |
| `ppsTotalPower` | PPS Total Power | — |

### State Fields
| Key | Full Name |
|-----|-----------|
| `gridState` | Grid Connection State |
| `pvState` | PV Connection State |
| `batState` | Battery State |
| `batElectricQuantity` | Battery Charge Level (SOC) |
| `emsStatus` | EMS Status |
| `emsMode` | EMS Mode |
| `mainSnDisconnected` | Main SN Disconnected |

### System Topology
| Key | Full Name |
|-----|-----------|
| `batTotalCount` | Total Battery Pack Count |
| `numberOfParallelDevice` | Number of Parallel Devices |
| `pcsOnlineNum` | PCS Online Count |
| `pcsTotal` | PCS Total Count |
| `evChargerOnlineNums` | EV Charger Online Count |
| `ppsTotalCount` | PPS Total Count |
| `ppsTotalElectricQuantity` | PPS Total Charge |

### Energy Flow (nested in `dataFlow`)
| Key | Full Name |
|-----|-----------|
| `pvToLoadPower` | PV → Load |
| `pvToGridPower` | PV → Grid |
| `batToLoadPower` | Battery → Load |
| `batToGridPower` | Battery → Grid |
| `gridToBatPower` | Grid → Battery |
| `gridToLoadPower` | Grid → Load |
| `dieselToLoadPower` | Diesel → Load |
| `dieselToBatPower` | Diesel → Battery |
| `pvToEvChargerPower` | PV → EV Charger |
| `gridToEvChargerPower` | Grid → EV Charger |
| `batToEvChargerPower` | Battery → EV Charger |

---

## A17X8 — Smart Plug 0405 Status Tags

Extracted from `parseDeviceAllInfo` (a17x8_device_commands.dart). 9 upstream-confirmed, 3 new.

| Tag | Field | Conversion | Upstream Name | Status |
|-----|-------|-----------|---------------|--------|
| fe | timestamp | int | `msg_timestamp` | CONFIRMED |
| a2 | device_sn | Utf8 string | `device_sn` | CONFIRMED |
| a3 | field_187 | bool (==1) | — | **NEW** — inferred: `schedule_active` |
| a4 | field_47b+4bb | bool (==1), dual | `ac_output_power_switch` | CONFIRMED |
| a5 | field_47b+4bb | bool, conditional | — | **NEW** — `ac_switch_confirmation` (only if field_49f set) |
| a6 | field_7b | getMainVersionWithHex | `sw_version` | CONFIRMED |
| a7 | field_2d7 | int | `sw_controller` | CONFIRMED |
| a8 | field_483 | int × 0.1 | `voltage` | CONFIRMED (float) |
| a9 | field_47f | int × 0.01 | `current` | CONFIRMED (float) |
| aa | field_487 | int × 0.1 | `power` | CONFIRMED (float) |
| ab | field_48b | int | `output_energy` (upstream ×0.001) | CONFIRMED |
| ad | → parseCountDownInfo() | sub-parser | `timer_status` | CONFIRMED |
| ae | field_49b | bool (==1) | — | **NEW** — inferred: `countdown_active` |

---

## A17C1 — Solarbank 2 Pro 0405 Status Tags

Extracted from `parseDeviceAllInfo` (a17c1_device_commands.dart, 8804 bytes).
20 upstream-confirmed, 11 new. Divisors extracted from assembly (sdiv instructions).

### Core Identity & Version
| Tag | Field | Conversion | Divisor | Upstream Name | Status |
|-----|-------|-----------|---------|---------------|--------|
| fe | field_6f | int | — | `msg_timestamp` | CONFIRMED |
| a2 | field_6b | Utf8 string | — | `device_sn` | CONFIRMED |
| a6 | field_7b | getMainVersionWithHex | — | `sw_version` | CONFIRMED (debug: "17c1 total package version") |
| a7 | field_2d7 | int | — | `sw_controller` | CONFIRMED |
| a8 | field_2eb | int | — | `sw_expansion` | CONFIRMED |

### Battery & SOC
| Tag | Field | Conversion | Divisor | Upstream Name | Status |
|-----|-------|-----------|---------|---------------|--------|
| a3 | field_317 + field_3d3 | int | — | `main_battery_soc` | CONFIRMED (stored to 2 offsets) |
| ad | field_3d7 | int | — | `battery_soc` | CONFIRMED (avg incl. expansions) |
| b0 | field_243 | int | ÷100 | `bat_charge_power` | CONFIRMED |
| b7 | field_247 | int | ÷100 | `bat_discharge_power` | CONFIRMED |
| e8 | field_2bf | bitlist | bits | `battery_heating` | CONFIRMED (bit[0]==2→heating) |

### Power & Energy
| Tag | Field | Conversion | Divisor | Upstream Name | Status |
|-----|-------|-----------|---------|---------------|--------|
| ab | field_20b | int | ÷10 | `photovoltaic_power` | CONFIRMED |
| ac | field_237 | int | ÷10 | `ac_output_power` | CONFIRMED |
| c8 | field_1db | int | ÷10 | `ac_socket_power` | CONFIRMED |
| d3 | field_23f | int | ÷10 | `output_power` | CONFIRMED |
| b1 | field_24b | int | — | `pv_yield` (upstream ×0.0001) | CONFIRMED |
| b2 | field_24f | int | — | `charged_energy` (upstream ×0.00001) | CONFIRMED |
| b3 | field_253 | int | — | `output_energy` (upstream ×0.0001) | CONFIRMED |
| c9 | field_257 | int | — | `consumed_energy` (upstream ×0.0001) | CONFIRMED |

### Settings & State
| Tag | Field | Conversion | Divisor | Upstream Name | Status |
|-----|-------|-----------|---------|---------------|--------|
| a5 | field_3db | int | — | `error_code` | CONFIRMED |
| a9 | field_3b7 | int | — | `temp_unit_fahrenheit` | CONFIRMED |
| aa | field_307 | int | SIGNED (≥0x80→−) | `temperature` | CONFIRMED (signed byte) |
| b4 | field_25b | int | — | `output_cutoff_data` | CONFIRMED |
| c2 | field_417 | int | — | `max_load` | CONFIRMED |
| c6 | field_473 | int | — | `usage_mode` | CONFIRMED |
| d2 | field_23b | int | — | `light_mode` | CONFIRMED |
| e0 | field_42f | bool (==7) | — | `grid_status` | CONFIRMED (7=connected) |
| e1 | field_2b7 | int | — | `light_off_switch` | CONFIRMED |
| fb | field_287 | bitfield | bits | `grid_export_disabled` (+flags) | CONFIRMED |

### NEW — Not in upstream 0405 mapping
| Tag | Field | Conversion | Inferred Name | Notes |
|-----|-------|-----------|---------------|-------|
| a4 | field_30f | int | `unknown_status_code` | Near error fields |
| ae | field_433 | bool (==1) | `ac_socket_switch?` | On/off flag |
| af | field_187 | bool (==1) | `schedule_enabled?` | |
| b8 | field_47f | int | `ac_input_power?` | Near control fields |
| b9 | field_4cb | bool (==1) | `self_consumption_mode?` | Sets false default |
| ba | field_26b | int | `status_bitmask` | Upstream has commented-out bitmask |
| bb | field_26f | int | `heating_power` | Upstream comments confirm "bb"=heating |
| c7 | consumed | int | `home_load_preset` | Read but value flows into next op |
| e9 | field_2cb | int | `battery_capacity?` | Defaults to 0 |
| fc | field_287+bits | bitfield | `extended_flags` | Schedule/parallel data |
