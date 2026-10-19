> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# platform_set_user_region_param

## Purpose

Saves the grid code settings of a product for the user: the app sends the grid parameter document (country, grid code, enabled and advanced parameters) plus the flag `is_push_device`, which tells whether the settings were also pushed to the device.

## Upstream name

`none` for the key; upstream lists the URL without a key in `api/apitypes.py` (line 352).

## Method+URL

`POST /power_service/v2/platform_set_user_region_param` (asm-traced). Senders: `GridParamSettingController.updateCloudSetting` in the `device` package (`device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart @0x47c84f0`; URL literal `@0x47c85d0`, `Method.post` `pp+0xa7e0`) and in the `settings` package (`settings/src/common/page/grid_param_setting/grid_param_setting_controller.dart @0x3a57130`), `GridSettingLogic._setEnwgSwitch` (`charging/ui/page/device/main/sitation_energy_system/station_home_settings/advanced_setting/grid_setting_logic.dart @0x3fac850`; URL `@0x3facb54`), `GridProtectSettingController.saveProtectParam` (`settings/src/common/page/grid_param_setting/grid_protect_setting_controller.dart @0x3a59ff0`; URL `@0x3a5a18c`) and the SDK closure of `SystemConfigController.updateCountryCodeByCloud` (`system_config_controller.dart @0x32558c0`).

## Encrypted?

`updateCloudSetting`, `_setEnwgSwitch` and `saveProtectParam` call `encryptionRequestHttp` (`device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart @0x47c85f4`, `settings/src/common/page/grid_param_setting/grid_protect_setting_controller.dart @0x3a5a1b4`, `_setEnwgSwitch` after `@0x3facb54`) without `needEncryption`, so the default `true` applies ([which calls are encrypted](../../encryption.md#which-calls-are-encrypted)); whether the call goes through the SDK is decided at run time. The `system_config_controller` closure is a direct SDK call (path C). `saveProtectParam` turns the loading overlay off (`r30 = false`, `@0x3a5a19c`).

## Request

The body is the grid parameter document (the `GridParamSettingInfo` keys, see [the model page](../../../models/grid_param_setting_info.md)) built by the page, completed by the sender. Keys the senders add or remove:

| field | type | required | example | source |
|---|---|---|---|---|
| `is_push_device` | int | yes | `2` | `updateCloudSetting`: `device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart @0x47c8564` (settings copy `@0x3a571a4`); value computed from a boolean field of the controller (offset 0x83, `@0x47c8548`) with `csetm`, `and #2`, `add #2` (`@0x47c8554` to `@0x47c855c`): tagged Smi 2 when the field is true, 1 when false (raw 4 / raw 2). `_setEnwgSwitch`: `charging/ui/page/device/main/sitation_energy_system/station_home_settings/advanced_setting/grid_setting_logic.dart @0x3facab4`, literal raw `2` (`@0x3facabc`, a map `[]=` argument, tagged), so 1. `saveProtectParam`: `settings/src/common/page/grid_param_setting/grid_protect_setting_controller.dart @0x3a5a0e8`, computed like `updateCloudSetting` from a field at offset 0x47 (`@0x3a5a0cc` to `@0x3a5a0e0`) |
| `grid_code`, `country_code`, `grid_code_name`, `enable_params` | String / map | `_setEnwgSwitch` | not decoded | `charging/ui/page/device/main/sitation_energy_system/station_home_settings/advanced_setting/grid_setting_logic.dart @0x3faca20`, `@0x3faca58`, `@0x3faca90`, `@0x3facaa4`; the first three come from the selected grid object (null if none), `enable_params` is the switch map (`1` / `0` strings `@0x3fac96c`, `@0x3fac978` select its value) |
| `scenario_type` | int | `saveProtectParam` | not decoded | `settings/src/common/page/grid_param_setting/grid_protect_setting_controller.dart @0x3a5a0b0`; value is a field at offset 0x4b (`@0x3a5a098`) |
| `advanced_params_template`, `enable_params` | removed | `saveProtectParam` only | n/a | the keys are removed from the document before sending (`remove`, key loads `@0x3a5a104`, `@0x3a5a120`); the advanced values travel as a JSON-encoded text (`jsonEncode`, `@0x3a5a044`) in the document built by the page |

`GridParamSettingController.setGridInfo` (`device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart @0x47c837c`) shows the loading overlay and then calls `updateCloudSetting` with three captured values (`@0x47c84cc`) or, when the device is reachable locally, first `sendCommend` to the device (`@0x47c8470`).

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no response model; see Response.

## Response

No response field is read by the traced senders (asm-traced): the success closures (`@0x3192d04`, a mixin closure `_updateCloudSetting` in the deduplicated mixin region, not in `grid_param_setting_controller.dart`; mixin-sourced, body not read; `charging/ui/page/device/main/sitation_energy_system/station_home_settings/advanced_setting/grid_setting_logic.dart @0x3facc64`) only close the loading overlay and report success; the failure closures (`@0x47c8614`, `@0x3facb9c`) report the error.

## Example request/response

Request, synthesized (`_setEnwgSwitch`)

```json
{ "grid_code": "<grid code>", "country_code": "DE", "grid_code_name": "<grid code name>", "enable_params": { ... }, "is_push_device": 1 }
```

Response: no captured response; no field is read.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or logs it; the shared transport codes are in [encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- `GridParamSettingController.setGridInfo` (`device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart @0x47c837c`; `settings/src/common/page/grid_param_setting/grid_param_setting_controller.dart @0x3a56fc0`) calling `updateCloudSetting` (`@0x47c84f0`; `@0x3a57130`): the grid parameter setting pages of the `device` and `settings` packages.
- `GridSettingLogic._setEnwgSwitch` (`charging/ui/page/device/main/sitation_energy_system/station_home_settings/advanced_setting/grid_setting_logic.dart @0x3fac850`), called from `onEnwg14aSwitchChanged`: the advanced grid setting page (package `charging`); the name suggests the German EnWG 14a switch.
- `GridProtectSettingController.saveProtectParam` (`settings/src/common/page/grid_param_setting/grid_protect_setting_controller.dart @0x3a59ff0`), called from `handleSave`: the grid protection setting page (package `settings`).

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 pool as a code-referenced URL; see the inventory row `since`). 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- What `is_push_device` 1 and 2 mean (probably "cloud only" and "also pushed to the device") is inferred; the semantics are not decoded.
- The full document structure sent by `updateCloudSetting` (built by the caller page) is not traced.
- Server behaviour is not known.

## Device-tested by

none
