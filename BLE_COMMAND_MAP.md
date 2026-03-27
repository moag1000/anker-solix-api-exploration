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
