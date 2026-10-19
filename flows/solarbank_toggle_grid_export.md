> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# Solarbank toggle grid export (switch_0w) and off-grid switch

How the app turns the grid feed-in ("0 W" switch) of a Solarbank 2 (A17C1 family) on or off, and how the separate off-grid output switch works. The grid feed-in switch sends a cloud request and the power-limit device command; the off-grid switch sends only its own device command. The payloads live with their owners: [set_device_attrs](../api/power_service/app/device/set_device_attrs.md), [get_device_attrs](../api/power_service/app/device/get_device_attrs.md), the device commands [mqtt/a17c1.md](../mqtt/a17c1.md#0080-setdevicepowerlimit) (opcode `0080`) and [mqtt/a17c1.md](../mqtt/a17c1.md#0073-setoffgridswitch) (opcode `0073`). "Audit row N" counts the data rows of [../docs/audit/FLOWS.md](../docs/audit/FLOWS.md), see the [README](README.md#audit-row-numbers).

## Trigger (UI action)

- Grid feed-in: on the A17C1 settings page the user taps the feed-in entry, the page calls `A17C1SettingLogic::showFeedGridSwitch` (call at `a17c1setting_page.dart @0x3d9023c`, function `a17c1setting_logic.dart @0x3d90258`), which opens a bottom picker with the entries `off` and `on` (`showBottomPicker`, `a17c1setting_logic.dart @0x3d90300`).
- Off-grid switch: the settings page calls `A17C1SettingLogic::setOffGridSwitch` (call at `a17c1setting_page.dart @0x3d97e00`, function `a17c1setting_logic.dart @0x3d97e28`); the home page has its own entry `A17C1homeLogic::setOffGridSwitch` (call at `a17c1home_page.dart @0x3d799b0`, function `a17c1home_logic.dart @0x3d799d8`).

## Preconditions

- Grid feed-in: the current state was read earlier with `get_device_attrs`; the power limit page reads 14 attributes in one batch (`getPowerLimitList`, `a17c1setting_logic.dart @0x26d2dbc`, array length raw 28 at `@0x26d2f4c`, call at `@0x26d3060`): `power_limit_option`, `user_power_limit`, `region_power_limit`, `legal_power_limit`, `ip_region`, `region_icroinverter_limit` (the app's spelling), `switch_0w`, `enable_0w`, `power_limit_option_real`, `pv_power_limit_option`, `pv_power_limit`, `unlock_default_power_type`, `unlock_pop_content`, `unlock_pop_image` (keys at `@0x26d2f58` to `@0x26d2ff4`). The owner page of the request does not list them yet. `enable_0w` says whether the device can do the 0 W mode, `switch_0w` is the current setting.
- Off-grid switch: `isSettingsEnable` must be true (`a17c1setting_logic.dart @0x3d97e40`) and the device must be connected (`isCurDeviceConnected`, `@0x3d97e5c`); otherwise `setOffGridSwitch` returns without a dialog.

## Steps

| # | actor | action | owner page link | asm citation |
|---|---|---|---|---|
| 1 | user | Picks `off` or `on` for the grid feed-in. | this page | `a17c1setting_logic.dart @0x3d90328` (picker callback) |
| 2 | app | Choosing `on` opens a confirm dialog with the text `turnOnGridContent` (`_showFeedGridDialog`); its OK callback calls `setFeedGridSwitch`. Choosing `off` calls `setFeedGridSwitch` directly: in the first branch (page flag `field_43` true and an inner state equal to 3) right after storing the text, otherwise after the generic text store. | this page | `a17c1setting_logic.dart @0x3d90520`, `@0x3d9053c` (dialog), `@0x3d90874` (OK callback), `@0x3d904b0`, `@0x3d905c8` (direct) |
| 3 | app | `setFeedGridSwitch(index)` reads the option element at the index, fires the UI message 2213 with the index and calls `setFeedGridValue`. | this page | `a17c1setting_logic.dart @0x3d908d4` (bounds test), `@0x3d90924` (id), `@0x3d9093c` (fire), `@0x3d90948` (call) |
| 4 | app | `setFeedGridValue` sends `set_device_attrs` with `device_sn` and `attributes` holding the single key `switch_0w` and the index, encrypted, with the loading overlay. | [set_device_attrs](../api/power_service/app/device/set_device_attrs.md) | `a17c1setting_logic.dart @0x3d90a14` (call); `http_request_repository_impl.dart @0x3d90b10` (key), `@0x3d90bbc` (URL), `@0x3d90be4` (call) |
| 5 | app | Without waiting for the cloud answer, `setFeedGridSwitch` calls `A17C1AnkerDevice::setDevicePowerLimit` with the named arguments `feeder0w` (a cached device value) and `switch0w` (the index). | [mqtt/a17c1.md](../mqtt/a17c1.md#0080-setdevicepowerlimit) | `a17c1setting_logic.dart @0x3d90968`, `@0x3d90978` (argument list), `@0x3d90980` (call) |
| 6 | app | The controller builds opcode `0080` and sends over one transport per call: `bleBusinessConnected` over BLE, `wifiConnected` wrapped for MQTT, any other status sends nothing. | [ble/protocol.md](../ble/protocol.md#stacks-and-send-routing) | `a17c1_device_controller.dart @0x2277590` (send), `@0x226e22c`, `@0x226e4e4` (gate) |
| 7 | user | Off-grid switch: taps the off-grid entry; the page opens the dialog `OffGridOutputSettingsDialog` as a bottom sheet. | this page | `a17c1setting_logic.dart @0x3d97e68`, `@0x3d97f20` |
| 8 | app | On confirm `_sendSetOffGridSwitch` calls `A17C1AnkerDevice::setOffGridSwitch` with the state as 0 or 1, then sets a page flag to false and, after 3 s, back (closure `@0x3d9847c`), and records the analytics event `APP_DEVICE_EMS_OFFP` with the value `open` or `close`. | this page | `a17c1setting_logic.dart @0x3d982d8` (call), `@0x3d98368` (`Future.delayed`), `@0x3d98438` (event name), `@0x3d98378` and `@0x3d98384` (`open`, `close`) |
| 9 | app | The controller builds opcode `0073` with tag `a2` (raw key 324) and the one-byte state and sends it through the same gate as step 6. | [mqtt/a17c1.md](../mqtt/a17c1.md#0073-setoffgridswitch) | `a17c1_device_controller.dart @0x3d79cd8` (key), `@0x3d79d44` (opcode) |

## Side effects

- Grid feed-in: the UI message 2213 (`a17c1setting_logic.dart @0x3d90924`, id as an unboxed value, data the chosen index) is fired before the cloud call.
- Off-grid: a 3 s lock on the control (step 8); analytics event `APP_DEVICE_EMS_OFFP`.
- The cloud value `switch_0w` and the device value can diverge if only one of the two sends succeeds; the app does not reconcile them in these functions.

## Timing (delays/polling)

3 s after the off-grid command: `Future.delayed` at `a17c1setting_logic.dart @0x3d98368` uses the pool `Duration` `pp+0x13660` with `off_8` 0x2dc6c0 = 3,000,000 microseconds (a pool object value, not a register immediate, so the Smi rule does not apply). The grid feed-in path has no delay of its own. No polling.

## Failure paths

- Off-grid, device not connected or settings disabled: no dialog (Preconditions).
- Grid feed-in cloud failure: `set_device_attrs` is sent with only the `showLoading` option (`http_request_repository_impl.dart @0x3d90bdc`); a failure callback was not seen, and the device command of step 5 is sent regardless.
- Device not reachable over BLE or WiFi: the opcode is dropped by the gate (`a17c1_device_controller.dart @0x226e238`). Error codes: `api/errors.md`.

## Since/changed

Corrections of the old FLOWS.md (audit rows in brackets), with the old value:

- The old page said the grid export toggle "goes through the API, not 0x0080". In 3.24.3 `setFeedGridSwitch` does both: `set_device_attrs` (step 4) and opcode `0080` with `switch0w` (step 5). The old `setGridConnectedInput` sends `ac_power_limit`, not `switch_0w` (see [solarbank_power_limit_change.md](solarbank_power_limit_change.md)).
- The power limit page reads 14 attributes in one batch; 3.18.0 read 11 (array length raw 22 in 3.18.0, raw 28 in 3.24.3; row 52, changed). The three new ones are `unlock_default_power_type`, `unlock_pop_content` and `unlock_pop_image`.
- Unchanged and confirmed: the off-grid switch is its own opcode `0073` with tag `a2` (row 51), not `0080`.

## Known unknowns

- The two page states that let `off` skip the confirm path (`field_43` and the inner value tested against the tagged 6 at `a17c1setting_logic.dart @0x3d903fc`).
- Whether the cloud `switch_0w` write is needed for the device to apply the setting, or only for the app and cloud state (server behaviour).
- What `feeder0w` holds in step 5 (a cached device value at offset 727, read at `a17c1setting_logic.dart @0x3d90968`).
- The `A17C1homeLogic::setOffGridSwitch` variant was not read beyond its call into the device method (`a17c1home_logic.dart @0x3d79b7c`).
