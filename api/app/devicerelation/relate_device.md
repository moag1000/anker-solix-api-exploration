> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# relate_device

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/app/devicerelation/relate_device`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_business_impl.dart @0x33f81ec`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `charging/http/http_business_impl.dart @0x33f802c` |
| `product_code` | ? | ? | ? | `charging/http/http_business_impl.dart @0x33f802c` |
| `device_name` | ? | ? | ? | `charging/http/http_business_impl.dart @0x33f802c` |
| `bt_ble_id` | ? | ? | ? | `charging/http/http_business_impl.dart @0x33f802c` |
| `bt_ble_mac` | ? | ? | ? | `charging/http/http_business_impl.dart @0x33f802c` |
| `firmware_version` | ? | ? | ? | `charging/http/http_business_impl.dart @0x33f802c` |
| `wifi_name` | ? | ? | ? | `charging/http/http_business_impl.dart @0x33f802c` |
| `parent_device_sn` | ? | ? | ? | `charging/http/http_business_impl.dart @0x33f802c` |
| `parent_device_pn` | ? | ? | ? | `charging/http/http_business_impl.dart @0x33f802c` |

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

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
