> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

3.24.3: string present in the object pool, no code reference found (present in 3.18.0 with a sender)

# quit_disaster_prepare

## Purpose

Tells the cloud that the A1782 left the current disaster-preparedness event, before the app sends the quit command to the device (caller: the closure in `onQuitCurrentEvent` of the A1782 home logic mixin stack; the 3.18.0 success closure then refreshes the auto-disaster state and sends `setBackup` with `quitCurrentBackup`) (3.18.0 asm for the call chain; the meaning is string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_disaster_prepared/quit_disaster_prepare`, method `POST` in the 3.18.0 asm: in the closure `charging/ui/page/device/a1782/home/a1782_home_logic.dart @0x22a3384` (3.18.0 addresses) the method object `Instance_Method` is loaded at `@0x22a3504` (3.18.0 pool entry `pp+0x9b18`, enum index 1, `post`), the URL string at `@0x22a350c`, and the request goes through `HttpServiceImpl::encryptionRequestHttp` (`@0x22a3528`). In 3.24.3 the URL string exists only in the object pool, so no sender can be read.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys in 3.24.3 (no sender). In the 3.18.0 asm the map literal has the type arguments `<String, Object>` (`charging/ui/page/device/a1782/home/a1782_home_logic.dart @0x22a34d4`), which name no value type; array length raw 16 (`charging/ui/page/device/a1782/home/a1782_home_logic.dart @0x22a3460`), so four keys.

| field | type | required | example | source |
|---|---|---|---|---|
| `type` | int (Smi, w) | yes | `1` (raw immediate 2, 32-bit store) | `charging/ui/page/device/a1782/home/a1782_home_logic.dart @0x22a3468` (value store `@0x22a3474`, constant `@0x22a3470`) |
| `identifier_id` | ? | yes | `"<id>"` | `charging/ui/page/device/a1782/home/a1782_home_logic.dart @0x22a3478` (store `@0x22a34a8`; value from a chain of field loads `@0x22a3488`, `@0x22a34a0`) |
| `is_ble` | int (Smi, w) | yes | `1` (raw immediate 2, 32-bit store) | `charging/ui/page/device/a1782/home/a1782_home_logic.dart @0x22a34ac` (value store `@0x22a34bc`, constant `@0x22a34b8`) |
| `disaster_type` | int (Smi, w) | yes | `2` (raw immediate 4, 32-bit store) | `charging/ui/page/device/a1782/home/a1782_home_logic.dart @0x22a34c0` (value store `@0x22a34d0`, constant `@0x22a34cc`) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app as a model (3.18.0 asm): only a `success` closure is passed (argument descriptor `charging/ui/page/device/a1782/home/a1782_home_logic.dart @0x22a3520`); its body `@0x22a3560` logs a success line and calls `refreshAutoDisaster` (`@0x22a35dc`) and `AKIotDisasterPreparednessCommand::setBackup` (`@0x22a3640`); it reads no key of the response.

## Response

No response key is read by the app in the 3.18.0 asm (see Response model).

## Example request/response

Request, synthesized from the 3.18.0 asm (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "type": 1,
  "identifier_id": "<id>",
  "is_ble": 1,
  "disaster_type": 2
}
```

Response: not synthesized (no capture exists for this endpoint).

## Errors seen

none traced: no 3.24.3 sender; the 3.18.0 closures read compare no numeric error code. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a1782/home/a1782_home_logic.dart`: `<anonymous closure> in _A1782DeviceLogic&AnkerBaseController&DeviceCountDownLogic&DeviceBatteryStatusLogic&GetTickerProviderStateMixin&PreparednessModuleMixin&AutoDisasterPreparednessMixin::onQuitCurrentEvent` @0x22a3384 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present (sender read in the 3.18.0 asm, addresses below are 3.18.0 addresses). 3.24.3: string present in the object pool, no code reference found. since: <=3.18.0. `tools/out/diff_3.18.0_3.24.3.md` lists the endpoint under removed endpoints.

## Known unknowns

- Whether the server still serves this URL: the 3.24.3 app has no sender for it; the diff file lists it as removed.
- What `is_ble` 1, `disaster_type` 2 and `type` 1 select: constants read from the 3.18.0 asm only (decoded with `../v3.24.3/audit/SMI_RULE.md`, not re-checked in 3.24.3).
- Type of `identifier_id` (field-load chain, declared type not visible).

## Device-tested by

none
