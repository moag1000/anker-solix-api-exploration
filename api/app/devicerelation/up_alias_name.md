> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# up_alias_name

## Purpose

Renames a device (alias name); sent by the rename dialogs of the device settings (`DeviceNameMenuController::showRenameDialog`, `A2693DeviceNameMenuController`, `DeviceModifyNameController`, `RenameDeviceController::save`) and by `A17X8DeviceController._renameDevice` (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/devicerelation/up_alias_name` (asm-traced): URL string at `a2693/pages/a2693setting/a2693DeviceNameMenuController.dart @0x2cfa7fc`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2cfa7f4`, in `A2693DeviceNameMenuController::updateDeviceName` (`a2693/pages/a2693setting/a2693DeviceNameMenuController.dart @0x2cfa6f4`), sent through `encryptionRequestHttp` (`@0x2cfa824`).

Same URL in the other sender(s) read:

- `POST /app/devicerelation/up_alias_name` (asm-traced): URL string at `base_service/view/general_setting/device_name_controller.dart @0x2cfb36c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2cfb364`, in `DeviceNameMenuController::updateDeviceName` (`base_service/view/general_setting/device_name_controller.dart @0x2cfb264`), sent through `encryptionRequestHttp` (`@0x2cfb394`).
- `POST /app/devicerelation/up_alias_name` (asm-traced): URL string at `base_service/view/general_setting/device_name_controller_rn.dart @0x2d016a8`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2d016a0`, in `DeviceNameRNMenuController::updateDeviceName` (`base_service/view/general_setting/device_name_controller_rn.dart @0x2d015a0`), sent through `encryptionRequestHttp` (`@0x2d016d0`).
- `POST /app/devicerelation/up_alias_name` (asm-traced): URL string at `charging/ble/device/A17X8/a17x8_device_controller.dart @0x241a2dc`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x241a2d4`, in `A17X8DeviceController::_renameDevice` (`charging/ble/device/A17X8/a17x8_device_controller.dart @0x241a184`), sent through `encryptionRequestHttp` (`@0x241a304`).
- `POST /app/devicerelation/up_alias_name` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x27617e4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x27617dc`, in `HttpRequestControllerImpl::updateDeviceName` (`charging/http/http_request_repository_impl.dart @0x2761700`), sent through `encryptionRequestHttp` (`@0x276180c`).
- `POST /app/devicerelation/up_alias_name` (asm-traced): URL string at `charging/ui/page/device/a25x7/a25x7setting/general/a25x7_device_name_controller.dart @0x2cfc9fc`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2cfc9f4`, in `A25x7DeviceNameMenuController::updateDeviceName` (`charging/ui/page/device/a25x7/a25x7setting/general/a25x7_device_name_controller.dart @0x2cfc8f4`), sent through `encryptionRequestHttp` (`@0x2cfca24`).
- `POST /app/devicerelation/up_alias_name` (asm-traced): URL string at `charging/ui/page/device/a2687/a2687setting/menu_controller/general/a2687_device_name_controller.dart @0x2d0e040`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2d0e038`, in `A2687DeviceNameMenuController::updateDeviceName` (`charging/ui/page/device/a2687/a2687setting/menu_controller/general/a2687_device_name_controller.dart @0x2d0df38`), sent through `encryptionRequestHttp` (`@0x2d0e068`).
- `POST /app/devicerelation/up_alias_name` (asm-traced): URL string at `small_charging_platform/src/scp/setting/menu_controller/device_modify_name_controller.dart @0x2cfbb24`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2cfbb1c`, in `DeviceModifyNameController::updateDeviceName` (`small_charging_platform/src/scp/setting/menu_controller/device_modify_name_controller.dart @0x2cfba1c`), sent through `encryptionRequestHttp` (`@0x2cfbb4c`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `a2693/pages/a2693setting/a2693DeviceNameMenuController.dart @0x2cfa774` (value store `@0x2cfa784`) |
| `device_mac` | string | yes | `"<device_mac>"` | `a2693/pages/a2693setting/a2693DeviceNameMenuController.dart @0x2cfa788` (value store `@0x2cfa798`) |
| `alias_name` | string | yes | `"<alias_name>"` | `a2693/pages/a2693setting/a2693DeviceNameMenuController.dart @0x2cfa79c` (value store `@0x2cfa7ac`) |

All values are Strings: the one map literal of each of the eight senders has type arguments `<String, String>` (for example `a2693/pages/a2693setting/a2693DeviceNameMenuController.dart @0x2cfa7b0`, `charging/http/http_request_repository_impl.dart @0x2761798`).

## `param_type`/`cmd`

n/a

## Response model (link)

not resolved (string-only): the senders pass shared closures that forward the response value unparsed to the caller's callback (`charging/http/http_request_repository_impl.dart @0x2268374` with `ClosureCall` `@0x22683a8`; `@0x24044f0`, `ClosureCall` `@0x240452c`); `A17X8DeviceController._renameDevice` ignores the value and completes its future (`charging/ble/device/A17X8/a17x8_device_controller.dart @0x241a3f4`). What the other callers do with the forwarded value was not traced.

## Response

Not listed: the callers' use of the forwarded value was not traced (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>",
  "device_mac": "<device_mac>",
  "alias_name": "<alias_name>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `a2693/pages/a2693setting/a2693DeviceNameMenuController.dart`: `updateDeviceName` @0x2cfa6f4 (encryptionRequestHttp; encrypted: true)
- `base_service/view/general_setting/device_name_controller.dart`: `updateDeviceName` @0x2cfb264 (encryptionRequestHttp; encrypted: true)
- `base_service/view/general_setting/device_name_controller_rn.dart`: `updateDeviceName` @0x2d015a0 (encryptionRequestHttp; encrypted: true)
- `charging/ble/device/A17X8/a17x8_device_controller.dart`: `_renameDevice` @0x241a184 (encryptionRequestHttp; encrypted: true)
- `charging/http/http_request_repository_impl.dart`: `updateDeviceName` @0x2761700 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/a25x7/a25x7setting/general/a25x7_device_name_controller.dart`: `updateDeviceName` @0x2cfc8f4 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/a2687/a2687setting/menu_controller/general/a2687_device_name_controller.dart`: `updateDeviceName` @0x2d0df38 (encryptionRequestHttp; encrypted: true)
- `small_charging_platform/src/scp/setting/menu_controller/device_modify_name_controller.dart`: `updateDeviceName` @0x2cfba1c (encryptionRequestHttp; encrypted: true)

Called from:

- `a2693/pages/a2693setting/a2693DeviceNameMenuController.dart::showRenameDialog`
- `base_service/view/general_setting/device_name_controller.dart::showRenameDialog`
- `base_service/view/general_setting/device_name_controller_rn.dart::showRenameDialog`
- `charging/ble/device/A17X8/a17x8_device_controller.dart::A17X8DeviceController`
- `charging/http/http_request_repository.dart::updateDeviceName`
- `charging/ui/page/device/a1340/a1340setting/a1340setting_logic.dart::_saveDeviceName`
- `charging/ui/page/device/a172x/a172xsetting/a172xsetting_logic.dart::_saveDeviceName`
- `charging/ui/page/device/a1770/a1770setting/a1770setting_logic.dart::_saveDeviceName`
- `charging/ui/page/device/a1780/a1780setting/a1780setting_logic.dart::_saveDeviceName`
- `charging/ui/page/device/a1781/a1781setting/a1781setting_logic.dart::_saveDeviceName`
- `charging/ui/page/device/a17b1/device_setting/a17b1device_setting_logic.dart::_saveDeviceName`
- `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart::_saveDeviceName`
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart::_saveDeviceName`
- `charging/ui/page/device/a17x7/a17x7setting/a17x7setting_logic.dart::_saveDeviceName`
- `charging/ui/page/device/a17x8/a17x8home/a17x8home_logic.dart::_saveDeviceName`
- `charging/ui/page/device/a17x8/a17x8scene_start/a17x8scene_start_logic.dart::_saveDeviceName`
- `charging/ui/page/device/a17x8/a17x8setting/a17x8setting_logic.dart::_saveDeviceName`
- `charging/ui/page/device/a2345/a2345setting/a2345setting_logic.dart::_saveDeviceName`
- `charging/ui/page/device/a25x7/a25x7setting/general/a25x7_device_name_controller.dart::showRenameDialog`
- `charging/ui/page/device/a2687/a2687setting/menu_controller/general/a2687_device_name_controller.dart::showRenameDialog`
- `charging/ui/page/device/a5101/device_home_page/device_home_logic.dart::_saveDeviceName`
- `charging/ui/page/device/a5101/setting/solix_setting/solix_setting_logic.dart::_saveDeviceName`
- `charging/ui/page/device/a5140/a5140setting/a5140setting_logic.dart::updateName`
- `charging/ui/page/device/a5150/homePage/a5150_home_logic.dart::showRenameDialog`
- `charging/ui/page/device/a91b2/a91b2setting/a91b2setting_logic.dart::_saveDeviceName`
- `charging/ui/page/device/connect/zx_connect_ble_success/zx_connect_ble_success_logic.dart::_updateDeviceName`
- `charging/ui/page/device/cooler/a17a3setting/a17a3setting_logic.dart::saveDeviceName`
- `charging/ui/page/device/cooler/coolerSetting/cooler_setting_logic.dart::saveDeviceName`
- `charging/ui/page/device/rename/rename_logic.dart::finish`
- `flutter_charging_beginning/beginning/state_cards/rename_device/rename_device_controller.dart::save`
- `small_charging_platform/src/scp/setting/menu_controller/device_modify_name_controller.dart::showRenameDialog`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Whether the callers of the rename dialogs read the response body: the closures forward it and the dialog code was not followed to the end.
- Length and character rules for `alias_name`: enforced on the server or in the dialog; neither was decoded here.
- Why eight senders exist: one per device family menu; the families are named by the controller classes.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
