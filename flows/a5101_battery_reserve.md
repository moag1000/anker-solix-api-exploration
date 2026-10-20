> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# A5101 HES battery reserve

How the app changes the battery reserve (`conserve_percent`) of an X1 HES (A5101 family) with the slider on the system policy page: a cloud `device_command` when the station is reachable through the cloud, or a Bluetooth write that is synchronised to the cloud afterwards. The request body is owned by [device_command](../api/charging_hes_svc/device_command.md); the Bluetooth write family by [ble/a5101.md](../ble/a5101.md). "Audit row N" counts the data rows of [../docs/audit/FLOWS.md](../docs/audit/FLOWS.md), see the [README](README.md#audit-row-numbers).

## Trigger (UI action)

On the system policy page (`system_policy_view.dart`) the user drags the reserve slider. The slider closure (`@0x3eb8b7c`) builds the slider; its release callback (closure `@0x3eb8ce4`) calls `checkConserveEnergyAndChargeSoc` (`@0x3eb8da4`) and then `SystemPolicyLogic::sendDeviceCommandOfConservepercent` with 100 minus the slider value (`r1 = 100` and `sub x3, x1, x0`, unboxed, at `@0x3eb8dc0` and `@0x3eb8dc4`; call at `@0x3eb8dd0`, function `system_policy_logic.dart @0x3eb8e28`).

## Preconditions

- Slider range: minimum 0 (zero-register store at `system_policy_view.dart @0x3eb8cb0`), maximum 100.0 (double immediate), and the displayed value is the inverted reserve: the slider shows 100 minus `conserve_percent` (`fsub` at `@0x3eb8c60`), so a full slider is a reserve of 0.
- The slider value falls back to 80.0 (double immediate at `@0x3eb8c20`) when the controller value is above 100 or below 0 (two `fcmp` branches at `@0x3eb8bd8` and `@0x3eb8c18`), not only when it is below 0.
- Conflict check: `checkConserveEnergyAndChargeSoc` shows the dialog `powerConflictDialogTitle` with `powerConflictDialogDetail` and the button `toAdjust` when the new reserve conflicts with the charge SOC setting (`system_policy_logic.dart @0x28ebf54` `getChargeSocTipShow`, texts at `@0x28ebf7c`, `@0x28ebf88`, `@0x28ebf98`, dialog at `@0x28ebfe4`); the rule is in the next bullet.
- Transport choice inside `sendDeviceCommandOfConservepercent`: the cloud path is taken when the page's connection data is non-null and both its flags are true (`field_2b`, `field_93`; `system_policy_logic.dart @0x3eb8e74`, `@0x3eb8e84`, `@0x3eb8e90`); otherwise the Bluetooth path. The Bluetooth branch is chosen by these flags, not by a failure of the cloud request: on the traced cloud path the same tap sends no Bluetooth write (the Bluetooth branch was not walked to its end), and Bluetooth is not a fallback for a station that is on WiFi (community finding, see [ble/protocol.md](../ble/protocol.md#connection-routing-and-the-wifi-exclusion-rule)).
- Initial slider state (before the device state is loaded): the page state `SystemPolicyState` creates the reserve value `field_23` as `IntExtension.obs` of the immediate 0x14 (`system_policy_state.dart @0x3eb087c`, a Smi argument, so 10; the old page's 20 is the raw immediate). The slider closure reads this field (`system_policy_view.dart @0x3eb8bb8`) and shows 100 minus it, so the slider starts at 90 and stays there until the device state overwrites the field. This is an app-side placeholder, not a device default.
- Conflict rule (`checkConserveEnergyAndChargeSoc`, `system_policy_logic.dart @0x28ebe9c`): it does nothing unless the state flag `field_9b` is true (`tbz` at `@0x28ebecc`; the flag is set by the listener closure `@0x28eb618` when the delivered object is non-null, `@0x28ebd50` to `@0x28ebd60`). It then sets the flag `field_a7` to whether the reserve value `field_23` (untagged with `LoadInt32Instr`) is greater than the charge-SOC value `field_9f` (64-bit unboxed, default 100 at `system_policy_state.dart @0x3eb0754` with `stur x0`; the listener writes it from a nested integer of the delivered object, default 100 at `@0x28ebdc0`, store `@0x28ebdd8`). When that holds and the persisted flag `chargeSocTipShow` (SharedPreferences bool, default false; `sp_util_impl.dart` `getChargeSocTipShow` read at `@0x28ec064`) is not true (`tbz` at `@0x28ebf58`), the dialog is shown. The dialog button closure (`@0x28ec088`) stores `chargeSocTipShow` as true (`setChargeSocTipShow`, `@0x28ec0b8`) and dismisses the dialog, so the dialog appears once per installation (app side). The compare reads the reserve value as it is held in the page state when the slider is released; the unit relation to the charge SOC limit is not decoded.

## Steps

| # | actor | action | owner page link | asm citation |
|---|---|---|---|---|
| 1 | user | Releases the slider. | this page | `system_policy_view.dart @0x3eb8dd0` |
| 2 | app | Runs the conflict check (Preconditions) and calls `sendDeviceCommandOfConservepercent(100 - slider)`. | this page | `system_policy_view.dart @0x3eb8da4`, `@0x3eb8dc4` |
| 3 | app | Cloud path: stores 1 in the page field `field_c3` (an unboxed command-kind marker, the debounce key) and builds the body `{"conserve_percent": <int>}` (the value is boxed with `BoxInt64Instr`). | this page | `system_policy_logic.dart @0x3eb8e94`, `@0x3eb8eac`, `@0x3eb8ebc`, `@0x3eb8edc` |
| 4 | app | `sendDeviceCommondOfNetWork` debounces by `field_c3` and `sendDeviceCommandWithDebounce` sends the `device_command` request with `electricityStrategy` set to the body, with a 10 s timer per key (same chain as [a5101_work_mode_change.md](a5101_work_mode_change.md#steps), steps 4 and 5). | [device_command](../api/charging_hes_svc/device_command.md) | `system_policy_logic.dart @0x3eb8f04`, `@0x24a133c`, `@0x24a13d0` |
| 5 | app | Bluetooth path (not on the cloud path): `isBleConnected` true calls `A5101BleLogic::setBatteryReserve(value)`, which writes the value as a one-element attribute list with the code pair `[0, 1]` through `setAtt`. In the set map `[0, 1]` is the key `0x0001` bound to the enum member `batteryReserve` (`a5101_commands.dart @0x3b89418` with the member loaded at `@0x3b89458`, pool object `pp+0x2b348`, enum index 0x21); [mqtt/a5101.md](../mqtt/a5101.md#data-code-maps-setdatacodemap-and-getdatacodemap) lists `batteryReserve` as `0x0001`. `isBleConnected` false calls `handlerDeviceCommandOfConservepercent(false)`. | [ble/a5101.md](../ble/a5101.md) | `system_policy_logic.dart @0x3eb8f1c`, `@0x3eb8f2c`, `@0x3eb8f48`; `a5101_ble_logic.dart @0x3eb8ff4` (pair), `@0x3eb9070` (`setAtt`) |
| 6 | device | After a Bluetooth write the app receives the result as the UI message with id 650 (`cmp x1, #0x28a`, unboxed) carrying a bool. | this page | `system_policy_logic.dart @0x278ac6c` |
| 7 | app | `handlerDeviceCommandOfConservepercent(ok)`: on true it logs `近场设置` (near-field setting) and sends the same `{conserve_percent}` body to the cloud with `sendDeviceCommand` (arguments `electricityStrategy`, `mainSn`, `time`); on false (or when the device test fails) it calls `updateEnergyValue`, which restores the displayed value. | [device_command](../api/charging_hes_svc/device_command.md) | `system_policy_logic.dart @0x278acbc` (call), `@0x24a3534` (bool test), `@0x24a3620`, `@0x24a3680`, `@0x24a3730` (`sendDeviceCommand`), `@0x24a37fc` (`updateEnergyValue`) |

## Side effects

- The Bluetooth write is followed by a cloud sync (step 7); the two sends are not in the same call. With Bluetooth failure the page restores the old value.
- The debounce key replaces a pending reserve command with the newest value on the cloud path.
- The old page's statement that the reserve command does not change other settings holds: the body carries only `conserve_percent`.
- The cloud sync of step 7 is gated: `handlerDeviceCommandOfConservepercent(true)` first writes the reserve value from the page state into the device object (offset 323, `system_policy_logic.dart @0x24a35e8`) and then continues to the cloud request only when the controller flag `field_87` is true (`tbnz` at `@0x24a3618` returns otherwise, `@0x24a3800`). When the flag is false only the local write is done.

## Timing (delays/polling)

10 s: the timer of `sendDeviceCommandWithDebounce` (`system_policy_logic.dart @0x24a133c`) uses the pool `Duration` `pp+0x12208` with `off_8` 0x989680 = 10,000,000 microseconds (a pool object value, not a register immediate). No polling.

## Failure paths

- Cloud failure: closure `@0x24a13ec` logs `sendDeviceCommandFail--->`, calls `setMattResult` and shows `deviceIsOffline` for the code 200000 (raw 400000 at `@0x24a1464`, tagged compare; listed on [errors](../api/errors.md)).
- Bluetooth failure: result message false, `updateEnergyValue` restores the slider (step 7).
- Bluetooth not connected on the Bluetooth path: `handlerDeviceCommandOfConservepercent(false)`.

## Since/changed

Corrections of the old FLOWS.md (audit rows in brackets), with the old value:

- Confirmed: slider 0 to 100 with the inverted display (row 64, OK); fallback 80 (row 65, OK) but the condition is "above 100 or below 0", not only "below 0".
- The old default initial value of 20 percent could not be found (row 66, UNVERIFIABLE): only unrelated size constants appear in the searched files; the page state creates the reserve field from the immediate 0x14, a Smi argument, so 10 (Preconditions, initial slider state); the old 20 is the raw immediate.
- New in this trace: the Bluetooth path is followed by a cloud sync (steps 6 and 7), and the conflict dialog `powerConflictDialog*`.

## Known unknowns

- Whether the flag that gates the cloud sync of step 7 (`field_87` of the controller object, see Preconditions) is true exactly when the station is online was not determined: its name is not in the dump and its setters were not traced (traced 2026-10-20, `system_policy_logic.dart @0x24a3618`).
