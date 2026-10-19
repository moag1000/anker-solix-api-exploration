> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_scen_info

## Purpose

<!-- TODO -->

## Upstream name

`scene_info` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/site/get_scen_info`, method: not extracted by the inventory <!-- TODO -->; string-only: `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a30788`
(literal also at 3 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a306b8` |

Rows are the union over 4 senders; `source` is the first sender that sets the key.

## `param_type`/`cmd`

n/a

## Response model (link)

<!-- TODO -->

## Response

<!-- TODO -->

## Example request/response

<!-- TODO -->

## Errors seen

`api/errors.md`: <!-- TODO -->

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

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
