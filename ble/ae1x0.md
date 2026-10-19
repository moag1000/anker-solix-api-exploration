> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# AE1X0 and AE1R0 (meters) BLE

The AE1X0 Meter and the P1 Energy Tracker (AE1R0); both are new `ProductModel` entries in 3.24.3. There is no `charging/ble/device/` directory for either. This page owns the BLE-specific facts of the product; the command payloads (opcodes, TLV tags, scales) are owned by no MQTT page (the product is not covered by [../mqtt/README.md](../mqtt/README.md)); the BLE opcode lists below are the only command facts this repository has for it. The frame, fragmentation and encryption are on [protocol.md](protocol.md), the negotiation on [handshake.md](handshake.md).

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
| AE1X0 | AE1X0 Meter | ZX family | yes | none | product_model.dart @0x22c3440 |
| AE1R0 | P1 Energy Tracker | ZX family | yes | none | product_model.dart @0x22c33d0 |

Connection status family (`AnkerDevice.updateStatus`, `base_service/device/anker_device.dart @0x22054c4`; the three families are described on [protocol.md](protocol.md#connection-routing-and-the-wifi-exclusion-rule)):

| code | family | test site |
|---|---|---|
| AE1X0 | not tested in `updateStatus` | none |
| AE1R0 | not tested in `updateStatus` | none |


Notes on this product:

- The factory has no branch for these codes. Both are in the product-scan map and use the ZX UUID triple; `DeviceConstant.shouldSkipWifiConfig` lists `AE1R0` together with the Shelly codes and `ECOIR`, that is the app skips its WiFi configuration step for it (`device_constant.dart @0x3913364`).
- The BLE use of the two meters was not traced.

## Commands

### No device class in the BLE package

#### Purpose

Records that the product has no device class and no controller under `charging/ble/device/`: the factory has no branch for its codes, so none of the methods or opcode lists on the other `ble/<pn>.md` pages applies to it.

#### Upstream name

none for the sequence; the opcode names are the app's `ZXOpcodeType` members (no upstream name).

#### Opcode

none: no device-class file and no pool opcode list exist for these codes in `charging/ble/device/`.

#### Direction

not applicable: no BLE method of this package exists for the product.

#### Packet framing

not applicable here; if the product is spoken to over BLE at all, the frame is the one of [protocol.md](protocol.md#frame-on-ble).

#### Handshake prerequisite

not applicable here; the generic handshake is on [handshake.md](handshake.md).

#### TLV tags

none: no BLE command of this package for the product.

#### Example

none: no capture of a handshake exists in this repository.

#### Related API endpoint

none: the handshake has no MQTT twin and the product has no MQTT page.

#### Since/changed

3.18.0: no device class either. 3.24.3: no device class; the `ProductModel` of AE1X0, AE1R0 is new in 3.24.3 (see [protocol.md](protocol.md#since-3180)).

#### Known unknowns

- Which negotiation implementation runs for this product, the Dart conferer or the native kit ([handshake.md](handshake.md#known-unknowns)).
- Whether and how BLE is used for these products: the `micro_hes` and `ak_soft_ems` modules were not traced for their transport.

BLE is unavailable while the device is on WiFi; see `ble/protocol.md`.

#### Device-tested by

none.

## Known unknowns on this page

Tag: untagged by design (no API fact).

- Whether the product is negotiated by the Dart conferers or by the native kit ([handshake.md](handshake.md#two-implementations)).
- Device-test status: no BLE session against a real device is recorded in this repository.

