> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# device_command

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/device_command`, method: not extracted by the inventory <!-- TODO -->; string-only: `base_service/api_url.dart @0x249e53c`
(literal also at 3 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x24a0aa8` |
| `main_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x24a0aa8` |
| `time` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x24a0aa8` |
| `electricity_strategy` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x24a0aa8` |
| `add_diesel` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x24a0aa8` |
| `screen_setting` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x24a0aa8` |
| `utility_rate_plan` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x24a0aa8` |
| `ack_peak_valley` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x24a0aa8` |
| `advanced_setting` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x24a0aa8` |
| `heat_pump_setting` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x24a0aa8` |
| `accuracy` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x24a0aa8` |
| `cls_reset` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x24a0aa8` |
| `off_grid_switching` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x24a0aa8` |
| `evcharger_setting` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x24a0aa8` |
| `version` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x24a0aa8` |
| `id` | ? | ? | ? | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278dc40` |
| `buy` | ? | ? | ? | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278dc40` |
| `sell` | ? | ? | ? | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278dc40` |
| `energy_unit` | ? | ? | ? | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278dc40` |
| `start_time_period` | ? | ? | ? | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278dc40` |
| `end_time_period` | ? | ? | ? | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278dc40` |
| `peak_type` | ? | ? | ? | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278dc40` |
| `day_type` | ? | ? | ? | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278dc40` |
| `mode` | ? | ? | ? | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278dc40` |

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

- `base_service/api_url.dart`: `sendDeviceCommand` @0x249e524 (URL literal only, no `*Http*` call)
- `charging/http/http_request_repository_impl.dart`: `sendDeviceCommand` @0x24a0aa8 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart`: `savePlanPrice` @0x278dc40 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/util/demosite_util_impl.dart`: `DemoSiteUtilImpl` @0x4a33a6c (URL literal only, no `*Http*` call)

Called from: `charging/boostrap_impl.dart::DIInit`, `charging/http/http_request_repository.dart::sendDeviceCommand`, `charging/ui/page/device/a5101/setting/advanced_config/advanced_config_logic.dart::setAdvancedConfig`, `charging/ui/page/device/a5101/setting/bluetooth_control/bleTest/peak_valley_test/peak_valley_test_logic.dart::sendDeviceCommondOfNetWork`, `charging/ui/page/device/a5101/setting/cls_setting/cls_setting_logic.dart::remoteResetCls`, `charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart::addHeatPump`, `charging/ui/page/device/a5101/setting/device_manager/ev_charger/ev_charger_manager_logic.dart::handleIsAllowChargerSwitch`, `charging/ui/page/device/a5101/setting/device_manager/ev_charger/ev_charger_manager_logic.dart::setChargeState`, `charging/ui/page/device/a5101/setting/device_manager/heat_pump/controller.dart::setHeatPumpConfig`, `charging/ui/page/device/a5101/setting/device_manager/heat_pump/timer_setting/timer_setting_logic.dart::cloudSynchronizationData`, `charging/ui/page/device/a5101/setting/device_manager/oil_engine/manage_devices_logic.dart::setDiesel`, `charging/ui/page/device/a5101/setting/device_manager/oil_engine/manage_devices_logic.dart::setDieselNearby`, `charging/ui/page/device/a5101/setting/device_manager/oil_engine/manage_devices_logic.dart::setNearbyOilTwoSetting`, `charging/ui/page/device/a5101/setting/device_manager/oil_engine/manage_devices_logic.dart::setRemoteOilTwoSetting`, `charging/ui/page/device/a5101/setting/grid_sensitivity/a5101_grid_sensitivity_logic.dart::_syncData`, `charging/ui/page/device/a5101/setting/screen_timeout/screen_timeout_logic.dart::handlerDeviceCommandRadarSwitch`, `charging/ui/page/device/a5101/setting/screen_timeout/screen_timeout_logic.dart::handlerDeviceCommandScreenSwitch`, `charging/ui/page/device/a5101/setting/screen_timeout/screen_timeout_logic.dart::handlerDeviceCommandScreenTime`, `charging/ui/page/device/a5101/setting/screen_timeout/screen_timeout_logic.dart::setRadarControl`, `charging/ui/page/device/a5101/setting/screen_timeout/screen_timeout_logic.dart::setScreenBrightnessControl`, `charging/ui/page/device/a5101/setting/screen_timeout/screen_timeout_logic.dart::setScreenSwitch`, `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::handlerDeviceCommandOfAutoDisaster`, `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::handlerDeviceCommandOfConservepercent`, `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::handlerDeviceCommandOfGridRecharging`, `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::handlerDeviceCommandOfManualBackupPower`, `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::handlerDeviceCommandOfMode`, `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::handlerDeviceCommandOfPeckShaving`, `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::handlerHesToCharger`, `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::sendDeviceCommandWithDebounce`, `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart::deleteData`, `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart::onMessageDispatch`, `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart::sendDeviceCommandOfMode`, `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart::sendDeviceCommondOfNetWork`, `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart::sendPeakValleyData`, `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_plan/nem_rate_plan_logic.dart::sendPeakValleyData`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
