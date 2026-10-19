> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# Solarbank 2 schedule (param_type 6)

How the app saves the custom schedule (energy plan) of a Solarbank 2 (A17C1 family) from the energy deployment page: a cloud save of the plan, a cloud save of the home load, and the schedule command to the device. The payloads live with their owners and are only linked here: the plan JSON on [set_site_device_param](../api/power_service/site/set_site_device_param.md) and [param_types](../api/param_types.md), the device command (opcode `005e`, tags, CRC) on [mqtt/a17c1.md](../mqtt/a17c1.md#005e-setbackpower-settacticstime-setpeakvalley). "Audit row N" counts the data rows of [../docs/audit/FLOWS.md](../docs/audit/FLOWS.md), see the [README](README.md#audit-row-numbers).

## Trigger (UI action)

On the energy deployment page the user taps the confirm control that runs the closure `energy_deploy_page.dart @0x3da9edc`, which calls `EnergyDeployLogic::sendHomeLoadData` (call at `energy_deploy_page.dart @0x3da9f08`, function `energy_deploy_logic.dart @0x2b48c8c`). The label of the control is not read from the asm. The old page claimed the entry was `ElectricityUsageHelper`; that class is not called on this path (audit row 1 names `energy_plan_logic.dart` as the sender, see the variant below).

Variant, not the main flow: deleting an entry on the energy plan page runs `EnergyPlanLogic::deleteHomeLoadData` (`energy_plan_logic.dart @0x3dac684`). It first stops with the toast `deviceOfflineConnect` (`@0x3dac800`) when the page has a device serial and its device flag (`field_7f.field_7`) is false (`@0x3dac7fc`). It then branches on the page's device-serial string (`field_7f.field_2b`, also passed to `getDeviceBySn` at `@0x3daca84`; empty test at `@0x3dac974`). With a serial it sends the device home load (`set17C1DeviceHomeLoadRes`, call at `@0x3dacb5c`) and the device command (call at `@0x3daccb0`). Without a serial it sends the same param_type 6 save as the main flow (literal `"6"` at `@0x3dacd58`, call at `@0x3dacd68`) and the device command (call at `@0x3dacf70`) only when the device status is `bleBusinessConnected`.

## Preconditions

- Network: the function stops with the toast `commonNetWorkErrorFix` when the connectivity check fails (`checkConnectivity` at `energy_deploy_logic.dart @0x2b48ccc`, text at `@0x2b48cec`, `_showNetWorkError` at `@0x2b48d00`).
- At least one repeat day: if `isPermitEditedSave` (`energy_deploy_logic.dart @0x2b48d10`) is false the page shows `a17c1RepeatPeriodEmpty` and stops (`@0x2b48d18`).
- Overlap: the page intersects the weekday sets of the other plan entries (`intersection` at `energy_deploy_logic.dart @0x2b49670`). On an overlap it shows a confirm dialog with the text `a17cxSiteHomeLoadCover` (`@0x2b499f0`, `showDialog` at `@0x2b49aac`) and returns; the confirm callback (closure `@0x2b48880`) loops twice over the plan entries (`@0x2b488d0`, `@0x2b48a78`), applies a closure to each entry's day list and then calls `sendHomeLoadData` again (`@0x2b48c28`). What the closure changes in the day lists is not read.
- The device is an A17C1-family device: `sendDeviceTacticsTime` tests the class id against four consecutive ids (`cmp x16, #3` at `energy_deploy_logic.dart @0x2b4b004`); the controller maps the four ids to the product strings `A17C1`, `A17C5`, `A17C3`, `A17C2` (`a17c1_device_controller.dart @0x226e138`, `@0x226e150`, `@0x226e168`, `@0x226e174`).

## Steps

| # | actor | action | owner page link | asm citation |
|---|---|---|---|---|
| 1 | user | Taps the confirm control; the closure calls `sendHomeLoadData`. | this page | `energy_deploy_page.dart @0x3da9edc` |
| 2 | app | `sendHomeLoadData` runs the connectivity, repeat-day and overlap checks of Preconditions, then calls `saveHomeLoadData`. | this page | `energy_deploy_logic.dart @0x2b48ccc`, `@0x2b48d10`, `@0x2b49670`, call at `@0x2b4aa98` |
| 3 | app | `saveHomeLoadData` shows the loading overlay (`showLoading`) and sets the plan-mode state from `PowerUsageScenarioLogic` (values chosen by compares at `@0x2b4ac98`, `@0x2b4acf8`). | this page | `energy_deploy_logic.dart @0x2b4abcc` |
| 4 | app | Sends the plan with `set17C1SiteDeviceParam`: `param_type` is the string `"6"`, named arguments `fail`, `showLoading`, `success`. `param_data` carries the `SiteConsumptionStrategyModel` JSON (mode, custom rate plan). The `cmd` value of this wrapper is listed on param_types (audit rows 1, 2). | [set_site_device_param](../api/power_service/site/set_site_device_param.md), [param_types](../api/param_types.md) | `energy_deploy_logic.dart @0x2b4adac` (literal), `@0x2b4adbc` (call); URL literal `http_request_repository_impl.dart @0x238cd60` |
| 5 | app | Does not wait for the answer. The same function goes on and sends the home load of the device with `set17C1DeviceHomeLoadRes`. | [set_device_home_load](../api/power_service/app/device/set_device_home_load.md) | `energy_deploy_logic.dart @0x2b4afa0`; URL literal `http_request_repository_impl.dart @0x2631510` |
| 6 | app | Calls `sendDeviceTacticsTime`, which sets the mode state again and calls `A17C1AnkerDevice::setTacticsTime` with the plan model. | this page | `energy_deploy_logic.dart @0x2b4afac` (call), `@0x2b4b118` (call of `setTacticsTime`) |
| 7 | app | `A17C1DeviceController::setTacticsTime` builds the tag map (29 data tags `a2` to `be`, then the CRC32 under tag `fd`) and sends opcode `005e` through `sendCommandWithParam`. The `mtu` argument is the Smi raw 400, real 200, and is only tested for non-zero. | [mqtt/a17c1.md](../mqtt/a17c1.md#005e-setbackpower-settacticstime-setpeakvalley) | `a17c1_device_controller.dart @0x288ac88` (array length), `@0x288b238` (CRC key), `@0x288b274` (`mtu` 200); audit rows 3, 4, 5, 6, 7, 9 |
| 8 | app | The transport is chosen by the connection status of the device. Status `bleBusinessConnected`: the frame is built for BLE (`isMoreLength` form) and written. Status `wifiConnected`: the same builder is called with `isBle` and wrapped by the MQTT transformer. Any other status: nothing is sent. | [ble/protocol.md](../ble/protocol.md#stacks-and-send-routing), [reference/enums.md](../reference/enums.md#deviceconnectionstatus) | `a17c1_device_controller.dart @0x226e22c` (BLE test), `@0x226e4e4` (WiFi test), `@0x226e238` and `@0x226e4f0` (fall through to return) |
| 9 | device | Receives the command. The reply handling is not part of this flow. | [mqtt/a17c1.md](../mqtt/a17c1.md#005e-setbackpower-settacticstime-setpeakvalley) untagged by design (no app-side fact) |

Dual-path claim of the old page ("BLE and API both sent"): the cloud save (steps 4 and 5) is always sent; the device command (steps 6 to 8) uses exactly one transport per call, chosen at `a17c1_device_controller.dart @0x226e22c` and `@0x226e4e4`. The call from `deleteHomeLoadData` is stricter: it sends the device command only when the status is `bleBusinessConnected` (`energy_plan_logic.dart @0x3dacda4` to `@0x3dacdb0`; the compared pool object is `pp+0xca68`, member `bleBusinessConnected`). BLE is not a live fallback for a device that is on WiFi, see [ble/protocol.md](../ble/protocol.md#connection-routing-and-the-wifi-exclusion-rule).

## Side effects

- The loading overlay stays up until the callbacks of the cloud save run (`showLoading` argument at `energy_deploy_logic.dart @0x2b4adb4`); what the callbacks do is not read, see Known unknowns.
- `sendDeviceTacticsTime` rewrites the plan-mode state (`field_7` of the mode object) before the send (`energy_deploy_logic.dart @0x2b4b088`, `@0x2b4b0bc`, `@0x2b4b0ec`).

## Timing (delays/polling)

No `Future.delayed` or timer is in `sendHomeLoadData`, `saveHomeLoadData` or `sendDeviceTacticsTime`. The three sends of steps 4 to 7 are issued one after the other without awaiting an answer (`saveHomeLoadData` is not `async`, `energy_deploy_logic.dart @0x2b4ab74`). A BLE frame longer than 200 bytes (`cmp x2, #0xc8` at `a17c1_device_controller.dart @0x226e2b0`) is split when the `mtu` argument is non-zero (`cbz x0` at `@0x226e3ec`, as it is for `setTacticsTime`), and the fragments are written with a delay between them, see [ble/protocol.md](../ble/protocol.md#timeouts-and-limits).

## Failure paths

- No network: toast, nothing sent (Preconditions).
- No repeat day: toast `a17c1RepeatPeriodEmpty`, nothing sent.
- Cloud errors: the `fail` callback of step 4 is a closure allocated at `energy_deploy_logic.dart @0x2b4ad8c`; its body is not read. Error codes: [errors](../api/errors.md).
- Device not connected over BLE or WiFi: the command of step 7 is dropped without a message at this level (`a17c1_device_controller.dart @0x226e238`).

## Since/changed

Corrections of the old FLOWS.md (audit rows in brackets), with the value the old page gave:

- The cloud request does not use the old `cmd` value 246 (raw immediate); the decoded value is on param_types (rows 1, 2, 67). "Both values work" is not an asm fact.
- The schedule command has 29 data tags `a2` to `be`, not 30 tags `a2` to `bb` (row 4); the last tag is the CRC32 under `fd`, not a timestamp (rows 5, 6) and not tag 506 (row 9).
- `mtu` is 200, not 400 (row 7); the default 200 is the same value (row 8).
- Seven slots, not 14 (row 11); the 14 `intToList(0)` calls at the start of the builder are zero defaults.
- `setTacticsTime` is 13,536 bytes (header size `0x34e0`) in 3.24.3 and was 14,020 bytes (`0x36c4`) in 3.18.0 (row 10).
- The old "dual path, both sent" is replaced by the gate in step 8.

Rows consumed without change: 3 (opcode `005e`), 14 (`mode_type` 3 is `ModeTypeCustom`, owner [param_types](../api/param_types.md)), 15 (worked example, not from asm).

## Known unknowns

- The bodies of the success and failure callbacks of step 4 (closures at `energy_deploy_logic.dart @0x2b4ad78` and `@0x2b4ad8c`).
- The mapping from the mode state to the value sent (steps 3 and 6) and whether any branch between `@0x2b4adbc` and `@0x2b4afa0` skips the home-load save.
- Which of the four slot tags carries start, end, power and charging percentage (owner: [mqtt/a17c1.md](../mqtt/a17c1.md#005e-setbackpower-settacticstime-setpeakvalley)); the byte layout of `DischargeTimeModel` and the seven "weekday groups" of the old page could not be re-derived (audit rows 12, 13).
- Other entry points that send the same pair: `power_usage_scenario_logic.dart`, `merge_system_energy_plan_logic.dart`, `custom_mode_usage_scenario_logic.dart` and `custom_mode_usage_scenario_detail_logic.dart` also call `setTacticsTime`; their gates were not read.
- The schedule enable condition of the old page (`NOT (is_charge_priority AND secondary flag)`) was not re-traced.
