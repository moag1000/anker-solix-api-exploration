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
| `param_types` | list | yes |  | `charging/http/http_request_repository_impl.dart @0x2890c10` (value store `@0x2890c20`, parameter) |

Values of `param_types` (app side, traced 2026-10-20): the three callers build it themselves as a growable list with the type argument `<String>` and two string literals (`AllocateGrowableArray`, element array of raw length 4): `["sm_mode", "fixedrate_mode"]` in `_getSiteConfig` of `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/a17b1_utility_rate_plan_logic.dart` (`@0x2937fdc`, `@0x2937fe8`, list `@0x2937ff8`, call `@0x2938038`) and `["cyclePercent", "sm_mode"]` in `_getSiteConfig` of `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart` (`@0x28bbbb0`, `@0x28bbbbc`, call `@0x28bbc28`) and in `requestSiteConfig` of `charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart` (`@0x288ce78`, `@0x288ce84`, call `@0x288cef0`). So `param_types` is a list of strings, and the strings are the same config names that [sync_config.md](sync_config.md#request) sends as `param_type`.

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed as a model: the closure passed as `complete` (`charging/http/http_request_repository_impl.dart @0x2890c9c`) reads the key `configs` (`@0x2890cc8`), requires a `List` (type test `@0x2890d18`) and hands a list built from it to the caller's callback (`ClosureCall` `@0x2890d68`, `@0x2890da0`). The list elements are not decoded in this wrapper.

## Response

Key read by the closure: `configs` (list). Nothing else is read.

Element structure (traced 2026-10-20, app side): the callback of `A17B1UtilityRatePlanLogic::_getSiteConfig` (`charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/a17b1_utility_rate_plan_logic.dart @0x2938060`, argument `List<dynamic>`) picks entries with `firstWhereOrNull` on the key `param_type`, comparing it with the text `sm_mode` (closure `@0x29383ac`, compare `@0x29383fc`) and with `fixedrate_mode` (closure `@0x293832c`, compare `@0x293837c`), and reads the key `param_data` of each hit (`@0x29380bc`, `@0x2938118`), casts it to `String` and converts it with `parse` (integer text, `@0x29381b4`, `@0x2938248`). The parsed integers are compared with 2 (`cmp x0, #2` `@0x2938250`, unboxed, real value) and 1 (`cmp x0, #1` `@0x29382a8`) to decide which of two list entries (`first`/`last` of `field_57`, `@0x293826c`, `@0x2938290`, `@0x29382c8`, `@0x29382f0`) is selected before `update` (`@0x2938310`). So each element of `configs` is a map with `param_type` (text) and `param_data` (text holding an integer in these two cases). The other two callers (`electricity_scene_logic.dart`, `system_policy_logic.dart`) were not decoded.

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

- The type of `station_id`: a wrapper parameter; the three callers pass a slot of their own frame (`charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/a17b1_utility_rate_plan_logic.dart @0x2938028`, `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart @0x28bbc14`, `charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart`); `param_types` is typed in Request — attempted 2026-10-20 (two-hop not readable for `station_id`).
- The `param_data` of `cyclePercent` and the use by `ElectricityScene` / `SystemPolicy` callers: the shape of the two entries `sm_mode` and `fixedrate_mode` is in Response; the other callers were not decoded — traced 2026-10-20
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
