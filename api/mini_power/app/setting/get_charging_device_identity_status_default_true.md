> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_charging_device_identity_status_default_true

## Purpose

Reads the A2345 device-identity status flag for the laboratory switch (callers `getDeviceIdentityStatusSwitch` in the A2345 home logic and the A2345 laboratory logic) (asm-traced, caller chain in `data/endpoints.json`; the meaning of the flag comes from the names only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /mini_power/v1/app/setting/get_charging_device_identity_status_default_true` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x28d8340`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x28d8338`, in `HttpRequestControllerImpl::getA2345DeviceIdentityStatus` (`charging/http/http_request_repository_impl.dart @0x28d828c`), sent through `encryptionRequestHttp` (`@0x28d8368`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) `HttpRequestControllerImpl::getA2345DeviceIdentityStatus` (`charging/http/http_request_repository_impl.dart @0x28d828c`) stores one key, `device_sn`, unconditionally in a map literal with type arguments `<String, String>` (`@0x28d82f4`), so the value is a String.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_request_repository_impl.dart @0x28d82e0` (map literal `<String, String>` `charging/http/http_request_repository_impl.dart @0x28d82f4`) |

## `param_type`/`cmd`

n/a

## Response model (link)

No model class (asm-traced): the success closure (`charging/http/http_request_repository_impl.dart @0x28d8384`) reads the key `charging_device_identity_status_default_true` (`@0x28d83b8`) without a cast or a default and passes a one-entry map `{"status": <value>}` to the callback (key literal `@0x28d83f0`, `ClosureCall` `@0x28d8418`).

## Response

Top-level key read by the app: `charging_device_identity_status_default_true` (value type not checked by the closure); the callback receives it under the key `status`. No other key is read.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure `charging/http/http_request_repository_impl.dart @0x226824c` forwards code and message to a stored callback without reading them). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getA2345DeviceIdentityStatus` @0x28d828c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getA2345DeviceIdentityStatus`
- `charging/ui/page/device/a2345/a2345home/a2345home_logic.dart::getDeviceIdentityStatusSwitch`
- `charging/ui/page/device/a2345/a2345laboratory/a2345laboratory_logic.dart::getDeviceIdentityStatusSwitch`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The type of the returned value (bool or int): the closure forwards it unchecked; the callers `getDeviceIdentityStatusSwitch` were not decoded for it.
- What the flag controls on the device (names only). — reclassified: device test row 154 (2026-10-20: what the setting does on the charger is behaviour of the device, only the endpoint and key names are in the app)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
