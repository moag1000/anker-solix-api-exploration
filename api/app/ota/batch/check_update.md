> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# check_update

## Purpose

<!-- TODO -->

## Upstream name

`get_ota_batch` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/app/ota/batch/check_update`, method: not extracted by the inventory <!-- TODO -->; string-only: `ats_ax170/src/ats_ax170/page/station/ax170_station_controller.dart @0x234de68`
(literal also at 8 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `path` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/firmware_upgrade/firmware_upgrade_controller.dart @0x2b0d200` |
| `method` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/firmware_upgrade/firmware_upgrade_controller.dart @0x2b0d200` |
| `param` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/firmware_upgrade/firmware_upgrade_controller.dart @0x2b0d200` |

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

- `ats_ax170/src/ats_ax170/page/station/ax170_station_controller.dart`: `checkDeviceUpdate` @0x234d650 (encryptionRequestHttp; encrypted: true)
- `base_service/util/firmware_update_utils.dart`: `checkBatchOTAUpdateWifi` @0x229e16c (encryptionRequestHttp; encrypted: true)
- `charging/http/http_request_repository_impl.dart`: `checkBatchOTAUpdateWifi` @0x264b354 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `device/src/station_setting/controller/common_station_firmware_update/station_firmware_update_view_model.dart`: `checkDeviceUpdate` @0x366ebb8 (encryptionRequestHttp; encrypted: true)
- `flutter_charging_beginning/beginning/state_cards/firmware_upgrade/firmware_upgrade_controller.dart`: `<anonymous closure> in FirmwareUpgradeController::checkDeviceUpdate` @0x2b0d200 (URL literal only, no `*Http*` call; sends in the same function (`AKIoTKitManagerImpl::handle`); resolved from the URL literal at `flutter_charging_beginning/beginning/state_cards/firmware_upgrade/firmware_upgrade_controller.dart @0x2b0d38c` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md)); `<anonymous closure> in FirmwareUpgradeController::checkUpgradeViaMultiDeploy` @0x2b0f898 (URL literal only, no `*Http*` call; sends in the same function (`AKIoTKitManagerImpl::handle`); resolved from the URL literal at `flutter_charging_beginning/beginning/state_cards/firmware_upgrade/firmware_upgrade_controller.dart @0x2b0fa14` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `micro_hes/src/a17e2/station/home/base_station_logic.dart`: `checkDeviceUpdate` @0x22c4c08 (encryptionRequestHttp; encrypted: true)
- `micro_hes/src/common_business/basic_station/basic_station_setting/component/general_setting/station_firmware_update_controller.dart`: `checkDeviceUpdate` @0x2cd17b8 (encryptionRequestHttp; encrypted: true)
- `micro_hes/src/common_business/basic_station/station/basic_station_logic.dart`: `checkDeviceUpdate` @0x235b830 (encryptionRequestHttp; encrypted: true)

Called from:

- `a1903/ota/combine_ota_check_logic.dart::checkAndShowUpdateDialog`
- `ats_ax170/src/ats_ax170/page/home/setting/menu_controller/ax170_firmware_version_rollback_controller.dart.dart::requestOTAStatus`
- `ats_ax170/src/ats_ax170/page/home/setting/menu_controller/firmware_update_controller.dart::requestOTAStatus`
- `ats_ax170/src/ats_ax170/page/station/ax170_station_controller.dart::updateBusinessMessages`
- `base_service/util/firmware_update_utils.dart::checkDeviceSettingFirmwareUpdate`
- `base_service/util/firmware_update_utils.dart::checkFirmwareUpdateDialog`
- `base_service/util/firmware_update_utils.dart::checkStationSettingFirmwareUpdate`
- `charging/http/http_request_repository.dart::checkBatchOTAUpdateWifi`
- `charging/impl/ems_station_service_impl.dart::checkBatchOTA`
- `charging/ui/page/device/a1782/a1782_setting/group_setting/a1782_group_setting_logic2.dart::getGroupOtaInfo`
- `charging/ui/page/device/a1782/station/setting/menu_controller/general/station_firmware_update_controller2.dart::getDeviceList`
- `charging/ui/page/device/a1790/batch_ota/device_pop_ota_manager.dart::checkGroupOta`
- `charging/ui/page/device/a1790/setting/group/a1790_setting_group_logic.dart::getGroupOtaInfo`
- `charging/ui/page/device/anker_ota/ats_ota/ats_ota_logic.dart::getOTAStatus`
- `charging/ui/page/device/anker_ota/batch_ota/batch_device_ota.dart::requestBateOta`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::toDeviceUpdatePage`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/add_devices_progress/add_devices_progress_logic.dart::checkBatchOTA`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/station_home_settings_logic.dart::getDeviceList`
- `device/src/station_setting/controller/common_station_firmware_update/station_firmware_update_controller.dart::didPopNext`
- `device/src/station_setting/controller/common_station_firmware_update/station_firmware_update_controller.dart::onInit`
- `device/src/station_setting/controller/common_station_firmware_update/station_firmware_update_view_model.dart::onInit`
- `flutter_charging_beginning/beginning/state_cards/firmware_upgrade/firmware_upgrade_controller.dart::checkATSOtaDeviceUpdate`
- `micro_hes/src/a17e2/station/home/base_station_logic.dart::updateBusinessMessages`
- `micro_hes/src/common_business/basic_station/basic_station_setting/component/general_setting/station_firmware_update_controller.dart::onInit`
- `micro_hes/src/common_business/basic_station/basic_station_setting/component/general_setting/station_firmware_update_controller.dart::onTapMenu`
- `micro_hes/src/common_business/basic_station/station/basic_station_logic.dart::updateBusinessMessages`
- `oe_a7320/src/oe_a7320/ota/range_extender_system_ota.dart::jumpToBatchOtaView`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
