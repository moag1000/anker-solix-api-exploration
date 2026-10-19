> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# Solarbank temperature unit (opcode 0050)

How the app switches the temperature unit shown by a Solarbank 2 (A17C1 family) between Celsius and Fahrenheit. The flow sends one device command and no cloud request. The command bytes are owned by [mqtt/a17c1.md](../mqtt/a17c1.md#0050-settempunit). "Audit row N" counts the data rows of [../docs/audit/FLOWS.md](../docs/audit/FLOWS.md), see the [README](README.md#audit-row-numbers).

## Trigger (UI action)

On the A17C1 settings page the user taps the temperature unit entry: `A17C1SettingLogic::showTempPicker` (`a17c1setting_logic.dart @0x3d98b0c` first instruction, called from the page) opens a bottom picker (`showBottomPicker`, argument list with `initData` at `@0x3d98c78`). Choosing an entry calls the picker callback, which calls `A17C1SettingLogic::setTempUnit` with the picker index (`a17c1setting_logic.dart @0x3d98cf4`, closure `@0x3d98cbc`, function `@0x3d98e54`).

## Preconditions

- No connection test in `showTempPicker` or `setTempUnit`; an unreachable device is handled only by the transport gate of step 4.
- The index 0 or 1 selects the unit; the mapping 0 Celsius and 1 Fahrenheit is the upstream constant (`CMD_TEMP_UNIT`), not an asm value. Tag: upstream-confirmed for the mapping.

## Steps

| # | actor | action | owner page link | asm citation |
|---|---|---|---|---|
| 1 | user | Taps the temperature unit entry; the page records the analytics click `DEVICE_TEMPERATURE_UNIT_CLICK` and shows the picker. | this page | `a17c1setting_logic.dart @0x3d98be8` (event name), `@0x3d98c04` (call), `@0x3d98c78` (picker) |
| 2 | user | Picks Celsius or Fahrenheit. | this page | `a17c1setting_logic.dart @0x3d98ce8` (index read) |
| 3 | app | `setTempUnit` calls `A17C1AnkerDevice::setTempUnit` with the index; the controller builds the payload as the one-byte list of the index (`intToList`) for opcode `0050`. | [mqtt/a17c1.md](../mqtt/a17c1.md#0050-settempunit) | `a17c1setting_logic.dart @0x3d98e98`; `a17c1_device_controller.dart @0x3d98ff0` (`intToList`), `@0x3d98ffc` (opcode), `@0x3d99008` (send) |
| 4 | app | The controller sends over one transport per call: `bleBusinessConnected` over BLE, `wifiConnected` wrapped for MQTT, any other status sends nothing. | [ble/protocol.md](../ble/protocol.md#stacks-and-send-routing) | `a17c1_device_controller.dart @0x226e22c`, `@0x226e4e4` |
| 5 | app | Right after the call the page sets a page flag (`field_7f` slot at offset 307) to false, and 3 s later a closure sets it back to true. | this page | `a17c1setting_logic.dart @0x3d98ea8`, `@0x3d98ebc` (false), `@0x3d98ed0` (`Future.delayed`), `@0x3d99054`, `@0x3d99068` (true) |
| 6 | device | Applies the unit and reports it in its next status message; the old page named tag `a9` of `0405` for this. | [mqtt/a17c1_status.md](../mqtt/a17c1_status.md) untagged by design (no app-side fact) |

## Side effects

- The page flag of step 5 is a 3 s lock on the control (what exactly it disables in the UI is not read).
- No cloud request is sent and no local copy of the unit is written by `setTempUnit` itself; the old page's "optimistic UI update" is not visible in this function.

## Timing (delays/polling)

3 s: `Future.delayed` at `a17c1setting_logic.dart @0x3d98ed0` uses the pool `Duration` `pp+0x13660` with `off_8` 0x2dc6c0 = 3,000,000 microseconds (a pool object value, not a register immediate, so the Smi rule does not apply). It is the same object as in the other A17C1 setting flows ([solarbank_power_limit_change.md](solarbank_power_limit_change.md), [solarbank_toggle_grid_export.md](solarbank_toggle_grid_export.md)). No polling.

## Failure paths

- Device not reachable over BLE or WiFi: the command is dropped by the gate (`a17c1_device_controller.dart @0x226e238`); the page does not show an error in `setTempUnit`. Error codes: [errors](../api/errors.md).
- No answer handling: `setTempUnit` does not await the send (`a17c1setting_logic.dart @0x3d98e98` is followed directly by the flag write).

## Since/changed

- The old page said "BLE only". The command goes through the shared gate, so it can also leave over MQTT when the device is on WiFi (no cloud HTTP request in either case). BLE is not a fallback while the device is on WiFi, see [ble/protocol.md](../ble/protocol.md#connection-routing-and-the-wifi-exclusion-rule).
- Unchanged: opcode `0050` (row 53). Row 54 (tag `a9` of the status) stays unverified.

## Known unknowns

- Which status field carries the unit (audit row 54): tag `a9` exists in the A17C1 status parser but its meaning is unconfirmed; owner [mqtt/a17c1_status.md](../mqtt/a17c1_status.md).
- Where the picker keeps the selected index shown on the page (the optimistic update of the old page).
- What the page flag at offset 307 disables.
