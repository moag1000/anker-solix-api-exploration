> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# A5190DeviceInfo

## Purpose

Carries the state of an EV charger as the app receives it from the device through the IoT kit; this page lists only the Modbus TCP keys of the model (the other keys are not documented yet).

## Dart class + file

`A5190DeviceInfo`, `ev_charger/src/ev_charger/sdk/model/a5190_device_info.dart` (package `ev_charger`), `fromJson` at `a5190_device_info.dart @0x45ac170` (asm-traced).

## Fields

Modbus subset only, in `fromJson` order. Each value is read with `[]` and type-tested as listed. Column `since`: `≤3.18.0` means the key string is also in the 3.18.0 pool (`String:` entries, e.g. `tcpModbusIp` read at 3.18.0 `a5190_device_info.dart @0x34bb50c`; earlier versions not checked). The meaning column is how the app uses the value; the owner of that usage is [../devices/modbus.md](../devices/modbus.md#ev-charger-modbus-tcp-device-properties).

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `supportModbusTcp` | `int?` | yes | ≤3.18.0 | `a5190_device_info.dart @0x45ad9cc`; the Modbus TCP section is shown when it equals 1 (`cmp w1, #2` on the loaded tagged field, so 1, `integrations_setting_logic.dart @0x35f523c`) |
| `modbusTcpSwitch` | `int?` | yes | ≤3.18.0 | `a5190_device_info.dart @0x45adecc`; 1 on, 0 off as written by the app (see [../devices/modbus.md](../devices/modbus.md#ev-charger-modbus-tcp-device-properties)) |
| `tcpModbusTimeout` | `int?` | yes | ≤3.18.0 | `a5190_device_info.dart @0x45adf54`; shown with the suffix `"S"` (string literal, `integrations_setting_page.dart @0x39724a8`) |
| `tcpModbusPhaseLimit` | `int?` | yes | ≤3.18.0 | `a5190_device_info.dart @0x45adfdc`; 0 default phase, 1 fixed single phase, 2 fixed three phase (`cmp w0, #2` and `cmp w0, #4` on the boxed value, `integrations_setting_logic.dart @0x3972894`, `@0x39728b4`, so 1 and 2; other values show the default text, `@0x39728d4`) |
| `tcpModbusMaxCurrent` | `int?` | yes | ≤3.18.0 | `a5190_device_info.dart @0x45ae064`; units of 0.1 A: divided by 10 (`sdiv` by raw 10, arithmetic, unboxed, `integrations_setting_logic.dart @0x3972970`) and shown with `"A"` (`@0x39729a8`) |
| `tcpModbusPort` | `int?` | yes | ≤3.18.0 | `a5190_device_info.dart @0x45ae0ec`; shown as is (`integrations_setting_page.dart @0x397222c`) |
| `tcpModbusIp` | `String?` | yes | ≤3.18.0 | `a5190_device_info.dart @0x45ae174`; empty means "not connected yet", the page then shows `evModbusIpAddressTips` (`integrations_setting_logic.dart @0x3972a40`) |
| `errorCodeArray` | list of int (bytes) | yes | ≤3.18.0 | `a5190_device_info.dart @0x45ae5b0`; bit 32 = Modbus link lost (`integrations_setting_logic.dart @0x35f498c`, rule on [../devices/modbus.md](../devices/modbus.md#ev-charger-modbus-tcp-device-properties)) |

The app defines no default or range of its own for `tcpModbusIp`, `tcpModbusPort`, `tcpModbusTimeout` or `tcpModbusMaxCurrent`: it only displays what the charger reports (asm-traced: the only uses are the display sites above).

## Produced by

No cloud endpoint. The charger's device info arrives through the IoT kit (`akiot.device.notification_events`, event `event_charging_real_time_data`, subscribed in `integrations_setting_logic.dart @0x33b6a80`, `@0x33b6b44`). Upstream maps the corresponding A5191 MQTT fields (`api/mqttmap.py`, upstream-confirmed); the MQTT owner page `mqtt/a5191.md` does not exist yet.

## Consumed by

EV charger "Integrations" page: `IntegrationsSettingLogic` (`integrations_setting_logic.dart`): `refreshSupportProtocolList` (`@0x35f51e8`), `analyzeModbusConnectError` (`@0x35f4740`), `getPhaseValue` (`@0x39727f4`), `getModbusMaxCurrent` (`@0x3972900`), `getModbusIpAddressTips` (`@0x39729dc`), `setModbusTcpStatus` (`@0x3972cfc`); and `integrations_setting_page.dart` (display sites cited in Fields).

## Changed since 3.18.0

No change found for the Modbus keys: all eight key strings are in the 3.18.0 pool and `analyzeModbusConnectError` exists in 3.18.0 `integrations_setting_logic.dart` (string-level comparison; the 3.18.0 casts were not re-read).

## Known unknowns

- All non-Modbus keys of the model (not documented here yet).
- The meaning of the other bits of `errorCodeArray`.
- How the IoT kit maps these JSON keys to MQTT or Bluetooth fields.
