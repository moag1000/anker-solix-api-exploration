> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# un_relate_and_unbind_device

## Purpose

Removes the relation between a device and the account (unbind); sent by `HttpRequestControllerImpl::deviceUnbind` and `::iotDeviceUnbind` and by `HttpBusinessImpl::iotDeviceUnbind` (used by `A17C0DeviceCommands::_cloudA17Y0InfoSync` for the A17C0 parent) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/devicerelation/un_relate_and_unbind_device` (asm-traced): URL string at `charging/http/http_business_impl.dart @0x33f7f68`, in `HttpBusinessImpl::iotDeviceUnbind` (`charging/http/http_business_impl.dart @0x33f7e44`), sent through the business wrapper `HttpBusinessImpl::encryptionRequestHttp` (`@0x33f7f84`; wrapper `charging/http/http_business_impl.dart @0x2618680`), which passes the method object `Method.post` (pool entry `pp+0xa7e0`, `charging/http/http_business_impl.dart @0x261877c`) to `requestHttp` (`@0x26187b8`).

Same URL in the other sender(s) read:

- `POST /app/devicerelation/un_relate_and_unbind_device` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3430b50`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3430b48`, in `HttpRequestControllerImpl::deviceUnbind` (`charging/http/http_request_repository_impl.dart @0x3430a64`), sent through `encryptionRequestHttp` (`@0x3430b78`).
- `POST /app/devicerelation/un_relate_and_unbind_device` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x2762fb4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2762fac`, in `HttpRequestControllerImpl::iotDeviceUnbind` (`charging/http/http_request_repository_impl.dart @0x2762e78`), sent through `encryptionRequestHttp` (`@0x2762fdc`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Union over the three senders; the first two senders (`iotDeviceUnbind`) use the map literal `<String, String>` (`charging/http/http_business_impl.dart @0x33f7f24`, `charging/http/http_request_repository_impl.dart @0x2762f68`), `deviceUnbind` uses `<String, String?>` (`charging/http/http_request_repository_impl.dart @0x3430b04`), so all values are Strings (nullable in `deviceUnbind`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_business_impl.dart @0x33f7ed0` (value store `@0x33f7ee0`) |
| `bt_ble_mac` | string | yes | `"<bt_ble_mac>"` | `charging/http/http_business_impl.dart @0x33f7ee4` (value store `@0x33f7ef4`) |
| `parent_device_sn` | string | yes (the two `iotDeviceUnbind` senders only) | `"<parent_device_sn>"` | `charging/http/http_business_impl.dart @0x33f7ef8` (value store `@0x33f7f08`) |
| `parent_device_pn` | string | yes (the two `iotDeviceUnbind` senders only) | `"A17C0"` in `HttpBusinessImpl::iotDeviceUnbind`, a parameter in the other | `charging/http/http_business_impl.dart @0x33f7f0c` (constant `@0x33f7f18`) |
| `unbind_type` | string | yes (`HttpRequestControllerImpl::deviceUnbind` only) | | `charging/http/http_request_repository_impl.dart @0x3430af0` (value store `@0x3430b00`, a parameter) |

The key sets differ per sender: `deviceUnbind` sends `bt_ble_mac`, `device_sn`, `unbind_type` (`charging/http/http_request_repository_impl.dart @0x3430ac8`); `HttpRequestControllerImpl::iotDeviceUnbind` sends `device_sn`, `bt_ble_mac`, `parent_device_sn`, `parent_device_pn` (`charging/http/http_request_repository_impl.dart @0x2762f10`).

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closures never read their response argument; `charging/http/http_business_impl.dart @0x33f7fa0` calls the stored callback and logs `unbind success: ` (`@0x33f800c`), `charging/http/http_request_repository_impl.dart @0x3430b94` and `charging/http/http_request_repository_impl.dart @0x2762ff8` delete the device by MAC twice (`deleteByMac` `@0x3430bf0`, `@0x2763054`) and then call the callback. No `fromJson`.

## Response

No response key is read by the app (see Response model).

The two `deleteByMac` calls (traced 2026-10-20, app side): the success closures of `deviceUnbind` (`charging/http/http_request_repository_impl.dart @0x3430b94`) and `iotDeviceUnbind` (`@0x2762ff8`) first delete the unbound device's rows by MAC from the local message table of system messages (`LocalSystemMessageDao::deleteByMac`, `local_system_message_dao.dart`; `_getInstance` `@0x3430bdc`, call `@0x3430bf0`) and then from the local table of device messages (`LocalDeviceMessageDao::deleteByMac`, `lacal_device_message_dao.dart`; `_getInstance` `@0x3430c00`, call `@0x3430c14`), awaiting each, before they call the stored success callback (`ClosureCall` `@0x3430c3c`). These are two different local stores, so the second call is not a repeat. (The MAC argument is `field_f` of the closure context.)

## Example request/response

Request, synthesized (decrypted body as built by `HttpBusinessImpl::iotDeviceUnbind`; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>",
  "bt_ble_mac": "<bt_ble_mac>",
  "parent_device_sn": "<parent_device_sn>",
  "parent_device_pn": "A17C0"
}
```

Response: not synthesized; no capture exists for this endpoint.

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_business_impl.dart`: `iotDeviceUnbind` @0x33f7e44 (encryptionRequestHttp; encrypted: true)
- `charging/http/http_request_repository_impl.dart`: `deviceUnbind` @0x3430a64 (encryptionRequestHttp; encrypted: true); `iotDeviceUnbind` @0x2762e78 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ble/device/A17C0/a17C0_device_commands.dart::_cloudA17Y0InfoSync`
- `charging/http/http_request_repository.dart::deviceUnbind`
- `charging/http/http_request_repository.dart::iotDeviceUnbind`
- `charging/ui/page/device/a1340/a1340setting/a1340setting_logic.dart::showRemoveDialog`
- `charging/ui/page/device/a172x/a172xsetting/a172xsetting_logic.dart::showRemoveDialog`
- `charging/ui/page/device/a1770/a1770setting/a1770setting_logic.dart::showRemoveDialog`
- `charging/ui/page/device/a1780/a1780setting/a1780setting_logic.dart::showRemoveDialog`
- `charging/ui/page/device/a1781/a1781setting/a1781setting_logic.dart::showRemoveDialog`
- `charging/ui/page/device/a17b1/device_setting/a17b1device_setting_logic.dart::showRemoveDialog`
- `charging/ui/page/device/a17c0/a17c0home/a17c0home_logic.dart::_cloudA17Y0InfoSync`
- `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart::showRemoveDialog`
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart::showRemoveDialog`
- `charging/ui/page/device/a17x7/a17x7setting/a17x7setting_logic.dart::_handleRemoveDevice`
- `charging/ui/page/device/a17x8/a17x8setting/a17x8setting_logic.dart::showRemoveDialog`
- `charging/ui/page/device/a17y0/a17y0home/a17y0home_logic.dart::_removeCloudDeviceInfo`
- `charging/ui/page/device/a2345/a2345setting/a2345setting_logic.dart::showRemoveDialog`
- `charging/ui/page/device/a5140/a5140setting/a5140setting_logic.dart::show5143RemoveCardDialog`
- `charging/ui/page/device/a5140/a5140setting/a5140setting_logic.dart::showRemoveDialog`
- `charging/ui/page/device/a5143/match_bluetooth_scan/a5143_match_bluetooth_scan_logic.dart::_jumpToConnectBluetoothPage`
- `charging/ui/page/device/a91b2/a91b2setting/a91b2setting_logic.dart::showRemoveDialog`
- `charging/ui/page/device/cooler/a17a3setting/a17a3setting_logic.dart::showRemoveDialog`
- `charging/ui/page/device/cooler/coolerSetting/cooler_setting_logic.dart::showRemoveDialog`
- `charging/ui/page/device/third_party_device/shelly/shellyhome/shellyhome_logic.dart::_handleRemoveDevice`
- `charging/ui/page/device/third_party_device/shelly/shellysetting/shellysetting_logic.dart::showRemoveDialog`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What `unbind_type` carries (the sender stores a parameter; the callers of `deviceUnbind` were not decoded for the value). — attempted 2026-10-20 (two-hop not readable: the three `deviceUnbind` callers pass `r5 = true` or `r5 = false` as a bool constant (`charging/ui/page/device/a1340/a1340setting/a1340setting_logic.dart @0x3c23f2c`, `charging/ui/page/device/a1770/a1770setting/a1770setting_logic.dart @0x3c816b8`, `charging/ui/page/device/a5143/match_bluetooth_scan/a5143_match_bluetooth_scan_logic.dart @0x343070c`) and the other arguments as slots of their frames; the string `unbind_type` is not among the constants)
- Server behaviour for a parent device with children (`parent_device_sn`): not visible.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
