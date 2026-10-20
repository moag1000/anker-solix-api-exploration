> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

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
| `device_sn` | string | yes |  | `charging/http/http_request_repository_impl.dart @0x38aa458` (typed by the one-hop caller trace in the second-hop paragraph below: `A2687ChargeModeLogic::setModeSubStatus` passes `field_3f?.field_6b ?? ""`, `String dyn:get:deviceSn(AnkerDevice)` `base_service/device/anker_device.dart @0x22053d4`) |
| `mode` | string | yes |  | `charging/http/http_request_repository_impl.dart @0x38aa46c` (parameter, not typed by the builder) |
| `protocol_key` | string | yes |  | `charging/http/http_request_repository_impl.dart @0x38aa480` (parameter, not typed by the builder) |
| `status` | bool | yes |  | `charging/http/http_request_repository_impl.dart @0x38aa494` (parameter, not typed by the builder) |

Second hop (app side, traced 2026-10-20, `charging/ui/page/device/a2687/a2687setting/a2687_charge_mode/a2687_charge_mode_view.dart`): `A2687ChargeModeLogic::setModeSubStatus` is called from five switch closures with the signature `(dynamic, bool)`; each passes the bool of the switch as `status` (`ldr x5, [fp, #0x10]`, `@0x38aa26c`, `@0x38aaf9c`, `@0x38ab0c0`, `@0x38ab17c`, `@0x38ab238`), so `status` is a bool. `protocol_key` is a string literal at each site: `"4.5-21V PPS"` (`@0x38aa27c`), `"5-16V PPS"` (`@0x38aafa4`), `"5-11V PPS"` (`@0x38ab0c8`), `"UFCS"` (`@0x38ab184`) and `"SCP"` (`@0x38ab240`). `mode` is the literal `"normal"` at the first site (`@0x38aa274`) and, at the second site, `"normal"` when a bool field of the closure context is true and `"ai"` otherwise (`@0x38aaf54`..`@0x38aaf64`); the other three sites pass the same kind of context slot (`@0x38ab0bc`, `@0x38ab178`, `@0x38ab234`). What a protocol key and the two modes mean on the charger is not known from the app.

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
  "mode": "<mode>",
  "protocol_key": "<protocol_key>",
  "status": "<status>"
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

- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
