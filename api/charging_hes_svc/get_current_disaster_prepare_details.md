> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_current_disaster_prepare_details

## Purpose

Reads the current disaster-preparedness details of a station (callers `SystemPolicyLogic::deviceToAutoDisasterStatus` and `AutoDisasterTipsLogic::_quitAutoDisasterPrepareFromDevice`, through `HttpRequestControllerImpl::getCurrentDisasterPrepareDetails`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_current_disaster_prepare_details` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3ebe778`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3ebe770`, in `HttpRequestControllerImpl::getCurrentDisasterPrepareDetails` (`charging/http/http_request_repository_impl.dart @0x3ebe5d8`), sent through `requestHttp` (`@0x3ebe79c`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::getCurrentDisasterPrepareDetails` (`charging/http/http_request_repository_impl.dart`, call `@0x3ebe79c`, argument list `@0x3ebe794`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

`HttpRequestControllerImpl::getCurrentDisasterPrepareDetails` (`charging/http/http_request_repository_impl.dart @0x3ebe5d8`) starts from an empty map literal with type arguments `<String, Object>` (`@0x3ebe68c`) and adds keys with `[]=`. `station_id` is added as received (`@0x3ebe6c0`), `unix` after `BoxInt64Instr` (`@0x3ebe6d0`, an unboxed 64-bit integer), and `auto_disaster_enable` only when its parameter is non-null (`cmp w3, NULL` `@0x3ebe714`, branch `@0x3ebe718`); its value is stored as received (`@0x3ebe734`).

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3ebe6b8` |
| `unix` | int (unboxed, x) | yes | a unix time | `charging/http/http_request_repository_impl.dart @0x3ebe6fc` |
| `auto_disaster_enable` | ? | optional | ? | `charging/http/http_request_repository_impl.dart @0x3ebe72c` |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`DisasterPrepareDetailsModel`](../../models/hes.md#disasterpreparedetailsmodel), parsed by `DisasterPrepareDetailsModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x3ebe8bc` (success closure `@0x3ebe850`, `bl` target `[package:charging/model/a5101/disaster_prepare_details_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::DisasterPrepareDetailsModel`): `details` (unknown).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "unix": "<unix>",
  "auto_disaster_enable": "<auto_disaster_enable>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getCurrentDisasterPrepareDetails` @0x3ebe5d8 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getCurrentDisasterPrepareDetails`
- `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::deviceToAutoDisasterStatus`
- `charging/ui/page/family/auto_disaster/auto_disaster_tips_logic.dart::_quitAutoDisasterPrepareFromDevice`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The types of `station_id` and `auto_disaster_enable`: both are parameters stored without conversion into a `<String, Object>` map.
- What the server returns when `auto_disaster_enable` is absent: the app omits the key for a null parameter.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
