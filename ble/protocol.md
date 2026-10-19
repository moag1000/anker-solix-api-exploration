> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# BLE protocol

This page owns what is specific to the Bluetooth LE transport of the Solix and Prime devices in App 3.24.3: which GATT UUIDs each product uses, how a command is chosen to go over BLE, the flag bits the transport adds to the opcode byte, fragmentation, payload encryption, the timeouts, and the WiFi/BLE exclusion rule. The binary frame itself (9-byte header, TLV fields, data type codes) is the same one that travels inside the MQTT `payload.data` and is owned by [../mqtt/envelope.md](../mqtt/envelope.md); this page links to it and adds only what differs on BLE. The negotiation that produces the session key is on [handshake.md](handshake.md). Per-product BLE facts are on the `ble/<pn>.md` pages listed in [README.md](README.md); their command tables live on the `mqtt/<pn>.md` pages ([../mqtt/README.md](../mqtt/README.md)).

Every number below follows the Smi rule of [../METHODOLOGY.md](../METHODOLOGY.md#smi-rule-reading-numbers-from-blutter-output). Evidence is the asm of 3.24.3 (`file.dart @0xADDR`, paths relative to the Blutter `asm/` root) and the audited rows of [../docs/audit/BLE_COMMAND_MAP.md](../docs/audit/BLE_COMMAND_MAP.md) (written `audit row N`) and [../docs/audit/BUSINESS_RULES.md](../docs/audit/BUSINESS_RULES.md) (rows are identified there by the `doc line` column and written `BUSINESS_RULES doc line N`). Where a row of an audit table was corrected by a fresh trace, the page says so.

## Contents

1. [Stacks and send routing](#stacks-and-send-routing)
1. [GATT profile per product](#gatt-profile-per-product)
1. [Frame on BLE](#frame-on-ble)
1. [Opcode byte 0 flags](#opcode-byte-0-flags)
1. [Fragmentation](#fragmentation)
1. [Payload encryption](#payload-encryption)
1. [MTU](#mtu)
1. [Timeouts and limits](#timeouts-and-limits)
1. [Connection routing and the WiFi exclusion rule](#connection-routing-and-the-wifi-exclusion-rule)
1. [ZX opcode names](#zx-opcode-names)
1. [Since 3.18.0](#since-3180)
1. [Known unknowns](#known-unknowns)

## Stacks and send routing

Tag: asm-traced.

The app has more than one BLE I/O path. `ReactiveBleManager` constructs `SdkBleScannerImpl`, `SdkBleDeviceConnectorImpl` and `SdkBleOperationImpl` (`charging/ble/reactive_ble_manager.dart @0x2217500`, `@0x2217538`, `@0x2217570`), so scanning, connecting and reading/writing characteristics are delegated to the AK IoT kit (`charging/ble/sdk_handler/*`, platform-channel methods such as `akiot.ble.write_characteristic`). The same class also keeps a `Uuid.parse` based `_setNotifyCharacteristic` / `_setWriteCharacteristic` pair (`@0x2217b58`) and a `_setMtu` (`@0x22179b4`). `SimpleBleConnector.connect` (`base_service/util/simple_ble_connector.dart @0x4317cec`) asks `_isLegacyDevice` (`@0x43184fc`) and then runs either `_connectLegacyDevice` (`@0x4318008`: `startScanWithConnect` with a timeout) or `_connectNewDevice` (`@0x4317f20`: `checkPermissionAndReconnect`); a second `connect` while one is running returns false with the log `Already connecting, skipped` (`@0x4317d28`).

Which of two transports carries a command is decided per call by the device controller. `A17C1DeviceController.sendCommandWithParam` (`charging/ble/device/A17C1/a17c1_device_controller.dart @0x226df0c`) reads the device connection status. When it equals `DeviceConnectionStatus.bleBusinessConnected` (`@0x226e22c`) the command is built by the ZX transformer (`formatCommand` with the named arguments `functionType`, `isEncrypted`, `isMoreLength`, `isNormalCommand`, `useSecureInteraction`, `valueMap`, `@0x226e288`; `functionType` is the Smi raw 30, real 15, `@0x226e26c`, BUSINESS_RULES doc line 207) and written to the BLE characteristic. When it equals `wifiConnected` (`@0x226e4e4`) the same builder is called with `isBle` instead and the result is wrapped by the MQTT transformer (`MqttCommandType.normalCommand`, `@0x226e574`), see [../mqtt/envelope.md](../mqtt/envelope.md#payload-variants). So the two transports share one command builder and differ in the wrapper and in the connection status that selects them.

## GATT profile per product

Tag: asm-traced.

The UUIDs are properties of the product table: `ProductModel` (`base_service/model/product_model.dart`) has the fields `productCode`, `name`, `labelName`, `scanUUID`, `serviceUUID`, `writeUUID` and `notifyUUID` (`toJson` `@0x2260184`), and one static `<pn>Model()` function per product fills them. The ZX family uses one UUID triple: service `8c850001-0302-41c5-b46e-cf057c562025`, write characteristic `8c850002-0302-41c5-b46e-cf057c562025`, notify characteristic `8c850003-0302-41c5-b46e-cf057c562025` (pool strings `[pp+0x9470]`, `[pp+0x9478]`, `[pp+0x9480]`), and the scan filter is the 16-bit service `0000FF09` (`[pp+0x9468]`). The frame marker `FF 09` of the binary layer ([../mqtt/envelope.md](../mqtt/envelope.md#binary-layer)) has the same value as this scan UUID. UUIDs are public identifiers of the GATT profile, not secrets.

| group | products (`<pn>Model` start address) | scan | service / write / notify |
|---|---|---|---|
| ZX family (lowercase) | A17C1 @0x22c3b38, A17C2 @0x22c3908, A17C3 @0x22c3978, A17C5 @0x22c3898, A17C0 @0x22c4388, A17B1 @0x22c40e8, A17X7 @0x22c3ac8, A17X7US @0x22c39e8, A17X8 @0x22c3a58, A17Y0 @0x22c3f98, A2345 @0x22c3eb8, A91B2 @0x22c3f28, A1722 @0x22c3e48, A1723 @0x22c3dd8, A1725 @0x22c3d68, A1726 @0x22c3cf8, A1727 @0x22c3c88, A1728 @0x22c3c18, A1729 @0x22c3ba8, A1753 @0x22c45b8, A1754 @0x22c4548, A1755 @0x22c44d8, A1761 @0x22c4468, A1762 @0x22c43f8, A1763 @0x22c32c0, A1772 @0x22c4158, A1780P @0x22c41c8, A1781 @0x22c4238, A1782 @0x22c2ff8, A1783 @0x22c2f88, A17A3 @0x22c47f0, A17A4 @0x22c4778, A17A5 @0x22c4708, A17E1 @0x22c36e0, A17E2 @0x22c3670, AE103 @0x22c3520, AE111 @0x22c3600, AE113 @0x22c3590, AX170 @0x22c34b0, AE1X0 @0x22c3440, AE1R0 @0x22c33d0, A5190 @0x22c3828, A5191 @0x22c37b8, A7320 @0x22c3750, A25X7 @0x22c3068, A2687 @0x353f200, A120J @0x45a6524, SHPPS @0x22c2e38, SHEMP3 @0x22c2ea8, SHEM3 @0x22c2f18 | `0000FF09` | `8c850001-0302-41c5-b46e-cf057c562025` / `8c850002-...` / `8c850003-...` (same suffix) |
| ZX family (uppercase literals) | A1790 @0x22c4078, A1790P @0x22c4008 | `0000FF09` | `8C850001-0302-41C5-B46E-CF057C562025` / `8C850002-...` / `8C850003-...` (`[pp+0x97f8]`, `[pp+0x9800]`, `[pp+0x9808]`) |
| Prime / HES power module | A5101 @0x22c42a8, A5102 @0x22c31a0, A5103 @0x22c3130 | `0000FF09` | `41580001-4002-81c5-b46e-cf057c562025` / `41580002-...` / `41580003-...` |
| F1200 (Bluetooth and WLAN) | A1771 @0x22c4628 | `00002540-0000-1000-8000-00805f9b34fb` | `25400001-4002-81c5-b46e-cf057c562025` / `25400002-...` / `25400003-...` |
| Prime power bank | A1340 @0x22c4698 | `00002215` | `22150001-4002-81C5-b46e-cf057c562025` / `22150002-4002-81c5-b46e-cf057c562025` / `22150003-4002-81c5-b46e-cf057c562025` |
| MI80 microinverter (BLE) | A5143 @0x22c4318 | `0000effe` | `016DF5DA-0000-1000-8000-00805F9B34FB` / `0000ef0a-0000-1000-8000-00805f9b34fb` / `0000ef0b-0000-1000-8000-00805f9b34fb` |
| legacy 0156F5DA-style | A17A0 @0x22c4940, A17A1 @0x22c48d0, A17A2 @0x22c4860, A1770 @0x22c49b0, A1780 @0x22c4a20 | `000017A0-...`, `000017A1-...`, `000017A2-...`, `00001770-...`, `00001780-...` (suffix `-0000-1000-8000-00805F9B34FB`) | service `0156F5DA-...` (A17A0), `0157F5DA-...` (A17A1), `0158F5DA-...` (A17A2), `0159F5DA-...` (A1770), `014BF5DA-...` (A1780); write and notify are the literals `7777` and `8888` |
| placeholder rows | A5150 @0x22600d8, A5450 @0x22c30d8, A5220 @0x22c3210, A5341 @0x22c3268 | `0000FF09` | service, write and notify all hold the short string `0000FF09` (no 128-bit UUID) |
| name strings | A5140 @0x22c3380, A5141 @0x22c3330 | the product name (`MI60 Microinverter`, `MI80 Microinverter`) | scan, service, write and notify all hold the product name string |

How to read the table. The `0000FF09` scan value is used by every ZX product and by the Prime power modules; the other families scan under their own 16-bit or 128-bit value. The 128-bit lowercase and uppercase forms of the ZX triple are two separate pool strings for the same UUID (A1790 stores the uppercase pair `[pp+0x97f8]` to `[pp+0x9808]`; UUID comparison is case-insensitive in the Bluetooth stack, so this is a spelling difference in the table, not a second profile). Two further places hold the scan UUID as a literal: `shelly_device.dart @0x36c0284` holds the full form `0000ff09-0000-1000-8000-00805f9b34fb` and `a1790_anker_device.dart @0x36c0278` holds `0000ff09`.

Which products the app scans for: `ankerProductForBleMap` (`product_model.dart @0x24e2ef0`) is keyed by product code and holds 52 of the 69 models: A17C2, A17X7, A17X7US, A17X8, A7320, A17C1, A17C3, A1340, A1780, A1770, A17A0 to A17A5, A1771, A17C0, A5143, A5101, A1781, A1780P, A1772, A1790, A1790P, A1753, A1754, A1755, A1761, A1762, A17B1, A17Y0, A91B2, A2345, A1722, A1723, A1725 to A1729, A17C5, A17E1, A17E2, AX170, A5190, A5191, AE111, AE113, AE103, AE1X0 and AE1R0. The 17 models not in that map are A5140, A5141, A1763, A5341, A5220, A5102, A5103, A5150, A5450, A25X7, A1782, A1783, A2687, A120J and the three Shelly models (SHEM3, SHEMP3, SHPPS); the map is built from the 52 `r2 = <model>` loads in the function body, so the list is exact for 3.24.3. The classification of products and the new 3.24.3 codes is on [../reference/enums.md](../reference/enums.md).

## Frame on BLE

Tag: asm-traced.

The BLE frame is the binary layer of [../mqtt/envelope.md](../mqtt/envelope.md#binary-layer) without the JSON wrapper: `ZXCommandTransformer._getNormalCommand` (`charging/communication/transformer/zx_command_transformer.dart @0x2273fec`) writes the `FF 09` marker, the 2-byte little-endian length, the constant `03`, a zero, one more header byte from the transformer, the 2-byte opcode, the payload and a trailing XOR byte; the TLV fields inside the payload are described there and on the per-product MQTT pages. The total length is payload + 9 + 1 (`add x0,x1,#9; add x3,x0,#1` @0x22742a8..0x22742ac). The checksum is an XOR over every byte that precedes it and is computed by `ZXCommandTransformer._getCheckSum` (`@0x22745f0`, loop `eor x4,x0,x1` @0x227463c), called at `@0x2274518` and stored in the last slot. Correction to audit row 14 and to the cell that cites it on [../mqtt/envelope.md](../mqtt/envelope.md#binary-layer): the `eor x3,x0,x1` at `@0x22744a4` is not the checksum, it is the encryption flag of the next section (it XORs the first opcode byte).

Two TLV scale facts that belong to the receive side of BLE frames: values are read little-endian (`CmdUtil.listToInt` cmd_util.dart @0x23c42dc: `and w2,w1,#0xff; lsl x3,x1,#3`, audit row 52) and signed 8-bit temperatures subtract 0x100 when the byte is at least 0x80 (`cmp x0,#0x80; sub x1,x0,#0x100` in the family parsers, audit row 57; for example `charging/ble/device/A17C1/a17c1_device_commands.dart` `parseDeviceAllInfo` @0x4865240). The scale factors 0.1 and 0.01 are loaded from the pool (`a17x8_device_commands.dart` `parseDeviceAllInfo` @0x3b65984 and @0x3b65a68, audit rows 53 and 54); the byte offset where the temperature is stored moved between versions (audit row 58, see [Since 3.18.0](#since-3180)).

## Opcode byte 0 flags

Tag: asm-traced.

The first byte of the 2-byte opcode carries transport flags: the response bit is in its low nibble, the encryption and fragment flags in its high nibble; the rest of the low nibble and the second byte are the opcode proper.

| bit pattern in byte 0 | meaning | evidence |
|---|---|---|
| `0x08` (low nibble bit 3) | response: the handshake map of [handshake.md](handshake.md#opcode-pairs) pairs each request opcode `00xx` with a response `08xx`, and `isResponseOrRequest` tests `(byte & 0x0F) >> 3 & 1` | `ZXCmdUtil.isResponseOrRequest` ak_cmd_util.dart @0x241fed8, audit row 15 |
| `0x40` (high nibble) | payload is encrypted | send: `r2 = 64` when the device flag and a key are present zx_command_transformer.dart @0x2274194, XOR into the first opcode byte @0x22744a4; receive: `and w1,w0,#0xf0; cmp w1,#0x40` in `PPSDeviceCommands.parseResponse` pps_device_commands.dart @0x241cbd0 |
| `0x80` (high nibble) | fragment: set by `splitPackageCmd` on every fragment (see below) | `eor x1,x2,#8` on the high nibble assemble_command_util.dart @0x2272880 |
| low nibble | opcode lookup key: `getOpcodeType` masks `and w1,w0,#0xf` before matching the opcode map | `ZXOpcodeTypeExtension.getOpcodeType` pps_device_commands.dart @0x2425f60 |

After reassembly `getTotalCmd` rebuilds byte 7 as `(b & 0x0F) ^ 0x40` (`AssembleCmdUtil.getTotalCmd` assemble_command_util.dart @0x4789ef0), that is the fragment bit is dropped and the encrypted bit is set, so a reassembled command always goes through the decrypt branch.

## Fragmentation

Tag: asm-traced.

A caller selects fragmented sending by passing a non-zero `mtu` argument to `sendCommandWithParam`: after the frame is built the controller tests that argument (`cbz x0` a17c1_device_controller.dart @0x226e3ec) and calls `AssembleCmdUtil.splitPackageCmd(command, mtu)` (`@0x226e3fc`) with the device field at offset 0xa3 as size (`LoadField r2 = r1->field_a3` @0x226e3f4). The number passed by the caller is not used as a size (the setter `setTacticsTime` passes the raw Smi 400, real 200, `@0x288b274`; FLOWS audit, doc line 41). The field at offset 0xa3 is written by the capability negotiation from tag `a2` ([handshake.md](handshake.md#capability-negotiation-response)). Each fragment is sent from a `Future.delayed` closure with the same 50 ms duration (Duration `[pp+0x25e70]`, 0xc350 microseconds, `@0x226e490`); the delays are all created in one loop, so they are not cumulative.

`splitPackageCmd` (`charging/ble_zx/base/assemble_command_util.dart @0x22721dc`):

| step | rule | evidence |
|---|---|---|
| chunk size | `mtu - 10 - 1`; when the size argument is 0 the chunk is exactly 200 | `sub x1,x0,#0xa; sub x2,x1,#1; cbnz x0 ...; mov x4,#200` @0x227226c..0x2272278, audit rows 45 to 47 |
| body | the command without its 9 header bytes and without the trailing XOR byte (`sublist(9, length-1)`) | `r2 = 9`, `sub x1,x2,#1` @0x2272514..0x227252c |
| fragment count | ceiling of body length divided by chunk size (`fdiv`, `fcvtps`) | @0x227254c..0x2272558 |
| index byte | one byte in front of each chunk: `(i + 1) << 4` XOR the fragment count, so the high nibble is the 1-based index and the low nibble the count | `lsl x1,x10,#4; eor x11,x3,x1` @0x2272618..0x227261c |
| header | the first 9 bytes of the original command are copied in front (`sublist(0, 9)`, `insertAll(0, ...)`); the length bytes are rewritten to chunk + 10 + 1 and byte 7 gets the 0x80 flag | `add x4,x2,#0xa` @0x2272810, `replaceRange` @0x2272914 and @0x2272974 |
| checksum | XOR over the new fragment, appended | loop `eor x6,x0,x2` @0x2272a30 |

Because the length field of a fragment is the chunk plus the 9-byte header, the index byte and the checksum, every fragment is exactly the size argument long (chunk + 11); with the default of 200 a fragment is a single 200-byte write. The count lives in one nibble, so at most 15 fragments can be indexed (arithmetic on the nibble width; the code does not test for it).

The receive side is `ZXCommandTransformer.validateCommand` (`zx_command_transformer.dart @0x4789138`), which calls `AssembleCmdUtil.saveOnePackage` (call at `@0x478932c`; the function is in `assemble_command_util.dart @0x4789810`): it keys the partial command by the hex string of bytes 7 and 8 (`sublist(7, 9)` @0x4789848..0x4789858), removes the index byte from the front (`removeAt(0)` @0x4789a0c) and reads the count from its low nibble and the index from its high nibble (`and w4,w0,#0xf` @0x4789a24; `asr x0,x1,#4`, `and w1,w0,#0xf` @0x4789a2c..0x4789a34), and `getTotalCmd` (`@0x4789b8c`) sorts the parts and concatenates them. The audit row 47 wording "MTU - 10" is corrected to MTU - 11 for the chunk (row 47 itself says so); row 45 (`sub #0xa`) is the first of the two subtractions.

## Payload encryption

Tag: asm-traced.

Encryption of the payload happens in `_getNormalCommand`, not in the GATT layer. The frame builder encrypts when the transformer's encrypted flag (offset 0x1f) is set and the key list of the transformer (offset 0x1b) is non-empty (`@0x22740d8..0x22740e0`, `@0x2274158..0x22741e4`). When `BleInfoHelper.getAesGcmTag` is true for that key and a further transformer flag (offset 0xb) is set, the encrypted flag and the GCM selector (offset 0x37) are both switched on (`@0x227411c..0x2274144`). With the GCM selector set the payload goes through `AesHelper.aesGcmEncrypt` (`ble_zx/helper/aes_helper.dart @0x2275194`, call `zx_command_transformer.dart @0x2274218`); otherwise through `AesHelper.encrypt` (`@0x2274988`, call `@0x2274244`). The receive side mirrors it in `PPSDeviceCommands.parseResponse`, which calls `AesHelper.decrypt` or `AesHelper.aesGcmDecrypt` (22 call sites each in `charging/command/pps_device_commands.dart`).

| scheme | implementation | parameters |
|---|---|---|
| AES-GCM (`aesGcmEncrypt` @0x2275194) | pointycastle `AESEngine` and `GCMBlockCipher` (`@0x2275234`, `@0x2275264`) | key from `BleInfoHelper.getAesKey(bleMac)`, nonce from `getAesIV(bleMac)`, MAC size 128 bits (64-bit unboxed field store `r0 = 128` @0x2275390, real 128), associated data is a fixed 16-element array built in code (`@0x22752b4`; role only, value not recorded) |
| AES-CBC (`encrypt` aes_helper.dart @0x2274988, `_aesEncrypt` @0x2274a80) | the `encrypt` package: `Key`, `IV`, `Encrypter`, `AES` with `AESMode.cbc` (`@0x2274ae4`..`@0x2274b78`) | key `getAesKey(bleMac)` or, when none is stored, `BleInfoHelper.defaultAESKey` (`ble_info_helper.dart @0x2275028`); the IV must be 16 bytes (error string `Initialization vector must be 16 bytes long`, `@0x2274d8c`) |

`BleInfoHelper` (`ble_zx/helper/ble_info_helper.dart`, singleton `@0x2275658`) keeps per-device maps keyed by the BLE MAC: the AES key (`setAesKey` @0x26323d0, `getAesKey` @0x227508c), the IV (`getAesIV` @0x22750e4), the encryption scheme (`setEncryptionScheme` @0x2425998, `getEncryptionScheme` @0x227513c), a GCM flag (`setAesGcmTag` @0x2632390, `getAesGcmTag` @0x2275600) and `isConfered` (`@0x26341b0`, true when a key is stored). `defaultAESKey` is the UTF-8 encoding of the first 16 characters of `BleInfoHelper.accountId()` (`substring(0, 16)`, raw 32 @0x2275050; `accountId` @0x226ee08). The negotiated key and IV are produced by [handshake.md](handshake.md); the app also hands them to the native kit after negotiation ([handshake.md](handshake.md#completion)).

## MTU

Tag: asm-traced.

There is one MTU value on the BLE side: the device-reported value from the capability negotiation, stored in the device object at offset 0xa3 (tag `a2` read with `listToInt` and stored zx_ble_confer.dart @0x2632cd4, logged with the text `能力协商成功-----mtu ----` @0x2632cf0) and passed to `splitPackageCmd`, which uses 200 when it is 0 (`mov x4,#200` assemble_command_util.dart @0x2272278, audit row 46). The overhead is 11 bytes per fragment (9 header, 1 index, 1 checksum), see above. `ReactiveBleManager._setMtu` (`reactive_ble_manager.dart @0x22179b4`) does not issue an MTU request: after cancelling a subscription it returns an already completed `Future<int>` whose value is the Smi raw 480 (`mov x2,#0x1e0` @0x2217a54), real 240; what consumes that value was not found. The 3.18.0 helper `BleInfoHelper.setmtuSize` no longer exists in 3.24.3 ([Since 3.18.0](#since-3180)). The OS-level MTU request and the concurrent-connection limits of the platforms are not in the Dart code (BUSINESS_RULES doc line 720).

## Timeouts and limits

Tag: asm-traced.

| what | value | evidence |
|---|---|---|
| connect timeout (legacy connect path only) | 30 seconds: Duration `[pp+0x29af0]` = 30,000,000 microseconds, text `Connection timeout (30s)` | `SimpleBleConnector._connectLegacyDevice` `simple_ble_connector.dart @0x43181c8`, text `@0x4318394`; BUSINESS_RULES doc lines 345 and 716 |
| command response wait | 5 seconds: default `delay` Duration `[pp+0x13850]` = 5,000,000 microseconds | `BleCommandController.sendCommand` (`charging/communication/command_controller/ble_command_controller.dart @0x226fb30`) default at `@0x226fc88`; BUSINESS_RULES doc line 345 (the old "30 s command timeout" is wrong) |
| delay before the connect command | 300 milliseconds: Duration `[pp+0x93f0]` = 0x493e0 microseconds, `Future.delayed` | `ZXBleConfer.sendConnectCommand` `zx_ble_confer.dart @0x2631fe0` |
| delay between fragments | 50 milliseconds, see [Fragmentation](#fragmentation) | `a17c1_device_controller.dart @0x226e490` |
| background disconnect | 30 minutes: Duration `[pp+0xd7e8]` = 1,800,000,000 microseconds | `charging/base/app_life_cycle_delegate.dart @0x2856970`; BUSINESS_RULES doc lines 348, 717 |

The 30-second timeout is attached only to the legacy path of `SimpleBleConnector`; `_connectNewDevice` (`simple_ble_connector.dart @0x4317f20`) has no timeout of its own in this function. The `A17X8` controller's `sendCommandWithParam` (`a17x8_device_controller.dart @0x24190c0`) has the Smi raw 30 (real 15) as `functionType`, not as a timeout (BUSINESS_RULES doc line 207).

## Connection routing and the WiFi exclusion rule

The app models the transport of one device as one value. Tag: asm-traced.

`AnkerDevice.updateStatus` (`base_service/device/anker_device.dart @0x22054c4`) writes a single `DeviceConnectionStatus` into the device (store to `field_cb`): `wifiConnected`, `wifiDisconnected`, `bleConnected`, `bleBusinessConnected`, `bleDisconnected`, `bleConnecting`, `disconnect`, `appUnable` or `unknown` (members and indices in [../reference/enums.md](../reference/enums.md#deviceconnectionstatus)). For the product codes that have a cloud path (the first chain of the function: A17C1, A17C2, A17C3, A17C5, A17C0, A17X7, A17X7US, A17X8, A1771, A1772, A1781, A1780P, A1790, A1790P, A7320, A17B1, A17A3 to A17A5, A5101, A5102, A5103, A5341, A5220, A5150, A5450, A2345, A91B2) it first sets `appUnable` when `isMQTTServerConnected` is false (`@0x2205c50`), then works through three tests in this order and stops at the first that holds: `wifiConnected` when a boolean device predicate (dispatch selector `0x2b337`, `@0x2205c90`) is true and the collection field at offset 0x87 answers the query with the pool string `"wifi"` (`@0x2205cbc`); `bleBusinessConnected` when `isBleBusinessConnected` is true and that field answers `"ble"` (`@0x2205d00`, `@0x2205d1c`); `bleConnected` when `isCurrentDeviceBleConnected` is true (`@0x2205d60`). The disconnected variants follow the same split (`@0x2205db8`, `@0x2205e18`). The WiFi test comes first and ends the chain, so a device that passes it is never given a BLE state. The same predicate chooses the route `/realProgressOTA` over `/parallelBleOta` in `settings/src/common/menu_controller/version_rollback_menu_controller.dart @0x2cd9b5c`. For the BLE-only codes (A1780, A17A0 to A17A2, A1770, A1340, A17Y0) the function sets `bleBusinessConnected`, `bleConnected` or `disconnect` and never a WiFi value (`@0x220611c`..`@0x2206164`); A5140, A5141 and A5143 end in `disconnect` (`@0x220626c`). `AnkerDevice.isBleAvailable` (`@0x36d2b48`) is true exactly when the status is `bleConnected` or `bleBusinessConnected`. For `IotDeviceAdapter` devices the product list `dualModePns` contains only `A5191` (`iot_device_adapter.dart @0x34af0f0`); for that product `IotDeviceAdapter.isBleAvailable` (`@0x36d2a98`) reads the BLE connect-state notifier instead (compare with `AkIotDeviceBleConnectState.bleBusinessConnected`, `@0x36d2b04`). So in the app a device is either in a WiFi state or in a BLE state, and a command is routed by that state (see [Stacks and send routing](#stacks-and-send-routing)).

What the asm does not show is the firmware behaviour. The rule "BLE is unavailable while the device is on WiFi" is the finding of the community BLE projects (the README of HaSolixBLE states that BLE and WiFi cannot be used at the same time on these devices; the project notes record the same observation for SolixBLE, AnkerSolixBLE and the maintainer of the upstream library, not re-verified here). It is kept here as an external statement, not a fact of this repository: Tag: untagged by design (no API fact). Do not present BLE as a live fallback when the cloud or WiFi path is down. Two code paths in 3.24.3 show that the app itself has a notion of both at once: the product list `dualModePns` above, and the parallel OTA page `WifiBleParallelOtaLogic` for A1780P (`charging/ui/page/device/a1780p/parallel_ota/wifi_ble_parallel_ota_logic.dart`, strings `WifiBleParallelOtaLogic BLE reconnect failed after 5 attempts, give up`); neither proves simultaneous telemetry, see [Known unknowns](#known-unknowns).

## ZX opcode names

Tag: asm-traced.

`PPSDeviceCommands.chargingOpcodeMap` (`charging/command/pps_device_commands.dart @0x2420104`) maps the wire opcode, written as a 4-digit hex string, to a `ZXOpcodeType` member for the charging products (the allocation holds 250 slots, so 125 entries). The key is `bytesToHexString` of a constant two-byte list, for example `[0x04, 0x05]` for `0405`; pool lists are real values. `commonOpcodeMap` (`@0x2422850`, 22 entries) is the handshake map and is on [handshake.md](handshake.md#opcode-pairs). The enum index is the `off_8` value of the pool object. Several opcodes are used by more than one member: `0842` is both `setAcCountDownTimeRes` and `setCarCountDownTimeRes`, `0206` is `setMiniChargeACRelaySwitchReq` and `setMiniChargeACRelaySwitchRes`, and `0037` is both `getMultiDevicesReq` and `getMultiDevicesRes`. The two maps overlap numerically with each other (`0021`, `0022`, `0023`, `0031`, `0032`, `0821`, `0822`, `0823`, `0831` appear in both with different meanings), so the same wire value means different things depending on the map in force.

Reading a row: the last column is the address of the map entry in `pps_device_commands.dart`.

| opcode | member | index | entry |
|---|---|---|---|
| `0022` | `scanWifiReq` | 19 | @0x2420148 |
| `0822` | `scanWifiRes` | 20 | @0x242018c |
| `0023` | `getWifiListReq` | 21 | @0x24201d0 |
| `0823` | `getWifiListRes` | 22 | @0x2420214 |
| `0024` | `connectWifiReq` | 24 | @0x2420258 |
| `0824` | `connectWifiRes` | 23 | @0x242029c |
| `0025` | `activateWifiReq` | 25 | @0x24202e0 |
| `0825` | `activateWifiRes` | 26 | @0x2420324 |
| `0035` | `exitConnectReq` | 27 | @0x2420368 |
| `0835` | `exitConnectRes` | 28 | @0x24203ac |
| `0400` | `postErrorInfoReq` | 29 | @0x24203f0 |
| `0401` | `postSwitchStateReq` | 31 | @0x2420434 |
| `0402` | `postWorkInfoReq` | 30 | @0x2420478 |
| `0403` | `postDeviceInfoReq` | 32 | @0x24204bc |
| `0404` | `postCountDownTimeReq` | 33 | @0x2420500 |
| `0426` | `postLinkageSystemErrorReq` | 34 | @0x2420544 |
| `0840` | `getAllDeviceInfoRes` | 37 | @0x2420588 |
| `0841` | `getAcCarCountDownTimeRes` | 39 | @0x24205cc |
| `0842` | `setAcCountDownTimeRes` | 41 | @0x2420610 |
| `0842` | `setCarCountDownTimeRes` | 43 | @0x2420654 |
| `0844` | `setAcChargePowerRes` | 45 | @0x2420698 |
| `0845` | `setDeviceWaitTimeRes` | 47 | @0x24206dc |
| `0846` | `setDeviceScreenTimeRes` | 49 | @0x2420720 |
| `0847` | `setInversionWaitTimeRes` | 51 | @0x2420764 |
| `0848` | `setMajorPkgRes` | 62 | @0x24207a8 |
| `0849` | `setMinorPkgRes` | 64 | @0x24207ec |
| `084a` | `setAcSwitchRes` | 66 | @0x2420830 |
| `084b` | `setCarSwitchRes` | 68 | @0x2420874 |
| `084c` | `setLcdLightRes` | 70 | @0x24208b8 |
| `084d` | `setAcFrequencyRes` | 72 | @0x24208fc |
| `084e` | `setEnergyModeRes` | 74 | @0x2420948 |
| `084f` | `setAmbientLightRes` | 76 | @0x242099c |
| `0850` | `setTempUnitRes` | 78 | @0x24209f0 |
| `0851` | `setResetRes` | 80 | @0x2420a44 |
| `0057` | `setDeviceUpdateEnergyReq` | 81 | @0x2420a98 |
| `0405` | `postDeviceAllInfoReq` | 82 | @0x2420aec |
| `0406` | `postUpgradeStateRes` | 100 | @0x2420b40 |
| `0061` | `getAllBMSSubBatteryInfoReq` | 83 | @0x2420b94 |
| `0861` | `getAllBMSSubBatteryInfoRes` | 84 | @0x2420be8 |
| `0409` | `postAllBMSMinorBatteryBTInfoReq` | 85 | @0x2420c3c |
| `040a` | `postAllBMSMinorBatteryWiFiInfoReq` | 86 | @0x2420c90 |
| `0410` | `postA17B2DeviceInfoWIFIReq` | 87 | @0x2420ce4 |
| `0411` | `postA17B2DeviceInfoBTReq` | 88 | @0x2420d38 |
| `0074` | `getA17B2DeviceInfoReq` | 89 | @0x2420d8c |
| `0874` | `getA17B2DeviceInfoRes` | 90 | @0x2420de0 |
| `005f` | `setBMSSubBatteryPowerSwitchReq` | 91 | @0x2420e34 |
| `085f` | `setBMSSubBatteryPowerSwitchRes` | 92 | @0x2420e88 |
| `0460` | `getDeviceSelfTestRes` | 93 | @0x2420edc |
| `0060` | `setBMSSubBatteryLightSwitchReq` | 94 | @0x2420f30 |
| `0860` | `setBMSSubBatteryLightSwitchRes` | 95 | @0x2420f84 |
| `085e` | `setDischargeTimeRes` | 60 | @0x2420fd8 |
| `040f` | `postSubBatteryErrorInfoReq` | 96 | @0x242102c |
| `085e` | `setSuperChargeRes` | 99 | @0x2421080 |
| `005e` | `setSuperChargeReq` | 98 | @0x24210d4 |
| `040e` | `getMicroInverterReq` | 59 | @0x2421128 |
| `0406` | `postUpgradeStateReq` | 101 | @0x242117c |
| `002e` | `sendOtaSubPackageReq` | 58 | @0x24211d0 |
| `0069` | `deviceFactorySettingRes` | 103 | @0x2421224 |
| `0869` | `deviceFactorySettingReq` | 104 | @0x2421278 |
| `006a` | `deviceFactorySettingClearRes` | 105 | @0x24212cc |
| `086a` | `deviceFactorySettingClearReq` | 106 | @0x2421320 |
| `0061` | `setA17b1CommandReq` | 107 | @0x2421374 |
| `0861` | `setA17b1CommandRes` | 108 | @0x24213c8 |
| `0500` | `postA17b1DeviceInfoReq` | 109 | @0x242141c |
| `0501` | `postA17b1SelfCheckReq` | 110 | @0x2421470 |
| `0503` | `postDeviceListReq` | 111 | @0x24214c4 |
| `0604` | `postGetUpdateListReq` | 112 | @0x2421518 |
| `0601` | `postA1790DeviceInfoReq` | 113 | @0x242156c |
| `0602` | `setA1790CommandReq` | 114 | @0x24215c0 |
| `0031` | `getScanBluetoothDeviceReq` | 115 | @0x2421614 |
| `0831` | `getScanBluetoothDeviceRes` | 116 | @0x2421668 |
| `0032` | `getBindBluetoothDeviceReq` | 117 | @0x24216bc |
| `0832` | `getBindBluetoothDeviceRes` | 118 | @0x2421710 |
| `0033` | `getUnBindBluetoothDeviceReq` | 119 | @0x2421764 |
| `0833` | `getUnBindBluetoothDeviceRes` | 120 | @0x24217b8 |
| `0021` | `getModuleInfoReq` | 121 | @0x242180c |
| `0821` | `getModuleInfoRes` | 122 | @0x2421860 |
| `0200` | `getMiniChargeAllDeviceInfoReq` | 123 | @0x24218b4 |
| `0a00` | `getMiniChargeAllDeviceInfoRes` | 124 | @0x2421908 |
| `0201` | `setMiniChargeResetReq` | 125 | @0x242195c |
| `0a01` | `setMiniChargeResetRes` | 126 | @0x24219b0 |
| `0202` | `getMiniChargeScreensaverReq` | 127 | @0x2421a04 |
| `0a02` | `getMiniChargeScreensaverRes` | 128 | @0x2421a58 |
| `0203` | `setMiniChargeScreenTimeoutReq` | 129 | @0x2421aac |
| `0a03` | `setMiniChargeScreenTimeoutRes` | 130 | @0x2421b00 |
| `0204` | `setMiniChargeScreenBrightnessReq` | 131 | @0x2421b54 |
| `0a04` | `setMiniChargeScreenBrightnessRes` | 132 | @0x2421ba8 |
| `0205` | `setMiniChargeScreensaverReq` | 133 | @0x2421bfc |
| `0a05` | `setMiniChargeScreensaverRes` | 134 | @0x2421c50 |
| `0206` | `setMiniChargeACRelaySwitchReq` | 135 | @0x2421ca4 |
| `0206` | `setMiniChargeACRelaySwitchRes` | 136 | @0x2421cf8 |
| `0207` | `setMiniChargeACRelaySwitchReq` | 135 | @0x2421d4c |
| `0a07` | `setMiniChargeACRelaySwitchRes` | 136 | @0x2421da0 |
| `0065` | `requestMcuLogUploadReq` | 140 | @0x2421df4 |
| `0865` | `requestMcuLogUploadRes` | 141 | @0x2421e48 |
| `0066` | `mcuLogUploadReq` | 142 | @0x2421e9c |
| `0866` | `mcuLogUploadRes` | 143 | @0x2421ef0 |
| `0067` | `bleOtaProgressReq` | 144 | @0x2421f44 |
| `0867` | `bleOtaProgressRes` | 145 | @0x2421f98 |
| `0030` | `getZXOTAStateReq` | 56 | @0x2421fec |
| `0830` | `getZXOTAStateRes` | 57 | @0x2422040 |
| `0076` | `carPortSavingReq` | 146 | @0x2422094 |
| `0876` | `carPortSavingRes` | 147 | @0x24220e8 |
| `0077` | `acOutputSmartReq` | 148 | @0x242213c |
| `0877` | `acOutputSmartRes` | 149 | @0x2422190 |
| `007a` | `setRelaySwitchReq` | 150 | @0x24221e4 |
| `087a` | `setRelaySwitchRes` | 151 | @0x2422238 |
| `007c` | `setTimingReq` | 152 | @0x242228c |
| `087c` | `setTimingRes` | 153 | @0x24222e0 |
| `007d` | `getTimingReq` | 154 | @0x2422334 |
| `087d` | `getTimingRes` | 155 | @0x2422388 |
| `007e` | `setCountdownReq` | 156 | @0x24223dc |
| `087e` | `setCountdownRes` | 157 | @0x2422430 |
| `007f` | `getCountdownReq` | 158 | @0x2422484 |
| `087f` | `getCountdownRes` | 159 | @0x24224d8 |
| `007b` | `setLocationLightReq` | 160 | @0x242252c |
| `087b` | `setLocationLightRes` | 161 | @0x2422580 |
| `0490` | `postPbFormatBackupMindData` | 35 | @0x24225d4 |
| `0036` | `setMultiDevicesReq` | 162 | @0x2422628 |
| `0836` | `setMultiDevicesRes` | 163 | @0x242267c |
| `0037` | `getMultiDevicesReq` | 164 | @0x24226d0 |
| `0037` | `getMultiDevicesRes` | 165 | @0x2422724 |
| `0089` | `getOTAStateReq` | 166 | @0x2422778 |
| `0889` | `getOTAStateRes` | 167 | @0x24227cc |
| `0489` | `upUpgradeCondition` | 168 | @0x2422820 |

The command payloads for these opcodes are owned by the `mqtt/<pn>.md` pages ([../mqtt/README.md](../mqtt/README.md)), indexed per upstream constant on [../mqtt/upstream_commands.md](../mqtt/upstream_commands.md).

## Since 3.18.0

Tag: asm-traced (3.24.3 side).

- The ZX transport code is structurally unchanged: the same files and the same number of functions in `ble_zx/helper/zx_ble_confer.dart`, `ble_confer/*`, `helper/aes_helper.dart` and `base/assemble_command_util.dart`; the chunk size rule and the default of 200 are at the same logical sites (3.18.0 address 0x19adebc, audit row 46).
- `BleInfoHelper` lost `setAesIV` and `setmtuSize`: 20 functions in 3.18.0, 18 in 3.24.3. In 3.18.0 the ECDH conferers called `BleInfoHelper.setAesIV` right after `setAesKey` (`secure_ecdh_confer.dart` at 3.18.0 address 0x36460e8, `ecdh_confer.dart` at 0x3644674); in 3.24.3 the same position is a dispatch-table call that Blutter labels `registerDeviceInfoListener` (`secure_ecdh_confer.dart @0x484cdf0`). The one call of `setmtuSize` in 3.18.0 (`pps_device_commands.dart` at 3.18.0 address 0x1eac488) has no counterpart.
- The device-class files `device/anker_device.dart`, `anker_device_delegate.dart`, `ble_feature.dart`, `ble_ota_field.dart`, `wifi_featrue.dart` and `ble_connection_state.dart` moved out of `charging/ble` (the first five now live under `base_service/device/`); no BLE device class directory is new.
- The opcode sets referenced by the device classes changed only slightly: the opcode `00f0` is gone from `a172x_anker_device.dart` and `a5101_anker_device.dart`; the opcodes `0031`, `0065`, `0066` (module and MCU log upload) are gone from the A172X and A17A3 controllers and `0031`, `0057`, `0066` from the A17X8 controller; the A1771 controller gained `0048`, the A1790 controller `007a`, and the A2345 controller `021d` and `0a1d`.
- ProductModel: six new models in 3.24.3 (A17E2, AE103, AE111, AE113, AE1R0, AE1X0), two new empty string fields on every model, and the service/write/notify fields of A5140, A5141, A5150, A5220, A5341 and A5450 went from empty strings to the placeholder values in the table above.
- The byte offset used by the family parsers for the temperature field is 787 in 3.24.3 and 775 in 3.18.0 (audit row 58).

## Known unknowns

Tag: untagged by design (no API fact).

- Which of the stacks (SDK handler or the `Uuid.parse` characteristic setters of `ReactiveBleManager`) carries the traffic for each product, and what makes `_isLegacyDevice` true.
- The meaning of the third header byte written from transformer `field_23` (byte 6 of the frame, `0F` in captures, audit row 6) and of the device string at offset 0x87 that selects "wifi" or "ble" in `updateStatus` (who sets it).
- The consumer of the Smi 240 that `ReactiveBleManager._setMtu` returns.
- Whether fragmentation is used by products other than the A17C1 family: only `A17C1DeviceController.sendCommandWithParam` calls `splitPackageCmd`; the other controllers were not checked for their own copy of the logic.
- The curve and key derivation of the native ECDH are not visible in Dart (see [handshake.md](handshake.md#known-unknowns)).
- Firmware behaviour for simultaneous BLE and WiFi (`dualModePns`, the A1780P parallel OTA). No device test is recorded in this repository.
- Whether the A5101 family uses the same binary layer: its commands go through the three opcode classes in `charging/ble/device/A5101/opcode/` ([a5101.md](a5101.md)).

BLE is unavailable while the device is on WiFi; see `ble/protocol.md`.
