> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced (lowest tag among the API facts; the UI-text table is excluded by design) · Owner page: this page · Page type: feature (not a PN page)

# Modbus (third-party control: Modbus TCP and RTU, Home Assistant, Homey)

This is not a product page. It is the owner page of the Modbus feature across products: which products expose it, where the app configures it, which local transport carries the setting, and what the app does and does not know about the Modbus protocol itself. Endpoint payloads stay on their endpoint pages; the user sequence is on [../flows/modbus_setup.md](../flows/modbus_setup.md). Every API fact on this page is `asm-traced` or `upstream-confirmed` as marked; the UI-text table at the end holds translation strings, which are not API facts and are untagged by design. Product codes and enums are owned by `reference/enums.md` (not written yet).

The app has two separate Modbus features that share nothing but the name:

1. **Third-party control** (new in 3.24.3): a page with a Modbus TCP switch, a Modbus RTU switch, an RTU slave id, and guide cards for Home Assistant and Homey. The app reads it with [query_modbus_setting](../api/charging_hes_third_party_service_svc/query_modbus_setting.md) and sends changes to the cloud with [set_modbus_setting](../api/charging_hes_third_party_service_svc/set_modbus_setting.md) (what the server does with them is not verified), and for RTU also over the path the app names Bluetooth when the device has no Wi-Fi.
2. **EV charger Modbus TCP** (already present in 3.18.0): a switch and a read-only parameter list on the EV charger "Integrations" page, written to the charger as a device property, not through a cloud endpoint.

## Contents

1. [PN, marketing name, generation/family](#pn-marketing-name-generationfamily)
2. [Features matrix](#features-matrix)
   - [Third-party control (cloud)](#third-party-control-cloud)
   - [Bluetooth path (IoT kit action)](#bluetooth-path-iot-kit-action)
   - [EV charger Modbus TCP (device properties)](#ev-charger-modbus-tcp-device-properties)
   - [Support flags](#support-flags)
   - [Home Assistant and Homey entry points](#home-assistant-and-homey-entry-points)
   - [Preconditions and the risk dialog](#preconditions-and-the-risk-dialog)
   - [Register map](#register-map)
   - [Not part of this feature: ECU AP-mode protocol](#not-part-of-this-feature-ecu-ap-mode-protocol)
   - [UI texts](#ui-texts)
3. [Known firmware notes](#known-firmware-notes)
4. [Known unknowns](#known-unknowns)
5. [Device-tested by](#device-tested-by)

## PN, marketing name, generation/family

Tag: asm-traced (marketing names upstream-confirmed where marked).

Products for which the 3.24.3 app builds a Modbus entry point. Product codes are owned by `reference/enums.md` (not written yet). Whether the entry is actually shown is decided at runtime by the support flags (see [Support flags](#support-flags)).

| product | marketing name | entry point in the app | source |
|---|---|---|---|
| `A17E2` | Solarbank Max AC (upstream-confirmed, `SolixDeviceCategory` comment in `api/apitypes.py`) | device settings, menu "Third-Party Control Settings" | `setting_config.dart @0x361abc0` (PN string literal), menu name `"communicationSetting"` at `@0x361ad0c` |
| `AE103` | Solarbank 4 E5000 Pro (upstream-confirmed, `api/apitypes.py`) | same menu | `setting_config.dart @0x361abd4`, `@0x361ad0c` |
| `AE111`, `AE113` | not known here | same menu | `setting_config.dart @0x361abec`, `@0x361ac04`, `@0x361ad0c` |
| AE1x0 family (third-device module) | not known here | AE1x0 settings page, same menu controller | `ae1x0_setting_page.dart @0x3af140c` |
| stations (site settings) | n/a | station settings, same menu, for four values of the int argument of `StationSettingConfig.getMenuFunctions`: 19, 20, 21, 25 | `station_config.dart @0x3a6f798`; compares `cmp x0, #0x13` / `#0x14` / `#0x15` / `#0x19` on the unboxed argument (`@0x3a6f80c` to `@0x3a6f838`, so 19, 20, 21, 25) and `cmp w2, #0x26` / `#0x32` on its boxed copy (`@0x3a6f820`, `@0x3a6f840`, so 19 and 25); menu entry `CommonConfigType.communicationSetting` at `@0x3a6fcf0` |
| any device with advanced settings | n/a | advanced settings, same menu, when the config list contains `CommonConfigType.communicationSetting` (enum index 34: pool `int(0x22)`, compared as `cmp w0, #0x44` on the boxed index, `device_advance_settings_controller.dart @0x35b32e0`, so 34) | `device_advance_settings_controller.dart @0x35b32f4` |
| `A17X8` | Smart Plug (upstream-confirmed, `api/apitypes.py`) | smart plug settings, entry `tapEnterHA` | `a17x8setting_logic.dart @0x3dde9b0`, product code literal `"A17X8"` at `@0x3ddeb50` |
| EV charger (`ev_charger` module, model `A5190DeviceInfo`) | EV charger; upstream maps the Modbus fields under `A5191` (upstream-confirmed, `api/mqttmap.py`) | EV charger settings, "Integrations" page, Modbus TCP section | `integrations_setting_logic.dart @0x35f51e8` |
| `A5101` (X1 HES) | X1 | none: its Bluetooth support list names `isSupportModbus`, but the value is only logged, not stored (see [Support flags](#support-flags)) | `a5101_device_controller.dart @0x34cdab0` |

All third-party control menus use one controller, `CommunicationSettingMenuController` (title key `threePartyControlSettings`, `communication_setting_menu_controller.dart @0x4154870`). The first two rows are the device-settings list returned by `SettingConfig.getSettingsConfig` for exactly these four PN strings; for any other PN it returns an empty list (`setting_config.dart @0x361af20`). Whether the int argument of the station rule is the site type is not verified; upstream lists site type 19 as "Main A17E2 Solarbank Max AC" (`SolixSiteType.t_19` in `api/apitypes.py`).

No asm site ties Modbus to `A17C5` (Solarbank 3); [a17c5.md](a17c5.md) is therefore unchanged.

## Features matrix

Tag: per cell; app-side cells asm-traced, MQTT cells upstream-confirmed.

| feature | API (link) | MQTT (link) | BLE (link) | device-tested? |
|---|---|---|---|---|
| third-party control: read support flags, state, IP, port, RTU id, guide URLs | [query_modbus_setting](../api/charging_hes_third_party_service_svc/query_modbus_setting.md) | unknown | none (read only through the cloud) | no |
| third-party control: switch Modbus TCP / RTU, set RTU id | [set_modbus_setting](../api/charging_hes_third_party_service_svc/set_modbus_setting.md) | unknown (whether the cloud forwards it is not traced) | IoT kit action `action_ha_communication_setting`, RTU only, see [Bluetooth path](#bluetooth-path-iot-kit-action) | no |
| EV charger Modbus TCP switch | none | upstream: command group `0100`, field `b7` `modbus_switch` for `A5191` (`mqtt/a5191.md`, not yet written; upstream-confirmed, `api/mqttmap.py`) | IoT kit property write `prop_write_evcharger`, see [EV charger Modbus TCP](#ev-charger-modbus-tcp-device-properties) | no |
| EV charger Modbus TCP parameters (IP, port, current limit, phase, timeout, link error) | none | upstream: `0405` fields `d0` `ip_address`, `cf` `tcp_port`, `cc` `tcp_timeout_seconds` for `A5191` (upstream-confirmed, `api/mqttmap.py`) | read from the charger's device info, see [EV charger Modbus TCP](#ev-charger-modbus-tcp-device-properties) | no |

### Third-party control (cloud)

Tag: asm-traced.

The page is `HomeAssistantPage` (route `/homeAssistantPage`, pool `pp+0x4f698`) with `HomeAssistantLogic` (`home_assistant_logic.dart`). Its state comes entirely from the [query_modbus_setting](../api/charging_hes_third_party_service_svc/query_modbus_setting.md#response) response, which the caller passes in as route argument `data` (`home_assistant_logic.dart @0x35ead84`). Changes go to [set_modbus_setting](../api/charging_hes_third_party_service_svc/set_modbus_setting.md#request). The page shows (asm-traced):

- a Modbus TCP card with a switch, the device IP (copyable, `home_assistant_page.dart @0x38da7d8`) and the port, visible when `tcpSupport` is `true` (`home_assistant_page.dart @0x38d9648`);
- a Modbus RTU card with a switch, the RTU id (editable, `showEditDialog`, `home_assistant_page.dart @0x38da834`) and the baud rate, visible when `rtuSupport` is `true` (`@0x38d9664`);
- an explanation dialog (`functionalDescription`, `home_assistant_logic.dart @0x38dcdc8`) and two guide cards (see [Home Assistant and Homey entry points](#home-assistant-and-homey-entry-points)).

Only one variant can be on: enabling TCP switches RTU off in the page and vice versa (`home_assistant_page.dart @0x38dca30` to `@0x38dcaa0`), and the app encodes the pair as one `modbusStatus` value (owner: [set_modbus_setting](../api/charging_hes_third_party_service_svc/set_modbus_setting.md#request)). The whole user sequence is on [../flows/modbus_setup.md](../flows/modbus_setup.md).

### Bluetooth path (IoT kit action)

Tag: asm-traced (the transport inside the IoT kit is not traced; the app names this path Bluetooth).

When the device's Wi-Fi is offline but the app has a local connection to it, the RTU setting (switch and RTU id) is written to the device first and then reported to the cloud with `isBluetooth: true`. Modbus TCP never takes this path: `checkConnectionEnvironment` requires device Wi-Fi for TCP and forces `isBluetooth` to `false` (`home_assistant_logic.dart @0x38dbf88` to `@0x38dbfb4`). This is a local configuration path for a device without Wi-Fi, not a cloud fallback: the cloud request still follows it.

`HomeAssistantLogic::bluetoothSend` (`home_assistant_logic.dart @0x38dbd50`, log prefix `HaBluetoothResponeseData: `) does not build a BLE frame itself. It calls the IoT kit (`AKIoTKitManagerImpl::handle`, `@0x38dbf18`) with the method string `"akiot.device.invoke_action"` (`@0x38dbf08`) and this argument map (asm-traced; outer map 3 pairs, raw `r2 = 12` at `@0x38dbd90`; `param` map 2 pairs, raw `r2 = 8` at `@0x38dbde4`):

Interim owner — moves to `ble/a5190.md` / `mqtt/a5191.md` when those pages exist (Task 3.7).

| key | value | source |
|---|---|---|
| `id` | string literal `"action_ha_communication_setting"` | `home_assistant_logic.dart @0x38dbdac` |
| `deviceSn` | device serial number (route argument `deviceSn`) | `home_assistant_logic.dart @0x38dbdb8` |
| `param.deviceID` | RTU id, `int.parse` of the RTU id text field | `home_assistant_logic.dart @0x38dbdf0`, parse at `@0x38dbe1c` |
| `param.communicationProtocolConfig` | the same value as `modbusStatus` (`modbusState()`, `home_assistant_logic.dart @0x38dbe74`; values on [set_modbus_setting](../api/charging_hes_third_party_service_svc/set_modbus_setting.md#request)) | `@0x38dbe64` |

The result is compared with `AKResultType.success` (pool `pp+0xa5b0`, `home_assistant_logic.dart @0x38daf04`). How the IoT kit turns this action into Bluetooth bytes (opcode, TLV) is not in the Dart code; no BLE command file in the asm names the action. The BLE owner page for the products concerned does not exist yet (`ble/<pn>.md`, Task 3.7).

### EV charger Modbus TCP (device properties)

Tag: asm-traced (upstream names: upstream-confirmed).

The EV charger "Integrations" page (route `/integrationsSettingPage`, `integrations_setting_menu_controller.dart @0x2cdfb54`; logic `IntegrationsSettingLogic`, `integrations_setting_logic.dart`) reads its Modbus values from the charger's device info (`A5190DeviceInfo.fromJson`, `a5190_device_info.dart @0x45ac170`) and writes the switch as a device property. No cloud endpoint is involved (asm-traced).

The Modbus keys of the charger's device info (`supportModbusTcp`, `modbusTcpSwitch`, `tcpModbusIp`, `tcpModbusPort`, `tcpModbusMaxCurrent`, `tcpModbusPhaseLimit`, `tcpModbusTimeout`, `errorCodeArray`), with types, units and value meanings, are owned by [../models/a5190_device_info.md](../models/a5190_device_info.md#fields). The app defines no default and no range of its own for the IP address, port, timeout or current limit: it only displays what the charger reports (asm-traced, the only uses are the display sites listed on the model page).

Switching: `IntegrationsSettingLogic::setModbusTcpStatus` (`integrations_setting_logic.dart @0x3972cfc`) turns the switch bool into 1 (on) or 0 (off) (`tst x0, #0x10` / `cset`, `@0x3972de8`) and calls `AKIotEVChargeCommand::setModbusTcpSwitch` (`ev_charge_command.dart @0x3972f40`), which writes the property group `"prop_write_evcharger"` (`@0x3972fa0`) with the single key `modbusTcpSwitch` (`@0x3972f74`; value tagged with `lsl` before the store, `@0x3972f84`, so the plain 1 or 0) through `AKIotBasicCommand::writeProperty` (`@0x3972fa8`). On a result other than `AKResultType.success` the page reloads its values and shows the toast key `failed` (`integrations_setting_logic.dart @0x3972ebc`).

Upstream names (upstream-confirmed, `api/mqttmap.py` and `api/mqttcmdmap.py`): for `A5191` the MQTT switch is `modbus_switch` (field `b7`, command group `0100`, `CMD_MODBUS_SWITCH`, off 0, on 1), and the status message `0405` carries `tcp_timeout_seconds` (`cc`), `tcp_port` (`cf`) and `ip_address` (`d0`). That the app keys above are the same values as these upstream names is `string-only` evidence (name match only): the mapping happens inside the IoT kit.

Link error detection (`analyzeModbusConnectError`, `integrations_setting_logic.dart @0x35f4740`, called from `onInit` at `@0x35f4600` and on every device-info update at `@0x35f52f4`): the app walks `errorCodeArray` byte by byte and counts trailing zero bits, adding 8 for each zero byte (`add x1, x3, #8`, arithmetic, `@0x35f48d8`, so 8) until it finds the first non-zero byte. If the lowest set bit is bit number 32 (`cmp x0, #0x20` on the unboxed count, `@0x35f498c`, so 32), it logs `Modbus connect error detected!` and, while the Modbus switch is on, shows the warning `evModbusConnectTips` (`@0x35f49f8`; text in [UI texts](#ui-texts)). Any other error bit, or an all-zero array, clears the warning. That is the only error class the app derives for Modbus.

Two EV charger enums also have a Modbus entry (labels only; their wire values are not traced): `StartWayEnum` index 7 shows the string literal `"Modbus TCP"` as the start/stop method of a charging session (`cmp x0, #7` on the unboxed enum index, `start_way_enum.dart @0x39593e4`, so 7; label at `@0x39593ec`), and `ChargingPauseReason` index 6 shows the pause reason `evChargerPauseModbusTCP` (`cmp x2, #6` / `#5` on the unboxed index, `charging_pause_reason_enum.dart @0x3505fd0`, `@0x3505fd8`, so 6; key at `@0x3505ff8`). The enum values belong to `reference/enums.md` (not written yet).

### Support flags

Tag: asm-traced.

- **Third-party control**: `tcpSupport` and `rtuSupport` in the [query_modbus_setting](../api/charging_hes_third_party_service_svc/query_modbus_setting.md#response) response. The menu is shown only if one of them is `true`. They come from the cloud, not from a device attribute, `get_device_attrs`, the scene info, or a PN list (asm-traced, `communication_setting_menu_controller.dart @0x2cd5270`).
- **EV charger**: `supportModbusTcp` in the charger's device info ([../models/a5190_device_info.md](../models/a5190_device_info.md#fields)), from the device through the IoT kit.
- **`isSupportModbus`**: only in the X1 (`A5101`) Bluetooth controller. `parseSupportFunction2` (`a5101_device_controller.dart @0x34cda1c`) names the entries of a 14-entry support list (name array allocated with raw `r2 = 28` at `@0x34cda7c`, a Smi length, so 14 slots; loop bound `cmp x2, #0xe` on the unboxed index, `@0x34cdb74`, so 14); `isSupportModbus` is entry 3 (fourth array slot, `@0x34cdab0`). An entry counts as supported when it equals 1 (`cmp w0, #2` on the boxed element, `@0x34cdba8`, so 1). Entry 3 falls through the index switch without a store (`@0x34cdbc0` to `@0x34cdc28`), so the flag is logged but not kept, and no X1 Modbus page exists in 3.24.3.

### Home Assistant and Homey entry points

Tag: asm-traced.

`modbustoha` and `modbustohomey` are translation keys, not URLs or deep links (asm-traced: both go through `Trans.tr`, `home_assistant_page.dart @0x38d8b3c` and `@0x38d8c3c`). They are the titles of two guide cards on the third-party control page, below the intro texts `modbusgettingstarted` (`@0x38d8890`) and `modbusquickguide` (`@0x38d8a68`). The links behind the cards come from the cloud: the Home Assistant card opens `helpH5Url` (`@0x38d8b4c`), the Homey card opens `homeyH5Url` (`@0x38d8c4c`), both fields of the [query_modbus_setting](../api/charging_hes_third_party_service_svc/query_modbus_setting.md#response) response. A tap calls `HomeAssistantLogic::openWebView` (`home_assistant_page.dart @0x38d945c`), which does nothing for an empty URL (`home_assistant_logic.dart @0x38d949c`) and otherwise opens the in-app web view route `/tutorialGuidePage` with `title` and `url` (`@0x38d9530`). The app contains no Home Assistant or Homey integration code of its own.

### Preconditions and the risk dialog

Tag: asm-traced.

`HomeAssistantLogic::checkConnectionEnvironment` (`home_assistant_logic.dart @0x38dbf30`) runs before every change (asm-traced):

| request | device Wi-Fi online (`isWifiOnline`) | local connection (`isConnected`) | result |
|---|---|---|---|
| Modbus TCP | yes | any | proceed over the cloud, `isBluetooth` false (`home_assistant_logic.dart @0x38dbfb4`) |
| Modbus TCP | no | any | stop, toast `modbuswifiOfflinetoast` (`home_assistant_logic.dart @0x38dbff4`) |
| Modbus RTU or RTU id | yes | any | proceed over the cloud, `isBluetooth` false (`home_assistant_logic.dart @0x38dc054`) |
| Modbus RTU or RTU id | no | yes | proceed, Bluetooth first, `isBluetooth` true (`home_assistant_logic.dart @0x38dc090`) |
| Modbus RTU or RTU id | no | no | stop, toast `deviceWifiOfflineDialogTitle` (`home_assistant_logic.dart @0x38dc0cc`) |

`isWifiOnline` and `isConnected` are route arguments (`home_assistant_logic.dart @0x35eaac8`, `@0x35eac90`); for the smart plug they are `AnkerDevice::isWifiConnected` and `AnkerDevice::isConnected` (`a17x8setting_logic.dart @0x3ddeac4`, `@0x3ddeb6c`).

Risk dialog (`riskControlToast`, `home_assistant_logic.dart @0x38dc778`): switching a variant on shows the dialog `tips` / `modbusanquantips` with Confirm and Cancel once per page instance. Confirm sets the page flag (`@0x38dc960`) and continues; Cancel drops the change. Switching off, or switching on after a confirmation on the same page, skips the dialog (`@0x38dc7c8`, `@0x38dc7d0`). The flag is not persisted (initialised `false` in the constructor, `@0x36f5338`).

### Register map

Tag: asm-traced (negative result: searched, not found).

The app does not speak Modbus. No Dart file in the 3.24.3 asm contains Modbus register numbers, function codes (`0x03`, `0x06`, `0x10`), holding or input register tables, or a Modbus frame builder; the pool has no such strings. The app only switches the device's Modbus server on or off and shows its address. For the EV charger, the dialog link "View Modbus Register Map" (`evModbusRegisterMapTips`, `integrations_setting_logic.dart @0x3973088`) opens the product's user manual URL (`SpServiceImpl::getUserManualLink` with the product code, route `/commonWebViewPlus`, closure `@0x39731a4`). For third-party control the register documentation, if any, is behind `helpH5Url` / `homeyH5Url`. The register map is therefore a Known unknown of this repository.

### Not part of this feature: ECU AP-mode protocol

Tag: asm-traced.

`charging/tcp/ecu_protocol.dart` (`setECUProtocolWithFunctionCode`, `@0x25f50a8`; `connectWifi`, `@0x3044970`) belongs to the local Wi-Fi provisioning protocol of the micro-inverter gateway (ECU), not to Modbus TCP. Its "function codes" are command codes of that protocol (AP password, close AP, scan Wi-Fi, connect router, network progress), and its replies arrive through `TcpSocketManager`, which hands received data to `ECUProtocol.parseTcpData` (`tcp_socket_manager.dart @0x4199ee0`). `TcpSocketManager::setTcpConfig` (`@0x33c2cb4`) holds the address string `"172.30.1.1"` and port 503 (raw `0x3ee` = 1006 at `@0x33c2cbc`, stored 32-bit with `stur w3` at `@0x33c2cc8`, Smi, so 503); no direct caller of `setTcpConfig` was found. The commands include closing the device's own access point, which is why this is called the AP-mode protocol here. Three log strings mention Modbus only as an inverter property: "get inverter ID list and Modbus address", "set inverter ID and Modbus address" and "whether setting inverter ID and Modbus address succeeded" (`ecu_protocol.dart @0x419b414`, `@0x419b4ec`, `@0x419b5a4`), i.e. the bus address of each micro-inverter behind the ECU. This page does not document that protocol further.

### UI texts

Tag: untagged by design (UI translation strings, not API facts). English texts from the 3.24.3 translation table in `pp.txt`; the keys are asm-traced at the cited sites.

| key | English text |
|---|---|
| `threePartyControlSettings` | Third‑Party Control Settings |
| `modbustoha` | Learn how to connect to Home Assistant via Modbus |
| `modbustohomey` | Learn how to connect to Homey via Modbus |
| `modbusquickguide` | Use the Modbus protocol to connect your device to third‑party platforms for remote monitoring and management. Just follow this quick guide to get set up and start using your device. |
| `modbusanquantips` | Enabling the Modbus service may expose the device to the risk of unauthorized control. This feature is intended for integration with third‑party systems only within a secure internal network. |
| `communicationExplanation1` | This switch is used to enable the local API, allowing external systems to access Anker devices. The available communication protocols depend on the device model and hardware capabilities. If the device supports multiple protocols, only one can be enabled at a time. |
| `communicationExplanation2` | Modbus TCP: Communication method that connects devices over a network, used for data exchange between devices and systems. |
| `communicationExplanation3` | Modbus RTU: Communication method that connects devices via RS‑485 serial communication, used to read and control device operating data. |
| `modbuswifiOfflinetoast` | Please connect to Wi‑Fi to enable this feature. |
| `modbusBluethFaildTips` | Please enable Wi‑Fi or Bluetooth on your phone. |
| `exceedTheLimit` | Invalid input. Please enter a value between 1 and 255. |
| `addedToStationSetting` | Added to system. Please go to the system to modify settings. |
| `evModbusTips` | Modbus TCP enables an energy management system to connect to the charger over the local network. It supports reading charging data, starting or stopping charging, and adjusting the charging current for smart home or EMS integration. |
| `evModbusIpAddressTips` | IP address and port will be shown once the charger is connected to the network. |
| `evModbusConnectTips` | Modbus communication lost. Charging current is limited to 6A. |

## Known firmware notes

Tag: untagged by design (no API fact).

- none recorded

## Known unknowns

- The Modbus register map, function codes and unit id handling of any product. The app does not contain them (see [Register map](#register-map)).
- The fixed TCP port of the third-party control devices; the app only displays `tcpPort` from the cloud.
- How the IoT kit encodes `action_ha_communication_setting` and `prop_write_evcharger` on Bluetooth or MQTT (opcode, TLV or field ids). Upstream has the EV charger MQTT field `b7` (`modbus_switch`); its identity with the app key `modbusTcpSwitch` is not traced.
- Whether `set_modbus_setting` reaches the device through the cloud (for example over MQTT) when the app took the cloud path, or whether the cloud only records the state.
- The meaning of the int argument of the station menu rule (19, 20, 21, 25), and the marketing names of `AE111` and `AE113`.
- Which other bits of the EV charger `errorCodeArray` exist; the app only names bit 32.
- The wire values of the `StartWayEnum` and `ChargingPauseReason` Modbus entries.
- Whether `A17C5` or other Solarbank 3 sites get the station menu (depends on the unverified station rule above).

## Device-tested by

none
