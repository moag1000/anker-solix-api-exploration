> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# set_device_attrs

## Purpose

Writes named device attributes (TOU plan, feed-grid and load-port settings, device currency/price, PV names, game status, location tag, power options) for many settings pages; 27 senders share this URL (callers e.g. `PPSTouHttpService::clearTouPlan`, `TouSettingLogic::opreateTouPlanAsync`, `CustomBranchController::syncIotCommand`, `LoginHandler::_reportDeviceGameStatus`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`set_device_attributes` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/device/set_device_attrs` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x2276a6c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2276a64`, in `HttpRequestControllerImpl::setDevicePowerOptionsReq` (`charging/http/http_request_repository_impl.dart @0x2276948`), sent through `encryptionRequestHttp` (`@0x2276a8c`).

Same URL and method object in the other sender(s) read:

- `POST /power_service/v1/app/device/set_device_attrs` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x386ad50`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x386ad48`, in `HttpRequestControllerImpl::setDeviceAttrsInfo` (`charging/http/http_request_repository_impl.dart @0x386acd0`), sent through `encryptionRequestHttp` (`@0x386ad78`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) 27 senders were found for this URL; two `HttpRequestControllerImpl` senders were read. `setDevicePowerOptionsReq` (`charging/http/http_request_repository_impl.dart @0x2276948`) builds `{device_sn, attributes}` in a `<String, Object>` literal (`@0x2276a20`; raw `r2 = 8` at `@0x22769f0`) whose `attributes` value is an inner literal `<String, int>` (`@0x2276994`), so that sender writes integer attribute values. `setDeviceAttrsInfo` (`@0x386acd0`) receives the body as parameters (`device_sn` from a field, `attributes` from a literal in the caller). Most other senders use the same two keys with an inner `attributes` literal of type `<String, int>`, `<String, String>` or `<String, Object>`; `GeneralPriceSettingLogic::setFixedPrice` adds `site_id`, `price`, `site_price_unit`, `price_type = "fixed"`, `site_co2`, `accuracy`, `sell_price` and `peak_sessions`; `setSolarName` sets `device_pn = "A17C5"`; `AKIotAX170Command::setCustomBranchList` sends the command map with `path`, `method = "POST"` and `param`.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x22769f8` |
| `attributes` | object (`Map`); value type per sender | yes | `{"<name>": <value>}` | `charging/http/http_request_repository_impl.dart @0x2276a0c` (this sender: inner `<String, int>` `@0x2276994`) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed in the builders read (asm-traced): both pass forwarding closures (`@0x2268374` style) that hand the response object to the caller; no `fromJson` or response key is read in them.

## Response

Not read in the builders read.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<?>",
  "attributes": {
    "<attribute name>": "<value>"
  }
}
```

Response: not synthesized (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart`: `setTouElectricAttrs` @0x27e3af8 (encryptionRequestHttp; encrypted: true)
- `ats_ax170/src/sdk/command/ax170_command.dart`: `setCustomBranchList` @0x2f2cd4c (URL literal only, no `*Http*` call; sends in the same function (`AKIoTKitManagerImpl::handle`); resolved from the URL literal at `ats_ax170/src/sdk/command/ax170_command.dart @0x2f2ce74` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `charging/http/http_request_repository_impl.dart`: `getCurrencySetDeviceAttrs` @0x2624ed8 (encryptionRequestHttp; encrypted: true); `setDeviceAttrsInfo` @0x386acd0 (encryptionRequestHttp; encrypted: true); `setDeviceFeedGridSwitch` @0x3d90a90 (encryptionRequestHttp; encrypted: true); `setDeviceGameStatus` @0x2703b6c (encryptionRequestHttp; encrypted: true); `setDevicePowerOptionsReq` @0x2276948 (encryptionRequestHttp; encrypted: true); `setDevicePvPowerOptionsReq` @0x3d97864 (encryptionRequestHttp; encrypted: true); `setLocationTag` @0x386ae3c (encryptionRequestHttp; encrypted: true); `setPpsSolarName` @0x42b8c80 (encryptionRequestHttp; encrypted: true); `setSolarName` @0x307aea4 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart`: `setGridConnectedInput` @0x3d91390 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/station_power_limit/station_power_limit_logic.dart`: `_setDevicePowerLimit` @0x4356240 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart`: `getSaveDeviceEMSPrice` @0x249e420 (URL literal only, no `*Http*` call; sender `ElectricityUsageHelper::setDeviceEMSPriceArgument` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x249e2cc`), reached through callers `ElectricityUsageHelper::setDeviceEMSPriceArgument` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x249e2cc`); resolved from the URL literal at `electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x249e4c4` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart`: `setFixedPrice` @0x41a7afc (encryptionRequestHttp; encrypted: true); `setTOU` @0x41a68ac (encryptionRequestHttp; encrypted: true)
- `ev_charger/src/ev_charger/page/home/schedule_charge/network/%20schedule_network.dart`: `_setDeviceAttrs` @0x3968464 (_requestHttp; encrypted: default-true (requestHttp) — verify)
- `micro_hes/src/a17ex/home/components/electricity_price/a17ex_electricity_price_logic.dart`: `_saveCurrencyThenPrice` @0x39cd088 (encryptionRequestHttp; encrypted: true)
- `micro_hes/src/common_business/basic_station/module/system_flow/common/energy_system_cover_helper.dart`: `editPvName` @0x32b02b4 (encryptionRequestHttp; encrypted: true)
- `settings/src/common/page/feed_grid/feed_grid_controller.dart`: `<anonymous closure> in FeedGridController::updateByDevice` @0x2283f70 (encryptionRequestHttp; encrypted: true)
- `settings/src/common/page/hardware_feed_grid/hardware_feed_grid_controller.dart`: `<anonymous closure> in HardwareFeedGridController::updateByDevice` @0x2aebd24 (encryptionRequestHttp; encrypted: true)
- `settings/src/common/page/load_port_setting/load_port_settings_controller.dart`: `updateLoadPortConfig` @0x2e889f4 (encryptionRequestHttp; encrypted: true); `updateLoadPortName` @0x3a68038 (encryptionRequestHttp; encrypted: true)
- `settings/src/common/page/timing_setting/timing_setting_controller.dart`: `_updateTimingToCloud` @0x35151b4 (encryptionRequestHttp; encrypted: true)
- `settings/src/sdk/util/grid_connect_util.dart`: `syncDeviceInputPower` @0x3514ee4 (encryptionRequestHttp; encrypted: true)
- `settings/src/sdk/util/load_port_util.dart`: `<anonymous closure>@0x3291c54` @0x3291c54 (encryptionRequestHttp; encrypted: true)
- `station_home/src/ui/shared/node_dialog/dialog_widget/pv_dialog_helper.dart`: `editSolarPvName` @0x3328374 (request; encrypted: default-true (requestHttp) — verify)

Called from:

- `ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart::clearTouPlan`
- `ak_soft_pps_ems/src/modules/pps_tou/ui/tou_price_preview/pps_tou_price_detail_preview_logic.dart::opreateTouPlanAsync`
- `ak_soft_pps_ems/src/modules/pps_tou/ui/tou_setting/tou_setting_logic.dart::opreateTouPlanAsync`
- `ats_ax170/src/ats_ax170/branch_circuit/pages/custom_branch/custom_branch_controller.dart::syncIotCommand`
- `ats_ax170/src/ats_ax170/branch_circuit/pages/custom_branch/custom_branch_controller.dart::syncToCloud`
- `charging/account/handlers/login_handler.dart::_reportDeviceGameStatus`
- `charging/common_bussiness/currency/app_currency_process_list_controller.dart::getAppDeciceSetCurrency`
- `charging/http/http_request_repository.dart::getCurrencySetDeviceAttrs`
- `charging/http/http_request_repository.dart::reportDeviceGameStatus`
- `charging/http/http_request_repository.dart::setDeviceAttrsInfo`
- `charging/http/http_request_repository.dart::setDeviceFeedGridSwitch`
- `charging/http/http_request_repository.dart::setDevicePowerOptionsReq`
- `charging/http/http_request_repository.dart::setDevicePvPowerOptionsReq`
- `charging/http/http_request_repository.dart::setLocationTag`
- `charging/http/http_request_repository.dart::setPpsSolarName`
- `charging/http/http_request_repository.dart::setSolarName`
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart::setDevicePvPowerLimit`
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart::setFeedGridValue`
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart::setPowerLimit`
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart::showGridConnectedInputPicker`
- `charging/ui/page/device/a17x8/a17x8scene_start/a17x8scene_start_logic.dart::setLocationTags`
- `charging/ui/page/device/a17x8/space_setup/space_setup_controller.dart::saveDeviceInfo`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::sendCommand`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::setSolarBankName`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::setSolarBankPpsName`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/station_power_limit/station_power_limit_logic.dart::showPowerLimitPicker`
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart::setDeviceEMSPriceArgument`
- `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart::build`
- `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart::setFixedPriceV2`
- `ev_charger/src/ev_charger/page/home/schedule_charge/network/%20schedule_network.dart::closeSmartCharging`
- `ev_charger/src/ev_charger/page/home/schedule_charge/network/%20schedule_network.dart::setOnlySmartCharging`
- `micro_hes/src/a17ex/home/components/electricity_price/a17ex_electricity_price_logic.dart::savePrice`
- `micro_hes/src/common_business/basic_station/module/system_flow/common/energy_system_cover_helper.dart::showEditPvNameDialog`
- `settings/src/common/page/grid_connected_settings/grid_connected_settings_controller.dart::setPowerByMqtt`
- `settings/src/common/page/load_port_setting/load_port_settings_controller.dart::autoStartTapped`
- `settings/src/common/page/load_port_setting/load_port_settings_controller.dart::changeToManual`
- `settings/src/common/page/load_port_setting/load_port_settings_controller.dart::manualControlTapped`
- `settings/src/common/page/load_port_setting/load_port_settings_controller.dart::smartSchedulingTapped`
- `settings/src/common/page/load_port_setting/load_port_settings_controller.dart::timeScheduleTapped`
- `settings/src/common/page/load_port_setting/load_port_settings_page.dart::_showRenameDialog`
- `settings/src/common/page/timing_setting/timing_setting_controller.dart::sendTimingToDeviceThenCloud`
- `settings/src/service/site_settings_service_impl.dart::_sendBleCommand`
- `station_home/src/ui/shared/node_dialog/dialog_widget/pv_dialog_helper.dart::<anonymous closure>@0x33282a4`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. Param delta in `tools/out/diff_3.18.0_3.24.3.md`: 3.24.3 added the attribute names `attributes.feed_setting`, `attributes.hardware_anti_backflow_config`, `attributes.load_port_name` and `attributes.load_port_setting` (feed-grid and load-port controllers) and the literals ` salePrice.value.isEmpty:` and `fixedPrice.value.isEmpty:` (price pages; their use was not decoded).

## Known unknowns

- Types of `device_sn` (parameter, field or constant depending on the sender) and the attribute value types of each sender (see Request); `<String, Object>` only says non-null.
- Which attribute names the server accepts: the senders give many names, none was decoded to a complete list here; upstream `set_device_attributes` documents some.
- The 25 senders not read in detail: bodies and the response handling were not decoded.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
