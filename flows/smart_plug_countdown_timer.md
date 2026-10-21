> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# Smart plug countdown timer (opcode 007e)

How the app starts, pauses, resumes and deletes the countdown timer of a smart plug (A17X8) and how the timer state comes back. The command bytes are owned by [mqtt/a17x8.md](../mqtt/a17x8.md#007e-setcountdowncmd), the timer status block by [mqtt/a17x8.md](../mqtt/a17x8.md#countdowninfo-tag-ad-of-0405-and-message-087f); this page holds the sequence and the gates. "Audit row N" counts the data rows of [../docs/audit/FLOWS.md](../docs/audit/FLOWS.md), see the [README](README.md#audit-row-numbers).

## Trigger (UI action)

On the countdown page (`a17x8countdown_view.dart`) the user taps the start, pause or resume control (labels `pause` at `@0x3dd0198` and `resume` at `@0x3dd0184`; callback closure `@0x3dd0350`, call at `@0x3dd0384`) which calls `A17x8CountdownLogic::changeStartOrPause` (`a17x8countdown_logic.dart @0x3dd03a0`). The delete control (label `delete` at `a17x8countdown_view.dart @0x3dcf7bc`, closure `@0x3dcf944`, call at `@0x3dcf978`) calls `deleteCountdown` (`a17x8countdown_logic.dart @0x3dcf994`).

## Preconditions

- The page considers the plug reachable (`_isCurDeviceConnected`, `a17x8countdown_logic.dart @0x275e4dc`, called at `@0x3dd03c4` and `@0x3dcf9b8`). If the page flag `field_8b` is true (BLE mode of the page) the test is: the BLE business connection state is `connectDone` (`@0x275e528`) and the connected MAC equals the plug's MAC (`getUnifiedMac` at `@0x275e550`). Otherwise the test is on the device status: `wifiConnected` gives true (`@0x275e5e8`); `wifiDisconnected` (`@0x275e618`), `appUnable` (`@0x275e638`) and `bleDisconnected` (`@0x275e658`) give false; every other status gives true (`@0x275e678`).
- When the test fails the page shows a toast and sends nothing: `deviceOfflineAndBluetoothDisconnected` in BLE mode (`@0x3dd0558`), else `deviceIsOffline` (`@0x3dd056c`), shown at `@0x3dd0580` (same texts in `deleteCountdown`, `@0x3dcfa24` and `@0x3dcfa38`).
- Initial values (`A17x8CountdownLogic::onInit`, `a17x8countdown_logic.dart @0x3461800` to `@0x346196c`): the page loads the cached `CountDownInfo` of the device (device offset 1167). The remaining-seconds value of the page is `info[0]` (`ArrayLoad ... List_8`, `@0x3461838`), 0 when no info is cached (`r4 = 0`, unboxed, `@0x3461858`). The page `type` (64-bit, unboxed) is `info.field_1f`, default 1 (`@0x34618d8`). The state value is `info.field_f`, default 2 (pause, `r2 = 2` at `@0x3461930`, unboxed, then boxed into the Rx). If the state then compares as running (`cmp w0, #6` at `@0x3461970`, running is 3) `onInit` starts the tick (`@0x346197c`). So the page starts in the pause state (2) when the device reports no timer, and the state is first set from the cached info; the cache is filled by the status parser of step 10.

## Steps

| # | actor | action | owner page link | asm citation |
|---|---|---|---|---|
| 1 | user | Taps start, pause/resume or delete. | this page | `a17x8countdown_view.dart @0x3dd0384`, `@0x3dcf978` |
| 2 | app | Runs `_isCurDeviceConnected` (Preconditions). | this page | `a17x8countdown_logic.dart @0x3dd03c4`, `@0x3dcf9b8` |
| 3 | app | Picks the new state from the current one: if the current state compares as running (`cmp w0, #6` on the tagged Rx value, so running is 3) the new state is 2 (pause), otherwise 3 (start or resume). Delete sets the state to 0 with a zero-register store. | this page | `a17x8countdown_logic.dart @0x3dd03e4`, `@0x3dd03ec`, `@0x3dd03f4`; delete `@0x3dcf9c4` |
| 4 | app | Stores the new state in the page's state value, in the cached `CountDownInfo` of the device (`field_f`; the info object sits at device offset 1167) and in the page's `type` field (64-bit, unboxed); a second value goes to `CountDownInfo.field_17`. Then it calls `_setCountdownCmd`. | this page | `a17x8countdown_logic.dart @0x3dd0404`, `@0x3dd0444`, `@0x3dd0488`, `@0x3dd04a8`, call at `@0x3dd04b0` |
| 5 | app | `_setCountdownCmd` passes the state and the times to `A17X8DeviceController::setCountdownCmd`, which builds the tags `a2` (type), `a3` (total time, 3 bytes), `a4` (switch state), `a5` (remaining time, 3 bytes) for opcode `007e`. | [mqtt/a17x8.md](../mqtt/a17x8.md#007e-setcountdowncmd) | `a17x8countdown_logic.dart @0x3dcfb7c`; `a17x8_device_controller.dart @0x3dcfde4`, `@0x3dcfe20`, `@0x3dcfe54`, `@0x3dcfe90`, opcode `@0x3dcfee0` |
| 6 | app | `sendCommandWithParam` of the plug controller chooses the transport per call: status `bleBusinessConnected` sends over BLE, status `wifiConnected` wraps the frame for MQTT, any other status sends nothing. | [ble/protocol.md](../ble/protocol.md#stacks-and-send-routing) | `a17x8_device_controller.dart @0x2419080` (BLE), `@0x24191bc` (WiFi) |
| 7 | app | Running state (compare `cmp w0, #6`, running is 3): starts the local one-second tick (`startCountdown`); otherwise cancels the tick. Then fires the UI message 1351 on the event bus. | this page | `a17x8countdown_logic.dart @0x3dd04bc`, `@0x3dd04c8`, `@0x3dd04e4`, `@0x3dd0524` |
| 8 | device | Answers with the response opcode `setCountdownRes`. | [mqtt/a17x8.md](../mqtt/a17x8.md#007e-setcountdowncmd) | `a17x8countdown_logic.dart @0x275e3d8` |
| 9 | app | `_dealWithResponse` accepts `setCountdownRes` (pool object `pp+0x10bd0`) when the page's `type` is 0: dismisses the loading overlay, replaces the cached timer info with a new zeroed `CountDownInfo`, fires message 1350 and closes the page. For other types nothing is done here. | this page | `a17x8countdown_logic.dart @0x275e3d8` (opcode compare), `@0x275e3ec` (type test), `@0x275e428` and `@0x275e440` (new info object, cache write), `@0x275e490` (message), `@0x275e4b4` (back) |
| 10 | device | Reports the timer in the periodic status `0405` (tag `ad`). The app parses it in `parseCountDownInfo`, stores it at device offset 1167 and fires message 1356. | [mqtt/a17x8.md](../mqtt/a17x8.md#countdowninfo-tag-ad-of-0405-and-message-087f) | `a17x8_device_commands.dart @0x3b6343c` (parser), `@0x3b63640` (store), `@0x3b63690` (message) |

State values on the wire (type byte `a2`): start and resume 3, pause 2, delete 0. There is no separate delete opcode. Delete is a start-style command with type 0, so the same `007e` frame is used (audit rows 17, 18, 20, 21).

## Side effects

- The cached timer info (`CountDownInfo`) is overwritten at step 4 before the device confirms and zeroed on a delete response (step 9).
- Event bus messages 1351 (after a send), 1350 (delete confirmed) and 1356 (status parsed) are fired for the UI (`a17x8countdown_logic.dart @0x3dd0524`, `@0x275e490`; `a17x8_device_commands.dart @0x3b63690`).
- The plug's relay is not touched by this flow; the relay toggle is [smart_plug_relay_toggle.md](smart_plug_relay_toggle.md).
- The tick closure (`a17x8countdown_logic.dart @0x3461a60` to `@0x3461b94`) reads the remaining seconds Rx; at 0 it cancels the timer (`@0x3461aa4`) and closes the page with `GetNavigation.back()` (`@0x3461ad0`); otherwise it decrements the value by 1 (unboxed `sub x2, x1, #1`, `@0x3461b10`), stores it back into the Rx (`@0x3461b30`) and writes it into element 0 of the cached `CountDownInfo` at device offset 1167 (`ArrayStore r2[0]`, `@0x3461b80`). It sends nothing.
- Two more messages are handled by `onMessageDispatch` besides the response ids (`a17x8countdown_logic.dart @0x275dee4`; the message id is read with a 64-bit load and compared raw): id 558 (`cmp x0, #0x22e`, `@0x275df0c`) carries a bool; when it is false the page calls `BleManager::disconnect` and clears its page flag `field_6b` (`@0x275df68`, `@0x275df78`). Id 575 (`cmp x0, #0x23f`, `@0x275df7c`) is ignored while the page is in BLE mode (`field_8b` true, `@0x275df90`); otherwise it carries a map with the keys `deviceSn`, `devicePn` and `connected` (strings at `@0x275e028`, `@0x275e060`, `@0x275e094`), and when the serial matches the page's device, the product is `A17X8` and `connected` is false (`@0x275e174`, `@0x275e184`) and a dialog is open, it dismisses the dialog and shows the toast `deviceIsOffline` (`@0x275e1bc`, `@0x275e1f0`). Ids 563 and 564 (`cmp x0, #0x233`, `#0x234`) go to `_dealWithResponse`. The names of the ids are not in the pool.

## Timing (delays/polling)

The page runs a periodic tick of 1 s while the timer is running: `Timer.periodic` with the pool `Duration` `pp+0x1458` whose `off_8` is 0xf4240 = 1,000,000 microseconds (`a17x8countdown_logic.dart @0x3461a20`, tick closure `@0x3461a60`; a pool object value, not a register immediate). `startCountdown` first cancels a running tick (`@0x34619dc`) and starts a new one only when the remaining time read from the cache is above 0 (`cmp x1, #0` at `@0x34619fc`). No delay on the command itself.

## Failure paths

- Device not reachable: toast, nothing sent (Preconditions).
- No answer: not handled in this logic class; the loading overlay of delete is dismissed only by the response of step 9.
- Error codes: [errors](../api/errors.md).

## Since/changed

Corrections of the old FLOWS.md (audit rows in brackets), with the old value:

- Running is state 3 (the old page said 6), pause is 2 (old 4), start and resume send 3 (old 6) (rows 17, 18, 21, 68). The old "idle (0)" could not be verified (row 19).
- The TLV key column `0x0144` to `0x014A` was the tagged Smi; the tag bytes are `a2` to `a5` (row 22).
- The status block of `0405`: total time is bytes 0 to 2 (old 0 to 5), the switch state is byte 3 (old 6), byte 4 is stored in `field_f` (old "byte 8, elapsed marker"), the elapsed time is bytes 5 to the end (rows 28, 29, 30); the owner page carries the decoded layout.
- `CountDownInfo` is stored at device offset 1167 (0x48F) in 3.24.3; 3.18.0 stored it at 1143 (0x477) (row 31, changed).
- Unchanged: opcode `007e` (row 23), field lengths 1, 3, 1, 3 bytes (row 24), status tag `ad` (row 26), minimum 8 bytes (row 27), message 1356 (row 32). Row 25 is a worked example, not from asm.

## Known unknowns

- Whether the relay switch state of the plug changes when a timer ends (device behaviour).
