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
- Negotiation and BLE use, app side: `AE1X0` and `AE1R0` are registered SDK product codes (`IotAnkerDeviceConfig.register` calls in `third_device/src/module/ae1x0/ae1x0_module.dart @0x45df200` and `third_device/src/module/ae1r0/ae1r0_module.dart @0x45de564`), so `BleHandler._getCurrentImpl` returns `BleHandlerImpl2` for them; that handler has no reference to `ZXBleConfer`, and the negotiation is the kit's, which runs in the native plugin and is not in the Dart asm ([handshake.md](handshake.md#which-implementation-runs-for-a-product)). BLE is used app side: `AE1X0HomeLogic.reconnectBle` (`third_device/src/module/ae1x0/home/ae1x0_home_logic.dart @0x3af086c`; log text `AE1X0HomeLogic: ble reconnect --->>> [` `@0x3af0954`) calls `PermissionUtilsProvider.checkBTEnable` (`@0x3af089c`) and then `AnkerBleConnectUtils.checkPermissionAndReconnect` (`base_service/util/ble_connect_utils.dart`, call `@0x3af0934`); the AE1R0 home logic has the same pair (`third_device/src/module/ae1r0/home/ae1r0_home_logic.dart @0x3ae20e4`, `@0x3ae21bc`, log texts `AE1R0HomeLogic: ble reconnect success` and `... failed`). The reconnect helper ends in `HomeDeviceManagerProvider.startScanWithConnect` (`ble_connect_utils.dart @0x24518a4`); see the open item below.

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

- Whether the reconnect helper reaches `BleHandler.startScanWithConnect`: the same open item as on [a17e2.md](a17e2.md) (service-locator dispatch behind `HomeDeviceManagerProvider.startScanWithConnect`). — traced 2026-10-20: see [a17e2.md](a17e2.md).

BLE is unavailable while the device is on WiFi; see `ble/protocol.md` (community finding, see protocol.md; not asm-traced).

#### Device-tested by

none.

## Known unknowns on this page

Tag: untagged by design (no API fact).

- What the kit's negotiation does for these codes (stages, key derivation): it runs in the native plugin — reclassified: native plugin, not in Dart asm, [device test row 123](../docs/DEVICE_TEST_BACKLOG.md#added-2026-10-20-depth-pass).
- Device-test status: no BLE session against a real device is recorded in this repository.

