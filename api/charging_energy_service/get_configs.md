> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_configs

## Purpose

Reads the configuration entries of an A17B1 station (callers `ElectricitySceneLogic::_getSiteConfig`, `A17B1UtilityRatePlanLogic::_getSiteConfig`, `A17B1SystemPolicyLogic::requestSiteConfig`) (string-only: inferred from the caller names, the chain is not in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_energy_service/get_configs` (asm-traced): URL string `@0x2890c58`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x2890c50`, in `HttpRequestControllerImpl::getSiteConfigs` (`charging/http/http_request_repository_impl.dart @0x2890b84`), sent through `HttpRequestControllerImpl::requestHttp` (`@0x2890c80`). The function returns without sending when `station_id` is null (`cmp w0, NULL` `@0x2890bcc`) or empty (`cbnz` `@0x2890bd8`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: both field types are not read) One sender. The map literal has the type arguments `<String, Object>` (`charging/http/http_request_repository_impl.dart @0x2890c24`), which name no value type; both keys are stored without a further guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | yes | `"<station_id>"` | `charging/http/http_request_repository_impl.dart @0x2890bfc` (value store `@0x2890c0c`, parameter) |
| `param_types` | ? | yes | `<param_types>` | `charging/http/http_request_repository_impl.dart @0x2890c10` (value store `@0x2890c20`, parameter) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed as a model: the closure passed as `complete` (`charging/http/http_request_repository_impl.dart @0x2890c9c`) reads the key `configs` (`@0x2890cc8`), requires a `List` (type test `@0x2890d18`) and hands a list built from it to the caller's callback (`ClosureCall` `@0x2890d68`, `@0x2890da0`). The list elements are not decoded in this wrapper.

## Response

Key read by the closure: `configs` (list). Nothing else is read.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "param_types": "<param_types>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getSiteConfigs` @0x2890b84 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getSiteConfigs`
- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart::_getSiteConfig`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/a17b1_utility_rate_plan_logic.dart::_getSiteConfig`
- `charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart::requestSiteConfig`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `station_id` and `param_types`: wrapper parameters; the literal `<String, Object>` names no value type. A list of numeric ids is plausible for `param_types` but not shown by the asm.
- The structure of the `configs` elements: the callers (`_getSiteConfig`, `requestSiteConfig`) parse them and were not read.
- Which `param_types` values the callers send.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
