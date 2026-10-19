> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# Smart plug schedule (opcode 007c)

How the app creates, edits and deletes a schedule slot of a smart plug (A17X8) from the timing settings page, and how the slot list is updated from the answer. The command tags are owned by [mqtt/a17x8.md](../mqtt/a17x8.md#007c-settimingcmd), the readback by [mqtt/a17x8.md](../mqtt/a17x8.md#007d-gettimingcmd-and-timinginfo); this page holds the sequence and the gates. "Audit row N" counts the data rows of [../docs/audit/FLOWS.md](../docs/audit/FLOWS.md), see the [README](README.md#audit-row-numbers).

## Trigger (UI action)

On the timing settings page (`a17x8timing_setting_view.dart`) the user sets the time (`saveTime`, call at `@0x3de3c88`), the repeat days (`saveTimedTaskOpenCycle`, call at `@0x3de50fc`) and the on/off choice (`setSwitchStatus`, `a17x8timing_setting_logic.dart @0x3de558c`) and taps save: the view calls `A17x8timingSettingLogic::saveData` (call at `a17x8timing_setting_view.dart @0x3de5780`, function `a17x8timing_setting_logic.dart @0x3de579c`). The delete control (label `delete` at `a17x8timing_setting_view.dart @0x3de3e40`) calls `deleteTiming` (call at `@0x3de3f4c`, function `a17x8timing_setting_logic.dart @0x3de3f68`).

## Preconditions

- The plug is considered reachable by `_isCurDeviceConnected` of the timing page (called at `a17x8timing_setting_logic.dart @0x3de580c` and `@0x3de3f8c`); when it fails the page shows `deviceOfflineAndBluetoothDisconnected` or `deviceIsOffline` (`@0x3de58e0`, `@0x3de58f4`, shown at `@0x3de5908`). The gate has the same shape as the one on [smart_plug_countdown_timer.md](smart_plug_countdown_timer.md#preconditions).
- Save only: the page state read at `@0x3de57f8` must allow saving; `saveData` returns when it is false (`tbnz` at `@0x3de5804`).
- Save only: no other slot may have the same time on the same day. `_checkSameTime` (`@0x3de5818`, function `@0x3de598c`) compares the new time with the list of slots; on a clash the page shows the dialog `a17x8SetSameTimeTips` (`@0x3de5840`, `showDialog` at `@0x3de5890`) and sends nothing.
- Slot limit: the home page reads the device attribute `timing_limit` and falls back to 24 when it is absent (`a17x8home_logic.dart @0x3463844` for the key, default at `@0x3463920`, an unboxed register, so 24; audit row 36).

## Steps

| # | actor | action | owner page link | asm citation |
|---|---|---|---|---|
| 1 | user | Sets time, repeat days and switch; taps save or delete. | this page | `a17x8timing_setting_view.dart @0x3de3c88`, `@0x3de50fc`, `@0x3de5780`, `@0x3de3f4c` |
| 2 | app | `saveData` stores the action type in the page field `field_bb`: the add case adds 2 to a zero or one flag after a compare, so the tagged value is 2 for create and 4 for modify, and `LoadInt32Instr` untags it to 1 (create) and 2 (modify). `deleteTiming` stores the zero register, so delete is 0. | this page | `a17x8timing_setting_logic.dart @0x3de57e0`, `@0x3de57f4`; delete `@0x3de3f98` |
| 3 | app | Checks reachability and the same-time rule (Preconditions), then calls `_setTimingCmd` with the slot and the action type, and records an analytics click. | this page | `a17x8timing_setting_logic.dart @0x3de5818`, `@0x3de58bc`, `@0x3de58c4` |
| 4 | app | `_setTimingCmd` shows the loading overlay and calls `A17X8DeviceController::setTimingCmd`. | this page | `a17x8timing_setting_logic.dart @0x3de4064`, call at `@0x3de40d8` |
| 5 | app | `setTimingCmd` builds the tags `a2` (action), `a3` (slot id), `a4` (enabled), `a5` (time, 2 bytes), `a6` (switch), `a7` (weekday list) for opcode `007c`. Weekdays are sequential day numbers, not a bit mask, and `a4` is 1 for an enabled slot (device test, not inverted). | [mqtt/a17x8.md](../mqtt/a17x8.md#007c-settimingcmd) | `a17x8_device_controller.dart @0x3de1b54`, `@0x3de1c0c`, `@0x3de1d34`, `@0x3de1d58`, `@0x3de1dd0`, `@0x3de1e8c`, opcode `@0x3de1eb8` |
| 6 | app | The plug controller sends over one transport per call: `bleBusinessConnected` over BLE, `wifiConnected` over MQTT, otherwise nothing. | [ble/protocol.md](../ble/protocol.md#stacks-and-send-routing) | `a17x8_device_controller.dart @0x2419080` (BLE), `@0x24191bc` (WiFi) |
| 7 | device | Answers with the response opcode `setTimingRes`. | [mqtt/a17x8.md](../mqtt/a17x8.md#007c-settimingcmd) | `string-only` |
| 8 | app | `_dealWithResponse` accepts `setTimingRes` (pool object `pp+0x10b90`), dismisses the loading overlay and branches on the stored action type: delete (0) removes the slot from the page list, fires message 1352 and closes the page; create (1) appends the slot, sorts the list and fires message 1354 with `isEdit` and `data`; modify (2) fires message 1354 as well. | this page | `a17x8timing_setting_logic.dart @0x2767d60` (opcode compare), `@0x2767da0` (branch), `@0x2767df8` (`removeWhere`), `@0x2767e2c` (1352), `@0x2767f40` (`sortTimingList`), `@0x276801c` and `@0x2768288` (1354) |
| 9 | device | Reports the stored slots and the relay state when the app queries them (`007d`, `TimingInfo`). The timing readback also updates the relay switch state: the parser logs "get timing, update relay switch state". | [mqtt/a17x8.md](../mqtt/a17x8.md#007d-gettimingcmd-and-timinginfo) | `a17x8_device_commands.dart @0x3b636c4` (`parseTimingInfo`), `@0x3b64094` (log text) |

## Side effects

- The slot list of the page is changed only after the device answers (step 8), not at the tap.
- The relay switch state in the page is refreshed by the timing readback (step 9); schedule and relay state travel together in that answer. Which of the two the parser writes first is not read.
- Event bus messages 1352 (delete) and 1354 (create or modify) are fired for the list page.

## Timing (delays/polling)

No delay, timer or retry in `saveData`, `deleteTiming` or `_setTimingCmd`. The loading overlay stays until the response of step 8 dismisses it.

## Failure paths

- Plug not reachable or same time clash: toast or dialog, nothing sent.
- Error or non-zero result codes in the response: `_dealWithResponse` shows no error text in the branches read here (no `Trans.tr` call between `a17x8timing_setting_logic.dart @0x2767d60` and `@0x2768378`); whether the response code is tested at all was not decoded.
- No answer: the overlay is not dismissed by this logic; no timeout is set here. Error codes: `api/errors.md`.

## Since/changed

Corrections of the old FLOWS.md (audit rows in brackets), with the old value:

- The TLV key column `0x0144` to `0x014E` was the tagged Smi; the tag bytes are `a2` to `a7` (row 34).
- The inversion of `isEffective` stays refuted: `a4` is 1 for an enabled slot (device test of the old page; the inversion was UI-layer logic).
- Unchanged and confirmed: action values 0, 1, 2 (row 33), opcode `007c` (row 35), default limit 24 (row 36), summary line (row 69). Rows 37 and 38 (hour and minute ranges, weekday numbering 1 to 7, the device-tested table) are not asm facts and stay with the device-tested notes on the owner page.

## Known unknowns

- Upstream documents the slot index as 1 to 10 (owner page); the app's default limit is 24. Which one the firmware enforces is open.
- Whether the weekday list is omitted from the frame when it is empty (the old page said so; not re-read).
- The meaning of the page-state flag tested at `a17x8timing_setting_logic.dart @0x3de5804`.
- The create and modify branches of the response handler (`a17x8timing_setting_logic.dart @0x2767e60` to `@0x2768378`) beyond the message ids.
