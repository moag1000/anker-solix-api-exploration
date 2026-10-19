> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# set_device_home_load

## Purpose

<!-- TODO -->

## Upstream name

`set_device_load` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/app/device/set_device_home_load`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x2631510`
(literal also at 5 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x26313ac` |
| `mode_type` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x26313ac` |
| `custom_rate_plan` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x26313ac` |
| `home_load_data` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x26313ac` |

Rows are the union over 2 senders; `source` is the first sender that sets the key.

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

- `charging/http/http_request_repository_impl.dart`: `postCloudSiteOrDeviceEms` @0x3d8864c (encryptionRequestHttp; encrypted: true); `set17C1DeviceHomeLoadRes` @0x26313ac (encryptionRequestHttp; encrypted: true); `setDeviceHomeLoadRes` @0x274a458 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart`: `getSetElectricityUsagePolicyUrl` @0x31b9e50 (URL literal only, no `*Http*` call; sender found through callers: `TOUEditPreviewLogic::savePlan` (`electricity_price/components/tou/page/tou_detail/view/tou_edit_preview_logic.dart @0x31de7dc`) via `ElectricityUsageHelper::setManualSetTOUDetail` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x31b8da8`) -> `TOUEditPreviewLogic::savePlan` (`electricity_price/components/tou/page/tou_detail/view/tou_edit_preview_logic.dart @0x31de7dc`); also `TOUPlanLogic::savePlan`); `setManualSetTOUDetail` @0x31b8da8 (URL literal only, no `*Http*` call; sender found through callers: `TOUEditPreviewLogic::savePlan` (`electricity_price/components/tou/page/tou_detail/view/tou_edit_preview_logic.dart @0x31de7dc`) via `TOUEditPreviewLogic::savePlan` (`electricity_price/components/tou/page/tou_detail/view/tou_edit_preview_logic.dart @0x31de7dc`); also `TOUPlanLogic::savePlan`)
- `electricity_price/components/tou/impl_v2/service/tou_http_service.dart`: `setDeviceHomeLoad` @0x4882f10 (request; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/feature/backup_power/back_power_logic.dart::onDoneClick`
- `charging/feature/peak_valley/confirm/confirm_peak_valley_logic.dart::onDoneClick`
- `charging/http/http_request_repository.dart::postCloudSiteOrDeviceEms`
- `charging/http/http_request_repository.dart::set17C1DeviceHomeLoadRes`
- `charging/http/http_request_repository.dart::setDeviceHomeLoadRes`
- `charging/ui/page/device/a1782/station/system_policy/a1782_system_policy_logic.dart::setMode`
- `charging/ui/page/device/a17c0/a17c0energyPlan/a17c0energy_plan_logic.dart::setDeviceHomeLoadData`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::_dealWithBleResponse`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::closeBackPower`
- `charging/ui/page/device/a17c1/energy_deploy/energy_deploy_logic.dart::saveHomeLoadData`
- `charging/ui/page/device/a17c1/energy_plan/energy_plan_logic.dart::deleteHomeLoadData`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::closeBackPower`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/merge_system_energy/merge_system_energy_plan_logic.dart::deleteHomeLoadData`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/ae100/custom_mode_usage_scenario_logic.dart::showModeUpgradeDialog`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/ae100/detail/custom_mode_usage_scenario_detail_logic.dart::_saveToDeviceAndCloud`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/power_usage_scenario_logic.dart::closeBackPower`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/power_usage_scenario_logic.dart::setHomeLoadSiteParam`
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart::setManualSetTOUDetail`
- `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart::savePlan`
- `electricity_price/components/tou/impl_v2/repository/charging_pile_tou_repository.dart::saveTouPlan`
- `electricity_price/components/tou/page/tou_detail/view/tou_edit_preview_logic.dart::saveMode`
- `electricity_price/components/tou/page/tou_detail/view/tou_edit_preview_logic.dart::savePlan`
- `electricity_price/components/tou/page/tou_result_view/tou_result/tou_result_logic.dart::_cyclePowerResultCallback`
- `electricity_price/components/tou/page/tou_result_view/tou_result/tou_result_logic.dart::saveMode`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
