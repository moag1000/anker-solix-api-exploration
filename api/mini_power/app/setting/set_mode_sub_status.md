> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# set_mode_sub_status

## Purpose

Sets the on/off state of one protocol inside a charging mode of an A2687 charger (caller `setModeSubStatus` in the A2687 charge-mode logic) (asm-traced for the caller chain in `data/endpoints.json`; the meaning of `mode`, `protocol_key` and `status` comes from the names only, string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /mini_power/v1/app/setting/set_mode_sub_status` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x38aa4f4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x38aa4ec`, in `HttpRequestControllerImpl::setA2687ModeSubStatus` (`charging/http/http_request_repository_impl.dart @0x38aa3fc`), sent through `encryptionRequestHttp` (`@0x38aa51c`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced for the stores, `?` where the value is not typed) `HttpRequestControllerImpl::setA2687ModeSubStatus` (`charging/http/http_request_repository_impl.dart @0x38aa3fc`) stores unconditionally in a map literal with type arguments `<String, Object>` (`@0x38aa4a8`), which types no value; all four come from parameters.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes |  | `charging/http/http_request_repository_impl.dart @0x38aa458` (typed by the one-hop caller trace in Known unknowns: `A2687ChargeModeLogic::setModeSubStatus` passes `field_3f?.field_6b ?? ""`, `String dyn:get:deviceSn(AnkerDevice)` `base_service/device/anker_device.dart @0x22053d4`) |
| `mode` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x38aa46c` (parameter, not typed by the builder) |
| `protocol_key` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x38aa480` (parameter, not typed by the builder) |
| `status` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x38aa494` (parameter, not typed by the builder) |

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
  "mode": "<?>",
  "protocol_key": "<?>",
  "status": "<?>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure `charging/http/http_request_repository_impl.dart @0x226824c` forwards code and message to a stored callback without reading them). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `setA2687ModeSubStatus` @0x38aa3fc (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ui/page/device/a2687/a2687setting/a2687_charge_mode/a2687_charge_mode_logic.dart::setModeSubStatus`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of all four values: parameters stored into a `<String, Object>` literal; the caller's argument types were not read.
- The valid values of `mode`, `protocol_key` and `status`: the caller `setModeSubStatus` was not decoded for them.
- One-hop caller tracing (controller ruling): the only caller `A2687ChargeModeLogic::setModeSubStatus` (`charging/ui/page/device/a2687/a2687setting/a2687_charge_mode/a2687_charge_mode_logic.dart @0x38aa2a0`) passes `field_3f?.field_6b ?? ""` (`@0x38aa344`) as `device_sn`, but `mode`, `protocol_key` and `status` are its own untyped parameters (context stores `@0x38aa2e8`..`@0x38aa300`), so those three need a second hop and stay `?`.
- Header stays `string-only` because the types are missing.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
