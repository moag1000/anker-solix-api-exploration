> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# set_charging_device_identity_status

## Purpose

Sets the device-identity status of an A2687 charger on the laboratory-function page (caller `setIdentityStatus` in the A2687 lab-function logic) (asm-traced, caller chain in `data/endpoints.json`; the meaning of the status comes from the names only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /mini_power/v1/app/setting/set_charging_device_identity_status` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x38c76c0`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x38c76b8`, in `HttpRequestControllerImpl::setA2687ChargingDeviceModelIdentityStatus` (`charging/http/http_request_repository_impl.dart @0x38c75f0`), sent through `encryptionRequestHttp` (`@0x38c76e8`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) `HttpRequestControllerImpl::setA2687ChargingDeviceModelIdentityStatus` (`charging/http/http_request_repository_impl.dart @0x38c75f0`) stores both keys unconditionally in a map literal with type arguments `<String, Object>` (`@0x38c7674`), which types nothing by itself. The second value is an unboxed int parameter that the builder tags as a Smi (`lsl` `@0x38c766c`). `device_sn` is typed from the caller: The only caller, `A2687LabFunctionLogic::setIdentityStatus` (`charging/ui/page/device/a2687/a2687setting/a2687_lab_function/a2687_lab_function_logic.dart @0x38c7478`), loads `field_3f` (`@0x38c7540`), null-checks it (`cmp w1, NULL` `@0x38c7548`), reads its `field_6b` (`@0x38c7558`) and replaces a null result by the empty string (`r4 = ""` `@0x38c7568`), so a String reaches the sender (call `@0x38c75d0`). `field_3f` is stored in `onInit` (`charging/ui/page/device/a2687/a2687setting/a2687_lab_function/a2687_lab_function_logic.dart @0x35e9250`) from the navigation arguments cast to `IotAnkerDevice?` (`r8 = IotAnkerDevice?` `@0x35e9308`, stored `@0x35e9324`). `IotAnkerDevice` extends a mixin application over `IotDeviceAdapter` (`charging/ble/device/iot_anker_device.dart`, class line 8), `IotDeviceAdapter` extends one over `AnkerDevice` (`base_service/device/iot_device_adapter.dart`, class line 8), and `field_6b` of `AnkerDevice` is the getter declared `String dyn:get:deviceSn(AnkerDevice)` (`base_service/device/anker_device.dart @0x22053d4`, loads `field_6b` `@0x22053d8`). The caller builds the int from a bool parameter (`tst x1, #0x10` `@0x38c7584`, `cset`, `lsl`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_request_repository_impl.dart @0x38c7648` (caller load `charging/ui/page/device/a2687/a2687setting/a2687_lab_function/a2687_lab_function_logic.dart @0x38c7558` (see below)) |
| `charging_device_identity_status` | int (Smi, w) | yes | | `charging/http/http_request_repository_impl.dart @0x38c765c` (unboxed int parameter tagged by `lsl x2, x1, #1` `charging/http/http_request_repository_impl.dart @0x38c766c` and stored with `stur w2` `@0x38c7670`) |

Values sent (app side, traced 2026-10-20): The caller sends 1 when its bool parameter is true and 0 otherwise; the read side `get_device_setting` casts the same-named key to `int` (`charging/http/http_request_repository_impl.dart @0x28a7eec`).

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
  "charging_device_identity_status": "<int>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure `charging/http/http_request_repository_impl.dart @0x226824c` forwards code and message to a stored callback without reading them). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `setA2687ChargingDeviceModelIdentityStatus` @0x38c75f0 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ui/page/device/a2687/a2687setting/a2687_lab_function/a2687_lab_function_logic.dart::setIdentityStatus`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the status controls on the device (names only). — reclassified: device test row 154 (2026-10-20: what the setting does on the charger is behaviour of the device, only the endpoint and key names are in the app)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
