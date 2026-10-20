> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# device_command

## Purpose

Sends a system setting command of an A5101 site (35 caller functions in the settings pages, among them `setAdvancedConfig`, `remoteResetCls`, `handlerDeviceCommandScreenTime`, `handlerDeviceCommandOfMode`, `handlerDeviceCommandOfPeckShaving`, `setDiesel`, `setHeatPumpConfig`, `sendPeakValleyData`); two senders were read, the generic `HttpRequestControllerImpl::sendDeviceCommand` and `FixedRateLogic::savePlanPrice` (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/device_command` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x24a0e54`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x24a0e4c`, in `HttpRequestControllerImpl::sendDeviceCommand` (`charging/http/http_request_repository_impl.dart @0x24a0aa8`), sent through `requestHttp` (`@0x24a0e7c`).

Same URL and method object in the other sender(s) read:

- `FixedRateLogic::savePlanPrice` (`charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278dc40`): URL string `@0x278e1bc`, method object `Method.post` (`pp+0xa7e0`) at `@0x278e1b4`, sent through `requestHttp` (`@0x278e1e4`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::sendDeviceCommand` (`charging/http/http_request_repository_impl.dart`, call `@0x24a0e7c`, argument list `@0x24a0e74`), `FixedRateLogic::savePlanPrice` (`charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart`, call `@0x278e1e4`, argument list `@0x278e1dc`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

Two senders. In the generic sender `station_id` is `field_7` of the `StationMainPageLogic` value (load `charging/http/http_request_repository_impl.dart @0x24a0b4c`, fallback `""` `@0x24a0b5c`): `StationMainPageLogic` holds an `Rx<StationModel>` (`charging/ui/page/device/main/station_device_home/station_main_page/station_main_page_logic.dart @0x22597b0`, stored `@0x22597cc`); `StationModel.field_7` is declared `String?` (cast `r8 = String?` `@0x238e858`, store `@0x238e870` in `base_service/ak_iot_kit/business/basic/model/station_model.dart`, key `site_id` `@0x238e808`), so it is a String. `HttpRequestControllerImpl::sendDeviceCommand` (`@0x24a0aa8`) stores 15 keys in one map literal with type arguments `<String, dynamic>` (`@0x24a0e0c`), which do not type the values; the values come from parameters (the stack reads `@0x24a0b94`..`@0x24a0dd0`), except the constants `accuracy` (`r16 = 10` `@0x24a0d6c`, a tagged immediate, so the Smi 5), `version` (`"1.0.0"` `@0x24a0e00`) and `ack_peak_valley` (the null constant `@0x24a0cec`). `FixedRateLogic::savePlanPrice` (`charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278dc40`) builds a nested body with a `<String, Object>` literal (`@0x278dfa0`): the rate plan with one `peak_sessions` entry holding one `peak_valley_prices` entry; the integers there are tagged immediates (raw 2 is Smi 1, raw 4 is Smi 2, raw 0 is the zero register), the strings are constants, and `electricity_strategy.mode` is only added when the named parameter `electricityMode` is non-null (`cmp w0, NULL` `@0x278e0f8`). Rows with the file of the second sender are the `savePlanPrice` rows; rows listing two addresses give the key and the value.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | string (generic sender); ? (`savePlanPrice`) | yes | `"<station_id>"` | `charging/http/http_request_repository_impl.dart @0x24a0b84`; `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278dcb0` |
| `main_sn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x24a0b98`; `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278dccc` |
| `time` | ? | yes | the parameter, else the result of `getCurrentTime` | `charging/http/http_request_repository_impl.dart @0x24a0bac`; `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278dce4` |
| `electricity_strategy` | ? (generic sender); object (`savePlanPrice`, a map with the key `mode`) | yes (generic sender); optional (`savePlanPrice`, guard `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278e0f8`) | ? | `charging/http/http_request_repository_impl.dart @0x24a0c00`; `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278e144` |
| `add_diesel` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x24a0c38` |
| `screen_setting` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x24a0c70` |
| `utility_rate_plan` | ? (generic sender); object (`savePlanPrice`, a map with the list `peak_sessions`) | yes | ? | `charging/http/http_request_repository_impl.dart @0x24a0ca8`; `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278dd20` |
| `ack_peak_valley` | ? | yes | `null` (constant null stored, no parameter) | `charging/http/http_request_repository_impl.dart @0x24a0ce0` |
| `advanced_setting` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x24a0cf0` |
| `heat_pump_setting` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x24a0d28` |
| `accuracy` | int (Smi, w) | yes | `5` | `charging/http/http_request_repository_impl.dart @0x24a0d60` |
| `cls_reset` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x24a0d74` |
| `off_grid_switching` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x24a0d84` |
| `evcharger_setting` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x24a0dbc` |
| `version` | string | yes | `"1.0.0"` | `charging/http/http_request_repository_impl.dart @0x24a0df4`; `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278e168` |
| `utility_rate_plan.peak_sessions` | list | yes | one element | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278dd3c`; `@0x278dfd0` |
| `utility_rate_plan.peak_sessions[].id` | int (Smi, w) | yes | `0` | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278dd58` |
| `utility_rate_plan.peak_sessions[].name` | string | yes | `"session1"` | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278dd68`; `@0x278dd70` |
| `utility_rate_plan.peak_sessions[].start_time` | string | yes | `"<year>-01-01 00:00:00"` (year from `getCurrentYear`) | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278dd7c`; `@0x278dda8` |
| `utility_rate_plan.peak_sessions[].end_time` | string | yes | `"<year>-12-01 00:00:00"` (year from `getCurrentYear`) | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278dde8`; `@0x278de14` |
| `utility_rate_plan.peak_sessions[].type` | int (Smi, w) | yes | `1` | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278de54` |
| `utility_rate_plan.peak_sessions[].peak_valley_prices` | list | yes | one element | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278de64`; `@0x278dfd0` |
| `utility_rate_plan.peak_sessions[].peak_valley_prices[].id` | int (Smi, w) | yes | `0` | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278de80` |
| `utility_rate_plan.peak_sessions[].peak_valley_prices[].buy` | ? | yes | result of a `parse` call | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278de90`; `@0x278deb4` |
| `utility_rate_plan.peak_sessions[].peak_valley_prices[].sell` | ? | yes | result of a `parse` call | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278dee4`; `@0x278df00` |
| `utility_rate_plan.peak_sessions[].peak_valley_prices[].energy_unit` | string | yes | `"/kWh"` | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278df30`; `@0x278df3c` |
| `utility_rate_plan.peak_sessions[].peak_valley_prices[].start_time_period` | string | yes | `"00:00"` | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278df48`; `@0x278df54` |
| `utility_rate_plan.peak_sessions[].peak_valley_prices[].end_time_period` | string | yes | `"00:00"` | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278df60`; `@0x278df6c` |
| `utility_rate_plan.peak_sessions[].peak_valley_prices[].peak_type` | int (Smi, w) | yes | `1` | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278df78` |
| `utility_rate_plan.peak_sessions[].peak_valley_prices[].day_type` | int (Smi, w) | yes | `2` | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278df8c` |
| `electricity_strategy.mode` | int (width not read) | optional | ? | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278e10c` |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the senders (asm-traced): the success closure of `sendDeviceCommand` (`charging/http/http_request_repository_impl.dart @0x24044f0`) calls the stored callback with the unchanged response (`ClosureCall` `@0x240452c`); the success closure of `savePlanPrice` is the folded closure `charging/ui/page/device/greenpower/recharge/select_pps/select_pps_logic.dart @0x278e200`, which calls `GetNavigation.back` with `result: true` (`@0x278e24c`). The models behind the answers are those of `get_device_command` (`A5101DeviceCommandModel`).

## Response

No response key is read in the senders.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "main_sn": "<main_sn>",
  "time": "<time>",
  "electricity_strategy": "<value or null>",
  "add_diesel": "<value or null>",
  "screen_setting": "<value or null>",
  "utility_rate_plan": "<value or null>",
  "ack_peak_valley": null,
  "advanced_setting": "<value or null>",
  "heat_pump_setting": "<value or null>",
  "accuracy": 5,
  "cls_reset": "<value or null>",
  "off_grid_switching": "<value or null>",
  "evcharger_setting": "<value or null>",
  "version": "1.0.0"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `base_service/api_url.dart`: `sendDeviceCommand` @0x249e524 (URL literal only, no `*Http*` call; sender `TouHttpService::sendDeviceCommand` (`electricity_price/components/tou/impl_v2/service/tou_http_service.dart @0x4884e40`), reached through callers `TouHttpService::sendDeviceCommand` (`electricity_price/components/tou/impl_v2/service/tou_http_service.dart @0x4884e40`); other senders: `ElectricityUsageHelper::setSiteTOUDetail`; resolved from the URL literal at `base_service/api_url.dart @0x249e53c` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `charging/http/http_request_repository_impl.dart`: `sendDeviceCommand` @0x24a0aa8 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart`: `savePlanPrice` @0x278dc40 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/util/demosite_util_impl.dart`: `DemoSiteUtilImpl` @0x4a33a6c (URL literal only, no `*Http*` call; no sender within 3 caller levels)

Called from:

- `charging/boostrap_impl.dart::DIInit`
- `charging/http/http_request_repository.dart::sendDeviceCommand`
- `charging/ui/page/device/a5101/setting/advanced_config/advanced_config_logic.dart::setAdvancedConfig`
- `charging/ui/page/device/a5101/setting/bluetooth_control/bleTest/peak_valley_test/peak_valley_test_logic.dart::sendDeviceCommondOfNetWork`
- `charging/ui/page/device/a5101/setting/cls_setting/cls_setting_logic.dart::remoteResetCls`
- `charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart::addHeatPump`
- `charging/ui/page/device/a5101/setting/device_manager/ev_charger/ev_charger_manager_logic.dart::handleIsAllowChargerSwitch`
- `charging/ui/page/device/a5101/setting/device_manager/ev_charger/ev_charger_manager_logic.dart::setChargeState`
- `charging/ui/page/device/a5101/setting/device_manager/heat_pump/controller.dart::setHeatPumpConfig`
- `charging/ui/page/device/a5101/setting/device_manager/heat_pump/timer_setting/timer_setting_logic.dart::cloudSynchronizationData`
- `charging/ui/page/device/a5101/setting/device_manager/oil_engine/manage_devices_logic.dart::setDiesel`
- `charging/ui/page/device/a5101/setting/device_manager/oil_engine/manage_devices_logic.dart::setDieselNearby`
- `charging/ui/page/device/a5101/setting/device_manager/oil_engine/manage_devices_logic.dart::setNearbyOilTwoSetting`
- `charging/ui/page/device/a5101/setting/device_manager/oil_engine/manage_devices_logic.dart::setRemoteOilTwoSetting`
- `charging/ui/page/device/a5101/setting/grid_sensitivity/a5101_grid_sensitivity_logic.dart::_syncData`
- `charging/ui/page/device/a5101/setting/screen_timeout/screen_timeout_logic.dart::handlerDeviceCommandRadarSwitch`
- `charging/ui/page/device/a5101/setting/screen_timeout/screen_timeout_logic.dart::handlerDeviceCommandScreenSwitch`
- `charging/ui/page/device/a5101/setting/screen_timeout/screen_timeout_logic.dart::handlerDeviceCommandScreenTime`
- `charging/ui/page/device/a5101/setting/screen_timeout/screen_timeout_logic.dart::setRadarControl`
- `charging/ui/page/device/a5101/setting/screen_timeout/screen_timeout_logic.dart::setScreenBrightnessControl`
- `charging/ui/page/device/a5101/setting/screen_timeout/screen_timeout_logic.dart::setScreenSwitch`
- `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::handlerDeviceCommandOfAutoDisaster`
- `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::handlerDeviceCommandOfConservepercent`
- `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::handlerDeviceCommandOfGridRecharging`
- `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::handlerDeviceCommandOfManualBackupPower`
- `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::handlerDeviceCommandOfMode`
- `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::handlerDeviceCommandOfPeckShaving`
- `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::handlerHesToCharger`
- `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::sendDeviceCommandWithDebounce`
- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart::deleteData`
- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart::onMessageDispatch`
- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart::sendDeviceCommandOfMode`
- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart::sendDeviceCommondOfNetWork`
- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart::sendPeakValleyData`
- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_plan/nem_rate_plan_logic.dart::sendPeakValleyData`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The types of the 13 parameter-valued keys of the generic sender: the map is `<String, dynamic>`; the typed shapes are in `models/hes.md#a5101devicecommandmodel` (Full SET request), which this page does not re-state.
- Which keys a given caller sets: the generic sender stores every key and the callers pass `null` for the ones they do not change; this was not decoded per caller.
- The types of `buy` and `sell` in `savePlanPrice`: they are results of `parse` calls (`charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x278deb4`, `@0x278df00`) on text fields.
- `ack_peak_valley` is always sent as null by this sender (`charging/http/http_request_repository_impl.dart @0x24a0cec`); whether the server needs the key was not tested.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
