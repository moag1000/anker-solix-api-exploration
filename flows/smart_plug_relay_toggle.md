> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# Smart plug relay toggle (opcode 007a)

How the app switches the relay of a smart plug (A17X8) on or off from the home page, how it guards against stale status updates while commands are pending, and which transport carries the command. The command bytes are owned by [mqtt/a17x8.md](../mqtt/a17x8.md#007a-setrelayswitchcmd). "Audit row N" counts the data rows of [../docs/audit/FLOWS.md](../docs/audit/FLOWS.md), see the [README](README.md#audit-row-numbers).

## Trigger (UI action)

On the plug home page the user taps the main switch; the view calls `A17X8homeLogic::changeSwitch` (call at `a17x8home_view.dart @0x3dd6fc0`, function `a17x8home_logic.dart @0x3dd6fdc`).

## Preconditions

- `changeSwitch` returns without doing anything unless the first page flag (`field_83.field_1b`) is true (`tbz` at `a17x8home_logic.dart @0x3dd7014` jumps on true; the fall-through at `@0x3dd7018` returns).
- It then sends when the second page flag (`field_83.field_23`) is false (`tbnz` at `@0x3dd7044` jumps to the send on false). When that flag is true it sends only if the device field at offset 999 holds 1 or 3 (compares against the tagged values 2 and 6 at `@0x3dd7060` and `@0x3dd7068`); otherwise it returns. In the 3.24.3 build a Dart `false` has bit 4 set, so `tbnz w, #4` branches on false and `tbz w, #4` on true. The names of the flags and of the offset 999 field are not in the asm.
- There is no reachability test in `changeSwitch` itself; an unreachable plug is handled by the transport gate in step 5.

## Steps

| # | actor | action | owner page link | asm citation |
|---|---|---|---|---|
| 1 | user | Taps the main switch. | this page | `a17x8home_view.dart @0x3dd6fc0` |
| 2 | app | Checks the flags of Preconditions. | this page | `a17x8home_logic.dart @0x3dd7014`, `@0x3dd7044`, `@0x3dd7060`, `@0x3dd7068` |
| 3 | app | `onSwitchCommandSent` raises the counter of pending switch commands (device offset 1231) by one, sets the update-allowed flag (device offset 1211) to false and logs the count. | this page | `a17x8_anker_device.dart @0x3073984` (read), `@0x307399c` (add one), `@0x30739e4` (flag), `@0x30739f4` (log text); call at `a17x8home_logic.dart @0x3dd708c` |
| 4 | app | Calls `A17X8DeviceController::setRelaySwitchCmd` with the opposite of the current switch value (`eor x2, x0, #0x10` flips the boolean). The controller builds tag `a2` as one byte (0 off, 1 on) for opcode `007a`. | [mqtt/a17x8.md](../mqtt/a17x8.md#007a-setrelayswitchcmd) | `a17x8home_logic.dart @0x3dd7110`, call at `@0x3dd7118`; `a17x8_device_controller.dart @0x307390c` (key `a2`), opcode `@0x3073938` |
| 5 | app | The plug controller sends over exactly one transport per call: `bleBusinessConnected` over BLE, `wifiConnected` wrapped for MQTT, any other status sends nothing. | [ble/protocol.md](../ble/protocol.md#stacks-and-send-routing) | `a17x8_device_controller.dart @0x2419080` (BLE), `@0x24191bc` (WiFi) |
| 6 | app | Optimistic update: writes the new value into the device field at offset 1171 and into the page's switch value without waiting for the device. If the new value is off, calls `_clearFromGridCurve`, which cancels the energy graph timer and clears two lists (the `tbz` at `@0x3dd71a4` skips the call when the value is true). | this page | `a17x8home_logic.dart @0x3dd714c`, `@0x3dd7184`, `@0x3dd71a4`, call at `@0x3dd71ac`; `_clearFromGridCurve` `@0x2764224` to `@0x276424c` |
| 7 | device | Answers with the response opcode `setRelaySwitchRes`. | [mqtt/a17x8.md](../mqtt/a17x8.md#007a-setrelayswitchcmd) | `string-only` |
| 8 | app | `_handleResponse` of the plug controller matches `setRelaySwitchRes` (pool object `pp+0x10b70`), logs the success text and calls `onSwitchCommandConfirmed`, which lowers the pending counter by one, clamped to the range 0 to 999 (the raw argument 1998 is a tagged Smi), and sets the update-allowed flag back to true when the counter reaches 0. | this page | `a17x8_device_controller.dart @0x3b62b4c`, `@0x3b62b84`, `@0x3b62ba8`; `a17x8_anker_device.dart @0x3b64380`, `@0x3b643a0`, `@0x3b64424` |
| 9 | device | Reports the relay state in the periodic status `0405`. `parseDeviceAllInfo` applies the switch tag to the device only while the update-allowed flag is true, so a status that arrives while commands are pending does not overwrite the optimistic value. | [mqtt/a17x8.md](../mqtt/a17x8.md#0405-status-message-param_info) | `a17x8_device_commands.dart @0x3b655c8` (flag read) |

## Side effects

- The device object and the page show the new relay value immediately (step 6).
- Turning the relay off clears the energy graph data the page built from the grid power curve (`_clearFromGridCurve`).
- Pending-command bookkeeping lives on the device object (offsets 1231 and 1211) and is shared by every page that uses the same device.

## Timing (delays/polling)

No delay or debounce timer in `changeSwitch`, `onSwitchCommandSent` or the setter. The protection against rapid toggling is the pending counter of steps 3 and 8, not a timer. The counter is clamped to 999 at `a17x8_anker_device.dart @0x3b643a4` (a call argument, tagged, so real 999).

## Failure paths

- Plug not connected over BLE or WiFi: the command is dropped by the gate in step 5 (`a17x8_device_controller.dart @0x2419080`, `@0x24191bc`); the optimistic value of step 6 has already been written and the counter stays raised until a response arrives, so the update-allowed flag stays false. How the page recovers from this is not read.
- No response: the counter is not lowered; no timeout is visible in these functions. Error codes: `api/errors.md`.

## Since/changed

- Debounce: 3.18.0 delayed the follow-up with `Future.delayed` of 2 s (pool `Duration` with `off_8` 0x1e8480 = 2,000,000 microseconds, loaded at 0x2f10da8 in the 3.18.0 asm). 3.24.3 has no delayed future in `changeSwitch` and counts pending commands instead (audit rows 56, 70).
- Dual path: the old page said "BLE for direct, MQTT for cloud sync (both sent)". 3.24.3 sends one frame through one transport per tap (step 5); no second send exists in `changeSwitch` or `setRelaySwitchCmd`.
- Unchanged: opcode `007a` and tag `a2` with 0 and 1 (row 55). `_clearFromGridCurve` is still called, but on switching off, not on (the old page said on; the bit-test polarity above decides it).

## Known unknowns

- The names of the two flags and the offset 999 field in Preconditions.
- How the page recovers when a command is dropped at the gate (the counter and flag then stay unchanged).
- Whether the response handler also runs for MQTT answers; only the shared controller function was read.
