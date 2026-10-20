> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_charging_device_identity_new_status

## Purpose

Reads the new device-identity status flag of an A2687 charger for the laboratory switch on the A2687 home page (caller `getLaboratorySwitch` in the A2687 home logic) (asm-traced, caller chain in `data/endpoints.json`; the meaning of the flag comes from the names only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /mini_power/v1/app/setting/get_charging_device_identity_new_status` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x353dac0`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x353dab8`, in `HttpRequestControllerImpl::getA2687StandardChargingDeviceModelIdentityStatus` (`charging/http/http_request_repository_impl.dart @0x353da0c`), sent through `encryptionRequestHttp` (`@0x353dae8`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) `HttpRequestControllerImpl::getA2687StandardChargingDeviceModelIdentityStatus` (`charging/http/http_request_repository_impl.dart @0x353da0c`) stores one key, `device_sn`, unconditionally in a map literal with type arguments `<String, String>` (`@0x353da74`), so the value is a String.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_request_repository_impl.dart @0x353da60` (map literal `<String, String>` `charging/http/http_request_repository_impl.dart @0x353da74`) |

## `param_type`/`cmd`

n/a

## Response model (link)

No model class (asm-traced): the success closure (`charging/http/http_request_repository_impl.dart @0x353db04`) reads the key `charging_device_identity_new_status` (`@0x353db38`), replaces `null` by `false` (`cmp w0, NULL` `@0x353db4c`, `r4 = false` `@0x353db54`), casts the value to `bool` (`r8 = bool` `@0x353db8c`) and passes a one-entry map with the same key to the callback (map literal `@0x353dbd0`, `ClosureCall` `@0x353dbe0`).

## Response

Top-level key read by the app: `charging_device_identity_new_status` (bool, `false` when absent). No other key is read.

Use of the flag (traced 2026-10-20, app side): the success closure in `A2687HomeLogic::getLaboratorySwitch` (`charging/ui/page/device/a2687/a2687home/a2687_home_logic.dart @0x353dc04`, argument `Map`) reads the key as a `bool` (`@0x353dca4`..`@0x353dcb8`), compares it with the device-side value `_deviceLabSwitchForCloudCompare` (`@0x353dcdc`; that function reads `getLocalChargingDeviceIdentityStandardStatus`, `@0x353e2c4`, when the device is connected, `@0x353e26c`) and, when they differ (`cmp w0, w1` `@0x353dd00`), sends the cloud value to the device with `_sendStandardChargingIdentityToDeviceWithRetry` (`@0x353dd24`). The sibling closure for `get_device_setting` (`@0x353e400`) reads the integer `charging_device_identity_status` and stores it for the device serial number with `setDeviceChargingIdentityStatus` (`@0x353e508`). So the bool is the cloud copy of the identity switch that the app pushes to a connected A2687, and the integer is the stored per-device status; the two are separate keys with separate uses.

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

- `charging/http/http_request_repository_impl.dart`: `getA2687StandardChargingDeviceModelIdentityStatus` @0x353da0c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ui/page/device/a2687/a2687home/a2687_home_logic.dart::getLaboratorySwitch`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the flag controls on the device: the endpoint and key names are the only evidence. — reclassified: device test row 154 (2026-10-20: what the setting does on the charger is behaviour of the device, only the endpoint and key names are in the app)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
