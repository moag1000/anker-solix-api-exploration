> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# set_charging_device_identity_status_default_true

## Purpose

Sets the A2345 device-identity flag on the laboratory page (caller `setChargingDeviceModeSwitch` in the A2345 laboratory logic) (asm-traced, caller chain in `data/endpoints.json`; the meaning of the flag comes from the names only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /mini_power/v1/app/setting/set_charging_device_identity_status_default_true` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3e55938`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3e55930`, in `HttpRequestControllerImpl::setA2345DeviceIdentityStatus` (`charging/http/http_request_repository_impl.dart @0x3e55868`), sent through `encryptionRequestHttp` (`@0x3e55960`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) `HttpRequestControllerImpl::setA2345DeviceIdentityStatus` (`charging/http/http_request_repository_impl.dart @0x3e55868`) stores both keys unconditionally in a map literal with type arguments `<String, Object>` (`@0x3e558ec`), which types nothing by itself. The second value is an unboxed int parameter that the builder tags as a Smi (`lsl` `@0x3e558e4`). `device_sn` is typed from the caller: The only caller, `A2345LaboratoryLogic::setChargingDeviceModeSwitch` (`charging/ui/page/device/a2345/a2345laboratory/a2345laboratory_logic.dart @0x3e556e0`), loads the device object from `field_7f` (`@0x3e5577c`), reads its value (`@0x3e557d4`) and passes `field_6b` (`@0x3e557d8`) as `device_sn`, without a null branch; it passes the second value as an unboxed int built from a bool parameter (`tst x1, #0x10` `@0x3e557f0`) and calls the sender at `@0x3e55840`. `field_7f` is created in the constructor `A2345LaboratoryLogic` (`charging/ui/page/device/a2345/a2345laboratory/a2345laboratory_logic.dart @0x4121cac`) as `<A2345AnkerDevice>` observable (`A2345AnkerDevice()` `@0x4121cd0`, type argument `@0x4121d10`, `RxT.obs` `@0x4121d24`, stored `@0x4121d2c`); `A2345AnkerDevice` extends a mixin application that includes `AnkerDevice` (`charging/ble/device/A2345/a2345_anker_device.dart`, class line 8), and `field_6b` of `AnkerDevice` is the getter declared `String dyn:get:deviceSn(AnkerDevice)` (`base_service/device/anker_device.dart @0x22053d4`, loads `field_6b` `@0x22053d8`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_request_repository_impl.dart @0x3e558c0` (caller load `charging/ui/page/device/a2345/a2345laboratory/a2345laboratory_logic.dart @0x3e557d8` (see below)) |
| `charging_device_identity_status_default_true` | int (Smi, w) | yes | ? | `charging/http/http_request_repository_impl.dart @0x3e558d4` (unboxed int parameter tagged by `lsl x2, x1, #1` `charging/http/http_request_repository_impl.dart @0x3e558e4` and stored with `stur w2` `@0x3e558e8`) |

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
  "charging_device_identity_status_default_true": "<int>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure `charging/http/http_request_repository_impl.dart @0x226824c` forwards code and message to a stored callback without reading them). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `setA2345DeviceIdentityStatus` @0x3e55868 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ui/page/device/a2345/a2345laboratory/a2345laboratory_logic.dart::setChargingDeviceModeSwitch`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The value domain of the flag: the caller sends 1 when its bool parameter is true and 0 otherwise (`tst` `@0x3e557f0`, `cset`, `lsl`); what the server does with the numbers is not known.
- What the flag controls on the device (names only).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
