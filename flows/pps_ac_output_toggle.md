> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# PPS AC output toggle (A1770)

How the app switches the AC output of a Bluetooth-only portable power station of the A1770 family (F1200) on or off. The command is a fixed legacy byte list that carries the state, not a TLV opcode, and the A1770 controller has no WiFi or MQTT path. The device class and its command list are owned by [ble/a1770.md](../ble/a1770.md); the opcode `004a` named by the old page does not belong to this product. "Audit row N" counts the data rows of [../docs/audit/FLOWS.md](../docs/audit/FLOWS.md), see the [README](README.md#audit-row-numbers).

## Trigger (UI action)

On the A1770 home page the user taps the AC output switch: the view calls `A1770homeLogic::setAcSwitch` (call at `a1770home_view.dart @0x3c79788`, function `a1770home_logic.dart @0x3c797a4`).

## Preconditions

- The page considers the device reachable: `isCurDeviceConnected` (`a1770home_logic.dart @0x3c797c8`); when it is false the function skips everything (`tbnz` at `@0x3c797cc`).
- No battery-level guard exists in this function: there is no compare of a charge value between `@0x3c797ac` and `@0x3c798f4` (the old page's "no explicit battery-low guard", confirmed by re-reading).

## Steps

| # | actor | action | owner page link | asm citation |
|---|---|---|---|---|
| 1 | user | Taps the AC switch. | this page | `a1770home_view.dart @0x3c79788` |
| 2 | app | Checks `isCurDeviceConnected`. | this page | `a1770home_logic.dart @0x3c797c8` |
| 3 | app | Flips the displayed AC state (`eor x2, x0, #0x10` on a page value), stores a device flag and reads the new state. | this page | `a1770home_logic.dart @0x3c797ec`, `@0x3c797f4`, `@0x3c7982c` |
| 4 | app | Calls `A1770AnkerDevice::setAcSwitch` with the new state as 0 or 1. | [ble/a1770.md](../ble/a1770.md) | `a1770home_logic.dart @0x3c79860` |
| 5 | app | `A1770DeviceController::setAcSwitch` turns the state into a one-byte list (`intToList`), loads the static command `A1770Commands.setAcSwitch` (static field offset 0x2130) and calls `_sendCommandWithParams` with the named argument `value`. | [ble/a1770.md](../ble/a1770.md) | `a1770_device_controller.dart @0x3c799e8`, `@0x3c799f0`, `@0x3c79a28` |
| 6 | app | `_sendCommandWithParams` formats the command with the controller's transformer and sends it with `sendCommand` (default wait 5 s); there is no connection-status test in this function. | [ble/protocol.md](../ble/protocol.md#timeouts-and-limits) | `a1770_device_controller.dart @0x33ead4c`, `@0x33ead5c`, `@0x33ead7c` |
| 7 | app | Records the analytics click `DEVICE_AC_OUTPUT_CLICK` with the value `"1"` or `"0"`, then calls `_clearAcCountdown` and `_setAcPowerCurve`. | this page | `a1770home_logic.dart @0x3c798c8`, `@0x3c798e4`, `@0x3c798ec`, `@0x3c798f4` |
| 8 | device | Reports the switch states in its status push. The parser `parseSwitchData` reads the list positions 9, 10, 11, 12 and 13 (the raw immediates 18, 20, 22, 24 and 26 are tagged indexes); the audit assigns the AC state to position 9, the DC state to 10 and the smart mode to 12. | [ble/a1770.md](../ble/a1770.md) | `a1770_commands.dart @0x45eb1f8`, `@0x45eb27c`, `@0x45eb300`, `@0x45eb384`, `@0x45eb460` |

The static command `A1770Commands.setAcSwitch` (function `a1770_commands.dart @0x3c79a44`) is a seven-element byte list. Its elements are the Smi immediates 16, 476, 0, 0, 0, 4 and 268 stored with `stur w` (`@0x3c79a68`, `@0x3c79a70`, `@0x3c79a74`, `@0x3c79a78`, `@0x3c79a7c`, `@0x3c79a84`, `@0x3c79a8c`), so the bytes are 8, 238, 0, 0, 0, 2 and 134 (0x08, 0xee, 0x00, 0x00, 0x00, 0x02, 0x86); how `formatCommand` inserts the state byte is not read. This command layout has no place on [ble/a1770.md](../ble/a1770.md) yet (that page says the tags of this product were not decoded), so it is recorded here until it moves.

## Side effects

- The displayed AC state changes immediately (step 3), before the device answers.
- `_clearAcCountdown` clears the AC countdown shown on the page and `_setAcPowerCurve` restarts the power curve (bodies not read).
- Analytics event `DEVICE_AC_OUTPUT_CLICK`.

## Timing (delays/polling)

The command wait is the controller default of 5 s ([ble/protocol.md](../ble/protocol.md#timeouts-and-limits)). No debounce or delay in the page function.

## Failure paths

- Device not reachable: nothing is sent (Preconditions).
- No answer within the wait: the controller's timeout path is not part of this flow; the page has already flipped its displayed state. Error codes: [errors](../api/errors.md).

## Since/changed

Corrections of the old FLOWS.md (audit rows in brackets), with the old value:

- The old title "004a / varies" and the claim that the command comes from the `[0, 0x4a]` list were not confirmed: that list is used by the A1771 and A172x controllers, not by the A1770 files, and the A1770 switch is the static list above (row 57).
- The `parseSwitchData` positions are 9, 10 and 12 (a further read at 11 and one at 13 sit in the same function), not 18, 20 and 24 (row 58).
- The old claim "A1790 has dual routing by an `isA17B2` flag": the string `isA17B2` is absent from both the 3.24.3 and the 3.18.0 pool and asm, and the A1790 files have no AC switch method (no `setAcSwitch`). The claim has no support in either version.
- Unchanged: no battery-low guard (confirmed, Preconditions).

## Known unknowns

- The meaning of the seven command bytes and how the state byte is merged (`formatCommand`, `a1770_device_controller.dart @0x33ead4c`).
- Which of the positions 9 to 13 of `parseSwitchData` is the AC state in the model (the audit row and the old page differ; the model field names were not read).
- Whether the AC switch of the A1771 and A172x controllers (list `[0, 0x4a]`) is the PPS family the old page meant for other products.
