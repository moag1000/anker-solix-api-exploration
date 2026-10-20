> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_scen_info

## Purpose

Reads the scene (energy-flow) document of a site: about 30 UI callers (A17C1 home, station energy system, AI-mode, backup power, dynamic price, share-site home center and others) go through four senders, `HttpRequestControllerImpl::querySceneInfo`, `A1782ChartHttpReposity::querySceneInfo`, `ElectricityCompanySelectLogic::querySceneInfo` and `EmsAiModeConditionLogic::_refreshSiteGridStatus`.

## Upstream name

`scene_info` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/site/get_scen_info` (asm-traced) at the senders that load a `Method` object next to the URL string (pool entry `pp+0xa7e0`, `Method.post`):

- `EmsAiModeConditionLogic::_refreshSiteGridStatus` (`ems_ai_mode_condition_logic.dart @0x2a306b8`): URL string `@0x2a30788`, method object `Method.post` (`pp+0xa7e0`) `@0x2a30780`.
- `HttpRequestControllerImpl::querySceneInfo` (`http_request_repository_impl.dart @0x23759e0`): URL string `@0x2375a94`, method object `Method.post` (`pp+0xa7e0`) `@0x2375a8c`.
- `A1782ChartHttpReposity::querySceneInfo` (`chart_http_repository.dart @0x23630a4`): URL string `@0x236315c`, method object `Method.post` (`pp+0xa7e0`) `@0x2363154`.
- `ElectricityCompanySelectLogic::querySceneInfo` (`electricty_company_select_logic.dart @0x29aa478`): URL string `@0x29aa54c`, method object `Method.post` (`pp+0xa7e0`) `@0x29aa544`.

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Every sender builds a 1-pair body with `site_id`.

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | yes |  | key `charging/http/http_request_repository_impl.dart @0x2375a38`; `HttpRequestControllerImpl::querySceneInfo` (`http_request_repository_impl.dart @0x23759e0`): map typed `<String, dynamic>` (`@0x2375a4c`), key `@0x2375a38`, store `@0x2375a48` (parameter at `fp-0x10`); `A1782ChartHttpReposity::querySceneInfo` (`chart_http_repository.dart @0x23630a4`): `<String, dynamic>` (`@0x2363114`), key `@0x2363100`, store `@0x2363110`; `ElectricityCompanySelectLogic::querySceneInfo` (`electricty_company_select_logic.dart @0x29aa478`): `<String, dynamic>` (`@0x29aa4dc`), key `@0x29aa4c8`, store `@0x29aa4d8`; the three map types give no value type and the callers (about 30) were not followed |
| `site_id` | string | yes | `"<site_id>"` | key `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a30720`; `EmsAiModeConditionLogic::_refreshSiteGridStatus` (`ems_ai_mode_condition_logic.dart @0x2a306b8`): map typed `<String, String>` (`@0x2a3073c`), key `@0x2a30720`, store `@0x2a30738` (`field_4b` of the logic object) |

## `param_type`/`cmd`

n/a

## Response model (link)

Per sender. `HttpRequestControllerImpl` and `A1782ChartHttpReposity`: `charging::SceneInfo` (`data/models.json` key; fields on [`models/energy.md`](../../../models/energy.md#sceneinfo)), parsed in the success closures `http_request_repository_impl.dart @0x2376064` and `chart_http_repository.dart @0x2363d68` (`SceneInfo.fromJson`, both calls resolve to `charging/model/green_energy/station/scene_info.dart`); the first then calls `setCurrentSolarName` and `setAllSiteInfo`. `ElectricityCompanySelectLogic`: `base_service::SceneInfoModel` (dedicated page [`models/scene_info_model.md`](../../../models/scene_info_model.md)), parsed in the closure `electricty_company_select_logic.dart @0x29aa590` (`SceneInfoModel.fromJson`). `EmsAiModeConditionLogic`: no model; its success closure `ems_ai_mode_condition_logic.dart @0x2a30834` reads the keys `grid_info`, `grid_list` and `power_site_type` and compares a product string with `"A17C5"`.

## Response

The keys are model-owned: see [`models/energy.md`](../../../models/energy.md#sceneinfo) for `charging::SceneInfo` and [`models/scene_info_model.md`](../../../models/scene_info_model.md) for `SceneInfoModel`; the AI-mode sender reads `grid_info`, `grid_list` and `power_site_type` only.

## Example request/response

Request, synthesized (decrypted body of the typed sender)

```json
{"site_id": "<site_id>"}
```

Response keys: see Response; no capture.

## Errors seen

None traced. The failure callbacks `ems_ai_mode_condition_logic.dart @0x2a307d0` (logs `"EmsAiModeConditionLogic: getSceneInfo fail "`) and the forwarding templates `charging/http/http_request_repository_impl.dart @0x2375ad8`, `charging/ui/page/device/a1782/station/station_main_page/chart/chart_http_repository.dart @0x2363d08`, `@0x226824c` compare no code. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart`: `_refreshSiteGridStatus` @0x2a306b8 (encryptionRequestHttp; encrypted: true)
- `charging/http/http_request_repository_impl.dart`: `querySceneInfo` @0x23759e0 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/a1782/station/station_main_page/chart/chart_http_repository.dart`: `querySceneInfo` @0x23630a4 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `electricity_price/components/dynamic_price/setting/electricty_company_select_logic.dart`: `querySceneInfo` @0x29aa478 (encryptionRequestHttp; encrypted: true)

Called from:

- `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart::onReady`
- `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart::refreshPagePurely`
- `charging/feature/backup_power/back_power_logic.dart::onReady`
- `charging/feature/utilitiy_rate_plan/dynamic_price/detail/dynamic_price_detail_logic.dart::getSiteInfo`
- `charging/feature/utilitiy_rate_plan/station_price_mode/station_price_mode_logic.dart::getSiteInfo`
- `charging/http/http_request_repository.dart::querySceneInfo`
- `charging/ui/page/device/a1782/station/add_devices/a1782_add_devices_logic.dart::getSiteInfo`
- `charging/ui/page/device/a1782/station/setting/power_station_setting_logic.dart::getSiteInfo`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::_queryStationInfo`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::addSiteDevice`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::getAiModeStatus`
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart::_ensureHomeLoadData`
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart::getSiteScenInfo`
- `charging/ui/page/device/a17c1/open_process/open_process_logic.dart::join`
- `charging/ui/page/device/a17c1/open_process/open_process_logic.dart::next`
- `charging/ui/page/device/a17c5/ai_mode_condition/ai_mode_condition_logic.dart::getSiteInfo`
- `charging/ui/page/device/connect/create_join_device_to_system/join_system/join_system_logic.dart::getScanInfoStationHome`
- `charging/ui/page/device/main/sitation_energy_mian/energy_home/controller/energy_home_controller.dart::getScanInfo`
- `charging/ui/page/device/main/sitation_energy_system/ai_mode_study/ai_mode_study_logic.dart::initModeData`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::getSiteInfo`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/add_devices/add_devices_logic.dart::getSiteInfo`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/add_devices/add_devices_logic.dart::manualInit`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/power_usage_scenario_logic.dart::initSceneInfo`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/station_home_settings_logic.dart::getSiteInfo`
- `charging/ui/page/device/main/station_device_home/station_main_page/station_main_page_logic.dart::quieryStationHomePage`
- `charging/ui/page/station/A17b1/a17b1_station_logic.dart::getStationScenceDetail`
- `charging/ui/page/user/share_site/home_center/home_center_logic.dart::checkCreateSiteProgressOpening`
- `electricity_price/components/dynamic_price/setting/electricty_company_select_logic.dart::getSceneInfoEnableAIEMS`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta. `charging::SceneInfo` and `base_service::SceneInfoModel` are `≤3.18.0` in `data/models.json`.

## Known unknowns

- Type of `site_id` in the three `<String, dynamic>` senders (parameters; about 30 callers). Header stays string-only. — attempted 2026-10-20 (two-hop not readable: about 30 callers pass the site id from Rx fields and parameters; not followed in this pass. Header stays string-only)
- Which `SceneInfo` class the AI-mode sender's callers use: it reads keys directly and builds no model. — traced 2026-10-20: not decoded in this pass (AI-mode sender callers); the reason given in the bullet stands
- The server rules behind `power_site_type` and the scene keys: not visible in the app.

## Device-tested by

none
