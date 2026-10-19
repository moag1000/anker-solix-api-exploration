> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# Shelly MQTT status (third-party devices)

Shelly Pro 3EM / Plug (third-party devices that the app handles through `ShellyDeviceCommands`): the status tags the parser reads and the location of the strings the old doc listed. There is no audit row for this section of the old doc (the audit marks the Shelly key tables NOT-FROM-ASM, row 649), so the page rests on new asm reads, each cited with its address. The envelope, topics, frame layout and data type codes are owned by [envelope.md](envelope.md).

Evidence rows are written `audit row N` and refer to [../docs/audit/BLE_COMMAND_MAP.md](../docs/audit/BLE_COMMAND_MAP.md); `file.dart @0xADDR` is 3.24.3 asm. Tag keys are halved Smi immediates (per the Smi rule in [../METHODOLOGY.md](../METHODOLOGY.md#smi-rule-reading-numbers-from-blutter-output)). Names are upstream's (`api/mqttmap.py`); a name of ours is marked `(no upstream name)`.

## Contents

1. [Commands](#commands): [parseDeviceAllInfo](#parsedeviceallinfo-shelly), [old doc strings](#old-doc-shelly-status-strings)

## Commands

### parseDeviceAllInfo (Shelly)

#### Purpose
Reads the status tags of a Shelly third-party device (Pro 3EM meter, plug) registered with the app.

#### Upstream name
`SHEMP3` (Shelly Pro 3EM) `"0405"`, topic `param_info`, tags `a2`, `a8`, `a9`, `aa`, `ab`, `fe` (`mqttmap.py` lines 5357-5369; `"0057"` realtime trigger at line 5358), upstream-confirmed. Product names: `SHEMP3` Shelly Pro 3EM, `SHPPS` Shelly Plus Plug S, `SHEM3` Shelly 3EM (`apitypes.py` lines 1157-1159). Upstream has no mapping for the plug.

#### Command code
`"0405"` (upstream message id for SHEMP3). `ShellyDeviceCommands.parseDeviceAllInfo` @0x3b612b4 (size 0xa10; `charging/ble/device/third_party_device/Shelly/shelly/shelly_device_commands.dart`). The Shelly device classes are `shelly_device.dart`, `shelly_pro_device.dart` and `shelly_plug_device.dart` in the same directory tree. New read; the audit has no row for Shelly (row 649 is a NOT-FROM-ASM note about key tables). Asm-traced for the tag set; upstream-confirmed for the names.

#### Direction
device→app. Tag: asm-traced.

#### Topic pattern
[envelope.md](envelope.md#topics): `dt/anker_power/SHEMP3/<sn>/param_info` (topic suffix upstream-confirmed).

#### Payload fields
The parser reads nine tags (new read, tag numbers only; the field binding of `fe` and `a2` is from the store instructions). The old doc listed no tags for Shelly, only seven debug strings (see the next section).

| tag | name | unit/scale | required | source |
|---|---|---|---|---|
| `fe` | `msg_timestamp` | int; stored to `field_6f` @0x3b61438 | n/a | new read (no audit row); shelly_device_commands.dart parseDeviceAllInfo @0x3b612b4 (function); tag read @0x3b61308, @0x3b61344; upstream-confirmed (`mqttmap.py` line 5367) |
| `a2` | `device_sn` | string; stored to `field_6b` @0x3b61508 | n/a | new read (no audit row); shelly_device_commands.dart parseDeviceAllInfo @0x3b612b4 (function); tag read @0x3b61448, @0x3b614a8; upstream-confirmed (`mqttmap.py` line 5362) |
| `a3` | (no upstream name) | - | n/a | new read (no audit row); shelly_device_commands.dart parseDeviceAllInfo @0x3b612b4 (function); tag read @0x3b61530, @0x3b6156c, @0x3b619bc, @0x3b61a50; read twice early (@0x3b61530, @0x3b6156c) and twice after the `shellyPlugOutPutPower` log string (@0x3b619bc, @0x3b61a50) |
| `a5` | (no upstream name) | - | n/a | new read (no audit row); shelly_device_commands.dart parseDeviceAllInfo @0x3b612b4 (function); tag read @0x3b615e8, @0x3b61b00; read early (@0x3b615e8) and after the `shellyPlugSwitch` log string (@0x3b61b00) |
| `a8` | `grid_to_home_power` | factor 0.01 (upstream) | n/a | new read (no audit row); shelly_device_commands.dart parseDeviceAllInfo @0x3b612b4 (function); tag read @0x3b6167c; upstream-confirmed (`mqttmap.py` line 5363) |
| `a9` | `pv_to_grid_power` | factor 0.01 (upstream) | n/a | new read (no audit row); shelly_device_commands.dart parseDeviceAllInfo @0x3b612b4 (function); tag read @0x3b61710; upstream-confirmed (`mqttmap.py` line 5364) |
| `aa` | `grid_import_energy` | factor 0.00001 (upstream) | n/a | new read (no audit row); shelly_device_commands.dart parseDeviceAllInfo @0x3b612b4 (function); tag read @0x3b617a4; upstream-confirmed (`mqttmap.py` line 5365) |
| `ab` | `grid_export_energy` | factor 0.00001 (upstream) | n/a | new read (no audit row); shelly_device_commands.dart parseDeviceAllInfo @0x3b612b4 (function); tag read @0x3b61838; upstream-confirmed (`mqttmap.py` line 5366) |
| `ac` | (no upstream name) | - | n/a | new read (no audit row); shelly_device_commands.dart parseDeviceAllInfo @0x3b612b4 (function); tag read @0x3b618e4 |

#### Example
synthesized. Frame layout only (TLV entries as in [envelope.md](envelope.md#tlv-frame)); not a capture.

```text
a1 01 22 | a2 <len> 00 <device_sn> | a8 03 02 <w lo> <hi> | aa 05 03 <energy 4 bytes> | fe 05 03 <ts 4 bytes> | xor
```

#### Related API endpoint
none (MQTT only).

#### Since/changed
No 3.18.0 comparison was made (no audit row).

#### Known unknowns
- The meaning of `a3`, `a5` and `ac` (no upstream name; `a3` and `a5` are read twice and sit next to the plug log strings).
- Which tags belong to the meter and which to the plug: upstream maps only the meter (SHEMP3).
- The widths and types of the values (tag numbers only).
- Whether upstream `grid_to_home_power` and `pv_to_grid_power` are the values the old doc called `fromGrid` and `toGrid`: the strings are not in the Shelly parser.

#### Device-tested by
none.

### Old doc Shelly status strings

#### Purpose
Locates the seven strings the old doc listed as "Shelly (3rd party) status fields" in the 3.24.3 asm.

#### Upstream name
none.

#### Command code
No command code; log strings and key literals. String-only: each string exists at the cited site, no value binding is traced.

#### Direction
device→app. Tag: string-only.

#### Topic pattern
Not applicable.

#### Payload fields
Only two of the seven strings belong to the Shelly parser. The others are key literals of other device models (AE1R0, A17X7) or app-wide event keys, so the old doc table is not a Shelly field map.

| string | meaning (old doc) | where it exists in 3.24.3 | old doc name |
|---|---|---|---|
| `shellyPlugOutPutPower` | plug output power | `string-only`: log text `ShellyPlugDevice shellyPlugOutPutPower: ` @0x3b61994 in the Shelly parser (no plain-key literal in the pool) | `plug_output_power` (old doc, no upstream name) |
| `shellyPlugSwitch` | plug switch state | `string-only`: log text `ShellyPlugDevice shellyPlugSwitch: ` @0x3b61acc in the Shelly parser; the plain key `shellyPlugSwitch` [pp+0xc5460] is used by `shellyhome_logic.dart` @0x27a33e0 and @0x30740d0 | `plug_switch_state` (old doc, no upstream name) |
| `fromGrid`, `toGrid` | grid import / export power | `string-only`: key literals in `third_device/sdk/model/ae1r0_device_info.dart` @0x35afae0, @0x35afafc (AE1R0 device model, not the Shelly files); also localisation labels | `grid_import_power`, `grid_export_power` (old doc) |
| `fromGridSum`, `toGridSum` | grid import / export totals | `string-only`: key literals in `ae1r0_device_info.dart` @0x35afb14, @0x35afb2c; `fromGridSum` also occurs in `charging/ble/device/A17X7/a17x7_device_commands.dart` (see [a17x7.md](a17x7.md)) | `grid_import_total`, `grid_export_total` (old doc) |
| `totalChargingPower` | total charging power | `string-only`: event key in `base_service/ak_iot_kit/event_receiver.dart` @0x220f7e8 and `a1903/module.dart` @0x4581818 (pool [pp+0xcf10]); log text in the A17C0 parser @0x3b533b8 | `total_charging_power` (old doc) |

#### Example
synthesized. Not applicable: the strings are log text and JSON keys, not frame content.

```text
(none)
```

#### Related API endpoint
none (MQTT only).

#### Since/changed
No 3.18.0 comparison was made.

#### Known unknowns
- Whether the Shelly cloud payload uses the keys `fromGrid`, `toGrid`, `fromGridSum`, `toGridSum`: the literals belong to AE1R0 and A17X7 code in 3.24.3.
- The old doc names (`grid_import_power` and so on) are labels of ours (no upstream name).

#### Device-tested by
none.

