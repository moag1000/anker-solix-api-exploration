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
| 8 | device | Reports the switch states in its status push. The parser `parseSwitchData` reads the list positions 9, 10, 11, 12 and 13 (the raw immediates 18, 20, 22, 24 and 26 are tagged indexes); `parseSwitchData` stores position 9 as a bool at device offset 935 (`@0x45eb26c`), position 10 at 939, position 11 at 955, position 12 as an int below 4 at 959 and its value 4 as a bool at 411 (`@0x45eb408`, `@0x45eb448`) and position 13 at 947 (`@0x45eb4cc`). The AC state is position 9: the page's optimistic write in step 3 stores the new state in the same device offset 935 (`a1770home_logic.dart @0x3c7982c`), so offset 935 is the AC switch of this page; the DC and smart-mode assignments of the audit (positions 10 and 12) were not checked against a consumer. | [ble/a1770.md](../ble/a1770.md) | `a1770_commands.dart @0x45eb1f8`, `@0x45eb27c`, `@0x45eb300`, `@0x45eb384`, `@0x45eb454` |

The static command `A1770Commands.setAcSwitch` is a seven-element byte list; its bytes and Smi widths are owned by [ble/a1770.md](../ble/a1770.md#setacswitch-static-command-list).

## Side effects

- The displayed AC state changes immediately (step 3), before the device answers.
- `_clearAcCountdown` clears the AC countdown shown on the page and `_setAcPowerCurve` restarts the power curve (bodies not read).
- Analytics event `DEVICE_AC_OUTPUT_CLICK`.
- Frame of step 6 (app side, from the asm): `formatCommand` of the PDP transformer (`pdp_command_transformer.dart @0x240ff84`) only stores the command list and the one-byte value in the transformer; `generateCommand` (`@0x240fc6c`) calls `CmdUtil::getTotalCmd` (`cmd_util.dart @0x240fcac`), which allocates a byte array of `len(command) + len(value) + 3` bytes (`@0x240fcd4` to `@0x240fd04`), copies the command at index 0, writes the total length as two bytes with `intToList2` (low byte first) at index `len(command)` (`@0x240fdd0` to `@0x240fe6c`), copies the value after them (`@0x240fe98`) and stores a checksum in the last byte: the sum of all bytes, masked with 0xff (`_getCheckSum`, `@0x240ff0c`, store at `@0x240fed4`). For `setAcSwitch` this is the seven command bytes 08 ee 00 00 00 02 86 (owner [ble/a1770.md](../ble/a1770.md#setacswitch-static-command-list)), the length 0b 00 (11), the state byte 01 or 00 and the checksum byte 8a (state 1) or 89 (state 0): 11 bytes. The receiving side checks the same layout in `validateCommand` (`@0x4788a6c`: length from bytes 7 to 8, checksum over all bytes but the last). Fact belongs on ble/a1770.md (`setAcSwitch` frame; its Known unknowns on the state byte position).

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

- Whether the AC switch of the A1771 and A172x controllers (list `[0, 0x4a]`) is the PPS family the old page meant for other products — traced 2026-10-20: not traced; the question is a product-naming one and needs the old page's product list, which is not in the asm.
