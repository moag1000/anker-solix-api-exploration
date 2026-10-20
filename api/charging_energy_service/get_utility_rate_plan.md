> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_utility_rate_plan

## Purpose

Reads the utility rate plan (peak sessions and fixed price) of an A17B1 station (callers `ElectricitySceneLogic::_getRatePlanDataByStation`, `A17B1UtilityRatePlanLogic::_getRatePlanData`, `A17B1SystemPolicyLogic::_getSystemPolicySetting`; started from the screens' `onReady`, `didPopNext` and `_getSiteConfig`) (string-only: the caller names are in the page's caller list, the chain is not in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_energy_service/get_utility_rate_plan` (asm-traced) at three senders, all through `BaseGetController::requestHttp`:

- `ElectricitySceneLogic::_getRatePlanDataByStation` (`charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart @0x28bbca4`): URL string `@0x28bbdd8`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x28bbdd0`, call `@0x28bbe08`.
- `A17B1UtilityRatePlanLogic::_getRatePlanData` (`charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/a17b1_utility_rate_plan_logic.dart @0x293842c`): URL `@0x293858c`, `Method.post` `@0x2938584`, call `@0x29385b0`.
- `A17B1SystemPolicyLogic::_getSystemPolicySetting` (`charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart @0x288cf18`): URL `@0x288d2e0`, `Method.post` `@0x288d2d8`, call `@0x288d308`.

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: two field types are not read) All three senders build a `<String, dynamic>` literal (`charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart @0x28bbd34`, `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/a17b1_utility_rate_plan_logic.dart @0x2938460`, `charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart @0x288d200`), which names no value type; the integer `accuracy` is typed from its constant.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | yes in `_getRatePlanDataByStation`; optional in the other two | `"<station_id>"` | `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart @0x28bbd64` (guard: the function returns when the station id string is empty, `cbnz` `@0x28bbd20`); `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/a17b1_utility_rate_plan_logic.dart @0x2938518` (guard: compare with `Instance_JumpPeakRouterType` `@0x29384f8`); `charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart @0x288d238` (guard: length test `cbz` `@0x288d228`) |
| `sn` | string in `_getSystemPolicySetting`; ? in `_getRatePlanData` | optional | `"<sn>"` | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/a17b1_utility_rate_plan_logic.dart @0x29384d8` (guard: compare with `Instance_JumpPeakRouterType` `@0x29384a0`); `charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart @0x288d26c` (value `field_6b` of `ankerDevice`, loads `@0x288d250`, `@0x288d258`; `ankerDevice` is declared `late A17B1AnkerDevice` in the class listing of the same file, and offset 0x6b of `AnkerDevice` is the getter `String dyn:get:deviceSn`, `base_service/device/anker_device.dart @0x22053d4`, load `@0x22053d8`); not sent by `_getRatePlanDataByStation` |
| `accuracy` | int (Smi, w) | yes | `5` (raw immediate 10, passed as a tagged argument to the map store) | `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart @0x28bbd88` (constant `@0x28bbd90`, store call `@0x28bbd94`); `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/a17b1_utility_rate_plan_logic.dart @0x293853c` (constant `@0x2938544`); `charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart @0x288d290` (constant `@0x288d298`) |

Router-type rule (traced 2026-10-20): in `A17B1UtilityRatePlanLogic::_getRatePlanData` (`charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/a17b1_utility_rate_plan_logic.dart`) `sn` is added when the router type is `devicePush` (compare `@0x29384a0`, value `field_5f`, key store `@0x29384d8`) and `station_id` when it is `sitePush` (compare `@0x29384f8`, value `field_1f`, key store `@0x2938518`); the two instances and the rule are in [get_world_monetary_unit](get_world_monetary_unit.md#request).

## `param_type`/`cmd`

n/a

## Response model (link)

Same class at all three senders, no `models/` page: `charging::A17B1RatePlanStructureModel`, parsed by `A17B1RatePlanStructureModel.fromJson` at `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart @0x28bbea0` (success closure `@0x28bbe24`), `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/a17b1_utility_rate_plan_logic.dart @0x2938654` (closure `@0x29385d8`) and `charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart @0x288d3ec` (closure `@0x288d3a8`).

## Response

(asm-traced for the model) Top-level keys of `A17B1RatePlanStructureModel` (`data/models.json`, `charging::A17B1RatePlanStructureModel`): `peak_sessions` (type not named by the extractor), `fixed_price` (FixedRate?). Each closure passes the model to `ParserPeakData::handlePeakValleyPriceDiffData` when `peak_sessions` is non-empty (for example `{ES} @0x28bbf10`).

Element shapes (traced 2026-10-20, app side; casts of the `fromJson` methods): `A17B1RatePlanStructureModel.fromJson` (`charging/ui/page/device/a17b1/device_setting/utility_rate_plan/config_data/a17b1_rate_plan_structure_model.dart`, key reads `peak_sessions` `@0x288f53c`, `fixed_price` `@0x288f5fc`) builds `peak_sessions` as a list with the type argument `<PeakSessions>` (`@0x288f56c`) and `fixed_price` with `FixedRate.fromJson` (`@0x288f664`). `FixedRate` has `id` (`int?`), `name`, `start_time`, `start_desc`, `end_time`, `end_desc` (`String?`), `type` (`int?`) and `peak_valley_prices`, a list of `PeakValleyPrices` (`<PeakValleyPrices>` `@0x288fea8`). `PeakSessions` (`charging/ui/page/device/a17b1/device_setting/utility_rate_plan/config_data/A17b1_device_command_model.dart`) has `id` (`int?`), `name`, `start_time`, `end_time` (`String?`), `type` (`int?`) and `peak_valley_prices`; `PeakValleyPrices` has `id` (`int?`), `buy` and `sell` (`num?`), `energy_unit`, `start_time_period`, `end_time_period` (`String?`) and `peak_type` (`int?`).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "sn": "<sn>",
  "accuracy": 5
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart`: `_getRatePlanDataByStation` @0x28bbca4 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/a17b1_utility_rate_plan_logic.dart`: `_getRatePlanData` @0x293842c (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart`: `_getSystemPolicySetting` @0x288cf18 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart::_getSiteConfig`
- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart::didPopNext`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/a17b1_utility_rate_plan_logic.dart::onReady`
- `charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart::didPopNext`
- `charging/ui/page/device/a17b1/system_policy/system_policy_logic.dart::requestSiteConfig`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `station_id` and `sn`: values loaded from fields or parameters; the literals name no value type. — attempted 2026-10-20 (two-hop not readable: an anonymous closure (`charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart @0x28bbc88`), an anonymous closure (`charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart @0x40adb40`), `onReady` (`charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/a17b1_utility_rate_plan_logic.dart @0x2937f54`) and 5 more pass slots or fields of their own frames; no literal or declared type in the argument setups)
- What `accuracy` 5 selects on the server (probably the number of decimals of the prices; not shown by the asm).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
