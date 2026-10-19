> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# iot decoder (generic MQTT decode pipeline)

This page owns the part of MQTT decoding that is the same for every product: how a received MQTT message reaches a device controller, how the product number (PN) picks the controller, how one binary frame is validated and turned into an opcode type plus a tag map, and what the generic fallback controller does with the result. Per-product tag tables stay on the `mqtt/<pn>.md` pages (for example [a17c1_status.md](a17c1_status.md) and [a17x8.md](a17x8.md)); the JSON head, topic strings and frame layout stay on [envelope.md](envelope.md).

## Which file is "the iot decoder"

The plan and the 3.6b report use the name `iot` for the last entry of the 3.18.0 decoder list (`a172x, a1771, ..., shelly, iot`). No audit row in `docs/audit/BLE_COMMAND_MAP.md` or `docs/audit/PARAM_DATA_STRUCTURES.md` uses that name (grep for `iot_anker`, `device_factory`, `ZXOpcode`, `getOpcode`, `iot_device_adapter` finds none; the only `iot` path hits are `ak_iot_kit` model files). The name resolves to one file and the helpers it shares:

- `charging/ble/device/iot_anker_controller.dart`, class `IotDeviceController` (class id 8355, instance size 0x68): the decoder. It is the only `DeviceController` subclass that has no PN of its own; `DeviceFactoryImpl.createByProductCode` builds it for every PN that matches none of its literals (see [Product routing](#product-routing-createbyproductcode)). Like the per-PN controllers it overrides `handleMQTTDeviceResponse` and has a `_handleResponse`, and it calls the same shared helpers (`PPSDeviceCommands`, `MqttServe`).
- `charging/command/pps_device_commands.dart`, class `PPSDeviceCommands`: the shared frame helpers (`parseResponse`, `_parsePayloadData`, `parseCommonData`, opcode maps). 18 of the 25 controller files in `charging/ble/device` (including the base `device_controller.dart`) call `parseResponse`: A1340, A172X, A1753, A1771, A1781, A1790, A17A3, A17B1, A17C0, A17C1, A17X7, A17X8, A17Y0, A2345, A5101, A91B2, Shelly and the fallback controller (grep for `r0 = parseResponse()`).
- `charging/mqtt/business/mqtt_serve.dart` and `charging/ble/device/device_controller.dart`: topic strings, topic gating and the stream wiring of every controller.

Ruled out as the decoder, with the evidence (all 3.24.3):

| file | what it is | source |
|---|---|---|
| `charging/aiot/iot_logic.dart` | `IoTLogicManager extends HttpRequestController` (class id 14884, size 0x64): `createTimer`, `onResumed`, `onPaused`, one poll log string; HTTP polling, no MQTT and no frame code | class header; `_getInstance` @0x27c1538 |
| `base_service/device/device_iot_base.dart` | `abstract class DeviceIoTBase<X0 bound DeviceInfoSpec>` (class id 0x18f9, size 0x14); the file is nine lines with no members | class header |
| `base_service/device/iot_device_adapter.dart` | `IotDeviceAdapter` (class id 8440, size 0x200), the device-model base of `IotAnkerDevice`: connection, OTA, battery and version getters; its `onMessageDispatch` @0x2855894 handles only the SDK event code 6000 (a BLE status event carrying `bleMac`), see below | class header; `onMessageDispatch` @0x2855894 |
| `ak_base_contract/src/iot_ak_result.dart` | `IoTAKResult<X0>` (class id 0x1c6f, size 0x24): result wrapper with `isSuccessful` and `fromAKIoTResult` | class header |

The code 6000 compare in `IotDeviceAdapter.onMessageDispatch` is `mov x17,#0x1770; cmp x0,x17` against a 64-bit field load (`ldur x0,[x2,#0xb]`), so the raw value is the real value (0x1770 = 6000) iot_device_adapter.dart @0x28558b8. It then reads `bleMac` and `data.type` from the event map and calls `_updateBleStatus` @0x2855a70. It never touches a frame.

## Contents

1. [Which file is "the iot decoder"](#which-file-is-the-iot-decoder)
1. [Audit rows consumed](#audit-rows-consumed)
1. [Commands](#commands)
   1. [MQTT receive path and topic gate](#mqtt-receive-path-and-topic-gate)
   1. [Product routing (createByProductCode)](#product-routing-createbyproductcode)
   1. [Frame decode and opcode dispatch](#frame-decode-and-opcode-dispatch)
   1. [Fallback handler (IotDeviceController)](#fallback-handler-iotdevicecontroller)

## Audit rows consumed

The shared helpers are covered by these rows of [../docs/audit/BLE_COMMAND_MAP.md](../docs/audit/BLE_COMMAND_MAP.md) (written `audit row N`): 14 (checksum), 15 (direction bit), 25 (gzip magic), 48 and 49 (`parseCommonData` tag loop), 50 and 51 (`parseCommonDataWithCustomLengthBytes`), 52 (`listToInt`). Everything else on this page is a new read of the 3.24.3 asm (grep and sed only; no audit row exists for the receive path, the factory, `parseResponse`, the two opcode maps or `IotDeviceController`). Audit row 51 was UNVERIFIABLE (the length-width map is a parameter); this page finds the one literal that fills it (below). Integers follow the Smi rule of [../METHODOLOGY.md](../METHODOLOGY.md#smi-rule-reading-numbers-from-blutter-output): 64-bit loads and stores and arithmetic are real, 32-bit stores into slots and fields are halved, sublist ends are tagged (raw/2) while sublist starts are unboxed.

## Commands

### MQTT receive path and topic gate

#### Purpose

Shows how one received MQTT message gets from the native SDK event to a device controller's `handleMQTTDeviceResponse`, and which messages are dropped on the way.

#### Upstream name

none for the app side. The same layering exists in the upstream `on_message` callback (`api/mqtt.py` lines 117-147: UTF-8 JSON, then `json.loads` of the `payload` string, then base64 of `data`; PN and serial from topic segments, lines 134-139), upstream-confirmed.

#### Command code

none (receive path, no opcode).

#### Direction

device→app. Tag: asm-traced. The send side (`MqttCommandController.sendCommand` mqtt_command_controller.dart @0x226f930, which JSON-encodes a map and calls `MqttServe.zxSendMessage` mqtt_serve.dart @0x226f9a4) is documented on [envelope.md](envelope.md#topics).

#### Topic pattern

[envelope.md](envelope.md#topics). The decoder reads only the parameter topic `dt/anker_power/<pn>/<sn>/param_info`. Callers of the topic predicates in the 3.24.3 asm (grep for `r0 = <name>()`): `isDeviceParamInfoTopic` is called in 14 controller files (12 PN controllers, the Shelly controller and `iot_anker_controller.dart`); `isDeviceStateInfoTopic` (`.../state_info`) only in `a17x7_device_controller.dart`; `isDeviceResponseInfoTopic` (`.../app/res`) only in five UI logic files (Wi-Fi list and switch, add-devices progress, sync Wi-Fi); `isGetBssidPwdTopic` only in two station and site UI logic files. So the `state_info` messages are decoded by the A17X7 controller alone ([a17x7.md](a17x7.md)); the fallback controller never sees them.

#### Payload fields

Hops in order; tag column is the hop id. Event codes are read from a 64-bit field, so they are real values.

| tag | name | type | unit/scale | required | source |
|---|---|---|---|---|---|
| h1 | SDK data event code | int64 | 0x1773 (6003) | yes | `sdk_imp_mqtt_manager.dart` `SdkMqttManagerImpl.onMessageDispatch` @0x2855138 |
| h1b | SDK connect event code | int64 | 0x1772 (6002), log `codeAKIoTKitMqttConnect` | no | same function @0x2855188 |
| h2 | event data | `Map<String, dynamic>` (type test) | added to the broadcast response stream | yes | same function @0x2855180 |
| h3 | manager choice | bool `field_7` of the late static `DemoSiteUtil` (field table offset 0xdf8) | true: Dart `MqttManagerImpl`; false: `SdkMqttManagerImpl` | yes | `mqtt_serve.dart` `_manager` @0x2207ed0, branch @0x2207ef8, targets @0x2207f04 and @0x2207f14; `response` getter @0x23c1e80 |
| h4 | per-controller stream | `StreamController.broadcast` in `MqttCommandController` | listens to `MqttServe().response` and re-adds every event | yes | `mqtt_command_controller.dart` ctor @0x3aaed60, `notifyCommand` @0x4859c40 (listen), @0x4859cb0 (add) |
| h5 | controller filter | `MqttServe.isCurrentDeviceMqttResponse(device, topic)` | topic must contain (case-insensitive) a value of one device selector and then a value of a second | yes | `mqtt_serve.dart` @0x242e328 (size 0xa4): `isCaseInsensitiveContainsAny` @0x242e37c and @0x242e3ac; caller `DeviceController._initMQTTDeviceResponse` closure device_controller.dart @0x242e2dc |
| h6 | handler call | virtual `handleMQTTDeviceResponse(event)` | per controller | yes | `device_controller.dart` closure @0x242e2fc |
| h7 | body | first chained property read, String, `JsonCodec.decode`, must be a `Map<String, dynamic>` | | yes | `IotDeviceController.handleMQTTDeviceResponse` iot_anker_controller.dart @0x3b69900: decode @0x3b69a1c, type test @0x3b69a8c |
| h8 | topic gate | second chained property read, String; `MqttServe.isDeviceParamInfoTopic(device, topic)` false returns | `param_info` only | yes | iot_anker_controller.dart @0x3b69b40 (`isDeviceParamInfoTopic` mqtt_serve.dart @0x3b33070, size 0x58, builds `"dt/" + getCommonTopicString + "/param_info"` through `getDeviceParamInfoTopic` @0x34d01fc, literals @0x34d0234 and @0x34d0278) |
| h9 | `payload` | key `"payload"` of the body; null returns; String decoded a second time to a `Map` | | yes | iot_anker_controller.dart @0x3b69b58 to @0x3b69be0 |
| h10 | `data` | key `"data"` of the inner map; String, `base64Decode` to bytes, then `_handleResponse(bytes)` | | yes | @0x3b69c5c, @0x3b69cc4, @0x3b69cd4 |
| h11 | defer | when `AnimationCriticalWindow.isInCriticalWindow` is true the call is wrapped in `defer(...)` and re-entered later | | no | @0x3b69960 to @0x3b6997c (late static field table 0x2060, pool [pp+0x1b938]); re-entry closure @0x3b6aa9c calls the handler at @0x3b6aad0 |

The same six steps (decode body, topic gate, `payload`, `data`, base64, `_handleResponse`) are in the other controllers' `handleMQTTDeviceResponse`; the A17C1 copy is a17c1_device_controller.dart @0x3b54fc0 (size 0x68) plus `_dealWithMqttResponse` @0x3b55028 (size 0x43c). The BLE entry point of the fallback controller, `handleZXProtocolDeviceResponse` iot_anker_controller.dart @0x3b90454 (size 0xd0), calls the same `_handleResponse` @0x3b904f4 and then `handleDeviceLogParser` @0x3b90508 under the same deferral; this page does not describe the BLE transport and makes no claim that it serves as a fallback for the cloud path (see [../ble/README.md](../ble/README.md)).

#### Example

synthesized

```text
topic  dt/anker_power/<pn>/<sn>/param_info
body   {"head":{...},"payload":"{\"data\":\"<base64 frame>\", ...}"}
step   decode(body) -> body["payload"] (String) -> decode -> ["data"] -> base64Decode -> bytes
```

#### Related API endpoint

none for the receive path itself; the MQTT credentials and topics come from the IoT-Kit login, see [../api/README.md](../api/README.md).

#### Since/changed

Both versions have the topic predicates and the `_manager` getter with equal function sizes (`_manager` 0x68; `isDeviceParamInfoTopic` and `isDeviceStateInfoTopic` 0x58); the bodies were not diffed beyond the sizes. `isCurrentDeviceMqttResponse` grew from 0x94 to 0xa4 and `handleMQTTDeviceResponse` of the fallback controller shrank from 0x528 to 0x4d8. Tag: asm-traced (3.24.3 side).

#### Known unknowns

- The two chained property reads that give the body and the topic of the event are dynamic calls through one shared pool object (`IMM 0x10fd1fba4`, iot_anker_controller.dart @0x3b69a9c to @0x3b69af4 and @0x3b69998 to @0x3b699d4), so the property names are not visible. The event is a `Map<String, dynamic>` (type test sdk_imp_mqtt_manager.dart @0x2855168); a single-entry topic-to-body map fits both reads but is not confirmed.
- The two device selectors tested by `isCurrentDeviceMqttResponse` are dispatch-table getters without names (offsets 0x2b43b and 0x2abf7). By the topic layout they are the PN and the serial; the second selector is also the key suffix of the debounce strings in `parseCommonData`, with the BLE MAC as fallback, which agrees with a serial.
- What the `DemoSiteUtil` bool (`field_7`) means (the class is `DemoSiteUtilImpl`, size 0x18) and which manager production builds use is not established.
- Where `MqttDecompressionUtil.decompressPayload` is applied: it has 12 call sites in 9 files (`ak_soft_ems`, `ats_ax170`, `scene_info_mgr`, `device_mode_tips_logic`, three `charging/ui/page/device/main` station pages, `micro_hes` station logic), none in `charging/ble/device`, `charging/mqtt` or `charging/command`. The per-device decode path above therefore has no gzip step; the topics that feed the station-level callers are not traced. This narrows the open question in [envelope.md](envelope.md#known-unknowns).

#### Device-tested by

none.

### Product routing (createByProductCode)

#### Purpose

Shows which device class, command class and controller class the app builds for a PN, and that every PN without a literal falls through to the generic `IotAnkerDevice` plus `IotDeviceController`.

#### Upstream name

none. Upstream routes by PN and message type instead of by class: `SOLIXMQTTMAP[model][msgtype]` in `DeviceHexData._get_fieldmap` (`api/mqtttypes.py` lines 863-868), upstream-confirmed.

#### Command code

none (factory, no opcode).

#### Direction

app-internal. Tag: asm-traced.

#### Topic pattern

[envelope.md](envelope.md#topics); the PN is the third topic segment.

#### Payload fields

`DeviceFactory.createByProductCode` device_factory.dart @0x24e2af8 (size 0x58) forwards to `DeviceFactoryImpl.createByProductCode` device_factory_impl.dart @0x240df30 (size 0x15b4). The function compares the PN with string literals through `==` in a fixed order, first `"A1781"` @0x240df58 and last `"AX1S0"` @0x240f45c: 52 literals. `createByDeviceModel` @0x240d5e4 calls it with `isInitListener` true @0x240d618 and, when the result is not null, `_generateAnkerDevice` @0x240d654 (size 0x7fc), which copies the model fields onto the device (it calls `getSkuBySN` @0x240d740). Class names are the allocation stubs in the asm; the constructor call after each allocation is labelled with another controller name in places (for example `A172xDeviceController` after `A17C0DeviceController`), which is a Blutter label for shared code, not a second object.

| controller class | commands class | PN literals (compare address) | device classes | page |
|---|---|---|---|---|
| `A1781DeviceController` | `A1771DeviceCommands` | A1781 @0x240df58 | `A1781AnkerDevice` | note in [a1753.md](a1753.md) |
| `A1770DeviceController` | none | A1770 @0x240dfe0 | `A1770AnkerDevice` | none |
| `A1780DeviceController` | none | A1780 @0x240e08c | `A1780AnkerDevice` | [a1780.md](a1780.md) |
| `A1771DeviceController` | `A1771DeviceCommands` | A1771 @0x240e138, A1772 @0x240e2a8 | `A1771AnkerDevice`, `A1772AnkerDevice` | [a1771.md](a1771.md) |
| `A1790DeviceController` | `A1790DeviceCommands` | A1790 @0x240e1c4, A1790P @0x240e22c | `A1790AnkerDevice`, `A1790PAnkerDevice` (string `A1790P_15Ah` @0x240e24c) | [a1790.md](a1790.md) |
| `A17A0DeviceController` | none | A17A0 @0x240e334, A17A1 @0x240e3a8, A17A2 @0x240e41c | `A17A0AnkerDevice`, `A17A1AnkerDevice`, `A17A2AnkerDevice` | none (EverFrost) |
| `A17A3DeviceController` | none | A17A3 @0x240e490, A17A4 @0x240e4ec, A17A5 @0x240e548 | `A17A3AnkerDevice`, `A17A4AnkerDevice`, `A17A5AnkerDevice` | none (EverFrost) |
| `A5140DeviceController` | none | A5140 @0x240e5a4, A5141 @0x240e774, A5143 @0x240e7e8 | `A5140AnkerDevice`, `A5141AnkerDevice`, `A5143AnkerDevice` | none |
| `A1340DeviceController` | none | A1340 @0x240e618 | `A1340AnkerDevice` | [a1340.md](a1340.md) |
| `A17C0DeviceController` | none | A17C0 @0x240e674 | `A17C0AnkerDevice` | [a17c0.md](a17c0.md) |
| `A17Y0DeviceController` | none | A17Y0 @0x240e6e4 | `A17Y0AnkerDevice` | none |
| `A5101DeviceController` | none | A5101 @0x240e858, A5102 @0x240e870, A5103 @0x240e888, A5341 @0x240e8a0 (one shared block) | `A5101AnkerDevice` | [a5101.md](a5101.md) |
| `A5150DeviceController` | none | A5150 @0x240e958 | `A5150AnkerDevice` | none |
| `A1753DeviceController` | `A1753DeviceCommands` | A1753 @0x240e9b0, A1754 @0x240ea2c, A1755 @0x240eaa8, A1761 @0x240eb24, A1762 @0x240eba0 | one `AnkerDevice` class per PN | [a1753.md](a1753.md) |
| `A17B1DeviceController` | none | A17B1 @0x240ec1c | `A17B1AnkerDevice` | [a17b1.md](a17b1.md) |
| `A172xDeviceController` | none | A1722 @0x240ec78, A1723 @0x240ecd4, A1725 @0x240ed30, A1726 @0x240ed8c, A1727 @0x240ede8, A1728 @0x240ee44, A1729 @0x240eea0 | one `AnkerDevice` class per PN, built on `A172xAnkerDevice` | [a172x.md](a172x.md) |
| `A91B2DeviceController` | none | A91B2 @0x240eefc | `A91B2AnkerDevice` | [a91b2.md](a91b2.md) |
| `A2345DeviceController` | none | A2345 @0x240ef58 | `A2345AnkerDevice` | [a2345.md](a2345.md) |
| `A17C1DeviceController` | `A17C1DeviceCommands` | A17C1 @0x240efe4, A17C3 @0x240f04c | `A17C1AnkerDevice`, `A17C3AnkerDevice` | [a17c1.md](a17c1.md), [a17c1_status.md](a17c1_status.md) |
| `A17C1DeviceController` | `A17C5DeviceCommands` | A17C5 @0x240f0b4 | `A17C5AnkerDevice` | [a17c5.md](a17c5.md) |
| `A17C1DeviceController` | `A17C2DeviceCommands` | A17C2 @0x240f3cc | `A17C2AnkerDevice` | [a17c2.md](a17c2.md) |
| `A17X7DeviceController` | `A17X7DeviceCommands` | A17X7 @0x240f11c | `A17X7AnkerDevice` | [a17x7.md](a17x7.md) |
| `A17X7DeviceController` | `A17X7USDeviceCommands` | A17X7US @0x240f184 | `A17X7USAnkerDevice` | [a17x7.md](a17x7.md) |
| `A17X8DeviceController` | none | A17X8 @0x240f1ec | `A17X8AnkerDevice` | [a17x8.md](a17x8.md) |
| `A1780PDeviceController` | `A1771DeviceCommands` | A1780P @0x240f250 | `A1780pAnkerDevice` | none |
| `ShellyDeviceController` | none | SHEM3 @0x240f2b8, SHEMP3 @0x240f314, SHPPS @0x240f370 | `ShellyDevice`, `ShellyProDevice`, `ShellyPlugDevice` | [shelly.md](shelly.md) |
| none (returns null) | none | A5220 @0x240f434, AX1S0 @0x240f45c | no device object | none |
| `IotDeviceController` (fallback) | none | every other PN, allocation @0x240f484 and @0x240f4a4, `setDeviceController` @0x240f4c4 | `IotAnkerDevice` (class id 8442, size 0x20c) | this page |

The A5101 compares jump into the block that follows the A5341 literal @0x240e8b8; the A5220 and AX1S0 compares return null @0x240f44c and @0x240f474, so the factory creates no object for them and never reaches the fallback.

#### Example

synthesized

```text
createByProductCode("A17C1")  -> A17C1AnkerDevice + A17C1DeviceCommands + A17C1DeviceController
createByProductCode("ZZ999")  -> IotAnkerDevice + IotDeviceController     (no literal matches)
createByProductCode("A5220")  -> null
```

#### Related API endpoint

The PN comes from the device model passed to `createByDeviceModel`; which API response fills that field is not traced here. See [../api/README.md](../api/README.md).

#### Since/changed

The 52 literals and their order are identical in 3.18.0 (3.18.0 `device_factory_impl.dart`, compare chain @0x1993e20 to @0x19955e0). The allocated classes are identical per PN; the differences in a name comparison come only from the constructor labels. In 3.18.0 the A17A3, A17A4 and A17A5 blocks additionally stored the string `Removable Battery` (3.18.0 `device_factory_impl.dart`, for A17A3 @0x1994378 and @0x19943f8); the 3.24.3 blocks store no string. Tag: asm-traced (3.24.3 side).

#### Known unknowns

- Which callers pass which PN to this factory is not traced; the ev_charger, ats and micro_hes Dart modules have their own controllers and may never ask for those PNs here.
- A1770, A1780P, A5140, A5150, A17Y0, the EverFrost group A17A0 to A17A5 and the A17D0 have a controller here but no `mqtt/<pn>.md` page (EverFrost and A17D0 are niche or have no UI page; see the Not covered note in [README.md](README.md)).
- `_generateAnkerDevice` copies about twenty model fields; which model field is the PN and which the BLE MAC is not mapped.

#### Device-tested by

none.

### Frame decode and opcode dispatch

#### Purpose

Shows how `PPSDeviceCommands.parseResponse` validates a frame, maps its two opcode bytes to a `ZXOpcodeType`, hands the payload to the parser for that type, and what the generic TLV parser returns.

#### Upstream name

none. Upstream splits a frame in `DeviceHexDataHeader.__post_init__` and `DeviceHexData.__post_init__` (`api/mqtttypes.py` lines 56-80 and 833-853) and keys its field map by the 4-hex message type; the app keys by a `ZXOpcodeType` enum, upstream-confirmed for the byte layout only.

#### Command code

Hex strings built by `bytesToHexString` (two lowercase digits per byte: `_toPow2String(16)` cmd_util.dart @0x21d4f60 and, for a one-digit result, a leading `0` written first, `cmp x2,#2` @0x21d4f74 and `toString` of 0 @0x21d4f80 in `cmd_util.dart`), used as map keys; string literals, never halved. The two maps are listed under Payload fields.

#### Direction

device→app (the same helpers also resolve the opcode of requests through `getOpcodeFromType`). Tag: asm-traced.

#### Topic pattern

[envelope.md](envelope.md#binary-layer) for the frame header and [envelope.md](envelope.md#tlv-frame) for the field layout; the receive path is the previous section.

#### Payload fields

`parseResponse(bytes, bleMac, device:)` pps_device_commands.dart @0x241c8bc (size 0x560) returns a `Map<String, dynamic>`; every index below is a byte offset of the frame. Sublist starts are unboxed (real), sublist ends are tagged (raw/2).

| tag | name | rule | unit/scale | required | source |
|---|---|---|---|---|---|
| p1 | minimum length | `cmp x1,#0xa` on the unboxed length: shorter than 10 bytes returns the empty map | bytes | yes | @0x241c964 |
| p2 | declared length | `listToInt(bytes[2..4))`: start 2 @0x241c984, end raw 8 = 4 @0x241c978; a declared length above the actual length returns the empty map | bytes | yes | @0x241c9a4, @0x241c9e4 |
| p3 | opcode bytes | `bytes[7..9)`: start 7 @0x241ca1c, end raw 18 = 9 @0x241ca10 | 2 bytes | yes | @0x241ca24 |
| p4 | group byte | `bytes[6]` (array index 6 @0x241ca40) is the second argument of `getOpcodeType` | 1 byte | yes | @0x241ca6c |
| p5 | payload | `bytes[9 .. length-1)`: loop starts at 9 @0x241ca88 and ends one byte before the end @0x241caa8, so the last (XOR) byte is dropped | bytes | yes | @0x241caa0 |
| p6 | `FEATURE_OPCODE_KEY` | the `ZXOpcodeType` from `getOpcodeType` | enum | yes | @0x241cb88 |
| p7 | encrypted flag | `(opcodeBytes[0] & 0xf0) == 0x40`, unboxed compare | bool | yes | @0x241cbcc, @0x241cbd0 |
| p8 | `PAYLOAD_KEY` | result of `_parsePayloadData(type, payload, groupByte, bleMac, device, flag, opcodeBytes)` | map | yes | call @0x241cc2c, store @0x241cc50 |
| p9 | `BLE_CMD_STATUS_KEY` | `BleStatusCode.getCmdStatus(payload["a0"])` when the payload map has key `a0` (`indexString(0xa0)`, argument 160) | enum | no | @0x241cc80, @0x241cd04, @0x241cd28 |
| p10 | `OPCODE_KEY` | the opcode bytes with element 0 replaced by `element0 & 0xf` | 2 bytes | yes | mask @0x241cd74, store @0x241cddc |

No XOR checksum is compared on this path (`parseResponse`, `_parsePayloadData`, `parseCommonData` and `iot_anker_controller.dart`): `pps_device_commands.dart` has no `eor` instruction and no call to a checksum function (grep), and the length check above is the only frame check. A receive-side XOR validator does exist on the BLE reassembly path: `ZXCmdUtil._isLegallyCmd` in ak_cmd_util.dart @0x478a2e8 calls `getCheckSum` @0x478a348 and compares the result with the last byte (`cmp x2,x1` @0x478a37c); it is called from `ZXCommandTransformer.validateCommand` (zx_command_transformer.dart @0x4789138, call @0x4789240). Whether any MQTT frame reaches `validateCommand` was not traced (no caller of the form `r0 = validateCommand()` was found, grep); the checksum builders of the send side are in [envelope.md](envelope.md#binary-layer) (audit row 14).

`getOpcodeFromCmd(bytes)` @0x2634538 (size 0xac) is the entry the controllers call: `getOpcodeType(bytes.sublist(7, 9), bytes[6])` with start raw 7 @0x263456c, end raw 18 = 9 @0x2634560 and index raw 12 = 6 @0x263459c. `getOpcodeType` @0x2425dc8 (size 0x2f0) copies the two bytes, replaces element 0 by `element0 & 0xf` @0x2425f60, builds the hex key, and looks it up in `commonOpcodeMap` when the group byte equals 1 (`cmp x0,#1` @0x2425fcc) and in `chargingOpcodeMap` otherwise; a missing key gives the enum value `unknown` (index 0x61, pool [pp+0x10e80]) @0x2426088. `getOpcodeFromType(type, group)` @0x241ff90 (size 0xd4) is the reverse: `forEach` over the same maps, `hexStringToBytes(key)` for each matching value.

**commonOpcodeMap** (built @0x2422850, size 0x608; array length raw 88 = 44 elements = 22 pairs @0x2422878). Selected when byte 6 equals 1. Key bytes are `[b0 & 0xf, b1]`; a first byte of 8 marks a response.

| opcode key | ZXOpcodeType | enum index | source |
|---|---|---|---|
| `0001` | `startConnectReq` | 0x0 | @0x2422894 |
| `0801` | `startConnectRes` | 0x1 | @0x24228d8 |
| `0002` | `startDisconnectReq` | 0x2 | @0x242291c |
| `0802` | `startDisconnectRes` | 0x3 | @0x2422960 |
| `0003` | `capabilityNegotiationReq` | 0x4 | @0x24229a4 |
| `0803` | `capabilityNegotiationRes` | 0x5 | @0x24229e8 |
| `0004` | `configureCapabilityReq` | 0x6 | @0x2422a2c |
| `0005` | `setCapabilityReq` | 0x7 | @0x2422a70 |
| `0805` | `setCapabilityRes` | 0x8 | @0x2422ab4 |
| `0027` | `getAuthenticationReq` | 0xd | @0x2422af8 |
| `0827` | `getAuthenticationRes` | 0xe | @0x2422b3c |
| `0029` | `getDeviceInfoReq` | 0x9 | @0x2422b80 |
| `0829` | `getDeviceInfoRes` | 0xa | @0x2422bc4 |
| `0022` | `getAesKeyReq` | 0xb | @0x2422c08 |
| `0822` | `getAesKeyRes` | 0xc | @0x2422c4c |
| `0023` | `bindUserIdReq` | 0xf | @0x2422c90 |
| `0823` | `bindUserIdRes` | 0x10 | @0x2422cd4 |
| `0021` | `getPublicKeyReq` | 0x11 | @0x2422d18 |
| `0821` | `getPublicKeyRes` | 0x12 | @0x2422d5c |
| `0031` | `requestModuleLogUploadReq` | 0x89 | @0x2422da0 |
| `0831` | `requestModuleLogUploadRes` | 0x8a | @0x2422de4 |
| `0032` | `moduleLogUploadRes` | 0x8b | @0x2422e28 |

**chargingOpcodeMap** (built @0x2420104, size 0x274c; array length raw 500 = 250 elements = 125 pairs @0x242012c, 118 distinct keys). Selected for every other group byte. Seven keys occur twice; by Dart map-literal semantics (a later entry replaces the earlier value; not an asm citation) the later value is kept, so the earlier type can never come out of `getOpcodeType`; `getOpcodeFromType` runs `forEach` over the stored entries, so it never yields a key for a shadowed type either (the table marks both rows).

| opcode key | ZXOpcodeType | enum index | source |
|---|---|---|---|
| `0022` | `scanWifiReq` | 0x13 | @0x2420148 |
| `0822` | `scanWifiRes` | 0x14 | @0x242018c |
| `0023` | `getWifiListReq` | 0x15 | @0x24201d0 |
| `0823` | `getWifiListRes` | 0x16 | @0x2420214 |
| `0024` | `connectWifiReq` | 0x18 | @0x2420258 |
| `0824` | `connectWifiRes` | 0x17 | @0x242029c |
| `0025` | `activateWifiReq` | 0x19 | @0x24202e0 |
| `0825` | `activateWifiRes` | 0x1a | @0x2420324 |
| `0035` | `exitConnectReq` | 0x1b | @0x2420368 |
| `0835` | `exitConnectRes` | 0x1c | @0x24203ac |
| `0400` | `postErrorInfoReq` | 0x1d | @0x24203f0 |
| `0401` | `postSwitchStateReq` | 0x1f | @0x2420434 |
| `0402` | `postWorkInfoReq` | 0x1e | @0x2420478 |
| `0403` | `postDeviceInfoReq` | 0x20 | @0x24204bc |
| `0404` | `postCountDownTimeReq` | 0x21 | @0x2420500 |
| `0426` | `postLinkageSystemErrorReq` | 0x22 | @0x2420544 |
| `0840` | `getAllDeviceInfoRes` | 0x25 | @0x2420588 |
| `0841` | `getAcCarCountDownTimeRes` | 0x27 | @0x24205cc |
| `0842` | `setAcCountDownTimeRes` | 0x29 | @0x2420610 (shadowed by `setCarCountDownTimeRes`) |
| `0842` | `setCarCountDownTimeRes` | 0x2b | @0x2420654 (later entry wins) |
| `0844` | `setAcChargePowerRes` | 0x2d | @0x2420698 |
| `0845` | `setDeviceWaitTimeRes` | 0x2f | @0x24206dc |
| `0846` | `setDeviceScreenTimeRes` | 0x31 | @0x2420720 |
| `0847` | `setInversionWaitTimeRes` | 0x33 | @0x2420764 |
| `0848` | `setMajorPkgRes` | 0x3e | @0x24207a8 |
| `0849` | `setMinorPkgRes` | 0x40 | @0x24207ec |
| `084a` | `setAcSwitchRes` | 0x42 | @0x2420830 |
| `084b` | `setCarSwitchRes` | 0x44 | @0x2420874 |
| `084c` | `setLcdLightRes` | 0x46 | @0x24208b8 |
| `084d` | `setAcFrequencyRes` | 0x48 | @0x24208fc |
| `084e` | `setEnergyModeRes` | 0x4a | @0x2420948 |
| `084f` | `setAmbientLightRes` | 0x4c | @0x242099c |
| `0850` | `setTempUnitRes` | 0x4e | @0x24209f0 |
| `0851` | `setResetRes` | 0x50 | @0x2420a44 |
| `0057` | `setDeviceUpdateEnergyReq` | 0x51 | @0x2420a98 |
| `0405` | `postDeviceAllInfoReq` | 0x52 | @0x2420aec |
| `0406` | `postUpgradeStateRes` | 0x64 | @0x2420b40 (shadowed by `postUpgradeStateReq`) |
| `0061` | `getAllBMSSubBatteryInfoReq` | 0x53 | @0x2420b94 (shadowed by `setA17b1CommandReq`) |
| `0861` | `getAllBMSSubBatteryInfoRes` | 0x54 | @0x2420be8 (shadowed by `setA17b1CommandRes`) |
| `0409` | `postAllBMSMinorBatteryBTInfoReq` | 0x55 | @0x2420c3c |
| `040a` | `postAllBMSMinorBatteryWiFiInfoReq` | 0x56 | @0x2420c90 |
| `0410` | `postA17B2DeviceInfoWIFIReq` | 0x57 | @0x2420ce4 |
| `0411` | `postA17B2DeviceInfoBTReq` | 0x58 | @0x2420d38 |
| `0074` | `getA17B2DeviceInfoReq` | 0x59 | @0x2420d8c |
| `0874` | `getA17B2DeviceInfoRes` | 0x5a | @0x2420de0 |
| `005f` | `setBMSSubBatteryPowerSwitchReq` | 0x5b | @0x2420e34 |
| `085f` | `setBMSSubBatteryPowerSwitchRes` | 0x5c | @0x2420e88 |
| `0460` | `getDeviceSelfTestRes` | 0x5d | @0x2420edc |
| `0060` | `setBMSSubBatteryLightSwitchReq` | 0x5e | @0x2420f30 |
| `0860` | `setBMSSubBatteryLightSwitchRes` | 0x5f | @0x2420f84 |
| `085e` | `setDischargeTimeRes` | 0x3c | @0x2420fd8 (shadowed by `setSuperChargeRes`) |
| `040f` | `postSubBatteryErrorInfoReq` | 0x60 | @0x242102c |
| `085e` | `setSuperChargeRes` | 0x63 | @0x2421080 (later entry wins) |
| `005e` | `setSuperChargeReq` | 0x62 | @0x24210d4 |
| `040e` | `getMicroInverterReq` | 0x3b | @0x2421128 |
| `0406` | `postUpgradeStateReq` | 0x65 | @0x242117c (later entry wins) |
| `002e` | `sendOtaSubPackageReq` | 0x3a | @0x24211d0 |
| `0069` | `deviceFactorySettingRes` | 0x67 | @0x2421224 |
| `0869` | `deviceFactorySettingReq` | 0x68 | @0x2421278 |
| `006a` | `deviceFactorySettingClearRes` | 0x69 | @0x24212cc |
| `086a` | `deviceFactorySettingClearReq` | 0x6a | @0x2421320 |
| `0061` | `setA17b1CommandReq` | 0x6b | @0x2421374 (later entry wins) |
| `0861` | `setA17b1CommandRes` | 0x6c | @0x24213c8 (later entry wins) |
| `0500` | `postA17b1DeviceInfoReq` | 0x6d | @0x242141c |
| `0501` | `postA17b1SelfCheckReq` | 0x6e | @0x2421470 |
| `0503` | `postDeviceListReq` | 0x6f | @0x24214c4 |
| `0604` | `postGetUpdateListReq` | 0x70 | @0x2421518 |
| `0601` | `postA1790DeviceInfoReq` | 0x71 | @0x242156c |
| `0602` | `setA1790CommandReq` | 0x72 | @0x24215c0 |
| `0031` | `getScanBluetoothDeviceReq` | 0x73 | @0x2421614 |
| `0831` | `getScanBluetoothDeviceRes` | 0x74 | @0x2421668 |
| `0032` | `getBindBluetoothDeviceReq` | 0x75 | @0x24216bc |
| `0832` | `getBindBluetoothDeviceRes` | 0x76 | @0x2421710 |
| `0033` | `getUnBindBluetoothDeviceReq` | 0x77 | @0x2421764 |
| `0833` | `getUnBindBluetoothDeviceRes` | 0x78 | @0x24217b8 |
| `0021` | `getModuleInfoReq` | 0x79 | @0x242180c |
| `0821` | `getModuleInfoRes` | 0x7a | @0x2421860 |
| `0200` | `getMiniChargeAllDeviceInfoReq` | 0x7b | @0x24218b4 |
| `0a00` | `getMiniChargeAllDeviceInfoRes` | 0x7c | @0x2421908 |
| `0201` | `setMiniChargeResetReq` | 0x7d | @0x242195c |
| `0a01` | `setMiniChargeResetRes` | 0x7e | @0x24219b0 |
| `0202` | `getMiniChargeScreensaverReq` | 0x7f | @0x2421a04 |
| `0a02` | `getMiniChargeScreensaverRes` | 0x80 | @0x2421a58 |
| `0203` | `setMiniChargeScreenTimeoutReq` | 0x81 | @0x2421aac |
| `0a03` | `setMiniChargeScreenTimeoutRes` | 0x82 | @0x2421b00 |
| `0204` | `setMiniChargeScreenBrightnessReq` | 0x83 | @0x2421b54 |
| `0a04` | `setMiniChargeScreenBrightnessRes` | 0x84 | @0x2421ba8 |
| `0205` | `setMiniChargeScreensaverReq` | 0x85 | @0x2421bfc |
| `0a05` | `setMiniChargeScreensaverRes` | 0x86 | @0x2421c50 |
| `0206` | `setMiniChargeACRelaySwitchReq` | 0x87 | @0x2421ca4 (shadowed by `setMiniChargeACRelaySwitchRes`) |
| `0206` | `setMiniChargeACRelaySwitchRes` | 0x88 | @0x2421cf8 (later entry wins) |
| `0207` | `setMiniChargeACRelaySwitchReq` | 0x87 | @0x2421d4c |
| `0a07` | `setMiniChargeACRelaySwitchRes` | 0x88 | @0x2421da0 |
| `0065` | `requestMcuLogUploadReq` | 0x8c | @0x2421df4 |
| `0865` | `requestMcuLogUploadRes` | 0x8d | @0x2421e48 |
| `0066` | `mcuLogUploadReq` | 0x8e | @0x2421e9c |
| `0866` | `mcuLogUploadRes` | 0x8f | @0x2421ef0 |
| `0067` | `bleOtaProgressReq` | 0x90 | @0x2421f44 |
| `0867` | `bleOtaProgressRes` | 0x91 | @0x2421f98 |
| `0030` | `getZXOTAStateReq` | 0x38 | @0x2421fec |
| `0830` | `getZXOTAStateRes` | 0x39 | @0x2422040 |
| `0076` | `carPortSavingReq` | 0x92 | @0x2422094 |
| `0876` | `carPortSavingRes` | 0x93 | @0x24220e8 |
| `0077` | `acOutputSmartReq` | 0x94 | @0x242213c |
| `0877` | `acOutputSmartRes` | 0x95 | @0x2422190 |
| `007a` | `setRelaySwitchReq` | 0x96 | @0x24221e4 |
| `087a` | `setRelaySwitchRes` | 0x97 | @0x2422238 |
| `007c` | `setTimingReq` | 0x98 | @0x242228c |
| `087c` | `setTimingRes` | 0x99 | @0x24222e0 |
| `007d` | `getTimingReq` | 0x9a | @0x2422334 |
| `087d` | `getTimingRes` | 0x9b | @0x2422388 |
| `007e` | `setCountdownReq` | 0x9c | @0x24223dc |
| `087e` | `setCountdownRes` | 0x9d | @0x2422430 |
| `007f` | `getCountdownReq` | 0x9e | @0x2422484 |
| `087f` | `getCountdownRes` | 0x9f | @0x24224d8 |
| `007b` | `setLocationLightReq` | 0xa0 | @0x242252c |
| `087b` | `setLocationLightRes` | 0xa1 | @0x2422580 |
| `0490` | `postPbFormatBackupMindData` | 0x23 | @0x24225d4 |
| `0036` | `setMultiDevicesReq` | 0xa2 | @0x2422628 |
| `0836` | `setMultiDevicesRes` | 0xa3 | @0x242267c |
| `0037` | `getMultiDevicesReq` | 0xa4 | @0x24226d0 (shadowed by `getMultiDevicesRes`) |
| `0037` | `getMultiDevicesRes` | 0xa5 | @0x2422724 (later entry wins) |
| `0089` | `getOTAStateReq` | 0xa6 | @0x2422778 |
| `0889` | `getOTAStateRes` | 0xa7 | @0x24227cc |
| `0489` | `upUpgradeCondition` | 0xa8 | @0x2422820 |

Cross-check against the opcodes that have a `### <opcode>` section on the PN pages (grep of the headings). These are keys: `0405` is `postDeviceAllInfoReq`, `0840` is `getAllDeviceInfoRes`, `0500` is `postA17b1DeviceInfoReq`, `0601` is `postA1790DeviceInfoReq`, the A17X8 opcodes `007a`, `007c`, `007d`, `007e` and `007f` are `setRelaySwitchReq`, `setTimingReq`, `getTimingReq`, `setCountdownReq` and `getCountdownReq`, and `0030`, `0057`, `005e`, `005f` and `0067` are `getZXOTAStateReq`, `setDeviceUpdateEnergyReq`, `setSuperChargeReq`, `setBMSSubBatteryPowerSwitchReq` and `bleOtaProgressReq`. These are not keys of either map and decode to `unknown`: `002d`, `0040`, `0050`, `0068`, `0071`, `0073`, `0079`, `0080`, `0081`, `0085`, `009a` and `0408` (the `state_info` family). The enum names are the app's internal decode types; they do not always match the command names of the PN pages (`005e` is `setBackPower` and `setTacticsTime` on [a17c1.md](a17c1.md) but `setSuperChargeReq` here), and the type is used only to choose a parser branch. The pool holds 146 `ZXOpcodeType` objects (every `Obj!ZXOpcodeType` in `pp.txt`, already untagged).

`_parsePayloadData` @0x241ce7c (size 0x7e8) picks the parser by comparing the type with pool constants in this order:

| ZXOpcodeType (index) | parser | source |
|---|---|---|
| `startConnectRes` (0x1) | `parseConnectResponse` | @0x241cf00 |
| `startDisconnectRes` (0x3) | `parseDisconnectResponse` | @0x241cf28 |
| `capabilityNegotiationRes` (0x5) | `parseCapabilitiesNegotiationResponse` | @0x241cf54 |
| `setCapabilityRes` (0x8) | `parseSetCapabilitiesResultResponse` | @0x241cf80 |
| `getDeviceInfoRes` (0xa) | `parseDeviceInfoData` | @0x241cfac |
| `setCapabilityRes` (0x8) again | `parseSetCapabilitiesData`, unreachable because the same constant was compared first | @0x241cfd8 |
| `getPublicKeyRes` (0x12) | `parseGetPublicKeyData` | @0x241d004 |
| `getAesKeyRes` (0xc) | `parseGetAESKeyData` | @0x241d02c |
| `scanWifiRes` (0x14) | `parseScanWIFIData` | @0x241d058 |
| `getWifiListRes` (0x16) | `parseWifiListIData` | @0x241d084 |
| `connectWifiRes` (0x17) | `parseConnectWifiData` | @0x241d0b0 |
| `bindUserIdRes` (0x10) | `parseBindUserIdData` | @0x241d0dc |
| `activateWifiRes` (0x1a) | `parseActivateWifiData` | @0x241d108 |
| `getMultiDevicesRes` (0xa5) | `parseMultiDevicesData` | @0x241d134 |
| `setA17b1CommandRes` (0x6c), `postA17b1DeviceInfoReq` (0x6d), `postA17b1SelfCheckReq` (0x6e), `postDeviceListReq` (0x6f), `postGetUpdateListReq` (0x70), `postA1790DeviceInfoReq` (0x71) | for `setA17b1CommandRes` on a device whose class id is A1790, A1790P, A17C1, A17C5, A17C3 or A17C2 (class ids 8495 and 8496, 8479 to 8482, tested by `add`/`cmp` @0x241d1c8 and @0x241d1d8): `parseCommonData`; every other case: `parseReqJsonData` with the flag "type is `setA17b1CommandRes`" | `parseCommonData` @0x241d270, `parseReqJsonData` @0x241d300 |
| `getScanBluetoothDeviceRes` (0x74), `getUnBindBluetoothDeviceRes` (0x78), `getModuleInfoRes` (0x7a) | `parseBluetoothListIData` | @0x241d354 |
| `getBindBluetoothDeviceRes` (0x76) | `parseY0BindUserIdData` | @0x241d380 |
| `moduleLogUploadRes` (0x8b) | `parseBleLogCommonData` | @0x241d3ac |
| `postAllBMSMinorBatteryWiFiInfoReq` (0x56), `postAllBMSMinorBatteryBTInfoReq` (0x55) on a device of class id 8479 to 8482 | `parseCommonDataWithDataType` | @0x241d42c |
| `postPbFormatBackupMindData` (0x23) | `parseCommonDataWithCustomLengthBytes` with the literal map `{0xa2: 2}` (raw key 324 and value 4 stored into the map-literal array, array length raw 4, halved) | map @0x241d47c, @0x241d484; call @0x241d4b0 |
| every other type (including `unknown` and all post/get/set types of the PN pages) | `isResponseOrRequest(getOpcodeFromType(type, group) or opcodeBytes)` (byte 0 bit 3, [envelope.md](envelope.md#direction-detection)), debug line `isResponse common:`, then `parseCommonData` | @0x241d4e4 to @0x241d600 |

In the last three rows of the table (the BMS row, the `postPbFormatBackupMindData` row and the "every other type" row) the first TLV parser argument "isResponse" comes from the canonical opcode bytes of the type, not from the received bytes (the received bytes are used only when `getOpcodeFromType` finds no key). The parsers share a decrypt step: when the encrypted flag (p7) is set, `AesHelper.aesGcmDecrypt(payload, bleMac)` @0x241fb70 runs if the bool `field_3f` of the device object is true, otherwise `AesHelper.decrypt(payload, bleMac)` @0x241fb88 (a null result becomes an empty list); `parseCommonDataWithDataType` has the same step @0x241e4f8 and @0x241e510. With the flag clear the payload is copied unchanged.

`parseCommonData(payload, isResponse, bleMac, device, encrypted)` @0x241f9a0 (size 0x538), the TLV parser behind the per-PN `parseDeviceAllInfo` maps:

| tag | name | rule | unit/scale | required | source |
|---|---|---|---|---|---|
| c1 | status byte | when `isResponse`: `map["a0"] = payload[0]` (`indexString(160)`); a payload of exactly one byte (tagged length compare `cmp w0,#2` = 1) returns the map; otherwise parsing starts at index 1; when not a response it starts at index 0 | | no | @0x241fbc0, @0x241fc1c, @0x241fc34 |
| c2 | first entry | the loop variable starts at 161 (0xa1, unboxed); while it equals 0xa1 (the first iteration) the entry is read by a separate branch: key `a1`, length byte L at `i+1`, value from `i+2`, next entry at `i+2+L`; afterwards the variable is 162 (@0x241fd6c) and, in the generic branch, the previous tag byte | | yes | @0x241fc4c, @0x241fc78 (audit row 48), advance @0x241fca4 to @0x241fcb4 |
| c3 | other entries | tag `payload[i]`, length byte L = `payload[i+1]` (it counts the type byte), type byte at `i+2` is skipped, value = `payload[i+3 .. i+2+L)`, key = two lowercase hex digits of the tag (`bytesToHexString`), next entry at `i+2+L` | bytes | yes | @0x241fd90 to @0x241fe0c (audit row 49), advance @0x241fe84 |
| c4 | result | `Map<String, List<int>>` of tag key to raw value bytes (plus `a0`); typed conversion and scaling happen later in the per-PN parser | | yes | return @0x241fea8 |

`parseCommonDataWithCustomLengthBytes` @0x241d664 (size 0x800) reads the width of the length field of a tag from its map argument and defaults to 1 byte (`r5 = 1` @0x241d940), builds `lenList = payload.sublist(i, i+width)` @0x241da24 and `length = listToInt(lenList)` (little endian, audit row 52) @0x241da30; tag 0xa1 is special-cased (`cmp w3,#0x142`, tagged, = 0xa1 @0x241db5c, audit row 50). The caller literal above fills audit row 51: only `postPbFormatBackupMindData` passes a width, tag 0xa2 with 2 bytes. The superseded `BLE_COMMAND_MAP.md` at the repository root says tag `0xA2` "might use a 4-byte length prefix": the raw immediate 4 sits in a 32-bit array slot, so the real width is 2 bytes (Smi rule); the same file lists five parsers for the dispatch, the table above has all of them. `parseCommonDataWithDataType` @0x241e3d8 (size 0x424) reads tag, length and a type byte per entry and returns entries with the keys `index` (tag, two hex digits, `padLeft` with `"0"` @0x241e718), `length`, `dataType` and `data` @0x241e740 to @0x241e77c.

`BleStatusCode.getCmdStatus(int)` ble_status_code.dart @0x241ce1c (size 0x60) looks the status byte up in a 17-entry const map `Map<int, BleCmdStatus>` ([pp+0xe480], keys 0x0 to 0x6, 0x21 to 0x25, 0x71, 0x72, 0x9, 0xa, 0xb) and returns the enum value `unknown` (index 0x11, [pp+0xe488]) for a miss. Only four values have a name in `pp.txt`: key 0x0 `success` (index 0x0), key 0x5 `noMoreData` (0x5), key 0x9 `needAuthentication` (0xe), key 0xa `passwordWrongAuthenticationFailed` (0xf), key 0xb `passwordRetryCountExceededAuthenticationFailed` (0x10).

#### Example

synthesized decode-side example (built from the rules above, not a capture; XOR byte computed over the 16 preceding bytes; the send-side convention and its worked example live on [a17x8.md](a17x8.md#007a-setrelayswitchcmd))

```text
ff 09 11 00 03 00 0f 04 05 a1 01 22 a2 02 01 07 ce
length 17 (0x11, includes the XOR byte)   opcode bytes 04 05   byte 6 = 0x0f -> chargingOpcodeMap
key "0405" -> postDeviceAllInfoReq (index 0x52); isResponse false (0x04 & 0x08 = 0)
payload = a1 01 22 a2 02 01 07 (bytes 9..15)
parseCommonData -> {"a1": [0x22], "a2": [0x07]}   (type byte 0x01 of a2 skipped)
```

#### Related API endpoint

none; the typed fields of these frames are documented per PN, see [upstream_commands.md](upstream_commands.md) for the opcode index.

#### Since/changed

The `pps_device_commands.dart` helper constants are unchanged in 3.18.0: `parseResponse`, `parseCommonData` and the dispatch chain use the same compare values (0x40 after the 0xf0 mask, 0xa1, 0xa2, 10, the 7/9 opcode window) and the same parser order. The two opcode maps are identical: 125 and 22 pairs with the same keys, enum names and enum indices (3.18.0 `pps_device_commands.dart` maps @0x1e22a48 and @0x1e25194, same sizes 0x274c and 0x608). Function sizes shrank because debug logging was removed (3.18.0 logged `parseResponse,data:` and `,bleMac:`): `parseResponse` 0x5e8 to 0x560, `_parsePayloadData` 0x9e8 to 0x7e8, `parseCommonData` 0x578 to 0x538, `parseCommonDataWithCustomLengthBytes` 0xa2c to 0x800, `getOpcodeType` 0x308 to 0x2f0, `getOpcodeFromCmd` 0xa4 to 0xac. Tag: asm-traced (3.24.3 side).

#### Known unknowns

- Which frames carry an opcode byte with upper nibble 4 (the encrypted flag) is open. The status frames of the PN pages use `04 05` (upper nibble 0), so they are parsed without a decrypt step. The AES key and IV derivation of `AesHelper` (`charging/ble_zx/helper/aes_helper.dart`) from `bleMac` is not read here.
- The value range of the first (`a1`) entry rests on the start register left by pps_device_commands.dart @0x241fca4 at the `sublist` call @0x241fcdc; the generic branch passes its start explicitly. If the Mint-allocation path of `BoxInt64Instr` @0x241fcbc ran it would clobber that register; the inline path does not.
- Byte 9 is the status byte of a response in the app (only when the canonical opcode of the type has bit 3 set); upstream calls byte 9 an optional increment byte (`api/mqtttypes.py` lines 71-76). How the two views fit for a response with a non-response opcode key is not established.
- `getCmdStatus` names are known for five of the 17 keys; the other twelve enum objects have no printed name in `pp.txt`.
- Several names look swapped relative to the response bit (`0069` is `deviceFactorySettingRes` and `0869` is `deviceFactorySettingReq`; `0406` is listed as `postUpgradeStateRes` and then `postUpgradeStateReq`), and seven keys are shadowed duplicates; whether this is intended is unknown.
- `ZXCommandTransformer.validateCommand` zx_command_transformer.dart @0x4789138 (XOR check through `_isLegallyCmd`, see above), `unpackCmd` @0x478a3a0 and `_checkStickyPack` @0x478a5dc form the BLE multi-packet reassembly; they were not traced as MQTT-reachable and only the checksum compare was read.
- `parseDeviceInfoData` and the other ZX common parsers (Wi-Fi provisioning and key exchange) are listed but their field maps are out of scope; `decodeResponse` pps_device_commands.dart @0x3b45e64 (a second decrypt entry, only called from the A1790 controller) was not read.

#### Device-tested by

none.

### Fallback handler (IotDeviceController)

#### Purpose

Documents what the generic controller does with a decoded frame: which opcode types it acts on and which events it fires.

#### Upstream name

none (upstream has no per-device controller; its generic hex decode is `DeviceHexData` with a model-specific field map).

#### Command code

none; it reacts to `ZXOpcodeType` values, listed under Payload fields.

#### Direction

device→app. Tag: asm-traced.

#### Topic pattern

`param_info` only, see [the receive path](#mqtt-receive-path-and-topic-gate).

#### Payload fields

`IotDeviceController._handleResponse(bytes)` iot_anker_controller.dart @0x3b69dd8 (size 0xcc4):

| tag | name | rule | unit/scale | required | source |
|---|---|---|---|---|---|
| f1 | type | `PPSDeviceCommands.getOpcodeFromCmd(bytes)` (the byte at index 6, raw 12, is read first and the result is discarded) | enum | yes | @0x3b69e14, @0x3b69e2c |
| f2 | gate | continues when the type is not a value of `commonOpcodeMap`, or when it is `getDeviceInfoRes`; every other common-map type returns (the `getDeviceInfoRes` compare is redundant because that type is itself in the common map) | | yes | `contains` @0x3b69f48, compare @0x3b69f54 |
| f3 | decode | `parseResponse(bytes, <device getter>, device: device)`, then `PAYLOAD_KEY` and `OPCODE_KEY` | maps | yes | @0x3b69fb0, @0x3b69fc4, @0x3b69ffc |
| f4 | decrypt-failure log | a payload that is a `List` and answers true to a dispatch-table getter (the selector is not resolved) logs `解密失败` (decrypt failed) | | no | @0x3b6a0fc, @0x3b6a1ac |
| f5 | branch 1 | type `getZXOTAStateRes` (0x39, [pp+0x10b10]): reads payload keys `a1` and `a2` (`indexString` arguments 161 and 162), each an `Iterable<int>`, converts both with `String.fromCharCodes` and assigns them to two device properties; logs `获取到模组版本信息` (module version info obtained) | 2 strings | no | compare @0x3b6a1e0, reads @0x3b6a1f4 and @0x3b6a220, conversion @0x3b6a2ec and @0x3b6a358 |
| f6 | branch 2 | type `postUpgradeStateReq` (0x65, [pp+0x108b8]) or `OPCODE_KEY == [0x3, 0x6]` (`listEquals` against the pool list @0x3b6a4dc): `parseOTAUpdateProgress(payload)` (@0x3b2c848, size 0x678), then two `MessageEvent` fires | | no | compares @0x3b6a48c and @0x3b6a4ec, parse @0x3b6a51c |
| f6a | event 1 | `MessageEvent(code 0x24c = 588, {device, data: progress})` (64-bit store, real) | | | @0x3b6a5c4, fire @0x3b6a5dc |
| f6b | event 2 | `MessageEvent(code 0x10cd = 4301, {data: progress})` | | | @0x3b6a620, fire @0x3b6a638 |
| f7 | branch 3 | type `postPbFormatBackupMindData` (0x23, [pp+0xe568]): returns early when a boolean getter of the payload (selector not resolved) is true; else `a2` (`indexString(162)`) base64-encoded, `a3` (`indexString(163)`) UTF-8 decoded with `\x00` removed (file name), then `MessageEvent(code 1357, {device, data, pbFileName})` and `postEventData(..., "pb")` | | no | compare @0x3b6a654, reads @0x3b6a708 and @0x3b6a7b4, event @0x3b6a9b0, call @0x3b6aa64 |

Any other type is ignored after `parseResponse` has run: the controller has no per-PN field map, so a `postDeviceAllInfoReq` (`0405`) frame is decoded into its tag map and dropped. The file contains no reference to `parseDeviceAllInfo` or to a per-PN command class (grep, 0 hits in `iot_anker_controller.dart` and `iot_anker_device.dart`). In the per-PN controllers the same type names lead to the `parseDeviceAllInfo` calls: the nearest preceding `ZXOpcodeType` constants are `postDeviceAllInfoReq`/`getAllDeviceInfoRes` in the A1753 (a1753_device_controller.dart @0x3b754c4), A17C0 (a17C0_device_controller.dart @0x3b4f938) and A17X8 (a17x8_device_controller.dart @0x3b62800) controllers, `postDeviceAllInfoReq` in the Shelly controller (shelly_device_controller.dart @0x3b61028) and `postA17b1DeviceInfoReq` in the A17B1 controller (a17b1_device_controller.dart @0x3b48a38).

The send side of the fallback controller builds only OTA and info requests: `getOTAState` sends `[0, 0x30]` iot_anker_controller.dart @0x24104f0, `getDeviceOTAState` `[0, 0x89]` @0x2410a3c, and the sub-package sender uses the pool lists `[0, 0x2e]` @0x45636bc and `[0, 0x2f]` @0x4614744 through `sendCommandWithParam` @0x2410528 (pool lists are real byte values). These opcodes are request keys of the charging map (`0030` is `getZXOTAStateReq`, `0089` is `getOTAStateReq`, `002e` is `sendOtaSubPackageReq`).

#### Example

synthesized

```text
frame opcode 03 06  (masked key "0306", not in either map -> type unknown)
branch 2 matches by OPCODE_KEY == [3, 6] -> parseOTAUpdateProgress -> MessageEvent 588 and 4301
```

#### Related API endpoint

none; the OTA progress is consumed by the OTA UI pages through the event bus, not through an API endpoint.

#### Since/changed

`_handleResponse` is 0xe1c bytes in 3.18.0 (3.18.0 `charging/ble/device/iot_anker_controller.dart` @0x341fc38) and 0xcc4 in 3.24.3; the 3.24.3 body has the same gate, the same three branches, the same tags (161, 162, 163) and the same event codes (588, 4301, 1357). The 3.18.0 version also logged the OTA progress (`准备发送进度 iot上报OTA升级进度：opcode: ... , payload: ...`, debounce key `iot_ota_progress_`); that log is gone. The classes moved: 3.18.0 kept `IotAnkerDevice` in one 11033-line file with instance size 0x19c; 3.24.3 splits it into `iot_anker_device.dart` (687 lines, size 0x20c) and the new `base_service/device/iot_device_adapter.dart`, `device_iot_base.dart` and `ak_base_contract/src/iot_ak_result.dart` (none of the three exists in the 3.18.0 tree). `IotDeviceController` went from 0x74 to 0x68 bytes. Tag: asm-traced (3.24.3 side).

#### Known unknowns

- The two device properties that receive the module version strings in branch 1 (dispatch-table setters, selectors not resolved) and the meaning of the two tags: `IotDeviceAdapter` has `otaMcuVersion` iot_device_adapter.dart @0x3b161d4 and `otaModuleVersion` @0x407bd9c as getters, which would fit the two strings; the setters were not matched to them.
- Whether the opcode `0306` ever occurs on the wire: branch 2 accepts it, but no frame source or builder for it was found.
- Which products reach this controller in practice (the factory's fallback is for every PN not in the 50 routed literals; see [Product routing](#product-routing-createbyproductcode)).
- The `postPbFormatBackupMindData` data (tag `a2`, tag `a3` as a file name) is only forwarded as an event; its consumer page and format were not read.

#### Device-tested by

none.
