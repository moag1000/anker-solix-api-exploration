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

- The relation between this V2 endpoint and the V1 site scene (`get_scen_info`) is not documented here.
- Which keys of `SceneInfoModel` the V2 answer fills is not known.
- Server behaviour is not known.

## Device-tested by

none
