> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# un_relate_and_unbind_device

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/app/devicerelation/un_relate_and_unbind_device`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_business_impl.dart @0x33f7f68`
(literal also at 2 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `charging/http/http_business_impl.dart @0x33f7e44` |
| `bt_ble_mac` | ? | ? | ? | `charging/http/http_business_impl.dart @0x33f7e44` |
| `parent_device_sn` | ? | ? | ? | `charging/http/http_business_impl.dart @0x33f7e44` |
| `parent_device_pn` | ? | ? | ? | `charging/http/http_business_impl.dart @0x33f7e44` |
| `unbind_type` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3430a64` |

Rows are the union over 3 senders; `source` is the first sender that sets the key.

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

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
