> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# A5190DeviceInfo

## Purpose

Carries the state of an EV charger as the app receives it from the device through the IoT kit; this page lists the Modbus TCP keys with their consumers and, as a second table, all other keys with their Dart types.

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

### Other keys of `fromJson` (new read)

Tag: asm-traced for key and type; no consumer was traced for these keys, so their meaning and units are not stated here (the Modbus rows above have their consumers). Order is the `fromJson` order. The switch keys are read as `value == true` (the key load, then a compare with `true` through the dispatch table, for example `@0x45acf7c` to `@0x45acfb4`), so the model field is a Dart `bool`; the two LED time keys are read once to test for null and once more with a `<int>` cast (`@0x45add1c` to `@0x45add88`).

| JSON key | Dart type | read site |
|---|---|---|
| `deviceSn` | `String?` | `a5190_device_info.dart @0x45ac230` |
| `wifiSignal` | `int?` | `a5190_device_info.dart @0x45ac2b4` |
| `productCode` | `String?` | `a5190_device_info.dart @0x45ac338` |
| `dynamicLoadBalancing` | `int?` | `a5190_device_info.dart @0x45ac3bc` |
| `weekdayStart` | `String?` | `a5190_device_info.dart @0x45ac440` |
| `weekdayEnd` | `String?` | `a5190_device_info.dart @0x45ac4c4` |
| `weekendStart` | `String?` | `a5190_device_info.dart @0x45ac548` |
| `weekendEnd` | `String?` | `a5190_device_info.dart @0x45ac5cc` |
| `carChargerLockStatus` | `int?` | `a5190_device_info.dart @0x45ac650` |
| `maximumCurrentLimit` | `int?` | `a5190_device_info.dart @0x45ac6d4` |
| `lightBrightness` | `int?` | `a5190_device_info.dart @0x45ac758` |
| `gunStatus` | `int?` | `a5190_device_info.dart @0x45ac7dc` |
| `otaStatus` | `int?` | `a5190_device_info.dart @0x45ac860` |
| `workStatus` | `int?` | `a5190_device_info.dart @0x45ac8e4` |
| `networkingMethod` | `int?` | `a5190_device_info.dart @0x45ac968` |
| `packageVersion` | `int?` | `a5190_device_info.dart @0x45ac9ec` |
| `mcuVersion` | `String?` | `a5190_device_info.dart @0x45aca70` |
| `moduleVersion` | `String?` | `a5190_device_info.dart @0x45acaf4` |
| `initSettings` | `int?` | `a5190_device_info.dart @0x45acb78` |
| `rfidCardMaxNum` | `int` | `a5190_device_info.dart @0x45acbfc` |
| `maxDelayStartTime` | `int?` | `a5190_device_info.dart @0x45acc8c` |
| `meterConnMode` | `int` | `a5190_device_info.dart @0x45acd2c` |
| `loadBalancingErrorCode` | `int` | `a5190_device_info.dart @0x45acdbc` |
| `greenEnergyPriorityErrorCode` | `int` | `a5190_device_info.dart @0x45ace4c` |
| `boostMode` | `int?` | `a5190_device_info.dart @0x45acedc` |
| `schedChargeSwitch` | `bool` (read as `value == true`) | `a5190_device_info.dart @0x45acf7c` |
| `everyDaySwitch` | `bool` | `a5190_device_info.dart @0x45acfd0` |
| `plugAndChargeSwitch` | `bool` (read as `value == true`) | `a5190_device_info.dart @0x45ad054` |
| `rfidCardSwitch` | `bool` (read as `value == true`) | `a5190_device_info.dart @0x45ad0a8` |
| `aTouchSwitch` | `bool` (read as `value == true`) | `a5190_device_info.dart @0x45ad0fc` |
| `electricMeterSwitch` | `bool` (read as `value == true`) | `a5190_device_info.dart @0x45ad150` |
| `smartChargingSwitch` | `bool` (read as `value == true`) | `a5190_device_info.dart @0x45ad1a4` |
| `delayStartSwitch` | `bool` (read as `value == true`) | `a5190_device_info.dart @0x45ad1f8` |
| `rechargingPowerOutage` | `bool` (read as `value == true`) | `a5190_device_info.dart @0x45ad24c` |
| `loadBalancingSwitch` | `bool` (read as `value == true`) | `a5190_device_info.dart @0x45ad2a0` |
| `greenEnergyPrioritySwitch` | `bool` (read as `value == true`) | `a5190_device_info.dart @0x45ad2f4` |
| `loadBalancingConnectedType` | `int?` | `a5190_device_info.dart @0x45ad348` |
| `loadBalancingConnectionMode` | `int?` | `a5190_device_info.dart @0x45ad3cc` |
| `loadBalancingConnectedId` | `String?` | `a5190_device_info.dart @0x45ad450` |
| `greenEnergyPriorityConnectedId` | `String?` | `a5190_device_info.dart @0x45ad4d4` |
| `greenEnergyPriorityChargingMode` | `int?` | `a5190_device_info.dart @0x45ad558` |
| `loadBalancingMainBreakerCurrent` | `int?` | `a5190_device_info.dart @0x45ad5dc` |
| `greenEnergyPriorityMinOutputCurrent` | `int?` | `a5190_device_info.dart @0x45ad660` |
| `greenEnergyPriorityConnectedType` | `int?` | `a5190_device_info.dart @0x45ad6e4` |
| `greenEnergyPriorityConnectionMode` | `int?` | `a5190_device_info.dart @0x45ad768` |
| `greenEnergyPriorityThreePhaseSwitch` | `bool` (read as `value == true`) | `a5190_device_info.dart @0x45ad7ec` |
| `version` | `String?` | `a5190_device_info.dart @0x45ad840` |
| `supportOcppServiceSwitching` | `int?` | `a5190_device_info.dart @0x45ad8c4` |
| `supportLedControl` | `int?` | `a5190_device_info.dart @0x45ad948` |
| `supportIOPowerControl` | `int?` | `a5190_device_info.dart @0x45ada50` |
| `supportShareMeter` | `int` | `a5190_device_info.dart @0x45adad4` |
| `supportIrMeter` | `int` | `a5190_device_info.dart @0x45adb64` |
| `shareMeterFlag` | `int` | `a5190_device_info.dart @0x45adbf4` |
| `ledSwitch` | `int?` | `a5190_device_info.dart @0x45adc94` |
| `ledCloseStartTime` | `List<int>?` (typed list cast) | `a5190_device_info.dart @0x45add1c` |
| `ledCloseEndTime` | `List<int>?` (typed list cast) | `a5190_device_info.dart @0x45addf4` |
| `ioDetectionSwitch` | `int?` | `a5190_device_info.dart @0x45ae1fc` |
| `ioDetectionType` | `int?` | `a5190_device_info.dart @0x45ae284` |
| `ioDetectionMaxCurrent` | `int?` | `a5190_device_info.dart @0x45ae30c` |
| `aTouchSwipeDown` | `int?` | `a5190_device_info.dart @0x45ae394` |
| `aTouchSwipeUp` | `int?` | `a5190_device_info.dart @0x45ae41c` |
| `rainTouchPreventionStatus` | `int?` | `a5190_device_info.dart @0x45ae4a4` |
| `chargerMode` | `int?` | `a5190_device_info.dart @0x45ae52c` |

The reads of `ledCloseStartTime`, `ledCloseEndTime` and `errorCodeArray` occur twice each in `fromJson` (null test and cast). For the app-side writes of the switches see [../devices/ev_charger.md](../devices/ev_charger.md#values-the-app-writes): the writer passes a Dart boolean.

## Produced by

No cloud endpoint. The charger's device info arrives through the IoT kit (`akiot.device.notification_events`, event `event_charging_real_time_data`, subscribed in `integrations_setting_logic.dart @0x33b6a80`, `@0x33b6b44`). Upstream maps the corresponding A5191 MQTT fields (`api/mqttmap.py`, upstream-confirmed); the MQTT owner page `mqtt/a5191.md` does not exist yet.

## Consumed by

EV charger "Integrations" page: `IntegrationsSettingLogic` (`integrations_setting_logic.dart`): `refreshSupportProtocolList` (`@0x35f51e8`), `analyzeModbusConnectError` (`@0x35f4740`), `getPhaseValue` (`@0x39727f4`), `getModbusMaxCurrent` (`@0x3972900`), `getModbusIpAddressTips` (`@0x39729dc`), `setModbusTcpStatus` (`@0x3972cfc`); and `integrations_setting_page.dart` (display sites cited in Fields).

## Changed since 3.18.0

No change found for the Modbus keys: all eight key strings are in the 3.18.0 pool and `analyzeModbusConnectError` exists in 3.18.0 `integrations_setting_logic.dart` (string-level comparison; the 3.18.0 casts were not re-read).

## Known unknowns

- The meaning of the other bits of `errorCodeArray`.
- How the IoT kit maps these JSON keys to MQTT or Bluetooth fields.
