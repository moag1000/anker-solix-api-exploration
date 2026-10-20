> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# SHEM3, SHEMP3, SHPPS (Shelly 3EM, 3EM Pro, Plus Plug S) BLE

The third-party Shelly devices that the app handles with its own BLE class (Shelly 3EM, Shelly 3EM Pro, Shelly Plus Plug S). This page owns the BLE-specific facts of the product; the command payloads (opcodes, TLV tags, scales) are owned by the MQTT page [../mqtt/shelly.md](../mqtt/shelly.md) and are not repeated here. The frame, fragmentation and encryption are on [protocol.md](protocol.md), the negotiation on [handshake.md](handshake.md).

Evidence is the asm of 3.24.3 (`file.dart @0xADDR`, relative to `charging/ble/device/` unless a path is given). Pool lists such as `[0, 0x5e]` are real values. A row that says `no` in the column `on the MQTT page` means the opcode is not mentioned on the linked page; it can still be a command that also goes over MQTT.

## Contents

1. [BLE profile](#ble-profile)
1. [Commands](#commands)
1. [Known unknowns on this page](#known-unknowns-on-this-page)

## BLE profile

Tag: asm-traced.

Products (from `product_model.dart`; the UUID values are in the table of [protocol.md](protocol.md#gatt-profile-per-product)):

| code | name | GATT group | BLE map | factory branch | ProductModel |
|---|---|---|---|---|---|
| SHEM3 | Shelly3EM | ZX family | no | `ShellyDevice` device_factory_impl.dart @0x240f2d0 | product_model.dart @0x22c2f18 |
| SHEMP3 | Shelly3EM Pro | ZX family | no | `ShellyProDevice` device_factory_impl.dart @0x240f32c | product_model.dart @0x22c2ea8 |
| SHPPS | Shelly Plus Plug S | ZX family | no | `ShellyPlugDevice` device_factory_impl.dart @0x240dba0 | product_model.dart @0x22c2e38 |

Device classes in this directory (base class as printed in the asm; `_MixinApplication` names are Dart's synthetic mixin classes):

| class | extends | file |
|---|---|---|
| `ShellyDevice` | `AnkerDevice&PpsDeviceFeature&ZXBleFeature` | `Shelly/shelly/shelly_device.dart` |
| `ShellyDeviceCommands` | `Object` | `Shelly/shelly/shelly_device_commands.dart` |
| `ShellyDeviceController` | `DeviceController&PpsDeviceFeature&DeviceLogFeature` | `Shelly/shelly/shelly_device_controller.dart` |
| `ShellyPlugDevice` | `ShellyDevice` | `Shelly/shelly_plug_device.dart` |
| `ShellyProDevice` | `ShellyDevice` | `Shelly/shelly_pro_device.dart` |

Connection status family (`AnkerDevice.updateStatus`, `base_service/device/anker_device.dart @0x22054c4`; the three families are described on [protocol.md](protocol.md#connection-routing-and-the-wifi-exclusion-rule)):

| code | family | test site |
|---|---|---|
| SHEM3 | not tested in `updateStatus` | none |
| SHEMP3 | not tested in `updateStatus` | none |
| SHPPS | not tested in `updateStatus` | none |


Notes on this product:

- `ShellyDevice` mixes in `ZXBleFeature` and `PpsDeviceFeature`; `ShellyProDevice` and `ShellyPlugDevice` extend it. The factory builds `ShellyDevice` for `SHEM3`, `ShellyProDevice` for `SHEMP3` and `ShellyPlugDevice` for `SHPPS` (`device_factory_impl.dart @0x240f2d0`, `@0x240f32c`, `@0x240f388`). The ProductModels use the ZX GATT triple, and `shelly_device.dart` holds the full-form scan UUID as a literal (`@0x36c0284`, see [protocol.md](protocol.md#gatt-profile-per-product)).
- The device class implements the same handshake methods as the Solix classes (`startConnect`, `capabilitiesNegotiation`, `setCapability`, `getPublicKey`, `getAESKey`, `bindUserId`, `getDeviceBasicInfo`), so a Shelly device is negotiated with the ZX handshake. `DeviceConstant.shouldSkipWifiConfig` lists `SHEM3`, `SHEMP3` and `SHPPS`; none of the three is in the product-scan map `ankerProductForBleMap` ([../reference/enums.md](../reference/enums.md#code-lists)).
- Negotiation, app side: `ShellyDevice` and its two subclasses (class ids 8459 to 8461) have `ZXBleFeature` in their `extends` lines and `SHEM3`, `SHEMP3` and `SHPPS` are not registered SDK product codes, so `BleHandler` picks `BleHandlerImpl1`, whose `_authDevice` starts the Dart `ZXBleConfer`. Which of the three conferers then runs depends on the capability response, not on the product ([handshake.md](handshake.md#which-implementation-runs-for-a-product)).

## Commands

### Device-class methods

#### Purpose

Lists the non-controller operations of the device class: the methods that carry the ZX handshake (capability exchange, key setup, account binding), the status request and the opcode each uses.

#### Upstream name

none for the sequence; the opcode names are the app's `ZXOpcodeType` members (no upstream name).

#### Opcode

Tag: asm-traced.

`ShellyDevice` extends `_MixinApplication306&AnkerDevice&PpsDeviceFeature&ZXBleFeature` and defines the methods below itself; `startConnect` and the other ZX methods that it does not define come from that shared mixin application (the same one that `A17B1AnkerDevice.startConnect` calls, `a17b1_anker_device.dart @0x3725d3c`), which is not a per-product file. Sites are in `third_party_device/Shelly/shelly/shelly_device.dart`.

| method | group | opcode | site |
|---|---|---|---|
| `bindUserId` | handshake | `0023` | shelly_device.dart @0x3364408 |
| `setCapability` | handshake | `0005` | shelly_device.dart @0x3663c84 |
| `getPublicKey` | handshake | `0021` | shelly_device.dart @0x36b5fc0 |
| `getDeviceBasicInfo` | handshake | `0029` | shelly_device.dart @0x36c47b8 |
| `capabilitiesNegotiation` | handshake | `0003` | shelly_device.dart @0x36d15ac |
| `getAESKey` | handshake | `0022` | shelly_device.dart @0x3b03944 |
| `sendDeviceInfoCmd` | status request | `0040` | shelly_device.dart @0x3b0eb10 |

#### Direction

both: requests go app to device, the responses (`08xx` in the common map, [handshake.md](handshake.md#opcode-pairs)) come back device to app.

#### Packet framing

[protocol.md](protocol.md#frame-on-ble); the handshake frames carry the flag bits of [protocol.md](protocol.md#opcode-byte-0-flags).

#### Handshake prerequisite

The rows of group `handshake` are the handshake. Which conferer runs (`SecureEcdhConfer`, `EcdhConfer` or `AesConferV1`) is chosen from the capability response, not from the product: [handshake.md](handshake.md#capability-negotiation-response). The other rows are ordinary commands that need a completed handshake for encrypted frames.

#### TLV tags

The handshake payloads are positional bytes or single tags and are not per-product; they are described in [handshake.md](handshake.md#capability-negotiation-response) and [handshake.md](handshake.md#the-three-conferers). The payloads of the WiFi, OTA and status-request rows were not decoded for this page.

#### Example

none: no capture of a handshake exists in this repository.

#### Related API endpoint

MQTT twin and device page: [../mqtt/shelly.md](../mqtt/shelly.md). The handshake itself has no MQTT twin.

#### Since/changed

3.18.0: the same device-class files. 3.24.3: the opcode set of the device-class file(s) is unchanged; the `ProductModel` of SHEM3, SHEMP3, SHPPS existed in 3.18.0 (see [protocol.md](protocol.md#since-3180)).

#### Known unknowns

none.

BLE is unavailable while the device is on WiFi; see `ble/protocol.md` (community finding, see protocol.md; not asm-traced).

#### Device-tested by

none.

### Controller send set

#### Purpose

Lists the command opcodes that the controller class of this product writes over BLE, each tied to the controller method that uses it.

#### Upstream name

none for the methods (the app's method names are used); the upstream constant for an opcode is indexed on [../mqtt/upstream_commands.md](../mqtt/upstream_commands.md).

#### Opcode

Tag: asm-traced.

| method | opcode | on the MQTT page | site |
|---|---|---|---|
| `getOTAState` | `0030` | no | shelly_device_controller.dart @0x2418070 |
| `setDeviceUpdateEnergy` | `0057` | no | shelly_device_controller.dart @0x4081c38 |
| `getOTAInfo` | `0063` | no | shelly_device_controller.dart @0x4563398 |
| `getOTAInfo` | `002e` | no | shelly_device_controller.dart @0x45633a4 |
| `sendSubPackageData` | `0064` | no | shelly_device_controller.dart @0x4614414 |
| `sendSubPackageData` | `002f` | no | shelly_device_controller.dart @0x4614420 |

#### Direction

app to device for the requests; the matching responses and the periodic status push `0405` (`postDeviceAllInfoReq` in the charging map, [protocol.md](protocol.md#zx-opcode-names)) come back device to app.

#### Packet framing

[protocol.md](protocol.md#frame-on-ble) and [protocol.md](protocol.md#fragmentation); the controller's `sendCommand` waits 5 s by default ([protocol.md](protocol.md#timeouts-and-limits)).

#### Handshake prerequisite

A completed handshake is needed for encrypted commands: the frame builder encrypts only when the device has a key ([protocol.md](protocol.md#payload-encryption)).

#### TLV tags

Owned by the linked MQTT page: [../mqtt/shelly.md](../mqtt/shelly.md). Opcodes marked `no` in the table have no tag table there. Their payload shapes, read from the controller methods (shape definitions: [protocol.md](protocol.md#controller-send-wrappers)): `getOTAInfo` and `sendSubPackageData` (shape OTA info and OTA data); `getOTAState` (shape OTA state); `setDeviceUpdateEnergy` (`0057`, `shelly_device_controller.dart @0x4081c38`) builds the same map but passes it as a positional argument (call descriptor `[0, 0x4, 0, 0x4, null]`). Response handling: none in these methods, see the end of [Controller send wrappers](protocol.md#controller-send-wrappers).

#### Example

none: the MQTT pages hold the synthesized frames of their products; this page adds none.

#### Related API endpoint

MQTT twin: [../mqtt/shelly.md](../mqtt/shelly.md)

#### Since/changed

3.18.0: the controller file(s) exist. 3.24.3: the opcode set is unchanged.

#### Known unknowns

- Rows marked `no` may be commands that are MQTT-only on the cloud side or simply undocumented on the MQTT page; this page does not decide which.

BLE is unavailable while the device is on WiFi; see `ble/protocol.md` (community finding, see protocol.md; not asm-traced).

#### Device-tested by

none recorded on this page.

## Known unknowns on this page

Tag: untagged by design (no API fact).

- Device-test status: no BLE session against a real device is recorded in this repository.

