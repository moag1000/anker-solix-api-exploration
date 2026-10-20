> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

3.24.3: string present in the object pool, no code reference found (present in 3.18.0 with a sender)

# clear

## Purpose

Clears the disaster-preparedness (backup power) state of a device before the app also sends the clear command to the device itself (callers `clearDisasterPreparednessInfo` of the `PreparednessModuleMixin` copies in `A1782RestoreDefaultMenuController` and `DeviceMainLogic`) (3.18.0 asm: the HTTP call is followed by `AKIotDisasterPreparednessCommand::clearBackup`; the meaning is string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_disaster_prepared/clear`, method `POST` in the 3.18.0 asm: in `clearDisasterPreparednessInfo` (`charging/ui/page/device/a1782/a1782_setting/menu_controller/a1782_restore_default_controller.dart @0x366d558`, 3.18.0 addresses) the method object `Instance_Method` is loaded at `@0x366d614` (3.18.0 pool entry `pp+0x9b18`, enum index 1, `post`, per the 3.18.0 `pp.txt`), the URL string at `@0x366d61c`, and the request goes through `HttpServiceImpl::encryptionRequestHttp` (`@0x366d630`). The copy in `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x1f4a208` has the URL at `@0x1f4a2cc`. In 3.24.3 the URL string exists only in the object pool, so no sender can be read.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys in 3.24.3 (no sender). In the 3.18.0 asm both senders build the same two-key map with the type arguments `<String, Object>` (`charging/ui/page/device/a1782/a1782_setting/menu_controller/a1782_restore_default_controller.dart @0x366d5fc`), which name no value type.

| field | type | required | example | source |
|---|---|---|---|---|
| `identifier_id` | ? | yes | `"<id>"` | `charging/ui/page/device/a1782/a1782_setting/menu_controller/a1782_restore_default_controller.dart @0x366d5d8` (parameter, stored unconditionally at `@0x366d5e8`) |
| `type` | int (Smi, w) | yes | `1` (raw immediate 2, 32-bit store) | `charging/ui/page/device/a1782/a1782_setting/menu_controller/a1782_restore_default_controller.dart @0x366d5ec` (value store `@0x366d5f8`, constant `@0x366d5f4`) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (3.18.0 asm): the call passes no `success`, `fail` or `complete` closure (argument descriptor `charging/ui/page/device/a1782/a1782_setting/menu_controller/a1782_restore_default_controller.dart @0x366d62c` lists no named argument); the function continues with the device command `AKIotDisasterPreparednessCommand::clearBackup` (`charging/ui/page/device/a1782/a1782_setting/menu_controller/a1782_restore_default_controller.dart @0x366d63c`).

## Response

No response key is read by the app in the 3.18.0 asm (see Response model).

## Example request/response

Request, synthesized from the 3.18.0 asm (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "identifier_id": "<id>",
  "type": 1
}
```

Response: not synthesized (no capture exists for this endpoint).

## Errors seen

none traced: no 3.24.3 sender; the 3.18.0 closures read compare no numeric error code. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a1782/a1782_setting/menu_controller/a1782_restore_default_controller.dart`: `clearDisasterPreparednessInfo` @0x366d558 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart`: `clearDisasterPreparednessInfo` @0x1f4a208 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present (sender read in the 3.18.0 asm, addresses below are 3.18.0 addresses). 3.24.3: string present in the object pool, no code reference found. since: <=3.18.0. `tools/out/diff_3.18.0_3.24.3.md` lists the endpoint under removed endpoints.

## Known unknowns

- Whether the server still serves this URL: the 3.24.3 app has no sender for it; the diff file lists it as removed.
- Type of `identifier_id` (parameter) and what `type` 1 selects: read from the 3.18.0 asm only, the constants were not re-checked in 3.24.3. — traced 2026-10-20: a search of the whole 3.24.3 asm finds no `/charging_disaster_prepared/clear` literal (the other four endpoints of the service are loaded as literals), so the 3.18.0 constants cannot be re-checked; the endpoint has no 3.24.3 sender
- What replaced the call in 3.24.3: the sibling endpoints [get_site_device_disaster](get_site_device_disaster.md) and [get_support_func](get_support_func.md) are new; no new clear call was located. — traced 2026-10-20: no replacement is visible; the 3.24.3 literals of the service are `get_support_func`, `quit_disaster_prepare` (two `EmsServiceImpl` senders), `set_site_device_disaster` (`ManualPowerBackupLogic::_callSaveDisasterApi`) and `get_site_device_disaster`, and which of them takes over the role of `clear` was not decided

## Device-tested by

none
