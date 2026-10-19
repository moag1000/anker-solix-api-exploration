> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# update_relate_device_info

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/app/devicemanage/update_relate_device_info`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_business_impl.dart @0x2631874`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `charging/http/http_business_impl.dart @0x2631760` |
| `ble_mac` | ? | ? | ? | `charging/http/http_business_impl.dart @0x2631760` |
| `product_code` | ? | ? | ? | `charging/http/http_business_impl.dart @0x2631760` |
| `device_name` | ? | ? | ? | `charging/http/http_business_impl.dart @0x2631760` |
| `main_sw_version` | ? | ? | ? | `charging/http/http_business_impl.dart @0x2631760` |
| `sec_sw_version` | ? | ? | ? | `charging/http/http_business_impl.dart @0x2631760` |

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

- `charging/http/http_business_impl.dart`: `updateDeviceInfo` @0x2631760 (encryptionRequestHttp; encrypted: true)
- `charging/http/http_request_repository_impl.dart`: `updateDeviceInfo` @0x26315b4 (encryptionRequestHttp; encrypted: true)

Called from: `charging/ble/ble_handler_impl_1.dart::_startResponseListener`, `charging/http/http_request_repository.dart::updateDeviceInfo`, `charging/ui/page/device/a1340/a1340home/a1340home_logic.dart::_bleResponeListen`, `charging/ui/page/device/a172x/a172xhome/a172xhome_logic.dart::_dealWithBleResponse`, `charging/ui/page/device/a1771/a1771home/a1771home_logic.dart::dealWithBleResponse`, `charging/ui/page/device/a1772/a1772home/a1772home_logic.dart::_dealWithBleResponse`, `charging/ui/page/device/a1780p/home/a1780p_home_logic.dart::_dealWithBleResponse`, `charging/ui/page/device/a1781/a1781home/a1781home_logic.dart::_dealWithBleResponse`, `charging/ui/page/device/a1790/a1790home_logic.dart::_dealWithBleResponse`, `charging/ui/page/device/a17b1/device_home/a17b1home_logic.dart::_dealWithBleResponse`, `charging/ui/page/device/a17c0/a17c0home/a17c0home_logic.dart::_dealWithBleResponse`, `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::_dealWithBleResponse`, `charging/ui/page/device/a17y0/a17y0home/a17y0home_logic.dart::_updateA17Y0Info`, `charging/ui/page/device/a2345/a2345home/a2345home_logic.dart::_dealResponse`, `charging/ui/page/device/a2687/a2687home/a2687_home_logic.dart::onMessageDispatch`, `charging/ui/page/device/a91b2/a91b2home/a91b2home_logic.dart::_dealResponse`, `charging/ui/page/device/cooler/a17a3home/a17a3home_logic.dart::handleResponse`, `charging/ui/page/device/cooler/coolerHome/cooler_home_logic.dart::_handleDeviceInfo`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
