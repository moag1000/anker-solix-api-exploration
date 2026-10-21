> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# A5101 HES storm guard (disaster preparedness)

How the app starts or stops the manual backup power (manual disaster preparedness) and switches the automatic disaster preparedness of an X1 HES (A5101 family) from the system policy page. Each setting has a cloud path and a Bluetooth path; the path is chosen per tap, and after a successful Bluetooth write the app synchronises the value to the cloud in a second request. The cloud request is owned by [device_command](../api/charging_hes_svc/device_command.md), the automatic data read by [get_current_disaster_prepare_details](../api/charging_hes_svc/get_current_disaster_prepare_details.md), the Bluetooth opcode `0115` of the automatic data by [mqtt/a5101.md](../mqtt/a5101.md#0115-sendautodisasterdatacmd). "Audit row N" counts the data rows of [../docs/audit/FLOWS.md](../docs/audit/FLOWS.md), see the [README](README.md#audit-row-numbers).

## Trigger (UI action)

- Manual: on the system policy page the manual backup power card calls `SystemPolicyLogic::sendDeviceCommandOfManualBackupPower` (calls at `system_policy_view.dart @0x3ebc040`, `@0x3ebcd04`, `@0x3ebcf0c`; function `system_policy_logic.dart @0x3ebc05c`) with a parameter map.
- Automatic: the automatic disaster preparedness switch calls `switchAutoDisasterPrepareStatue` (call at `system_policy_view.dart @0x3ebd27c`, function `system_policy_logic.dart @0x3ebd298`).

## Preconditions

- Same transport test as on the other system policy commands: the cloud path is taken when the page's connection data is non-null and both its flags are true (`field_2b`, `field_93`); otherwise the Bluetooth path. The Bluetooth branch is chosen by these flags, not by a failure of the cloud request: on the traced cloud path the same tap sends no Bluetooth write (the Bluetooth branch was not walked to its end), and Bluetooth is not a fallback for a station that is on WiFi (community finding, see [ble/protocol.md](../ble/protocol.md#connection-routing-and-the-wifi-exclusion-rule)). Manual: `system_policy_logic.dart @0x3ebc0cc`, `@0x3ebc0d4`, `@0x3ebc0e0`. Automatic: `@0x3ebd358`, `@0x3ebd360`, `@0x3ebd36c`.
- The manual parameter map carries the keys `disaster_preparedness_enable`, `disaster_preparedness_start`, `disaster_preparedness_end` and `disaster_preparedness_soc` (`system_policy_logic.dart @0x3ebc168`, `@0x3ebc1c4`, `@0x3ebc1fc`, `@0x3ebc234`). The SOC reserve is user-set; no default is hard-coded in these functions.

## Steps

| # | actor | action | owner page link | asm citation |
|---|---|---|---|---|
| 1 | user | Manual: sets the backup window and SOC, or cancels it. | this page | `system_policy_view.dart @0x3ebc040` |
| 2 | app | Manual, cloud path: logs `onLine`, stores 5 in `field_c3` (unboxed command-kind marker) and sends the parameter map with `sendDeviceCommondOfNetWork` (debounced, then `device_command`). | [device_command](../api/charging_hes_svc/device_command.md) | `system_policy_logic.dart @0x3ebc0e4`, `@0x3ebc0f8`, `@0x3ebc12c` |
| 3 | app | Manual, Bluetooth path: if `isBleConnected` is false it calls `handlerDeviceCommandOfManualBackupPower(false)`. Otherwise it compares `disaster_preparedness_enable` with 1 (the raw 2 is a tagged Smi) and builds a text with the keys `dpe` and `dpn`: enabled gives `{"dpe":1,"dpn":[{"start":<start>,"end":<end>,"type":1,"soc":<soc>}]}`, disabled gives `{"dpe":0,"dpn":[]}`; the digits inside the quotes are string text. | this page | `system_policy_logic.dart @0x3ebc138`, `@0x3ebc148`, `@0x3ebc19c`, `@0x3ebc268`, `@0x3ebc2c0` |
| 4 | app | Manual, Bluetooth path: keeps the map in a page field and calls `A5101BleLogic::setManualBackupPower`, which writes the text with the code pair `[0xf0, 0x0c]` (the data code `manualBackupPower`) through `setAtt`. | [mqtt/a5101.md](../mqtt/a5101.md#data-code-maps-setdatacodemap-and-getdatacodemap) | `system_policy_logic.dart @0x3ebc34c`, `@0x3ebc370`; `a5101_ble_logic.dart @0x3ebc41c` (pair), `@0x3ebc480` (`setAtt`) |
| 5 | app | Manual result: `handlerDeviceCommandOfManualBackupPower(ok)` logs `近场设置` (near-field setting) and, on success, builds the list text `[{"start":..,"end":..,"type":1,"soc":..}]` and syncs it to the cloud with `sendDeviceCommand` (arguments `electricityStrategy`, `mainSn`, `time`). | [device_command](../api/charging_hes_svc/device_command.md) | `system_policy_logic.dart @0x278b988`, `@0x278bbc8`, `@0x278bc88` |
| 6 | user | Automatic: toggles the automatic switch. | this page | `system_policy_view.dart @0x3ebd27c` |
| 7 | app | Automatic, cloud path: `netToSetAutoDisasterStatus` stores 6 in `field_c3` and sends the body with the single key `auto_disaster_preparedness_enable` with `sendDeviceCommondOfNetWork`. | [device_command](../api/charging_hes_svc/device_command.md) | `system_policy_logic.dart @0x3ebd374` (call), `@0x3ebee58`, `@0x3ebee6c`, `@0x3ebeec4` |
| 8 | app | Automatic, Bluetooth path: `deviceToAutoDisasterStatus` reads the disaster preparedness details from the cloud for the station (`getCurrentDisasterPrepareDetails`, named argument `autoDisasterEnable`), builds an `AutoDisasterCommandModel` from the returned list, encodes it as JSON and sends it with `sendAutoDisasterData` over Bluetooth. The enable state travels in the same data; there is no separate enable step after the data in this function. | [get_current_disaster_prepare_details](../api/charging_hes_svc/get_current_disaster_prepare_details.md), [mqtt/a5101.md](../mqtt/a5101.md#0115-sendautodisasterdatacmd) | `system_policy_logic.dart @0x3ebd380` (call), `@0x3ebd410`, `@0x3ebd418`, `@0x3ebd46c`, `@0x3ebd488`, `@0x3ebd4d4` |
| 9 | app | Automatic result: `handlerDeviceCommandOfAutoDisaster` with the marker `syncToCloud` sends `auto_disaster_preparedness_enable` to the cloud with `sendDeviceCommand`. | [device_command](../api/charging_hes_svc/device_command.md) | `system_policy_logic.dart @0x24a1fc0`, `@0x24a21c0`, `@0x24a2288` |
| 10 | app | Automatic failure on the Bluetooth path: the cloud read of step 8 fails, the loading overlay is dismissed and `switchAutoDisasterStatusError` restores the switch. | this page | `system_policy_logic.dart @0x3ebd4e0`, `@0x3ebd510`, `@0x3ebd518` |

## Side effects

- `field_c3` records the command kind for the debouncer: 5 for the manual backup power, 6 for the automatic switch (both unboxed stores), so a newer command of the same kind replaces a pending one on the cloud path.
- The Bluetooth results are followed by cloud syncs (steps 5 and 9), so the cloud copy is written after the device accepted the change.
- Manual and automatic settings use different markers and different bodies; whether both can be active at once is not read here.
- Wire form of the manual value (app side): `A5101BleLogic::setManualBackupPower` (`a5101_ble_logic.dart @0x3ebc38c`) builds one `SetList` entry with the code `[0xf0, 0x0c]` (`const [0xf0, 0xc]` at `@0x3ebc41c`), value type 0 (zero-register store at `@0x3ebc42c`) and the text as value; `setAtt` (`a5101_device_controller.dart @0x23bc7d0`) encodes a type-0 value as the UTF-8 bytes of the text (`Utf8Encoder.convert` at `@0x23bca38`, `writeParamWithType` at `@0x23bcaa4`). The payload starts with the raw byte 161 (`BleWritePayloadHelper.field_b`, `@0x23bc834`), then the one-byte sequence counter at device offset 735 (wraps at 0x100, `@0x23bc92c`), the item count and the items; the frame leaves through `formatCommand` with the opcode list `[1, 0]` (`@0x23bcea8`, the `setAtt` opcode `0100` of [ble/a5101.md](../ble/a5101.md)) and `isEncrypted` true (`@0x23bceb0`), then `sendCommand`. Fact belongs on ble/a5101.md (SetAtt payload) and mqtt/a5101.md (`manualBackupPower` text with the keys `dpe` and `dpn`).
- Result handlers (`system_policy_logic.dart onMessageDispatch @0x278aa5c`, message id read with a 64-bit load and compared raw): 608 (`cmp x1, #0x260`, `@0x278aadc`) is the device online status change (logs `isDeviceOnline`, then `setDefaultDataOfBle`, `@0x278ac64`); 609 (0x261) is the MQTT order result and the device state and info models; 650 (0x28a) calls `handlerDeviceCommandOfConservepercent`; 651 (0x28b) `handlerDeviceCommandOfMode`; 652 (0x28c) `handlerDeviceCommandOfGridRecharging`; 653 (0x28d) `handlerDeviceCommandOfPeckShaving` (the app's spelling); 656 (0x290) calls `handlerDeviceCommandOfManualBackupPower` (`@0x278ae1c`); 681 (0x2a9) is the automatic disaster result (`handlerDeviceCommandOfAutoDisaster` on success, `switchAutoDisasterStatusError` on error, `@0x278b49c`, `@0x278b510`). The bool payload of 650 to 653 and 656 is the Bluetooth result.
- Other users of `AutoDisasterMixin` (found from the mixin-application class names in the dump): `PowerUsageScenarioController` (`ak_soft_ems/ems_list/power_usage_scenario_controller.dart`), `ModeTipLogic` (`micro_hes/.../mode_tip/mode_tip_logic.dart`), `StationLocationController`, the station setting controllers `common_station_setting_logic.dart`, `ax170_station_setting_controller.dart` and `a17e1_station_setting_logic.dart`, and `PpsAutoDisasterFeature` (`ak_soft_pps_ems/.../pps_auto_disaster_feature.dart`). `charging/ui/page/station/mixin/auto_disaster.dart` defines a separate class, `StationAutoDisasterMixin`. Their request paths were not traced.

## Timing (delays/polling)

The cloud path uses the 10 s per-key timer of `sendDeviceCommandWithDebounce` (`system_policy_logic.dart @0x24a133c`, pool `Duration` `pp+0x12208`, `off_8` 0x989680 = 10,000,000 microseconds, see [a5101_work_mode_change.md](a5101_work_mode_change.md#timing-delayspolling)). The Bluetooth path has no delay in these functions. No polling.

## Failure paths

- Cloud failure: the shared failure callback `@0x24a13ec` logs `sendDeviceCommandFail--->` and shows `deviceIsOffline` for code 200000 (see [errors](../api/errors.md)).
- Manual Bluetooth write not accepted: `handlerDeviceCommandOfManualBackupPower(false)` path; the body was not read beyond the success branch.
- Automatic Bluetooth path, cloud read failure: step 10.
- Manual Bluetooth result (`handlerDeviceCommandOfManualBackupPower`, `system_policy_logic.dart @0x278b80c`): with ok true it writes the enable value into the device field at offset 415 (1 or 0 from the page's enable switch, `@0x278b8e8`), builds the list text `[{"start":..,"end":..,"type":1,"soc":..}]` into the device field at offset 359 (`@0x278baf4`), calls `calculateManualRemainingChargeTime` (`@0x278bbac`) and, only when the controller flag `field_87` is true (`@0x278bbbc`), syncs with `sendDeviceCommand` (its success closure logs `近场设置完手动备灾并同步云端成功`, the failure closure `@0x278bd90` logs `近场设置完手动备灾并同步云端失败` and does nothing else). With ok false (`tbnz` at `@0x278b82c`, branch `@0x278bc90`) it sets the page's enable switch from the device field at offset 415 (equal to 1) so the switch returns to the device state.

## Since/changed

Corrections of the old FLOWS.md (audit rows in brackets):

- The two `{"dpe":...}` texts are string literals in the app and contain digits that the Smi rule does not touch (row 61, NOT-FROM-ASM). In 3.24.3 they are built in `sendDeviceCommandOfManualBackupPower` (`system_policy_logic.dart @0x3ebc268`, `@0x3ebc2c0`; pool strings `pp+0xbe2a8`, `pp+0xbe2b0`, `pp+0xbe2b8`).
- The old "`AutoDisasterMixin::request()` via HTTP" is not the path of this page: the system policy page reads `getCurrentDisasterPrepareDetails` and sends the result over Bluetooth, or sends one cloud command (step 7).
- The old "enable and disable are sent AFTER the sync" is not visible in `deviceToAutoDisasterStatus`; the enable state is a named argument of the details request.
- The old statement that the SOC reserve has no hard-coded default is confirmed.

## Known unknowns

- Whether the manual backup window and the automatic disaster preparedness can be active together is device behaviour — reclassified: device, [device test row 127](../docs/DEVICE_TEST_BACKLOG.md#added-2026-10-20-depth-pass).
