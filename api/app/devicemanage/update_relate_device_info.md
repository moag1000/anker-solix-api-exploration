> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# update_relate_device_info

## Purpose

Pushes the identity of a device (serial number, BLE MAC, product code, name and firmware version) to the cloud after a BLE response; called from the device home pages (for example `A1340HomeLogic::_bleResponeListen`, `A172xHomeLogic::_dealWithBleResponse`) and `BleHandlerImpl1::_startResponseListener` through `updateDeviceInfo` (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/devicemanage/update_relate_device_info` (asm-traced): URL string at `charging/http/http_business_impl.dart @0x2631874`, in `HttpBusinessImpl::updateDeviceInfo` (`charging/http/http_business_impl.dart @0x2631760`), sent through the business wrapper `HttpBusinessImpl::encryptionRequestHttp` (`@0x263189c`; wrapper `charging/http/http_business_impl.dart @0x2618680`), which passes the method object `Method.post` (pool entry `pp+0xa7e0`, `charging/http/http_business_impl.dart @0x261877c`) to `requestHttp` (`@0x26187b8`).

Same URL in the other sender(s) read:

- `POST /app/devicemanage/update_relate_device_info` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x26316e0`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x26316d8`, in `HttpRequestControllerImpl::updateDeviceInfo` (`charging/http/http_request_repository_impl.dart @0x26315b4`), sent through `encryptionRequestHttp` (`@0x2631708`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_business_impl.dart @0x26317a4` (value store `@0x26317b4`) |
| `ble_mac` | string | yes | `"<ble_mac>"` | `charging/http/http_business_impl.dart @0x26317b8` (value store `@0x26317c8`) |
| `product_code` | string | yes | `"<product_code>"` | `charging/http/http_business_impl.dart @0x26317cc` (value store `@0x26317dc`) |
| `device_name` | string | yes | `"<device_name>"` | `charging/http/http_business_impl.dart @0x26317e0` (value store `@0x26317f0`) |
| `main_sw_version` | string | yes | `"<main_sw_version>"` | `charging/http/http_business_impl.dart @0x26317f4` (value store `@0x2631804`) |
| `sec_sw_version` | string | yes | `""` | `charging/http/http_business_impl.dart @0x2631808` (value store `@0x2631818`) |

All values are Strings: the one map literal of each sender has type arguments `<String, String>` (`charging/http/http_business_impl.dart @0x2631828`, `charging/http/http_request_repository_impl.dart @0x2631680`). `sec_sw_version` is the constant empty string in both senders (`@0x2631814`, `@0x2631678`).

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closures never read their response argument; `charging/http/http_business_impl.dart @0x26318b8` only logs `updateDeviceInfo success` (`@0x26318cc`) and `charging/http/http_request_repository_impl.dart @0x26318f4` logs the same text (`@0x2631908`). No `fromJson`.

## Response

No response key is read by the app (see Response model).

App side result handling (traced 2026-10-20): the failure closure of the sender (`charging/http/http_business_impl.dart @0x2631724`, signature `(int, String)`) only logs `updateDeviceInfo fail` (`@0x2631738`, `@0x2631744`) and the success closure (`@0x26318b8`) only logs `updateDeviceInfo success` (`@0x26318cc`); neither retries nor changes app state.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>",
  "ble_mac": "<ble_mac>",
  "product_code": "<product_code>",
  "device_name": "<device_name>",
  "main_sw_version": "<main_sw_version>",
  "sec_sw_version": ""
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_business_impl.dart`: `updateDeviceInfo` @0x2631760 (encryptionRequestHttp; encrypted: true)
- `charging/http/http_request_repository_impl.dart`: `updateDeviceInfo` @0x26315b4 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ble/ble_handler_impl_1.dart::_startResponseListener`
- `charging/http/http_request_repository.dart::updateDeviceInfo`
- `charging/ui/page/device/a1340/a1340home/a1340home_logic.dart::_bleResponeListen`
- `charging/ui/page/device/a172x/a172xhome/a172xhome_logic.dart::_dealWithBleResponse`
- `charging/ui/page/device/a1771/a1771home/a1771home_logic.dart::dealWithBleResponse`
- `charging/ui/page/device/a1772/a1772home/a1772home_logic.dart::_dealWithBleResponse`
- `charging/ui/page/device/a1780p/home/a1780p_home_logic.dart::_dealWithBleResponse`
- `charging/ui/page/device/a1781/a1781home/a1781home_logic.dart::_dealWithBleResponse`
- `charging/ui/page/device/a1790/a1790home_logic.dart::_dealWithBleResponse`
- `charging/ui/page/device/a17b1/device_home/a17b1home_logic.dart::_dealWithBleResponse`
- `charging/ui/page/device/a17c0/a17c0home/a17c0home_logic.dart::_dealWithBleResponse`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::_dealWithBleResponse`
- `charging/ui/page/device/a17y0/a17y0home/a17y0home_logic.dart::_updateA17Y0Info`
- `charging/ui/page/device/a2345/a2345home/a2345home_logic.dart::_dealResponse`
- `charging/ui/page/device/a2687/a2687home/a2687_home_logic.dart::onMessageDispatch`
- `charging/ui/page/device/a91b2/a91b2home/a91b2home_logic.dart::_dealResponse`
- `charging/ui/page/device/cooler/a17a3home/a17a3home_logic.dart::handleResponse`
- `charging/ui/page/device/cooler/coolerHome/cooler_home_logic.dart::_handleDeviceInfo`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the server does with the values (whether it updates the stored device record or checks for conflicts): not visible in the app.
- How often the callers send it: it is triggered from the BLE response handlers of each device home page (about fourteen callers); the trigger condition was not decoded. — traced 2026-10-20: the call sits in the BLE response handlers listed under Callers in app; each call site is behind a handler-specific condition (for example the closure in `BleHandlerImpl1::_startResponseListener`, `charging/ble/ble_handler_impl_1.dart @0x4196b08`, follows two dispatch calls whose selectors are not named by Blutter), so no common trigger rule is readable
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
