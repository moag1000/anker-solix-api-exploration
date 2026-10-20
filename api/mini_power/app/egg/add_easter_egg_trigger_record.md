> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# add_easter_egg_trigger_record

## Purpose

Uploads an easter-egg trigger record that a charger reported over BLE (callers `parseUploadEasterEggTrigger` in the A2345 and A91B2 device-command classes) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /mini_power/v1/app/egg/add_easter_egg_trigger_record` (asm-traced): URL string at `charging/http/http_business_impl.dart @0x3b2d694`, in `HttpBusinessImpl::addEasterEggRecord` (`charging/http/http_business_impl.dart @0x3b2d58c`), sent through `HttpBusinessImpl::encryptionRequestHttp` (call `@0x3b2d6b0`). The call passes no method argument (argument descriptor `@0x3b2d6ac`); `HttpBusinessImpl::encryptionRequestHttp` (`charging/http/http_business_impl.dart @0x2618680`) supplies the method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x261877c` when it forwards the request.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced for the stores, `?` where the value is not typed) `HttpBusinessImpl::addEasterEggRecord` (`charging/http/http_business_impl.dart @0x3b2d58c`) stores three keys unconditionally in a map literal with type arguments `<String, Object>` (`@0x3b2d650`), which does not type `device_sn`; the two integer values are unboxed 64-bit values boxed by `BoxInt64Instr`.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | yes | ? | `charging/http/http_business_impl.dart @0x3b2d5ec` (parameter, not typed by the builder) |
| `egg_type` | int (unboxed, x) | yes | ? | `charging/http/http_business_impl.dart @0x3b2d600` (value boxed by `BoxInt64Instr` `charging/http/http_business_impl.dart @0x3b2d610`) |
| `trigger_time` | int (unboxed, x) | yes | ? | `charging/http/http_business_impl.dart @0x3b2d628` (value boxed by `BoxInt64Instr` `@0x3b2d638`) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closure `charging/http/http_request_repository_impl.dart @0x261b9a0` calls the stored callback with the constant `true` (`@0x261b9cc`) and reads no response key; the failure closure `@0x226824c` forwards its two arguments (`ClosureCall` `@0x2268288`).

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<?>",
  "egg_type": "<int>",
  "trigger_time": "<int>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure `charging/http/http_request_repository_impl.dart @0x226824c` forwards code and message to a stored callback without reading them). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_business_impl.dart`: `addEasterEggRecord` @0x3b2d58c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ble/device/A2345/a2345_device_commands.dart::parseUploadEasterEggTrigger`
- `charging/ble/device/A91B2/a91b2_device_commands.dart::parseUploadEasterEggTrigger`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `device_sn`: a parameter stored into a `<String, Object>` literal; the callers' argument type was not read. — attempted 2026-10-20 (two-hop not readable: the two callers of `A2345DeviceCommands::parseUploadEasterEggTrigger` are `_handleResponse` of the A2345 and A91B2 controllers (`charging/ble/device/A2345/a2345_device_controller.dart @0x3b290f8`, `charging/ble/device/A91B2/a91b2_device_controller.dart @0x3b5d754`); the chain `field_f` then `field_6b` of the passed object (`a2345_device_commands.dart @0x3b2d518`, `@0x3b2d520`) is not declared)
- Which `egg_type` values exist and what unit `trigger_time` uses (seconds or milliseconds): the values come from the BLE parser's arguments (`parseUploadEasterEggTrigger`), which were not decoded for this. — reclassified: device test row 154 (2026-10-20: egg numbers and times are produced by the charger and passed on by the BLE parser)
- Whether the server deduplicates repeated records.
- One-hop caller tracing (controller ruling): `A2345DeviceCommands::parseUploadEasterEggTrigger` (`charging/ble/device/A2345/a2345_device_commands.dart @0x3b2d3c8`) reads `device_sn` as `field_f` of its first argument (`@0x3b2d518`) and `field_6b` of that (`@0x3b2d520`); the argument is an untyped parameter of the BLE parser (`SetupParameters` `@0x3b2d3d4`), so its class and the declared type of that field were not established, and the A91B2 parser was not traced. — attempted 2026-10-20 again: `A2345DeviceController::_handleResponse` passes `this` (the controller object, `fp-8`) as the first argument (`charging/ble/device/A2345/a2345_device_controller.dart @0x3b290f4`..`@0x3b290f8`); `field_f` of that object belongs to the mixin `DeviceController` (`charging/ble/device/device_controller.dart`) whose field types are not declared in the dump, so the class behind `field_f.field_6b` is not shown (the A91B2 caller was not traced); two-hop not readable
- Header stays `string-only` because the type of `device_sn` is missing. — rechecked 2026-10-20: still true; the typing attempts are recorded on the bullets of this section
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
