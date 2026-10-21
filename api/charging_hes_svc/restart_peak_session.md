> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# restart_peak_session

## Purpose

Deletes and restarts the peak-valley sessions of a rate plan (callers `FixedRateLogic::deleteData`, `NemPlanEditLogic::cleanNemPeakRate` and `deleteOldData`, `NemRatePlanLogic::deleteOldData`, through `HttpRequestControllerImpl::deleteAndRestartPeakValley`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/restart_peak_session` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x278fd3c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x278fd34`, in `HttpRequestControllerImpl::deleteAndRestartPeakValley` (`charging/http/http_request_repository_impl.dart @0x278fc6c`), sent through `requestHttp` (`@0x278fd64`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::deleteAndRestartPeakValley` (`charging/http/http_request_repository_impl.dart`, call `@0x278fd64`, argument list `@0x278fd5c`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

`HttpRequestControllerImpl::deleteAndRestartPeakValley` (`charging/http/http_request_repository_impl.dart @0x278fc6c`) stores 2 keys in a map literal with type arguments `<String, Object?>` (`@0x278fcf0`), which do not type the values. `far_field_model` is an integer: the unboxed parameter is tagged to a Smi by `lsl x2, x1, #1` (`@0x278fce8`) before the store (`@0x278fcec`), so the number is the parameter value; `station_id` is stored as received (`@0x278fcd4`). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x278fcc4` |
| `far_field_model` | int (Smi, w) | yes | a number from the caller | `charging/http/http_request_repository_impl.dart @0x278fcd8` |

Values of `far_field_model` (app side, traced 2026-10-20): `FixedRateLogic::deleteData` passes the unboxed constant 1 (`r3 = 1`, `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x3ecff7c`, call `@0x3ecff80`) and `NemPlanEditLogic::cleanNemPeakRate` the constant 2 (`r3 = 2`, `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart @0x278fbf8`, call `@0x278fbfc`); the argument is unboxed, so these are the real values. `NemPlanEditLogic::deleteOldData` (`charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart @0x3ed51fc`) and `NemRatePlanLogic::deleteOldData` (`charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_plan/nem_rate_plan_logic.dart @0x3ed6488`) pass a slot of their own frame (`@0x3ed51f0`, `@0x3ed647c`); what 1 and 2 select is not named in the asm.

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the sender (asm-traced): the success closure is the folded forwarder `charging/http/http_request_repository_impl.dart @0x2268374`, which passes the response object unchanged to the callback stored in the context (`ClosureCall` `@0x22683a8`); the failure closure (`@0x278fd80`) forwards code and message (`ClosureCall` `@0x278fdbc`) and logs `---> deleteAndRestartPeakValley failed, code` (`@0x278fdd4`).

## Response

No response key is read in the sender.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "far_field_model": "<far_field_model>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `deleteAndRestartPeakValley` @0x278fc6c (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::deleteAndRestartPeakValley`
- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart::deleteData`
- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart::cleanNemPeakRate`
- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart::deleteOldData`
- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_plan/nem_rate_plan_logic.dart::deleteOldData`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The type of `station_id`: the parameter is stored without conversion into a `<String, Object?>` map. — attempted 2026-10-20 (two-hop not readable: the four callers pass slots of their own frames, `fixed_rate_logic.dart @0x3ecff74`, `nem_plan_edit_logic.dart @0x278fbf0`, `@0x3ed51f4`, `nem_rate_plan_logic.dart @0x3ed6480`)
- What the callers do with the raw response: only the sender was read. — traced 2026-10-20: each caller passes a success closure and a failure closure (`AllocateClosure` before the call, e.g. `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart @0x3ecff68`); the closure bodies were not read
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
