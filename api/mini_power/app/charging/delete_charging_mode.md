> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# delete_charging_mode

## Purpose

Deletes one custom charging mode of an A2345 or A2687 charger by its id (`_deleteCustomChargeModeByCloud` in the A2345 and A2687 custom-mode logic classes) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /mini_power/v1/app/charging/delete_charging_mode` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x26c4004`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x26c3ffc`, in `HttpRequestControllerImpl::deleteCustomChargeMode` (`charging/http/http_request_repository_impl.dart @0x26c3f3c`), sent through `encryptionRequestHttp` (`@0x26c402c`).

Same URL and method object in the other sender(s) read:

- `POST /mini_power/v1/app/charging/delete_charging_mode` (asm-traced): URL string at `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x3a9f534`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3a9f52c`, in `CustomChargeCloudApi::deleteCustomChargeMode` (`small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x3a9f464`), sent through `encryptionRequestHttp` (`@0x3a9f55c`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) Both senders store one key, `id`, unconditionally in a map literal with type arguments `<String, int>` (`charging/http/http_request_repository_impl.dart @0x26c3fbc`; second sender `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x3a9f500`); the value is an unboxed 64-bit integer boxed by `BoxInt64Instr` (`charging/http/http_request_repository_impl.dart @0x26c3fa4`; second sender `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x3a9f4e8`).

| field | type | required | example | source |
|---|---|---|---|---|
| `id` | int (unboxed, x) | yes | | `charging/http/http_request_repository_impl.dart @0x26c3f94` (map literal `<String, int>` `charging/http/http_request_repository_impl.dart @0x26c3fbc`, value boxed by `BoxInt64Instr` `@0x26c3fa4`) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closure `charging/http/http_request_repository_impl.dart @0x261b9a0` calls the stored callback with the constant `true` (`@0x261b9cc`, `ClosureCall` `@0x261b9d4`) and reads no response key; the second sender's success closure (`small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x3192444`) does the same (`@0x3192470`, `ClosureCall` `@0x3192478`).

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "id": "<int>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure `charging/http/http_request_repository_impl.dart @0x226824c` forwards code and message to a stored callback without reading them). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `deleteCustomChargeMode` @0x26c3f3c (encryptionRequestHttp; encrypted: true)
- `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart`: `deleteCustomChargeMode` @0x3a9f464 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::deleteCustomChargeMode`
- `charging/ui/page/device/a2345/a2345custom_charging_mode/a2345custom_charging_mode_logic.dart::_deleteCustomChargeModeByCloud`
- `charging/ui/page/device/a2687/a2687setting/a2687_charge_mode/a2687_custom_charge_mode/a2687_custom_charge_mode_logic.dart::_deleteCustomChargeModeByCloud`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types). The `small_charging_platform` sender was not compared with 3.18.0.

## Known unknowns

- What the server does when the mode is in use by a device, or when the id does not exist: the app ignores the answer body (see Response model).
- Which id the callers pass beyond "the `id` returned by `add_charging_mode` or listed by `get_charging_mode_list`" (the callers were not decoded for it).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
