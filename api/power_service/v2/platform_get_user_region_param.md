> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# platform_get_user_region_param

## Purpose

Reads the grid code (grid standard) settings of a product for the user: the country, the grid code and its name, the enabled parameters and the advanced parameter template and values, used by the grid parameter setting pages.

## Upstream name

`none` for the key; upstream lists the URL without a key in `api/apitypes.py` (line 351).

## Method+URL

`POST /power_service/v2/platform_get_user_region_param` (asm-traced). Senders: `GridParamSettingController.getGridSetting` in the `device` package (`device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart @0x2a4f638`; URL literal `@0x2a4f8ac`, `Method.post` pool entry `pp+0xa7e0`, `@0x2a4f8a4`) and in the `settings` package (`settings/src/common/page/grid_param_setting/grid_param_setting_controller.dart @0x29e4b8c`; URL `@0x29e4e00`), `GridSettingLogic._getGridSetting` (`charging/ui/page/device/main/sitation_energy_system/station_home_settings/advanced_setting/grid_setting_logic.dart @0x28f5bb8`; URL `@0x28f5cf8`), and, as direct SDK closures, `SystemConfigController.updateCountryCodeByCloud` (`flutter_charging_beginning/beginning/state_cards/settings/system_config/system_config_controller.dart`, closure `@0x3256434`) and the pickers `showGridPicker` (`device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart @0x390d94c`, `settings/src/common/page/grid_param_setting/grid_param_setting_controller.dart @0x3a58b94`).

## Encrypted?

`getGridSetting` (both packages) and `_getGridSetting`: `encryptionRequestHttp` (`device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart @0x2a4f8d0`, `charging/ui/page/device/main/sitation_energy_system/station_home_settings/advanced_setting/grid_setting_logic.dart @0x28f5d1c`; no `needEncryption`, default `true`; [which calls are encrypted](../../encryption.md#which-calls-are-encrypted)); whether the call goes through the SDK is decided at run time. The `system_config_controller` closure is a direct SDK call (path C, identifier `akiot.cloud_api`). The `showGridPicker` closures were not read.

## Request

`GridParamSettingController.getGridSetting` builds a map literal with six pairs, `<String, Object?>` (`r2 = 24`, `@0x2a4f79c`):

| field | type | required | example | source |
|---|---|---|---|---|
| `product_code` | String | yes | `"A5102"` | `device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart @0x2a4f7a4`; value is a controller argument stored at `@0x2a4f7b4` (example from upstream's note on the sibling endpoint `platform_get_pn_region_code`) |
| `identifier_id` | String | yes | `"<device or site id>"` | `@0x2a4f7b8`; value stored at `@0x2a4f7c8`, empty string literal as default (`r1 = ""`, `@0x2a4f744`) |
| `scenario_type` | int | yes | `1` or `2` | `@0x2a4f7cc`; value is computed from a boolean argument: `csetm`, `and #2`, `add #2` (`@0x2a4f7e4` to `@0x2a4f7ec`), which yields tagged Smi 2 when the boolean is true and tagged Smi 1 when it is false (raw 4 and raw 2; the arithmetic runs on the tagged representation, so decoded 2 / 1) |
| `grid_code_name` | String? | no | `"VDE-AR-N 4105"` | `@0x2a4f7f4`; field at offset 0x13 of the selected grid object (`@0x2a4f788`), null if no object; example is illustrative |
| `country_code` | String? | no | `"DE"` | `@0x2a4f808`; field at offset 0x1b of the same object (`@0x2a4f76c`) |
| `grid_code` | String? | no | `"<grid code>"` | `@0x2a4f81c`; field at offset 0xf of the object (`@0x2a4f83c`) |

The `settings` copy has the same keys (`product_code` `@0x29e4cf8`, `identifier_id` `@0x29e4d0c`, `scenario_type` `@0x29e4d20`, `grid_code_name` `@0x29e4d48`, `country_code` `@0x29e4d5c`, `grid_code` `@0x29e4d70`). `GridSettingLogic._getGridSetting` copies a base map (field at offset 0x93, `LinkedHashMap.of` `@0x28f5bf4`) and sets `grid_code_name` (`@0x28f5c30`), `country_code` (`@0x28f5c68`) and `grid_code` (`@0x28f5ca0`) from its selected grid object; the content of the base map was not traced. The `system_config_controller` closure sends `path`, `method`, `param` through the SDK (param keys not read).

## `param_type`/`cmd`

n/a

## Response model (link)

`GridParamSettingInfo` ([../../../models/grid_param_setting_info.md](../../../models/grid_param_setting_info.md)), `fromJson` called at `device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart @0x2a4f934`, `settings/src/common/page/grid_param_setting/grid_param_setting_controller.dart @0x29e4e88`, `charging/ui/page/device/main/sitation_energy_system/station_home_settings/advanced_setting/grid_setting_logic.dart @0x28f5d80` (and in the picker closures `device ... @0x390df1c`, `settings ... @0x3a58ef8`).

## Response

All fields live in the model page (wrapper `code`, `msg`, `data` as in [encryption.md](../../encryption.md#response-handling-and-error-codes)).

## Example request/response

Request, synthesized

```json
{ "product_code": "A5102", "identifier_id": "<device or site id>", "scenario_type": 1,
  "grid_code_name": "<grid code name>", "country_code": "DE", "grid_code": "<grid code>" }
```

Response: no captured response; the key list is on the model page.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or logs it; the shared transport codes are in [encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- `GridParamSettingController.getGridSetting` (`device/src/station_setting/controller/common_grid_param/page/grid_param_setting_controller.dart @0x2a4f638`; `settings/src/common/page/grid_param_setting/grid_param_setting_controller.dart @0x29e4b8c`), called from `onReady`, `_watchGridCode` and `showGridPicker` of both controllers: the grid parameter setting page of the `device` (station setting) and `settings` packages.
- `GridSettingLogic._getGridSetting` (`charging/ui/page/device/main/sitation_energy_system/station_home_settings/advanced_setting/grid_setting_logic.dart @0x28f5bb8`), called from `onReady`: the advanced grid setting page of the station home settings (package `charging`).
- `SystemConfigController.updateCountryCodeByCloud` (closure `@0x3256434`): the system config card of the initial setup flow (`flutter_charging_beginning`).

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 pool as a code-referenced URL; see the inventory row `since`). 3.24.3: present (new). since: 3.24.3. `GridParamSettingInfo` is new in 3.24.3 (model page).

## Known unknowns

- What `scenario_type` 1 and 2 mean is not decoded.
- Which other keys the `system_config_controller` and picker senders send is not read.
- The content of the base map used by `_getGridSetting` is not traced.
- Server behaviour is not known.

## Device-tested by

none
