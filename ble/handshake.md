> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# BLE handshake

This page owns the negotiation that runs between the app and a Solix or Prime device after the GATT connection is up: the message sequence, the opcodes, what the capability response carries, which of three negotiation variants the app picks, and how the AES key and IV are derived. Frame layout and fragmentation are on [protocol.md](protocol.md); the cloud-side key exchange is on [../api/encryption.md](../api/encryption.md) and is compared with this one at the end.

The short answer to the question "Dart or native?": the elliptic-curve step is not done in Dart. The conferers call two methods of the `encryption` platform plugin, `getClientPublicKey` and `computeEcdhWithPublicKey` (channel methods in `encryption/encryption_method_channel.dart @0x2faf454` and `@0x484b8b4`); the plugin returns the public key text and the shared secret as hex strings. Dart then cuts the secret into key and IV and runs the AES step itself. The `pointycastle` package is in the app and contains the secp256r1 curve class, but nothing outside `pointycastle/` references any EC domain, key generator or agreement class; the only pointycastle classes the BLE code uses are `AESEngine` and `GCMBlockCipher` ([protocol.md](protocol.md#payload-encryption)). No key material and no preset constants are written on this page; where the app embeds a constant its role and pool or code address are given.

## Contents

1. [Two implementations](#two-implementations)
1. [Which implementation runs for a product](#which-implementation-runs-for-a-product)
1. [Stage machine of ZXBleConfer](#stage-machine-of-zxbleconfer)
1. [Opcode pairs](#opcode-pairs)
1. [Capability negotiation response](#capability-negotiation-response)
1. [The three conferers](#the-three-conferers)
1. [Key derivation](#key-derivation)
1. [Built-in initial key](#built-in-initial-key)
1. [Completion](#completion)
1. [Authentication status](#authentication-status)
1. [Comparison with the cloud key exchange](#comparison-with-the-cloud-key-exchange)
1. [Earlier claims](#earlier-claims)
1. [Since 3.18.0](#since-3180)
1. [Known unknowns](#known-unknowns)

## Two implementations

Tag: asm-traced.

There are two places that finish a negotiation and they hand the result to each other.

- Dart: `ZXBleConfer` (`charging/ble_zx/helper/zx_ble_confer.dart`) drives the stages and delegates the key exchange to one of three conferer classes. When the conferer succeeds, `ZXBleConfer` pushes the key and IV to the native kit with the channel methods `akiot.device.set_device_encrypt_key` and `akiot.device.set_device_negotiated` ([Completion](#completion)).
- Native kit: `SdkBleDeviceConnectorImpl.onMessageDispatch` (`charging/ble/sdk_handler/sdk_ble_device_connector.dart @0x2855c8c`) receives kit messages (message id 6000, an unboxed compare at `@0x2855cb0`) whose map has the keys `bleMac`, `data`, `type` and `capability`. For the message with the log text `type=5` the map also carries `encryptKey`, `encryptIv`, `encryptType` and `encryptCapability`; the handler stores the key (`BleInfoHelper.setAesKey` `@0x28562a0`), the IV (`@0x28562cc`) and the scheme (`setEncryptionScheme` `@0x2856328`), and sets the GCM flag when `encryptCapability` is 1 (`cmp w0,#2` against a tagged map value `@0x2856390`, `setAesGcmTag` `@0x28563a0`; the log text is `cipher mode resolved, cap:1, gcm:true`).

Which product goes through which implementation is decided by the product code and the device class, see [Which implementation runs for a product](#which-implementation-runs-for-a-product). The rest of this page describes the Dart implementation, which is the one with Dart-visible stages.

## Which implementation runs for a product

Tag: asm-traced.

App side only: what the kit or the device does after the app has handed over is not visible in Dart. Class ids below are plain integers from the `class id` lines of the asm headers (not Smis); the product-code counts are list lengths.

The handler is chosen per call. `BleHandler.startScanWithConnect` (`charging/ble/ble_handler.dart @0x23badac`) calls `BleHandler._getCurrentImpl` (`@0x23baee4`, function `@0x23bb144`). That function reads the product code of the device (dispatch-table getter `GDT[cid+0x2b43b]`, `@0x23bb174`; it is the same getter that `BleHandlerImpl1._isA5101Pn` compares with the strings `A5101`, `A5341`, `A5102` and `A5103`, `ble_handler_impl_1.dart @0x28574d4`) and passes it to `IotAnkerDeviceConfig.isSdkSupport` (`base_service/util/iot_device_config.dart @0x23bb228`). The result of `tbnz w0,#4` at `@0x23bb190` branches on FALSE: true returns `BleHandlerImpl2` (`_impl2`, `@0x23bb1d8`), false returns `BleHandlerImpl1` (`_impl1`, `@0x23bb208`); the true branch first calls `BleHandlerImpl1.clearTimer` (`@0x23bb1bc`) and then returns `_impl2`. `isSdkSupport` is `keys.contains(productCode)` over the static map `IotAnkerDeviceConfig._configurations` (`@0x23bb248` to `@0x23bb29c`); the map is empty at creation (`@0x220bfd0`) and `IotAnkerDeviceConfig.register` (`@0x4544808`, stores under `field_7` of the built config) is its only writer. Most modules register with a product-code literal that their config builder stores in `field_b` (for example `AE1X0` in `third_device/src/module/ae1x0/ae1x0_module.dart`, load `@0x45df150`, store `@0x45df158`, `register` call `@0x45df200`).

The keys registered in 3.24.3 are 34 literals (AE100, AS200, A7320, A5191, AX170, A17E1, A110W, A110Y, A1115, A121D, A1113, A1504, A17E2, AE103, AE111, AE113, AS220, AS510, AS520, AS521, AE1R0, AE1X0, A1903, A1341, A110A, A110B, A110G, ECOIR, A1785, A1783, A1765, AS100, A1763, A1782) and three codes that the modules `a2687/module.dart`, `a2687/module_a120j.dart` and `a25x7/module.dart` take from their product models (`a2687Model`, `a120jModel`, `a25x7Model`). Registration call sites for the codes that have a BLE page: A17E1 `micro_hes/src/module.dart @0x45b757c` (also `ats_ax170/src/ats_ax170/ax170_module.dart @0x458a050`), A17E2 `@0x45b7808`, AE103 `@0x45b7a9c`, AE111 `@0x45b7d38`, AE113 `@0x45b7fdc`, AE1X0 `@0x45df200`, AE1R0 `third_device/src/module/ae1r0/ae1r0_module.dart @0x45de564`, A5191 `ev_charger/src/ev_charger/module.dart @0x45aafe8`.

- Registered code: `BleHandlerImpl2`. Its file `charging/ble/ble_handler_impl_2.dart` has no reference to `ZXBleConfer` or to a conferer class; it handles kit messages (`onMessageDispatch`, log text `BleHandler onMessageDispatch _startConnectStateListener` `@0x48051e8`). The only calls of `startZXBleConfer` in the whole asm are `ble_handler_impl_1.dart @0x4196dec`, `charging/ui/page/device/connect/zx_connect_ble/zx_connect_ble_logic.dart @0x417866c`, `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart @0x26319f8` and `charging/ui/page/device/anker_ota/a17y0_ble_ota/a17y0connect_logic.dart @0x41779bc`. For these codes the negotiation result reaches the app as the `type=5` kit message ([Two implementations](#two-implementations)); what the kit does to produce it happens in the native plugin and is not in the Dart asm. The pairing screen `zx_connect_ble_logic.dart` calls `startZXBleConfer` without an `isSdkSupport` test (its own call, `@0x417866c`); whether it is reached for a registered code was not traced.
- Any other code: `BleHandlerImpl1`. Its `onBleConnect` (`@0x419636c`) calls `_authDevice` (`@0x41964b0`, call `@0x4196400`), which calls `ZXBleConfer.startZXBleConfer` (`@0x4196dec`) with the named arguments `success`, `fail`, `userAuthentication` and `needBind`. `needBind` is the negation of `_isA5101Pn`: the code `A5101`, `A5341`, `A5102` or `A5103` gives `needBind = false` (`@0x4196d80`), every other code `true` (`@0x4196d88`). The bind-account stage of [The three conferers](#the-three-conferers) is the stage that this flag gates.
- The gate in `ZXBleConfer.sendConnectCommand` (`zx_ble_confer.dart @0x2631f3c`): the 300-millisecond delay and the start-connect call run only when the class id of `device` is 8442, in 8449 to 8451, or in 8459 to 8506 (compares `@0x2631fa4`, `@0x2631fb4` to `@0x2631fbc`, `@0x2631fc0` to `@0x2631fc8`); otherwise the function returns at `@0x263201c` without sending a request and without calling `fail`. These ids are exactly the device classes whose `extends` line contains `ZXBleFeature` (`IotAnkerDevice` 8442; `A1340AnkerDevice` 8449; `A5101AnkerDevice` 8451; `ShellyDevice` 8459 and its two subclasses; every class from `A17Y0AnkerDevice` 8462 to `A1722AnkerDevice` 8506). The product device classes outside the ids have no `ZXBleFeature` in their `extends` line: `A5150AnkerDevice` 8436, `A17B2AnkerDevice` 8437, `A17A0AnkerDevice` 8444 with `A17A2AnkerDevice` 8445 and `A17A1AnkerDevice` 8446, `A5140AnkerDevice` 8453 with `A5143AnkerDevice` 8454 and `A5141AnkerDevice` 8455, `A1780AnkerDevice` 8456 and `A1770AnkerDevice` 8457. For these ten classes the Dart conferers send no start-connect request, so they never begin a ZX negotiation from the app side.

Per product, app side: the codes of [a17e2.md](a17e2.md) and [ae1x0.md](ae1x0.md) are registered (kit path); A1770, A1780, A17A0 to A17A2, A17B2, A5140, A5141, A5143 (A5142 has no device class in the asm) and A5150 pass through `BleHandlerImpl1` but start no ZX handshake; all other products with a page under `ble/` pass through `BleHandlerImpl1` and start the Dart conferer. Which of the three conferers then runs is not a product property: [Capability negotiation response](#capability-negotiation-response).

## Stage machine of ZXBleConfer

Tag: asm-traced.

`ZXBleConfer.startZXBleConfer` (`zx_ble_confer.dart @0x2631a2c`, log text `开始握手协商` at `@0x2631ce8`) receives the device and the callbacks `success`, `fail` and `progress` plus the flags `getDeviceInfo`, `needBind`, `userAuthentication` and `retryCount`. It resets the previous state (`disposeResource` `@0x2631e08`), subscribes to the device's response stream (`listen` `@0x2631eb0`), installs the built-in initial key when the device flag at offset 0x3f is set (`_setInitialKeyForSecure`, `@0x2631f18`, see [Built-in initial key](#built-in-initial-key)) and calls `sendConnectCommand` (`@0x2631f3c`). That function waits 300 milliseconds (`Future.delayed`, Duration `[pp+0x93f0]`, `@0x2631fe0`) and then calls the device's start-connect method (log text `开始连接设备`, `@0x2632068`).

`ZXBleConfer.parseResponseData` (`@0x2632694`) calls `PPSDeviceCommands.parseResponse` (`@0x2632784`) for every notification. The result is a map with the keys `FEATURE_OPCODE_KEY` (the `ZXOpcodeType`), `BLE_CMD_STATUS_KEY` (a `BleCmdStatus`) and `PAYLOAD_KEY`; the handler then works through these cases in order.

| stage | waits for | on success | on failure |
|---|---|---|---|
| connect | `startConnectRes` (`@0x2632928`..`@0x26329a0`, response opcode in [Opcode pairs](#opcode-pairs)) with `BleCmdStatus.success` | log `连接成功` (`@0x26329ac`), progress callback, then the capability stage | status other than success: if `retryCount` (offset 0x13) is above 0 it is decremented and `sendConnectCommand` runs again (`@0x2632890`..`@0x26328a8`); otherwise the fail callback runs and `clearAction` (`@0x26328dc`) |
| capability negotiation | `capabilityNegotiationRes` (`@0x2632b04`) with `BleCmdStatus.success` (`@0x2632b60`) | log `能力协商` (`@0x2632aa8`), parse the payload ([next section](#capability-negotiation-response)), choose and create the conferer, start it (`@0x26336a4`) | not distinguished here: the case is skipped |
| key exchange and authentication | the conferer, see [The three conferers](#the-three-conferers) | the conferer's last stage sets `AnkerConnectState.connectDone` | the fail callback; the conferer's own `clearAction` |
| completion | the conferer's success callback | push key and IV to the native kit ([Completion](#completion)) | key or IV missing: the push is skipped with a warning |

Before the conferer is started the code logs the scheme stored for the device with an error-level log (`aes getEncryptionScheme [` `@0x2633504`..`@0x26335c8`, text `NULL` when none is stored, `@0x263357c`), and it copies two of its own fields into the conferer (`field_3b` and `field_3f` of the conferer from `field_1b` and `field_1f`, `@0x2633470`..`@0x2633488`: the `getDeviceInfo` and `needBind` flags).

## Opcode pairs

Tag: asm-traced.

`PPSDeviceCommands.commonOpcodeMap` (`charging/command/pps_device_commands.dart @0x2422850`; the allocation holds 88 raw slots, so 22 entries) maps the handshake opcodes to `ZXOpcodeType` members. Keys are `bytesToHexString` of constant two-byte lists (pool lists are real values). Every request `00xx` has a response `08xx` (flag bit 3 of the first byte, [protocol.md](protocol.md#opcode-byte-0-flags)); the device classes expose one method per request: `startConnect` `0001`, `disconnectBle` `0002`, `capabilitiesNegotiation` `0003`, `setCapability` `0005`, `getPublicKey` `0021`, `getAESKey` `0022`, `bindUserId` `0023`, `userSecureInteraction` `0027`, `getDeviceBasicInfo` `0029` (for example `charging/ble/device/A17C1/a17c1_anker_device.dart`; the same set is referenced by every ZX device class, see the per-product pages). The index column is the `ZXOpcodeType` enum index (`off_8` of the pool object).

| opcode | member | index | entry |
|---|---|---|---|
| `0001` | `startConnectReq` | 0 | @0x2422894 |
| `0801` | `startConnectRes` | 1 | @0x24228d8 |
| `0002` | `startDisconnectReq` | 2 | @0x242291c |
| `0802` | `startDisconnectRes` | 3 | @0x2422960 |
| `0003` | `capabilityNegotiationReq` | 4 | @0x24229a4 |
| `0803` | `capabilityNegotiationRes` | 5 | @0x24229e8 |
| `0004` | `configureCapabilityReq` | 6 | @0x2422a2c |
| `0005` | `setCapabilityReq` | 7 | @0x2422a70 |
| `0805` | `setCapabilityRes` | 8 | @0x2422ab4 |
| `0027` | `getAuthenticationReq` | 13 | @0x2422af8 |
| `0827` | `getAuthenticationRes` | 14 | @0x2422b3c |
| `0029` | `getDeviceInfoReq` | 9 | @0x2422b80 |
| `0829` | `getDeviceInfoRes` | 10 | @0x2422bc4 |
| `0022` | `getAesKeyReq` | 11 | @0x2422c08 |
| `0822` | `getAesKeyRes` | 12 | @0x2422c4c |
| `0023` | `bindUserIdReq` | 15 | @0x2422c90 |
| `0823` | `bindUserIdRes` | 16 | @0x2422cd4 |
| `0021` | `getPublicKeyReq` | 17 | @0x2422d18 |
| `0821` | `getPublicKeyRes` | 18 | @0x2422d5c |
| `0031` | `requestModuleLogUploadReq` | 137 | @0x2422da0 |
| `0831` | `requestModuleLogUploadRes` | 138 | @0x2422de4 |
| `0032` | `moduleLogUploadRes` | 139 | @0x2422e28 |

`0004` is not the opcode argument of any send in the asm: its two-byte list `[0, 0x4]` occurs as an entry key of `commonOpcodeMap` (`@0x24229f4`, member `@0x2422a2c`), in the A5101 opcode and data-code maps (`A5101/opcode/zx_opcode_0x01.dart @0x23c6c8c`, `A5101/a5101_commands.dart @0x3b8950c` and `@0x3b8b814`), as the list stored into `SetList` objects of the A5101 WiFi screen (`ui/page/device/a5101/setting/change_wifi_and_password/a5101_ble_logic.dart @0x28eac30`, `@0x3ec01e4`, `@0x42f3f38`) and in a map of `charging/tcp/tcp_data_code.dart @0x419bc90`. `0031` and `0032` are sent, but not by a `ble/<pn>.md` device class: the A17C0 accessory screens pass them to the controller's `sendCommandWithParam` (`ui/page/device/a17c0/a17c0accessory/add_accessory/a17c0add_accessory_logic.dart @0x27488dc` for `0031`, `.../bind_accessory/a17c0bind_accessory_logic.dart @0x344c980` for `0032`); in the charging map they are `getScanBluetoothDeviceReq` and `getBindBluetoothDeviceReq` ([protocol.md](protocol.md#zx-opcode-names)). The names `requestModuleLogUploadReq` and `moduleLogUploadRes` belong to the common map of this page only, so the module-log reading of `0031` and `0032` applies to the response parser that uses that map and not to these two sends. The charging products' own map (`chargingOpcodeMap`) reuses `0022` and `0023` for `scanWifiReq` and `getWifiListReq`; see [protocol.md](protocol.md#zx-opcode-names).

## Capability negotiation response

Tag: asm-traced.

`PPSDeviceCommands.parseCapabilitiesNegotiationResponse` (`@0x2425398`, called from `_parsePayloadData` `@0x241cf54`) turns the payload of `capabilityNegotiationRes` into a map keyed by the synthetic tag numbers 0xA0 to 0xA6. The payload is first decrypted when the frame's encrypted flag is set: `AesHelper.aesGcmDecrypt` when the device flag at offset 0x3f is true (`@0x24254a8`), otherwise `AesHelper.decrypt` (`@0x24254c0`). Then fixed byte positions are read; a position is read only when the payload is long enough (the compares are unboxed list lengths).

| key | payload position | needs length | used for | evidence |
|---|---|---|---|---|
| key `a0` | byte 0 | 8 | stored in the map; no reader found in `ZXBleConfer` | `cmp x2,#8` `@0x24254f8`, `r1 = 160` `@0x2425504` |
| key `a1` | byte 3 | 8 | the scheme: `BleInfoHelper.setEncryptionScheme(bleMac, byte 3)` (`pps_device_commands.dart @0x2425614`); the CBC path requires the value 2 (`cmp w0,#4` against a tagged scheme `aes_helper.dart @0x22749e4` and `@0x23c514c`), any other value makes `AesHelper.encrypt` and `decrypt` return an empty list (`@0x22749f4`) | `pps_device_commands.dart`: `r1 = 161` `@0x242555c`, index 3 `@0x2425574` |
| key `a2` | bytes 6 and 7 (`sublist(6, 8)`) | 8 | the MTU: read with `listToInt` and stored at device offset 0xa3 (`zx_ble_confer.dart @0x2632cd4`); [protocol.md](protocol.md#mtu) | `r1 = 162` `pps_device_commands.dart @0x2425638`; `r1 = 162` `zx_ble_confer.dart @0x2632bf0` |
| key `a3` | byte 10 | 11 | bit 6 (`and w1,w2,#0x40; asr x4,x1,#6`) is the selector `S` below | `cmp x2,#0xb` `@0x2425690`, `r1 = 163` `@0x242569c`; reader `@0x2632dfc`, mask `@0x2632fc4` |
| key `a4` | byte 13 | 14 | compared with 1; the result is stored as a boolean at device offset 299 (0x12b) | `cmp x2,#0xe` `@0x24256fc`; reader `@0x263331c`, store `@0x26333f4` |
| key `a5` | byte 16 | 17 | stored at device offset 0x43 (only read when the device flag 0x3f is set); later echoed as `authenticationType` in the set-capability request | `cmp x2,#0x11` `@0x2425768`; reader `@0x2632f30`, store `@0x2632fac` |
| key `a6` | byte 19 | 20 | bit 6 is the selector `E` below | `cmp x2,#0x14` `@0x24257d4`; reader `@0x2633010`, mask `@0x2633084` |

The positions step by 3 (0, 3, 6), by 4 over the two-byte MTU and by 3 afterwards, so the payload is a sequence of small records; the record format is not decoded and the first value sits at byte 0. On the Dart side the keys behave like TLV tags `a0` to `a6` (the reader calls `indexString` with 160 to 166), which is why the old documents describe the response in tag terms.

Choosing the conferer. `S` is bit 6 of `a3`, `E` is bit 6 of `a6` (0 when `a6` is absent), `F` is the device flag at offset 0x3f. `ZXBleConfer` logs `设备广播的数据------secureModel: <cloud value>--encryptType: <S>---<F>` (`zx_ble_confer.dart @0x2633114`), where the cloud value is `HomePageUtilImpl.getCloudEncryptModel(productCode)` (`zx_ble_confer.dart @0x26330fc`; the function reads `getSecureInfoByPn(pn)["model"]`, default -1, `home_page_util_impl.dart @0x24e2560`). The cloud value is only logged; the branches test `S` and `E`.

| F | S | E | conferer | evidence |
|---|---|---|---|---|
| any | tag `a3` absent from the payload | any | `AesConferV1` | `containsKey` result tested with `tbnz` `zx_ble_confer.dart @0x2632e34`, jump to the constructor `@0x26332e4` |
| true | 1 | any | `SecureEcdhConfer` | `cmp x0,#1` `@0x2633190`, constructor `@0x26331ac` |
| true | 0 | 1 | `SecureEcdhConfer` | `lsl x2,x1,#1; cmp w2,#2` `@0x26331a0` |
| true | 0 | 0 | `AesConferV1` | `@0x2633228` |
| false | 1 | any | `EcdhConfer` | `cmp x0,#1` `@0x2633264`, constructor `@0x263326c` |
| false | 0 | any | `AesConferV1` | `@0x26332a4` |

The compiled code also contains an `EcdhConfer` constructor in the `F` true branch (`@0x26331f0`) that tests the same value `S` again after the first compare already selected `SecureEcdhConfer`; that arm cannot be reached. After the choice the conferer gets the constant 5 in its first field (`@0x2633434`; the field's meaning is not decoded).

## The three conferers

Tag: asm-traced.

All three extend `BleConfer` (`charging/ble_zx/ble_confer/ble_confer.dart`), listen to the device's responses and call `parseResponseData`; each handler compares the opcode with a `ZXOpcodeType` instance and the status with `BleCmdStatus.success`. The request that provokes a response is the one the common map pairs with it ([Opcode pairs](#opcode-pairs)). Log texts are Chinese pool strings; English glosses are given. `d` is the connected device.

| stage | `SecureEcdhConfer` (AES-GCM) | `EcdhConfer` (AES-CBC) | `AesConferV1` (device-supplied key) |
|---|---|---|---|
| start | log `获取基本信息` "get basic info" (`secure_ecdh_confer.dart @0x484bdb8`) | `startConfer` `ecdh_confer.dart @0x4849ff4` | log `获取设备数据` "get device data" (`aes_confer_v1.dart @0x4848804`) |
| device info (`getDeviceInfoRes`) | `@0x484c208`; reads tags `a4` (serial number) and `a5` (MAC), replaces `d.deviceSn` and `d.bleMac` when the serial is empty (`@0x484c3e4`..`@0x484c5e8`) | `@0x484a700`; same reads | `@0x4848db4`; same reads |
| set capability (`setCapabilityRes`) | request payload: the capability byte `intToList(64)` and `authenticationType` = `intToList(d` offset 0x43`)` (`@0x484c65c`..`@0x484c698`); response `@0x484c704` | capability byte `intToList(64)` (`@0x484ab54`); response `@0x484abdc` | response `@0x4849580`; log `设置能力` "set capability" (`@0x4849450`) |
| public key (`getPublicKeyRes`) | native `getClientPublicKey` (`@0x484c808`), empty result fails the stage (`@0x484c820`); response `@0x484c984` | `getClientPublicKey` (`@0x484ace0`); response `@0x484ae5c` | not used |
| key | `computeEcdhWithPublicKey` (`@0x484cc48`), see [Key derivation](#key-derivation) | `computeEcdhWithPublicKey` (`@0x484b120`) | the device sends the key: `getAesKeyRes` (`@0x48497c0`, log `获取密钥成功` `@0x4849844`) carries it under tag `a1` and `setAesKey` stores it (`@0x4849964`) |
| key confirm (`getAesKeyRes`) | `@0x484cf58`, log `身份验证成功` "identity verified" | `@0x484b430`, same log | the key stage itself |
| bind account (`bindUserIdRes`) | not in this conferer | `@0x484b5e0`, log `绑定账户成功` "account bound" | `@0x4849c00`, same log |
| user authentication (`getAuthenticationRes`) | `@0x484d0d8`; success gives `UserAuthenticationStatus.succeed` (`@0x484d208`) | not in this conferer | not in this conferer |
| all device info | log `获取设备所有信息` "get all device info" (`@0x484d2e0`); a `BleCmdStatus` of `needAuthentication` sets `UserAuthenticationStatus.wait` (`@0x484d44c`), the two password failures set `fail` (`@0x484d574`); success `@0x484d680` | log at `@0x484b6bc`, success `@0x484b718` | log at `@0x4849ce8`, success `@0x4849d54` |
| end | `AnkerConnectState.connectDone` (`@0x484d278`, `@0x484d648`) | `connectDone` (`@0x484b7f0`) | `connectDone` (`@0x4849e80`) |

`AesConferV1` derives its IV from the device serial number: after storing the key it reads `deviceSn` (the dispatch selector `0x2abf7` is the one the conferer logs as `device.deviceSn`, for example `@0x4848fbc`; `0x27cd2` is `device.bleMac`), and when the serial is at least 17 characters long (`cmp x0,#0x11`, `b.lt` `@0x4849998`) takes its first 16 characters (`substring(0, 16)` with raw end 32, `@0x48499f8`), otherwise the whole serial; the string is UTF-8 encoded (`@0x4849a1c`) and stored with the IV setter (`@0x4849a38`, `@0x4849ac0`). So in this variant the key comes from the device and the IV is public information. The CBC fallback key `BleInfoHelper.defaultAESKey` is built the same way from `accountId()` ([protocol.md](protocol.md#payload-encryption)).

## Key derivation

Tag: asm-traced.

Both ECDH conferers do the same four steps after the `getPublicKeyRes` handler has the device's public key bytes from tag `a1`:

1. The bytes are converted to a hex string and `04` is prepended (the uncompressed-point marker; the log texts `生成的固件端公钥---` and `公钥key的长度` print the string and its length, `@0x484cb8c`..`@0x484cc38`). The app's own key pair is held by the native plugin: `getClientPublicKey` returns the public key as text and the same plugin method family is used by the login flow (the login pages call `Encryption::getClientPublicKey`; `clearClientKeyPairs` is called only from the login screen).
2. `computeEcdhWithPublicKey` is awaited; its result is a string (`@0x484cc48` and `@0x484b120`).
3. The string length must be 64 characters: `cmp w1,#0x80` against the tagged length (`@0x484ccc8`, `@0x484b1a0`; 0x80 as a Smi is 64), otherwise the conferer fails. So the secret is 32 bytes.
4. The hex string is sliced with `substring` and the pieces are converted with `hexStringToBytes`; the first piece becomes the AES key (`BleInfoHelper.setAesKey`), the second the IV (the IV setter, called at the same position as `setAesIV` in 3.18.0, see [Since 3.18.0](#since-3180)). The `substring` arguments are tagged values:

| conferer | key piece | IV piece | resulting sizes | evidence |
|---|---|---|---|---|
| conferer `SecureEcdhConfer` | characters 0 to 32 (raw end 64, `@0x484cd0c`..`@0x484cd20`) | characters 32 to 56 (raw start 64, raw end 112, `@0x484cd28`..`@0x484cd3c`) | key 16 bytes, IV 12 bytes (a GCM nonce) | `setAesKey` `@0x484cdac`, IV setter `@0x484cdf0` |
| conferer `EcdhConfer` | characters 0 to 32 (raw end 64, `@0x484b1e4`) | characters 32 to 64 (raw start 64, raw end 128, `@0x484b200`..`@0x484b214`) | key 16 bytes, IV 16 bytes (a CBC IV) | `setAesKey` `@0x484b284` |

Cross-checks for the Smi reading: the pieces must fit into the 64-character string, the 16-byte IV of the CBC path matches the IV-length error string of the `encrypt` package (`Initialization vector must be 16 bytes long`), and the 12-byte IV of the GCM path is the usual GCM nonce size; with the raw numbers instead the second slice of `SecureEcdhConfer` would start beyond the end of the string. The 3.18.0 code has the same raw numbers (`secure_ecdh_confer.dart`, 3.18.0 addresses 0x3646014 to 0x3646044). This is the "shared secret first half and second half" of the earlier notes, with the correction that the GCM variant takes only 12 bytes as IV. The log text `协商后的加密用的密钥` prints the pieces at `@0x484ce38` and `ecdh_confer.dart @0x484b2d0`.

## Built-in initial key

Tag: asm-traced.

`ZXBleConfer._setInitialKeyForSecure` (`zx_ble_confer.dart @0x2632130`, called only when the device flag at offset 0x3f is set, `@0x2631f18`) allocates two constant integer arrays in code: 16 elements (`r0 = 32` before `AllocateArray`, `@0x263213c`) and 12 elements (`r2 = 24`, `@0x2632208`). It stores the first as the device's AES key (`BleInfoHelper.setAesKey` `@0x26322fc`), the second with the IV setter (`@0x2632334`) and marks the device as GCM (`setAesGcmTag` `@0x2632368`). So a device that carries the flag has a built-in 16-byte key, a 12-byte IV and GCM mode installed before the first message; the key and the IV are app-embedded constants (role: pre-negotiation key and nonce for secure devices), their values are not written here. Together with the transformer's encryption condition ([protocol.md](protocol.md#payload-encryption)) this means the messages before the ECDH result can already be GCM-encrypted for such a device; whether they are depends on the transformer's key list, see [Known unknowns](#known-unknowns). The same pattern exists in the cloud path as the preset key ([../api/encryption.md](../api/encryption.md)): a constant of the app that protects the first leg of a key exchange.

## Completion

Tag: asm-traced.

When a conferer reports success, the closure at `ZXBleConfer @0x263376c` logs `ZXBleConfer: BLE协商成功，开始调用AKIoT API encryptType：` (`@0x26337b4`), reads the key (`BleInfoHelper.getAesKey` `@0x2633854`) and IV (`getAesIV` `@0x26338a4`) of the device and, when both exist, calls `BasicCommand.setDeviceEncryptKey` (`base_service/ak_iot_kit/business/basic/command/basic_command.dart @0x2633d54`, call `zx_ble_confer.dart @0x2633930`) and then `BasicCommand.setNegotiated` (`@0x2633adc`, call `@0x2633984`). These send the platform-channel calls `akiot.device.set_device_encrypt_key` (map keys `bleMac`, `encryptType`, `encryptKey`, `encryptIv`, `@0x2633ec8`) and `akiot.device.set_device_negotiated` (map keys `bleMac`, `isNegotiation`, the value is `true`, `@0x2633bc4`). Without key or IV the closure logs `无法获取aesKey或aesIv，跳过AKIoT API调用` and skips both calls (`@0x26339a8`). The `encryptType` passed to the kit is read from the same scheme map that `parseCapabilitiesNegotiationResponse` fills.

## Authentication status

Tag: asm-traced.

Some devices require a user password before they answer data requests. The conferer reacts to the `BleCmdStatus` of the answer: `needAuthentication` (`secure_ecdh_confer.dart @0x484d334`) reads tag `a1` of the payload with `listToInt` as the lock-wait time and sets `UserAuthenticationStatus.wait` (`@0x484d3e0`, log `用户需要进行安全鉴权--鉴权时长--`); `passwordWrongAuthenticationFailed` (`@0x484d4b0`, log `鉴权失败，密码错误`) and `passwordRetryCountExceededAuthenticationFailed` (`@0x484d52c`, log `鉴权失败，密码次数超过，已锁定`) set `UserAuthenticationStatus.fail`; any other answer logs `未匹配指令，失败` and fails (`@0x484d5cc`). The enum values and the status codes on the wire (9, 10 and 11 for the three authentication statuses; the indices 14, 15 and 16 are not wire values) are in [../reference/enums.md](../reference/enums.md#blecmdstatus), corrected by the ENUMS audit rows for doc lines 338 to 341. `ZXBleConfer` takes a `userAuthentication` callback (`startZXBleConfer` parameter, stored at offset 0x33, `zx_ble_confer.dart @0x2631d98`).

## Comparison with the cloud key exchange

Tag: asm-traced.

| aspect | BLE (this page) | cloud ([../api/encryption.md](../api/encryption.md)) |
|---|---|---|
| curve and key agreement | native plugin, `computeEcdhWithPublicKey` (`encryption_method_channel.dart @0x484b8b4`) | native plugin, `getExchangedAesKey` (`@0x4017c28`) |
| client key pair | `getClientPublicKey` (shared with the login screens) | `getClientPublicKey` (`@0x2faf454`), same plugin method |
| device or server public key | plain bytes in the BLE payload (tag `a1`), the string `04` is prepended in Dart (`secure_ecdh_confer.dart @0x484cbd4`) | encrypted under the app preset key on the wire (`aesCbcDecrypt`), decrypted text passed to the plugin |
| key derivation | Dart slices the returned 64-character hex secret (16-byte key, 12- or 16-byte IV) | inside the plugin; `Encryption::HKDF` exists in the channel and is called by `EncryptionUtilImpl` (`charging/aiot/EncryptionUtilImpl.dart @0x49dde94`), not by the BLE conferers |
| symmetric cipher | AES-GCM (pointycastle) or AES-CBC (`encrypt` package) | AES-CBC through the plugin for the exchange; request signing is HMAC |
| result lifetime | per BLE MAC, kept in `BleInfoHelper` and pushed to the kit | `currentAesKey` and `currentIdentifyKey` in shared preferences |

The two exchanges share the plugin and the client key pair but not the derivation: this repository has no trace that the plugin applies a hash or HKDF inside `computeEcdhWithPublicKey`, and the Dart code treats its return value as raw key material. The community library `SolixBLE` reports that its handshake uses a fixed, public static key on the client side; whether the app's plugin generates a fresh key pair per call (the older notes said it does, citing `uECC_make_key` in the native library) is not visible in Dart. `libecc-encryption.so` in 3.24.3 exports `uECC_make_key`, `uECC_shared_secret` and the JNI methods `EccEncryption.generateEccKey`, `eccEncrypt` and `eccDecrypt` (package `com.anker.esiotkit.support.crypto`), which is the kit's ECC code; that the Flutter `encryption` plugin calls it is not shown.

## Earlier claims

Tag: untagged by design (no API fact).

The root documents of this repository describe the BLE encryption in two lines (`BLE_COMMAND_MAP.md`: ECDH with `SecureEcdhConfer` and `EcdhConfer`, AES with `AesConferV1` and `AesHelper`, GCM and CBC, opcodes `getAesKeyReq` and `getAesKeyRes`); both are consistent with what is traced above. `REVERSE_ENGINEERING_REPORT.md` contains no negotiation text beyond the list of channel methods (`akiot.device.set_device_negotiated`, `set_device_encrypt_key`); the "6-stage negotiation", the `uECC_make_key` remark and the "first 16 bytes key, rest IV" split came from the project notes and the external SolixBLE library. Against the asm: the stage count depends on the conferer (after the connect and capability stages of `ZXBleConfer` there are 5 opcode-dispatched handlers in `SecureEcdhConfer` and `EcdhConfer` (7 request/response pairs including connect and capability) and 4 in `AesConferV1` (6 pairs); `SecureEcdhConfer` and `EcdhConfer` additionally send a conditional all-device-info request (`@0x484d2b8` to `@0x484d2e0` in `secure_ecdh_confer.dart`) with no response handler in the conferer), the key is bytes 0 to 15 of the 32-byte secret, and the IV is bytes 16 to 27 (GCM) or 16 to 31 (CBC), not "the rest".

## Since 3.18.0

Tag: asm-traced (3.24.3 side).

The Dart negotiation is structurally the same in 3.18.0: the same four files and function counts, the same `substring` raw bounds in `SecureEcdhConfer` (3.18.0 addresses 0x3646014 to 0x3646044) and `EcdhConfer`, and `BleInfoHelper.setAesIV` called right after `setAesKey` (`secure_ecdh_confer.dart`, 3.18.0 address 0x36460e8). In 3.24.3 `BleInfoHelper` no longer has `setAesIV` and `setmtuSize`; the IV is set through the dispatch-table call at the same position, and the kit-to-Dart path (`type=5` message) is present. `parseCapabilitiesNegotiationResponse` and the stage structure were not changed in a way that moves a position; the `commonOpcodeMap` has the same 22 members.

## Known unknowns

Tag: untagged by design (no API fact).

- What sets the device flag at offset 0x3f to true, and what fills the device field at offset 0x87 (which products use which implementation is answered in [Which implementation runs for a product](#which-implementation-runs-for-a-product)). — traced 2026-10-20: `AnkerDevice` stores `false` into offset 0x3f in its constructor (`base_service/device/anker_device.dart @0x23bb6f8`) and has no other store to it; stores to offset 0x3f in other files belong to other classes with the same offset and cannot be told apart by offset. Offset 0x87 is a list, not a string: the constructor stores an empty growable list (`@0x23bb87c`, `@0x23bb884`), `updateWith` copies `field_33` of its argument into it when that is not null (`@0x3667d70`), `toString` prints it after the label `relateType` (`@0x4689cc4`), and `updateStatus` passes the strings `wifi` (`@0x2205cbc`) and `ble` (`@0x2205d1c`) to a one-argument dispatch call on it; what builds the argument of `updateWith` and the name of that selector were not found.
- The call that sends each request: the conferers call the device-class methods through dispatch-table calls that Blutter does not name, so the request opcode for each stage is taken from the response pairing, not from a traced call. — traced 2026-10-20: the calls carry selector numbers only (for example `GDT[cid+0x2abf7]` for `deviceSn`, `aes_confer_v1.dart @0x4848fbc`); the asm has no table from a selector number to a method name, and `charging/ble/device/zx_ble_feature.dart` is an empty class (`class id: 8427, size: 0x8`, no method), so a request cannot be tied to its opcode from the call.
- The format of the public key text returned by `getClientPublicKey`, whether the key pair is fresh per negotiation, the curve used by `computeEcdhWithPublicKey` and whether a hash or HKDF is applied inside it. The size of the result (32 bytes) fits a 256-bit curve; the curve name is not in the Dart code.
- The record format of the capability response (positions 0, 3, 6, 10, 13, 16 and 19) and the meaning of the values of `a0`, `a3`, `a4`, `a5` and `a6`; the correlation that the app answers with the capability byte 64 (bit 6, the same bit tested in `a3` and `a6`) is an observation, not a decoded rule.
- Whether messages before the key exchange are encrypted with the built-in key: the transformer's key list (offset 0x1b) is filled outside the code seen.
- Whether the serial number of every product is long enough for the 16-character cut of the `AesConferV1` IV (the shorter branch uses the whole serial).

BLE is unavailable while the device is on WiFi; see `ble/protocol.md` (community finding, see protocol.md; not asm-traced).
