> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# report_easter_egg_trigger_status

## Purpose

Reports an easter-egg status record for a charger from the easter-egg pages (callers `requestAddEasterEggStatusRecord` in the A2345 and A91B2 easter-egg logic) (asm-traced for the caller chain in `data/endpoints.json`; what the status means is inferred from the names, string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /mini_power/v1/app/egg/report_easter_egg_trigger_status` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3e3c0ac`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3e3c0a4`, in `HttpRequestControllerImpl::addEasterEggStatusRecord` (`charging/http/http_request_repository_impl.dart @0x3e3bf9c`), sent through `encryptionRequestHttp` (`@0x3e3c0d4`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced for the stores, `?` where the value is not typed) `HttpRequestControllerImpl::addEasterEggStatusRecord` (`charging/http/http_request_repository_impl.dart @0x3e3bf9c`) stores three keys unconditionally in a map literal with type arguments `<String, Object>` (`@0x3e3c060`), which does not type `device_sn`; the two integer values are unboxed 64-bit values boxed by `BoxInt64Instr`.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3e3bffc` (parameter, not typed by the builder) |
| `egg_type` | int (unboxed, x) | yes | ? | `charging/http/http_request_repository_impl.dart @0x3e3c010` (value boxed by `BoxInt64Instr` `charging/http/http_request_repository_impl.dart @0x3e3c020`) |
| `report_time` | int (unboxed, x) | yes | ? | `charging/http/http_request_repository_impl.dart @0x3e3c038` (value boxed by `BoxInt64Instr` `@0x3e3c048`) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closure `charging/http/http_request_repository_impl.dart @0x261b9a0` calls the stored callback with the constant `true` (`@0x261b9cc`) and reads no response key.

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<?>",
  "egg_type": "<int>",
  "report_time": "<int>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure `charging/http/http_request_repository_impl.dart @0x226824c` forwards code and message to a stored callback without reading them). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `addEasterEggStatusRecord` @0x3e3bf9c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::addEasterEggStatusRecord`
- `charging/ui/page/device/a2345/a2345easter_egg/a2345easter_egg_logic.dart::requestAddEasterEggStatusRecord`
- `charging/ui/page/device/a91b2/a91b2easter_egg/a91b2easter_egg_logic.dart::requestAddEasterEggStatusRecord`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `device_sn`: a parameter stored into a `<String, Object>` literal; the callers' argument type was not read.
- What `egg_type` and `report_time` carry (value domain, time unit): the callers were not decoded for them.
- What "status" the record reports: the endpoint name is the only evidence.
- Header stays `string-only` because the type of `device_sn` is missing.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
