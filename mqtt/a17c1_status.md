> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# A17C1 MQTT status messages and requests

Solarbank 2 Pro/Plus (A17C1): the 0405 status message and the two request opcodes (0040, 0057) that make the device send it. This page is split from [a17c1.md](a17c1.md) (the SET commands) because the full set of sections would exceed the 600-line limit; the split follows the `mqtt/<pn>_status.md` rule of [../docs/STRUCTURE.md](../docs/STRUCTURE.md). A17C5 (Solarbank 3) differences are on [a17c5.md](a17c5.md). The envelope, topics, frame layout and data type codes are owned by [envelope.md](envelope.md) and not repeated here.

Evidence rows are written `audit row N` and refer to [../docs/audit/BLE_COMMAND_MAP.md](../docs/audit/BLE_COMMAND_MAP.md); `file.dart @0xADDR` is 3.24.3 asm. Opcodes are the hex strings of the Dart source; field keys are halved Smi immediates (324 is tag `a2`), per the Smi rule in [../METHODOLOGY.md](../METHODOLOGY.md#smi-rule-reading-numbers-from-blutter-output). Names are upstream's (`api/mqttmap.py`, `api/mqttcmdmap.py`); a name of ours is marked `(no upstream name)`.

## Contents

1. [Commands](#commands): [0405](#0405-status-message-param_info), [0040](#0040-status-request), [0057](#0057-realtime-trigger)

## Commands

### 0405 status message (param_info)

#### Purpose
Periodic status report of a Solarbank 2: power, SOC, energy counters, settings and version.

#### Upstream name
`_A17C1_0405` (topic `param_info`), `mqttmap.py` lines 1796-1863, upstream-confirmed.

#### Command code
`"0405"`; the string is the message type of the frame (opcode bytes `04 05`, [envelope.md](envelope.md#binary-layer)). Parsed by `A17C1DeviceCommands.parseDeviceAllInfo` @0x48648b4 (size 0x2450 in 3.24.3; 0x2264 in 3.18.0, audit row 369). Tag: upstream-confirmed for the message id (`mqttmap.py` line 5033); asm-traced for the parser.

#### Direction
device→app (`param_info` topic). Tag: asm-traced.

#### Topic pattern
[envelope.md](envelope.md#topics): `dt/anker_power/A17C1/<sn>/param_info`.

#### Payload fields
Rows are the tags that `parseDeviceAllInfo` reads as `indexString` arguments (hex number equals the decimal argument, untagged). The parser decodes with `listToInt` (little endian) and the divisors below are unboxed `sdiv` values (audit rows 56, 182). Where the audit gives no store site for a tag the cited address is the function start and only the tag-level binding is confirmed. Scales that upstream applies later (for example 0.0001 for `b1`) are not applied in the parser (audit row 183).

| tag | name | type | unit/scale | required | source |
|---|---|---|---|---|---|
| `fe` | `msg_timestamp` | int | - | n/a | audit row 370; parseDeviceAllInfo @0x48648b4 (function); upstream-confirmed (`mqttmap.py` line 1842) |
| `a2` | `device_sn` | string | UTF-8 | n/a | audit row 371; parseDeviceAllInfo @0x48648b4 (function); upstream-confirmed (`mqttmap.py` line 1799) |
| `a3` | `main_battery_soc` | int | two model fields are written | n/a | audit row 375; parseDeviceAllInfo @0x48648b4 (function); upstream-confirmed (`mqttmap.py` line 1800) |
| `a4` | (no upstream name) | int, unsigned | - | n/a | audit row 398; parseDeviceAllInfo @0x48648b4 (function) |
| `a5` | `error_code` | int | - | n/a | audit row 388; parseDeviceAllInfo @0x48648b4 (function); upstream-confirmed (`mqttmap.py` line 1801) |
| `a6` | `sw_version` | version bytes | `getMainVersionWithHex`, stored at 0x7b | n/a | audit row 372; parseDeviceAllInfo @0x48648b4 (function); upstream-confirmed (`mqttmap.py` line 1802) |
| `a7` | `sw_controller?` | int | - | n/a | audit row 373; parseDeviceAllInfo @0x48648b4 (function); upstream-confirmed (`mqttmap.py` line 1803) |
| `a8` | `sw_expansion` | int | - | n/a | audit row 374; parseDeviceAllInfo @0x48648b4 (function); upstream-confirmed (`mqttmap.py` line 1804) |
| `a9` | `temp_unit_fahrenheit` | int | - | n/a | audit row 389; parseDeviceAllInfo @0x48648b4 (function); upstream-confirmed (`mqttmap.py` line 1805) |
| `aa` | `temperature` | int, signed 8-bit | value >= 0x80 minus 0x100 | n/a | audit row 390; parseDeviceAllInfo @0x4865240; upstream-confirmed (`mqttmap.py` line 1806) |
| `ab` | `photovoltaic_power` | int | /10 (sdiv) | n/a | audit rows 380, 56; parseDeviceAllInfo @0x48652ec; upstream-confirmed (`mqttmap.py` line 1807) |
| `ac` | `ac_output_power` | int | /10 (sdiv) | n/a | audit rows 381, 56; parseDeviceAllInfo @0x4865384; upstream-confirmed (`mqttmap.py` line 1808) |
| `ad` | `battery_soc` | int | - | n/a | audit row 376; parseDeviceAllInfo @0x48648b4 (function); upstream-confirmed (`mqttmap.py` line 1809) |
| `ae` | (no upstream name) | bool | value == 1 | n/a | audit row 399; parseDeviceAllInfo @0x4864d9c |
| `af` | (no upstream name) | bool | value == 1 | n/a | audit row 400; parseDeviceAllInfo @0x4865458 |
| `b0` | `bat_charge_power` | int | /100 (sdiv) | n/a | audit rows 377, 56; parseDeviceAllInfo @0x48654fc; upstream-confirmed (`mqttmap.py` line 1810) |
| `b1` | `pv_yield` | int | no divisor in the parser (upstream FACTOR applies later) | n/a | audit row 384; parseDeviceAllInfo @0x48648b4 (function); upstream-confirmed (`mqttmap.py` line 1811) |
| `b2` | `charged_energy` | int | no divisor in the parser | n/a | audit row 385; parseDeviceAllInfo @0x48648b4 (function); upstream-confirmed (`mqttmap.py` line 1813) |
| `b3` | `output_energy` | int | no divisor in the parser | n/a | audit row 386; parseDeviceAllInfo @0x48648b4 (function); upstream-confirmed (`mqttmap.py` line 1812) |
| `b4` | `output_cutoff_data` | int | - | n/a | audit row 391; parseDeviceAllInfo @0x48648b4 (function); upstream-confirmed (`mqttmap.py` line 1814) |
| `b7` | `bat_discharge_power` | int | /100 (sdiv) | n/a | audit row 378; parseDeviceAllInfo @0x4865984; upstream-confirmed (`mqttmap.py` line 1817) |
| `b8` | (no upstream name) | int, unsigned | - | n/a | audit row 401; parseDeviceAllInfo @0x48648b4 (function) |
| `b9` | (no upstream name) | bool | value == 1 | n/a | audit row 402; parseDeviceAllInfo @0x4865b58 |
| `ba` | (no upstream name) | int | the read path divides by 100.0 | n/a | audit row 403; read path `a17c1home_logic.dart` @0x2623c8c..0x2623cac (the parser stores the raw int, @0x4865c1c..0x4865c3c) |
| `bb` | (no upstream name) | int, unsigned | - | n/a | audit row 404; parseDeviceAllInfo @0x48648b4 (function) |
| `c2` | `max_load` | int | - | n/a | audit row 392; parseDeviceAllInfo @0x48648b4 (function); upstream-confirmed (`mqttmap.py` line 1822) |
| `c6` | `usage_mode` | int | - | n/a | audit row 393; parseDeviceAllInfo @0x48648b4 (function); upstream-confirmed (`mqttmap.py` line 1824) |
| `c7` | `home_load_preset` | int | read, not stored; feeds the c8 chain | n/a | audit row 405; parseDeviceAllInfo @0x4865f50; upstream-confirmed (`mqttmap.py` line 1825) |
| `c8` | `ac_socket_power` | int | /10 (sdiv) | n/a | audit rows 382, 56; parseDeviceAllInfo @0x4865fc4; upstream-confirmed (`mqttmap.py` line 1826) |
| `c9` | `consumed_energy` | int | - | n/a | audit row 387; parseDeviceAllInfo @0x48648b4 (function); upstream-confirmed (`mqttmap.py` line 1827) |
| `d2` | `light_mode` | int | - | n/a | audit row 394; parseDeviceAllInfo @0x48648b4 (function); upstream-confirmed (`mqttmap.py` line 1832) |
| `d3` | `output_power` | int | /10 (sdiv) | n/a | audit row 383; parseDeviceAllInfo @0x486622c; upstream-confirmed (`mqttmap.py` line 1833) |
| `e0` | `grid_status` | bool | value == 7 | n/a | audit row 395; parseDeviceAllInfo @0x4866314; upstream-confirmed (`mqttmap.py` line 1834) |
| `e1` | `light_off_switch` | int | - | n/a | audit row 396; parseDeviceAllInfo @0x48648b4 (function); upstream-confirmed (`mqttmap.py` line 1835) |
| `e8` | `battery_heating` | bit list | element 0 == 1 means heating; element 1 == 1 sets a second flag | n/a | audit row 379; parseDeviceAllInfo @0x4866ac0; upstream-confirmed (`mqttmap.py` line 1836) |
| `e9` | (no upstream name) | int, unsigned | default 0 when absent | n/a | audit row 406; parseDeviceAllInfo @0x4866bd4 |
| `fb` | `(bytes)` | byte list | see the fb/fc table | n/a | audit row 397; parseDeviceAllInfo @0x48648b4 (function); upstream-confirmed (`mqttmap.py` line 1837) |
| `fc` | (no upstream name) | byte list | see the fb/fc table | n/a | audit rows 407, 408; parseDeviceAllInfo @0x486651c |

Upstream names tags the app parser does not read as listed rows: `b5` `lowpower_input_data` (line 1815), `b6` `input_cutoff_data` (line 1816), `bc` `grid_to_home_power`, `bd` `pv_to_grid_power`, `be` `grid_import_energy`, `bf` `grid_export_energy`, `c4` `home_demand`, `ca` to `cd` `pv_N_power` (lines 1818-1831). The audit's reading range `b0` to `bb` includes `b5` and `b6` without separate rows (audit row 638), and the A17C1 parser does not read `bd` to `c1` at all (audit row 638). The parser also checks the product strings `"A17C1"`, `"A17C5"`, `"A17C3"` and `"A17C2"` (audit row 353, pool strings), so one parser serves those products. The firmware bytes of `a6` are formatted with `getMainVersionWithHex`; the version format is owned by `ble/protocol.md` (default three segments, `getMainVersion` @0x263c6d4, audit rows 98-99). Conversions that use a mask or bit position (`e8`, `fb`) are in the rows above and below.

Byte lists of tags `fb` and `fc` (`field` = 3.24.3 store offset; both tags write the same list; `fb` is the primary and `fc` overwrites it when `fb` was empty, audit row 408):

| list element | meaning in the parser | 3.24.3 store | source |
|---|---|---|---|
| `[0]` | raw value | 675 (0x2a3) | audit row 410; parseDeviceAllInfo @0x48663bc, @0x4866478 |
| `[1]` | bool, element == 1 (the old doc compared with 2 at index 2) | 1203 (0x4b3) | audit row 411; @0x48665bc..0x48665f0 |
| `[5]` | bool, element == 1 | 1123 (0x463) | audit row 412; @0x486660c..0x4866648 |
| `[7]` | bool, element == 1 | 663 (0x297) | audit row 413; @0x4866770..0x48667a4 |
| `[9]` | raw value | 667 (0x29b) | audit row 414; @0x486670c..0x4866730 |
| `[11]` | bool, element == 1 | 1307 (0x51b) | audit row 409; @0x48667c0 (raw index 22, tagged) |
| `[12]`, `[13]` | read with `safeGet` (unboxed indexes) | not stored by the cited sites | audit row 409; @0x4866660, @0x48666b0 |
| `[14]` | bool, element == 1, only when the list has at least 15 bytes (`cmp x1,#0xf`); the app logs "supports10DevicesNetwork" | 283 (0x11b) | audit row 409; @0x4866858 (raw index 28, tagged) |

The old doc compared elements with 2; every such compare is a tagged compare and means 1 (audit rows 61, 411-413). Upstream decodes only byte `00` of `fb` as `grid_export_disabled` with mask 0x01 (`mqttmap.py` lines 1837-1841, upstream-confirmed); the app reads `[0]` raw (row `[0]` above) and does not apply that mask in the parser.

#### Example
synthesized. Not a capture; field contents are placeholders.

```text
ff 09 <len> 03 01 0f 04 05 | a1 01 22 | a2 <len> 00 <device_sn ...> | a3 02 01 <soc> | ... | fe 05 03 <ts> | xor
```

#### Related API endpoint
Site-level equivalents: [get_site_device_param](../api/power_service/site/get_site_device_param.md).

#### Since/changed
Every tag keeps its meaning; the store offsets inside the app's model moved in 3.24.3 (changed since 3.18.0, audit rows named in the table; offsets are Blutter byte offsets, not Smi-affected). Most moved by 0xC, `c6`, `b8`, `b9` by 0x18, `af` by 0x8; `fe`, `a2`, `a6` did not move. The `setTacticsTime` builder also changed size, see [a17c1.md](a17c1.md#005e-setbackpower-settacticstime-setpeakvalley).

| tag | 3.18.0 store | 3.24.3 store | source |
|---|---|---|---|
| `fe` | 0x6f | 0x6f | audit row 370; parseDeviceAllInfo @0x48648b4 (function) |
| `a2` | 0x6b | 0x6b | audit row 371; parseDeviceAllInfo @0x48648b4 (function) |
| `a6` | 0x7b | 0x7b | audit row 372; parseDeviceAllInfo @0x48648b4 (function) |
| `a7` | 0x2d7 | 0x2e3 (739) | audit row 373; parseDeviceAllInfo @0x48648b4 (function) |
| `a8` | 0x2eb | 0x2f7 (759) | audit row 374; parseDeviceAllInfo @0x48648b4 (function) |
| `a3` | 0x317, 0x3d3 | 0x323 (803), 0x3df (991) | audit row 375; parseDeviceAllInfo @0x48648b4 (function) |
| `ad` | 0x3d7 | 0x3e3 (995) | audit row 376; parseDeviceAllInfo @0x48648b4 (function) |
| `b0` | 0x243 | 0x24f (591) | audit row 377; parseDeviceAllInfo @0x48648b4 (function) |
| `b7` | 0x247 | 0x253 (595) | audit row 378; parseDeviceAllInfo @0x48648b4 (function) |
| `e8` | 0x2bf | 0x2cb (715) | audit row 379; parseDeviceAllInfo @0x48648b4 (function) |
| `ab` | 0x20b | 0x217 (535) | audit row 380; parseDeviceAllInfo @0x48648b4 (function) |
| `ac` | 0x237 | 0x243 (579) | audit row 381; parseDeviceAllInfo @0x48648b4 (function) |
| `c8` | 0x1db | 0x1e7 (487) | audit row 382; parseDeviceAllInfo @0x48648b4 (function) |
| `d3` | 0x23f | 0x24b (587) | audit row 383; parseDeviceAllInfo @0x48648b4 (function) |
| `b1` | 0x24b | 0x257 (599) | audit row 384; parseDeviceAllInfo @0x48648b4 (function) |
| `b2` | 0x24f | 0x25b (603) | audit row 385; parseDeviceAllInfo @0x48648b4 (function) |
| `b3` | 0x253 | 0x25f (607) | audit row 386; parseDeviceAllInfo @0x48648b4 (function) |
| `c9` | 0x257 | 0x263 (611) | audit row 387; parseDeviceAllInfo @0x48648b4 (function) |
| `a5` | 0x3db | 0x3e7 (999) | audit row 388; parseDeviceAllInfo @0x48648b4 (function) |
| `a9` | 0x3b7 | 0x3c3 (963) | audit row 389; parseDeviceAllInfo @0x48648b4 (function) |
| `aa` | 0x307 | 0x313 (787) | audit row 390; parseDeviceAllInfo @0x48648b4 (function) |
| `b4` | 0x25b | 0x267 (615) | audit row 391; parseDeviceAllInfo @0x48648b4 (function) |
| `c2` | 0x417 | 0x423 (1059) | audit row 392; parseDeviceAllInfo @0x48648b4 (function) |
| `c6` | 0x473 | 0x48b (1163) | audit row 393; parseDeviceAllInfo @0x48648b4 (function) |
| `d2` | 0x23b | 0x247 (583) | audit row 394; parseDeviceAllInfo @0x48648b4 (function) |
| `e0` | 0x42f | 0x43b (1083), 0x493 (1171) | audit row 395; parseDeviceAllInfo @0x48648b4 (function) |
| `e1` | 0x2b7 | 0x2c3 (707), 0x2c7 (711) | audit row 396; parseDeviceAllInfo @0x48648b4 (function) |
| `fb` | 0x287 | 0x293 (659) for the byte list | audit row 397; parseDeviceAllInfo @0x48648b4 (function) |
| `a4` | 0x30f | 0x31b (795) | audit row 398; parseDeviceAllInfo @0x48648b4 (function) |
| `ae` | 0x433 | 0x43f (1087) | audit row 399; parseDeviceAllInfo @0x48648b4 (function) |
| `af` | 0x187 | 0x18f (399) | audit row 400; parseDeviceAllInfo @0x48648b4 (function) |
| `b8` | 0x47f | 0x497 (1175) | audit row 401; parseDeviceAllInfo @0x48648b4 (function) |
| `b9` | 0x4cb | 0x4e3 (1251) | audit row 402; parseDeviceAllInfo @0x48648b4 (function) |
| `ba` | 0x26b | 0x277 (631) | audit row 403; parseDeviceAllInfo @0x48648b4 (function) |
| `bb` | 0x26f | 0x27b (635) | audit row 404; parseDeviceAllInfo @0x48648b4 (function) |
| `e9` | 0x2cb | 0x2d7 (727) | audit row 406; parseDeviceAllInfo @0x48648b4 (function) |

The fb list moved from 0x287 (647) to 0x293 (659) (audit row 408); the temperature store of every family parser moved from 0x307 to 0x313 (audit row 58).

#### Known unknowns
- `e0` is tested `== 7` in the parser (audit row 395) while upstream lists grid OK 1, no grid 6, connecting 3 (`mqttmap.py` line 1834): the meaning of 7 is open.
- The roles of `fb` elements `[1]`, `[5]`, `[7]`, `[9]`, `[11]`, `[12]`, `[13]`, `[14]` (no upstream names) are open; the old doc's labels were not confirmed.
- `ba` percentage scaling is confirmed on the read path only (audit row 403); `a3` and `ad` dual-store purpose is open.
- The bytes of tag `ab` and others are unsigned except `aa`; sign handling for `ac` was not seen in the parser (upstream name `ac_output_power`).
- Tags `a2` and `a4` are also read by `parseSubBatteryErrorInfoMap`; which of them is the error code and which the message was not traced (audit row 102; the status error code is tag `a5`).

#### Device-tested by
A17C1 FW 1.0.6.10, mqtt_monitor session of 2026-03-28 (136 messages): values listed in the old doc (audit row 415, not decoded from asm); client version and tester are not recorded in this repo, so no field above carries `device-tested`. Source note: [../devices/solarbank.md](../devices/solarbank.md).


### 0040 status request

#### Purpose
Asks the device for one status message round (upstream: "more reliable than the realtime trigger").

#### Upstream name
`CMD_STATUS_REQUEST` in `mqttcmdmap.py` line 222; bound to `"0040"` for A17X8 at `mqttmap.py` line 5372 (not bound for A17C1 in upstream), upstream-confirmed.

#### Command code
`"0040"`, pool list `[0, 0x40]` (audit row 230; pool lists are untagged, real values). Asm-traced.

#### Direction
app→device. Tag: asm-traced.

#### Topic pattern
[envelope.md](envelope.md#topics): `cmd/anker_power/A17C1/<sn>/req`.

#### Payload fields
| tag | name | type | unit/scale | required | source |
|---|---|---|---|---|---|
| (none) | no payload besides the frame trailer | - | - | - | audit row 230; a172x_device_controller.dart @0x40f3ff4 (an example use of the pool list) |

#### Example
synthesized

```text
ff 09 <len> 03 00 0f 00 40 | a1 01 22 | fe 05 03 <ts> | xor
```

#### Related API endpoint
none (MQTT only).

#### Since/changed
No change recorded by the audit.

#### Known unknowns
- The audit found the pool list used by the controllers (example @0x40f3ff4) but not the A17C1 call site of this opcode.

#### Device-tested by
none recorded for this opcode.


### 0057 realtime trigger

#### Purpose
Starts the regular status messages (0405 and others) for a limited time.

#### Upstream name
`CMD_REALTIME_TRIGGER` (`mqttcmdmap.py` line 227; bound at `mqttmap.py` line 4992), upstream-confirmed.

#### Command code
`"0057"`, pool list `[0, 0x57]` (audit row 229). The builder with one 1-byte tag and one 4-byte tag sits at function 0x4081988 (size 0xf8, found next to A17C0 `setDeviceUpdateEnergy` @0x4081890); it is not a `remoteConfigWifi` call (that function @0x3b71bd8 is the MQTT `remoteSwitchWifi` call with ssid and pwd and no opcode). Asm-traced.

#### Direction
app→device. Tag: asm-traced.

#### Topic pattern
[envelope.md](envelope.md#topics): `cmd/anker_power/A17C1/<sn>/req`.

#### Payload fields
| tag | name | type | unit/scale | required | source |
|---|---|---|---|---|---|
| `a2` | `set_realtime_trigger` | 1 byte (`intToList`) | 0 off, 1 on (upstream) | yes | audit row 229; function @0x4081988; upstream-confirmed (`mqttcmdmap.py` line 231) |
| `a3` | `trigger_timeout_sec` | 4 bytes (`intToList4`) | seconds, 60 to 600 (upstream) | yes | audit row 229; function @0x4081988; upstream-confirmed (`mqttcmdmap.py` line 237) |

#### Example
synthesized

```text
ff 09 <len> 03 00 0f 00 57 | a1 01 22 | a2 02 01 01 | a3 05 03 3c 00 00 00 | fe 05 03 <ts> | xor
```

#### Related API endpoint
none (MQTT only).

#### Since/changed
No change recorded by the audit.

#### Known unknowns
- Which controller class owns the 0x4081988 function for A17C1 (the audit names the address, not the class).
- Upstream's limits 60 to 600 s are upstream values; the app's own value is not in the audit.

#### Device-tested by
none recorded in this repo for the app's builder; upstream sends it routinely (upstream-confirmed).

