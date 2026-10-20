> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# restart_peak_session

## Purpose

Clears and restarts the peak session of an A17B1 station's rate plan (callers `A17B1PeakValleyPriceDiffSecondaryEditLogic::cleanPeakRate` and `A17B1FixedRateLogic::cleanPeakRate` through `HttpRequestControllerImpl::restartPeakSession`) (string-only: inferred from the caller names, the chain is not in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_energy_service/restart_peak_session` (asm-traced): URL string `@0x2745324`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x274531c`, in `HttpRequestControllerImpl::restartPeakSession` (`charging/http/http_request_repository_impl.dart @0x27451e0`), sent through `HttpRequestControllerImpl::requestHttp` (`@0x274534c`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: two field types are not read) One sender. The map literal has the type arguments `<String, dynamic>` (`charging/http/http_request_repository_impl.dart @0x274523c`), which name no value type.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | optional | `"<station_id>"` | `charging/http/http_request_repository_impl.dart @0x2745274` (guard: `cmp w3, NULL` `@0x2745258`, length test `cbz` `@0x2745264`) |
| `sn` | ? | optional | `"<sn>"` | `charging/http/http_request_repository_impl.dart @0x27452b0` (guard: `cmp w3, NULL` `@0x2745290`, length test `cbz` `@0x274529c`) |
| `far_field_model` | int (Smi, w) | yes | `1` (raw immediate 2, tagged argument of the map store) | `charging/http/http_request_repository_impl.dart @0x27452d4` (constant `@0x27452dc`, store call `@0x27452e0`) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed in this wrapper: the closure passed as `complete` (`charging/http/http_request_repository_impl.dart @0x2268374`) forwards its argument to a stored callback and reads no key; the callers' callbacks were not read.

## Response

No response key is read by the wrapper (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "sn": "<sn>",
  "far_field_model": 1
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `restartPeakSession` @0x27451e0 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::restartPeakSession`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley_price_diff_secondary_edit/a17b1_peak_valley_price_diff_secondary_edit_logic.dart::cleanPeakRate`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart::cleanPeakRate`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `station_id` and `sn`: wrapper parameters; the literal names no value type.
- What `far_field_model` 1 selects (constant only) and why the name says "far field".
- What the callers' callbacks do with the answer.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
