> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_electric_utility_and_electric_plan_list

## Purpose

Loads the NEM utility and rate-plan list for the NEM rate page (`NemRateLogic::getNemRatePlan`, called from `NemRateLogic::onReady`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_electric_utility_and_electric_plan_list` (asm-traced): URL string at `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart @0x2973df4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2973dec`, in `NemRateLogic::getNemRatePlan` (`charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart @0x2973cf0`), sent through `requestHttp` (`@0x2973e1c`).

The request is only built when a cached value is empty: `getNemRatePlan` calls `parseUtilityPlanData` instead (`charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart @0x2973d3c`) when the checked field is non-null (`cmp w2, NULL` `@0x2973d34`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `NemRateLogic::getNemRatePlan` (`charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart`, call `@0x2973e1c`, argument list `@0x2973e14`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `NemRateLogic::getNemRatePlan` (`charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart @0x2973da8`, 3 keys). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | string | yes | `"<siteId>"` | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart @0x2973d50` |
| `country` | string | yes | `"US"` | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart @0x2973d78` |
| `state_code` | string | yes | `"CA"` | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart @0x2973d90` |

## `param_type`/`cmd`

n/a

## Response model (link)

- `charging::NemUtilityRateModel`, parsed by `NemUtilityRateModel.fromJson` at `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart @0x29781a4` (success closure `@0x2978158`, `bl` target `[package:charging/model/a5101/nem_utility_rate_model.dart]`). The parse is in the success closure `@0x2978158`.

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::NemUtilityRateModel`): `electric_utility_and_elecric_plan_list` (unknown).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "siteId": "<siteId>",
  "country": "US",
  "state_code": "CA"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart`: `getNemRatePlan` @0x2973cf0 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart::onReady`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which field makes `getNemRatePlan` skip the request (`charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart @0x2973d34`): the `LoadField` chain was not resolved to a name.
- Whether other countries or state codes than the constants `US` and `CA` are ever sent: the two values are stored as constants (`charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart @0x2973d84`, `@0x2973d9c`).
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
