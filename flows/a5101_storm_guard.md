> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# A5101 HES storm guard (disaster preparedness)

How the app starts or stops the manual backup power (manual disaster preparedness) and switches the automatic disaster preparedness of an X1 HES (A5101 family) from the system policy page. Each setting has a cloud path and a Bluetooth path; the path is chosen per tap, and after a successful Bluetooth write the app synchronises the value to the cloud in a second request. The cloud request is owned by [device_command](../api/charging_hes_svc/device_command.md), the automatic data read by [get_current_disaster_prepare_details](../api/charging_hes_svc/get_current_disaster_prepare_details.md), the Bluetooth opcode `0115` of the automatic data by [mqtt/a5101.md](../mqtt/a5101.md#0115-sendautodisasterdatacmd). "Audit row N" counts the data rows of [../docs/audit/FLOWS.md](../docs/audit/FLOWS.md), see the [README](README.md#audit-row-numbers).

## Trigger (UI action)

- Manual: on the system policy page the manual backup power card calls `SystemPolicyLogic::sendDeviceCommandOfManualBackupPower` (calls at `system_policy_view.dart @0x3ebc040`, `@0x3ebcd04`, `@0x3ebcf0c`; function `system_policy_logic.dart @0x3ebc05c`) with a parameter map.
- Automatic: the automatic disaster preparedness switch calls `switchAutoDisasterPrepareStatue` (call at `system_policy_view.dart @0x3ebd27c`, function `system_policy_logic.dart @0x3ebd298`).

## Preconditions

- Same transport test as on the other system policy commands: the cloud path is taken when the page's connection data is non-null and both its flags are true (`field_2b`, `field_93`); otherwise the Bluetooth path. The Bluetooth branch is chosen by these flags, not by a failure of the cloud request: the app never sends the same command over both paths in one tap, and Bluetooth is not a fallback for a station that is on WiFi (community finding, see [ble/protocol.md](../ble/protocol.md#connection-routing-and-the-wifi-exclusion-rule)). Manual: `system_policy_logic.dart @0x3ebc0cc`, `@0x3ebc0d4`, `@0x3ebc0e0`. Automatic: `@0x3ebd358`, `@0x3ebd360`, `@0x3ebd36c`.
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

## Timing (delays/polling)

The cloud path uses the 10 s per-key timer of `sendDeviceCommandWithDebounce` (`system_policy_logic.dart @0x24a133c`, pool `Duration` `pp+0x12208`, `off_8` 0x989680 = 10,000,000 microseconds, see [a5101_work_mode_change.md](a5101_work_mode_change.md#timing-delayspolling)). The Bluetooth path has no delay in these functions. No polling.

## Failure paths

- Cloud failure: the shared failure callback `@0x24a13ec` logs `sendDeviceCommandFail--->` and shows `deviceIsOffline` for code 200000 (see [errors](../api/errors.md)).
- Manual Bluetooth write not accepted: `handlerDeviceCommandOfManualBackupPower(false)` path; the body was not read beyond the success branch.
- Automatic Bluetooth path, cloud read failure: step 10.

## Since/changed

Corrections of the old FLOWS.md (audit rows in brackets):

- The two `{"dpe":...}` texts are string literals in the app and contain digits that the Smi rule does not touch (row 61, NOT-FROM-ASM). In 3.24.3 they are built in `sendDeviceCommandOfManualBackupPower` (`system_policy_logic.dart @0x3ebc268`, `@0x3ebc2c0`; pool strings `pp+0xbe2a8`, `pp+0xbe2b0`, `pp+0xbe2b8`).
- The old "`AutoDisasterMixin::request()` via HTTP" is not the path of this page: the system policy page reads `getCurrentDisasterPrepareDetails` and sends the result over Bluetooth, or sends one cloud command (step 7).
- The old "enable and disable are sent AFTER the sync" is not visible in `deviceToAutoDisasterStatus`; the enable state is a named argument of the details request.
- The old statement that the SOC reserve has no hard-coded default is confirmed.

## Known unknowns

- The wire form of the Bluetooth value of `manualBackupPower` (the text is built; how `setAtt` encodes it as bytes was not read).
- The body of the failure branch of `handlerDeviceCommandOfManualBackupPower` and the message ids that trigger the result handlers (`onMessageDispatch` compares ids 608, 650 and 651 at `system_policy_logic.dart @0x278aadc`, `@0x278ac6c`, `@0x278acc4`; only 650 was mapped, to the reserve result).
- The other users of `AutoDisasterMixin` (`ak_soft_ems/common_location/auto_disaster.dart`, `charging/ui/page/station/mixin/auto_disaster.dart`) and whether manual and automatic can be active together.
- The owner pages do not list the `dpe` / `dpn` keys of the manual text yet.
