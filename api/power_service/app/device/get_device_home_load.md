> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_device_home_load

## Purpose

<!-- TODO -->

## Upstream name

`get_device_load` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/app/device/get_device_home_load`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x262c194`
(literal also at 11 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x262c0b0` |
| `param_type` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x262c0b0` |
| `device_pn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x262c0b0` |
| `site_id` | ? | ? | ? | `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart @0x2c49144` |
| `accuracy` | ? | ? | ? | `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart @0x2c49144` |

Rows are the union over 6 senders; `source` is the first sender that sets the key.

## `param_type`/`cmd`

see `api/param_types.md`

param_type is a variable at this sender (traced by heuristic — verify against the callers in `data/param_types.json`).

## Response model (link)

<!-- TODO -->

## Response

<!-- TODO -->

## Example request/response

<!-- TODO -->

## Errors seen

`api/errors.md`: <!-- TODO -->

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `get17C1DeviceHomeLoadPort` @0x262c0b0 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`); `getDeviceHomeLoadPort` @0x2674420 (encryptionRequestHttp; encrypted: true); `getDeviceHomeLoadRes` @0x274a794 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart`: `<anonymous closure> in ElectricityUsageHelper::getCurEmsModeType` @0x292e774 (URL literal only, no `*Http*` call; no sender within 3 caller levels); `<anonymous closure> in ElectricityUsageHelper::getManualSetTOUDetailWithUrl` @0x2c4fdfc (URL literal only, no `*Http*` call; no sender within 3 caller levels); `assembleRemoteApiParametersWidthGetDetail` @0x2c4f694 (URL literal only, no `*Http*` call; no sender within 3 caller levels); `getCurEmsModeType` @0x292e1f4 (encryptionRequestHttp; encrypted: true); `getElectricityUsagePolicyUrl` @0x292e5e8 (URL literal only, no `*Http*` call; sender found through callers: `ElectricityUsageHelper::getCurEmsModeType` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x292e1f4`) via `ElectricityUsageHelper::getCurEmsModeType` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x292e1f4`))
- `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart`: `<anonymous closure> in TOUPlanLogic::getDataFromAPi` @0x2c49658 (URL literal only, no `*Http*` call; no sender within 3 caller levels); `getDataFromAPi` @0x2c49144 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/tou/impl_v2/service/tou_http_service.dart`: `getDeviceHomeLoad` @0x4878c74 (request; encrypted: default-true (requestHttp) — verify, param_type/cmd: see `api/param_types.md`)
- `ev_charger/src/ev_charger/page/home/a5190_home_logic.dart`: `_fetchDeviceStationInfo` @0x3504e80 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::get17C1DeviceHomeLoadPort`
- `charging/http/http_request_repository.dart::getDeviceHomeLoadPort`
- `charging/http/http_request_repository.dart::getDeviceHomeLoadRes`
- `charging/ui/page/device/a17c0/a17c0SwitchMode/a17c0_switch_mode_logic.dart::deviceConnect`
- `charging/ui/page/device/a17c0/a17c0energyPlan/a17c0energy_plan_logic.dart::getDeviceHomeLoadData`
- `charging/ui/page/device/a17c0/a17c0home/a17c0home_logic.dart::getDeviceHomeLoad`
- `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart::onInit`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::_preloadHomeLoadData`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::getDeviceHomeLoad`
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart::_ensureHomeLoadData`
- `charging/ui/page/device/a17c1/energy_plan/energy_plan_logic.dart::getHomeLoadSiteParam`
- `charging/ui/page/device/a17x7/a17x7home/a17x7home_logic.dart::_fetchDeviceStationInfo`
- `charging/ui/page/device/a17x8/a17x8home/a17x8home_logic.dart::_fetchDeviceStationInfo`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/merge_system_energy/merge_system_energy_plan_logic.dart::getHomeLoadSiteParam`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/power_usage_scenario_logic.dart::getHomeLoadDeviceParam`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::detectionDeviceJoinSystem`
- `electricity_price/components/electricity_module/electricity_price_serviceImpl.dart::getCurEmsModeType`
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart::getCurEmsModeType`
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart::getManualSetTOUDetail`
- `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart::parserRouterInfo`
- `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart::updateData`
- `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart::onReady`
- `electricity_price/components/tou/impl_v2/repository/charging_pile_tou_repository.dart::getTouDetail`
- `ev_charger/src/ev_charger/page/home/a5190_home_logic.dart::onInit`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
