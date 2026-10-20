> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_error_infos

## Purpose

Reads the error descriptions for the serial numbers and codes found by the A17B1 self-check (caller chain `A17B1SystemTestLogic::handlerSelfCheckError`, `HttpRequestController::getErrorInfos`, in `data/endpoints.json`) (asm-traced).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_energy_service/get_error_infos` (asm-traced): URL string `@0x26ec070`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x26ec068`, in `HttpRequestControllerImpl::getErrorInfos` (`charging/http/http_request_repository_impl.dart @0x26ebfbc`), sent through `HttpRequestControllerImpl::requestHttp` (`@0x26ec098`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) One sender, one key. The map literal has the type arguments `<String, Map>` (`charging/http/http_request_repository_impl.dart @0x26ec024`), so the value is a map; it is stored without a guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `sn_errors` | object | yes | `{"<sn>": ...}` | `charging/http/http_request_repository_impl.dart @0x26ec010` (value store `@0x26ec020`, parameter) |

## `param_type`/`cmd`

n/a

## Response model (link)

[`ErrorInfosModel`](../../models/other.md#errorinfosmodel), parsed by `ErrorInfosModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x26ec0e4` in the success closure `@0x26ec0b4`.

## Response

(asm-traced) Top-level keys of `ErrorInfosModel` (`data/models.json`, `charging::ErrorInfosModel`): `error_infos` (Iterable). The closure forwards the parsed model to the caller's callback.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "sn_errors": {
    "<sn>": "<error codes>"
  }
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getErrorInfos` @0x26ebfbc (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getErrorInfos`
- `charging/ui/page/device/a17b1/a17b1system_test/system_test_logic.dart::handlerSelfCheckError`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The value layout inside `sn_errors` (the field name suggests device serial numbers as keys; not shown by the asm): the literal type `<String, Map>` shows only that the value is a map; the caller `handlerSelfCheckError` builds it and was not read.
- The element structure of `error_infos`: owned by the model page.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
