> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

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

(asm-traced for the stores, `?` where the value is not typed) `HttpRequestControllerImpl::saveCompatibilityStatusSetting` (`charging/http/http_request_repository_impl.dart @0x3e55e80`) stores both keys unconditionally in a map literal with type arguments `<String, dynamic>` (`@0x3e55f04`), which types neither value; both come from parameters.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3e55ed8` (parameter, not typed by the builder) |
| `compatibility_status` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3e55eec` (parameter, not typed by the builder) |

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
  "compatibility_status": "<?>"
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

- Types of `device_sn` and `compatibility_status`: parameters stored into a `<String, dynamic>` literal; the caller's argument types were not read. The read side `get_device_setting` casts the same-named key to `int` (`charging/http/http_request_repository_impl.dart @0x28a7e74`), which does not prove the write-side type.
- Value domain of the switch.
- Header stays `string-only` because both types are missing.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
