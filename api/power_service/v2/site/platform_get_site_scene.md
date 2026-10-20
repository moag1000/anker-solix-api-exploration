> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# platform_get_site_scene

## Purpose

Reads the scene (energy flow) information of a micro HES site: the app parses it into a `SceneInfoModel` with the solarbank, grid, diesel, smart plug and charging pile information and the feature switches.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /power_service/v2/site/platform_get_site_scene` (asm-traced): URL literal `@0x23485cc` in `BaseStationLogic._fetchSiteSceneByDio` (`micro_hes/src/a17e2/station/home/base_station_logic.dart @0x23484a8`), method object `Method.post` (pool entry `pp+0xa7e0`, `@0x23485c4`). The name says "by Dio"; the call goes through the normal wrapper.

## Encrypted?

Yes by wrapper (asm-traced): ``_fetchSiteSceneByDio`` calls `encryptionRequestHttp` (`micro_hes/src/a17e2/station/home/base_station_logic.dart @0x23485f4`) without passing `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../../../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../../../encryption.md)); asm alone does not decide it. `showLoading` is off (`r30 = false`, `@0x23485dc`).

## Request

Map literal with one string pair, `<String, String>` (`r2 = 4`, `@0x2348568`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | String | yes | `"<site id>"` | `micro_hes/src/a17e2/station/home/base_station_logic.dart @0x2348570`; value is the function argument stored at `@0x2348580` |

## `param_type`/`cmd`

n/a

## Response model (link)

`SceneInfoModel` ([../../../../models/scene_info_model.md](../../../../models/scene_info_model.md)), `fromJson` called at `micro_hes/src/a17e2/station/home/base_station_logic.dart @0x2348a88` inside `_parseSiteSceneV2` (`@0x2348720`).

## Response

Success closure `@0x23486b4` hands the payload to `_parseSiteSceneV2` (`micro_hes/src/a17e2/station/home/base_station_logic.dart @0x2348720`, call `@0x23486f4`) and completes the pending future with the result. `_parseSiteSceneV2` reads the key `data` (`@0x234891c`), copies the maps (`LinkedHashMap.from`, `@0x2348840`, `@0x2348a18`, `@0x2348a30`) and calls `SceneInfoModel.fromJson`; on a parse error it logs `解析 V2 场景数据失败` ("failed to parse V2 scene data", `@0x2348aa4`).

| field | type | required | example | source |
|---|---|---|---|---|
| `data` | map | yes | `{ "site_id": "...", ... }` | `micro_hes/src/a17e2/station/home/base_station_logic.dart @0x234891c`; the content is the `SceneInfoModel` document, keys on the model page |

Relation to the V1 scene endpoint [get_scen_info](../../site/get_scen_info.md) (from `data/models.json`): V1 parses `charging::SceneInfo` (45 top-level keys, the AI-mode and EMS senders use other classes), V2 parses `base_service::SceneInfoModel` (35 keys). Both take `site_id` and return the scene document. They share 14 top-level keys: `aiems_profit`, `charging_pile_info`, `custom_charging_type`, `ems_mode_power`, `error_code`, `feature_switch`, `grid_info`, `home_load_power`, `power_site_type`, `site_id`, `smart_plug_info`, `solarbank_info`, `style_id` and `switch_0w`; 31 keys occur only in `SceneInfo` (for example `statistics`, `site_info`, `solar_list`, `pps_info`, `powerpanel_list`) and 21 only in `SceneInfoModel` (for example `branch_list`, `diesel_info`, `hardware_info`, `off_grid_info`, `home_backup_system_info`, `ems_mode`, `function_switch`).

## Example request/response

Request, synthesized

```json
{ "site_id": "<site id>" }
```

Response: no captured response; the key list is on the model page.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or logs it; the shared transport codes are in [encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `BaseStationLogic._fetchSiteSceneByDio` (`micro_hes/src/a17e2/station/home/base_station_logic.dart @0x23484a8`), called at `@0x233c79c`: the station home of the micro HES (A17E2, package `micro_hes`).

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 pool as a code-referenced URL; see the inventory row `since`). 3.24.3: present (new). since: 3.24.3. `SceneInfoModel` exists in 3.18.0 but 3.24.3 added many keys (model page).

## Known unknowns

- Which keys of `SceneInfoModel` the V2 answer fills is not known.
- Server behaviour is not known.

## Device-tested by

none
