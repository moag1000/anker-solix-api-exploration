> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# sync_installation_inspection

## Purpose

Reports the A17B1 installation inspection (page reached and errors) to the cloud (callers `ElectricitySceneLogic::createOrJoinSuccess` and `syncGoHome`, `A17B1SystemTestLogic::handlerSelfCheckComplete`, `SiteLogic::toHomeInitialProcess` through `HttpRequestControllerImpl::syncInstallation`) (string-only: inferred from the caller and function names, the chain is not in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_energy_service/sync_installation_inspection` (asm-traced): URL string `@0x26eb180`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x26eb178`, in `HttpRequestControllerImpl::syncInstallation` (`charging/http/http_request_repository_impl.dart @0x26eb06c`), sent through `HttpRequestControllerImpl::requestHttp` (`@0x26eb1b0`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: two field types are not read) One sender. The map literal has the type arguments `<String, Object>` (`charging/http/http_request_repository_impl.dart @0x26eb130`), which name no value type; three pairs (array length raw 12 at `@0x26eb0bc`), stored without a guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | ? | yes | `"<sn>"` | `charging/http/http_request_repository_impl.dart @0x26eb0c8` (value store `@0x26eb0d8`, parameter) |
| `page` | ? | yes | `"<page>"` | `charging/http/http_request_repository_impl.dart @0x26eb0dc` (value store `@0x26eb0ec`, parameter) |
| `errors` | list | yes | `[]` | `charging/http/http_request_repository_impl.dart @0x26eb0f0` (value is a new empty growable list, `_GrowableList` with length 0 `@0x26eb100`, `@0x26eb104`) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed in this wrapper: the closure passed as `complete` (`charging/http/http_request_repository_impl.dart @0x24044f0`) forwards its argument to a stored callback and reads no key; the callers' callbacks were not read.

## Response

No response key is read by the wrapper (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "sn": "<sn>",
  "page": "<page>",
  "errors": []
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `syncInstallation` @0x26eb06c (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::syncInstallation`
- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart::createOrJoinSuccess`
- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart::syncGoHome`
- `charging/ui/page/device/a17b1/a17b1system_test/system_test_logic.dart::handlerSelfCheckComplete`
- `charging/ui/page/green_energy/site/site_logic.dart::toHomeInitialProcess`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `sn` and `page`: wrapper parameters; the literal names no value type.
- Whether `errors` is ever filled: the wrapper always sends an empty list (`charging/http/http_request_repository_impl.dart @0x26eb104`); a caller cannot add entries through this function.
- What `page` values the callers send and what the server stores.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
