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

**Note**: Two protocol layers exist:
- **MQTT binary**: `FF 09` header (thomluther's mqtt_monitor), `03 00/01 0f` pattern
- **BLE command**: `0xA1` tag marker (APK's ZXCommandTransformer), inside the payload

```
MQTT layer: [FF 09] [len_lo len_hi] [03 00/01 0f] [cmd_lo cmd_hi] [TLV payload...]
BLE layer:  [0xA1] [0x02] [dir] [tag] [len_lo] [len_hi] [type] [data...] [timestamp_4B] [xor_checksum]
```

| Offset | Bytes | Value | Description |
|--------|-------|-------|-------------|
| 0 | 1 | `0xA1` | BLE TLV tag frame marker (inside MQTT payload) |
| 1 | 1 | `0x02` | Protocol version (APK-observed) |
| 2 | 1 | `0x42`/`0x44` | Direction byte (APK internal) |
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
| 1 (ui) | unsigned int | 1 | `intToList()` |
| 2 (sile) | **signed** int, little-endian | 2 | `intToList2()` |
| 3 (var) | variable (1-4 bytes, can be signed) | N | raw bytes |
| 4 (bin) | **bitmap** (bit pattern for settings) | N | raw bytes |
| 5 (sfle) | signed float, little-endian | 4 | — |
| 0 (str) | string | N | — |

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
    "sess_id": "1234-5678",
    "msg_seq": 1,
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

## MQTT Topic Structure

Topics are deterministic, built from device info:

```
Subscribe: cmd/anker_power/{product_key}/{device_sn}/app/res     (command responses)
Subscribe: dt/anker_power/{product_key}/{device_sn}/basic_info   (basic device info)
Subscribe: dt/anker_power/{product_key}/{device_sn}/param_info   (parameter updates)
Publish:   cmd/anker_power/{product_key}/{device_sn}/req         (send commands)
```

`product_key` = device product type identifier, `device_sn` = serial number.

---

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

### Sub-Field Extraction — NOT Bitmasks, but Indexed Byte Arrays
The Dart AOT compiler does **not** generate ARM `and` bitmask instructions for field extraction.
Instead, the APK stores raw `List<int>` and accesses individual bytes by index:

```
// APK pattern (Dart → ARM64):
list[N] == 2  →  "feature enabled" (value 2 = true in this protocol)
list[N] raw   →  raw value stored to separate field offset
```

The only traditional bitmask pattern found is **7-bit magnitude + sign bit** (A91B2):
```
magnitude = value & 0x7F       // bits 0-6
is_negative = (value & 0x80)   // bit 7
```

thomluther's `BYTES: {"00": {...}, "01": {...}}` structures correspond to byte-index access,
not bit-level extraction. The "00", "01" keys are **byte positions** within the data payload.

## MQTT Connection Details

### QoS & Keepalive
- **Default QoS**: 1 (atLeastOnce)
- Available: atMostOnce(0), atLeastOnce(1), exactlyOnce(2)
- **Keepalive**: configurable period, auto-ping, disconnect on no ping response
- **Auto-reconnect**: built-in, with status logging
- **Transport**: TLS-secured WebSocket (`MqttServerSecureConnection`)

### Request-Response Correlation
- `sess_id`: hardcoded (APK uses `"1"`, upstream uses `"1234-5678"` — not dynamic either way)
- `msg_seq`: hardcoded (APK uses `2`, upstream uses `1` — not dynamic either way)
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

## Data Structures (byte-level layouts from assembly)

### CountDownInfo (A17X8 Smart Plug timer — tag `0xAD`)
Minimum payload: **8 bytes**. Class size: 0x28 (40 bytes).

```
Offset  Bytes  Field            Derivation
[0..3]  4      totalTimeMinutes listToInt(bytes[0:3]) — little-endian
[4]     1      (unused)
[5..7]  3      elapsedTime      listToInt(bytes[5:8])
[6]     1      switchState      0=off, 1=on (single byte)
[8]     1      endHour          hour of shutdown
```
`remainingTime = max(0, totalTimeMinutes - elapsedTime)`

### TimingInfo (A17X8 Smart Plug schedule — tag `0x7C`)
Per schedule entry: **5 fixed bytes + variable weekday bytes**. Class size: 0x40 (64 bytes).

```
Offset  Bytes  Field        Values
[0]     1      id           Schedule slot index (0-based)
[2]     1      switchState  0=off, 2=on (note: 2, not 1!)
[4]     1      hours        Start hour (0-23)
[6]     1      minutes      Start minute (0-59)
[8]     1      endHour      End hour (0-23)
[9..]   N      weekdays     Variable: one byte per day (1=Mon..7=Sun)
```
Weekdays are **not a bitmask** — they are sequential day numbers of variable length.

### DischargeTimeModel (A17C1 Solarbank schedule — `setTacticsTime` 005e)
**14 maximum time slots**. Each slot: 4 fields, 32 bytes (0x20).

| Field | Offset | Type | Description |
|-------|--------|------|-------------|
| startTime | 0x08 | int | Start time (minutes from midnight?) |
| endTime | 0x0c | int | End time |
| power | 0x10 | int | Output power (W) |
| chargingPercentage | 0x14 | int | Charge target (%) |

The full `setTacticsTime` function is 14020 bytes — the largest in the codebase.
Uses tags a2-bb (30 tags) + fd (timestamp).

### SubBatteryInfo (A1790 F3800 expansion pack)
Class size: 0x4C (76 bytes). Complete fields:

| JSON Key | Type | Description |
|----------|------|-------------|
| `sn` | String | Serial number |
| `batteryId` | String | Battery identifier |
| `snNumber` | int | SN as number |
| `version` | int | Firmware version |
| `temperature` | int | Battery temperature |
| `chargingStatus` | int | Charge status code |
| `electricQuantity` | int | SOC / charge level (%) |
| `heatingFilmOpened` | int | Heating film active flag |
| `healthDegree` | int | Battery health (%) |
| `isLightBlink` | int | LED blink indicator |
| `lightOff` | int | LED off indicator |
| `powerOff` | int | Power off status |
| `errorCode` | int | Error code (integer, not bitmask) |
| `type` | int | Battery type |
| `equalType` | int | Equalization type |
| `status` | int | Status code |
| `batteryPackType` | int | Pack type identifier |

### OutputPortInfo (A2345 Prime Charger — per USB port)
Minimum payload: **7 bytes**. Class size: 0x40 (64 bytes).

```
Offset  Bytes  Field        Unit
[0]     1      portIndex    Port number (0-based)
[1..4]  4      voltage      mV (millivolts, little-endian)
[5..8]  4      current      mA (milliamps)
[9..12] 4      power        mW (milliwatts)
[14]    1      status       Port status code
[16]    1      temperature  Degrees (single byte)
```

Additional per-port protocol info: `chargeProtocol`, `maxChargePower`, `protocolCurrent`, `protocolVoltage`.

### Firmware Version Format
Two encoding variants:

**`getMainVersion`** — decimal dotted: each byte → decimal string, joined with `.`
- Input: `[1, 5, 0]` → Output: `"1.5.0"`
- Default 3 segments, configurable

**`getMainVersionWithHex`** — hex dotted with `v` prefix: each byte → hex string
- Input: `[0x01, 0x05, 0x00]` → Output: `"v01.05.00"`
- Used in debug logs: "17c1总包版本号" / "17X8总包版本号"

### DataFlow (A17B1 power flow — nested JSON object)
Exactly **8 nullable int fields**, fixed order:

```json
{"p2bp": null, "mpp": null, "p2lp": null, "p2gp": null,
 "b2lp": null, "b2gp": null, "g2bp": null, "g2lp": null}
```

| Key | Full Name |
|-----|-----------|
| p2bp | PV → Battery Power |
| mpp | MPPT Power (max power point tracking) |
| p2lp | PV → Load Power |
| p2gp | PV → Grid Power |
| b2lp | Battery → Load Power |
| b2gp | Battery → Grid Power |
| g2bp | Grid → Battery Power |
| g2lp | Grid → Load Power |

### Bd (A17B1 battery device list entry)
In the `bds` array. Class size: 0x20 (32 bytes).

```json
{"sn": "...", "related": "...", "name": "...", "power": null, "error": null, "soc": null}
```

All power/error/soc fields are nullable int.

### Error Codes
**Simple integers**, not bitmasks or lists. Companion tags carry UTF-8 error message strings.
Example: tag 0xA2 = error code (int), tag 0xA4 = error message (Utf8 string).

---

# Enum Value Tables (from objs.txt)

> Concrete integer values used in SET commands and returned in STATUS messages.
> Extracted from Dart enum object pool with actual API values (`off_14` field).

### EmsModeType — HES Work Mode (`workMode` / `sceneMode`)
| API Value | Name | Description |
|-----------|------|-------------|
| 1 | `selfConsumption` | Self-consumption (Eigenverbrauch) |
| 4 | `manualPowerBackup` | Manual power backup |
| 5 | `timeOfUse` | Time-of-use / peak-valley pricing |
| 8 | `onlyBackupPower` | Backup-only mode |
| 9 | `severeWeatherMode` | Severe weather / Storm Guard |
| 10 | `offGrid` | Off-grid mode |

### EvChargerDeviceStatus — OCPP-aligned charger status
| API Value | Name | Description |
|-----------|------|-------------|
| 0 | `available` | Ready to charge |
| 1 | `preparing` | Connector plugged, not yet charging |
| 2 | `charging` | Actively charging |
| 3 | `suspendedEVSE` | Suspended by charger |
| 4 | `suspendedEV` | Suspended by vehicle |
| 5 | `finishing` | Charge complete |
| 6 | `reserved` | Reserved |
| 7 | `unavailable` | Unavailable |
| 8 | `faulted` | Fault condition |

### StartWayEnum — EV Charge Start Method
| API Value | Name |
|-----------|------|
| 1 | `wifi` |
| 2 | `ble` |
| 3 | `touch` |
| 4 | `rfid` |
| 5 | `plug` (plug & charge) |
| 6 | `timed` |
| 7 | `autoResume` |
| 8 | `modbus` |
| -1 | `unknown` |

### EvChargerGestureFunction — Swipe/Touch Actions
| API Value | Action |
|-----------|--------|
| 0 | `disable` |
| 1 | `startCharging` |
| 2 | `stopCharging` |
| 3 | `startBoostMode` |
| 4 | `startImmediately` |

### GeneratorMode — A7320 Range Extender
| API Value | Name | Description |
|-----------|------|-------------|
| 0 | `silentDc` / `dcQuiet` | DC quiet mode |
| 1 | `saveDc` / `dcECO` | DC economy |
| 2 | `fastDc` / `dcTurbo` | DC turbo |
| 3 | `eco` / `acECO` | AC economy |
| 4 | `turbo` / `acTurbo` | AC turbo |
| 5 | `exerciseAc` / `acExercise` | AC exercise |
| 6 | `exerciseDc` / `dcExercise` | DC exercise |

### ScreenBrightType — Display Brightness (all PPS + charger devices)
| API Value | Level |
|-----------|-------|
| 0 | off |
| 1 | low |
| 2 | medium |
| 3 | high |

### LoadBalancingErrorType — EV Charger
| API Value | Meaning |
|-----------|---------|
| 0 | `normal` |
| 1 | `mainDeviceDisconnected` |
| 2 | `mainDeviceAndMeterDisconnected` |

### BatterySubPackageConnectionStatus — A1790 Expansion
| API Value | State |
|-----------|-------|
| 1 | `normal` |
| 2 | `offline` |
| 3 | `highTemp` |
| 4 | `mainPackagePressureDifference` |
| 5 | `subPackagePressureDifference` |
| 6 | `other` |

### AddDeviceType — Station Device Categories
| Index | Type |
|-------|------|
| 0 | `homeBackupSystem` |
| 1 | `energyStorage` |
| 2 | `smartMeter` |
| 3 | `generator` |
| 4 | `pps` |

### EvStationType — Compatible Station Types for EV Charger
| API Value | Station |
|-----------|---------|
| 5 | A17C1 (Solarbank 2 Pro) |
| 10 | A17C3 (Solarbank 2 Plus) |
| 11 | A17C2 (Solarbank 2 AC) |
| 12 | A17C5 (Solarbank 3) |
| 18 | AE100 (Power Dock) |

---

# GET→SET Communication Patterns

> The app NEVER sends a SET without first doing a GET to retrieve valid ranges.
> Power limits, SOC values, and schedules are **server-constrained**, not hardcoded.

### Pattern: Power Limit Change
```
1. GET /power_service/v1/site/get_power_limit
   → Response: {legal_power_limit, power_limit_option: [{value, label}...], ac_input_power_unit}
2. User selects from power_limit_option (clamped to legal_power_limit)
3. SET /power_service/v1/site/set_site_device_param
   → param_type=19, param_data={"power_limit":{"limit":<selected>,"limit_real":<selected>}}
```

### Pattern: SOC Reserve Change
```
1. GET /power_service/v1/site/get_site_device_param (param_type=18)
   → Response: {soc_list: [{id, soc, is_selected}...], switch_0w, enable_0w, feed-in_power_limit}
2. User selects from soc_list options
3. SET /power_service/v1/site/set_site_device_param (param_type=18)
   → param_data={soc_list: [{id:<selected_id>, soc:<value>, is_selected:1}...], switch_0w, enable_0w}
```

### Pattern: Usage Mode + Schedule (A17C1)
```
1. GET /power_service/v1/site/get_site_device_param (param_type=6)
   → Response: {mode_type, custom_rate_plan, default_home_load, min_load, max_load, step}
2. User builds schedule (clamped to min_load..max_load with step)
3. SET /power_service/v1/site/set_site_device_param (param_type=6)
   → param_data={mode_type:<1-8>, custom_rate_plan:[{index,week,ranges:[{start_time,end_time,power}]}]}
   AND simultaneously via MQTT/BLE: command 005e with mode + schedule tags
```

### Pattern: Device Attributes (Power/Grid)
```
1. GET /power_service/v1/app/device/get_device_attrs
   → Response: {attributes: {pv_power_limit, ac_power_limit, power_limit, switch_0w, ...}}
2. User modifies one attribute
3. SET /power_service/v1/app/device/set_device_attrs
   → {device_sn: "...", attributes: {<changed_field>: <new_value>}}
```

### Pattern: EV Charger Max Current
```
1. Device reports ev_max_current capability in device info
2. App reads maxCurrentRangeHint (localized range string, e.g. "6-32")
3. User selects within range
4. SET via prop_write_evcharger: {"maximumCurrentLimit": <value>}
```

### Pattern: Smart Plug Toggle (simplest)
```
Single BLE/MQTT command: 007a with tag a2 = 0(off) or 1(on)
No GET required — fire and forget.
```

---

# Value Ranges and Constraints

> **Critical**: Value ranges are NOT hardcoded in the app. They are retrieved from the
> server per-device, per-region. The table below shows the **field types and known
> constraints** from the APK — actual valid ranges MUST be queried via GET first.

| Field | Type | Known Values | Constraint Source | Devices |
|-------|------|-------------|-------------------|---------|
| `switch_0w` | int | 0=allow export, 1=block | Fixed (boolean) | A17C1, A17C0 |
| `enable_0w` | int | 0, 1 | Fixed (boolean) | A17C1 |
| `temp_unit_fahrenheit` | int | 0=Celsius, 1=Fahrenheit | Fixed (enum) | All |
| `light_mode` | int | 0=normal, 1=mood (SB); 0=off,1-3=low/med/high (PPS) | Fixed (enum) | All |
| `display_mode` | int | 0=off, 1=low, 2=medium, 3=high | Fixed (ScreenBrightType) | PPS, Charger |
| `usage_mode` | int | 1,2,3,4,5,7,8 | Fixed (UsageModeType) | A17C1/C5 |
| `temperature` | int (SIGNED) | -40..+80°C typical | 8-bit signed (cmp 0x80) | All |
| `battery_soc` | int | 0-100 (%) | Dynamic from device | All |
| `max_load` | int | min_load..legal_limit, step | Dynamic from `get_power_limit` | A17C1 |
| `power_limit` | int | From `power_limit_option` list | Dynamic from `get_power_limit` | A17C1 |
| `pv_power_limit` | int | From `pv_power_limit_option` | Dynamic from `get_device_attrs` | A17C1 |
| `feed-in_power_limit` | int | 0..legal_limit | Dynamic (HYPHEN in name!) | A17C1 |
| `output_cutoff_data` | int | 5, 10 (%) | Fixed options | A17C1, A17C0 |
| `maximumCurrentLimit` | int | 6-32+ (A, model-dependent) | Dynamic from device capability | A5190 |
| `lightBrightness` | int | 0-100 (%) | Fixed range | A5190 |
| `controlType` | int | 1=Start, 2=Stop, 3=SkipDelay, 4=Boost | Fixed (ChargeControlType) | A5190 |
| `carChargerLockStatus` | int | 2=off, 4=on (bit-shifted) | Fixed | A5190 |
| `port_saving_mode` | int | 1=normal, 2=smart, 4=custom | Fixed (DeviceSavingModeEnum) | A1790 |
| `device_timeout_minutes` | int | 0,30,60,120,240,360,720,1440 | Fixed option set | PPS |
| `display_timeout_seconds` | int | 20,30,60,300,1800 | Fixed option set | PPS |
| `dc_output_timeout_seconds` | int | 0-86400, step 300 | Range + step | PPS |
| `voltage` | float | ×0.1 (reads as int, multiply) | Measurement | A17X8 |
| `current` | float | ×0.01 | Measurement | A17X8 |
| `power` | float | ×0.1 | Measurement | A17X8 |
| `photovoltaic_power` | int | ÷10 from raw | Measurement | A17C1 |
| `bat_charge_power` | int | ÷100 from raw | Measurement | A17C1 |
| `pv_yield` | int | ×0.0001 (upstream) | Cumulative energy | A17C1 |

### Error Codes
**Simple integers**, not bitmasks or lists. Companion tags carry UTF-8 error message strings.
Example: tag 0xA2 = error code (int), tag 0xA4 = error message (Utf8 string).

---

# Device → Command Matrix (from upstream SOLIXMQTTMAP)

> Which device supports which SET commands. Extracted from thomluther's `mqttmap.py`.
> Opcode groups (0101, 0102, etc.) are Gen2-specific compound commands.

### Solarbank Family
| Command | A17C0 | A17C1 | A17C2 | A17C3 | A17C5 | AE100 |
|---------|-------|-------|-------|-------|-------|-------|
| TEMP_UNIT (0050) | x | x | x | x | x | — |
| STATUS_REQUEST (0040) | x | — | — | — | — | — |
| REALTIME_TRIGGER (0057) | x | x | x | x | x | x |
| SB_STATUS_CHECK (0056) | x | — | — | — | — | — |
| SB_POWER_CUTOFF (0067) | x | x | x | x | — | — |
| SB_MIN_SOC (0067) | — | — | — | — | x | x |
| SB_INVERTER_TYPE (0068) | x | — | — | — | — | — |
| SB_LIGHT (0068) | — | x | x | x | x | — |
| SB_MAX_LOAD (005a) | — | x | x | x | x | — |
| SB_GRID_EXPORT (0080) | — | x | x | x | x | x |
| SB_PV_LIMIT (0080) | — | — | — | — | x | — |
| SB_AC_INPUT (0080) | — | — | x | — | x | — |
| SB_USAGE_MODE (005e) | — | — | — | — | x | — |
| AC_SOCKET (0073) | — | — | — | — | x | — |
| 3RD_PARTY_PV (0085) | — | — | — | — | x | x |
| EV_CHARGER_SW (0084) | — | — | — | — | — | x |
| DEVICE_TIMEOUT (009a) | — | — | — | — | x | — |

### PPS Family (selected models)
| Command | A1726 | A1761 | A1763 | A1780 | A1790 |
|---------|-------|-------|-------|-------|-------|
| REALTIME_TRIGGER (0057) | x | x | x | x | x |
| AC_OUTPUT_SWITCH (004a) | — | x | grp | x | x |
| DC_OUTPUT_SWITCH (004b) | x | x | grp | x | x |
| DEVICE_MAX_LOAD (0044) | — | x | — | — | x |
| DEVICE_TIMEOUT (0045) | — | x | grp | — | x |
| DISPLAY_TIMEOUT (0046) | — | x | grp | — | x |
| DISPLAY_MODE (004c) | — | x | grp | — | x |
| LIGHT_MODE (004f) | x | x | — | — | x |
| TEMP_UNIT (0050) | — | x | — | x | x |
| DISPLAY_SWITCH (0052) | x | x | grp | — | x |
| AC_FAST_CHARGE (005e) | — | x | — | — | — |
| DC_12V_MODE (0076) | — | x | grp | — | x |
| AC_OUTPUT_MODE (0077) | — | x | — | — | x |
| PORT_MEMORY (0079) | — | — | grp | — | x |
| SOC_LIMITS (grp 0103) | — | — | x | — | — |
| AC_CHARGE_LIMIT (grp) | — | — | x | — | — |

`grp` = Gen2 compound command groups (0101-0103 for PPS, 0105-010e for EV)

### Smart Devices
| Command | A17X8 | A2345 | A5191 |
|---------|-------|-------|-------|
| STATUS_REQUEST | 0040 | 0200 | — |
| REALTIME_TRIGGER | 0057 | 020b | 0057 |
| AC_OUTPUT_SWITCH | 007a | — | — |
| PLUG_SCHEDULE | 007c | — | — |
| PLUG_DELAYED_TOGGLE | 007e | — | — |
| TIMER_REQUEST | 007f | — | — |
| USB_PORT_SWITCH | — | 0207 | — |
| EV_CHARGER_MODE | — | — | 0105 (enc=2) |
| EV_SCHEDULE | — | — | 0106 |
| EV_POWER_MODE | — | — | 0108 (enc=2) |
| EV_LOAD_BALANCE | — | — | 010c |
| EV_SOLAR_CHARGE | — | — | 010e |
| EV settings (10 cmds) | — | — | 0100 |

### Minimal-Command Devices (REALTIME_TRIGGER only)
A17E1 (E10), AX170 (Power Dock Hub), A17X7 (Smart Meter), A17B1 (Power Panel),
A5101/02/03 (HES X1), A1782 (F3000), SHEMP3 (Shelly Pro 3EM)

---

# API Response Model Structures (from toJson/fromJson)

> Complete nested structures for key API responses. Extracted from Dart model classes.

## SceneInfo (master site response — `get_site_detail`)

| Field | Type | Description |
|-------|------|-------------|
| `site_info` | object | Site metadata |
| `feature_switch` | FeatureSwitch | 22 capability flags (see below) |
| `solar_list` | list | Per-panel solar data |
| `pps_info` | object | PPS device info |
| `solarbank_info` | object | SolarBank data |
| `smart_plug_info` | object | Smart plug data |
| `grid_info` | object | Grid info + ammeter list |
| `error_info_map` | object | Error info |
| `aiems_profit` | object | AI EMS profit data |
| `combiner_box_info` | object | Combiner box / Power Dock |
| `charging_pile_info` | object | EV charging pile |
| `statistics` | object | Energy statistics |

### FeatureSwitch (22 boolean flags — what a site supports)
| Flag | Description | Flag | Description |
|------|-------------|------|-------------|
| `multi_pv` | Multiple PV arrays | `smart_plug` | Smart plug support |
| `manual_backup_mode` | Manual backup | `exceed_power` | Exceed power alert |
| `peak_valley_mode` | Peak/valley pricing | `heating` | Heating support |
| `shelly_meter` | Shelly meter | `support_p1_meter` | P1 meter |
| `support_0w` | 0W feed-in | `0w_feed_v2` | 0W feed v2 |
| `micro_inverter_power_exceed` | MI power alert | `micro_inverter_output_exceed` | MI output alert |
| `offgrid_with_micro_inverter_alert` | Off-grid MI | `enable_parallel` | Parallel ops |
| `plug_switch_report` | Plug reporting | `show_third_party_pv_panel` | 3rd party PV |
| `meter_self_testing` | Meter test | `power_limit_status` | Power limit active |
| `power_saving_mode` | Power saving | `third_party_pv_enable` | 3rd party PV on |
| `enable_aiems_v2` | AI EMS v2 | `grid_to_ev` | Grid→EV charging |

## SiteConsumptionStrategyModel (param_type=6 response)

| Field | Type | Description |
|-------|------|-------------|
| `mode_type` | int | Mode (1-8) |
| `default_home_load` | int | Default (W) |
| `max_load` | int | Maximum (W) |
| `min_load` | int | Minimum (W) |
| `step` | int | Step (W) |
| `custom_rate_plan` | list | Schedule: `[{index, week:[0-6], ranges:[{start_time, end_time, power, exceed_alarm}]}]` |
| `blend_plan` | list | Blend schedule |
| `ai_ems` | object | `{status: int}` |
| `reserved_soc` | int | Reserved SOC (%) |
| `manual_backup` | object | Backup config |
| `dynamic_price` / `fixed_price` | object | Pricing config |

## StationPowerLimitModel (`get_power_limit` response)

| Field | Type | Description |
|-------|------|-------------|
| `legal_power_limit` | int | Legal max (W) |
| `ac_input_power_unit` | string | Unit ("W") |
| `power_limit_option` | list | Per-device: `[{device_sn, limit, limit_real, ac_input_limit, status}]` |
| `parallel_type` | int | Parallel type |
| `exceed_alarm` | int | Exceed alarm |

## HomeLoadData (`get_device_home_load` response)

| Field | Type | Description |
|-------|------|-------------|
| `min_load` / `max_load` / `step` | int | Range (W) |
| `default_home_load` | int | Default (W) |
| `schedule_mode` | int | Mode |
| `is_charge_priority` | bool | Charge priority |
| `is_show_priority_discharge` | bool | Priority discharge UI |
| `display_advanced_mode` | bool | Advanced mode UI |
| `ranges` | list | See HomeRange below |

### HomeRange (schedule entry)
```json
{"id": 0, "turn_on": true, "start_time": "00:00", "end_time": "08:00",
 "power_setting_mode": 1, "charge_priority": 80,
 "priority_discharge_switch": false,
 "appliance_loads": [{"name": "Fridge", "power": 100, "number": 1, "id": 0}],
 "device_power_loads": [{"device_sn": "...", "power": 50}]}
```

## A5101DeviceCommandModel (HES `sendDeviceCommand`)

17+ fields with 8 nested sub-models:

### electricity_strategy
```json
{"conserve_percent": 10, "mode": 1, "grid_recharging": true,
 "peck_shaving": false, "peck_shaving_max_power": 5000,
 "disaster_preparedness_enable": false,
 "disaster_preparedness_plans": [{"soc": 100, "start_time": "...", "end_time": "...", "type": 2}],
 "auto_disaster_preparedness_enable": false}
```

### off_grid_switching
```json
{"off_grid_enable": false, "off_grid_sensitivity": 50}
```

### heat_pump_setting
```json
{"heat_pump_state": 0, "heat_pump_power": 2000, "heat_pump_mode": 1,
 "heat_pump_manual_enable": false, "heat_pump_min_launch_time": 30,
 "heat_pump_min_running_time": 10,
 "heat_pump_plan": [{"day_type": 1, "start_time": "06:00", "end_time": "22:00"}]}
```

### advanced_setting
```json
{"arc_fault_circuit_interrupter": false, "rapid_shutdown": false,
 "mppt_multi_peak_scanning": {"scanning_switch": false, "scanning_interval": 10}}
```

### screen_setting
```json
{"radar": true, "screen": true, "screen_timeout": 60}
```

### utility_rate_plan (seasons + pricing)
```json
{"peak_sessions": [{"id": 1, "name": "Summer", "start_time": "06-01", "end_time": "09-30",
  "peak_valley_prices": [{"buy": 0.30, "sell": 0.08, "energy_unit": "€",
    "start_time_period": "06:00", "end_time_period": "22:00", "peak_type": 1, "day_type": 1}]}],
 "nem_plan_info": {"template_id": "...", "template_name": "...", "customer_segment_type": "..."}}
```

## A5101 BLE Data Codes — GET vs SET

131 total DataCodeType enum values. Selected important ones by direction:

### SET-only (writable)
| Hex | Name | Description |
|-----|------|-------------|
| 0x02BE-0x02D1 | `diesel*` (14 codes) | All generator params |
| 0x09C9 | `gridSensitivity` | Grid sensitivity value |
| 0x09D4 | `softwarePowerExportLimitInput` | Export limit value |
| 0x09D3 | `x1AllowCharge` | X1 charge permission |
| 0x0284 | `clsStateReset` | CLS reset |

### GET-only (readable)
| Hex | Name | Description |
|-----|------|-------------|
| 0x014C | `pvState` | PV connection |
| 0x014D | `batRemain` | Battery remaining |
| 0x0155 | `supportFunction` | Capability flags |
| 0x0160 | `minSoc` | Minimum SOC |
| 0xE004 | `systemStatus` | System status |

### Both GET and SET
| Hex | Name | Hex | Name |
|-----|------|-----|------|
| 0xF009 | `gridStandardCode` | 0x0137 | `backupMode` |
| 0x0222 | `pvLoadPower` | 0x020E | `batteryLoadPower` |
| 0xF00C | `gridBatteryPower` | 0x0221 | `gridLoadPower` |

~60 codes in enum but NOT in either BLE map — used via MQTT:
`soc`(0x3a), `workMode`(0x46), `batteryReserve`(0x21), `peakShaving`(0x24),
`heatPumpSGEnable`(0x57), `evChargerAllPower`(0x85), `autoDisaster`(0x44)

---

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

## A17X7 / A17X7US — Smart Meter 0405 Status Tags (P1)

> **Not in upstream** — NO `_A17X7_0405` exists in mqttmap.py. ALL tags are new.
> A17X7US delegates entirely to A17X7.

### parseDeviceAllInfo
| Tag | Field | Conversion | Debug String | Inferred Name |
|-----|-------|-----------|-------------|---------------|
| fe | field_6f | int | "a17x7_updateTime_" | `msg_timestamp` |
| a2 | field_6b | Utf8 string | — | `device_sn` |
| a3 | field_187 | bool (==1) | "17X7是否在升级中" | `ota_in_progress` |
| a5 | field_3db | int | — | `grid_power` |
| a6 | field_7b | getMainVersionWithHex | "总包版本号" | `sw_version` |
| a7 | field_2d7 | int | — | `sw_controller` |
| a8 | field_477 | int | "fromGrid" | `grid_to_home_power` (upstream-confirmed) |
| a9 | field_47b | int | "toGrid" | `pv_to_grid_power` (upstream-confirmed) |
| aa | field_47f | int | "fromGridSum" | `grid_import_energy` (upstream FACTOR: 0.01) |
| ab | field_483 | int | "toGridSum" | `grid_export_energy` (upstream FACTOR: 0.01) |
| ac | field_477 | int | — | APK alternate path for same field as a8 (NOT in upstream) |
| ad | field_47b | int | — | APK alternate path for same field as a9 (upstream: commented out) |
| fd | field_473 | bool (presence) | "showTwoDecimal" | `show_two_decimal` |

### parseWorkInfo (real-time data — shares offsets with A17C0/A17C1)
| Tag | Field | Inferred Name | Tag | Field | Inferred Name |
|-----|-------|---------------|-----|-------|---------------|
| a2 | 0x18b | grid_power_rt | a3 | 0x317+3d3 | soc (dual store) |
| a4 | 0x30f | status_code | a5 | 0x3db | total_power |
| a6 | 0x2f3 | version_raw | a7 | 0x2d7 | controller_ver |
| a8 | 0x2eb | hw_version | a9 | 0x3b7 | temp_unit |
| aa | 0x307 | temperature | ab | 0x20b | pv_power (÷10?) |
| ac | 0x237 | output_power | ae | 0x3df | load_schedule |
| b0 | 0x243 | charge_power | b1-b3 | 0x24b-253 | energy fields |
| b4 | 0x25b | cutoff_data | b7 | — | — |
| b8-bc | 0x25f-26f | extended fields | fb-fc | 0x287/283 | status flags |

---

## A1771 / A1753 / A1781 — C800/C1000/F2600 0405 Status Tags (P3)

> A1753 extends A1771. A1781/A1780P also extend A1771 chain.

### A1771 parseDeviceAllInfo (base for C1000/C800/F2600)
| Tag | Field | Conversion | Debug | Inferred Name | Status |
|-----|-------|-----------|-------|---------------|--------|
| fe | 0x6f | int | — | `msg_timestamp` | — |
| d0 | 0x6b | Utf8 | "更新设备sn" | `device_sn` | — |
| d1 | 0x2ff | int | — | `max_load` | — |
| d2 | 0x1b3 | int | — | `device_timeout` | — |
| d3 | 0x1bb | int | — | `display_timeout` | — |
| d7 | 0x39b | bool (==1) | — | `ac_output_switch` | — |
| d8 | 0x39f | bool (==1) | — | `dc_output_switch` | — |
| d9 | 0x3a3 | int | — | `display_mode` | — |
| db | 0x3af | bool (==1) | — | `energy_saving_mode` | — |
| dc | 0x3b3 | int | — | `light_mode` | — |
| dd | 0x3b7 | int | — | `temp_unit_fahrenheit` | — |
| de | 0x3a7 | bool (==1) | — | `display_switch` | — |
| df | 0x3c3 | int | "[绿电模式]" | `green_energy_mode` | **NEW** |
| e0 | 0x3c7 | int | "[绿电充电功率上限]" | `green_charge_power_limit` | **NEW** |
| e2 | 0x3cf | list | "[是否启用波峰波谷]" | `peak_valley_enabled` | **NEW** |
| e3 | 0x187 | bool (==1) | — | `unknown_flag` | **NEW** |
| e4 | 0x3e3 | int | "[波峰波谷数据]" | `peak_valley_data` | **NEW** |

### A1753 extra tags (added on top of A1771)
| Tag | Field | Conversion | Inferred Name | Status |
|-----|-------|-----------|---------------|--------|
| e5 | 0x3f3 | bool (==1) | `backup_charge_switch` | **NEW** |
| f8 | 0x197+19b | DeviceSavingModeEnum | `port_saving_mode` (1=normal,2=smart,4=custom) | **NEW** |
| f9 | 0x42b | int | `saving_mode_ext` | **NEW** |

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
| ab | "总输出功率（单位W" | `total_output_power` | W (note: APK is missing closing `）` — Anker typo) |
| c2 | "总输入功率 设备主页totalInput" | `total_input_power` | W |
| ae | "并网口功率（单位W）" | `grid_connected_port_power` | W, `hexStringToDouble` conversion, offset 0x21b |
| af | "离网口功率（单位W）" | `off_grid_port_power` | W, `hexStringToDouble` conversion, offset 0x21f |
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

### A17D0 — Generator Input Adapter
Found in A17B1 parser (line 3663). Referenced 4× alongside A1790/A1790P.
This is the [Anker SOLIX Generator Input Adapter](https://support.ankersolix.com/s/article/Anker-SOLIX-Generator-Input-Adapter-User-Guide-A17D0)
(A17D0111, $399) — connects gas generators to F3800 Plus / Home Power Panel.
Shipping product, not unreleased.

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
| ae | field_433 | bool (`cmp #1 → csel`) | `ac_output_power_signed?` | Upstream (commented) says ac_output_power, NOT ac_socket_switch |
| af | field_187 | bool (`cmp #1 → csel`) | `schedule_enabled` | Same offset as A17X8 a3 (field_187 = schedule flag cross-device) |
| b8 | field_47f | int, unsigned, default=0 | `ac_input_power` | Same offset as A17X8 a9 (current ×0.01), raw int here = milliwatts? |
| b9 | field_4cb | bool (`cmp #1`, default=false) | `self_test_enabled` | Defaults false when absent, boolean flag |
| ba | field_26b | int → ÷100.0 (float) | `percentage_value` | APK uses as percentage (÷100). Upstream claims bitmask — may differ by firmware. Read path: `_realUpdateData`, `gotoSiteSettingPricePage` |
| bb | field_26f | int, unsigned | `heating_power` | Same offset as A17C0 bb — upstream comments confirm "bb"=heating |
| c7 | (consumed) | int, NOT stored | `home_load_power_raw` | Value read but consumed by c8 ÷10 chain → `ac_socket_power` |
| e9 | field_2cb | int, unsigned, default=0 | `battery_capacity` | Writes `wzr` (zero register) if absent |
| fb/fc | field_287 | List\<int\> (indexed byte array, NOT bitmask) | `status_byte_array` | See sub-field table below |

#### fb/fc Sub-Field Extraction (traced via READ paths in UI/Controller)

Tags fb and fc write to the same field (0x287). fb is primary, fc overwrites if fb was empty.
The APK does NOT use ARM `and` bitmask instructions — it uses **indexed byte access** (`list[N] == 2`).

| Index | Comparison | Dest Offset | Semantic Name | Evidence (READ path) |
|-------|-----------|-------------|---------------|---------------------|
| [0] | raw value | 0x297 | `power_limit_ref` | Compared in DevicePowerLimit closure; triggers `setDevicePowerLimit()` if changed |
| [2] | `== 2` → bool | 0x49b | `ui_feature_flag` | Conditional UI rendering in a17c1setting_logic |
| [10] | `== 2` → bool | 0x457 | `unknown_bool` | Boolean flag |
| [14] | `== 2` → bool | 0x28b | **`is_enable_0w`** | Debug: "-isEnable0w-". Zero-export enable flag. Checked with `isItalyPowerLimit()` fallback |
| [18] | raw value | 0x28f | **`feeder0w_config`** | Used in `setDevicePowerLimit()` with params "feeder0w" and "switch0w". `cmp #2` check |

> **Key insight**: Dart AOT does not compile bitmask `and` instructions. Sub-fields are stored
> as individual bytes in a List\<int\>, accessed by index. `list[N] == 2` means "feature enabled"
> (value 2 = true in this protocol, NOT value 1).

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

---

# GAP FILL: Final Analysis (2026-03-28)

## Task 1: A1780 (F2000) Positional Parser

The A1780 uses **positional byte parsing** (NOT TLV tags like Solarbanks). The `parseOtherData` function reads sequential 2-byte fields from the data buffer using `sublist(offset, offset+2)` then `listToInt()`. The `r16` register holds the **start offset** into the data buffer, and `r2` holds the **end offset** (start + field_width). The `r17` register holds the **object field offset** where the result is stored.

The A1780 `parseCountdownData` is inherited from A1770 (`A1770Commands::parseCountdownData`).

### parseOtherData: Positional Byte Map

The function parses the data buffer sequentially. `r16` = buffer read position, `r2` = bytes to read (field width=2 for most, then varying), `r17` = object store offset.

| Pos (r16) | End (r2) | Obj Offset (r17) | Upstream Tag | Field Name | Conversion |
|-----------|----------|-------------------|--------------|------------|------------|
| 26 | 9 | 0x1AB (427) | `a4` | remaining_time_hours | listToInt(), x0.1 |
| 34 | 13 | 0x1AF (431) | `a5` | grid_to_battery_power | listToInt() |
| 38 | 17 | 0x1D3 (467) | `a6` | ac_socket_power | listToInt() |
| 42 | 19 | 0x1D7 (471) | `a7` | usbc_1_power | listToInt() |
| 46 | 21 | 0x1DB (475) | `a8` | usbc_2_power | listToInt() |
| 50 | 23 | 0x1DF (479) | `a9` | usbc_3_power | listToInt() |
| 54 | 25 | 0x1E3 (483) | `aa` | usba_1_power | listToInt() |
| 58 | 27 | 0x1E7 (487) | `ab` | usba_2_power | listToInt() |
| 62 | 29 | 0x1EB (491) | `ac` | dc_12v_1_power | listToInt() |
| 66 | 31 | 0x1EF (495) | `ad` | dc_12v_2_power | listToInt() |
| 70 | 33 | 0x1FB (507) | `ae` | dc_input_power | listToInt() |
| 74 | 35 | 0x1FF (511) | `af` | ac_input_power | listToInt() |
| 78 | 37 | 0x203 (515) | `b0` | ac_output_power_total | listToInt() |
| 82 | 39 | 0x20B (523) | -- | (unknown, gap in upstream) | listToInt() |
| 86 | 41 | 0x237 (567) | -- | (unknown, gap in upstream) | listToInt() |
| 90 | 43 | 0x2CF (719) | `b3` | sw_version | toString (special) |
| 94 | 45 | 0x2D3 (723) | `b9` | sw_expansion | listToInt() |
| 98 | 47 | 0x2D7 (727) | `ba` | sw_controller | listToInt() |
| 102 | 49 | 0x2DB (731) | -- | (unknown fw field) | listToInt() |
| 106 | 51 | 0x2DF (735) | -- | (unknown fw field) | listToInt() |
| 110 | 53 | 0x2E3 (739) | -- | (unknown fw field) | listToInt() |
| 114 | 55 | 0x2E7 (743) | -- | (unknown fw field) | listToInt() |
| 118 | 57 | 0x2EB (747) | -- | (unknown fw field) | listToInt() |
| 122 | 59 | 0x2EF (751) | -- | (unknown fw field) | listToInt() |
| 126 | 61 | 0x2F3 (755) | `bd` | temperature | listToInt() -> getMainVersion() |
| 130 | 63 | 0x2FB (763) | -- | temp_unit_bool | listToInt() == 1 -> bool |
| 132 | 65 | 0x303 (771) | `c1` | main_battery_soc | listToInt() |
| 134 | 66 | 0x307 (775) | `bd` | temperature | signed: if >= 0x80, subtract 0x100 |
| 136 | 67 | 0x30B (779) | `be` | exp_1_temperature | signed: if >= 0x80, subtract 0x100 |
| 138 | 68 | 0x30F (783) | -- | (unknown) | listToInt() |
| 140 | 69 | 0x313 (787) | `c2` | exp_1_soc | listToInt() |
| 142 | 70 | 0x317 (791) | -- | (unknown) | listToInt() |
| 144 | 71 | 0x3D3 (979) | `c3` | battery_soh | listToInt() |
| 146 | 72 | 0x31F (799) | `c4` | exp_1_soh | listToInt() |
| 148 | 73 | 0x323 (803) | -- | (unknown) | listToInt() |
| 150 | 74 | 0x327 | `c5` | expansion_packs_b? | listToInt() == 1 -> bool |
| 152 | 75 | 0x32B | `d8` | dc_output_power_switch | listToInt() == 1 -> bool |
| 154 | 76 | 0x32F | `d7` | ac_output_power_switch | listToInt() == 1 -> bool |
| 156 | 77 | 0x333 | `db` | energy_saving_mode | listToInt() == 1 -> bool |
| 158 | 78 | 0x337 | `de` | display_switch | listToInt() == 1 -> bool |
| 160 | 79 | 0x33B | `dd` | temp_unit_fahrenheit | listToInt() == 1 -> bool |
| 162 | 80 | 0x347 | `e5` | backup_charge_switch | listToInt() == 1 -> bool |
| 164 | 81 | -- | -- | (unknown bool) | listToInt() == 1 -> bool |
| 166 | 82 | -- | -- | (unknown bool) | listToInt() == 1 -> bool |
| 168 | 83 | 0x3DB (987) | `d9` | display_mode | listToInt() |
| 170 | 84 | -- | `dc` | light_mode | listToInt() |

### parseSwitchData: Switch Fields

Parses 4 switch/boolean fields from sequential 2-byte positions in the data buffer:

| Position (r16) | Obj Offset | Upstream Tag | Field Name | Conversion |
|----------------|------------|--------------|------------|------------|
| 18 | 0x39B (923) | `d7` | ac_output_power_switch | listToInt() == 1 -> bool |
| 20 | 0x39F (927) | `d8` | dc_output_power_switch | listToInt() == 1 -> bool |
| 22 | 0x3AF (943) | `db` | energy_saving_mode | listToInt() == 1 -> bool |
| 24 | 0x3B3 (947) + cmp >= 4 -> 0x193 (403) | `dc` | light_mode + bool flag | listToInt(): if < 4 -> store raw, cmp == 4 -> bool |

**Note**: The 4th switch entry has dual logic: it stores the raw light_mode value AND compares against 4 (blinking mode) to set a separate boolean flag.

### parseCountdownData (inherited from A1770)

The countdown parser reads 4 elements from positions 18, 20, 22, 24 into a 4-element list, then calls `listToInt()` on the combined 4 bytes to produce a single countdown value stored at object offset 0x1AB (427). Then it reads another pair of values from positions 26, 28 and 30 to produce more countdown fields.

Format: 4 bytes assembled into a 32-bit value representing countdown time.

| Position (r16) | Field | Description |
|----------------|-------|-------------|
| 18-24 | countdown_value_packed | 4 bytes -> combined listToInt at obj offset 427 |
| 26-28 | countdown_hours | Additional countdown hours |
| 30 | countdown_minutes? | Additional field |

### parseDeviceInfo

This is a **wrapper** that first calls `parseOtherData()`, then reads additional fields starting from the position where parseOtherData left off. The additional fields in parseDeviceInfo (after parseOtherData returns) include:

| Continuation | Obj Offset (r17) | Upstream Tag | Field Name |
|-------------|-------------------|--------------|------------|
| +0 (from return) | 0x2FF (767) | `c0` | expansion_packs_a? |
| +2 | 0x1B3 (435) | -- | additional power/status |
| +4 | 0x1BB (443) | -- | additional power/status |
| +6 | 0x1BF (447) | -- | additional power/status |
| +8 | 0x1C3 (451) | -- | additional power/status |
| +10 | 0x1C7 (455) | -- | additional power/status |
| +12 | 0x1CB (459) | -- | additional power/status |
| +14 | 0x1CF (463) | -- | additional power/status |
| ... | ... | ... | ... continues with more fields |

**Key insight**: The A1780 positional parser makes TLV tags unnecessary for BLE -- the byte offsets ARE the implicit tags. Upstream mqttmap.py maps these same fields to explicit TLV tags (a4-fe) for the MQTT path. The BLE positional format and the MQTT TLV format carry identical data, just encoded differently.

---

## Task 2: All Upstream SET Commands (from mqttcmdmap.py)

### Group 1: PPS AC/DC Controls

#### CMD_AC_CHARGE_SWITCH
**Command**: `ac_charge_switch` | **Devices**: A1780, A1790, A5140, A5143
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_ac_charge_switch | ui (1B) | off=0, on=1 |
| `fe` | msg_timestamp | var (4B) | (auto) |
**STATE_NAME**: `backup_charge_switch`

#### CMD_AC_FAST_CHARGE_SWITCH
**Command**: `ac_fast_charge_switch` | **Devices**: A1780
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_ac_fast_charge_switch | ui (1B) | off=0, on=1 |
| `fe` | msg_timestamp | var (4B) | (auto) |
**STATE_NAME**: `fast_charge_switch`

#### CMD_AC_CHARGE_LIMIT
**Command**: `ac_charge_limit` | **Devices**: A5140, A5143
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_ac_input_limit | sile (2B) | (device-specific watt value) |
| `fe` | msg_timestamp | var (4B) | (auto) |
**STATE_NAME**: `ac_input_limit`

#### CMD_AC_OUTPUT_SWITCH
**Command**: `ac_output_switch` | **Devices**: A1780, A5140, A5143, A17X8
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_ac_output_switch | ui (1B) | off=0, on=1 |
| `fe` | msg_timestamp | var (4B) | (auto) |
**STATE_NAME**: `ac_output_power_switch`

#### CMD_AC_OUTPUT_MODE
**Command**: `ac_output_mode_select` | **Devices**: A1780, A5140, A5143
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_ac_output_mode | ui (1B) | smart=0, normal=1 |
| `fe` | msg_timestamp | var (4B) | (auto) |
**STATE_NAME**: `ac_output_mode` (with converter: setting 0 -> state 2, setting 1 -> state 1)

#### CMD_AC_OUTPUT_TIMEOUT_SEC
**Command**: `ac_output_timeout_seconds` | **Devices**: A5140, A5143
| Tag | NAME | TYPE | Range |
|-----|------|------|-------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_ac_output_timeout_seconds | var (3B) | 0-86400, step 300 |
| `fe` | msg_timestamp | var (4B) | (auto) |
**STATE_NAME**: `ac_output_timeout_seconds`

#### CMD_DC_OUTPUT_SWITCH
**Command**: `dc_output_switch` | **Devices**: A1780, A5140, A5143
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_dc_output_switch | ui (1B) | off=0, on=1 |
| `fe` | msg_timestamp | var (4B) | (auto) |
**STATE_NAME**: `dc_output_power_switch`

#### CMD_DC_12V_OUTPUT_MODE
**Command**: `dc_12v_output_mode_select` | **Devices**: A1780, A5140, A5143
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_dc_12v_output_mode | ui (1B) | smart=0, normal=1 |
| `fe` | msg_timestamp | var (4B) | (auto) |
**STATE_NAME**: `dc_12v_output_mode` (with converter: setting 0 -> state 2, setting 1 -> state 1)

#### CMD_DC_OUTPUT_TIMEOUT_SEC
**Command**: `dc_output_timeout_seconds` | **Devices**: A5140, A5143
| Tag | NAME | TYPE | Range |
|-----|------|------|-------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_dc_output_timeout_seconds | var (3B) | 0-86400, step 300 |
| `fe` | msg_timestamp | var (4B) | (auto) |
**STATE_NAME**: `dc_output_timeout_seconds`

### Group 2: PPS Display/Light/Port Controls

#### CMD_LIGHT_SWITCH
**Command**: `light_switch` | **Devices**: A1780, A5140, A5143
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_light_switch | ui (1B) | off=0, on=1 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_LIGHT_MODE
**Command**: `light_mode_select` | **Devices**: A1780, A5140, A5143
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_light_mode | ui (1B) | off=0, low=1, medium=2, high=3, blinking=4 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_DISPLAY_SWITCH
**Command**: `display_switch` | **Devices**: A1780, A5140, A5143 (and all PPS)
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_display_switch | ui (1B) | off=0, on=1 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_DISPLAY_MODE
**Command**: `display_mode_select` | **Devices**: A1780, A5140, A5143
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_display_mode | ui (1B) | off=0, low=1, medium=2, high=3 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_DISPLAY_TIMEOUT_SEC
**Command**: `display_timeout_seconds` | **Devices**: A1780, A5140, A5143
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_display_timeout_sec | sile (2B) | [20, 30, 60, 300, 1800] |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_PORT_MEMORY_SWITCH
**Command**: `port_memory_switch` | **Devices**: A5140, A5143
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_port_memory_switch | ui (1B) | off=0, on=1 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_USB_PORT_SWITCH
**Command**: `usbc_1/2/3/4_port_switch`, `usba_port_switch` | **Devices**: A5140, A5143
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_port_switch_select | ui (1B) | usbc_1=0, usbc_2=1, usbc_3=2, usbc_4=3, usba=4 |
| `a3` | set_port_switch | ui (1B) | off=0, on=1 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_SOC_LIMITS_V2
**Command**: `soc_limits` | **Devices**: A5140, A5143 (uses CMD_COMMON_V2 with `fd` timestamp)
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `aa` | set_max_soc | ui (1B) | [80, 85, 90, 95, 100] |
| `ab` | set_min_soc | ui (1B) | [1, 5, 10, 15, 20] |
| `fd` | msg_timestamp | str | (milliseconds) |

### Group 3: Solarbank Extras

#### CMD_SB_STATUS_CHECK
**Command**: `sb_status_check` | **Devices**: A17C0 (Solarbank 1)
| Tag | NAME | TYPE | Notes |
|-----|------|------|-------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | device_sn | str (16B) | Device serial |
| `a3` | charging_status | ui (1B) | Current status |
| `a4` | set_output_preset | var | Output W |
| `a5` | status_timeout_sec? | var | Timeout |
| `a6` | local_timestamp | var | Time sync |
| `a7` | next_status_timestamp | var | +56-57s |
| `a8` | status_check_unknown_1? | ui | Unknown |
| `a9` | status_check_unknown_2? | ui | Unknown |
| `aa` | status_check_unknown_3? | ui | Unknown |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_SB_POWER_CUTOFF
**Command**: `sb_power_cutoff_select` | **Devices**: A17C0-C3 (SB1, SB2)
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_output_cutoff_data | ui (1B) | [5, 10] |
| `a3` | set_lowpower_input_data | ui (1B) | follows a2: {5:4, 10:5} |
| `a4` | set_input_cutoff_data | ui (1B) | follows a2: {5:5, 10:10} |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_SB_MIN_SOC
**Command**: `sb_min_soc_select` | **Devices**: A17C5, A17C6 (SB3)
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_min_soc | ui (1B) | [5, 10] |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_SB_INVERTER_TYPE
**Command**: `sb_inverter_type_select` | **Devices**: A17C0 (SB1)
| Tag | NAME | TYPE | Notes |
|-----|------|------|-------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_output_cutoff_data | ui | inherited from CMD_SB_POWER_CUTOFF |
| `a3` | set_lowpower_input_data | ui | inherited |
| `a4` | set_input_cutoff_data | ui | inherited |
| `a5` | set_inverter_brand | bin | Hex bytes of brand |
| `a6` | set_inverter_model | bin | Hex bytes of model |
| `a7` | set_min_load | sile (2B) | Watts |
| `a8` | set_max_load | sile (2B) | Watts |
| `a9` | set_inverter_unknown_1? | ui | Usually 0 |
| `aa` | set_ch_1_min_what? | var | 500 etc |
| `ab` | set_ch_1_max_what? | var | 10000 etc |
| `ac` | set_ch_2_min_what? | var | 500 etc |
| `ad` | set_ch_2_max_what? | var | 10000 etc |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_SB_AC_SOCKET_SWITCH
**Command**: `sb_ac_socket_switch` | **Devices**: A17C5 (SB3)
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_ac_socket_switch | ui (1B) | off=0, on=1 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_SB_3RD_PARTY_PV_SWITCH
**Command**: `sb_3rd_party_pv_switch` | **Devices**: A17C5, A17C6 (cloud-driven)
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_3rd_party_pv_switch | ui (1B) | off=0, on=1 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_SB_EV_CHARGER_SWITCH
**Command**: `sb_ev_charger_switch` | **Devices**: A17C6 (cloud-driven)
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_ev_charger_switch | ui (1B) | off=0, on=1 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_SB_MAX_LOAD
**Command**: `sb_max_load` | **Devices**: A17C1-C6 (all SB2/SB3)
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_max_load | sile (2B) | device-specific: [350,600,800,1000] or [350,600,800,1000,1200] |
| `a3` | set_max_load_type | sile (2B) | individual=0, parallel=2, single=3 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_SB_MAX_LOAD (parallel variant, opcode 005a)
**Command**: `sb_max_load_parallel` | **Devices**: A17C1-C6
Same structure as CMD_SB_MAX_LOAD but with `VALUE_OPTIONS: [1200, 2400, 3600, 4800]` and `a3` default=2 (parallel).

#### CMD_SB_DISABLE_GRID_EXPORT_SWITCH
**Command**: `sb_disable_grid_export_switch` | **Devices**: A17C1-C6
| Tag | NAME | TYPE | VALUE_OPTIONS / Range |
|-----|------|------|----------------------|
| `a1` | pattern_22 | auto | (header) |
| `a5` | set_disable_grid_export_a5? | sile (2B) | default=0 |
| `a6` | set_disable_grid_export_switch | sile (2B) | off=0, on=1 |
| `a9` | set_grid_export_limit | sile (2B) | 0-100000, step 100 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_SB_PV_LIMIT
**Command**: `sb_pv_limit_select` | **Devices**: A17C5 (SB3, in 0080 group)
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a7` | set_sb_pv_limit_select | sile (2B) | [2000, 3600] |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_SB_AC_INPUT_LIMIT
**Command**: `sb_ac_input_limit` | **Devices**: A17C2, A17C5 (in 0080 group)
| Tag | NAME | TYPE | Range |
|-----|------|------|-------|
| `a1` | pattern_22 | auto | (header) |
| `a8` | set_ac_input_limit | sile (2B) | 0-1200 W, step 100 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_SB_LIGHT_SWITCH
**Command**: `sb_light_switch` | **Devices**: A17C1-C6 (in 0068 group)
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_light_mode | ui (1B) | uses actual light_mode state |
| `a3` | set_light_off_switch | ui (1B) | off=0 (light on), on=1 (light off) |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_SB_LIGHT_MODE
**Command**: `sb_light_mode_select` | **Devices**: A17C1-C6 (in 0068 group)
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_light_mode | ui (1B) | normal=0, mood=1 |
| `a3` | set_light_off_switch | ui (1B) | uses actual light_off_switch state |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_SB_DEVICE_TIMEOUT
**Command**: `sb_device_timeout` | **Devices**: A17C5 (opcode 009a)
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_device_timeout_min | ui (1B) | [0,30,60,120,240,360,720,1440] (VALUE_DIVIDER=30) |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_SB_USAGE_MODE
**Command**: `sb_usage_mode` | **Devices**: A17C5 (opcode 005e, cloud-driven, NOT supported directly)
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_usage_mode | ui (1B) | manual=1, smartmeter=2, smartplugs=3, backup=4, use_time=5, smart=7, time_slot=8 |
| `a3` | set_timestamp_a3_or_0? | ui | Unknown |
| `a4` | set_backup_charge_switch | ui (1B) | off=0, on=1 |
| `a5` | set_dynamic_soc_limit | ui (1B) | 10-100%, default=0 |
| `a6` | set_timestamp_backup_start | var | Timestamp |
| `a6_mode_8` | set_time_slot_modes | bin | 48 x 1-byte slots: discharge=1, charge=4, default=6 |
| `a7` | set_timestamp_backup_end | var | Timestamp |
| `fe` | msg_timestamp | var (4B) | (auto) |

### Group 4: Smartplug Controls

#### CMD_PLUG_SCHEDULE
**Command**: `plug_schedule` | **Devices**: A17X8
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_plug_schedule_a2? | ui (1B) | default=1 |
| `a3` | set_plug_schedule_order? | ui (1B) | 1-10 |
| `a4` | set_plug_schedule_a4? | ui (1B) | default=1 |
| `a5` | set_plug_schedule_time | sile (2B) | 0-5947 (hour*256+minute) |
| `a6` | set_plug_schedule_switch | ui (1B) | off=0, on=1 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_PLUG_DELAYED_TOGGLE
**Command**: `plug_delayed_toggle` | **Devices**: A17X8
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_toggle_to_switch? | ui (1B) | off=0, on=1 |
| `a3` | set_toggle_to_delay_time | bin/var (3B) | sec:min:hour, 0-1522491 |
| `a4` | set_toggle_back_switch? | ui (1B) | off=0, on=1 |
| `a5` | set_toggle_back_delay_time | bin/var (3B) | sec:min:hour, 0-1522491 |
| `fe` | msg_timestamp | var (4B) | (auto) |

### Group 5: EV Charger Controls

#### CMD_EV_CHARGER_MODE
**Command**: `ev_charger_mode_select` | **Devices**: A17B1 (EV Charger)
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_ev_charger_mode | ui (1B) | start_charge=1, stop_charge=2, skip_delay=3, boost_charge=4 |
| `fe` | msg_timestamp | var (4B) | (auto) |
**COMMAND_ENCODING**: 2

#### CMD_DEVICE_POWER_MODE
**Command**: `device_power_mode` | **Devices**: A17B1 (EV Charger)
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_device_power_mode | ui (1B) | restart=5 |
| `fe` | msg_timestamp | var (4B) | (auto) |
**COMMAND_ENCODING**: 2

#### CMD_PLUG_LOCK_SWITCH
**Command**: `plug_lock_switch` | **Devices**: A17B1
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a3` | set_plug_lock_switch | ui (1B) | off=1, on=2 (!) |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_EV_AUTO_START_SWITCH
**Command**: `ev_auto_start_switch` | **Devices**: A17B1
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a4` | set_auto_start_switch | ui (1B) | off=0, on=1 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_EV_MAX_CHARGE_CURRENT
**Command**: `ev_max_charge_current` | **Devices**: A17B1
| Tag | NAME | TYPE | Range |
|-----|------|------|-------|
| `a1` | pattern_22 | auto | (header) |
| `a8` | set_max_evcharge_current | sile (2B) | 6-32 A, step 1 (VALUE_DIVIDER=0.1) |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_EV_LIGHT_BRIGHTNESS
**Command**: `light_brightness` | **Devices**: A17B1
| Tag | NAME | TYPE | Range |
|-----|------|------|-------|
| `a1` | pattern_22 | auto | (header) |
| `aa` | set_light_brightness | ui (1B) | 0-100%, step 10 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_EV_LIGHT_OFF_SCHEDULE
**Command**: `light_off_schedule` | **Devices**: A17B1
| Tag | NAME | TYPE | VALUE_OPTIONS / Range |
|-----|------|------|----------------------|
| `a1` | pattern_22 | auto | (header) |
| `b4` | set_light_off_schedule_switch | ui (1B) | off=0, on=1 |
| `b5` | set_light_off_start_time | sile (2B) | 0-5947 (hour*256+minute) |
| `b6` | set_light_off_end_time | sile (2B) | 0-5947 (hour*256+minute) |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_EV_AUTO_CHARGE_RESTART_SWITCH
**Command**: `ev_auto_charge_restart_switch` | **Devices**: A17B1
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `ac` | set_auto_charge_restart_switch | ui (1B) | off=0, on=1 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_EV_CHARGE_RANDOM_DELAY_SWITCH
**Command**: `ev_random_delay_switch` | **Devices**: A17B1
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `ad` | set_random_delay_switch | ui (1B) | off=0, on=1 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_SWIPE_UP_MODE
**Command**: `swipe_up_mode_select` | **Devices**: A17B1
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `af` | set_wipe_up_mode_select | ui (1B) | off=0, start_charge=1, stop_charge=2, boost_charge=3 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_SWIPE_DOWN_MODE
**Command**: `swipe_down_mode_select` | **Devices**: A17B1
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `b0` | set_wipe_down_mode_select | ui (1B) | off=0, start_charge=1, stop_charge=2, boost_charge=3 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_SMART_TOUCH_MODE
**Command**: `smart_touch_mode_select` | **Devices**: A17B1
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `b2` | set_smart_touch_mode_select | ui (1B) | simple=0, anti_mistouch=1 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_MODBUS_SWITCH
**Command**: `modbus_switch` | **Devices**: A17B1
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `b7` | set_modbus_switch | ui (1B) | off=0, on=1 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_MAIN_BREAKER_LIMIT
**Command**: `main_breaker_limit` | **Devices**: A17B1
| Tag | NAME | TYPE | Range |
|-----|------|------|-------|
| `a1` | pattern_22 | auto | (header) |
| `a3` | set_main_breaker_limit | sile (2B) | 10-500 A, step 1 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_EV_LOAD_BALANCING
**Command**: `ev_load_balancing` | **Devices**: A17B1
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_load_balance_switch | ui (1B) | off=0, on=1 |
| `a4` | set_load_balance_setting_d5 | ui (1B) | off=0, on=1 |
| `a5` | set_load_balance_setting_d6 | ui (1B) | off=0, on=1 |
| `a6` | set_load_balance_monitor_device | str (16B) | Device SN |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_EV_SOLAR_CHARGING
**Command**: `ev_solar_charging` | **Devices**: A17B1
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_solar_evcharge_switch | ui (1B) | off=0, on=1 |
| `a3` | set_solar_evcharge_mode | ui (1B) | solar_grid=0, solar_only=1 |
| `a4` | set_solar_evcharge_min_current | sile (2B) | 6-32 A, step 1 |
| `a5` | set_phase_operating_mode? | ui (1B) | one_phase=1, three_phase=3 |
| `a6` | set_solar_evcharge_monitoring_mode | ui (1B) | off=0, on=1 |
| `a7` | set_auto_phase_switch | ui (1B) | off=0, on=1 |
| `a8` | set_solar_evcharge_monitor_device | str (16B) | Device SN |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_EV_CHARGER_SCHEDULE_SETTINGS
**Command**: `ev_charger_schedule_settings` | **Devices**: A17B1
| Tag | NAME | TYPE | VALUE_OPTIONS |
|-----|------|------|---------------|
| `a1` | pattern_22 | auto | (header) |
| `a2` | set_schedule_switch | ui (1B) | off=2(!), on=1 |
| `a8` | schedule_mode | ui (1B) | normal=0, smart=1 |
| `fe` | msg_timestamp | var (4B) | (auto) |

#### CMD_EV_CHARGER_SCHEDULE_TIMES
**Command**: `ev_charger_schedule_times` | **Devices**: A17B1
| Tag | NAME | TYPE | Range |
|-----|------|------|-------|
| `a1` | pattern_22 | auto | (header) |
| `a3` | set_week_start_time | sile (2B) | 0-5947 (hour*256+minute) |
| `a4` | set_week_end_time | sile (2B) | 0-5947 |
| `a5` | set_weekend_start_time | sile (2B) | 0-5947 |
| `a6` | set_weekend_end_time | sile (2B) | 0-5947 |
| `a7` | set_weekend_mode | ui (1B) | same=1, different=2 |
| `fe` | msg_timestamp | var (4B) | (auto) |

### Group 6: Common Controls (already mapped but listed for completeness)

These are already in BLE_COMMAND_MAP or are trivial request-only commands:
- **CMD_STATUS_REQUEST** (`status_request`): a1 + fe only
- **CMD_REALTIME_TRIGGER** (`realtime_trigger`): a2=enable(0/1), a3=timeout_sec(60-600)
- **CMD_TIMER_REQUEST** (`timer_request`): a1 + fe only
- **CMD_TEMP_UNIT** (`temp_unit_switch`): a2=celsius(0)/fahrenheit(1)
- **CMD_DEVICE_MAX_LOAD** (`device_max_load`): a2=watts (sile)
- **CMD_DEVICE_TIMEOUT_MIN** (`device_timeout_minutes`): a2=[0,30,60,120,240,360,720,1440]

---

## Task 3: A17C5 (Solarbank 3) vs A17C1 (Solarbank 2) Tag Differences

The A17C5 class **extends** A17C1DeviceCommands, so it inherits all A17C1 tags and adds extras.

### Method: Comparing indexString() calls (TLV tag lookups)

Each `indexString(N)` call extracts tag 0xN from the TLV data. By comparing the decimal values used in both files:

#### Tags present in BOTH A17C1 and A17C5 (shared, from A17C1 parseDeviceAllInfo)
| Decimal | Hex Tag | Upstream Field |
|---------|---------|----------------|
| 254 | 0xFE | msg_timestamp |
| 162 | 0xA2 | device_sn |
| 163 | 0xA3 | main_battery_soc |
| 164 | 0xA4 | (varies) |
| 165 | 0xA5 | error_code / temperature |
| 166 | 0xA6 | sw_version / battery_soc |
| 167 | 0xA7 | sw_controller? / sw_version |
| 168 | 0xA8 | sw_expansion / sw_controller? |
| 169 | 0xA9 | temp_unit / sw_expansion |
| 173 | 0xAD | (power field) |
| 174 | 0xAE | (power field) |
| 175 | 0xAF | (power field) |
| 176 | 0xB0 | bat_charge_power / pv_yield |
| 177 | 0xB1 | pv_yield / charged_energy |
| 178 | 0xB2 | charged_energy / discharged_energy |
| 179 | 0xB3 | output_energy |
| 180 | 0xB4 | output_cutoff_data / consumed_energy |
| 181 | 0xB5 | lowpower_input_data / min_soc |
| 182 | 0xB6 | input_cutoff_data / min_soc_exp_1? |
| 183 | 0xB7 | bat_discharge_power / min_soc_exp_2? |
| 184 | 0xB8 | (field) |
| 185 | 0xB9 | (field) |
| 186 | 0xBA | (bitmask: light/socket/temp) |
| 187 | 0xBB | heating_power |
| 189 | 0xBD | (power/soc field) |
| 190 | 0xBE | (energy/max_load) |
| 191 | 0xBF | timestamp_backup_start |
| 192 | 0xC0 | timestamp_backup_end |
| 193 | 0xC1 | (field) |
| 194 | 0xC2 | max_load / photovoltaic_power? |
| 198 | 0xC6 | usage_mode / pv_1_power |
| 199 | 0xC7 | home_load_preset / pv_2_power |
| 200 | 0xC8 | ac_socket_power / pv_3_power |
| 201 | 0xC9 | consumed_energy / pv_4_power |
| 251 | 0xFB | grid_export_disabled bitmask |
| 252 | 0xFC | (unknown) |

#### Tags ONLY in A17C5 (NOT in A17C1)
| Decimal | Hex Tag | Probable Upstream Field | Evidence |
|---------|---------|------------------------|----------|
| **170** | **0xAA** | temperature (signed) | In A17C5 only, not in A17C1's parseDeviceAllInfo |
| **171** | **0xAB** | photovoltaic_power | Matches A17C5_0405["ab"] |
| **172** | **0xAC** | battery_power_signed | Matches A17C5_0405["ac"] |
| **202** | **0xCA** | pv_1_power (SB2) / pv_4_power (SB3) | In A17C5 overridden parseDeviceAllInfo |
| **203** | **0xCB** | expansion_packs (SB3) | Matches A17C5_0405["cb"] |
| **195** | **0xC3** | battery_soh | In A17C5 only |
| **210** | **0xD2** | light_mode | In A17C1's parseDeviceAllInfo at the end |
| **211** | **0xD3** | output_power | In A17C5 additional |
| **212** | **0xD4** | device_timeout_minutes | Matches A17C5_0405["d4"] -- SB3 exclusive |
| **213** | **0xD5** | pv_limit | Matches A17C5_0405["d5"] -- SB3 exclusive |
| **214** | **0xD6** | ac_input_limit | Matches A17C5_0405["d6"] -- SB3 exclusive |
| **224** | **0xE0** | grid_status | In A17C1_0405["e0"] but parsed differently in A17C5 |
| **225** | **0xE1** | light_off_switch | Additional in A17C5 |
| **232** | **0xE8** | battery_heating | A17C1_0405["e8"], in A17C5 parseDeviceAllInfo |
| **233** | **0xE9** | (unknown, SB3 only) | Only in A17C5, not in any upstream map |

### A17C5 Extra Commands vs A17C1 (from mqttmap.py device entries)

| Opcode | Command | A17C1 | A17C5 | Notes |
|--------|---------|-------|-------|-------|
| `005e` | CMD_SB_USAGE_MODE | no | yes | Usage mode (cloud-driven, not direct) |
| `0067` | CMD_SB_MIN_SOC | CMD_SB_POWER_CUTOFF | CMD_SB_MIN_SOC | Different command! SB3 uses simpler min_soc |
| `0073` | CMD_SB_AC_SOCKET_SWITCH | no | yes | Emergency AC socket toggle |
| `0080.a4` | set_max_load_a4? | no | yes | Extra field in SB3's max_load group |
| `0080.a7` | CMD_SB_PV_LIMIT | no | yes | PV MPPT limit: 2000 or 3600 W |
| `0080.a8` | CMD_SB_AC_INPUT_LIMIT | no (A17C2 has it) | yes | AC charge input limit: 0-1200W |
| `0085` | CMD_SB_3RD_PARTY_PV_SWITCH | no | yes | 3rd party PV support |
| `009a` | CMD_SB_DEVICE_TIMEOUT | no | yes | Device auto-off timeout (30min chunks) |
| `0420` | multisystem msg | no | yes | Multi-device status |
| `0421` | multisystem msg | no | yes | Multi-device params |
| `0428` | multisystem msg | no | yes | Multi-device energy |

### Summary of SB3-Exclusive Features
1. **AC Socket**: Tag 0x73 controls an emergency AC output socket (CMD_SB_AC_SOCKET_SWITCH)
2. **Device Timeout**: Tag 0x9A sets auto-shutdown timer in 30-minute increments (CMD_SB_DEVICE_TIMEOUT)
3. **PV Limit**: In the 0x80 compound group, tag a7 sets MPPT limit to 2000 or 3600W (CMD_SB_PV_LIMIT)
4. **Usage Mode**: Tag 0x5E controls the SB3 usage mode directly (cloud-driven, complex field structure)
5. **Min SOC**: SB3 uses simplified CMD_SB_MIN_SOC at 0x67 instead of SB2's 3-field CMD_SB_POWER_CUTOFF
6. **Grid Export Control**: Both have it in 0x80 group, identical
7. **3rd Party PV**: Tag 0x85, cloud-driven switch
8. **AC Input Limit**: In 0x80 group, tag a8, 0-1200W in 100W steps
9. **Extra data tags**: 0xD4 (timeout), 0xD5 (pv_limit), 0xD6 (ac_input_limit), 0xE9 (unknown SB3-only)
10. **Multi-system messages**: 0420, 0421, 0428 for multi-device coordination
