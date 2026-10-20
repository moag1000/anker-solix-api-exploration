> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

3.24.3: string present in the object pool, no code reference found (present in 3.18.0 with a sender)

# set_site_device_disaster

## Purpose

Writes the automatic disaster-preparedness switch of a site (caller `_updateAutoDisasterSwitch` of the A1782 modules logic mixin stack; the 3.18.0 success closure then sends the switch to the device with `sendCommandToSetPreparednessSwitch`) (3.18.0 asm for the call chain; the meaning is string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_disaster_prepared/set_site_device_disaster`, method `POST` in the 3.18.0 asm: in `_updateAutoDisasterSwitch` (`charging/ui/page/device/a1782/module_list/modules_logic.dart @0x1dc5f6c`, 3.18.0 addresses) the method object `Instance_Method` is loaded at `@0x1dc6240` (3.18.0 pool entry `pp+0x9b18`, enum index 1, `post`), the URL string at `@0x1dc6248`, and the request goes through `HttpServiceImpl::encryptionRequestHttp` (`@0x1dc6264`). In 3.24.3 the URL string exists only in the object pool, so no sender can be read.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys in 3.24.3 (no sender). In the 3.18.0 asm the map literal has the type arguments `<String, Object>` (`charging/ui/page/device/a1782/module_list/modules_logic.dart @0x1dc6210`), which name no value type; array length raw 12 (`charging/ui/page/device/a1782/module_list/modules_logic.dart @0x1dc61b0`), so three keys.

| field | type | required | example | source |
|---|---|---|---|---|
| `type` | int (Smi, w) | yes | `1` (raw immediate 2, 32-bit store) | `charging/ui/page/device/a1782/module_list/modules_logic.dart @0x1dc61b8` (value store `@0x1dc61c4`, constant `@0x1dc61c0`) |
| `identifier_id` | ? | yes | `"<id>"` | `charging/ui/page/device/a1782/module_list/modules_logic.dart @0x1dc61c8` (store `@0x1dc61f0`; value from field loads `@0x1dc61d8`, `@0x1dc61e8`) |
| `auto_disaster_switch` | ? | yes | `<switch>` | `charging/ui/page/device/a1782/module_list/modules_logic.dart @0x1dc61f4` (value store `@0x1dc620c`, `LoadField` `@0x1dc6204`) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app as a model (3.18.0 asm): only a `success` closure is passed (argument descriptor `charging/ui/page/device/a1782/module_list/modules_logic.dart @0x1dc625c`); its body `@0x1dc6bf0` logs a success line and calls `sendCommandToSetPreparednessSwitch` (`@0x1dc6cb4`), then unlocks the status (`@0x1dc6d4c`); it reads no key of the response.

## Response

No response key is read by the app in the 3.18.0 asm (see Response model).

## Example request/response

Request, synthesized from the 3.18.0 asm (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "type": 1,
  "identifier_id": "<id>",
  "auto_disaster_switch": "<switch>"
}
```

Response: not synthesized (no capture exists for this endpoint).

## Errors seen

none traced: no 3.24.3 sender; the 3.18.0 closures read compare no numeric error code. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a1782/module_list/modules_logic.dart`: `_updateAutoDisasterSwitch` @0x1dc5f6c (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present (sender read in the 3.18.0 asm, addresses below are 3.18.0 addresses). 3.24.3: string present in the object pool, no code reference found. since: <=3.18.0. `tools/out/diff_3.18.0_3.24.3.md` lists the endpoint under removed endpoints.

## Known unknowns

- Whether the server still serves this URL: the 3.24.3 app has no sender for it; the diff file lists it as removed.
- Type of `identifier_id` and `auto_disaster_switch` (field values with no visible declared type) and what `type` 1 selects.
- Which call replaced it in 3.24.3: `DisasterSetting` is still parsed from [get_site_device_disaster](get_site_device_disaster.md), but no new write call was located.

## Device-tested by

none
