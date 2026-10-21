> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# relate_device

## Purpose

Binds a device to the logged-in account; sent by the login and bind-phone flows (`LoginHandler::_bindAndMigrateDevice`, `LoginNavigationHandler::_bindDeviceBle`, `LoginLogic::_bindDeviceBle`, `BindPhoneNumberLogic::_bindDeviceBle`) and by `A17C0DeviceCommands::_cloudA17Y0InfoSync` through `deviceBind` (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/devicerelation/relate_device` (asm-traced): URL string at `charging/http/http_business_impl.dart @0x33f81ec`, in `HttpBusinessImpl::deviceBind` (`charging/http/http_business_impl.dart @0x33f802c`), sent through the business wrapper `HttpBusinessImpl::encryptionRequestHttp` (`@0x33f8214`; wrapper `charging/http/http_business_impl.dart @0x2618680`), which passes the method object `Method.post` (pool entry `pp+0xa7e0`, `charging/http/http_business_impl.dart @0x261877c`) to `requestHttp` (`@0x26187b8`).

Same URL in the other sender(s) read:

- `POST /app/devicerelation/relate_device` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x26ff360`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x26ff358`, in `HttpRequestControllerImpl::deviceBind` (`charging/http/http_request_repository_impl.dart @0x26ff01c`), sent through `encryptionRequestHttp` (`@0x26ff390`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_business_impl.dart @0x33f80d8` (value store `@0x33f80e8`) |
| `product_code` | string | yes | `"A17Y0"` | `charging/http/http_business_impl.dart @0x33f80ec` (value store `@0x33f8100`) |
| `device_name` | string | yes | `"<device_name>"` | `charging/http/http_business_impl.dart @0x33f8104` (value store `@0x33f8114`) |
| `bt_ble_id` | string | yes | `"<bt_ble_id>"` | `charging/http/http_business_impl.dart @0x33f8118` (value store `@0x33f8128`) |
| `bt_ble_mac` | string | yes | `"<bt_ble_mac>"` | `charging/http/http_business_impl.dart @0x33f812c` (value store `@0x33f813c`) |
| `firmware_version` | string | yes | `"<firmware_version>"` | `charging/http/http_business_impl.dart @0x33f8140` (value store `@0x33f8150`) |
| `wifi_name` | string | yes | `""` | `charging/http/http_business_impl.dart @0x33f8154` (value store `@0x33f8164`) |
| `parent_device_sn` | string | yes | `"<parent_device_sn>"` | `charging/http/http_business_impl.dart @0x33f8168` (value store `@0x33f8178`) |
| `parent_device_pn` | string | yes | `"A17C0"` | `charging/http/http_business_impl.dart @0x33f817c` (value store `@0x33f8190`) |

All values are Strings: the one map literal of each sender has type arguments `<String, String>` (`charging/http/http_business_impl.dart @0x33f8194`, `charging/http/http_request_repository_impl.dart @0x26ff300`). The examples that look like constants come from `HttpBusinessImpl::deviceBind` only: `product_code` `"A17Y0"`, `wifi_name` the empty string and `parent_device_pn` `"A17C0"` (`charging/http/http_business_impl.dart @0x33f80f8`, `@0x33f8160`, `@0x33f8188`, the sender used by the A17C0/A17Y0 sync); `HttpRequestControllerImpl::deviceBind` takes all nine values from its parameters (`charging/http/http_request_repository_impl.dart @0x26ff25c`..`@0x26ff2fc`).

## `param_type`/`cmd`

n/a

## Response model (link)

[`DeviceModel`](../../../models/device.md#devicemodel) (`data/models.json`, `base_service::DeviceModel`), parsed by `DeviceModel.fromJson` at `charging/http/http_business_impl.dart @0x33f8268` (success closure `@0x33f8230`) and at `charging/http/http_request_repository_impl.dart @0x26ff49c` (success closure `@0x26ff464`); call target `#0x2270620` in `base_service/bean/model/device_model.dart`.

## Response

(asm-traced) Top-level keys of `base_service::DeviceModel` (`data/models.json`): `device_id` (String?), `device_sn` (String?), `product_code` (String?), `bt_ble_id` (String?), `bt_ble_mac` (String?), `device_name` (String?), `alias_name` (String?), `img_url` (String?), `bind_time` (int?), `wifi_name` (String?), `wifi_online` (bool?), `relate_type` (List?), `charge` (bool?), `bws_surplus` (int?), `link_time` (int), `device_sw_version` (String?), `has_manual` (bool?), `init_status` (int?), `hes_data` (unknown), `group_info` (unknown), `tag` (String?), `tag_img` (String?), `blue_password` (String?), `wifi_mac` (String?), `time_zone` (String?), `ms_device_type` (int?), `owner_user_id` (String?), `ocpp_connect_status` (int?), `tag_alias` (String?), `tag_id` (int?), `type_tag` (String?), `type_tag_id` (int?), `type_tag_img` (String?), `rssi` (String?), `intgr_device` (IntegratorDeviceStatusModel?), `link_info` (DeviceLinkInfoModel?). Both closures store the model as the last device (`setLastDevice` `charging/http/http_business_impl.dart @0x33f8288`, `charging/http/http_request_repository_impl.dart @0x26ff4bc`) and pass it to the stored callback (`ClosureCall` `@0x33f82a4`, `@0x26ff50c`).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>",
  "product_code": "A17Y0",
  "device_name": "<device_name>",
  "bt_ble_id": "<bt_ble_id>",
  "bt_ble_mac": "<bt_ble_mac>",
  "firmware_version": "<firmware_version>",
  "wifi_name": "",
  "parent_device_sn": "<parent_device_sn>",
  "parent_device_pn": "A17C0"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_business_impl.dart`: `deviceBind` @0x33f802c (encryptionRequestHttp; encrypted: true)
- `charging/http/http_request_repository_impl.dart`: `deviceBind` @0x26ff01c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/account/handlers/login_handler.dart::_bindAndMigrateDevice`
- `charging/account/handlers/login_navigation_handler.dart::_bindDeviceBle`
- `charging/ble/device/A17C0/a17C0_device_commands.dart::_cloudA17Y0InfoSync`
- `charging/http/http_request_repository.dart::deviceBind`
- `charging/ui/page/account/bind_phone_number/bind_phone_number_logic.dart::_bindDeviceBle`
- `charging/ui/page/account/login/login_logic.dart::_bindDeviceBle`
- `charging/ui/page/device/a17c0/a17c0accessory/bind_accessory/a17c0bind_accessory_logic.dart::_bindA17Y0`
- `charging/ui/page/device/a17c0/a17c0home/a17c0home_logic.dart::_cloudA17Y0InfoSync`
- `charging/ui/page/device/a5140/wifi/network_inspection/network_inspection_logic.dart::_bindDevice`
- `charging/ui/page/device/a5143/match_scan/a5143_match_scan_logic.dart::_bindDevice`
- `charging/ui/page/device/connect/connect_logic.dart::initDeviceResponse`
- `charging/ui/page/device/connect/zx_connect_ble/zx_connect_ble_logic.dart::bindDevice`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Meaning and values of `bt_ble_id`, `firmware_version` and `parent_device_pn` for devices other than the A17C0/A17Y0 pair: the constant values are specific to `HttpBusinessImpl::deviceBind`; the parameter senders were not traced to their callers.
- Server rules for a device that is already bound to another account (error codes): no code is compared in the senders; see the callers listed above.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
