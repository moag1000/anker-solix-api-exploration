> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# check_update

## Purpose

Asks the server which of a list of devices (the station and its sub-devices) have a firmware update; sent by the firmware update pages of the stations (`FirmwareUpdateUtils::checkBatchOTAUpdateWifi`, `StationFirmwareUpdateViewModel::checkDeviceUpdate`, `BaseStationLogic`/`BasicStationLogic::checkDeviceUpdate`, `AX170StationController::checkDeviceUpdate`, `FirmwareUpgradeController` and others in the caller chain of `data/endpoints.json`) (asm-traced).

## Upstream name

`get_ota_batch` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /app/ota/batch/check_update` (asm-traced): URL string at `ats_ax170/src/ats_ax170/page/station/ax170_station_controller.dart @0x234de68`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x234de60`, in `AX170StationController::checkDeviceUpdate` (`ats_ax170/src/ats_ax170/page/station/ax170_station_controller.dart @0x234d650`), sent through `encryptionRequestHttp` (`@0x234de90`).

Same URL in the other sender(s) read:

- `POST /app/ota/batch/check_update` (asm-traced): URL string at `base_service/util/firmware_update_utils.dart @0x229e364`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x229e35c`, in `FirmwareUpdateUtils::checkBatchOTAUpdateWifi` (`base_service/util/firmware_update_utils.dart @0x229e16c`), sent through `encryptionRequestHttp` (`@0x229e394`).
- `POST /app/ota/batch/check_update` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x264b510`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x264b508`, in `HttpRequestControllerImpl::checkBatchOTAUpdateWifi` (`charging/http/http_request_repository_impl.dart @0x264b354`), sent through `requestHttp` (`@0x264b540`).
- `POST /app/ota/batch/check_update` (asm-traced): URL string at `device/src/station_setting/controller/common_station_firmware_update/station_firmware_update_view_model.dart @0x366f8c4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x366f8bc`, in `StationFirmwareUpdateViewModel::checkDeviceUpdate` (`device/src/station_setting/controller/common_station_firmware_update/station_firmware_update_view_model.dart @0x366ebb8`), sent through `encryptionRequestHttp` (`@0x366f8ec`).
- `POST /app/ota/batch/check_update` (asm-traced): URL string at `micro_hes/src/a17e2/station/home/base_station_logic.dart @0x22c544c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x22c5444`, in `BaseStationLogic::checkDeviceUpdate` (`micro_hes/src/a17e2/station/home/base_station_logic.dart @0x22c4c08`), sent through `encryptionRequestHttp` (`@0x22c5474`).
- `POST /app/ota/batch/check_update` (asm-traced): URL string at `micro_hes/src/common_business/basic_station/basic_station_setting/component/general_setting/station_firmware_update_controller.dart @0x2cd20c4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2cd20bc`, in `StationFirmwareUpdateController::checkDeviceUpdate` (`micro_hes/src/common_business/basic_station/basic_station_setting/component/general_setting/station_firmware_update_controller.dart @0x2cd17b8`), sent through `encryptionRequestHttp` (`@0x2cd20ec`).
- `POST /app/ota/batch/check_update` (asm-traced): URL string at `micro_hes/src/common_business/basic_station/station/basic_station_logic.dart @0x235c060`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x235c058`, in `BasicStationLogic::checkDeviceUpdate` (`micro_hes/src/common_business/basic_station/station/basic_station_logic.dart @0x235b830`), sent through `encryptionRequestHttp` (`@0x235c088`).

Two more senders go through the SDK handler instead of the Dart wrappers: the closures in `FirmwareUpgradeController::checkDeviceUpdate` (`flutter_charging_beginning/beginning/state_cards/firmware_upgrade/firmware_upgrade_controller.dart @0x2b0d200`) and `::checkUpgradeViaMultiDeploy` (`@0x2b0f898`) build the map `{path, method, param}` with `path` `/app/ota/batch/check_update` (`@0x2b0d38c`, `@0x2b0fa14`), `method` the constant string `"POST"` (`@0x2b0d3a4`, `@0x2b0fa28`) and `param` the `toJson` result (`@0x2b0d3cc`, `@0x2b0fa40`) and call `handle` of the handler `akiot.cloud_api` (`@0x2b0d410`, `@0x2b0d420`). The same closures send `/charging_hes_installer_svc/v2/ota/batch/check_update` with a `LinkedHashMap.of` body for installer accounts (`flutter_charging_beginning/beginning/state_cards/firmware_upgrade/firmware_upgrade_controller.dart @0x2b0d29c`, `@0x2b0f928`).

## Encrypted?

encrypted: `true` for the Dart senders (asm-traced): the `encryptionRequestHttp` senders default to true, and `HttpRequestControllerImpl::checkBatchOTAUpdateWifi` calls `requestHttp` with the named arguments `cancelToken`, `fail`, `isLogResponse`, `showLoading` only (`charging/http/http_request_repository_impl.dart @0x264b538`), so `needEncryption = true` (`charging/http/http_request_repository_impl.dart @0x2264944`) applies. The two SDK-handler closures go through `akiot.cloud_api` (SDK path, `api/encryption.md`). Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No literal body keys in the seven Dart senders: the body is the result of a `toJson` call on an object built before (for example `charging/http/http_request_repository_impl.dart @0x264b4d0` in `HttpRequestControllerImpl::checkBatchOTAUpdateWifi`, which first removes devices with the product codes `"SHEM3"`, `"SHEMP3"`, `"SHPPS"` and `"ECOIR"` by `removeWhere`, closure `@0x264b610`; my reading of the tests). The SDK-handler closures wrap that body:

| field | type | required | example | source |
|---|---|---|---|---|
| `path` | string | yes | `"/app/ota/batch/check_update"` | `flutter_charging_beginning/beginning/state_cards/firmware_upgrade/firmware_upgrade_controller.dart @0x2b0d384` (value store `@0x2b0d394`) |
| `method` | string | yes | `"POST"` | `flutter_charging_beginning/beginning/state_cards/firmware_upgrade/firmware_upgrade_controller.dart @0x2b0d398` (value store `@0x2b0d3ac`) |
| `param` | object | yes | the `toJson` result of the device list | `flutter_charging_beginning/beginning/state_cards/firmware_upgrade/firmware_upgrade_controller.dart @0x2b0d3b0` (value store `@0x2b0d3d4`) |

The three keys exist only in the SDK-handler path (3.24.3 added `method`, `param` and `path`, see Since/changed); the other senders post the `toJson` object directly.

## `param_type`/`cmd`

n/a

## Response model (link)

[`BatchDeviceModel`](../../../../models/firmware.md#batchdevicemodel) (`data/models.json`, `base_service::BatchDeviceModel`), parsed by `BatchDeviceModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x264b5d0` in the success closure `@0x264b564` of `HttpRequestControllerImpl::checkBatchOTAUpdateWifi`; the other six Dart senders carry the same response class in the inventory (their parse sites were not read one by one).

## Response

Top-level keys of `base_service::BatchDeviceModel` (`data/models.json`): `update_infos` (unknown), `popup_info` (BatchPopupInfo?). The repository closure logs `Ota upgrade pop: data: ` (`@0x264b598`) and passes the model to the callback (`ClosureCall` `@0x264b5ec`).

## Example request/response

Request: the keys of the device-list object are in its `toJson`, which was not decoded, so no body is synthesized. Response: not synthesized; no capture exists for this endpoint.

## Errors seen

none traced: no numeric error code is compared in the senders read. Code meanings are owned by `api/errors.md`.

## Callers in app

- `ats_ax170/src/ats_ax170/page/station/ax170_station_controller.dart`: `checkDeviceUpdate` @0x234d650 (encryptionRequestHttp; encrypted: true)
- `base_service/util/firmware_update_utils.dart`: `checkBatchOTAUpdateWifi` @0x229e16c (encryptionRequestHttp; encrypted: true)
- `charging/http/http_request_repository_impl.dart`: `checkBatchOTAUpdateWifi` @0x264b354 (requestHttp; encrypted: true, `needEncryption` default)
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

3.18.0: present. 3.24.3: present. since: <=3.18.0. Parameter delta in `tools/out/diff_3.18.0_3.24.3.md`: added `method`, `param`, `path` (string-level diff only; it compares literals, not types).

## Known unknowns

- The request body: the `toJson` of the device-list object (`StationDeviceList`, `StationDevice`, `SubPackageVersionModel` appear in `AX170StationController::checkDeviceUpdate`) was not decoded, so no field types are known; `AX170StationController` reads `deviceSn`, `productCode`, `device_type`, `version` and `forceVersion` from device JSON (`anka`-independent station data, `ats_ax170/src/ats_ax170/page/station/ax170_station_controller.dart @0x234d788`..`@0x234dc08`).
- How the nine senders differ (which product families use which): one sender per station family, named by the controller class.
- The response parse of the six other senders, and the element classes of `update_infos` (typed `unknown` in `data/models.json`).
- Server behaviour for the installer variant (`/charging_hes_installer_svc/v2/ota/batch/check_update`): documented on its own page under `charging_hes_installer_svc`.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
