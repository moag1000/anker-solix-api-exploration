> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# Solarbank power limit change (opcode 0080)

How the app changes the output limit, the PV limit, the AC input limit and the grid feed-in value of a Solarbank 2 (A17C1 family). Each of the four settings is a separate entry point on the A17C1 settings page that sends one cloud `set_device_attrs` request and one call of `A17C1AnkerDevice::setDevicePowerLimit` with its own named argument; a fifth entry, a listener on the home page, calls the same method with `feeder0w` and `switch0w`. The system output limit of a station (param_type 19) is another flow: [system_output_limit.md](system_output_limit.md). Payloads live with their owners: [set_device_attrs](../api/power_service/app/device/set_device_attrs.md) and the command [mqtt/a17c1.md](../mqtt/a17c1.md#0080-setdevicepowerlimit). "Audit row N" counts the data rows of [../docs/audit/FLOWS.md](../docs/audit/FLOWS.md), see the [README](README.md#audit-row-numbers).

## Trigger (UI action)

On the A17C1 settings page (`a17c1setting_page.dart`) the user opens one of four pickers. The cloud attribute and the named argument that each sends are traced in the logic class (`a17c1setting_logic.dart`):

| entry | page call | cloud attribute | named argument of `setDevicePowerLimit` | asm citation |
|---|---|---|---|---|
| output power limit | `showPowerLimitPicker` (`a17c1setting_page.dart @0x3d919c8`, function `a17c1setting_logic.dart @0x3d919e4`) | `power_limit` | `power` | `a17c1setting_logic.dart @0x3d92790`, `@0x3d92828` |
| PV power limit | `showPvPowerLimitPicker` (`a17c1setting_page.dart @0x3d970b0`) | `pv_power_limit` | `pvPowerLimit` | `a17c1setting_logic.dart @0x3d976b8`, `@0x3d976d0` |
| AC input limit | `showGridConnectedInputPicker` (handler `setGridConnectedInput`, function `a17c1setting_logic.dart @0x3d91390`) | `ac_power_limit` | `acPowerLimit` | `a17c1setting_logic.dart @0x3d914b8`, `@0x3d91460` |
| grid feed-in value | see [solarbank_toggle_grid_export.md](solarbank_toggle_grid_export.md) | `switch_0w` | `feeder0w` and `switch0w` | `a17c1setting_logic.dart @0x3d90978` |

The home page listener is the closure `a17c1home_logic.dart @0x33d0e0c` (parameter type `DevicePowerLimit`); it calls the method at `a17c1home_logic.dart @0x33d104c` and `@0x33d15b0`.

## Preconditions

- Output power picker: `showPowerLimitPicker` first reloads the options with `getPowerLimitList` (14 device attributes, see [solarbank_toggle_grid_export.md](solarbank_toggle_grid_export.md#preconditions); call at `a17c1setting_logic.dart @0x3d91a3c`) and logs the country code and the language (`@0x3d91ad4`, `@0x3d91b10`) before it shows the picker (`showBottomPicker` at `@0x3d91bac`).
- Legal limit prompts, output power picker callback (`a17c1setting_logic.dart @0x3d91bd4`): the selected text loses its `W` and is parsed. When the page's legal power limit state is 0 (`cbnz` on the Smi at `@0x3d91d14`; not a mode state), a value of 800 or more (`cmp x0, #0x320`, unboxed) on a device that is not an Italian-limit device (`isItalyPowerLimit`, `@0x3d91d38`) schedules a reminder dialog after 200 ms (`Future.delayed`, closure `@0x3d93338`, `reminderPowerLimitDialog` at `@0x3d933d8`). On an Italian-limit device (`showItalyPowerLimit`, `@0x3d91da4`) a value above 350 (`cmp x0, #0x15e`) schedules a confirm dialog with the text `makeSureCompleteCertificationTips` (closure `@0x3d93198`, `@0x3d931e0`). The callback can also open the `DiyLegalPowerLimitSheet` (`@0x3d91fa8`, `show` at `@0x3d92008`) whose two callbacks call `setPowerLimit` (`@0x3d93024`, `@0x3d93108`); that sheet is the flow [diy_unlock.md](diy_unlock.md). Which condition leads to which exit: [Output picker decision tree](#output-picker-decision-tree).
- Home page listener: the closure reads the received `DevicePowerLimit` and compares it with cached device values at offsets 0x2a3 (`a17c1home_logic.dart @0x33d0e7c`) and 0x2d7 (`@0x33d0f40`); the device online flag at offset 0x4e7 (`@0x33d0f00`, 1255 in 3.24.3) must be true; the second send is guarded by the flag at offset 0x297 (`@0x33d1508`, 663).

## Steps

| # | actor | action | owner page link | asm citation |
|---|---|---|---|---|
| 1 | user | Opens a picker and confirms a value; for the output power picker the legal-limit prompts above may come first. | this page | `a17c1setting_logic.dart @0x3d91bd4` |
| 2 | app | `setPowerLimit` parses the value (`NNNW`), sends `set_device_attrs` with `device_sn` and `attributes` holding `power_limit` through `setDevicePowerOptionsReq`, encrypted. The other two pickers send `ac_power_limit` and `pv_power_limit` the same way. | [set_device_attrs](../api/power_service/app/device/set_device_attrs.md) | `a17c1setting_logic.dart @0x3d92764`, `@0x3d92790`; `http_request_repository_impl.dart @0x22769d8` (key `power_limit`), `@0x2276a6c` (URL), `@0x2276a8c` (call) |
| 3 | app | Without waiting for the answer calls `A17C1AnkerDevice::setDevicePowerLimit(power: value)`; the wrapper takes the named arguments `acPowerLimit`, `countryCode`, `feeder0w` (default 0), `power`, `pvPowerLimit`, `switch0w` (default 0) and passes them on to the controller. | [mqtt/a17c1.md](../mqtt/a17c1.md#0080-setdevicepowerlimit) | `a17c1_anker_device.dart @0x2276b6c` (argument list), `@0x2276e20` (call); `a17c1setting_logic.dart @0x3d92830` |
| 4 | app | The controller starts with an empty tag map, adds entries in five guarded blocks and sends the map once. (1) The second positional slot, which the wrapper fills with `countryCode`, is non-null: tags `a2` (from the `power` slot), `a3` (zero), `a4` (from `countryCode`), `a5` (from `feeder0w`), `a6` and `a7` (from `pvPowerLimit`). (2) `acPowerLimit` non-null: tag `a8` alone (log label `acPowerLimit`). (3) `power` non-null: tags `a2` and `a3` (zero). (4) `pvPowerLimit` non-null: tag `a7` alone (log label `pvPowerLimit`). (5) Tags `a5` and `a6` from `feeder0w` and `switch0w`, reached only when blocks 1 to 4 were all skipped and sent only when the device flag at offset 663 is true (see [Block-5 guard](#block-5-guard-and-the-a6-source)). The tags are consecutive, not `a2`, `a4`, `a6`, `a8`, `aa`, `ac`. | [mqtt/a17c1.md](../mqtt/a17c1.md#0080-setdevicepowerlimit) | `a17c1_device_controller.dart @0x2276ea0` (gate 1), `@0x2277100` (gate 2), `@0x22771dc` (gate 3), `@0x2277328` (gate 4), `@0x2277410` (gate 5), tag keys `@0x2276ec0`, `@0x2276f08`, `@0x2276f44`, `@0x2276f90`, `@0x2276fcc`, `@0x227704c`, `@0x2277134`; opcode `@0x2277580` |
| 5 | app | One `sendCommandWithParam` call sends the result; transport by connection status: `bleBusinessConnected` over BLE, `wifiConnected` wrapped for MQTT, any other status sends nothing. | [ble/protocol.md](../ble/protocol.md#stacks-and-send-routing) | `a17c1_device_controller.dart @0x2277590`, `@0x226e22c`, `@0x226e4e4` |
| 6 | app | After the send the output picker goes back (`GetNavigation.back`) and a 3 s delay runs a closure. | this page | `a17c1setting_logic.dart @0x3d9289c`, `@0x3d928c4` |
| 7 | app | Home page listener: when the received mode state is 1 and the current route is `/a17c1Home` the app logs the feed-in change, fires the UI message 2123 and shows the dialog `deviceInformationUpdate`; it caches the 0 W off-net state with `setZeroWPowerOffNetCache`. | this page | `a17c1home_logic.dart @0x33d1088` (compare, offset 667), `@0x33d10cc` (route), `@0x33d124c` (message), `@0x33d1268`, `@0x33d133c` |
| 8 | app | Home page listener, after the second send: sets the charge-priority flags from the received `charge_priority`: the value 2 sets `is_charge_priority` (offset 0x2cf), the value 1 sets the secondary flag (offset 0x2d3). | this page | `a17c1home_logic.dart @0x33d160c`, `@0x33d1658`, `@0x33d1884`, `@0x33d189c` |

## Output picker decision tree

Tag: asm-traced. Callback `a17c1setting_logic.dart @0x3d91bd4` (the confirm callback of the wheel picker: `SinglePickerRoute` calls the stored closure on commit, `single_picker_route.dart @0x314ebd8`; the scroll callback `@0x3d93710` is a different closure and never calls `setPowerLimit`). It receives the picked index into the option list, strips the `W` from the label and parses it (`@0x3d91c40..0x3d91c8c`). `legal` below is the page's legal power limit (`legal_power_limit`, state field `f7f`, 800 when the response has none, `@0x26d24f8`); `last` is the last output power confirmed on this page instance (`f2f`, written only by `setPowerLimit`, `@0x3d92870`, its only writer found; see Known unknowns for the role). The picked power and the 800 W and 350 W thresholds are unboxed 64-bit integers (the picked value is compared in the same function against an untagged value, `@0x3d91e4c`), so `cmp x0, #0x320` is 800 W and `cmp x0, #0x15e` is 350 W. Evaluate top to bottom; the first row that matches decides.

| # | condition | compare (width) | action | citation |
|---|---|---|---|---|
| 1 | `legal == 0` and picked >= 800 W and not `isItalyPowerLimit()` (Italy region flag set and no meter flag) | `cbnz w0` on the Smi (0); `cmp x0, #0x320`, 64-bit unboxed, 800 W | after 200 ms the reminder dialog `reminderPowerLimitDialog`; no `setPowerLimit` yet. First time per device (`powerLimit800W` flag in shared preferences not 1): flag set to 1, dialog with confirm, confirm calls `setPowerLimit`; later: `setPowerLimit` at once | `@0x3d91d10..0x3d91d58`; closure `@0x3d93338`; `@0x3d933f4`, `@0x3d93488`, `@0x3d93514` |
| 2 | `legal != 0`, `showItalyPowerLimit()` true and picked > 350 W | `cmp x0, #0x15e`, 64-bit unboxed, 350 W | after 200 ms the dialog `makeSureCompleteCertificationTips` (certification, Italy); confirm calls `setPowerLimit` | `@0x3d91da4..0x3d91dd8`; closure `@0x3d93198`, `@0x3d93254` |
| 3 | `legal != 0`, not Italian, picked > `legal` and `last <= legal` | two signed 64-bit compares of untagged values (`b.le`, `b.gt` skip) | close the picker and open `DiyLegalPowerLimitSheet`; both of its closures call `setPowerLimit` (flow [diy_unlock.md](diy_unlock.md)) | `@0x3d91e4c`, `@0x3d91ebc`, `@0x3d91ef0`, `@0x3d91fa8`, `@0x3d92008`; closures `@0x3d930b4`, `@0x3d92fd0` |
| 4 | none of rows 1 to 3 (default path), and the home-load state has no `current_home_load` or no `custom_rate_plan`, or the largest plan range `power` is <= the picked power | `cmp x2, x1`, `b.le`, both unboxed 64-bit | `setPowerLimit` directly | `@0x3d92078..0x3d92084`, `@0x3d92338`, `@0x3d92360` |
| 5 | default path and the largest custom-rate-plan range `power` is > the picked power | same compare, falls through | after 200 ms `upperPowerLimitDialog` (text `switchLimitationPower`, confirm button); confirm calls `setPowerLimit` | closure `@0x3d92c98`; `@0x3d92d38`; confirm closure `@0x3d92f48` |

Value source. The picker is a wheel list of strings built from `power_limit_option` (one `"<n>W"` per entry, `@0x26d21f8`, closure `@0x26d2cb8`); the callback only gets an index, so no free value and no slider exist for the output limit here (the `PowerSliderView` of this logic belongs to the AC input picker, `@0x3d911f4`). `setPowerLimit` (`@0x3d92698`) sends two values: the cloud call `set_device_attrs` takes the number parsed from the display label (`@0x3d92764`, `@0x3d92790`), while the device command 0080 takes the number parsed from `power_limit_option_real[index]` when `power_limit_option` and `power_limit_option_real` have equal length (`cmp w1, w0`, 32-bit lengths, `@0x3d927b8`, `@0x3d927dc`), else from the label. Whether the two lists differ in real responses is a question about server data.

No request of `param_type` 18 or 19 exists in this page tree: no reference to `set_site_device_param`, `param_type` or the pool strings `"18"` and `"19"` in the A17C1 setting and home files, the two A17C1 device helper files or the DIY sheet; the callees of the logic into `HttpRequestController` do not include `setSiteDeviceParam` (asm-traced as absence; a request fired by a shared widget outside these files is not excluded). Which generation uses which path is summarised in [../devices/solarbank.md](../devices/solarbank.md).

## Side effects

- The cloud attribute and the device value are written independently; a failure of one does not stop the other.
- Home page listener: the cached 0 W state and the charge-priority flags change; both flags affect whether the schedule is shown as enabled (the exact condition is not re-traced here).
- The output picker closes after the call and re-enables itself after 3 s.

## Timing (delays/polling)

- 3 s after the output limit call: `Future.delayed` at `a17c1setting_logic.dart @0x3d928c4` uses the pool `Duration` `pp+0x13660` with `off_8` 0x2dc6c0 = 3,000,000 microseconds (a pool object value, not a register immediate).
- 200 ms before the legal-limit reminder: pool `Duration` with `off_8` 0x30d40 = 200,000 microseconds (`a17c1setting_logic.dart @0x3d91d44`, `@0x3d91dc4`, `@0x3d9236c`).

## Failure paths

- Cloud failure: `setDevicePowerOptionsReq` passes `fail` and `success` closures (`http_request_repository_impl.dart @0x2276a40`, `@0x2276a54`); the failure text `set setDevicePowerOptionsReq failed, code:` exists for the PV variant (`http_request_repository_impl.dart @0x3d97a2c`). The device command is sent regardless.
- Device not reachable over BLE or WiFi: the command is dropped by the gate (`a17c1_device_controller.dart @0x226e238`). Error codes: [errors](../api/errors.md).
- Home page listener: offline (flag 0x4e7 false) skips the send (`a17c1home_logic.dart @0x33d0f0c`).

## Since/changed

Corrections of the old FLOWS.md (audit rows in brackets), with the old value:

- The TLV key column `0x0144` to `0x014E` and the tags `a2`, `a4`, `a6`, `a8`, `aa`, `ac` were the tagged Smi; the tags are `a2` to `a7` (and `a8`) (row 40).
- The old "4 code paths" (full for `acPowerLimit`, AC for `param2`, PV, default) do not match the asm: four settings entries call the method with different named arguments, and the controller has five guarded blocks (step 4); the full block is gated by `countryCode`, not by `acPowerLimit` (row 46, prose count).
- Guards, 3.18.0 to 3.24.3 (rows 41 to 43, changed): device online offset 1231 (0x4cf) became 1255 (0x4e7); cached `feeder_power` 663 (0x297) became 675 (0x2a3); `fc_enabled` 651 (0x28b) became 663 (0x297).
- The 0 W dialog test is mode 1, not 2 (row 44; the raw `cmp w3, #2` is a tagged value); the charge-priority values are 2 and 1, not 4 and 2 (row 45).
- Unchanged: opcode `0080` (row 39). The old claim that the device command is the only path is replaced by step 2: every entry also sends `set_device_attrs`.

## Block-5 guard and the `a6` source

Tag: asm-traced. Widths: the flag is a Dart bool (object word, compared on bit 4); `feeder0w` and `switch0w` are 64-bit unboxed ints; the tag values are 16-bit (`intToList2`).

- Guard (`a17c1_device_controller.dart @0x2277404..0x2277420`): `field_67` of the controller, then `ldr w2, [x1, #663]`, then `tbz w2, #4, #0x2277430`. `tbz` branches when bit 4 is clear, which is Dart `true`; so a true flag builds block 5, and a false flag (bit 4 set) falls into `r0 = Null; ret` at `@0x2277420`: nothing is built and no `0080` frame is sent, with no log line. The block is reached only when `pvPowerLimit` is null (`cmp w0, NULL; b.eq #0x2277404` at `@0x2277328`).
- Where the flag is written: `A17C1DeviceCommands::parseDeviceAllInfo` (`a17c1_device_commands.dart @0x48648b4`) stores `list[7] == 1` of the byte list in tag `fc` (index 252) into offset 663 (`cmp w0, #2` against the tagged Smi, so 1, then `csel true/false`, store `@0x48667a4`; list index: the raw 14 passed to the list getter is the Smi 7, `@0x4866770`); when tag `fc` is absent the flag is stored false (`@0x48668d8..0x48668e4`, branch `b.eq` at `@0x48664e0`). Same field as `fc_enabled` of 3.18.0 (see the guard list above) and `capability_flag_14` ("isEnable0w", labelled a static firmware capability in the 3.18.0 device test, [archive](../docs/archive/BLE_COMMAND_MAP-3.18.0.md), audit row 413 in [docs/audit/BLE_COMMAND_MAP.md](../docs/audit/BLE_COMMAND_MAP.md)); this page does not rename it. The home listener reads the same offset for its second send (`a17c1home_logic.dart @0x33d1508`).
- `a6` source: `switch0w` is the last named parameter of the wrapper `A17C1AnkerDevice::setDevicePowerLimit` (`a17c1_anker_device.dart @0x2276b60`); it is read as an int (Smi `sbfx x2, x0, #1, #0x1f` or Mint `ldur x2, [x0, #7]`, `@0x2276d80..0x2276d88`), defaults to 0 (`@0x2276d94`), is stored unboxed (`@0x2276d98`) and passed on the stack (`str x0, [SP]`, `@0x2276e04`, call `@0x2276e20`). The controller reads it as `[fp, #0x10]` (`@0x2277484`) and writes it through `intToList2` under key 332 (raw `0x14c`, tag `a6`; `feeder0w`, from register `r5`, goes under raw 330, tag `a5`, `@0x2277440..0x227744c`). Values passed by the callers: the grid feed-in toggle sends the new switch value as `switch0w` and the cached device word at offset 727 as `feeder0w` (`a17c1setting_logic.dart @0x3d90964..0x3d90980`).

## Known unknowns

- Block-5 flag: the initial value of offset 663 before the first `parseDeviceAllInfo` was not traced (constructor not decoded); the behaviour of `list[7]` on a `fc` list shorter than 8 bytes (Dart list index; the visible guards at `@0x48665a0` test only non-emptiness); and which transport delivers the TLV map that `parseDeviceAllInfo` reads (not determined here). The argument-to-block mapping above comes from the guard registers and the two log labels; the owner page [mqtt/a17c1.md](../mqtt/a17c1.md#0080-setdevicepowerlimit) still lists it as open.
- Decision tree details not resolved: which of the two DIY sheet closures (`@0x3d930b4`, `@0x3d92fd0`) is bound to which sheet event (both end in `setPowerLimit`); whether this page's `deviceModel` can carry the A17C2 class, which changes `showItalyPowerLimit`; the setter of the meter flag `f43`; the cancel behaviour of the reminder and upper-limit dialogs; the body of the scroll warning closure `@0x3d93bc8`; the plan class field names of the range list (taken from the loop shape); the role of `last` (`f2f`) as the last confirmed output power rests on its single writer found.
- The order of the guards in the home listener; the old page's "any fail skips" is not re-derived.
- Whether the server applies `power_limit` without the device command (server behaviour).
