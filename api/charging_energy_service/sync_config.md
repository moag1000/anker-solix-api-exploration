> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# sync_config

## Purpose

Writes one configuration entry of an A17B1 or A1782 station (for example the mode or the battery reserve) (callers `ElectricitySceneLogic::updateMode` and `setBatteryReserve`, `A17B1SystemPolicyLogic::updateMode`, `A17B1UtilityRatePlanLogic::setMode`, `A1782ElectricitySceneLogic::setBatteryReserve` and more through `HttpRequestControllerImpl::syncSiteConfig`) (string-only: inferred from the caller names, the chain is not in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_energy_service/sync_config` (asm-traced): URL string `@0x2678754`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x267874c`, in `HttpRequestControllerImpl::syncSiteConfig` (`charging/http/http_request_repository_impl.dart @0x2678638`), sent through `HttpRequestControllerImpl::requestHttp` (`@0x2678778`). The function returns without sending when `station_id` is null (`cmp w0, NULL` `@0x2678664`) or empty (`cbnz` `@0x2678670`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: all three field types are not read) One sender. The map literal has the type arguments `<String, dynamic>` (`charging/http/http_request_repository_impl.dart @0x2678684`), which name no value type; all three keys are stored without a further guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | yes | `"<station_id>"` | `charging/http/http_request_repository_impl.dart @0x26786ac` (value store call `@0x26786b4`, parameter) |
| `param_type` | string | yes | `"sm_mode"`, `"fixedrate_mode"` or `"cyclePercent"` | `charging/http/http_request_repository_impl.dart @0x26786d4` (parameter, store call `@0x26786dc`) |
| `param_data` | ? | yes | `<param_data>` | `charging/http/http_request_repository_impl.dart @0x2678730` (value is the result of a one-argument dispatch-table call on a parameter, `@0x2678708`, selector not named by Blutter; store call `@0x2678738`) |

Callers (app side, traced 2026-10-20): the eleven call sites of `syncSiteConfig` pass a string literal as the second argument, which the sender stores as `param_type`: `"sm_mode"` (`charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart @0x26ea940`, `@0x28bc08c`; `charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart @0x2678454`; `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/a17b1_utility_rate_plan_logic.dart @0x27c6008`; `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3fe08`; `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley_price_diff_secondary_edit/a17b1_peak_valley_price_diff_secondary_edit_logic.dart @0x274579c`), `"fixedrate_mode"` (`a17b1_utility_rate_plan_logic.dart @0x27c6118`, `a17b1_peak_valley_price_diff_secondary_edit_logic.dart @0x2745a24`) and `"cyclePercent"` (the three `setBatteryReserve` functions `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart @0x3d07300`, `charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart @0x3d48334` and `charging/ui/page/device/a1782/station/electricity_scene/a1782_electricity_scene_logic.dart @0x3cdd0fc`), so `param_type` is a string. The value argument is the integer constant raw 2 (1 under the Smi rule) at `@0x27457a4` and `@0x27c6010`, and the strings `"1"` and `"2"` at `@0x2745a2c`, `@0x3d3fe10` and `@0x27c6120`, so callers pass numbers and texts, which the sender turns into `param_data` with a dispatch-table call whose selector Blutter does not name; the type of `param_data` therefore stays `?`.

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed in the wrapper: it passes no `complete`, `fail` or `success` closure (argument descriptor `charging/http/http_request_repository_impl.dart @0x2678770` names only `showLoading`) and returns the result of `requestHttp` to its caller; how the callers read it was not followed.

## Response

No response key is read by the wrapper (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "param_type": "<param_type>",
  "param_data": "<param_data>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `syncSiteConfig` @0x2678638 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::syncSiteConfig`
- `charging/ui/page/device/a1782/station/electricity_scene/a1782_electricity_scene_logic.dart::setBatteryReserve`
- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart::_getRatePlanDataByStation`
- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart::setBatteryReserve`
- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart::updateMode`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley_price_diff_secondary_edit/a17b1_peak_valley_price_diff_secondary_edit_logic.dart::ackUtilityRatePlan`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley_price_diff_secondary_edit/a17b1_peak_valley_price_diff_secondary_edit_logic.dart::setMode`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/a17b1_utility_rate_plan_logic.dart::_fixedRateSuccess`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/a17b1_utility_rate_plan_logic.dart::setMode`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart::setMode`
- `charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart::setBatteryReserve`
- `charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart::updateMode`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The types of `station_id` and `param_data` (the first is a wrapper parameter, the second the result of an unnamed dispatch-table call): `param_type` is typed in Request — attempted 2026-10-20 (two-hop not readable: `param_data` selector not named, `charging/http/http_request_repository_impl.dart @0x2678708`).
- What the server does with the three `param_type` strings (`sm_mode`, `fixedrate_mode`, `cyclePercent`): not known from the app; the callers and literals are in Request (traced 2026-10-20).
- How the callers parse the returned object: the worksheet lists `A17B1RatePlanStructureModel` for one caller; that parse was not read.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
