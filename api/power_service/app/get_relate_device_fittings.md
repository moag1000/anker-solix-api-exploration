> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_relate_device_fittings

## Purpose

Reads the accessories (fittings) that belong to a device, for the A17C0 home page (callers `A17c0homeLogic::_getCloudA17Y0Info`; builder `getRelateAccessory`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`get_device_fittings` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/get_relate_device_fittings` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x33f773c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x33f7734`, in `HttpRequestControllerImpl::getRelateAccessory` (`charging/http/http_request_repository_impl.dart @0x33f7688`), sent through `encryptionRequestHttp` (`@0x33f775c`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) The body is one map literal of 1 pair (`AllocateArray`, raw `r2 = 4` at `@0x33f76d4`, so 2 slots) with type arguments `<String, String>` at `@0x33f76f0`, so every value is typed in the literal; all keys are stored unconditionally.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_request_repository_impl.dart @0x33f76dc` |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`DeviceModel`](../../../models/device.md#devicemodel), parsed by `DeviceModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x33f78cc`

## Response

(asm-traced) The success closure (`charging/http/http_request_repository_impl.dart @0x33f7778`) reads the key `data` (string literal `@0x33f77c4`) and calls `DeviceModel.fromJson` on it (`@0x33f78cc`).

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `DeviceModel` top-level keys (`data/models.json`, `base_service::DeviceModel`): `device_id` (String?), `device_sn` (String?), `product_code` (String?), `bt_ble_id` (String?), `bt_ble_mac` (String?), `device_name` (String?), `alias_name` (String?), `img_url` (String?), `bind_time` (int?), `wifi_name` (String?), `wifi_online` (bool?), `relate_type` (List?), `charge` (bool?), `bws_surplus` (int?), `link_time` (int), `device_sw_version` (String?), `has_manual` (bool?), `init_status` (int?), `hes_data` (unknown), `group_info` (unknown), `tag` (String?), `tag_img` (String?), `blue_password` (String?), `wifi_mac` (String?), `time_zone` (String?), `ms_device_type` (int?), `owner_user_id` (String?), `ocpp_connect_status` (int?), `tag_alias` (String?), `tag_id` (int?), `type_tag` (String?), `type_tag_id` (int?), `type_tag_img` (String?), `rssi` (String?), `intgr_device` (IntegratorDeviceStatusModel?), `link_info` (DeviceLinkInfoModel?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getRelateAccessory` @0x33f7688 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getRelateAccessory`
- `charging/ui/page/device/a17c0/a17c0home/a17c0home_logic.dart::_getCloudA17Y0Info`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Whether the `data` entry is a single object or a list: the closure calls `DeviceModel.fromJson` once on the value it reads (`@0x33f78cc`); the caller's use was not decoded.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
