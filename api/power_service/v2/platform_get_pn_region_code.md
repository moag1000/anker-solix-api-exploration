> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# platform_get_pn_region_code

## Purpose

Reads the list of region codes (countries with their states and grid codes) that a product supports; the grid selection pages use it to fill the country and grid-code pickers.

## Upstream name

`none` for the key; upstream lists the URL without a key in `api/apitypes.py` (line 346, comment "shows region codes per PN, but purpose unclear", body `{"product_code": "A5102"}`; upstream-confirmed for the key and the body).

## Method+URL

`POST /power_service/v2/platform_get_pn_region_code` (asm-traced). Two senders: `GridParamUtil.requestRegionCodes` (`base_service/view/grid/grid_param_util.dart @0x28f5f1c`; URL literal `@0x28f6080`, `Method.post` pool entry `pp+0xa7e0`) and the SDK closure inside `PowerPlantConfigController.requestRegionCodes` (`flutter_charging_beginning/beginning/state_cards/settings/power_plant_config_controller.dart @0x2b07c9c`; path literal `@0x2b07cfc`, method `"POST"` `@0x2b07d14`).

## Encrypted?

`requestRegionCodes`: `encryptionRequestHttp` (`base_service/view/grid/grid_param_util.dart`, no `needEncryption`, default `true`; [which calls are encrypted](../../encryption.md#which-calls-are-encrypted)); whether the call goes through the SDK is decided at run time. `PowerPlantConfigController` closure: direct SDK call, path C (`flutter_charging_beginning/beginning/state_cards/settings/power_plant_config_controller.dart @0x2b07d50`, identifier `akiot.cloud_api`).

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `product_code` | String | yes | `"A5102"` | `base_service/view/grid/grid_param_util.dart @0x28f5ff0` (map literal, one pair); value is the function argument. The SDK closure of `PowerPlantConfigController` sends a `param` map as well (`flutter_charging_beginning/beginning/state_cards/settings/power_plant_config_controller.dart @0x2b07d20`; keys not read) |

The example value is upstream's (`apitypes.py` line 346).

## `param_type`/`cmd`

n/a

## Response model (link)

`GridCodeModel` ([../../../models/grid_code_model.md](../../../models/grid_code_model.md)), `fromJson` called at `base_service/view/grid/grid_param_util.dart @0x28f649c` (success closure `@0x28f6464`) and at `flutter_charging_beginning/beginning/state_cards/settings/power_plant_config_controller.dart @0x2b07498`; the app also restores a cached copy with `GridCodeModel.fromJson` from storage (`base_service/utils/sp_helper.dart @0x2b080dc`, `charging/util/save/sp_util_impl.dart @0x2cbae14`).

## Response

All fields live in the model page (wrapper `code`, `msg`, `data` as in [encryption.md](../../encryption.md#response-handling-and-error-codes)).

## Example request/response

Request, synthesized

```json
{ "product_code": "A5102" }
```

Response: no captured response; the key list is on the model page.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or logs it; the shared transport codes are in [encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- `GridParamUtil.requestRegionCodes` (`base_service/view/grid/grid_param_util.dart @0x28f5f1c`), called from `choose_grid_view.dart` and `choose_grid_view_v2.dart` (`_fetchRegionCodes`), from `grid_setting_logic.dart` (`_getGridSetting`) and from both `grid_param_setting_controller.dart` copies (`device/src/station_setting/controller/common_grid_param/page/` and `settings/src/common/page/grid_param_setting/`; `onReady`): the grid pickers and the grid parameter setting pages.
- `PowerPlantConfigController.requestRegionCodes` (closure `flutter_charging_beginning/beginning/state_cards/settings/power_plant_config_controller.dart @0x2b07c9c`): the power plant config card of the initial setup flow.

## Since/changed

3.18.0: present (the URL string is in the 3.18.0 pool; its senders were in `power_plant_config_controller.dart`, `station_location_controller.dart` and `power_usage_scenario_controller.dart`, short names of the 3.18.0 tree, whose paths differ from 3.24.3). 3.24.3: present, now also through `GridParamUtil.requestRegionCodes`. since: ≤3.18.0.

## Known unknowns

- Server behaviour is not known beyond upstream's remark that the purpose is unclear.
- Whether the answer depends on the account region is not known.

## Device-tested by

none
