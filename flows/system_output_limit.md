> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# System output limit

How the app sets the system output power limit of a station in 10 W steps (param_type 19). This page links to the owners of every payload; it copies none. The `display_type` key that 3.24.3 adds to the request is described on the endpoint page. The DIY prompt sheet of steps 9 to 12, with its two other entry points, is traced in [diy_unlock.md](diy_unlock.md); the A17C1 settings variant of an output limit is in [solarbank_power_limit_change.md](solarbank_power_limit_change.md).

## Trigger (UI action)

On the station power limit page (station settings), the user taps the output power entry. The tap handler is a closure built in `_StationPowerLimitContentView::_buildSingleDeviceLayout` (`station_power_limit_view.dart @0x4354f3c`, created at `@0x43545a8`); it calls `StationPowerLimitLogic::showOutputPowerPicker` (`station_power_limit_view.dart @0x4354f6c`, function `station_power_limit_logic.dart @0x4354f88`). It is the only output-limit path in 3.24.3; the other picker on the page is the legacy AC input picker below.

Legacy picker, not this flow: the page has a second picker, `showPowerLimitPicker` (`station_power_limit_view.dart @0x4355f04` and `@0x4357f7c`, logic `@0x4355f20`), which opens the older `PowerSliderView`. It ends in `_setDevicePowerLimit`, which sends `set_device_attrs {device_sn, attributes: {ac_power_limit}}` (asm-traced, confirmed in 3.24.3); owner page: [set_device_attrs](../api/power_service/app/device/set_device_attrs.md). That owner page is still a skeleton; this trace will be folded into it in Task 3.9/4.4. This is the per-device AC input limit, not the system output limit: upstream maps `ac_power_limit` to `ac_input` (`api/api.py` around line 1925, upstream-confirmed). The closure in `_buildSingleDeviceLayout` checks for `A17C1` and `A17C3` and shows the `noCapabilityForCharging` toast otherwise (asm-traced). `_updateSupportFlags` (`station_power_limit_logic.dart`, lines 471 to 816 of the asm dump) derives `supportAcLimit` for `AE103`, `A17E2` and `AE111` (strings `1200W` and `inputPower`; asm-traced). In the multi-device layout `_buildDeviceRow` calls the picker per device (asm-traced).

## Preconditions

- Logged-in account and a site id: `_getStationPowerLimit` returns without a request when the site id is empty (`station_power_limit_logic.dart @0x28cab98`). Upstream notes that `get_power_limit` needs the site owner (`api/apitypes.py`, comment on `get_site_power_limit`, upstream-confirmed).
- The station power limit page has loaded the model through [`get_power_limit`](../api/power_service/site/get_power_limit.md), and `power_limit_option` is not empty: the picker returns without showing anything when the option list is empty (`station_power_limit_logic.dart @0x4354fc8`).
- Cloud path only. This flow makes no BLE or MQTT call.
- Entry gate (asm-traced): the entry to this page is guarded by `_updateStationPowerLimitStatus` (`station_home_settings_logic.dart`, around line 4530 of the asm dump). It calls `getSitePowerLimit` with the body `{"site_id": ..., "app_ability": {"site_power_limit": true}}` (the `app_ability` key is part of the [get_power_limit](../api/power_service/site/get_power_limit.md) request). If that call fails, the status flag (Rx field `field_c3`) becomes `false`; on success the flag is `true` when model field 13 is non-null. That field is inferred to be `legal_power_limit` from the constructor store order (inferred, not confirmed by a name in the asm). `gotoStationOutPutPowerPage` routes to `/stationPowerLimit`.
- Which devices show which rows on the page is only partly traced: `_updateSupportFlags` (`station_power_limit_logic.dart`) derives per-model flags, see the legacy AC input picker note in Trigger.

## Steps

| # | actor | action | owner page link | asm citation |
|---|---|---|---|---|
| 1 | user | Opens the station power limit page; `StationPowerLimitLogic::onInit` calls `_getStationPowerLimit`. | [get_power_limit](../api/power_service/site/get_power_limit.md) | `station_power_limit_logic.dart @0x34b0bdc` |
| 2 | app | Sends `get_power_limit` (encrypted) for the site. | [get_power_limit](../api/power_service/site/get_power_limit.md) | `station_power_limit_logic.dart @0x28cac9c` |
| 3 | app | Receives the response and parses it into `StationPowerLimitModel` in the success closure of `getSitePowerLimit`. | [StationPowerLimitModel](../models/station_power_limit.md) | `http_request_repository_impl.dart @0x23790e0`, `fromJson` at `station_power_limit_model.dart @0x2379150` |
| 4 | app | Parses the model and keeps: `legal_limit` as the prompt threshold, `legal_power_limit` as the displayed current limit (`"<value>W"`), `power_limit_option` as the list `"<limit>W"`. | [StationPowerLimitModel](../models/station_power_limit.md#consumed-by) | `station_power_limit_logic.dart @0x28cacc4` |
| 5 | user | Taps the output power entry (trigger above). | this page | `station_power_limit_view.dart @0x4354f6c` |
| 6 | app | Opens `NewPowerSliderView` in a bottom sheet. Start value: the displayed current limit parsed as int, or 100 if that fails (raw 100 at `@0x435505c`, unboxed). Minimum: 100 W (raw 100, `mov x0, #0x64`, stored 64-bit `stur x0` at `@0x43550bc`, unboxed, so 100). Maximum: the last entry of the option list, parsed as int (`@0x4354fdc`, stored 64-bit at `@0x43550c4`; 0 if parsing fails, `@0x4355008`). Step: 10 W (raw 10, `mov x1, #0xa`, stored 64-bit `stur x1` at `@0x43550cc`, unboxed, so 10). | this page | `station_power_limit_logic.dart @0x43550b8`, `@0x43550c8` |
| 7 | app | The slider widget itself rounds to multiples of 10 (`d0 = 10.0` at `new_power_slider_view.dart @0x30bd61c`, `mul` by raw 10 at `@0x30bd684`, unboxed) and clamps to 100 ... maximum (raw 200 passed as a boxed Smi argument to `clamp`, so 100, at `@0x30bd6c4`); the +/- buttons add or subtract 10 (`add x3, x2, #0xa` on an untagged value, so 10, at `@0x30bdd78`). | this page | `new_power_slider_view.dart @0x30bd5b0` |
| 8 | user | Confirms a value `v` (W). | this page | `station_power_limit_logic.dart @0x43551bc` |
| 9 | app | Decides whether the DIY prompt is needed. No prompt (go to step 13) if `v <= legal_limit` (`@0x43552a0`), or if the value last set on this page is above `legal_limit` (`@0x4355308`), or if `legal_limit <= 0` (`@0x4355338`, compare with 0 on an untagged value). Otherwise continue with step 10. | [StationPowerLimitModel](../models/station_power_limit.md) | `station_power_limit_logic.dart @0x43552a0` |
| 10 | app | Picks the prompt variant from `unlock_default_power_type` (null becomes 0, `@0x4355380`): 1 gives `image`, 2 gives `imagePassword`, anything else gives `h5`. The compares run on the boxed value, `cmp w0, #2` (Smi 1) at `@0x43553b4` and `cmp w0, #4` (Smi 2) at `@0x43553dc`; enum objects `image` = `pp+0xa5748`, `imagePassword` = `pp+0xa5750`, `h5` = `pp+0xa5758`. `DiyLegalPowerLimitType.fromInt` (`diy_legal_power_limit_sheet.dart @0x2af0180`) uses the same mapping (`@0x2af01a8`, `@0x2af01d8`). | [StationPowerLimitModel](../models/station_power_limit.md) | `station_power_limit_logic.dart @0x43553bc`, `@0x43553e4`, `@0x43553f0` |
| 11 | app | Shows `DiyLegalPowerLimitSheet` with the variant, `unlock_pop_image`, `unlock_pop_content` and the site id, plus two callbacks that both close the sheet and call `_setOutputPowerLimit(v)` (closures `@0x4355b94` and `@0x4355aec`). | this page | `station_power_limit_logic.dart @0x4355524` |
| 12a | user, app | Variant `imagePassword`: the user types the code and confirms; the app sends `verify_unlock_default_power_code` with `unlock_code` and `site_id`. If `verify_result` is `true` the sheet calls its success callback (closure `@0x4355aec`), which continues with step 13; otherwise the sheet shows the translated text `passwordError`. | [verify_unlock_default_power_code](../api/devicecontrol/device/verify_unlock_default_power_code.md) | `diy_legal_power_limit_sheet.dart @0x30bc02c` |
| 12b | user, app | Variant `image`: the content widget receives the callback `@0x4355b94` (`diy_legal_power_limit_sheet.dart @0x30b940c`) and continues with step 13 when the user confirms. Variant `h5`: the confirm path is not traced. | this page | `diy_legal_power_limit_sheet.dart @0x30b93f0` |
| 13 | app | `_setOutputPowerLimit(v)` sends `set_site_device_param` with param_type 19 (encrypted), `limit` = `limit_real` = `v`. | [set_site_device_param](../api/power_service/site/set_site_device_param.md#usage-param_type-19-system-output-power-limit), [param_types](../api/param_types.md) | `station_power_limit_logic.dart @0x435567c` |
| 14 | app | Receives the result of `set_site_device_param`; the success callback and the failure callback only write log lines (no state change, no retry). | [set_site_device_param](../api/power_service/site/set_site_device_param.md) | `station_power_limit_logic.dart @0x4355a70` (success), `@0x4355a1c` (failure log) |

## Side effects

All of these run right after the request is handed to the HTTP layer, without waiting for the response (`setSiteDevicePowerLimit` returns `void`, `http_request_repository_impl.dart @0x4355990`):

- The displayed current limit becomes `"<v>W"` (`station_power_limit_logic.dart @0x4355690`).
- The "last set value" kept by the page becomes `v` (`@0x43556ac`); step 9 uses it, so after one value above the legal limit has been set, later values above it skip the prompt for as long as the page lives.
- If the exceed alarm flag is set, it is cleared (`@0x43556d4`).
- An internal boolean of the page (field at offset 0xa3, initially `true`, `@0x413d47c`) is set to `false` (`@0x43556e8`) and back to `true` after a delay (see Timing). Its effect in the UI is not traced.
- The flow does not re-read `get_power_limit` afterwards; the success callback only writes a log line (`@0x4355a70`).

## Timing (delays/polling)

3 s: `Future.delayed` at `station_power_limit_logic.dart @0x43556fc` uses the constant `Duration` object `pp+0x13660` with `off_8: int(0x2dc6c0)` = 3,000,000 microseconds (a pool object value, not a register immediate, so the Smi rule does not apply). After it the internal boolean is set back to `true` (closure `@0x43559a8`). No polling.

## Failure paths

- `set_site_device_param` fails: the failure callback only logs `StationPowerLimit - 设置输出功率限制失败: code=<code>, msg=<msg>` ("setting output power limit failed", `station_power_limit_logic.dart @0x4355a1c`). The side effects above have already happened, so the page keeps showing `v` even though the server rejected it. Error codes: `api/errors.md`.
- `verify_unlock_default_power_code` fails at transport or server level: log line `verifyUnlockDefaultPowerCode fail: code=<code>, msg=<msg>` and the translated text `netWorkError` in the sheet (`diy_legal_power_limit_sheet.dart @0x30bc328`, `@0x30bc374`). No limit is set.
- `verify_result` is `false` or missing: the sheet shows `passwordError` (`diy_legal_power_limit_sheet.dart @0x30bc490`). No limit is set.
- Empty unlock code: `_onConfirm` returns without a request (`diy_legal_power_limit_sheet.dart @0x30bbef4`).

## Known unknowns

- Server validation: partly answered by a device test on an A17C5, see [set_site_device_param, Device-tested by](../api/power_service/site/set_site_device_param.md#device-tested-by); other devices and firmware are untested. The app never sends `display_type: 0`.
- Whether the server accepts every 10 W value between 100 W and the maximum, or only some of them, for a given device and firmware.
**Warning:** `legal_limit` is the regulatory feed-in limit of the site's region; the server not enforcing it is not permission — exceeding it may be unlawful or void the installation's certification, and this reference does not endorse it.

- Whether the server enforces the legal limit on other devices; the A17C5 result is on the endpoint page (linked above). The prompt in steps 9 to 12 is app-only.
- The confirm path of the `h5` prompt variant.
- What the internal boolean toggled around the 3 s delay controls in the UI.
- The server meaning of `display_type` and whether the upstream library's `cmd` value is accepted as well as the app's; both are tracked on [set_site_device_param](../api/power_service/site/set_site_device_param.md#known-unknowns).
