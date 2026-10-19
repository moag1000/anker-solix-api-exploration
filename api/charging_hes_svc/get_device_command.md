> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_device_command

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/get_device_command`, method: not extracted by the inventory <!-- TODO -->; string-only: `ak_soft_ems/http/ems_api.dart @0x2a31630`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x277caa0` |
| `accuracy` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x277caa0` |

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

- `ak_soft_ems/http/ems_api.dart`: `getDeviceCommand` @0x2a31618 (URL literal only, no `*Http*` call)
- `charging/http/http_request_repository_impl.dart`: `getDeviceCommand` @0x277caa0 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getDeviceCommand`
- `charging/ui/page/device/a5101/setting/advanced_config/advanced_config_logic.dart::getAdvancedConfigStateFromCloud`
- `charging/ui/page/device/a5101/setting/bluetooth_control/bleTest/peak_valley_test/peak_valley_test_logic.dart::onReady`
- `charging/ui/page/device/a5101/setting/cls_setting/cls_setting_logic.dart::_getCLSState`
- `charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart::getDeviceData`
- `charging/ui/page/device/a5101/setting/device_manager/ev_charger/ev_charger_manager_logic.dart::_getData`
- `charging/ui/page/device/a5101/setting/device_manager/oil_engine/manage_devices_logic.dart::_getData`
- `charging/ui/page/device/a5101/setting/grid_sensitivity/a5101_grid_sensitivity_logic.dart::_getOffGridState`
- `charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart::_getCLSState`
- `charging/ui/page/device/a5101/setting/screen_timeout/screen_timeout_logic.dart::getRadarAndScreenConfig`
- `charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart::_getSmartModeAuthorizationStatus`
- `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::_getSystemPolicySetting`
- `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::_updateRemainingChargeTime`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
