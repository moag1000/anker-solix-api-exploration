> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# A5101 HES work mode change

How the app changes the work mode of an X1 HES (A5101 family) from the system policy page: a cloud `device_command` with the new mode when the station is reachable through the cloud, or a Bluetooth write of the mode when it is not. The request body is owned by [device_command](../api/charging_hes_svc/device_command.md); the Bluetooth write family by [ble/a5101.md](../ble/a5101.md). "Audit row N" counts the data rows of [../docs/audit/FLOWS.md](../docs/audit/FLOWS.md), see the [README](README.md#audit-row-numbers).

## Trigger (UI action)

On the system policy page (`system_policy_view.dart`) the user taps one of the mode cards. Each card handler calls `SystemPolicyLogic::sendDeviceCommandOfMode` (`system_policy_logic.dart @0x249f5a0`) with a mode number, directly or through a small wrapper. The handler names come from the log texts in the handlers; the numbers are unboxed register values and therefore real:

| mode card (log or function name) | mode sent | asm citation |
|---|---|---|
| `selfPowered` | 0 | `system_policy_view.dart @0x3ec9dc0` |
| time-of-use (`SmartShiftMode`, `sendDeviceCommandOfTouAndMode`, text `timeOfUse`) | 1 | `system_policy_logic.dart @0x249f50c`, `@0x3ec99c4` |
| `offGridPowerConsumption` | 2 | `system_policy_view.dart @0x3ec477c` |
| `billSavingOptimization` | 11 | `system_policy_view.dart @0x3ec3fbc` |
| time slot (`sendDeviceCommandOfTimeslot`, text `timeSlot`) | 16 | `system_policy_logic.dart @0x3ec7f40`, `@0x3ec7e28` |
| AI EMS (`sendDeviceCommandOfAIEmsMode`) | 20 | `system_policy_logic.dart @0x3eca5e8` |

The old page named 0x10 (16) as AI EMS and left 0x14 (20) open; the function names show 16 is the time-slot mode and 20 the AI EMS mode. The mode names are the app's UI names; which firmware mode each number selects is the device's business.

## Preconditions

- Each card handler logs and may stop before the send when the EMS strategy is disabled, when the station is off-grid, or when Bluetooth is not connected (log texts such as `SystemPolicyPage========selfPowered--->禁用ems策略`, `离网状态`, `蓝牙未连接`, `system_policy_view.dart @0x3ec9c2c`, `@0x3ec9cd0`, `@0x3ec9d0c`). The exact truth table of these guards was not decoded. The off-grid card also refuses a manual off-grid when the battery level is at or below 10 percent and shows `a5101BatteryPowerLow` (`system_policy_view.dart @0x3ec4578`).
- Transport choice inside `sendDeviceCommandOfMode`: the cloud path is taken when the page's connection data is non-null (`system_policy_logic.dart @0x249f624`) and both its flags are true (`field_2b` at `@0x249f648`, `field_93` at `@0x249f654`; `tbnz` branches on false); otherwise the Bluetooth path. The Bluetooth branch is chosen by these flags, not by a failure of the cloud request: the app never sends the same command over both paths in one tap, and Bluetooth is not a fallback for a station that is on WiFi (community finding, see [ble/protocol.md](../ble/protocol.md#connection-routing-and-the-wifi-exclusion-rule)).

## Steps

| # | actor | action | owner page link | asm citation |
|---|---|---|---|---|
| 1 | user | Taps a mode card. | this page | `system_policy_view.dart @0x3ec9dc4`, `@0x3ec4780`, `@0x3ec3fc0`, `@0x3ec97f4` |
| 2 | app | `sendDeviceCommandOfMode` sets the AI-flag value `field_9b` of the device info to `mode == 0x10` and then tests the connection data. | this page | `system_policy_logic.dart @0x249f5f4`, `@0x249f608` |
| 3 | app | Cloud path: stores 2 in the page field `field_c3` (an unboxed command-kind marker, also the debounce key) and builds the body `{"mode": <mode>}`; the mode is the tagged copy of the argument (`lsl x2, x1, #1`). | this page | `system_policy_logic.dart @0x249f5dc`, `@0x249f660`, `@0x249f670`, `@0x249f690` |
| 4 | app | Calls `sendDeviceCommondOfNetWork`, which hands the body to the page's debouncer (`debounce`, key `field_c3`, timer `Duration` zero) and then to `sendDeviceCommandWithDebounce`. | this page | `system_policy_logic.dart @0x249f6b8`, `@0x24a112c`; timer `@0x24a11c8` |
| 5 | app | `sendDeviceCommandWithDebounce` cancels an older timer for the key, arms a 10 s timer and calls `HttpRequestController::sendDeviceCommand` with `electricityStrategy` and an `evchargerSetting` map that holds the key `evcharger_enable` (its value comes from the optional `isCharge` argument). The request is the `device_command` call. | [device_command](../api/charging_hes_svc/device_command.md) | `system_policy_logic.dart @0x24a1310`, `@0x24a133c` (10 s), `@0x24a1364` (key), `@0x24a13d0` (call); body key `electricity_strategy` at `http_request_repository_impl.dart @0x24a0c00` |
| 6 | cloud | Applies the strategy and answers. | [device_command](../api/charging_hes_svc/device_command.md) untagged by design (no app-side fact) |
| 7 | app | Success callback (closure `@0x24a3ddc`): logs `设置备电模式提交成功`. For mode 20 (tagged compare `cmp w1, #0x28`, real 20) it sets the control model to `smartMode`, stores a flag and, if the flag is true, reloads the utility rate plan and the smart-mode subtitle (`_getUtilityRatePlan`, `fetchAndUpdateSmartModeSubtitle`); every other path dismisses the loading overlay. | this page | `system_policy_logic.dart @0x24a3e04`, `@0x24a3e1c`, `@0x24a3eb4`, `@0x24a3ec4`, `@0x24a3eec` |
| 8 | app | Bluetooth path: for mode 20 the loading overlay is dismissed first, then `isBleConnected` decides. Connected: `A5101BleLogic::setShiftMode(mode)` writes the mode as a one-element attribute list with the code pair `[0, 0]` through `setAtt`. Not connected: `handlerDeviceCommandOfMode(false)` handles the failure in the page. | [ble/a5101.md](../ble/a5101.md) | `system_policy_logic.dart @0x249f6c8`, `@0x249f6f0`, `@0x249f6f8`, `@0x249f708`, `@0x249f72c`; `a5101_ble_logic.dart @0x249f7d8` (pair), `@0x249f844` (`setAtt`) |

## Side effects

- The mode request changes only the mode. It does not send `peak_shaving` or `conserve_percent`; those have their own commands ([a5101_battery_reserve.md](a5101_battery_reserve.md) for the reserve).
- The page state `field_c3` records the command kind (2 for a mode change, 1 for the reserve, 5 for the manual backup power; all unboxed stores) and, with the debouncer, replaces a pending command of the same kind.
- The device info flag `field_9b` follows the mode being 16 until the next change.

## Timing (delays/polling)

10 s: the timer armed in `sendDeviceCommandWithDebounce` (`system_policy_logic.dart @0x24a133c`) uses the pool `Duration` `pp+0x12208` with `off_8` 0x989680 = 10,000,000 microseconds (a pool object value, not a register immediate); its closure removes the key (`@0x24a3cd4`). The first debounce step uses a zero `Duration` (`@0x24a11c8`, `off_8` 0). No polling.

## Failure paths

- Cloud failure: closure `@0x24a13ec` calls `setMattResult`, logs `sendDeviceCommandFail--->`, and shows the toast `deviceIsOffline` when the code is 200000 (raw 400000 at `@0x24a1464`, tagged compare, so 200000; listed on [errors](../api/errors.md)), else a generic toast.
- Bluetooth not connected on the Bluetooth path: `handlerDeviceCommandOfMode(false)` (`@0x249f708`); the body of the handler was not read.
- Guards of the cards stop the send with a log line only.

## Since/changed

Corrections of the old FLOWS.md (audit rows in brackets), with the old value:

- Mode values: time-of-use 1, 16 and 20 are confirmed (row 59, OK). The old names "AI EMS" for 16 and "another AI variant" for 20 are replaced by time slot (16) and AI EMS (20), and the values 0, 2 and 11 exist as well.
- The old "3 guard checks" (row 60, prose count) correspond to one non-null test and two flag tests in `sendDeviceCommandOfMode` (`@0x249f624`, `@0x249f648`, `@0x249f654`) plus the guards of the cards.
- The old "debounce then sendDeviceCommand" is confirmed in structure, with the 10 s timer of step 5.

## Known unknowns

- Which firmware mode each number selects, and the response fields `electricity_strategy_mode` and `price_source_sub_type` the old page named (not read here; owner [device_command](../api/charging_hes_svc/device_command.md)).
- The truth table of the card guards and the meaning of the connection-data flags `field_2b` and `field_93`.
- The body of `handlerDeviceCommandOfMode` and the code pair `[0, 0]` of `setShiftMode` against the data-code map ([mqtt/a5101.md](../mqtt/a5101.md#data-code-maps-setdatacodemap-and-getdatacodemap)).
