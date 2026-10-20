> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_auto_disaster_prepare_detail

## Purpose

Reads the detail of the auto disaster-preparedness plan for the family page tips (`AutoDisasterTipsLogic::clickAutoDisasterTips` through `HttpRequestControllerImpl::getAutoDisasterPrepareDetail`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_auto_disaster_prepare_detail` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x43695f8`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x43695f0`, in `HttpRequestControllerImpl::getAutoDisasterPrepareDetail` (`charging/http/http_request_repository_impl.dart @0x43694a4`), sent through `requestHttp` (`@0x4369620`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::getAutoDisasterPrepareDetail` (`charging/http/http_request_repository_impl.dart`, call `@0x4369620`, argument list `@0x4369618`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

`HttpRequestControllerImpl::getAutoDisasterPrepareDetail` (`charging/http/http_request_repository_impl.dart @0x43694a4`) stores 3 keys in a map literal with type arguments `<String, Object>` (`@0x43695ac`), which do not type the values. `unix` is boxed from an unboxed 64-bit integer (`BoxInt64Instr` `@0x4369580`), so it is an integer; `station_id` and `near_field` are stored as received (`@0x436956c`, `@0x43695a8`). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x436955c` |
| `unix` | int (unboxed, x) | yes | a unix time | `charging/http/http_request_repository_impl.dart @0x4369570` |
| `near_field` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x4369598` |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`AutoDisasterDetailModel`](../../models/hes.md#autodisasterdetailmodel), parsed by `AutoDisasterDetailModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x4369740` (success closure `@0x43696d4`, `bl` target `[package:charging/model/a5101/auto_disaster_detail_model.dart]`). The success closure also calls `isErrorData` (`@0x4369748`) on the model before it completes the future.

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::AutoDisasterDetailModel`): `uuid` (String?), `event` (String?), `start` (int?), `end` (int?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "unix": "<unix>",
  "near_field": "<near_field>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getAutoDisasterPrepareDetail` @0x43694a4 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getAutoDisasterPrepareDetail`
- `charging/ui/page/family/auto_disaster/auto_disaster_tips_logic.dart::clickAutoDisasterTips`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The types of `station_id` and `near_field`: both are parameters stored without conversion.
- What `unix` stands for (time of the event or the request): the caller was not decoded.
- What `isErrorData` (`charging/http/http_request_repository_impl.dart @0x4369748`) tests on the parsed model.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
