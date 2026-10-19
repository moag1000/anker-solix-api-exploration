> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# up_alias_name

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/app/devicerelation/up_alias_name`, method: not extracted by the inventory <!-- TODO -->; string-only: `a2693/pages/a2693setting/a2693DeviceNameMenuController.dart @0x2cfa7fc`
(literal also at 7 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `a2693/pages/a2693setting/a2693DeviceNameMenuController.dart @0x2cfa6f4` |
| `device_mac` | ? | ? | ? | `a2693/pages/a2693setting/a2693DeviceNameMenuController.dart @0x2cfa6f4` |
| `alias_name` | ? | ? | ? | `a2693/pages/a2693setting/a2693DeviceNameMenuController.dart @0x2cfa6f4` |

Rows are the union over 8 senders; `source` is the first sender that sets the key.

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

- `a2693/pages/a2693setting/a2693DeviceNameMenuController.dart`: `updateDeviceName` @0x2cfa6f4 (encryptionRequestHttp; encrypted: true)
- `base_service/view/general_setting/device_name_controller.dart`: `updateDeviceName` @0x2cfb264 (encryptionRequestHttp; encrypted: true)
- `base_service/view/general_setting/device_name_controller_rn.dart`: `updateDeviceName` @0x2d015a0 (encryptionRequestHttp; encrypted: true)
- `charging/ble/device/A17X8/a17x8_device_controller.dart`: `_renameDevice` @0x241a184 (encryptionRequestHttp; encrypted: true)
- `charging/http/http_request_repository_impl.dart`: `updateDeviceName` @0x2761700 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/a25x7/a25x7setting/general/a25x7_device_name_controller.dart`: `updateDeviceName` @0x2cfc8f4 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/a2687/a2687setting/menu_controller/general/a2687_device_name_controller.dart`: `updateDeviceName` @0x2d0df38 (encryptionRequestHttp; encrypted: true)
- `small_charging_platform/src/scp/setting/menu_controller/device_modify_name_controller.dart`: `updateDeviceName` @0x2cfba1c (encryptionRequestHttp; encrypted: true)

Called from: `a2693/pages/a2693setting/a2693DeviceNameMenuController.dart::showRenameDialog`, `base_service/view/general_setting/device_name_controller.dart::showRenameDialog`, `base_service/view/general_setting/device_name_controller_rn.dart::showRenameDialog`, `charging/ble/device/A17X8/a17x8_device_controller.dart::A17X8DeviceController`, `charging/http/http_request_repository.dart::updateDeviceName`, `charging/ui/page/device/a1340/a1340setting/a1340setting_logic.dart::_saveDeviceName`, `charging/ui/page/device/a172x/a172xsetting/a172xsetting_logic.dart::_saveDeviceName`, `charging/ui/page/device/a1770/a1770setting/a1770setting_logic.dart::_saveDeviceName`, `charging/ui/page/device/a1780/a1780setting/a1780setting_logic.dart::_saveDeviceName`, `charging/ui/page/device/a1781/a1781setting/a1781setting_logic.dart::_saveDeviceName`, `charging/ui/page/device/a17b1/device_setting/a17b1device_setting_logic.dart::_saveDeviceName`, `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart::_saveDeviceName`, `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart::_saveDeviceName`, `charging/ui/page/device/a17x7/a17x7setting/a17x7setting_logic.dart::_saveDeviceName`, `charging/ui/page/device/a17x8/a17x8home/a17x8home_logic.dart::_saveDeviceName`, `charging/ui/page/device/a17x8/a17x8scene_start/a17x8scene_start_logic.dart::_saveDeviceName`, `charging/ui/page/device/a17x8/a17x8setting/a17x8setting_logic.dart::_saveDeviceName`, `charging/ui/page/device/a2345/a2345setting/a2345setting_logic.dart::_saveDeviceName`, `charging/ui/page/device/a25x7/a25x7setting/general/a25x7_device_name_controller.dart::showRenameDialog`, `charging/ui/page/device/a2687/a2687setting/menu_controller/general/a2687_device_name_controller.dart::showRenameDialog`, `charging/ui/page/device/a5101/device_home_page/device_home_logic.dart::_saveDeviceName`, `charging/ui/page/device/a5101/setting/solix_setting/solix_setting_logic.dart::_saveDeviceName`, `charging/ui/page/device/a5140/a5140setting/a5140setting_logic.dart::updateName`, `charging/ui/page/device/a5150/homePage/a5150_home_logic.dart::showRenameDialog`, `charging/ui/page/device/a91b2/a91b2setting/a91b2setting_logic.dart::_saveDeviceName`, `charging/ui/page/device/connect/zx_connect_ble_success/zx_connect_ble_success_logic.dart::_updateDeviceName`, `charging/ui/page/device/cooler/a17a3setting/a17a3setting_logic.dart::saveDeviceName`, `charging/ui/page/device/cooler/coolerSetting/cooler_setting_logic.dart::saveDeviceName`, `charging/ui/page/device/rename/rename_logic.dart::finish`, `flutter_charging_beginning/beginning/state_cards/rename_device/rename_device_controller.dart::save`, `small_charging_platform/src/scp/setting/menu_controller/device_modify_name_controller.dart::showRenameDialog`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
