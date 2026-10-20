> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_device_attrs

## Purpose

Reads named device attributes (power limit, time zone, price type, feed-grid and load-port settings, PV names, TOU data) for many settings pages; 25 senders share this URL (callers e.g. `PowerUsageScenarioController::getDeviceTimezoneWithCallback`, `AS200HomeLogic::onReady`, `CustomBranchController::onInit`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`get_device_attributes` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/device/get_device_attrs` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x239edb4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x239edac`, in `HttpRequestControllerImpl::getDeviceAttrs` (`charging/http/http_request_repository_impl.dart @0x239ec40`), sent through `encryptionRequestHttp` (`@0x239eddc`).

Same URL and method object in the other sender(s) read:

- `POST /power_service/v1/app/device/get_device_attrs` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x238410c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2384104`, in `HttpRequestControllerImpl::getDeviceAttrsInfo` (`charging/http/http_request_repository_impl.dart @0x2384088`), sent through `encryptionRequestHttp` (`@0x2384134`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) 25 senders were found for this URL in `tools/out/request_fields_all.json`; the two senders of `HttpRequestControllerImpl` were read. `getDeviceAttrs` (`charging/http/http_request_repository_impl.dart @0x239ec40`) stores `device_sn` and `attributes` (both parameters) in a `<String, Object>` literal (`@0x239ecfc`), then adds `supports` = `{"enable_0w_v2": <parameter>}` (`<String, bool>` literal `@0x239ed40`) only when its first parameter is not null (`cmp w0, NULL` `@0x239ed18`). `getDeviceAttrsInfo` (`@0x2384088`) sends the two keys with the body passed in as a parameter. The other 23 senders (`TimezoneUtil::getDeviceTimezone`, `PPSTouHttpService::getTouElectricAttrs`, `AS200HomeLogic::_getLowLoadAutoShutdownTimeout`, `AKIotAX170Command::getCustomBranchList`, `ElectricityUsageHelper::getPriceType`, `TOUPlanLogic::getDataFromAPi`, `GeneralPriceSettingLogic`, `ScheduleNetwork::_getDeviceAttrs`, `A17EXElectricityPriceLogic::_fetchDeviceCurrency`, the feed-grid, load-port and PV-name helpers and others) send the same two keys `device_sn` and `attributes` in `<String, Object>`, `<String, Object?>` or `<String, dynamic>` literals; `TOUPlanLogic` and `GeneralPriceSettingLogic::getDevicePriceType` add keys such as `site_id`, `accuracy`, `station_id`, `not_include_nem`, `currency`.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x239ecd4` |
| `attributes` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x239ece8` |
| `supports` | object (`Map<String, bool>`) | optional (first parameter not null, guard `@0x239ed18`) | `{"enable_0w_v2": true}` | `charging/http/http_request_repository_impl.dart @0x239ed68` (key `enable_0w_v2` at `@0x239ed2c`; the value is a parameter of type `bool` by the `<String, bool>` literal) |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`DevicePowerLimit`](../../../../models/power.md#devicepowerlimit), parsed by `DevicePowerLimit.fromJson` at `charging/http/http_request_repository_impl.dart @0x239eee8`. Model of the `getDeviceAttrs` sender.
- [`DeviceAttributes`](../../../../models/other.md#deviceattributes), parsed by `DeviceAttributes.fromJson` at `charging/http/http_request_repository_impl.dart @0x2384254`. Model of the `getDeviceAttrsInfo` sender (the key `charging::DeviceAttributes`). Other senders parse `DeviceAttributesModel` (`settings::DeviceAttributesModel`), `SolarNameModel`, `LoadPortConfig`, `BranchCircuitModel`, `PriceSmartStatusModel` and `EmsModeModel`; their closures were not read.

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `DevicePowerLimit` top-level keys (`data/models.json`, `charging::DevicePowerLimit`): `device_sn` (String?), `attributes` (Attributes?).
- `DeviceAttributes` top-level keys (`data/models.json`, `charging::DeviceAttributes`): `attributes` (Attributes?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<?>",
  "attributes": "<?>",
  "supports": {
    "enable_0w_v2": true
  }
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `ak_soft_ems/util/timezone_util.dart`: `getDeviceTimezone` @0x22ba090 (URL literal only, no `*Http*` call; sender `HttpHelper::getDataFromService` (`ak_soft_ems/http/http_helper.dart @0x22ba2bc`) (HTTP helper wrapper), called from the same function; resolved from the URL literal at `ak_soft_ems/util/timezone_util.dart @0x22ba254` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart`: `getTouElectricAttrs` @0x2a3ebd0 (encryptionRequestHttp; encrypted: true)
- `as200/src/page/home/as200_home_logic.dart`: `_getLowLoadAutoShutdownTimeout` @0x29f088c (encryptionRequestHttp; encrypted: true)
- `ats_ax170/src/sdk/command/ax170_command.dart`: `getCustomBranchList` @0x27d664c (URL literal only, no `*Http*` call; sends in the same function (`AKIoTKitManagerImpl::handle`); resolved from the URL literal at `ats_ax170/src/sdk/command/ax170_command.dart @0x27d66a4` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `charging/http/http_request_repository_impl.dart`: `getDeviceAttrs` @0x239ec40 (encryptionRequestHttp; encrypted: true); `getDeviceAttrsInfo` @0x2384088 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart`: `<anonymous closure> in ElectricityUsageHelper::getPriceType` @0x35f72e8 (URL literal only, no `*Http*` call; sends in the same function (`HttpServiceImpl::encryptionRequestHttp`); resolved from the URL literal at `electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x35f7420` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md)); `getPriceType` @0x35f70c8 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/electricity_price_common/tou_auto_preview/tou_auto_price_pkg_result_logic.dart`: `_getDevicePriceUnit` @0x31acd90 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart`: `getDataFromAPi` @0x2c49144 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart`: `<anonymous closure> in GeneralPriceSettingLogic::getDevicePriceType` @0x29a4e04 (URL literal only, no `*Http*` call; sends in the same function (`HttpServiceImpl::encryptionRequestHttp`); resolved from the URL literal at `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a5064` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md)); `_getDevicePriceUnit` @0x2a799d0 (encryptionRequestHttp; encrypted: true); `getDevicePriceType` @0x29a4974 (encryptionRequestHttp; encrypted: true); `getPriceTypeUrl` @0x29a4d20 (URL literal only, no `*Http*` call; sender `GeneralPriceSettingLogic::getDevicePriceType` (`electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a4974`), reached through callers `GeneralPriceSettingLogic::getDevicePriceType` (`electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a4974`); resolved from the URL literal at `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a4d44` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `ev_charger/src/ev_charger/page/home/schedule_charge/network/%20schedule_network.dart`: `_getDeviceAttrs` @0x2851084 (_requestHttp; encrypted: default-true (requestHttp) — verify)
- `micro_hes/src/a17ex/home/components/electricity_price/a17ex_electricity_price_logic.dart`: `_fetchDeviceCurrency` @0x35fe644 (encryptionRequestHttp; encrypted: true)
- `micro_hes/src/common_business/basic_station/module/system_flow/common/energy_system_cover_helper.dart`: `getSolarPvNameMode` @0x2c8d5a0 (encryptionRequestHttp; encrypted: true)
- `settings/src/common/menu_controller/equipment_feed_power_menu_controller.dart`: `getMenuVisible` @0x3691b40 (encryptionRequestHttp; encrypted: true)
- `settings/src/common/menu_controller/feed_grid_menu_controller.dart`: `getMenuVisible` @0x367a224 (encryptionRequestHttp; encrypted: true)
- `settings/src/common/page/feed_grid/feed_grid_controller.dart`: `getDeviceAttrs` @0x2aed8b0 (encryptionRequestHttp; encrypted: true)
- `settings/src/common/page/hardware_feed_grid/hardware_feed_grid_controller.dart`: `getDeviceAttrs` @0x2aeb688 (encryptionRequestHttp; encrypted: true)
- `settings/src/common/page/load_port_setting/load_port_settings_controller.dart`: `getLoadPortConfig` @0x2af7c04 (encryptionRequestHttp; encrypted: true); `getLoadPortName` @0x2af9188 (encryptionRequestHttp; encrypted: true)
- `settings/src/sdk/util/load_port_util.dart`: `updateLoadPortSetting` @0x3291ac0 (encryptionRequestHttp; encrypted: true)
- `settings/src/service/site_settings_service_impl.dart`: `_getDeviceFeedAttributes` @0x3515784 (encryptionRequestHttp; encrypted: true)

Called from:

- `ak_soft_ems/ems_list/power_usage_scenario_controller.dart::getDeviceTimezoneWithCallback`
- `ak_soft_ems/manual_power_backup/manual_power_backup_logic.dart::getTimeZone`
- `ak_soft_pps_ems/src/modules/setting/modules_setting_logic.dart::getTouElectricAttrsFn`
- `as200/src/page/home/as200_home_logic.dart::onReady`
- `ats_ax170/src/ats_ax170/branch_circuit/pages/custom_branch/custom_branch_controller.dart::onInit`
- `charging/ble/device/anker_device_delegate_impl.dart::a17C1JumpToBleSuccessPage`
- `charging/common_bussiness/currency/app_currency_process_list_controller.dart::getDeciceGetCurrency`
- `charging/feature/backup_power/back_power_logic.dart::getTimeZone`
- `charging/http/http_request_repository.dart::getDeviceAttrs`
- `charging/http/http_request_repository.dart::getDeviceAttrsInfo`
- `charging/ui/page/device/a1782/module_list/modules_logic.dart::getTouElectricAttrsFn`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::_preloadDeviceAttrs`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::getMicorLimitData`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::getWifiSignal`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::onInit`
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart::_updateGridConnectedInput`
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart::getPowerLimitList`
- `charging/ui/page/device/a17x7/a17x7home/a17x7home_logic.dart::getWifiSignal`
- `charging/ui/page/device/a17x8/a17x8home/a17x8home_logic.dart::_getTimingLimit`
- `charging/ui/page/device/a17x8/a17x8home/a17x8home_logic.dart::getWifiSignal`
- `charging/ui/page/device/a17x8/a17x8scene_start/a17x8scene_start_logic.dart::getLocationTagList`
- `charging/ui/page/device/a17x8/space_setup/space_setup_controller.dart::getList`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::getSiteInfo`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/power_usage_scenario_logic.dart::getTimeZone`
- `electricity_price/components/electricity_module/electricity_price_serviceImpl.dart::getPriceType`
- `electricity_price/components/electricity_price_common/tou_auto_preview/tou_auto_price_pkg_result_logic.dart::goToReSelectPlan`
- `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart::parserRouterInfo`
- `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart::updateData`
- `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart::changePriceType`
- `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart::getDevicePriceType`
- `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart::onReady`
- `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart::setFixedPriceV2`
- `ev_charger/src/ev_charger/page/home/schedule_charge/network/%20schedule_network.dart::_getAllDeviceAttrs`
- `micro_hes/src/a17e2/home/a17e2_home_controller.dart::toggleOffGridSwitch`
- `micro_hes/src/a17e2/station/home/base_station_logic.dart::getDeviceTimezoneWithCallback`
- `micro_hes/src/a17e2/station/home/base_station_logic.dart::refreshDeviceTimezone`
- `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart::homeLoadSwitchChanged`
- `micro_hes/src/a17ex/home/components/electricity_price/a17ex_electricity_price_logic.dart::_initializeDeviceIfAvailable`
- `micro_hes/src/common_business/basic_station/dialog/multiple_pv_data.dart::_requestSolarPvNames`
- `settings/src/common/menu_controller/equipment_feed_power_menu_controller.dart::onInit`
- `settings/src/common/menu_controller/feed_grid_menu_controller.dart::onInit`
- `settings/src/common/page/feed_grid/feed_grid_controller.dart::onReady`
- `settings/src/common/page/hardware_feed_grid/hardware_feed_grid_controller.dart::onReady`
- `settings/src/common/page/load_port_setting/load_port_settings_controller.dart::switchPort`
- `settings/src/service/site_settings_service_impl.dart::_sendDefaultParameters`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `device_sn` and `attributes`: parameters or fields in every sender, with `<String, Object>`/`<String, dynamic>` literals; senders with a `<String, String>` outer literal do not exist for this URL.
- Which attribute names each sender requests (`attributes` is a list in most senders and a parameter in others) and which names the server knows (upstream `get_device_attributes` lists some).
- The 23 senders other than the two `HttpRequestControllerImpl` ones: bodies and response parsing were not decoded (see Request).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
