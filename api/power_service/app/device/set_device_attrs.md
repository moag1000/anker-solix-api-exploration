> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# set_device_attrs

## Purpose

<!-- TODO -->

## Upstream name

`set_device_attributes` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/app/device/set_device_attrs`, method: not extracted by the inventory <!-- TODO -->; string-only: `ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart @0x27e3cc4`
(literal also at 26 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Some senders wrap these keys in `param_data` as a JSON string (`jsonEncode`); outer keys: `attributes`, `device_sn`.

| field | type | required | example | source |
|---|---|---|---|---|
| `pps_use_time` | ? | ? | ? | `ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart @0x27e3af8` |
| `path` | ? | ? | ? | `ats_ax170/src/sdk/command/ax170_command.dart @0x2f2cd4c` |
| `method` | ? | ? | ? | `ats_ax170/src/sdk/command/ax170_command.dart @0x2f2cd4c` |
| `param.device_sn` | ? | ? | ? | `ats_ax170/src/sdk/command/ax170_command.dart @0x2f2cd4c` |
| `param.attributes.custom_branch.custom_branches` | ? | ? | ? | `ats_ax170/src/sdk/command/ax170_command.dart @0x2f2cd4c` |
| `param.attributes.custom_branch.third_party_pv_connect_status` | ? | ? | ? | `ats_ax170/src/sdk/command/ax170_command.dart @0x2f2cd4c` |
| `param.attributes.custom_branch.third_party_diesel_connect_status` | ? | ? | ? | `ats_ax170/src/sdk/command/ax170_command.dart @0x2f2cd4c` |
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x2624ed8` |
| `attributes.currency` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x2624ed8` |
| `attributes.switch_0w` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3d90a90` |
| `init_status` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x2703b6c` |
| `attributes` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x2276948` |
| `attributes.pv_power_limit` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3d97864` |
| `attributes.tag` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x386ae3c` |
| `device_pn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x42b8c80` |
| `attributes.ac_power_limit` | ? | ? | ? | `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d91390` |
| `attributes.price_type` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `attributes.fixed_price` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `site_id` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `price` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `site_price_unit` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `price_type` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `site_co2` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `accuracy` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `id` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `buy` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `sell` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `energy_unit` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `start_time_period` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `end_time_period` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `peak_type` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `day_type` | ? | ? | ? | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x41a7afc` |
| `attributes.feed_setting` | ? | ? | ? | `settings/src/common/page/feed_grid/feed_grid_controller.dart @0x2283f70` |
| `attributes.hardware_anti_backflow_config` | ? | ? | ? | `settings/src/common/page/hardware_feed_grid/hardware_feed_grid_controller.dart @0x2aebd24` |
| `attributes.load_port_setting` | ? | ? | ? | `settings/src/common/page/load_port_setting/load_port_settings_controller.dart @0x2e889f4` |
| `attributes.load_port_name` | ? | ? | ? | `settings/src/common/page/load_port_setting/load_port_settings_controller.dart @0x3a68038` |

Rows are the union over 25 senders; `source` is the first sender that sets the key.

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

- `ak_soft_pps_ems/src/modules/pps_tou/service/pps_tou_http_service.dart`: `setTouElectricAttrs` @0x27e3af8 (encryptionRequestHttp; encrypted: true)
- `ats_ax170/src/sdk/command/ax170_command.dart`: `setCustomBranchList` @0x2f2cd4c (URL literal only, no `*Http*` call; sends in the same function (SDK `handle`))
- `charging/http/http_request_repository_impl.dart`: `getCurrencySetDeviceAttrs` @0x2624ed8 (encryptionRequestHttp; encrypted: true); `setDeviceAttrsInfo` @0x386acd0 (encryptionRequestHttp; encrypted: true); `setDeviceFeedGridSwitch` @0x3d90a90 (encryptionRequestHttp; encrypted: true); `setDeviceGameStatus` @0x2703b6c (encryptionRequestHttp; encrypted: true); `setDevicePowerOptionsReq` @0x2276948 (encryptionRequestHttp; encrypted: true); `setDevicePvPowerOptionsReq` @0x3d97864 (encryptionRequestHttp; encrypted: true); `setLocationTag` @0x386ae3c (encryptionRequestHttp; encrypted: true); `setPpsSolarName` @0x42b8c80 (encryptionRequestHttp; encrypted: true); `setSolarName` @0x307aea4 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart`: `setGridConnectedInput` @0x3d91390 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/station_power_limit/station_power_limit_logic.dart`: `_setDevicePowerLimit` @0x4356240 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/electricity_price_common/electricity_usage_helper.dart`: `getSaveDeviceEMSPrice` @0x249e420 (URL literal only, no `*Http*` call; sender found through callers: `ElectricityUsageHelper::setDeviceEMSPriceArgument` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x249e2cc`) via `ElectricityUsageHelper::setDeviceEMSPriceArgument` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x249e2cc`))
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

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
