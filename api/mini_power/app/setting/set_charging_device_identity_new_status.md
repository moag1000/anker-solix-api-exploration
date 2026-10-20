> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# set_charging_device_identity_new_status

## Purpose

Switches the new device-identity flag of an A2687 charger on the new laboratory-function page (caller `setChargingDeviceIdentification` in the A2687 new lab-function logic) (asm-traced, caller chain in `data/endpoints.json`; the meaning of the flag comes from the names only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /mini_power/v1/app/setting/set_charging_device_identity_new_status` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x38c97fc`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x38c97f4`, in `HttpRequestControllerImpl::setA2687StandardChargingDeviceModelIdentityStatus` (`charging/http/http_request_repository_impl.dart @0x38c971c`), sent through `encryptionRequestHttp` (`@0x38c9824`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) `HttpRequestControllerImpl::setA2687StandardChargingDeviceModelIdentityStatus` (`charging/http/http_request_repository_impl.dart @0x38c971c`) stores both keys unconditionally in a map literal with type arguments `<String, Object>` (`@0x38c97b0`). The second value is a bool that the builder derives from an integer parameter (`cmp x1, #1`); the worksheet `tools/out/request_fields_all.json` lists it as the constant `false`, the asm shows the compare with the parameter. `device_sn` is typed from the caller: The only caller, `A2687NewLabFunctionLogic::setChargingDeviceIdentification` (`charging/ui/page/device/a2687/a2687setting/a2687_lab_function/a2687_new_lab_function_logic.dart @0x38c95a4`), loads `field_3f` (`@0x38c966c`), null-checks it (`cmp w1, NULL` `@0x38c9674`), reads its `field_6b` (`@0x38c9684`) and replaces a null result by the empty string (`r4 = ""` `@0x38c9694`), so a String reaches the sender (call `@0x38c96fc`). `field_3f` is stored in `onInit` (`charging/ui/page/device/a2687/a2687setting/a2687_lab_function/a2687_new_lab_function_logic.dart @0x35e977c`) from the navigation arguments cast to `IotAnkerDevice?` (`r8 = IotAnkerDevice?` `@0x35e9834`, stored `@0x35e9850`). `IotAnkerDevice` extends a mixin application over `IotDeviceAdapter` (`charging/ble/device/iot_anker_device.dart`, class line 8), `IotDeviceAdapter` extends one over `AnkerDevice` (`base_service/device/iot_device_adapter.dart`, class line 8), and `field_6b` of `AnkerDevice` is the getter declared `String dyn:get:deviceSn(AnkerDevice)` (`base_service/device/anker_device.dart @0x22053d4`, loads `field_6b` `@0x22053d8`). The caller builds the int from a bool parameter (`tst x1, #0x10` `@0x38c96b0`, `cset`, `lsl`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_request_repository_impl.dart @0x38c9774` (caller load `charging/ui/page/device/a2687/a2687setting/a2687_lab_function/a2687_new_lab_function_logic.dart @0x38c9684` (see below)) |
| `charging_device_identity_new_status` | bool | yes | | `charging/http/http_request_repository_impl.dart @0x38c9788` (`true` when the unboxed int parameter equals 1: `cmp x1, #1` `charging/http/http_request_repository_impl.dart @0x38c9798`, `r1 = true` `@0x38c97a0`, `r1 = false` `@0x38c97a8`) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closure `charging/http/http_request_repository_impl.dart @0x261b9a0` calls the stored callback with the constant `true` (`@0x261b9cc`, `ClosureCall` `@0x261b9d4`) and reads no response key.

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>",
  "charging_device_identity_new_status": "<bool>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure `charging/http/http_request_repository_impl.dart @0x226824c` forwards code and message to a stored callback without reading them). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `setA2687StandardChargingDeviceModelIdentityStatus` @0x38c971c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ui/page/device/a2687/a2687setting/a2687_lab_function/a2687_new_lab_function_logic.dart::setChargingDeviceIdentification`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which integer values the caller passes: it sends 1 when its bool parameter is true and 0 otherwise (`tst` `@0x38c96b0`), so the builder sends `true` for 1 only.
- What the flag controls on the device (names only).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
