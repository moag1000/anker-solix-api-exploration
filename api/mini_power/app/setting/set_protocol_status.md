> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# set_protocol_status

## Purpose

Stores the user's protocol-agreement decision for an A2687 charger (callers `setProtocolAgreementStatus` in the A2687 lab-function logic classes and two closures of the A2687 device-info service) (asm-traced, caller chain in `data/endpoints.json`; the meaning of the agreement comes from the names only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /mini_power/v1/app/setting/set_protocol_status` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x35407c4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x35407bc`, in `HttpRequestControllerImpl::setA2687ProtocolAgreementStatus` (`charging/http/http_request_repository_impl.dart @0x35406a8`), sent through `encryptionRequestHttp` (`@0x35407ec`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced for the stores, `?` where the value is not typed) `HttpRequestControllerImpl::setA2687ProtocolAgreementStatus` (`charging/http/http_request_repository_impl.dart @0x35406a8`) stores unconditionally in a map literal with type arguments `<String, Object>` (`@0x3540778`), which does not type `device_sn`. The second value is a bool that the builder derives from an integer parameter; the worksheet `tools/out/request_fields_all.json` lists it as the constant `false`, the asm shows the compare with the parameter.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x354073c` (parameter, not typed by the builder) |
| `protocol_status` | bool | yes | ? | `charging/http/http_request_repository_impl.dart @0x3540750` (`true` when the unboxed int parameter equals 1: `cmp x1, #1` `charging/http/http_request_repository_impl.dart @0x3540760`, `r1 = true` `@0x3540768`, `r1 = false` `@0x3540770`) |

Values the callers pass (traced 2026-10-20, app side): both `setProtocolAgreementStatus` functions (`charging/ui/page/device/a2687/a2687setting/a2687_lab_function/a2687_lab_function_logic.dart @0x38c683c` and `a2687_new_lab_function_logic.dart @0x38c8b4c`) receive a bool from a switch closure of their page (`(dynamic, bool)`, `a2687_lab_function_view.dart @0x38c6804`, `a2687_new_lab_function_view.dart @0x38c8b14`) and convert it to an integer before the call: `tst x1, #0x10` then `cset x2, eq` and a tag shift (`@0x38c6948`..`@0x38c6954`), i.e. 1 for true and 0 for false. So the callers pass 1 (switch on) or 0 (off), and the builder turns 1 back into `protocol_status: true`.

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
  "protocol_status": "<bool>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure `charging/http/http_request_repository_impl.dart @0x226824c` forwards code and message to a stored callback without reading them). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `setA2687ProtocolAgreementStatus` @0x35406a8 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ak_iot_kit/business/A2687/service/a2687_device_info_service.dart::<anonymous closure>@0x3540538`
- `charging/ak_iot_kit/business/A2687/service/a2687_device_info_service.dart::<anonymous closure>@0x3540844`
- `charging/ui/page/device/a2687/a2687setting/a2687_lab_function/a2687_lab_function_logic.dart::setProtocolAgreementStatus`
- `charging/ui/page/device/a2687/a2687setting/a2687_lab_function/a2687_new_lab_function_logic.dart::setProtocolAgreementStatus`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `device_sn`: a parameter stored into a `<String, Object>` literal; the callers' argument type was not read. — attempted 2026-10-20 (two-hop not readable: the callers `setProtocolAgreementStatus` pass slots of their own frames (`charging/ui/page/device/a2687/a2687setting/a2687_lab_function/a2687_new_lab_function_logic.dart @0x38c8c94`..`@0x38c8ca0`, `a2687_lab_function_logic.dart @0x38c6980`..`@0x38c698c`))
- What the user agrees to (the endpoint and key names are the only evidence); the read side is `get_protocol_status`. — reclassified: server (2026-10-20: the agreement text is not visible in the app code read here; the sender and getter names `A2687ProtocolAgreementStatus` and the callers `a2687_lab_function_logic.dart`, `a2687_new_lab_function_logic.dart` tie it to the A2687 lab-function pages)
- One-hop caller tracing (controller ruling): `A2687LabFunctionLogic::setProtocolAgreementStatus` (`charging/ui/page/device/a2687/a2687setting/a2687_lab_function/a2687_lab_function_logic.dart @0x38c683c`) and `A2687NewLabFunctionLogic::setProtocolAgreementStatus` (`charging/ui/page/device/a2687/a2687setting/a2687_lab_function/a2687_new_lab_function_logic.dart @0x38c8b4c`) pass `field_3f?.field_6b ?? ""` (`@0x38c691c`, `@0x38c8c2c`) like the other A2687 lab callers, but the two closures of the device-info service (`charging/ak_iot_kit/business/A2687/service/a2687_device_info_service.dart @0x3540538` and `@0x3540844`) take `device_sn` from their closure context (`LoadField r4 = r0->field_f` `@0x3540620`, `@0x3540914`), a captured value whose declared type was not traced, so the field stays `?`.
- Header stays `string-only` because the type of `device_sn` is missing. — rechecked 2026-10-20: still true; the typing attempts are recorded on the bullets of this section
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
