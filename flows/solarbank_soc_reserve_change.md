> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# Solarbank SOC reserve change

How the app changes the battery reserve of a Solarbank 2 (A17C1 family) from the device settings: the cloud call `set_power_cutoff` first, and only after its success the device command (opcode `0067`). 3.24.3 has two routes: the legacy wheel picker and a new SoC settings page (new in 3.24.3) that sends a larger body. The payloads live with their owners: [set_power_cutoff](../api/power_service/app/compatible/set_power_cutoff.md), [get_power_cutoff](../api/power_service/app/compatible/get_power_cutoff.md), the model [soc_setting_param](../models/soc_setting_param.md) and the device command [mqtt/a17c1.md](../mqtt/a17c1.md#0067-setsoc). Source conflict, two-sided: the earlier mapping on [mqtt/a17c1.md](../mqtt/a17c1.md#0067-setsoc) lists `set_site_device_param` param type 18 as the related API of opcode `0067`; the 3.24.3 trace here shows `set_power_cutoff` in front of `setSoc` on both routes and no param type 18 call. The API mapping has no device test (the 0067 opcode itself is device-tested on mqtt/a17c1.md, FW 1.0.6.10 via mqtt_monitor); this page follows the asm trace and leaves the older mapping marked unconfirmed there. "Audit row N" counts the data rows of [../docs/audit/FLOWS.md](../docs/audit/FLOWS.md), see the [README](README.md#audit-row-numbers).

## Trigger (UI action)

On the A17C1 settings page the user taps the safety SoC entry: `A17C1SettingLogic::onTapSafetySoC` (`a17c1setting_logic.dart @0x3d946ac`, call at `@0x3d94694`). The route is chosen by a bool of the device model at offset 1307 (`@0x3d946f0`, `tbnz` at `@0x3d946fc`; the field name is not in the asm). A Dart `false` has bit 4 set in this build, so `tbnz w, #4` branches on false.

- Flag true: new route, `SocManager.gotoSocSetting` with the named arguments `isSupportBackupReserve`, `isSupportChargeLimit`, `defaultBackupReserveValue`, `enforceStrictBackupReserveRange`, `isShowTips` (argument list `@0x3d94830`, call `@0x3d94838`) and a result callback (closure `@0x3d955f4`, referenced at `@0x3d947ec`).
- Flag false: legacy route. If `isAcChargingOrGridOutputConditionMet` (`@0x3d94848`) is true the page shows `showDeviceInSiteTips` (`@0x3d94854`) and stops; otherwise it opens the picker `showSocPicker` (`@0x3d9489c`, function `@0x3d948d4`).

## Preconditions

- Legacy route: the reserve options come from the cloud, not from the app. `requestSoc` sends `get_power_cutoff` with `device_sn` (`a17c1setting_logic.dart @0x3454204` URL, `@0x3454228` call) and `updateWithNewSocValue` reads the answer; model defaults when a value is missing are 100, 5 and 0 (`@0x34544f0`, `@0x345454c`, `@0x34545a8`, merged into unboxed registers).
- Both routes: the page shows the loaded values; the device must be reachable by the transport gate of step 8 for the device command to leave the app.

## Steps

| # | actor | action | owner page link | asm citation |
|---|---|---|---|---|
| 1 | user | Taps the safety SoC entry; `onTapSafetySoC` picks the route (Trigger). | this page | `a17c1setting_logic.dart @0x3d946fc` |
| 2L | app | Legacy: the picker (`showBottomPicker`) offers the server's reserve values; after a selection `showSocDialog` shows the texts `recommended` and `apply` when the value is below 10 (`cmp x3, #0xa`, unboxed) and otherwise goes straight on. | this page | `a17c1setting_logic.dart @0x3d949bc`, `@0x3d94bc4`, `@0x3d94bec`, `@0x3d94c50` |
| 3L | app | Legacy: `requestToSetSoc` finds the selected entry in the option list (`indexOf`) and sends `set_power_cutoff` with `device_sn` and `cutoff_data_id` (encrypted POST), success callback only. | [set_power_cutoff](../api/power_service/app/compatible/set_power_cutoff.md) | `a17c1setting_logic.dart @0x3d94cd0`, `@0x3d94da8` (key), `@0x3d94e2c` (URL), `@0x3d94e48` (call) |
| 4L | app | Legacy success callback: fires the UI message 2214, then calls `A17C1AnkerDevice::setSoc` with three values (output cutoff, low-power input, input cutoff; fallbacks 10, 5, 10 when the server value is missing) and reports the choice to analytics (`APP_DEVICE_RESERVE_POWER_CHOOSE`). | [mqtt/a17c1.md](../mqtt/a17c1.md#0067-setsoc) | `a17c1setting_logic.dart @0x3d94ec8` (id), `@0x3d94ed0` (data), `@0x3d94f1c`, `@0x3d94f44`, `@0x3d94f6c` (fallbacks), call at `@0x3d94f90`, `@0x3d95044` (event name) |
| 2N | app | New: the SoC page returns a `SocLimitModel`; the callback builds a `NewSocParamModel` (`charge_upper_limit`, `discharge_lower_limit`, `backup_reserve`, `backup_reserve_switch`) and calls `requestNewSetSoc`. | [soc_setting_param](../models/soc_setting_param.md) | `a17c1setting_logic.dart @0x3d956c4`, call at `@0x3d95738` |
| 3N | app | New: `requestNewSetSoc` sends `set_power_cutoff` with `cutoff_data_id`, `device_sn`, `charge_upper_limit`, `discharge_lower_limit`, `backup_reserve`, `backup_reserve_switch` and `cmd_type`; `cmd_type` is the Smi raw 2 stored with `stur w`, so 1. | [set_power_cutoff](../api/power_service/app/compatible/set_power_cutoff.md) | `a17c1setting_logic.dart @0x3d957c0` to `@0x3d95974` (keys), `@0x3d95980` (`cmd_type`), `@0x3d959d4` (URL), `@0x3d959f8` (call) |
| 4N | app | New success callback: calls `setSoc` with the named arguments `backupReserve`, `backupReserveEnable`, `chargeUpperLimit`, `dischargeLowerLimit`. | [mqtt/a17c1.md](../mqtt/a17c1.md#0067-setsoc) | `a17c1setting_logic.dart @0x3d95b3c` (argument list), `@0x3d95b44` (call) |
| 5 | cloud | Stores the new cutoff; the answer is not parsed by the success callbacks beyond triggering them. | [set_power_cutoff](../api/power_service/app/compatible/set_power_cutoff.md) untagged by design (no app-side fact) |
| 6 | app | `setSoc` builds opcode `0067`: the three-value call writes tags `a2`, `a3`, `a4`; the four-value call writes `a2`, `a5`, `a6`, `a7`. | [mqtt/a17c1.md](../mqtt/a17c1.md#0067-setsoc) | `a17c1_device_controller.dart @0x3d95494`, `@0x3d954d0`, `@0x3d95510` (three tags), `@0x3d95304`, `@0x3d95368`, `@0x3d953b4`, `@0x3d95414` (four tags), opcode `@0x3d95578` |
| 7 | app | Same transport gate as every A17C1 command: `bleBusinessConnected` over BLE, `wifiConnected` wrapped for MQTT, any other status sends nothing. | [ble/protocol.md](../ble/protocol.md#stacks-and-send-routing) | `a17c1_device_controller.dart @0x226e22c`, `@0x226e4e4` |

The `L` rows belong to the legacy route and the `N` rows to the new one; rows 1, 5, 6 and 7 are shared.

## Side effects

- Legacy only: the UI message 2214 is fired before the device command (data value 1: the raw 2 is a tagged Smi), not after it as the old page said.
- The device command exists only if the cloud call succeeded: both `setSoc` calls are inside the success callbacks (`a17c1setting_logic.dart @0x3d94f90`, `@0x3d95b44`). If the cloud call fails the command is never built.
- Analytics: `APP_DEVICE_RESERVE_POWER_CHOOSE` on the legacy route (`@0x3d95044`).

## Timing (delays/polling)

No delay or timer in `requestToSetSoc`, `requestNewSetSoc` or their callbacks. The device command follows the cloud answer.

## Failure paths

- Cloud failure on the legacy route: `requestToSetSoc` passes only a `success` callback (`a17c1setting_logic.dart @0x3d94e40`), so nothing happens on failure at this level and no device command is sent.
- Cloud failure on the new route: `requestNewSetSoc` passes `fail` and `success` (`@0x3d959f0`); the closure result of `@0x3d955f4` is a `Future<bool>` for the SoC page. The bodies were not read.
- Device not reachable over BLE or WiFi: the `0067` command is dropped by the gate (`a17c1_device_controller.dart @0x226e238`); the cloud value is already changed. Error codes: [errors](../api/errors.md).

## Since/changed

Corrections of the old FLOWS.md (audit rows in brackets), with the old value:

- Tag bytes: the three-value form uses `a2`, `a3`, `a4` (old `a2`, `a4`, `a6`; row 48). The old roles "currentSOC, minSOC, newSOC" do not match the parameters (output cutoff, low-power input, input cutoff; row 50 note).
- The UI message is `fire(2214, 1)`, not `(2214, 2)` (row 49); the id 2214 is correct.
- New in 3.24.3: the SoC settings page route, the `NewSocParamModel`, `requestNewSetSoc` and the `cmd_type` field (`requestNewSetSoc` does not exist in the 3.18.0 asm).
- Unchanged and confirmed: opcode `0067` (row 47); the fallbacks 10, 5, 10 (row 50); "API first, device only after success".

## Known unknowns

- What the offset 1307 flag means (the name is not in the asm) and which devices have it set.
- The bodies of the failure callbacks and of the `Future<bool>` result closure `a17c1setting_logic.dart @0x3d955f4`.
- How the new SoC page chooses `backup_reserve_switch` and its defaults (`SocManager`, not read).
- Which of the 3-tag and 4-tag forms the device accepts for which firmware (owner page: [mqtt/a17c1.md](../mqtt/a17c1.md#0067-setsoc)).
