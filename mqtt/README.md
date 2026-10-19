> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# MQTT

This directory holds one decoder page per product number (`<pn>.md`, lowercase PN) that owns the MQTT field maps for that product, plus `envelope.md` for the JSON envelope, topics, compression, command types and the binary frame shared by all products.

Not here: endpoint payloads ([../api/README.md](../api/README.md)), BLE opcodes and TLV ([../ble/README.md](../ble/README.md)); owner map in [../docs/STRUCTURE.md](../docs/STRUCTURE.md).

## Pages written (Task 3.6a)

| page | covers | audit rows (docs/audit/BLE_COMMAND_MAP.md) |
|---|---|---|
| [envelope.md](envelope.md) | head fields, command types, payload variants, topics, gzip check, binary layer, TLV frame, data type codes | 4-44, 63-66 (and 165, 167 for the opcode bytes) |
| [a17c1.md](a17c1.md) | A17C1 SET commands 0050, 005e, 0067, 0068, 0073, 0080, 009a, 005f, 0071, 0081 and the opcodes without a confirmed builder | 24, 84-88, 103-160 (enums, linked), 165, 169, 175, 180, 217-228, 231-235, 645 |
| [a17c1_status.md](a17c1_status.md) | A17C1 0405 status (split from a17c1.md for the 600-line limit), 0040, 0057 | 56, 58, 61, 98-99, 102, 182-183, 229-230, 353, 369-415, 638 |
| [a17c5.md](a17c5.md) | A17C5 differences from A17C1 (tag sets, shared SET opcodes, 0085, multi-system messages) | 56, 58, 159, 180, 182, 228, 637-648 |
| [a17x8.md](a17x8.md) | A17X8 0405, CountDownInfo, TimingInfo, 007a, 007c, 007e, 007f, 007d, 0079, 007b | 1, 55, 67-77, 79-83, 167, 187, 229-230, 236-242, 355-368 |
| [a17x7.md](a17x7.md) | A17X7 0405 and parseWorkInfo, A17X7US variant note | 58, 264-294 |
| [a17b1.md](a17b1.md) | A17B1 JSON status messages and the app model with DataFlow and Bd | 100-101, 350-354 |
| [a5101.md](a5101.md) | A5101 JSON status, BLE data code maps (corrected pairing), 002d (getBluetoothOTAStatus), 0115, 0030, work mode numbers | 199-216, 316-317, 651 (189-198 are API models owned by `models/hes.md`) |

Pages carry their own status header with the lowest tag on that page. `asm-traced`: envelope, a17c1, a17c1_status, a17c5, a17b1, a5101, a172x, a1771, a1753, a1780, a1790, a2345, a91b2, a17c0, iot. `string-only`: a17x8 (the 0040/0057 binding), a17x7 (the `ad` alternate source), a17c2 (field labels from debug strings), a1340 (device-level debug strings) and shelly (strings and a new tag read, no audit row). `upstream-confirmed`: upstream_commands (index of upstream constants). The three enum references (audit rows 103-160) are linked from the PN pages and will be owned by `reference/enums.md`.

## Pages written (Task 3.6b)

| page | covers | audit rows (docs/audit/BLE_COMMAND_MAP.md) |
|---|---|---|
| [a172x.md](a172x.md) | A172X (C300 family): 0405 status tags of the A1726 parser, the PPS single-value setters 0043 to 0079 | 440-458, 245-248, 250-260 (249 in Known unknowns) |
| [a1771.md](a1771.md) | A1771 (F1200): 0405 status tags, sibling-map names | 295-311, 459-485 |
| [a1753.md](a1753.md) | A1753 (C800): tags e5, f8, f9 on top of A1771; A1781 note | 312-314 |
| [a1780.md](a1780.md) | A1780 (F2000): positional parser (`parseOtherData`, `parseSwitchData`, `parseCountdownData`, `parseDeviceInfo`) with the audit's corrected byte windows | 517-582 |
| [a1790.md](a1790.md) | A1790 (F3800): 0405 status tags, SubBatteryInfo model, setters 0078, 005f, 0060, 0091 | 89-90, 486-516, 261-263 |
| [a2345.md](a2345.md) | A2345 (250 W Prime Charger): status tags, OutputPortInfo (`parseChargePortInfo`), setters | 91-97, 324-328 (A2345 parts), 329-341 |
| [a91b2.md](a91b2.md) | A91B2 (240 W Charging Station): status tags (new tag read), setters | 324-328 (A91B2 parts) |
| [a17c0.md](a17c0.md) | A17C0 (Solarbank E1600): 0405 status tags, setters 0050, 005e, 0067, 0068, 0071 | 416-439, 243-244 |
| [a17c2.md](a17c2.md) | A17C2 (Solarbank 2 AC): 0405 status tags, setters shared with A17C1 | 342-349, 217-235 (by link to a17c1.md) |
| [a1340.md](a1340.md) | A1340 (portable power bank): per-port tags, device-level debug strings | 350-351, 650 |
| [shelly.md](shelly.md) | Shelly Pro 3EM / Plug: status tags and the location of the old doc strings (new asm reads, no audit row) | none (row 649 is a NOT-FROM-ASM note) |
| [upstream_commands.md](upstream_commands.md) | Index of every `mqttcmdmap.py` constant with its bindings and the PN pages | 583-636 |
| [envelope.md](envelope.md#infrastructure) | New Infrastructure section: `i_mqtt_serve.dart`, `mqtt_types.dart`, `local.dart` (new asm reads) | none |

Audit rows without an MQTT page: 189-198 are API response models and examples (not MQTT facts); their owners are the `models/` pages ([../models/scene_info_model.md](../models/scene_info_model.md) for 189-190, [../models/site_device_param_response.md](../models/site_device_param_response.md) for 191, [../models/hes.md](../models/hes.md) for 193-195 and 197-198, [../models/heat_pump_param.md](../models/heat_pump_param.md) for 196; row 192 is a JSON example with no asm value). Rows 89-97 (data structures) are owned by [a1790.md](a1790.md) (SubBatteryInfo, 89-90) and [a2345.md](a2345.md) (OutputPortInfo, 91-97).

## Pages written (Task 3.6c)

| page | covers | audit rows (docs/audit/BLE_COMMAND_MAP.md) |
|---|---|---|
| [iot.md](iot.md) | The generic decoder (`IotDeviceController` in `iot_anker_controller.dart`, 3.18.0 list entry `iot`) and the shared pipeline: MQTT receive path and topic gate, PN routing in `createByProductCode` (52 literals, fallback to the iot controller), `parseResponse` frame checks, the `chargingOpcodeMap` and `commonOpcodeMap` opcode tables, `_parsePayloadData` dispatch, `parseCommonData` tag map, the fallback controller's three branches | 14, 15, 25, 48-52 (no audit row names the iot decoder; the rest is new asm reads) |

## Source conflicts (unresolved)

- Tag `fd`: upstream describes a millisecond timestamp string, the app builders write a CRC32 (audit rows 24, 219-221). See [envelope.md](envelope.md#tlv-frame) and [a17c1.md](a17c1.md#005e-setbackpower-settacticstime-setpeakvalley). Untested here.
- A17C1 tag `e0`: the parser tests `== 7` (audit row 395), upstream lists 1, 6 and 3. See [a17c1_status.md](a17c1_status.md#payload-fields).
- Opcode `005a`: the app has no builder (audit row 222) while [../devices/solarbank.md](../devices/solarbank.md) lists it as tested. See [a17c1.md](a17c1.md#opcodes-without-a-confirmed-app-builder-005a-0082-006a-0069).
- A2345 message id: the old doc calls the parser "0405", upstream binds `"0a00"` and `"0303"` for A2345 and A91B2 and has no `"0405"` for either; the asm audit does not bind either parser to a message id (the old doc mentions A91B2 only as a 4th port). See [a2345.md](a2345.md#parsedeviceallinfo-status-tags-upstream-message-0a00) and [a91b2.md](a91b2.md#parsedeviceallinfo-status-tags-upstream-message-0a00).
- A2345 port tags: upstream has six port blocks (`a4` to `a9`), the old doc listed `a4` to `a6` as port blocks and `a7` to `ab` as plain ints; the asm calls the port sub-parser six times. Same pages.
- `f8` port saving modes (A1753, A1790): upstream (A1761/A1780 maps) calls bytes [0] and [1] Normal (1) / Smart (2); the app enum maps 1 to close and 2 to open (audit rows 313, 515). See [a1753.md](a1753.md#payload-fields) and [a1790.md](a1790.md#known-unknowns).
- A17C2 field labels: the debug strings in the parser (for example `ab` total output power) conflict with the upstream names via the A17C5 map (`ab` `photovoltaic_power`). See [a17c2.md](a17c2.md#payload-fields).
- A1771 names: upstream has no A1771 key; the sibling maps (A1761, A1780) disagree with the old doc labels at `a5`, `d1`, `d5` and at `a2`/`a3`. See [a1771.md](a1771.md#payload-fields).
- A1780 positional windows: the old doc mapped two blocks to the tag `bd` and six names differ from upstream (`a5`, `a6`, `af`, `b0`, `c5`, `db`). See [a1780.md](a1780.md#known-unknowns).
- Opcode `005a` for A17C2: upstream binds it (parallel-system max load), the app has no builder in the audited files (audit row 222). See [a17c2.md](a17c2.md#known-unknowns-1) and [upstream_commands.md](upstream_commands.md).
- Opcode `0067` related API: the earlier mapping names `set_site_device_param` param type 18, the flow trace shows `set_power_cutoff` before `setSoc` and no param type 18 call. See [a17c1.md](a17c1.md#0067-setsoc) and [../flows/solarbank_soc_reserve_change.md](../flows/solarbank_soc_reserve_change.md).
- Upstream `CMD_SOC_LIMITS_V2` describes `fd` as a timestamp, the app writes a CRC32 (audit rows 599, 219); same finding as the `fd` item above.
- Old doc Shelly strings: only `shellyPlugOutPutPower` and `shellyPlugSwitch` exist in the Shelly parser; `fromGrid`, `toGrid`, `fromGridSum`, `toGridSum` and `totalChargingPower` belong to other models (AE1R0, A17X7) or app-wide keys. See [shelly.md](shelly.md#old-doc-shelly-status-strings).
- Frame byte 6: [envelope.md](envelope.md#binary-layer) records it as `0F` in captures with its source unresolved; [iot.md](iot.md#frame-decode-and-opcode-dispatch) shows the app reads byte 6 as the group byte that selects `commonOpcodeMap` (value 1) or `chargingOpcodeMap` (any other value). Refinement, not a contradiction; envelope.md is not edited here.
- `charging/mqtt/local.dart` holds certificate and key material, not a local MQTT client. See [envelope.md](envelope.md#infrastructure).

## Not covered by 3.6a and 3.6b

Audit rows 318-323 and 653 (EverFrost cooler A17A0 to A17A5: command-key map, not TLV), row 315 (A5190/A5191 `encoding_type`, UNVERIFIABLE, recorded in [envelope.md](envelope.md#known-unknowns)) and the EV charger constants of [upstream_commands.md](upstream_commands.md) (no EV charger PN page yet) have no page. They were not part of the 3.6a or 3.6b scope; the 3.6a list of pending products is empty. The `iot` decoder is now [iot.md](iot.md); its product-routing table also lists the products that have a controller but no PN page (A1770, A1780P, A5140 family, A5150, A17Y0, EverFrost A17A0 to A17A5).
