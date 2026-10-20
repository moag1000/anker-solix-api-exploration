> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# Enums and product codes

This page owns the enum value tables and the product-code classification that the BLE, MQTT, device and flow pages refer to. It replaces the deleted root document `ENUMS.md`, whose numbers the audit [../docs/audit/ENUMS.md](../docs/audit/ENUMS.md) checked against the asm, and the enum tables of the deleted `BLE_COMMAND_MAP.md` (rows 103 to 160 of [../docs/audit/BLE_COMMAND_MAP.md](../docs/audit/BLE_COMMAND_MAP.md), written `audit row N`). Rows of the ENUMS audit carry no number; they are cited by the `doc line` column and written `ENUMS audit, doc lines A to B`.

How the values were read. An enum member is a constant object in the pool (`pp.txt`), printed as `Obj!<Enum>@... { off_8: <index>, off_10: "<name>", off_14: <value> }`. `off_8` is the enum index (the position in the declaration), `off_10` the name and `off_14` the optional wire value that the enum declares for itself. Pool objects are real values: the Smi rule of [../METHODOLOGY.md](../METHODOLOGY.md#smi-rule-reading-numbers-from-blutter-output) concerns register immediates and does not apply to them. The `site` column of each table gives the first asm instruction that loads the pool object (`file.dart @0xADDR`), found by scanning the 3.24.3 asm for the pool offset; it proves the member is referenced, it is not the only place. A table is complete for the members that exist in the pool; a member that the app declares but never loads is not in the pool dump and is listed under [Known unknowns](#known-unknowns). Tag: asm-traced unless a row or section says otherwise.

## Contents

1. [Product codes](#product-codes)
1. [Device and connection enums](#device-and-connection-enums)
1. [BLE and MQTT protocol enums](#ble-and-mqtt-protocol-enums)
1. [Device-type and product-category enums](#device-type-and-product-category-enums)
1. [Energy, mode and price enums](#energy-mode-and-price-enums)
1. [Device-specific enums](#device-specific-enums)
1. [String lists](#string-lists)
1. [Since 3.18.0](#since-3180)
1. [Known unknowns](#known-unknowns)

## Product codes

### ProductModel table

Tag: asm-traced.

`base_service/model/product_model.dart` has one static function per product that builds a `ProductModel` (fields `productCode`, `name`, `labelName`, the GATT UUIDs and, new in 3.24.3, two more string fields that are empty in every model). The table lists all 69 models of 3.24.3. `GATT group` is the UUID family from [../ble/protocol.md](../ble/protocol.md#gatt-profile-per-product) (the UUID values are there); `BLE map` says whether the model is in `ankerProductForBleMap`, the set the app scans for; `function` is the start address of the `<pn>Model()` function in `product_model.dart`. The name column is the literal string of the model (`name` and `labelName` are equal except for A17A4, whose label lacks the trailing `L`). Where the upstream library knows a product under another name, upstream wins for display (`api/apitypes.py`, `SolixDeviceCapacity` comments, upstream-confirmed): A17E2 is "Solarbank Max AC" there and AE103 "SOLIX Solarbank 4 E5000 Pro", while the app strings are "Solarbank Prime AC" and "Solarbank AE103"; A110A and A110B are Prime power banks (300 W and 220 W).

| code | name | GATT group | BLE map | BLE page | MQTT page | function |
|---|---|---|---|---|---|---|
| A120J | 160W Prime Charger | ZX | no | none | none | product_model.dart @0x45a6524 |
| A1340 | Prime Power Bank | power bank (2215) | yes | [a1340.md](../ble/a1340.md) | [a1340.md](../mqtt/a1340.md) | product_model.dart @0x22c4698 |
| A1722 | SOLIX C300 | ZX | yes | [a172x.md](../ble/a172x.md) | [a172x.md](../mqtt/a172x.md) | product_model.dart @0x22c3e48 |
| A1723 | SOLIX C300X | ZX | yes | [a172x.md](../ble/a172x.md) | [a172x.md](../mqtt/a172x.md) | product_model.dart @0x22c3dd8 |
| A1725 | SOLIX C200(X) | ZX | yes | [a172x.md](../ble/a172x.md) | [a172x.md](../mqtt/a172x.md) | product_model.dart @0x22c3d68 |
| A1726 | SOLIX C300 DC | ZX | yes | [a172x.md](../ble/a172x.md) | [a172x.md](../mqtt/a172x.md) | product_model.dart @0x22c3cf8 |
| A1727 | SOLIX C200 DC | ZX | yes | [a172x.md](../ble/a172x.md) | [a172x.md](../mqtt/a172x.md) | product_model.dart @0x22c3c88 |
| A1728 | SOLIX C300X DC | ZX | yes | [a172x.md](../ble/a172x.md) | [a172x.md](../mqtt/a172x.md) | product_model.dart @0x22c3c18 |
| A1729 | SOLIX C200X DC | ZX | yes | [a172x.md](../ble/a172x.md) | [a172x.md](../mqtt/a172x.md) | product_model.dart @0x22c3ba8 |
| A1753 | SOLIX C800 | ZX | yes | [a1753.md](../ble/a1753.md) | [a1753.md](../mqtt/a1753.md) | product_model.dart @0x22c45b8 |
| A1754 | SOLIX C800 Plus | ZX | yes | [a1753.md](../ble/a1753.md) | [a1753.md](../mqtt/a1753.md) | product_model.dart @0x22c4548 |
| A1755 | SOLIX C800X | ZX | yes | [a1753.md](../ble/a1753.md) | [a1753.md](../mqtt/a1753.md) | product_model.dart @0x22c44d8 |
| A1761 | SOLIX C1000(X) | ZX | yes | [a1753.md](../ble/a1753.md) | [a1753.md](../mqtt/a1753.md) | product_model.dart @0x22c4468 |
| A1762 | Portable Power Station 1000 | ZX | yes | [a1753.md](../ble/a1753.md) | [a1753.md](../mqtt/a1753.md) | product_model.dart @0x22c43f8 |
| A1763 | SOLIX C1000 Gen 2 | ZX | no | none | none | product_model.dart @0x22c32c0 |
| A1770 | F1200 (Bluetooth) | legacy F5DA | yes | [a1770.md](../ble/a1770.md) | none | product_model.dart @0x22c49b0 |
| A1771 | F1200 (Bluetooth and WLAN) | F1200 (2540) | yes | [a1771.md](../ble/a1771.md) | [a1771.md](../mqtt/a1771.md) | product_model.dart @0x22c4628 |
| A1772 | SOLIX F1500 | ZX | yes | [a1772.md](../ble/a1772.md) | none | product_model.dart @0x22c4158 |
| A1780 | 767 PowerHouse (SOLIX F2000) | legacy F5DA | yes | [a1780.md](../ble/a1780.md) | [a1780.md](../mqtt/a1780.md) | product_model.dart @0x22c4a20 |
| A1780P | 767 Power House (SOLIX F2000) with WLAN | ZX | yes | [a1780p.md](../ble/a1780p.md) | none | product_model.dart @0x22c41c8 |
| A1781 | SOLIX F2600 | ZX | yes | [a1781.md](../ble/a1781.md) | none | product_model.dart @0x22c4238 |
| A1782 | SOLIX F3000 | ZX | no | none | none | product_model.dart @0x22c2ff8 |
| A1783 | SOLIX C2000 Gen 2 | ZX | no | none | none | product_model.dart @0x22c2f88 |
| A1790 | SOLIX F3800 | ZX | yes | [a1790.md](../ble/a1790.md) | [a1790.md](../mqtt/a1790.md) | product_model.dart @0x22c4078 |
| A1790P | SOLIX F3800 Plus | ZX | yes | [a1790.md](../ble/a1790.md) | [a1790.md](../mqtt/a1790.md) | product_model.dart @0x22c4008 |
| A17A0 | Powered Cooler 30 | legacy F5DA | yes | [a17a0.md](../ble/a17a0.md) | none | product_model.dart @0x22c4940 |
| A17A1 | Powered Cooler 40 | legacy F5DA | yes | [a17a0.md](../ble/a17a0.md) | none | product_model.dart @0x22c48d0 |
| A17A2 | Powered Cooler 50 | legacy F5DA | yes | [a17a0.md](../ble/a17a0.md) | none | product_model.dart @0x22c4860 |
| A17A3 | SOLIX Everfrost 2 26L | ZX | yes | [a17a3.md](../ble/a17a3.md) | none | product_model.dart @0x22c47f0 |
| A17A4 | SOLIX Everfrost 2 40L | ZX | yes | [a17a3.md](../ble/a17a3.md) | none | product_model.dart @0x22c4778 |
| A17A5 | SOLIX Everfrost 2 58L | ZX | yes | [a17a3.md](../ble/a17a3.md) | none | product_model.dart @0x22c4708 |
| A17B1 | SOLIX Home Power Panel | ZX | yes | [a17b1.md](../ble/a17b1.md) | [a17b1.md](../mqtt/a17b1.md) | product_model.dart @0x22c40e8 |
| A17C0 | Solarbank E1600 | ZX | yes | [a17c0.md](../ble/a17c0.md) | [a17c0.md](../mqtt/a17c0.md) | product_model.dart @0x22c4388 |
| A17C1 | Solarbank 2 E1600 Pro | ZX | yes | [a17c1.md](../ble/a17c1.md) | [a17c1.md](../mqtt/a17c1.md) | product_model.dart @0x22c3b38 |
| A17C2 | Solarbank 2 E1600 AC | ZX | yes | [a17c2.md](../ble/a17c2.md) | [a17c2.md](../mqtt/a17c2.md) | product_model.dart @0x22c3908 |
| A17C3 | Solarbank 2 E1600 Plus | ZX | yes | [a17c3.md](../ble/a17c3.md) | none | product_model.dart @0x22c3978 |
| A17C5 | Solarbank 3 E2700 Pro | ZX | yes | [a17c5.md](../ble/a17c5.md) | [a17c5.md](../mqtt/a17c5.md) | product_model.dart @0x22c3898 |
| A17E1 | Anker SOLIX E10 | ZX | yes | [a17e2.md](../ble/a17e2.md) | none | product_model.dart @0x22c36e0 |
| A17E2 | Solarbank Prime AC | ZX | yes | [a17e2.md](../ble/a17e2.md) | none | product_model.dart @0x22c3670 |
| A17X7 | Smart Meter | ZX | yes | [a17x7.md](../ble/a17x7.md) | [a17x7.md](../mqtt/a17x7.md) | product_model.dart @0x22c3ac8 |
| A17X7US | Smart Meter | ZX | yes | [a17x7.md](../ble/a17x7.md) | [a17x7.md](../mqtt/a17x7.md) | product_model.dart @0x22c39e8 |
| A17X8 | Smart Plug | ZX | yes | [a17x8.md](../ble/a17x8.md) | [a17x8.md](../mqtt/a17x8.md) | product_model.dart @0x22c3a58 |
| A17Y0 | E1600 0W Output Switch | ZX | yes | [a17y0.md](../ble/a17y0.md) | none | product_model.dart @0x22c3f98 |
| A2345 | 250W Prime Charger | ZX | yes | [a2345.md](../ble/a2345.md) | [a2345.md](../mqtt/a2345.md) | product_model.dart @0x22c3eb8 |
| A25X7 | Anker Wireless Charger | ZX | no | none | none | product_model.dart @0x22c3068 |
| A2687 | 160W Prime Charger | ZX | no | none | none | product_model.dart @0x353f200 |
| A5101 | Power Module | HES module | yes | [a5101.md](../ble/a5101.md) | [a5101.md](../mqtt/a5101.md) | product_model.dart @0x22c42a8 |
| A5102 | Power Module | HES module | no | [a5101.md](../ble/a5101.md) | [a5101.md](../mqtt/a5101.md) | product_model.dart @0x22c31a0 |
| A5103 | Power Module | HES module | no | [a5101.md](../ble/a5101.md) | [a5101.md](../mqtt/a5101.md) | product_model.dart @0x22c3130 |
| A5140 | MI60 Microinverter | name string | no | [a5140.md](../ble/a5140.md) | none | product_model.dart @0x22c3380 |
| A5141 | MI80 Microinverter | name string | no | [a5140.md](../ble/a5140.md) | none | product_model.dart @0x22c3330 |
| A5143 | MI80 Microinverter(BLE) | A5143 (effe) | yes | [a5140.md](../ble/a5140.md) | none | product_model.dart @0x22c4318 |
| A5150 | A5150 Module | placeholder FF09 | no | [a5150.md](../ble/a5150.md) | none | product_model.dart @0x22600d8 |
| A5190 | Ev Charger | ZX | yes | none | none | product_model.dart @0x22c3828 |
| A5191 | Ev Charger | ZX | yes | none | none | product_model.dart @0x22c37b8 |
| A5220 | Battery Module | placeholder FF09 | no | none | none | product_model.dart @0x22c3210 |
| A5341 | Backup Controller | placeholder FF09 | no | none | none | product_model.dart @0x22c3268 |
| A5450 | A5450 Module | placeholder FF09 | no | none | none | product_model.dart @0x22c30d8 |
| A7320 | A7320 | ZX | yes | none | none | product_model.dart @0x22c3750 |
| A91B2 | 240W Charging Station | ZX | yes | [a91b2.md](../ble/a91b2.md) | [a91b2.md](../mqtt/a91b2.md) | product_model.dart @0x22c3f28 |
| AE103 | Solarbank AE103 | ZX | yes | [a17e2.md](../ble/a17e2.md) | none | product_model.dart @0x22c3520 |
| AE111 | Solarbank E7000H Premium | ZX | yes | [a17e2.md](../ble/a17e2.md) | none | product_model.dart @0x22c3600 |
| AE113 | Solarbank AE113 | ZX | yes | [a17e2.md](../ble/a17e2.md) | none | product_model.dart @0x22c3590 |
| AE1R0 | P1 Energy Tracker | ZX | yes | [ae1x0.md](../ble/ae1x0.md) | none | product_model.dart @0x22c33d0 |
| AE1X0 | AE1X0 Meter | ZX | yes | [ae1x0.md](../ble/ae1x0.md) | none | product_model.dart @0x22c3440 |
| AX170 | Power Dock | ZX | yes | none | none | product_model.dart @0x22c34b0 |
| SHEM3 | Shelly3EM | ZX | no | [shelly.md](../ble/shelly.md) | [shelly.md](../mqtt/shelly.md) | product_model.dart @0x22c2f18 |
| SHEMP3 | Shelly3EM Pro | ZX | no | [shelly.md](../ble/shelly.md) | [shelly.md](../mqtt/shelly.md) | product_model.dart @0x22c2ea8 |
| SHPPS | Shelly Plus Plug S | ZX | no | [shelly.md](../ble/shelly.md) | [shelly.md](../mqtt/shelly.md) | product_model.dart @0x22c2e38 |

Reading the table. Products sharing a GATT group and a BLE page share a device class; the class hierarchy is on the `ble/<pn>.md` pages. A5102 and A5103 are on the [../ble/a5101.md](../ble/a5101.md) page because they carry the same profile as A5101 and have no class of their own. Models marked `BLE map` no are not scanned by name: the 15 not in the map besides A2687 and A120J are A5140, A5141, A1763, A5341, A5220, A5102, A5103, A5150, A5450, A25X7, A1782, A1783 and the three Shelly models. The rows A5140 and A5141 carry the product name instead of UUIDs, and A5150, A5220, A5341 and A5450 carry the short string `0000FF09` in service, write and notify, so they have no usable GATT profile in the table.

### Code lists

Tag: asm-traced.

`DeviceConstant` (`base_service/constant/device_constant.dart`) holds the product-code lists the app uses to decide behaviour:

| list | members | evidence |
|---|---|---|
| `iotDevices` (48 entries) | A1771, A1772, A1781, A1790, A1790P, A17C0, A1753, A1754, A1755, A1761, A1762, A17Y0, A17B1, A1722, A1723, A1725, A1726, A1727, A1728, A1729, A91B2, A2345, A1780P, A17C1, A17C2, A17C3, A17C5, A17X7, A17X7US, A17X8, SHEM3, SHEMP3, A17A3, A17A4, A17A5, A1782, A1783, A1785, A1763, AS100, A1765, SHPPS, A2693, A7320, AS220, AS510, AS520, AS521 | `device_constant.dart @0x22660a0`; array allocation raw 96, real 48 elements (`@0x22660ac`); 3.18.0 had 44 (raw 88) |
| E2 series (`isE2Series`, `needsDefaultParameters`, `supportsSellElectricity`) | A17E2, AE103, AE111, AE113 | `device_constant.dart @0x268f6d0`, `@0x3515db0`, `@0x37a0054` |
| skip WiFi configuration (`shouldSkipWifiConfig`) | SHEM3, SHEMP3, SHPPS, ECOIR, AE1R0 | `device_constant.dart @0x3913364` |

The 3.18.0 list had 44 entries; the four added in 3.24.3 are AS220, AS510, AS520 and AS521 (an `as510_home` page exists in the `s1_s2` module: `s1_s2/src/page/home/as510_home/as510_home_page.dart`). Eight codes of `iotDevices` have no `ProductModel`: A1765, A1785, AS100, A2693, AS220, AS510, AS520 and AS521. For the first three the upstream library names them (A1765 SOLIX C1000X Gen 2, A1785 SOLIX C2000X Gen 2, AS100 SOLIX C1000 Gen 2 LE, `api/apitypes.py` lines 1193, 1194 and 1208, upstream-confirmed); A2693 has its own module directory `a2693` in the asm tree. The old root page added "additional codes from message models" (A110A, A110B, A110G, A120J, A1340, A1341, A1770, A1780, A17A0, A17A1, A17A2, A1903, A25X7, A2687, AE100, AS200): the pool has the strings A110A, A110B, A110G, A110W, A110Y, and `AE100` appears as `EvStationType.ae100`; the other additional codes are covered by the ProductModel table or are not found as standalone pool strings.

### New tokens in 3.24.3

Tag: string-only.

The list handed over for classification contained tokens that look like product codes. Classified by the strings and files in which they occur (pool strings of 3.24.3 and 3.18.0, asm file names):

| token | class | evidence | in 3.18.0 |
|---|---|---|---|
| A17C8 | solar-station family, no BLE class | pool strings `A17C8` (`[pp+0xeb068]`), `a17c8ExternalDeviceList`, `[Bootstrap] A17C8 device setting strategy registered`; files `s1_s2/src/page/setting/a17c8_station_strategy.dart`, `a17c8_setting_strategy.dart`, `a17c8_smart_generator_controller.dart`; no `ProductModel` | no |
| A1201 | solar-station family, no BLE class | `[Bootstrap] A1201 device setting strategy registered`; files `s1_s2/src/page/setting/a1201_station_strategy.dart` and siblings; device images under `assets/img/a1201/` (online and offline, with and without battery) | no |
| A17CX | family token of the A17C* solarbanks, not a product code | pool string `A17CX`; file `charging/ui/page/device/a17c1/a17c1home/a17cxhome_state.dart` (shared home state) | yes |
| A17E2 | product: Solarbank (E2 series) | `ProductModel` A17E2 (name `Solarbank Prime AC`), `EvStationType.a17e2`, `DeviceConstant.isE2Series`, module `micro_hes/src/a17e2`; in the BLE map | no |
| A17B6 | accessory of the A1782 family (F3000) | pool strings `A17B6`, `supportA17B6`, `A1782_A17B6`, image `assets/img/a1782/img_a17b6_device_normal.png`; no `ProductModel` | yes |
| A110B, A110Y | small-charger products (Prime power banks) | pool strings `A110B`, `A110Y`; `small_charging_platform/src/pn_configs/a110Y_config.dart`; A110B image under `assets/img/a1903_batteries/`; upstream calls A110B a Prime power bank | A110B yes, A110Y no (A110W is also new) |
| A1115, A1113 | small-charging-platform products | `small_charging_platform/src/pn_configs/a1115_config.dart`, `a1113_config.dart`; `scp_a1113_a1115_device_image` widget; images `a1115_device_image_lottie.json` | no |
| A120D, A121D | small-charging-platform products with screen | pool strings `A120D`, `A121D`; `pn_configs/a121d_config.dart`; screen-saver assets `a120d_crop_cover.png` | no |
| A1504, A1505 | small-charging-platform modules | pool string `A1504`; `small_charging_platform/src/pn_configs/app_modules/a1504_module.dart`; `A1505` appears only in asset names (`assets/img/new_standard/a1505/`, variants for phone, watch and earphone) | no |
| A1289 | a power bank mentioned in a disclaimer text | only in the localized text of key `A2687AA4` (readings of some power banks, `model A1289`); not a code in any list | no |
| A146*, A156*, A166*, A546*, A556*, A5560, A566B | not Anker products | Samsung Galaxy model numbers in the device-name lookup table of `device_info_plus` data (`SM-A146B`, `SM-A156B`, `SM-A166B`, `SM-A546B`, `SM-A556B`, `SM-A566B`, ...); the six `SM-` keys are not pool strings in 3.18.0 | no |

None of the new tokens except A17E2 (and the AE10x, AE111, AE113, AE1R0 and AE1X0 models) has a BLE device class under `charging/ble/device/`; no BLE device directory is new in 3.24.3 ([../ble/protocol.md](../ble/protocol.md#since-3180)).

## Device and connection enums

Tag: asm-traced. These enums are the states of the BLE and WiFi connection code; they are used on [../ble/protocol.md](../ble/protocol.md#connection-routing-and-the-wifi-exclusion-rule) and [../ble/handshake.md](../ble/handshake.md).

### DeviceConnectionStatus

The single connection value of a device (`AnkerDevice.updateStatus`, `base_service/device/anker_device.dart @0x22054c4`). WiFi and BLE are different members of the same field.

| index | wire value | member | site |
|---|---|---|---|
| 0 | none (index only) | `wifiConnected` | as200_home_logic.dart @0x29edab0 |
| 1 | none (index only) | `wifiDisconnected` | ae100_home_logic.dart @0x29c8ca8 |
| 2 | none (index only) | `bleConnected` | ae100_home_logic.dart @0x29c8d04 |
| 3 | none (index only) | `bleBusinessConnected` | ae100_home_logic.dart @0x29c8c4c |
| 4 | none (index only) | `bleDisconnected` | ae100_home_logic.dart @0x29c8d74 |
| 5 | none (index only) | `bleConnecting` | ae100_home_logic.dart @0x29c8d3c |
| 6 | none (index only) | `disconnect` | clock_style_logic.dart @0x35b794c |
| 7 | none (index only) | `appUnable` | ae100_home_logic.dart @0x3503030 |
| 8 | none (index only) | `unknown` | scp_home_widget_controller.dart @0x3baf668 |

The other connection enums (`AkIotDeviceBleConnectState`: the BLE connect state reported by the AK IoT kit, read by `IotDeviceAdapter.isBleAvailable`, `base_service/device/iot_device_adapter.dart @0x36d2a98`; `DeviceConnectionState`: the connector state `ReactiveBleManager` reacts to, `charging/ble/reactive_ble_manager.dart @0x2217888`; `AnkerConnectState`: the state a conferer ends in, see [../ble/handshake.md](../ble/handshake.md#the-three-conferers); `LegacyConnectStatus`: the legacy connect path of `base_service/util/simple_ble_connector.dart`, `_connectLegacyDevice` `@0x4318008`):

| enum | index | wire value | member | site |
|---|---|---|---|---|
| AkIotDeviceBleConnectState | 0 | none | `bleConnected` | ae100_home_logic.dart @0x29c8a1c |
| AkIotDeviceBleConnectState | 1 | none | `connecting` | ae100_home_logic.dart @0x29c89fc |
| AkIotDeviceBleConnectState | 2 | none | `disconnected` | ae100_home_logic.dart @0x29c8a88 |
| AkIotDeviceBleConnectState | 3 | none | `disconnecting` | iot_device_adapter.dart @0x2855bb8 |
| AkIotDeviceBleConnectState | 4 | none | `bleBusinessConnected` | site_settings_service_impl.dart @0x3515d0c |
| AkIotDeviceBleConnectState | 5 | none | `searching` | ae100_home_logic.dart @0x29c8a0c |
| AkIotDeviceBleConnectState | 6 | none | `searchTimeOut` | ae100_home_logic.dart @0x29c8a78 |
| DeviceEnableType | 0 | none | `bleBind` | ble_connect_logic.dart @0x3513284 |
| DeviceEnableType | 1 | none | `bleConnect` | iot_device_adapter.dart @0x2855b64 |
| DeviceEnableType | 2 | none | `wifiConnect` | iot_device_adapter.dart @0x2416bf8 |
| DeviceEnableType | 3 | none | `usbConnect` | usb_device_manager.dart @0x21d23a8 |
| DeviceConnectionState | 1 | none | `connected` | device_serviceImpl.dart @0x481e570 |
| DeviceConnectionState | 2 | none | `disconnecting` | reactive_ble_manager.dart @0x221a280 |
| DeviceConnectionState | 3 | none | `disconnected` | reactive_ble_manager.dart @0x22173e0 |
| AnkerConnectState | 0 | none | `disconnected` | boostrap_impl.dart @0x49e016c |
| AnkerConnectState | 1 | none | `searched` | a1780p_home_logic.dart @0x2874124 |
| AnkerConnectState | 2 | none | `connected` | a1780p_home_logic.dart @0x287416c |
| AnkerConnectState | 3 | none | `connectDone` | device_serviceImpl.dart @0x2e1a994 |
| UserAuthenticationStatus | 0 | none | `wait` | zx_connect_ble_logic.dart @0x41787bc |
| UserAuthenticationStatus | 1 | none | `succeed` | zx_connect_ble_logic.dart @0x4178a5c |
| UserAuthenticationStatus | 2 | none | `fail` | zx_connect_ble_logic.dart @0x4178b24 |
| LegacyConnectStatus | 0 | none | `initial` | legacy_ble_handler_impl.dart @0x49e1850 |
| LegacyConnectStatus | 1 | none | `searching` | legacy_ble_handler_impl.dart @0x49e185c |
| LegacyConnectStatus | 2 | none | `scanFailure` | simple_ble_connector.dart @0x4318470 |
| LegacyConnectStatus | 3 | none | `connecting` | legacy_ble_handler_impl.dart @0x49e187c |
| LegacyConnectStatus | 4 | none | `connectFailure` | simple_ble_connector.dart @0x4318480 |
| LegacyConnectStatus | 5 | none | `connected` | legacy_ble_handler_impl.dart @0x49e18a4 |
| LegacyConnectStatus | 6 | none | `linked` | simple_ble_connector.dart @0x4318424 |
| LegacyConnectStatus | 7 | none | `bound` | legacy_ble_handler_impl.dart @0x49e18c4 |

## BLE and MQTT protocol enums

Tag: asm-traced.

### BleCmdStatus

The status of a BLE response (`BLE_CMD_STATUS_KEY` of the parsed response). Index and wire code are different numbers: the pool object has only the index (`off_8`), and the code is the key of a `Map<int, BleCmdStatus>` constant with 17 entries (`ble_status_code.dart`, `getCmdStatus @0x241ce60`; pool map `[pp+0xe480]`); `unknown` is the fallback for a code that is not in the map and has no wire code. ENUMS audit, doc lines 322 to 341, corrected the old table: the old numbers 14, 15 and 16 were indices, the codes are 9, 10 and 11; and the members after `lowPower` have the codes 33 to 37, 113 and 114, not the indices 7 to 13.

| code | index | member | site |
|---|---|---|---|
| 0 | 0 | `success` | zx_select_wifi_logic.dart @0x28b8434 |
| 5 | 5 | `noMoreData` | zx_select_wifi_logic.dart @0x28b87ac |
| 9 | 14 | `needAuthentication` | secure_ecdh_confer.dart @0x484d334 |
| 10 | 15 | `passwordWrongAuthenticationFailed` | secure_ecdh_confer.dart @0x484d4b0 |
| 11 | 16 | `passwordRetryCountExceededAuthenticationFailed` | secure_ecdh_confer.dart @0x484d52c |
| none (fallback) | 17 | `unknown` | ble_status_code.dart @0x241ce60 |

The remaining members are in the map as keys 1, 2, 3, 4 and 6 (names `fail`, `accountVerifyFailed`, `timestampVerifyFailed`, `parameterVerifyFailed`, `lowPower` by pool order) and the keys 33 to 37, 113 and 114 (see [Known unknowns](#known-unknowns)); only the five members in the table are dumped as pool objects. The indices of the pool objects are `off_8`: `success` 0, `noMoreData` 5, `needAuthentication` 14, `passwordWrongAuthenticationFailed` 15, `passwordRetryCountExceededAuthenticationFailed` 16, `unknown` 17 (`unknown` is loaded at `ble_status_code.dart` `getCmdStatus` `@0x241ce60` as the default).

### MqttCommandType

The `head.cmd` value is not the enum index: `cmdMap` (`charging/communication/transformer/mqtt_command_transformer.dart @0x226f274`) maps each member to a code (normal 17, OTA 6, upload log 5, remote scan WiFi 25, remote switch WiFi 26, unbind 12, get BSSID 28; owner [../mqtt/envelope.md](../mqtt/envelope.md#command-types)). The indices below are `off_8`; index 3 is absent from the pool, as in the old table (ENUMS audit, doc lines 307 to 318).

| index | wire value | member | site |
|---|---|---|---|
| 0 | none (index only) | `normalCommand` | scp_setting_logic.dart @0x3aaec2c |
| 1 | none (index only) | `otaCommand` | iot_anker_controller.dart @0x3b06f70 |
| 2 | none (index only) | `a17y0OtaCommand` | a17C0_device_controller.dart @0x406b7dc |
| 4 | none (index only) | `uploadLogCommand` | mqtt_command_transformer.dart @0x226f2d4 |
| 5 | none (index only) | `remoteScanWifi` | a172x_device_controller.dart @0x3baeca0 |
| 6 | none (index only) | `remoteSwitchWifi` | shelly_device_controller.dart @0x3b71ed0 |
| 7 | none (index only) | `unbindDevice` | scp_setting_logic.dart @0x3aaec70 |
| 8 | none (index only) | `getDeviceBssid` | a17c1_device_controller.dart @0x3731e44 |

`ZXOpcodeType`: the opcode enum of the BLE side has more than 150 members; the handshake members are in [../ble/handshake.md](../ble/handshake.md#opcode-pairs) and the charging products' members in [../ble/protocol.md](../ble/protocol.md#zx-opcode-names), each with the enum index from the pool object (`off_8`) and the wire opcode of the map entry.

## Device-type and product-category enums

Tag: asm-traced. Audit references: `StationDeviceType` ENUMS audit doc lines 9 to 12; `DeviceTypeEnum` 15 to 19 (range-extender context); `ChargingDeviceType` 22 to 28 (the 3.18.0 pool lacked one instance, no value differs); `ReSystemDevicePnType` 31 to 36 (the members are the product codes A7320, A1782, A1790 and A1790P); `ANKDeviceType` 39 to 43 (physical device type of the phone); `ProductCategory` is new on this page; `AddDeviceType` has eight members in 3.24.3 and the 3.18.0 pool has no instance, so it is verified for 3.24.3 only (audit rows 151 to 155; the old table had five); `EvStationType` has its wire value in `off_14` (audit rows 156 to 160; the old table lacked `hes` 3, `a17e2` 19, `ae103` 20 and `ae111` 21).

| enum | index | wire value | member | site |
|---|---|---|---|---|
| StationDeviceType | 0 | none | `solarBank` | device_energy_home_widget.dart @0x30d2bb8 |
| StationDeviceType | 1 | none | `pps` | device_energy_home_widget.dart @0x30d035c |
| DeviceTypeEnum | 0 | 0 | `undefined` | manage_devices_logic.dart @0x37099a0 |
| DeviceTypeEnum | 1 | 1 | `oilMachine` | manage_devices_logic.dart @0x37099ac |
| DeviceTypeEnum | 2 | 2 | `pps` | manage_devices_logic.dart @0x37099b8 |
| ChargingDeviceType | 0 | 0 | `chargingPile` | general_price_setting.dart @0x27d2b24 |
| ChargingDeviceType | 1 | 1 | `largeChargingDevice` | general_price_setting.dart @0x43a7aac |
| ChargingDeviceType | 2 | 2 | `mediumChargingDevice` | general_price_setting.dart @0x29a4d58 |
| ChargingDeviceType | 3 | 3 | `smallChargingDevice` | device_type_helper.dart @0x289b7c0 |
| ChargingDeviceType | 4 | 4 | `platformDevice` | general_price_setting.dart @0x29a4d68 |
| ReSystemDevicePnType | 0 | "A7320" | `generatorA7320` | re_system_local_network_controller.dart @0x43144a4 |
| ReSystemDevicePnType | 1 | "A1782" | `ppsA1782` | a7320_home_page.dart @0x39e0950 |
| ReSystemDevicePnType | 2 | "A1790" | `ppsA1790` | a7320_home_page.dart @0x39e1328 |
| ReSystemDevicePnType | 3 | "A1790P" | `ppsA1790p` | a7320_home_page.dart @0x39e1318 |
| ANKDeviceType | 0 | none | `phone` | ank_device_detector.dart @0x4406388 |
| ANKDeviceType | 1 | none | `tablet` | ank_device_detector.dart @0x4406374 |
| ANKDeviceType | 2 | none | `foldable` | ank_device_detector.dart @0x4406338 |
| ProductCategory | 0 | none | `pps` | anker_ota_base_logic.dart @0x3b1477c |
| ProductCategory | 1 | none | `hes` | none_model.dart @0x37438a8 |
| ProductCategory | 2 | none | `solarBank` | scan_logic.dart @0x47ca95c |
| ProductCategory | 3 | none | `smallCharge` | a1340_anker_device.dart @0x3743884 |
| ProductCategory | 4 | none | `cooler` | a17a0_anker_device.dart @0x3743890 |
| ProductCategory | 5 | none | `accessory` | a17y0_anker_device.dart @0x374386c |
| AddDeviceType | 0 | none | `homeBackupSystem` | device_wifi_info_controller.dart @0x29ebda0 |
| AddDeviceType | 1 | none | `energyStorage` | device_wifi_info_controller.dart @0x29ebd60 |
| AddDeviceType | 2 | none | `smartMeter` | device_wifi_info_controller.dart @0x29ebe2c |
| AddDeviceType | 3 | none | `generator` | device_wifi_info_controller.dart @0x29ebe54 |
| AddDeviceType | 4 | none | `pps` | device_wifi_info_controller.dart @0x29ebe7c |
| AddDeviceType | 5 | none | `evCharger` | device_wifi_info_controller.dart @0x29ebea4 |
| AddDeviceType | 6 | none | `smartPlug` | device_wifi_info_controller.dart @0x29ebecc |
| AddDeviceType | 7 | none | `ats` | device_wifi_info_controller.dart @0x29ebe04 |
| EvStationType | 0 | 3 | `hes` | load_balancing_logic.dart @0x395e524 |
| EvStationType | 1 | 5 | `a17c1` | load_balancing_logic.dart @0x395e538 |
| EvStationType | 2 | 10 | `a17c3` | load_balancing_logic.dart @0x395e54c |
| EvStationType | 3 | 11 | `a17c2` | load_balancing_logic.dart @0x395e560 |
| EvStationType | 4 | 12 | `a17c5` | load_balancing_logic.dart @0x395e56c |
| EvStationType | 5 | 18 (0x12) | `ae100` | load_balancing_logic.dart @0x395e590 |
| EvStationType | 6 | 19 (0x13) | `a17e2` | load_balancing_logic.dart @0x395e59c |
| EvStationType | 7 | 20 (0x14) | `ae103` | load_balancing_logic.dart @0x395e5b0 |
| EvStationType | 8 | 21 (0x15) | `ae111` | load_balancing_logic.dart @0x395e5d8 |

`FirmwareCountry` (new on this page): `us` 0, `jp` 1, `eu` 2, `uk` 3, `au` 4, `ar` 5, `sa` 6, `ca` 7, `cn` 8, `tw` 9, `za` 10 and `gs` 11, as indices of pool objects (for example `FirmwareCountry.jp` `[pp+0xb338]`, used `anker_device.dart @0x22f61b8`). The old root page listed supported countries as strings (see [String lists](#string-lists)); this enum is the firmware-country classification, not the same list.

### power_site_type (upstream SolixSiteType)

The app reads `power_site_type` from the site scene info (`SceneInfo` field_53, key `power_site_type`) and declares no enum for it. The names come from upstream `SolixSiteType` in `api/apitypes.py` lines 1219 to 1246 (`t_<value>`, upstream-confirmed; names verbatim). The two values the app compares in the output-limit gate are asm-traced.

| value | upstream name | main device (upstream comment) | tag | app compare (width) |
|---|---|---|---|---|
| 2 | `t_2` | A17C0 SB1 | upstream-confirmed | not compared in the gate |
| 5 | `t_5` | A17C1 SB2 Pro | upstream-confirmed | not compared in the gate |
| 10 | `t_10` | A17C3 SB2 Plus | upstream-confirmed | not compared in the gate |
| 11 | `t_11` | A17C2 SB2 AC | upstream-confirmed | not compared in the gate |
| 12 | `t_12` | A17C5 SB3 Pro, including the power dock option | asm-traced (compare), upstream-confirmed (name) | `cmp w1, #0x18`, 32-bit Smi, so 12: `station_home_settings_logic.dart @0x28b2e28` |
| 18 | `t_18` | AE100 Power Dock for SB2+ (A17C1, A17C3, A17C5, ...) | asm-traced (compare), upstream-confirmed (name) | `cmp w1, #0x24`, 32-bit Smi, so 18: `station_home_settings_logic.dart @0x28b2aa0` |

Use of the two compared values: [get_power_limit, Who gets the output-limit page](../api/power_service/site/get_power_limit.md#who-gets-the-output-limit-page-app-gate). The values 12 and 18 equal the `EvStationType` members `a17c5` and `ae100` above (a separate enum of the load-balancing code; the gate does not read it).

## Energy, mode and price enums

Tag: asm-traced.

Notes per enum (the table below lists the pool members):

- `PvType`: ENUMS audit, doc lines 48 to 52.
- `EmsModeType`: the API value is `off_14`; the index (`off_8`) is not stable across versions (3.24.3 added `normalMode`, `customMode`, `timeSlot` and `smartMode`, so the old indices 0 to 5 moved; ENUMS audit, doc lines 209 to 216, audit rows 103 to 108). Two members share the value 8 in the pool, `timeSlot` and `onlyBackupPower`; which one the app sends for which screen is not decided by the enum.
- `AiModeEnum`: ENUMS audit, doc lines 218 to 229; `TOUDynamicPrice` (index 6) has the wire value 8 and `ModeTypeAIEMS` (index 7) the wire value 7; the old table was right.
- `EnergyFlowType`: the wire value is a single-bit mask; the enum is an 18-bit field in 3.24.3 (`batteryToLoadPort` 0x10000 and `batteryToGrid` 0x20000 are new). The flags are tested on unboxed integers (`and x4,x2,x1` in `base_service/view/energy_flow/energy_flow_type.dart @0x22f3214`), so the masks are real values. Only the instantiated entries are in the pool; `dcToHome` 0x80, `dcToGrid` 0x100, `acToHome` 0x400 and `acToGrid` 0x800 follow the pattern mask = 1 shifted by the index but have no pool object (see [Known unknowns](#known-unknowns)). ENUMS audit, doc lines 231 to 252.
- `ChargeDischargeStatus` (PPS work status): ENUMS audit, doc lines 297 to 305; five members with wire values 0 to 4, and the pool name of 0 is `standby`, not `idle`. A second enum with the same name has the members `charging`, `discharging` and `idle` (no wire value) in `station_home/src/ui/shared/node_dialog/default_battery_dialog.dart`; it is left out of the table.
- `RangeExtenderStrategyType`: ENUMS audit, doc lines 343 to 348; the wire values are 1 for `bySoc` and 2 for `byTime` (`off_14`) and the indices are 0 and 1.
- `PlatformPricePlan`: ENUMS audit, doc lines 105 to 109. The old table listed the indices; the wire values (`off_14`) are what the app sends: fixed 0, manualTou 5, autoTou 52 (0x34) and dynamic 6. Do not send the index.
- `ElectricityIntervalEnum`: indices 0 to 3 and no wire value. The wire values 1 to 4 (`peak` 1, `normal` 2, `valley` 3, `super_valley` 4) come from a constant `Map<String, int>` with 4 entries (`[pp+0xeb970]` and `[pp+0xfbd88]`), not from the enum (ENUMS audit, doc lines 98 to 103).
- `PreparednessModeType` (backup mode, ENUMS audit doc lines 162 to 166): the objects are `none`, `manual` and `auto` as indices. The value the app writes in the `backupMode` field is built from a compare in `setBackup` (`ak_soft_pps_ems/src/disaster_preparedness/command/disaster_preparedness_command.dart @0x3574770`: `cmp w4,w16; cset x3,eq; lsl x3,x3,#1`): 1 when the mode equals `auto` and 0 otherwise, so auto is 1 and manual is 0, the opposite of the old table. `clearBackup` (`@0x2603c00`, same file) writes the raw 4 into a map-literal slot, real 2.

| enum | index | wire value | member | site |
|---|---|---|---|---|
| PvType | 0 | none | `bodyPv` | system_a17e1_flow_chart_logic.dart @0x235ef28 |
| PvType | 1 | none | `thirdPv` | system_a17e1_flow_chart_logic.dart @0x235e728 |
| PvType | 2 | none | `total` | system_a17e1_flow_chart_logic.dart @0x235e840 |
| EmsModeType | 0 | 12 | `normalMode` | power_usage_scenario_controller.dart @0x37aec0c |
| EmsModeType | 1 | 1 | `selfConsumption` | power_usage_scenario_controller.dart @0x37a95a4 |
| EmsModeType | 2 | 3 | `customMode` | power_usage_scenario_controller.dart @0x2a2eddc |
| EmsModeType | 3 | 4 | `manualPowerBackup` | power_usage_scenario_controller.dart @0x22ada9c |
| EmsModeType | 4 | 5 | `timeOfUse` | power_usage_scenario_controller.dart @0x37a95d8 |
| EmsModeType | 5 | 8 | `timeSlot` | power_usage_scenario_controller.dart @0x2550d30 |
| EmsModeType | 6 | 7 | `smartMode` | power_usage_scenario_controller.dart @0x2a27a78 |
| EmsModeType | 7 | 8 | `onlyBackupPower` | power_usage_scenario_controller.dart @0x37a9640 |
| EmsModeType | 8 | 9 | `severeWeatherMode` | power_usage_scenario_controller.dart @0x22ad898 |
| EmsModeType | 9 | 10 | `offGrid` | power_usage_scenario_page.dart @0x37a6e50 |
| AiModeEnum | 0 | 0 | `Default` | ai_mode_enum.dart @0x28f5764 |
| AiModeEnum | 1 | 1 | `SelfUse` | ai_mode_enum.dart @0x28f577c |
| AiModeEnum | 2 | 2 | `ModeTypeAdd` | ai_mode_enum.dart @0x28f5794 |
| AiModeEnum | 3 | 3 | `ModeTypeCustom` | ai_mode_enum.dart @0x28f57ac |
| AiModeEnum | 4 | 4 | `ModeTypeManualBackup` | ai_mode_enum.dart @0x28f57c4 |
| AiModeEnum | 5 | 5 | `ModeTypeUseTime` | ai_mode_enum.dart @0x28f57dc |
| AiModeEnum | 6 | 8 | `TOUDynamicPrice` | ai_mode_enum.dart @0x28f57f4 |
| AiModeEnum | 7 | 7 | `ModeTypeAIEMS` | ai_mode_enum.dart @0x28f580c |
| EnergyFlowType | 0 | 1 | `pvToBattery` | device_data_mapper.dart @0x22f2834 |
| EnergyFlowType | 1 | 2 | `pvToHome` | unity_energy_flow_service.dart @0x22ed3fc |
| EnergyFlowType | 2 | 4 | `pvToGrid` | unity_energy_flow_service.dart @0x22ed40c |
| EnergyFlowType | 3 | 8 | `thirdPvToBattery` | device_line_data.dart @0x22f2d74 |
| EnergyFlowType | 4 | 16 (0x10) | `thirdPvToHome` | device_data_mapper.dart @0x22f27e4 |
| EnergyFlowType | 5 | 32 (0x20) | `thirdPvToGrid` | device_data_mapper.dart @0x22f27f8 |
| EnergyFlowType | 6 | 64 (0x40) | `dcToBattery` | device_line_data.dart @0x22f2d58 |
| EnergyFlowType | 9 | 512 (0x200) | `acToBattery` | device_line_data.dart @0x22f2d44 |
| EnergyFlowType | 12 | 4096 (0x1000) | `gridToBattery` | device_line_data.dart @0x22f2d30 |
| EnergyFlowType | 13 | 8192 (0x2000) | `gridToHome` | system_a17e2_flow_chart_logic.dart @0x22f3770 |
| EnergyFlowType | 14 | 16384 (0x4000) | `batteryToHome` | device_line_data.dart @0x22f2d1c |
| EnergyFlowType | 15 | 32768 (0x8000) | `batteryToDC` | device_line_data.dart @0x22f2d08 |
| EnergyFlowType | 16 | 65536 (0x10000) | `batteryToLoadPort` | device_line_data.dart @0x22f2cf4 |
| EnergyFlowType | 17 | 131072 (0x20000) | `batteryToGrid` | device_line_data.dart @0x22f2ce0 |
| ChargeDischargeStatus | 0 | 0 | `standby` | s1_s2_home_state.dart @0x35528a0 |
| ChargeDischargeStatus | 1 | 1 | `discharge` | s1_s2_home_state.dart @0x3a44190 |
| ChargeDischargeStatus | 2 | 2 | `charge` | s1_s2_home_state.dart @0x2a0efc0 |
| ChargeDischargeStatus | 3 | 3 | `sleep` | as510_home_page.dart @0x3a38120 |
| ChargeDischargeStatus | 4 | 4 | `shutdown` | as510_home_page.dart @0x3a3813c |
| RangeExtenderStrategyType | 0 | 1 | `bySoc` | range_extender_strategy_logic.dart @0x3600a54 |
| RangeExtenderStrategyType | 1 | 2 | `byTime` | range_extender_strategy_logic.dart @0x39d9ae8 |
| PlatformPricePlan | 1 | 0 | `fixed` | base_tou_result_controller.dart @0x39405a4 |
| PlatformPricePlan | 2 | 5 | `manualTou` | electricity_price_mode_type.dart @0x47c650c |
| PlatformPricePlan | 3 | 52 (0x34) | `autoTou` | electricity_price_mode_type.dart @0x47bf7f0 |
| PlatformPricePlan | 4 | 6 | `dynamic` | electricity_price_mode_type.dart @0x2a2f988 |
| ElectricityIntervalEnum | 0 | none | `peak` | electricity_price_pad_setting_logic.dart @0x29c4a08 |
| ElectricityIntervalEnum | 1 | none | `midPeak` | electricity_price_pad_setting_logic.dart @0x29c4b08 |
| ElectricityIntervalEnum | 2 | none | `offPeak` | electricity_price_pad_preview_logic.dart @0x29bdb0c |
| ElectricityIntervalEnum | 3 | none | `superOffPeak` | electricity_price_pad_setting_logic.dart @0x29c4cec |
| PreparednessModeType | 0 | 0 | `none` | pps_current_disaster_card.dart @0x420b44c |
| PreparednessModeType | 1 | 1 | `manual` | acrp_controller.dart @0x2d18f40 |
| PreparednessModeType | 2 | 2 | `auto` | acrp_controller.dart @0x2d18f6c |

### ModeState

Three different enums are called `ModeState` in the pool (ENUMS audit, doc lines 256 to 283). All members are indices; there is no wire value.

SolarBank (8 members): 0 `forcedRechargeState` (`[pp+0x2d950]`), 1 `sohCalibrationState` (`[pp+0x2d958]`), 2 `socCalibrationState` (`[pp+0x2d978]`), 3 `autoDisasterState` (`[pp+0x2d960]`), 4 `manualDisasterState` (`[pp+0x2d970]`), 5 `fastStopState` (`[pp+0x2d948]`), 6 `lowPowerState` (`[pp+0x2d890]`), 7 `defaultState` (`[pp+0x2d980]`). Tag: string-only (pool objects listed; the audit rows verify the member positions and give no use site).

Home Power System (11 members): 0 `naStatus` (`[pp+0x23e68]`), 1 `selfUserState` (`[pp+0x23e70]`), 2 `timeOfUserState` (`[pp+0x23e78]`), 3 `manualBackupState` (`[pp+0x23e80]`), 4 `automaticBackupState` (`[pp+0x23e88]`), 5 `onlyBackupPower` (`[pp+0x23e90]`), 6 `manualGridOutage` (`[pp+0x23e98]`), 7 `socCalibration` (`[pp+0x23ea0]`), 8 `physicalOffGrid` (`[pp+0x23ea8]`), 9 `lowSolarInput` (`[pp+0x23eb0]`), 10 `forcedRecharge` (`[pp+0x23eb8]`). Tag: string-only (pool objects listed; the audit rows verify the member positions and give no use site).

The 17-member enum has `selfUserState` 0, `timeOfUserState` 1, `manualBackupState` 2, `automaticBackupState` 3, `onlyBackupPower` 4, `socCalibration` 5, `gridOutage` 6, `naStatus` 7, `defaultState` 8, `offGridState` 9, `customState` 10, `smartPlugState` 11, `aiModeState` 12, `timeSlot` 13, `thirdPartyControlState` 14, `activateDeviceWhenWeakSunshine` 15 and `vppState` 16 (pool objects from `[pp+0x1cc40]` to `[pp+0x1ccf0]`). The old root page's "HES state machine values 0 to 9 and 20" has no source in the asm (BUSINESS_RULES audit, doc lines 541 to 559): the 11-member enum has `forcedRecharge` at index 10 and different names at 4, 6 and 8. Tag: string-only.

### Solarbank usage mode (upstream)

The app has no enum with these values; the numbers come from the upstream `SolarbankUsageMode` (`api/apitypes.py` line 1089, upstream-confirmed): `unknown` 0, `smartmeter` 1, `smartplugs` 2, `manual` 3, `backup` 4, `use_time` 5, `smart` 7 and `time_slot` 8 (6 is a TODO comment upstream). ENUMS audit, doc lines 123 to 133: identical to the old table. The values 1 to 5, 7 and 8 equal the `AiModeEnum` wire values above.

## Device-specific enums

Tag: asm-traced. Notes: `EvChargerDeviceStatus` audit rows 109 to 117; `EvChargerGestureFunction` has four members 0 to 3 (audit rows 127 to 131; the old `startImmediately` 4 has no pool object and upstream also has only 0 to 3); `ScreenBrightType` audit rows 139 to 142; `RESystemBatterySubPackageConnectionStatusEnum` is the sub-battery connection status of the range-extender system, its numbers are enum indices (no wire value) and index 0 `standby` is missing from the old table (audit rows 145 to 150); `RESystemTemperatureUnitEnum` has only `celsius` in the pool (ENUMS audit, doc lines 60 to 63); `RESystemDeviceLightEnum` (doc lines 66 to 69); `ReSystemConnectionStatus` (doc lines 74 to 79); `A17EXConnectStatus` also has `Connecting` 0 and `Connected` 1 in the pool, which the old table did not list (doc lines 82 to 84); `ApplianceType` (doc lines 89 to 93).

| enum | index | wire value | member | site |
|---|---|---|---|---|
| EvChargerDeviceStatus | 0 | 0 | `available` | a5190_home_logic.dart @0x3395c00 |
| EvChargerDeviceStatus | 1 | 1 | `preparing` | a5190_home_page.dart @0x43b25f8 |
| EvChargerDeviceStatus | 2 | 2 | `charging` | a5190_home_page.dart @0x43b5818 |
| EvChargerDeviceStatus | 3 | 3 | `suspendedEVSE` | a5190_home_page.dart @0x43b5904 |
| EvChargerDeviceStatus | 4 | 4 | `suspendedEV` | a5190_home_page.dart @0x43b594c |
| EvChargerDeviceStatus | 5 | 5 | `finishing` | a5190_home_logic.dart @0x3395cc4 |
| EvChargerDeviceStatus | 6 | 6 | `reserved` | a5190_home_logic.dart @0x3395a58 |
| EvChargerDeviceStatus | 7 | 7 | `unavailable` | ev_charger_device_status.dart @0x350a0ac |
| EvChargerDeviceStatus | 8 | 8 | `faulted` | ev_charger_light_explanation_logic.dart @0x2ab2ba0 |
| EvChargerGestureFunction | 0 | 0 | `disable` | gesture_menu_controller.dart @0x464f9bc |
| EvChargerGestureFunction | 1 | 1 | `startCharging` | gesture_util.dart @0x43c31ac |
| EvChargerGestureFunction | 2 | 2 | `stopCharging` | gesture_util.dart @0x43c31b8 |
| EvChargerGestureFunction | 3 | 3 | `startBoostMode` | gesture_util.dart @0x43c31c4 |
| ScreenBrightType | 0 | 0 | `off` | a7320_widget.dart @0x32c9a70 |
| ScreenBrightType | 1 | 1 | `low` | a7320_widget.dart @0x32c9aac |
| ScreenBrightType | 2 | 2 | `medium` | a7320_widget.dart @0x32c9ae8 |
| ScreenBrightType | 3 | 3 | `high` | a7320_widget.dart @0x32c9b24 |
| RESystemBatterySubPackageConnectionStatusEnum | 0 | none | `standby` | res_device_sheet_helper.dart @0x446f294 |
| RESystemBatterySubPackageConnectionStatusEnum | 1 | none | `normal` | res_device_sheet_helper.dart @0x446f2a8 |
| RESystemBatterySubPackageConnectionStatusEnum | 2 | none | `offline` | res_device_sheet_helper.dart @0x446f2bc |
| RESystemBatterySubPackageConnectionStatusEnum | 3 | none | `highTemp` | res_device_sheet_helper.dart @0x446f2d0 |
| RESystemBatterySubPackageConnectionStatusEnum | 4 | none | `mainPackagePressureDifference` | res_device_sheet_helper.dart @0x446f2e4 |
| RESystemBatterySubPackageConnectionStatusEnum | 5 | none | `subPackagePressureDifference` | res_device_sheet_helper.dart @0x446f2f8 |
| RESystemBatterySubPackageConnectionStatusEnum | 6 | none | `other` | res_device_sheet_helper.dart @0x446f30c |
| RESystemTemperatureUnitEnum | 0 | 0 | `celsius` | re_system_device_status_enum.dart @0x3606e60 |
| RESystemDeviceLightEnum | 0 | none | `on` | re_system_pps_status_ui_helper.dart @0x447fb78 |
| RESystemDeviceLightEnum | 1 | none | `off` | range_extender_model.dart @0x360d47c |
| ReSystemConnectionStatus | 0 | none | `loading` | generator_top_more_bar.dart @0x445a8bc |
| ReSystemConnectionStatus | 1 | none | `notNetworked` | re_system_status_controller.dart @0x229c1f4 |
| ReSystemConnectionStatus | 2 | none | `networkedOffline` | re_system_network_status_cache.dart @0x228e28c |
| ReSystemConnectionStatus | 3 | none | `networkedOnline` | re_system_status_controller.dart @0x229c314 |
| A17EXConnectStatus | 0 | none | `Connecting` | a17ex_home_logic.dart @0x3590178 |
| A17EXConnectStatus | 1 | none | `Connected` | a17ex_home_page.dart @0x39cacb0 |
| A17EXConnectStatus | 2 | none | `DisConnected` | a17ex_home_logic.dart @0x35902d4 |
| ApplianceType | 0 | none | `refrigerator` | range_extender_model.dart @0x360c8e4 |
| ApplianceType | 1 | none | `washingMachine` | range_extender_model.dart @0x360c910 |
| ApplianceType | 2 | none | `kettle` | range_extender_model.dart @0x360c93c |

### StartWayEnum, GeneratorMode and LoadBalancingErrorType

Only one member of each enum is in the pool as an object: `StartWayEnum.unknown` (index 8, wire value -1, `ev_charger/.../start_way_enum.dart @0x39594bc`), `GeneratorMode.eco` (value 3, `oe_a7320/src/oe_a7320/page/range_extender_system/models/generator_mode.dart @0x446e3f4`) and `LoadBalancingErrorType.normal` (value 0, `ev_charger/.../load_balancing_logic.dart @0x36fd7a8`). The other members are in [Known unknowns](#known-unknowns).

## String lists

Tag: string-only.

The old root page also listed sets of names. Each member below was checked as a standalone pool string of 3.24.3; none of these lists is an enum with values, and the usage of the strings was not traced.

- Dynamic price providers: `Nordpool`, `Tibber`, `Flatpeak`, `Octopus Energy` (all four are pool strings).
- Schedule constants: `blend_plan`, `custom_rate_plan`, `manual_backup`, `peak_sessions`, `peak_valley_prices`, `use_time` are pool strings; `ai_ems` is not a standalone pool string in 3.24.3. Day types `weekday`, `weekend`, `everyday` are pool strings.
- Fault info fields: `failureCode`, `failureDesc`, `failureLevel`, `failureActualLevel`, `failureTime`, `failureTimeUnix`, `failureType`, `handlingSuggestion`, `stationId`, `sn`, `subSn`, `pn`, `compositeSystemId`, `allow_delete` (all are pool strings).
- KV config keys (per-device feature flags): `bindConfig`, `is_share`, `needCheckBind`, `needCheckOTA`, `needUserLogin`, `otaConfig`, `otaLimitType`, `otaProgressTimeout`, `requires_bluetooth_pwd`, `supportEthernet`, `support_dual_mode_online` (all are pool strings; the last one, `support_dual_mode_online`, is a KV-config string whose use was not traced — see ble/protocol.md)).
- App module names from the log registration: the old list has 55 names; 53 are pool strings, `dynamic_price` and `fixed_price` are not.
- The A17C5 timer duration labels `30min`, `hr`, `hrs`, `never` (audit row 353) are pool strings; they are display labels of the device timeout, not wire values.

The old sections "Disaster Preparedness Template" and "TOU Season/Period Template" are JSON examples that live inside app strings (ENUMS audit, doc lines 155 to 158 and 350 to 360); they are not enums and stay with their endpoint pages.

## Since 3.18.0

Tag: asm-traced (3.24.3 side).

- `EmsModeType` grew from six to ten members (`normalMode` 12, `customMode` 3, `timeSlot` 8, `smartMode` 7) and its indices moved (ENUMS audit, doc lines 209 to 216).
- `EnergyFlowType` grew from 16 to 18 bits (`batteryToLoadPort`, `batteryToGrid`).
- `EvStationType` gained `a17e2` 19, `ae103` 20 and `ae111` 21; `AddDeviceType` has eight members in 3.24.3 (`evCharger`, `smartPlug`, `ats` are new; the 3.18.0 pool has no instances).
- `ProductModel` gained six models (A17E2, AE103, AE111, AE113, AE1R0, AE1X0) and `DeviceConstant.iotDevices` four codes (AS220, AS510, AS520, AS521); see above.
- `ProductModel` gained two empty string fields, and A5140, A5141, A5150, A5220, A5341, A5450 gained placeholder values in their UUID fields (empty strings in 3.18.0), see [../ble/protocol.md](../ble/protocol.md#since-3180).
- The BLE enums (`DeviceConnectionStatus`, `BleCmdStatus` members in the pool) are unchanged in membership; the ENUMS audit found `BleCmdStatus` in both versions.

## Known unknowns

Tag: untagged by design (no API fact).

- `BleCmdStatus` keys 33 to 37, 113 and 114 exist in the code map; by pool-instance order the names are `scanWifi` 33, `wifiConnectFailedForWrongPwd` 34, `wifiConnectFailedForOtherReason` 35, `wifiActivateFailedForMissIp` 36, `wifiActivateFailedForCommFailed` 37, `crc32VerifyFailed` 113 and `fireWarmVeriryFailed` 114 (name binding inferred from instance order; the old table gave the indices 7 to 13). The names of keys 1 to 4 and 6 are bound the same way.
- `StartWayEnum`: the members `wifi`, `ble`, `touch`, `rfid`, `plug`, `timed`, `autoResume` and `modbus` are indices 0 to 7 (the string switch in `startMethodString` `@0x3959300` matches the old order); their wire values are not in the pool, the old values 1 to 8 are index + 1 by inference.
- `GeneratorMode`: the enum has 7 members (`List<GeneratorMode>(7)` `[pp+0xa9218]`) but the names `silentDc`, `saveDc`, `fastDc`, `exerciseAc` and `exerciseDc` are not found in the pool or the asm; only `eco` is an object (ENUMS audit, doc lines 285 to 295).
- `LoadBalancingErrorType`: the enum has 3 members but only `normal` is an object; `mainDeviceDisconnected` and `mainDeviceAndMeterDisconnected` are not pool strings.
- `EvChargerGestureFunction` `startImmediately` 4 and `RESystemTemperatureUnitEnum` `fahrenheit` 1 have no pool object.
- `EnergyFlowType` masks of `dcToHome`, `dcToGrid`, `acToHome` and `acToGrid` (indices 7, 8, 10 and 11) have no pool object.
- Which `ModeState` enum each screen uses, and the wire values of the mode-state numbers (none are declared).
- The meaning of the 15 products without a BLE class in the ProductModel table beyond their names (A25X7, A2687 and A120J, for example, have a ProductModel and the ZX UUIDs but no `charging/ble/device` class).

BLE is unavailable while the device is on WiFi (community finding, see `ble/protocol.md`; not asm-traced).
