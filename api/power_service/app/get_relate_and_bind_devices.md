> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_relate_and_bind_devices

## Purpose

Lists the devices related to and bound to the account for the device list, scan and OTA pages (callers `DeviceMainLogic::getDeviceList`, `ScanLogic::getDeviceList`, `CheckUpdateLogic::getDeviceList`, `AnkerOTABaseLogic::specialHandleOta`) and, in `BusinessService::fetchDevicesListDirect`, for the installer check at network set-up (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`bind_devices` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/get_relate_and_bind_devices` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x2289788`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2289780`, in `HttpRequestControllerImpl::getDevicesList` (`charging/http/http_request_repository_impl.dart @0x2289700`), sent through `encryptionRequestHttp` (`@0x22897b0`).

Same URL and method object in the other sender(s) read:

- `POST /power_service/v1/app/get_relate_and_bind_devices` (asm-traced): URL string at `base_service/service/business_service.dart @0x2ac45d8`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2ac45d0`, in `BusinessService::fetchDevicesListDirect` (`base_service/service/business_service.dart @0x2ac44b8`), sent through `encryptionRequestHttp` (`@0x2ac45fc`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) No request fields in either sender: both pass the empty map literal (`THR::empty_array`, `Map._fromLiteral`) at `charging/http/http_request_repository_impl.dart @0x228974c` (`HttpRequestControllerImpl::getDevicesList`) and `base_service/service/business_service.dart @0x2ac45a0` (`BusinessService::fetchDevicesListDirect`).

## `param_type`/`cmd`

n/a

## Response model (link)

- [`DeviceModel`](../../../models/device.md#devicemodel), parsed by `DeviceModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x22898b0`. Parsed per list entry by `HttpRequestControllerImpl::getDevicesList` after `resolveListResponseData` (`@0x228980c`).

## Response

(asm-traced) The second sender `BusinessService::fetchDevicesListDirect` (`base_service/service/business_service.dart`) does not use `DeviceModel`: its success closure (`@0x2ac4860`) reads the key `data` (string literal `@0x2ac4a30`), casts it to `String` (`@0x2ac4a78`), runs `jsonDecode` (`@0x2ac4a80`) and reads the key `deviceInfos` (`@0x2ac4ab4`).



(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `DeviceModel` top-level keys (`data/models.json`, `base_service::DeviceModel`): `device_id` (String?), `device_sn` (String?), `product_code` (String?), `bt_ble_id` (String?), `bt_ble_mac` (String?), `device_name` (String?), `alias_name` (String?), `img_url` (String?), `bind_time` (int?), `wifi_name` (String?), `wifi_online` (bool?), `relate_type` (List?), `charge` (bool?), `bws_surplus` (int?), `link_time` (int), `device_sw_version` (String?), `has_manual` (bool?), `init_status` (int?), `hes_data` (unknown), `group_info` (unknown), `tag` (String?), `tag_img` (String?), `blue_password` (String?), `wifi_mac` (String?), `time_zone` (String?), `ms_device_type` (int?), `owner_user_id` (String?), `ocpp_connect_status` (int?), `tag_alias` (String?), `tag_id` (int?), `type_tag` (String?), `type_tag_id` (int?), `type_tag_img` (String?), `rssi` (String?), `intgr_device` (IntegratorDeviceStatusModel?), `link_info` (DeviceLinkInfoModel?).

## Example request/response

Request, synthesized: the body is the empty object.

```json
{}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `base_service/service/business_service.dart`: `fetchDevicesListDirect` @0x2ac44b8 (encryptionRequestHttp; encrypted: true)
- `charging/http/http_request_repository_impl.dart`: `getDevicesList` @0x2289700 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getDevicesList`
- `charging/ui/page/device/a17b1/check_update/check_update_logic.dart::getDeviceList`
- `charging/ui/page/device/anker_ota/base/anker_ota_base_logic.dart::specialHandleOta`
- `charging/ui/page/device/connect/scan_logic.dart::getDeviceList`
- `charging/ui/page/device/main/sitation_energy_system/scan_appoint_device/scan_appoint_device_logic.dart::getDeviceList`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::getDeviceList`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the `deviceInfos` entries of the installer-check sender contain (the closure maps them with `List.from` in `@0x2ac46d0`; no model class is named).
- Why `data` holds a JSON string in that sender (the closure `jsonDecode`s it): the server shape is not visible from the app.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
