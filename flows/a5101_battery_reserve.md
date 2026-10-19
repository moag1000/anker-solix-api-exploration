> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# A5101 HES battery reserve

How the app changes the battery reserve (`conserve_percent`) of an X1 HES (A5101 family) with the slider on the system policy page: a cloud `device_command` when the station is reachable through the cloud, or a Bluetooth write that is synchronised to the cloud afterwards. The request body is owned by [device_command](../api/charging_hes_svc/device_command.md); the Bluetooth write family by [ble/a5101.md](../ble/a5101.md). "Audit row N" counts the data rows of [../docs/audit/FLOWS.md](../docs/audit/FLOWS.md), see the [README](README.md#audit-row-numbers).

## Trigger (UI action)

On the system policy page (`system_policy_view.dart`) the user drags the reserve slider. The slider closure (`@0x3eb8b7c`) builds the slider; its release callback (closure `@0x3eb8ce4`) calls `checkConserveEnergyAndChargeSoc` (`@0x3eb8da4`) and then `SystemPolicyLogic::sendDeviceCommandOfConservepercent` with 100 minus the slider value (`r1 = 100` and `sub x3, x1, x0`, unboxed, at `@0x3eb8dc0` and `@0x3eb8dc4`; call at `@0x3eb8dd0`, function `system_policy_logic.dart @0x3eb8e28`).

## Preconditions

- Slider range: minimum 0 (zero-register store at `system_policy_view.dart @0x3eb8cb0`), maximum 100.0 (double immediate), and the displayed value is the inverted reserve: the slider shows 100 minus `conserve_percent` (`fsub` at `@0x3eb8c60`), so a full slider is a reserve of 0.
- The slider value falls back to 80.0 (double immediate at `@0x3eb8c20`) when the controller value is above 100 or below 0 (two `fcmp` branches at `@0x3eb8bd8` and `@0x3eb8c18`), not only when it is below 0.
- Conflict check: `checkConserveEnergyAndChargeSoc` shows the dialog `powerConflictDialogTitle` with `powerConflictDialogDetail` and the button `toAdjust` when the new reserve conflicts with the charge SOC setting (`system_policy_logic.dart @0x28ebf54` `getChargeSocTipShow`, texts at `@0x28ebf7c`, `@0x28ebf88`, `@0x28ebf98`, dialog at `@0x28ebfe4`); the conflict rule itself was not decoded.
- Transport choice inside `sendDeviceCommandOfConservepercent`: the cloud path is taken when the page's connection data is non-null and both its flags are true (`field_2b`, `field_93`; `system_policy_logic.dart @0x3eb8e74`, `@0x3eb8e84`, `@0x3eb8e90`); otherwise the Bluetooth path.

## Steps

| # | actor | action | owner page link | asm citation |
|---|---|---|---|---|
| 1 | user | Releases the slider. | this page | `system_policy_view.dart @0x3eb8dd0` |
| 2 | app | Runs the conflict check (Preconditions) and calls `sendDeviceCommandOfConservepercent(100 - slider)`. | this page | `system_policy_view.dart @0x3eb8da4`, `@0x3eb8dc4` |
| 3 | app | Cloud path: stores 1 in the page field `field_c3` (an unboxed command-kind marker, the debounce key) and builds the body `{"conserve_percent": <int>}` (the value is boxed with `BoxInt64Instr`). | this page | `system_policy_logic.dart @0x3eb8e94`, `@0x3eb8eac`, `@0x3eb8ebc`, `@0x3eb8edc` |
| 4 | app | `sendDeviceCommondOfNetWork` debounces by `field_c3` and `sendDeviceCommandWithDebounce` sends the `device_command` request with `electricityStrategy` set to the body, with a 10 s timer per key (same chain as [a5101_work_mode_change.md](a5101_work_mode_change.md#steps), steps 4 and 5). | [device_command](../api/charging_hes_svc/device_command.md) | `system_policy_logic.dart @0x3eb8f04`, `@0x24a133c`, `@0x24a13d0` |
| 5 | app | Bluetooth path (not on the cloud path): `isBleConnected` true calls `A5101BleLogic::setBatteryReserve(value)`, which writes the value as a one-element attribute list with the code pair `[0, 1]` through `setAtt`. `isBleConnected` false calls `handlerDeviceCommandOfConservepercent(false)`. | [ble/a5101.md](../ble/a5101.md) | `system_policy_logic.dart @0x3eb8f1c`, `@0x3eb8f2c`, `@0x3eb8f48`; `a5101_ble_logic.dart @0x3eb8ff4` (pair), `@0x3eb9070` (`setAtt`) |
| 6 | device | After a Bluetooth write the app receives the result as the UI message with id 650 (`cmp x1, #0x28a`, unboxed) carrying a bool. | this page | `system_policy_logic.dart @0x278ac6c` |
| 7 | app | `handlerDeviceCommandOfConservepercent(ok)`: on true it logs `近场设置` (near-field setting) and sends the same `{conserve_percent}` body to the cloud with `sendDeviceCommand` (arguments `electricityStrategy`, `mainSn`, `time`); on false (or when the device test fails) it calls `updateEnergyValue`, which restores the displayed value. | [device_command](../api/charging_hes_svc/device_command.md) | `system_policy_logic.dart @0x278acbc` (call), `@0x24a3534` (bool test), `@0x24a3620`, `@0x24a3680`, `@0x24a3730` (`sendDeviceCommand`), `@0x24a37fc` (`updateEnergyValue`) |

## Side effects

- The Bluetooth write is followed by a cloud sync (step 7); the two sends are not in the same call. With Bluetooth failure the page restores the old value.
- The debounce key replaces a pending reserve command with the newest value on the cloud path.
- The old page's statement that the reserve command does not change other settings holds: the body carries only `conserve_percent`.

## Timing (delays/polling)

10 s: the timer of `sendDeviceCommandWithDebounce` (`system_policy_logic.dart @0x24a133c`) uses the pool `Duration` `pp+0x12208` with `off_8` 0x989680 = 10,000,000 microseconds (a pool object value, not a register immediate). No polling.

## Failure paths

- Cloud failure: closure `@0x24a13ec` logs `sendDeviceCommandFail--->`, calls `setMattResult` and shows `deviceIsOffline` for the code 200000 (raw 400000 at `@0x24a1464`, tagged compare; listed on [errors](../api/errors.md)).
- Bluetooth failure: result message false, `updateEnergyValue` restores the slider (step 7).
- Bluetooth not connected on the Bluetooth path: `handlerDeviceCommandOfConservepercent(false)`.

## Since/changed

Corrections of the old FLOWS.md (audit rows in brackets), with the old value:

- Confirmed: slider 0 to 100 with the inverted display (row 64, OK); fallback 80 (row 65, OK) but the condition is "above 100 or below 0", not only "below 0".
- The old default initial value of 20 percent could not be found (row 66, UNVERIFIABLE): only unrelated size constants appear in the searched files; the initial value comes from the device state.
- New in this trace: the Bluetooth path is followed by a cloud sync (steps 6 and 7), and the conflict dialog `powerConflictDialog*`.

## Known unknowns

- The initial value of the slider before the device state is loaded.
- The conflict rule behind `powerConflictDialogDetail` (`getChargeSocTipShow` and the compare at `system_policy_logic.dart @0x28ebf14`).
- Whether the cloud sync of step 7 also runs when the Bluetooth write was made while the station is online (the cloud path is preferred in that case).
- The code pair `[0, 1]` against the data-code map of [mqtt/a5101.md](../mqtt/a5101.md#data-code-maps-setdatacodemap-and-getdatacodemap).
