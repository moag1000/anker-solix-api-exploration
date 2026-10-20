> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

3.24.3: the URL literal is loaded by `ManualPowerBackupLogic::_callSaveDisasterApi` (found by a string search of the asm on 2026-10-20; the endpoint inventory has no row for it, see Request); 3.18.0 has its own sender

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

3.24.3 sender (app side, traced 2026-10-20): `ManualPowerBackupLogic::_callSaveDisasterApi` (`ak_soft_ems/manual_power_backup/manual_power_backup_logic.dart @0x25ecb7c`) sends the URL literal `/charging_disaster_prepared/set_site_device_disaster` (`@0x25ece54`) through `getDataFromService` (`@0x25ece64`) with a map `<String, Object>` of four keys (`AllocateArray` of 16 raw, `@0x25eccfc`, so 4 pairs): `type` is 1 when the bool field `field_63` of the logic is true and 2 when it is false (`tst x2, #0x10` `@0x25ecd18`, `csetm`, `and`, `add x3, x3, #4` `@0x25ecd1c`..`@0x25ecd24`: raw 2 or raw 4 in a tagged slot); `identifier_id` is `field_4b` of the logic (`@0x25ecd38`); `manual_disaster_switch` is a value stored from a register (`@0x25ecd54`, not decoded here); `manual_disaster_detail` is a nested map `<String, int>` (`@0x25ecde0`) with `disaster_type` = raw 4, so 2 (`@0x25ecd80`), `start_time` and `end_time`, both boxed from unboxed 64-bit values (`BoxInt64Instr` `@0x25ecd98`, `@0x25ecdc0`). The 3.18.0 body below (`type`, `identifier_id`, `auto_disaster_switch`) is a different shape; this page was not re-audited field by field against the 3.24.3 sender. The switch variant of the 3.24.3 call (`_setSiteDeviceDisaster` chooses between `_sendDeviceCommand` `@0x29c2720` and `_callSaveDisasterApi` `@0x29c272c`) was not followed.

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

3.18.0: present (sender read in the 3.18.0 asm, addresses below are 3.18.0 addresses). 3.24.3: present (sender `ManualPowerBackupLogic::_callSaveDisasterApi`, see Request). since: <=3.18.0. `tools/out/diff_3.18.0_3.24.3.md` lists the endpoint under removed endpoints because the inventory missed the 3.24.3 literal, not because the app dropped the call.

## Known unknowns

- Whether the server serves this URL for the 3.24.3 request: the app does send it (`_callSaveDisasterApi`, see Request); the answer of the server is not known from the app.
- Type of `identifier_id` and `auto_disaster_switch` (field values with no visible declared type) and what `type` 1 selects. — attempted 2026-10-20 (two-hop not readable for the 3.24.3 body: `identifier_id` is `field_4b` and `type` depends on the bool `field_63` of `ManualPowerBackupLogic` (`ak_soft_ems/manual_power_backup/manual_power_backup_logic.dart @0x25ecd38`, `@0x25ecd10`); `auto_disaster_switch` is not a key of the 3.24.3 body)
- Which call replaced it in 3.24.3: not replaced, the 3.24.3 app sends this URL from `ManualPowerBackupLogic::_callSaveDisasterApi` with a different body (see Request); traced 2026-10-20.

## Device-tested by

none
