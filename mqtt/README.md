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
| [a5101.md](a5101.md) | A5101 JSON status, BLE data code maps (corrected pairing), 002d, 0030 | 199-216, 316-317, 651 (189-198 are API models owned by `models/hes.md`) |

Pages carry their own status header with the lowest tag on that page: `asm-traced` on envelope, a17c1, a17c1_status, a17c5, a17b1 and a5101; `string-only` on a17x8 (the 0040/0057 binding) and a17x7 (the `ad` alternate source). The three enum references (audit rows 103-160) are linked from the PN pages and will be owned by `reference/enums.md`.

## Source conflicts (unresolved)

- Tag `fd`: upstream describes a millisecond timestamp string, the app builders write a CRC32 (audit rows 24, 219-221). See [envelope.md](envelope.md#tlv-frame) and [a17c1.md](a17c1.md#005e-setbackpower-settacticstime-setpeakvalley). Untested here.
- A17C1 tag `e0`: the parser tests `== 7` (audit row 395), upstream lists 1, 6 and 3. See [a17c1_status.md](a17c1_status.md#payload-fields).
- Opcode `005a`: the app has no builder (audit row 222) while [../devices/solarbank.md](../devices/solarbank.md) lists it as tested. See [a17c1.md](a17c1.md#opcodes-without-a-confirmed-app-builder-005a-0082-006a-0069).

## Pending (Task 3.6b)

A172X family (C300/C300X and the other PPS products), A1771 (C1000), A1780 and A1790 (F2000, F3800), A17C0, A17C2, A2345 and A91B2 (Prime chargers), A1753, A1781, A1340, A17a3, Shelly and the `iot` decoder. Their audit rows are 295-349, 416-636 (see the section index in [../docs/audit/BLE_COMMAND_MAP.md](../docs/audit/BLE_COMMAND_MAP.md)). The MQTT infrastructure files new in 3.24.3 (`i_mqtt_serve.dart`, `mqtt_types.dart`, `local.dart`) are not covered by any page yet.
