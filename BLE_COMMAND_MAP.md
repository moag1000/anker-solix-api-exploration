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

# Wire Protocol Reference (from APK static analysis)

> These details are extracted from `ZXCommandTransformer`, `ZXCmdUtil`, `PPSDeviceCommands`,
> and `MqttCommandTransformer` in the decompiled assembly. They describe how the app
> constructs and parses BLE/MQTT messages at the byte level.

## TLV Binary Frame Format

Constructed in `ZXCommandTransformer::_getSettingCommand`:

```
[0xA1] [0x02] [dir] [tag] [len_lo] [len_hi] [type] [data...] [timestamp_4B] [xor_checksum]
```

| Offset | Bytes | Value | Description |
|--------|-------|-------|-------------|
| 0 | 1 | `0xA1` | Frame start marker (Smi 322 in assembly) |
| 1 | 1 | `0x02` | Protocol version |
| 2 | 1 | `0x42`/`0x44` | Direction: `0x42`=one direction, `0x44`=other (bit 4 of field_b) |
| 3 | 1 | tag | TLV tag byte (e.g., `0xa2`, `0xa3`) |
| 4-5 | 2 | length | Payload length + 1, **little-endian** (via `intToList2`) |
| 6 | 1 | type | Data type code (see below) |
| 7.. | N | data | Payload bytes |
| -4 | 4 | timestamp | Unix epoch **seconds**, little-endian (via `intToList4`) |
| -1 | 1 | checksum | XOR of all preceding bytes |

### Direction Detection
```
isResponse = (byte[0] & 0x0F) >> 3 & 1
```
Bit 3 of the low nibble: **0 = request, 1 = response**.

### Data Type Codes (from `_getDataType`)
| Code | Meaning | Byte Length | APK Function |
|------|---------|-------------|--------------|
| 1 | unsigned int (1 byte) | 1 | `intToList()` |
| 2 | integer (2 bytes) | 2 | `intToList2()` |
| 3 | variable/binary | N | raw bytes |
| 4 | integer (4 bytes) | 4 | `intToList4()` |

### Byte Order
**All multi-byte integers are little-endian** (low byte first):
- `intToList2`: `[value & 0xFF, (value >> 8) & 0xFF]`
- `intToList4`: same pattern, 4 bytes
- `listToInt`: reconstructs in same LE order

### Checksum
Simple XOR: `result = 0; for each byte: result ^= byte`

### Timestamp
`getCurrentTimestamp()`: `DateTime.now().toUtc().microsecondsSinceEpoch / 1000 / 1000`
= **Unix epoch seconds** (not milliseconds). Encoded as 4 bytes LE.

Tags `fe` (older) and `fd` (newer) carry timestamps:
- `fe`: seconds (4 bytes, `intToList4`)
- `fd`: milliseconds (used in CMD_COMMON_V2)

## MQTT JSON Envelope

MQTT payloads are **base64-encoded**, optionally **GZip-compressed** JSON.

### Decompression Flow (`MqttDecompressionUtil::decompressPayload`)
```
1. base64Decode(payload_string) → bytes
2. if bytes[0]==0x1F && bytes[1]==0x8B:  // GZip magic
     GZipCodec.decode(bytes) → decompressed
   else:
     bytes → decompressed  // not compressed
3. Utf8Codec.decode(decompressed) → json_string
4. jsonDecode(json_string) → Map<String, dynamic>
```

### JSON Structure (`MqttCommandTransformer::generateCommand`)
```json
{
  "head": {
    "version": "<protocol_version>",
    "client_id": "<mqtt_client_id>",
    "sess_id": "1",
    "msg_seq": 2,
    "cmd": 34,
    "cmd_status": 4,
    "sign_code": 2,
    "seed": "1",
    "timestamp": 1711622400,
    "device_pn": "A17C1",
    "device_sn": "<serial>"
  },
  "payload": {
    "device_sn": "<serial>",
    "account_id": "<user_id>",
    "data": "<base64_encoded_TLV_binary>"
  }
}
```

### Command Types (`MqttCommandType` enum → `cmd` field value)
| cmd | Type | Description |
|-----|------|-------------|
| 0x22 (34) | `normalCommand` | Standard device command |
| 0x0C (12) | `otaCommand` | OTA firmware update |
| 0x0C (12) | `a17y0OtaCommand` | A17Y0 sub-device OTA |
| 0x0A (10) | `uploadLogCommand` | Log upload |
| 0x32 (50) | `remoteScanWifi` | Remote WiFi scan |
| 0x34 (52) | `remoteSwitchWifi` | Remote WiFi switch |
| 0x18 (24) | `unbindDevice` | Device unbinding |
| 0x38 (56) | `getDeviceBssid` | Get device BSSID |

### Payload Variants (based on command type)
| Type | Extra payload fields |
|------|---------------------|
| normalCommand (0) | `data`: base64 TLV binary |
| otaCommand (2) | `ota_type`: "A17Y0" |
| uploadLog (4) | `log_id`: device_sn + " " + timestamp |
| wifiConfig (6) | `ssid`, `pwd`, `timezone`, `timeid` |

## BLE Specifics

### MTU Fragmentation (`AssembleCmdUtil::splitPackageCmd`)
- MTU overhead: **10 bytes**
- Default MTU: **200 bytes** (if 0 reported)
- Fragments: `(MTU - 10)` bytes per packet

### Encryption
- **ECDH** key exchange for BLE sessions (`SecureEcdhConfer`, `EcdhConfer`)
- **AES** encryption after key exchange (`AesConferV1`, `AesHelper`)
- Modes: AES-GCM and AES-CBC available
- Opcodes: `getAesKeyReq` / `getAesKeyRes` for key negotiation

## TLV Parsing Details

### Tag Iteration (`parseCommonData`)
- Tags are **sequential**: starts at `0xA1`, then `0xA2`, `0xA3`, ...
- Each TLV entry: **Tag = 1 byte**, **Length = 1 byte**, **Value = length bytes**
- First tag `0xA1` parsed specially (frame header), subsequent tags follow same pattern
- Values extracted via `bytesToHexString()` and stored as `Map<String, dynamic>` keyed by hex tag

### `customLengthBytes` Variant
Some opcodes have tags with non-standard lengths. A `Map<int, int>` overrides the
1-byte length for specific tags (e.g., tag `0xA2` might use 4-byte length prefix).

### parseWorkInfo vs parseDeviceAllInfo
- `parseDeviceAllInfo`: Full status dump — firmware versions, serial numbers, all settings + power data
- `parseWorkInfo`: Real-time operational data only — power, temperature, SOC. Subset of tags.
- Both use identical TLV format, different tag sets

### Dispatch (`_parsePayloadData`)
Routes by ZXOpcodeType to:
- `parseCommonData` — most standard opcodes
- `parseReqJsonData` — JSON-formatted responses
- `parseBluetoothListIData` — BLE device list
- `parseCommonDataWithDataType` — typed data variants
- `parseCommonDataWithCustomLengthBytes` — variable-length overrides

## Value Encoding Details

### Integer Reconstruction (`listToInt` algorithm)
```
result = 0
for i in 0..list.length:
    byte = list[i] & 0xFF
    shift = i * 8
    result += byte << shift    // LITTLE-ENDIAN: LSB first
```
Returns unsigned. `listToIntNormal` exists as big-endian variant.

### Scaling Factors (complete from assembly)
| Factor | Hex (IEEE 754 double) | Used For |
|--------|----------------------|----------|
| ×0.1 | `0x3FB999999999999A` | Voltage, temperature, power (÷10) |
| ×0.01 | `0x3F847AE147AE147B` | Current, energy (÷0.01) |
| ×0.001 | `0x3F50624DD2F1A9FC` | Fine precision values |
| ÷10 (sdiv) | — | Integer division in controllers |
| ÷100 (sdiv) | — | Battery charge/discharge power |

### Signed Value Patterns

**8-bit signed (temperature)** — used in ALL device families:
```
value = listToInt(bytes)
if value >= 0x80:  value -= 0x100    // two's complement
```
Stores to field offset `0x307` (temperature) across A1770, A1726, A17C0, A17C1.

**7-bit magnitude + sign bit** (A91B2 charging direction):
```
magnitude = value & 0x7F     // lower 7 bits
is_negative = (value & 0x80) == 0x80    // bit 7 = sign
```

**16-bit signed**: NOT explicitly handled. Values stay unsigned from `listToInt`.

### Sub-Byte Extraction (BYTES sub-fields)
Tags whose data contains multiple sub-fields use bitmask extraction:
```
field_a = value & 0x7F       // bits 0-6
field_b = (value & 0x80) >> 7  // bit 7
```
This is how thomluther's `BYTES: {"00": {...}, "01": {...}}` structures work at the binary level.

## MQTT Connection Details

### QoS & Keepalive
- **Default QoS**: 1 (atLeastOnce)
- Available: atMostOnce(0), atLeastOnce(1), exactlyOnce(2)
- **Keepalive**: configurable period, auto-ping, disconnect on no ping response
- **Auto-reconnect**: built-in, with status logging
- **Transport**: TLS-secured WebSocket (`MqttServerSecureConnection`)

### Request-Response Correlation
- `sess_id`: hardcoded `"1"` (not dynamic)
- `msg_seq`: hardcoded `2` (not dynamic)
- Correlation via MQTT topic + `device_sn`, NOT sequence numbers

### Debounce System (systematic)
Every parse and HTTP call uses debounce:
- Key format: `"pps_parse_common_" + deviceSn` (per device, per operation)
- HTTP: `debounceMills` parameter on requests
- UI: separate button debounce (`ButtonDebounce`) + `AnkerDebounceThrottle`

### Decryption Flow (in parseCommonData)
```
if encrypted && device.hasKey:
    data = AesHelper.aesGcmDecrypt(data, key)     // AES-GCM preferred
elif encrypted:
    data = AesHelper.decrypt(data)                  // AES-CBC fallback
```

## Event Types (from string pool)
| Event | Description |
|-------|-------------|
| `event_charge_status_report` | Charging state change |
| `event_error_code_report` | Error occurred |
| `event_current_report` | Current measurement |
| `event_protective_charging_score_report` | Battery protection score |
| `event_charging_mode_report` | Mode change |
| `event_schedule_status_report` | Schedule state change |
| `event_unbind_extended_device_report` | Device unbind event |

## HES / X1 JSON Protocol (NOT TLV)

X1/HES devices (`A5101`) use a **different protocol**:
- Communication via HTTP to `/charging_hes_svc/*` endpoints
- Payloads are plain JSON (abbreviated field keys like `pvPower`, `batPower`)
- MQTT subscription delivers JSON "trans" payloads
- Uses `att_id` (attribute ID) system for BLE, not TLV tags
- See [devices/x1_hes_e10.md](devices/x1_hes_e10.md) for field dictionary

---

# SET Commands (App → Device)

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

## A2345 — Prime Charger 250W 0405 Status Tags (P3)

28 tags parsed in `parseDeviceAllInfo`. Debug strings from assembly.

| Tag | Format | Name / Debug String | Notes |
|-----|--------|---------------------|-------|
| fe | int | `msg_timestamp` | |
| a2 | getMainVersionWithHex | `sw_version` | "打印版本：otaModuleVersion" |
| a3 | int → field_3db | `error_state?` | "设备错误状态" |
| a4-a6 | → `parseChargePortInfo()` | `port_1/2/3_info` | Sub-parser for per-port data |
| a7 | int | `port_4_info?` | A91B2 has this as 4th port |
| a8-ab | int | port power/status fields | Sequential |
| ac-af | int | extended port fields | |
| b0-b5 | int | energy/battery fields | |
| b7-bf | int | extended settings | Only in A2345, not A91B2 |
| bc | int | `ac_port_switch` | "acPortSwitchState acPortNumber" |
| b8 | bitmask | `compatibility_switch` | Bits: 0x10,0x20,0x40,0x80,0x100,0x200,0x400 |
| — | bitmask | `ufcs_switch` | "UFCSSwitchValue" — Bits: 0x10,0x20 |

### A2345 Sub-Parser: parseChargePortInfo
Extracts per USB-C port: manufacturer, product, protocol, voltage, current.
Debug: "充电设备1的信息" (charging device 1 info)

### A2345 Port Debug Fields
| Debug String | Meaning |
|-------------|---------|
| "c1端口状态/电压/电流" | C1 port status/voltage/current |
| "c2端口状态/电压/电流" | C2 port status/voltage/current |
| "a端口状态/电压/电流" | USB-A port status/voltage/current |
| "p端口状态/电压/电流" | P port status/voltage/current |
| "屏幕关闭时间" | Screen off time |
| "屏幕亮度" | Screen brightness |
| "时钟屏保开关" | Clock screensaver switch |
| "蜂鸣器开关状态" | Buzzer switch state |
| "底座指示灯开关状态" | Base indicator light switch |
| "放电优化信息" | Discharge optimization info |
| "充电优化信息" | Charge optimization info |
| "输入总电量" | Input total energy |
| "输出总电量" | Output total energy |
| "底座状态" | Base status |
| "电池健康度" | Battery health (SOH) |
| "电池循环次数" | Battery cycle count |

---

## A17C2 — Solarbank 2 AC / Hybrid Inverter Status (P1)

Uses A17C1 base protocol with hybrid-inverter-specific extensions.
Debug strings reveal exact field meanings (power in Watts):

| Tag | Debug String (Chinese) | Resolved Name | Unit |
|-----|----------------------|---------------|------|
| ac | "电池充放电功率（单位W）" | `bat_charge_discharge_power` | W |
| ab | "总输出功率（单位W）" | `total_output_power` | W |
| c2 | "总输入功率 设备主页totalInput" | `total_input_power` | W |
| ae | "并网口功率（单位W）" | `grid_port_power` | W |
| af | "离网口功率（单位W）" | `off_grid_port_power` | W |
| b0 | "pv累计发电量（单位Wh）" | `pv_cumulative_generation` | Wh |
| b1 | "储能累计充电量（单位Wh）" | `storage_cumulative_charge` | Wh |
| d3 | "标识当前是否0溃网" | `grid_collapse_flag` | bool |

Additional: "副包数量" = sub-package count, "设备功率上限值" = device power upper limit,
"设备AC功率上限值" = AC power upper limit, "isMeterAvailable" = smart meter present.

---

## A1340 — Portable Power Bank Status (P3)

Richest PPS parser (10841 lines). 4 ports with individual monitoring.

### Per-Port Fields (USB-C1, USB-C2, USB-A, DC/P)
| Field | Debug String | Format |
|-------|-------------|--------|
| status | "c1端口状态" | int |
| voltage | "c1端口电压" | int (×0.1V?) |
| current | "c1端口电流" | int (×0.01A?) |
| power | per port | int |
| repeat | "c1端口repeat" | int |
| manufacturer | "C1厂商=" | string |
| product | "C1产品=" | string |
| protocol | from `chargeProtocol` list | string |

### Device-Level Fields
| Debug String | Resolved Name |
|-------------|---------------|
| "电池信息: 充电状态" | `battery_charge_state` |
| "充放电时间" | `charge_discharge_time` |
| "电池健康度" | `battery_soh` |
| "电池循环次数" | `battery_cycle_count` |
| "电池电量" | `battery_level` |
| "获取蜂鸣器开关状态" | `buzzer_switch` |
| "获取蜂鸣器时间" | `buzzer_time` |
| "获取充电开关状态" | `charge_switch_state` |
| "获取放电开关状态" | `discharge_switch_state` |

---

## Shelly (3rd Party) Status Fields

| Debug String | Field Name |
|-------------|-----------|
| "fromGrid" | `grid_import_power` |
| "toGrid" | `grid_export_power` |
| "fromGridSum" | `grid_import_total` |
| "toGridSum" | `grid_export_total` |
| "shellyPlugOutPutPower" | `plug_output_power` |
| "shellyPlugSwitch" | `plug_switch_state` |
| "totalChargingPower" | `total_charging_power` |

---

## Cross-Device Discoveries

### New Device Type: A17D0
Found in A17B1 parser (line 3663). Referenced 4× alongside A1790/A1790P.
Appears to be an **unreleased battery type** supported by the A17B1 hub.

### A5140 Microinverter = A1780 Protocol
The A5140 microinverter reuses `A1780DeviceCommands` entirely.
No device-specific BLE protocol — shares PPS command structure.

### Device Model Checks in A17C1 Parser
The `parseDeviceAllInfo` entry checks device model against:
`"A17C1"`, `"A17C5"`, `"A17C3"`, `"A17C2"` — confirming all SB2 variants
share the same base parser with model-specific branches.

### Timer Duration Enum (A17C5)
`"30min"`, `"hr"`, `"hrs"`, `"never"` — device timeout display values.

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
| a3 | field_187 | List\<int\>, len≥2 check, [4]==2→bool | **NEW** — `timer_data` (sub-parsed: relay state + timer status) | Cross-device: field_187 = schedule flag |
| a4 | field_47b+4bb | bool (`cmp #1`), dual store | `ac_output_power_switch` | CONFIRMED |
| a5 | field_3db | int, unsigned | **NEW** — `error_code` | Cross-device: field_3db = error_code on A17C1 + A17C0 |
| a6 | field_7b | getMainVersionWithHex | `sw_version` | CONFIRMED |
| a7 | field_2d7 | int | `sw_controller` | CONFIRMED |
| a8 | field_483 | int × 0.1 | `voltage` | CONFIRMED (float) |
| a9 | field_47f | int × 0.01 | `current` | CONFIRMED (float) |
| aa | field_487 | int × 0.1 | `power` | CONFIRMED (float) |
| ab | field_48b | int | `output_energy` (upstream ×0.001) | CONFIRMED |
| ad | → parseCountDownInfo() | sub-parser | `timer_status` | CONFIRMED |
| ae | field_49b | bool (`cmp #1 → csel`) | **NEW** — `countdown_active` | Boolean flag for delayed toggle |

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

### NEW — Not in upstream 0405 mapping (resolved via assembly analysis)
| Tag | Field | Format | Inferred Name | Evidence |
|-----|-------|--------|---------------|---------|
| a4 | field_30f | int, unsigned | `battery_soc_2` | Same offset as A17X8 a4, cross-device = SOC area |
| ae | field_433 | bool (`cmp #1 → csel`) | `ac_socket_switch` | Boolean on/off, unique to A17C1 |
| af | field_187 | bool (`cmp #1 → csel`) | `schedule_enabled` | Same offset as A17X8 a3 (field_187 = schedule flag cross-device) |
| b8 | field_47f | int, unsigned, default=0 | `ac_input_power` | Same offset as A17X8 a9 (current ×0.01), raw int here = milliwatts? |
| b9 | field_4cb | bool (`cmp #1`, default=false) | `self_test_enabled` | Defaults false when absent, boolean flag |
| ba | field_26b | int, unsigned | `cutoff_power` | Same offset as A17C0 ba — confirmed cross-device match |
| bb | field_26f | int, unsigned | `heating_power` | Same offset as A17C0 bb — upstream comments confirm "bb"=heating |
| c7 | (consumed) | int, NOT stored | `home_load_power_raw` | Value read but consumed by c8 ÷10 chain → `ac_socket_power` |
| e9 | field_2cb | int, unsigned, default=0 | `battery_capacity` | Writes `wzr` (zero register) if absent |
| fc | field_287 | List\<int\> raw + bit extraction | `extended_status_flags` | [2]→parallel_connected, [10]→export_enabled, [14]→schedule_active_2, [18]→config_value (all `cmp #2`) |

---

## A17C0 — Solarbank Gen 1 0405 Status Tags

23 upstream-confirmed + 11 new. Shares protocol base with A17C1.

### Confirmed tags (matching upstream)
| Tag | Upstream Name | Tag | Upstream Name |
|-----|-------------|-----|-------------|
| a2 | `device_sn` | a3 | `battery_soc` |
| a6 | `sw_version` | a7 | `sw_controller` |
| a8 | `hw_version` | a9 | `temp_unit_fahrenheit` |
| aa | `temperature` (signed) | ab | `photovoltaic_power` |
| ac | `output_power` | ad | `charging_status` |
| b0 | `bat_charge_power` | b1 | `pv_yield` |
| b2 | `charged_energy` | b3 | `output_energy` |
| b4 | `output_cutoff_data` | b5 | `lowpower_input_data` |
| b6 | `input_cutoff_data` | b7 | `inverter_brand` |
| b8 | `inverter_model` | b9 | `min_load` |
| c0 | `0w_switch_sn` | c1 | `0w_switch_bt_mac` |
| fe | `msg_timestamp` | | |

### NEW tags (resolved via assembly + cross-device correlation)
| Tag | Field | Format | Resolved Name | Evidence |
|-----|-------|--------|---------------|---------|
| a4 | field_30f | int | `battery_soc_2` | Upstream "?" — APK confirms. Same offset as A17C1 a4 |
| a5 | field_3db | int | `error_code` | Cross-device: field_3db = error_code on A17C1 + A17X8 |
| ae | field_3df | int/binary | `schedule_slot_data` | Upstream notes binary schedule format |
| af | field_f | int | `unknown_flag` | |
| ba | field_26b | int | `cutoff_power` | Cross-device match with A17C1 ba |
| bb | field_26f | int | `heating_power` | Cross-device match with A17C1 bb |
| bc | field_48b | object | `sub_device_connection` | Triggers `createByProductCode("A17Y0")` — sub-battery init! |
| bd | (nested) | forwarded | `sub_device_data` | Data forwarded to A17Y0 sub-device parser |
| be | field_27b | int | `extended_setting_1` | |
| bf | field_27f | int | `extended_setting_2` | |
| fb | field_287 | List\<int\> raw | `status_flags` | Same pattern as A17C1 fb bitfield |
| fc | field_283 | int | `status_counter` | |

---

## A172X — C300/C300X 0405 Status Tags (P3)

29 upstream-confirmed + 4 new. APK **confirms** upstream "?" tags b1-b4 as firmware versions.

### Key confirmed tags
| Tag | Upstream Name | Tag | Upstream Name |
|-----|-------------|-----|-------------|
| a2 | `dc_output_timeout_seconds` | a3 | `remaining_time_hours` (×0.1) |
| a4-a7 | `usbc_1-4_power` | a8-a9 | `usba_1-2_power` |
| aa | `dc_12v_1_power` | ab | `photovoltaic_power` |
| ac | `dc_input_power_total` | ad | `dc_output_power_total` |
| af | `battery_soc_ah` (×0.001) | b0 | `sw_version` |
| b5 | `temperature` (signed) | b6 | `charging_status` |
| b7 | `battery_soc` | b8 | `battery_soh` |
| b9-bc | `usbc_1-4_status` | c1 | `overload_event` |
| c3 | `device_sn` | c4 | `device_timeout_minutes` |
| c5 | `display_timeout_seconds` | c7 | `display_mode` |
| c8 | `light_mode` | c9 | `temp_unit_fahrenheit` |

### Upstream "?" tags CONFIRMED by APK
| Tag | Upstream had | APK confirms | Format |
|-----|-------------|-------------|--------|
| b1 | `version1?` (commented) | **Parsed** — `fw_sub_version_1` | int |
| b2 | `version2?` (commented) | **Parsed** — `fw_sub_version_2` | int |
| b3 | `version3?` (commented) | **Parsed** — `fw_sub_version_3` | int |
| b4 | `version4?` (commented) | **Parsed** — `fw_sub_version_4` | int |

### NEW tags (resolved)
| Tag | Field | Format | Resolved Name | Evidence |
|-----|-------|--------|---------------|---------|
| ae | field_2cf | int | `unknown_power` | Between output_total and soc_ah |
| c6 | field | int | `unknown_setting` | |
| cc | field | int | `unknown` | |
| f9 | field_42b | int | `unknown_flag` | |

---

## A1771 — C1000/C1000X 0405 Status Tags (P3)

30 upstream-confirmed + **18 new** — biggest gap in PPS family.

### Key confirmed tags
| Tag | Upstream Name | Tag | Upstream Name |
|-----|-------------|-----|-------------|
| a4 | `remaining_time_hours` | a5 | `grid_to_battery_power` |
| a6 | `ac_output_power` | a7-a8 | `usbc_1-2_power` |
| a9-aa | `usba_1-2_power` | ae | `dc_input_power` |
| af | `photovoltaic_power` | b0 | `output_power_total` |
| b3 | `sw_version` | b9 | `sw_expansion` |
| ba | `sw_controller` | bd | `temperature` (signed) |
| be | `exp_1_temperature` | c1 | `main_battery_soc` |
| c2 | `exp_1_soc` | d0 | `device_sn` |
| d1 | `max_load` | d2 | `device_timeout_minutes` |
| d3 | `display_timeout_seconds` | d5 | `display_mode` |
| dc | `light_mode` | dd | `temp_unit_fahrenheit` |

### NEW tags (18 — resolved where possible)
| Tag | Field | Format | Resolved Name | Evidence |
|-----|-------|--------|---------------|---------|
| a2 | field_1ab | int | `dc_output_timeout?` | Same offset pattern as A1790 |
| a3 | field_1af | int | `ac_output_timeout?` | Sequential with a2 |
| ab | field_1f3 | int | `dc_12v_power?` | Between usba_2 and dc_input |
| ac | field_1f7 | int | `dc_12v_2_power?` | Sequential |
| ad | field_1fb | int | `dc_input_power_2?` | Before photovoltaic |
| b1 | field_2cf | int | `unknown_energy` | Between output_total and sw_version |
| b2 | field_2d3 | int | `unknown_energy_2` | Sequential |
| b4-b8 | field_2db-2eb | int | `fw_sub_version_1..5` | Between sw_version(b3) and sw_expansion(b9) |
| bc | field_303 | int | `unknown_status` | |
| bf | field_30f | int | `exp_2_temperature?` | Near exp_1_temperature(be), signed? |
| c0 | field_313 | int | `exp_2_soc?` | Near exp_1_soc(c2) pattern |
| d4-d6 | field | int | `display_settings` | Display/timeout area |
| da | field | int | `unknown_mode` | |
| df-e0 | field | int | `switch_flags` | |
| e2-e4 | field | int/bool | `extended_status` | e3: bool (`cmp #1 → csel`) |
| f7 | field_f | int | `unknown_flag` | |

---

## A1790 — F3800 0405 Status Tags (P3)

39 upstream-confirmed + **19+ new**. Includes generator/ATS fields.

### Key confirmed tags
| Tag | Upstream Name | Tag | Upstream Name |
|-----|-------------|-----|-------------|
| a4 | `remaining_time_hours` | a5 | `ac_input_power` |
| a6 | `ac_output_power` | a7-a9 | `usbc_1-3_power` |
| aa-ab | `usba_1-2_power` | ad | `main_battery_soc` |
| ae | `photovoltaic_power` | af | `pv_1_power` |
| b1 | `bat_charge_power` | b2 | `output_power` |
| b4 | `bat_discharge_power` | b5 | `sw_version` |
| ba | `sw_expansion` | bc | `ac_output_power_switch` |
| bd | `charging_status` | be | `temperature` (debug: "bmsTempMajor") |
| bf | `display_status` | c0 | `battery_soc` (total) |
| c1 | `max_soc` | cc | `device_sn` |
| cd | `ac_input_limit` | cf | `display_timeout_seconds` |
| d5 | `display_mode` | d8 | `temp_unit_fahrenheit` |
| d9 | `light_mode` | f6 | `region` |
| f7 | `port_memory_switch` | fe | `msg_timestamp` |

### NEW tags (19+ resolved)
| Tag | Field | Format | Resolved Name | Evidence |
|-----|-------|--------|---------------|---------|
| a2 | field_1ab | int | `dc_output_timeout?` | Before remaining_time, timeout area |
| a3 | field_1af | int | `ac_output_timeout?` | Sequential with a2 |
| b3 | field_2cf | `bytesToHexString` → string | `battery_serial_hex` | NOT listToInt — hex string conversion! |
| b6 | field_2db | int | `fw_sub_version_1` | Between sw_version(b5) and sw_expansion(ba) |
| b7 | field_2df | int | `fw_sub_version_2` | Sequential |
| b8 | field_2e3 | int | `fw_sub_version_3` | Sequential |
| b9 | field_2e7 | int | `fw_sub_version_4` | Sequential |
| bb | field | int | `sw_expansion_2` | Between sw_expansion(ba) and ac_switch(bc) |
| c9-cb | field | int | `port_status` fields | After max_soc area |
| ce | field | int | `unknown_setting` | Before display_timeout |
| d0-d2 | field | int | `timeout_settings` | Display/power timeout area |
| d6-d7 | field | int | `mode_settings` | Between display and temp_unit |
| da-db | field | int | `light_settings` | After light_mode |
| dd | field | int | `unknown_switch` | |
| de-df | field | int | `extended_flags` | |
| f8 | field_197+19b | List\<int\>, DeviceSavingModeEnum | `port_saving_mode` | [0]→1=normal/2=smart/4=custom, [2]→mode2, [4]→bool(==2) |
| f9 | field | complex | `port_saving_mode_ext` | Continuation of f8 pattern |

---

## A17A0 / A17A3-A5 — EverFrost Cooler (entirely unmapped, P4)

> **Different protocol**: Uses command-key map (not TLV tags). NOT in upstream at all.

### Upload Commands (device → app status reports)
| Command | Description |
|---------|-------------|
| `uploadDeviceInfo` | Full device info |
| `uploadInputPower` | Charging input power |
| `uploadOutputPower` | Cooling output power |
| `uploadBatteryValue` | Battery level |
| `uploadBatteryState` | Charging state |
| `uploadSingleBoxTemp` | Single-zone current temp |
| `uploadDoubleBoxLTemp` | Dual-zone LEFT current temp |
| `uploadDoubleBoxRTemp` | Dual-zone RIGHT current temp |
| `uploadSingleBoxSetTemp` | Single-zone SET temp |
| `uploadDoubleBoxLSetTemp` | Dual-zone LEFT SET temp |
| `uploadDoubleBoxRSetTemp` | Dual-zone RIGHT SET temp |
| `uploadDoubleBoxLSwitchState` | LEFT zone on/off |
| `uploadDoubleBoxRSwitchState` | RIGHT zone on/off |
| `uploadTempUnit` | Temperature unit (C/F) |
| `uploadLcdLight` | LCD brightness |
| `uploadScreenAlwaysOn` | Screen always-on |
| `uploadVoltageProtection` | Low-voltage protection |
| `uploadExceptionMsgCode` | Exception messages |
| `uploadErrorCode` | Error codes |
