> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# check_update

## Purpose

Asks the cloud for firmware updates for a batch of devices of a system; in the installer flow the app sends the batch to the installer service together with the `system_id`, otherwise to the consumer service.

## Upstream name

`none` for the installer URL (no upstream name). The consumer twin `/app/ota/batch/check_update` is the upstream key `get_ota_batch` (`api/apitypes.py` line 185, upstream-confirmed; `apibase.py` `get_ota_batch` posts `{"device_list": [{"device_sn": <sn>, "version": ""}]}`).

## Method+URL

`POST /charging_hes_installer_svc/v2/ota/batch/check_update` (asm-traced). Two closures of `FirmwareUpgradeController` build the SDK request (`flutter_charging_beginning/beginning/state_cards/firmware_upgrade/firmware_upgrade_controller.dart`): the closure `@0x2b0d200` in `checkDeviceUpdate` (`@0x2b0932c`) and the closure `@0x2b0f898` in `checkUpgradeViaMultiDeploy` (`@0x2b0e14c`). Both choose between the installer path `/charging_hes_installer_svc/v2/ota/batch/check_update` (`@0x2b0d2a4`, `@0x2b0f930`; pool `pp+0x136458`) and the consumer path `/app/ota/batch/check_update` (`@0x2b0d38c`, `@0x2b0fa14`): the installer path is used when the field at offset 0x5b of `initialSetupController` is non-null (`cmp w1, NULL` at `@0x2b0d284`, `@0x2b0f910`; its name is not in the asm, by analogy with the platform list page it is probably the system id). The method string is the literal `"POST"` (`@0x2b0d2bc`, `@0x2b0f948`). The selector is a controller field, not the `isProApp` flag of [the variant selector](../../../README.md#variant-selector-installer-app-versus-consumer-app).

## Encrypted?

Direct SDK call (asm-traced), path C of [../../../../encryption.md](../../../../encryption.md#which-calls-are-encrypted): both closures build the map `path`, `method`, `param` and pass it to `akIoTKitManager.handle` with the identifier `akiot.cloud_api` (`@0x2b0d420`, `@0x2b0faa8`), wrapped in `startCommand`. The decorator tests are not involved; encryption and headers are native to the SDK. The inventory flag `encrypted: false` only means that no `*Http*` wrapper is called.

## Request

`param` is the result of `StationDeviceList.toJson()` (`base_service/bean/model/firmware_update/station_device_model.dart @0x229e3bc`), copied into a `LinkedHashMap` (`@0x2b0d2ec`) to which the installer branch adds one key:

| field | type | required | example | source |
|---|---|---|---|---|
| `device_list` | list of maps | yes | `[ { "device_sn": "...", ... } ]` | `station_device_model.dart @0x229e448` |
| `system_id` | not decoded (the controller field at offset 0x5b) | installer path only | `<system id>` | `flutter_charging_beginning/beginning/state_cards/firmware_upgrade/firmware_upgrade_controller.dart @0x2b0d324` (`checkDeviceUpdate`), `@0x2b0f9b0` (`checkUpgradeViaMultiDeploy`); set with `[]=` |

Each element of `device_list` is `StationDevice.toJson()` (`station_device_model.dart @0x229e4e4`):

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `"<device sn>"` | `@0x229e530` |
| `device_pn` | String | yes | `"<product code>"` | `@0x229e560` |
| `version` | String | yes | `""` | `@0x229e590` (upstream sends `""`) |
| `sub_package` | list | no | not decoded | `@0x229e640`; elements are `SubPackageVersionModel.toJson()` with `device_type` and `version` (`@0x229e844`, `@0x229e874`) |
| `sub_ota_way` | not decoded | no | not decoded | `@0x229e670` |
| `aliasName` | String | no | not decoded | `@0x229e6a0` |
| `link_mode` | not decoded | no | not decoded | `@0x229e6d0` |
| `force_version` | not decoded | no | not decoded | `@0x229e700` |
| `device_type` | not decoded | no | not decoded | `@0x229e730` |

The app sends no integer literal in this request.

## `param_type`/`cmd`

n/a

## Response model (link)

`BatchDeviceModel` (`base_service/bean/model/firmware_update/batch_device_model.dart`, `fromJson @0x229ea10`; legacy page [../../../../../models/firmware.md](../../../../../models/firmware.md#batchdevicemodel)), parsed with `BatchDeviceModel.fromJson` at `flutter_charging_beginning/beginning/state_cards/firmware_upgrade/firmware_upgrade_controller.dart @0x2b0ac98` in the success closure `@0x2b09bb8` of `checkDeviceUpdate`.

## Response

The SDK result must be of the success type (`@0x2b0ab88`); its payload is a JSON string that the app decodes (`JsonCodec.decode`, `@0x2b0ac58`) after a non-empty check (`@0x2b0ac44`) and parses with `BatchDeviceModel.fromJson` (`@0x2b0ac98`). A failed parse logs `Parse batch OTA error` (`@0x2b0ae00`); a failed SDK result shows the `networkError` text (`@0x2b0ae78`).

| field | type | required | example | source |
|---|---|---|---|---|
| `update_infos` | list (element type not resolved) | no | `[ { "device_sn": "...", "need_update": false } ]` | `batch_device_model.dart @0x229ea4c`; the upstream example for the consumer twin shows elements with `device_sn`, `need_update`, `upgrade_type`, `lastPackage`, `change_log`, `current_version` and `children[]` (upstream-confirmed, `apibase.py` docstring) |
| `popup_info` | `BatchPopupInfo?` | no | not decoded | `batch_device_model.dart @0x229eb00` |

The app uses the parsed object to decide whether any device needs an update (`every(...)` over the list, `@0x2b0ad1c`, then `setStateDelayFirmwareUpgradeNoNeed`, `@0x2b0ad50`).

## Example request/response

Request, synthesized

```json
{ "path": "/charging_hes_installer_svc/v2/ota/batch/check_update", "method": "POST",
  "param": { "device_list": [ { "device_sn": "<device sn>", "device_pn": "<product code>", "version": "" } ], "system_id": "<system id>" } }
```

Response: no captured response from the installer path; the consumer twin's response is documented upstream (`apibase.py`), not copied here.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or shows a toast; the shared transport codes are in [../../../../encryption.md](../../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../../errors.md).

## Callers in app

- `FirmwareUpgradeController.checkDeviceUpdate` (`flutter_charging_beginning/beginning/state_cards/firmware_upgrade/firmware_upgrade_controller.dart @0x2b0932c`), request closure `@0x2b0d200`, success closure `@0x2b09bb8`.
- `FirmwareUpgradeController.checkUpgradeViaMultiDeploy` (`@0x2b0e14c`), request closure `@0x2b0f898`.
UI: the firmware upgrade card of the initial-setup (`flutter_charging_beginning`) flow, i.e. the installer commissioning of a system.

## Since/changed

3.18.0: the consumer path `/app/ota/batch/check_update` is present; the installer path is absent (no `installer_svc` string in the 3.18.0 pool). 3.24.3: the installer path is present (new). since: 3.24.3 for the installer path.

## Known unknowns

- Server behaviour of the installer service (compared with the consumer answer) is not known.
- The name and type of the `initialSetupController` field behind `system_id` are not in the asm.
- The element layout of `update_infos` is not traced in 3.24.3; the upstream example is for the consumer twin.

## Device-tested by

none
