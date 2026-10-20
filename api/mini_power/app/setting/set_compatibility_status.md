> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# set_compatibility_status

## Purpose

Stores the compatibility switch of an A2345 charger on the laboratory page (caller `setCompatibilityStatusWithDevice` in the A2345 laboratory logic) (asm-traced, caller chain in `data/endpoints.json`; the meaning of the switch comes from the names only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /mini_power/v1/app/setting/set_compatibility_status` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3e55f4c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3e55f44`, in `HttpRequestControllerImpl::saveCompatibilityStatusSetting` (`charging/http/http_request_repository_impl.dart @0x3e55e80`), sent through `encryptionRequestHttp` (`@0x3e55f74`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) `HttpRequestControllerImpl::saveCompatibilityStatusSetting` (`charging/http/http_request_repository_impl.dart @0x3e55e80`) stores both keys unconditionally in a map literal with type arguments `<String, dynamic>` (`@0x3e55f04`), which types nothing by itself. The second value is an unboxed int parameter that the builder tags as a Smi (`lsl` `@0x3e55efc`). `device_sn` is typed from the caller: The only caller, `A2345LaboratoryLogic::setCompatibilityStatusWithDevice` (`charging/ui/page/device/a2345/a2345laboratory/a2345laboratory_logic.dart @0x3e55c10`), loads the device object from `field_7f` (`@0x3e55c94`), reads its value (`@0x3e55ce8`) and passes `field_6b` (`@0x3e55cec`) as `device_sn`, without a null branch; it passes the second value as an unboxed int built from a bool parameter (`tst x1, #0x10` `@0x3e55d04`) and calls the sender at `@0x3e55d50`. `field_7f` is created in the constructor `A2345LaboratoryLogic` (`charging/ui/page/device/a2345/a2345laboratory/a2345laboratory_logic.dart @0x4121cac`) as `<A2345AnkerDevice>` observable (`A2345AnkerDevice()` `@0x4121cd0`, type argument `@0x4121d10`, `RxT.obs` `@0x4121d24`, stored `@0x4121d2c`); `A2345AnkerDevice` extends a mixin application that includes `AnkerDevice` (`charging/ble/device/A2345/a2345_anker_device.dart`, class line 8), and `field_6b` of `AnkerDevice` is the getter declared `String dyn:get:deviceSn(AnkerDevice)` (`base_service/device/anker_device.dart @0x22053d4`, loads `field_6b` `@0x22053d8`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_request_repository_impl.dart @0x3e55ed8` (caller load `charging/ui/page/device/a2345/a2345laboratory/a2345laboratory_logic.dart @0x3e55cec` (see below)) |
| `compatibility_status` | int (Smi, w) | yes | | `charging/http/http_request_repository_impl.dart @0x3e55eec` (unboxed int parameter tagged by `lsl x2, x1, #1` `charging/http/http_request_repository_impl.dart @0x3e55efc` and stored with `stur w2` `@0x3e55f00`) |

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
  "compatibility_status": "<int>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure `charging/http/http_request_repository_impl.dart @0x226824c` forwards code and message to a stored callback without reading them). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `saveCompatibilityStatusSetting` @0x3e55e80 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::saveCompatibilityStatusSetting`
- `charging/ui/page/device/a2345/a2345laboratory/a2345laboratory_logic.dart::setCompatibilityStatusWithDevice`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The value domain of the switch: the caller sends 1 when its bool parameter is true and 0 otherwise (`tst` in `charging/ui/page/device/a2345/a2345laboratory/a2345laboratory_logic.dart @0x3e55d04`); the read side `get_device_setting` casts the same-named key to `int` (`charging/http/http_request_repository_impl.dart @0x28a7e74`).
- What the switch controls on the device (names only). — reclassified: device test row 154 (2026-10-20: what the setting does on the charger is behaviour of the device, only the endpoint and key names are in the app)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
