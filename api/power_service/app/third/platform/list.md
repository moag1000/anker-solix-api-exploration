> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# list

## Purpose

Lists the third-party (Shelly) platforms a user can add: `ScanLogic::onInit`, `ThirdPartyPlatformListLogic::requestThirdPartyPlatformList`, `ScanAppointDeviceLogic::onInit` and `DeviceMainLogic` (`_initLogic`, `onMessageDispatch`) call `getThirdPartyPlatformList`; the beginning flow (`PlatformAppointAddDeviceController::getThirdPartyPlatformList`) sends it through the IoT kit.

## Upstream name

`get_third_platforms` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/third/platform/list` (asm-traced): URL string at `http_request_repository_impl.dart @0x26192fc`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x26192f4`, in `HttpRequestControllerImpl::getThirdPartyPlatformList` (`http_request_repository_impl.dart @0x2619228`).

The IoT-kit sender `PlatformAppointAddDeviceController::getThirdPartyPlatformList` (`platform_appoint_add_device_controller.dart @0x24e60d8`) selects the path string `"/power_service/v1/app/third/platform/list"` (`@0x24e610c`) unless a field is non-null (`cmp w1, NULL` `@0x24e6134`), in which case it selects `"/charging_hes_installer_svc/v2/app/third/platform/list"` (`@0x24e613c`, another page); its command closure `@0x24e6bd8` puts that path, the string literal `"POST"` (`@0x24e6c58`) and a `param` map into the command map passed to `akIoTKitManager`.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Both senders send the single key `app_id`.

| field | type | required | example | source |
|---|---|---|---|---|
| `app_id` | string | yes | `"anker_power"` | key `http_request_repository_impl.dart @0x2619284` in the repository sender `getThirdPartyPlatformList` (function `@0x2619228`): map typed `<String, String>`, literal `@0x2619290`, store `@0x2619298`; IoT-kit sender: selected together with the path, literal `"anker_power"` `flutter_charging_beginning/beginning/state_cards/add_devices/platform_appoint_add_device/platform_appoint_add_device_controller.dart @0x24e611c` (the installer URL pairs with `"anker_pros"` `@0x24e6144`), put into the `param` map typed `<String, String>` (`@0x24e6c98`, key `@0x24e6c7c`, store `@0x24e6c94`) |

## `param_type`/`cmd`

n/a

## Response model (link)

`base_service::ThirdPartyPlatformInfoModel` (`data/models.json` key; fields on [`models/other.md`](../../../../../models/other.md#thirdpartyplatforminfomodel)), one object per list element. Repository sender: the success closure `http_request_repository_impl.dart @0x2619340` calls `resolveListResponseData` (`@0x261936c`) and `ThirdPartyPlatformInfoModel.fromJson` per element. IoT-kit sender: the controller reads `data` (`flutter_charging_beginning/beginning/state_cards/add_devices/platform_appoint_add_device/platform_appoint_add_device_controller.dart @0x24e61e8`), decodes the JSON string (`JsonCodec.decode` `@0x24e6258`) and calls `ThirdPartyPlatformInfoModel.fromJson` (`@0x24e63f0`) per element.

## Response

The response is a list. Keys of one element (from `data/models.json`, all nullable): `index` (int), `name`, `content`, `logo`, `tag`, `url`, `callback_url`, `tag_code` (String), `products` (List).

## Example request/response

Request, synthesized (decrypted body of the repository sender)

```json
{"app_id": "anker_power"}
```

Response keys: see Response; no capture.

## Errors seen

None traced. The repository sender's failure callback `http_request_repository_impl.dart @0x23a07f4` is a forwarding template; the IoT-kit controller logs `"Parse third party platform list error"` (`flutter_charging_beginning/beginning/state_cards/add_devices/platform_appoint_add_device/platform_appoint_add_device_controller.dart @0x24e6518`) on a parse failure; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getThirdPartyPlatformList` @0x2619228 (encryptionRequestHttp; encrypted: true)
- `flutter_charging_beginning/beginning/state_cards/add_devices/platform_appoint_add_device/platform_appoint_add_device_controller.dart`: `getThirdPartyPlatformList` @0x24e60d8 (URL literal only, no `*Http*` call; sends in the same function (`AKIoTKitManagerImpl::handle`); resolved from the URL literal at `flutter_charging_beginning/beginning/state_cards/add_devices/platform_appoint_add_device/platform_appoint_add_device_controller.dart @0x24e610c` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

Called from:

- `charging/http/http_request_repository.dart::getThirdPartyPlatformList`
- `charging/ui/page/device/connect/scan_logic.dart::onInit`
- `charging/ui/page/device/connect/third_party_platform_list/third_party_platform_list_logic.dart::requestThirdPartyPlatformList`
- `charging/ui/page/device/main/sitation_energy_system/scan_appoint_device/scan_appoint_device_logic.dart::onInit`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::_initLogic`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::onMessageDispatch`
- `flutter_charging_beginning/beginning/state_cards/add_devices/platform_appoint_add_device/platform_appoint_add_device_controller.dart::afterPermissionEnable`
- `flutter_charging_beginning/beginning/state_cards/add_devices/platform_appoint_add_device/platform_appoint_add_device_controller.dart::onInit`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta. The model `ThirdPartyPlatformInfoModel` is `≤3.18.0` in `data/models.json`.

## Known unknowns

- Which condition selects the installer variant (`field_5f` of the controller, `@0x24e612c`); only the pairing of `anker_pros` with the installer path is read.
- The element structure of `products` (the model keeps it as an untyped list). — reclassified: server (elements of an untyped list; the content is server data)
- Whether the server filters the list by `app_id`: not derivable from the app.

## Device-tested by

none
