> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

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

(asm-traced for the stores, `?` where the value is not typed) `HttpRequestControllerImpl::setA2687StandardChargingDeviceModelIdentityStatus` (`charging/http/http_request_repository_impl.dart @0x38c971c`) stores unconditionally in a map literal with type arguments `<String, Object>` (`@0x38c97b0`), which does not type `device_sn`. The second value is a bool that the builder derives from an integer parameter. The worksheet `tools/out/request_fields_all.json` lists it as the constant `false`; the asm shows the compare with the parameter.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x38c9774` (parameter, not typed by the builder) |
| `charging_device_identity_new_status` | bool | yes | ? | `charging/http/http_request_repository_impl.dart @0x38c9788` (`true` when the unboxed int parameter equals 1: `cmp x1, #1` `charging/http/http_request_repository_impl.dart @0x38c9798`, `r1 = true` `@0x38c97a0`, `r1 = false` `@0x38c97a8`) |

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
  "device_sn": "<?>",
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

- Type of `device_sn`: a parameter stored into a `<String, Object>` literal; the caller's argument type was not read.
- Which integer values the caller passes (the builder sends `true` only for 1); the caller `setChargingDeviceIdentification` was not decoded for it.
- What the flag controls on the device (names only).
- Header stays `string-only` because the type of `device_sn` is missing.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
