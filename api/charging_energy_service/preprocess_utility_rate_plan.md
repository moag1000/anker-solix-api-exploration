> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# preprocess_utility_rate_plan

## Purpose

Sends a peak/valley or fixed-rate plan to the cloud so it can be pre-processed into a rate plan for an A17B1 station (callers `ElectricitySceneLogic::sendPeakValleyData`, `A17B1PeakValleyPriceDiffSecondaryEditLogic::sendPeakValleyData`, `A17B1FixedRateLogic::save`) (string-only: inferred from the caller and function names, the chain is not in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_energy_service/preprocess_utility_rate_plan` (asm-traced) at two senders:

- `HttpRequestControllerImpl::dealUtilityRatePlanData` (`charging/http/http_request_repository_impl.dart @0x3d0377c`): URL string `@0x3d038e0`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x3d038d8`, `HttpRequestControllerImpl::requestHttp` `@0x3d03908`.
- `A17B1FixedRateLogic::savePlanPrice` (`charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f658`): URL `@0x3d3fbcc`, `Method.post` `@0x3d3fbc4`, `BaseGetController::requestHttp` `@0x3d3fbf4`.

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: most field types are not read) `dealUtilityRatePlanData` forwards the body parts of its caller in a `<String, dynamic>` literal (`charging/http/http_request_repository_impl.dart @0x3d037fc`); `savePlanPrice` builds the full body in place with `<String, Object>` literals. Neither names a value type for the parameter-backed keys.

`dealUtilityRatePlanData`:

| field | type | required | example | source |
|---|---|---|---|---|
| `peak_sessions` | ? | yes | `[...]` | `charging/http/http_request_repository_impl.dart @0x3d037e8` (value store `@0x3d037f8`, parameter) |
| `station_id` | ? | optional | `"<station_id>"` | `charging/http/http_request_repository_impl.dart @0x3d03830` (guard: length test `cbz` `@0x3d03820`) |
| `sn` | ? | optional | `"<sn>"` | `charging/http/http_request_repository_impl.dart @0x3d0386c` (guard: length test `cbz` `@0x3d03858`) |
| `accuracy` | int (Smi, w) | yes | `5` (raw immediate 10, tagged argument of the map store) | `charging/http/http_request_repository_impl.dart @0x3d03890` (constant `@0x3d03898`, store call `@0x3d0389c`) |

`savePlanPrice` (top level; array length raw 8 at `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f690`, so `time` and `peak_sessions` in the literal `<String, Object>` `@0x3d3fa44`, the other keys added by map stores):

| field | type | required | example | source |
|---|---|---|---|---|
| `time` | string | yes | `"<current time>"` | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f69c` (value from `DateUtil::getCurrentTime`, call `@0x3d3f6a8`) |
| `peak_sessions` | list | yes | one session (below) | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f6d8` (growable list of `<Map<String, Object>>`, `@0x3d3f980`, store `@0x3d3fa20`) |
| `sn` | ? | yes | `""` when no device is selected | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3fad0` (fallback constant `@0x3d3fab8`, store call `@0x3d3fad8`) |
| `station_id` | ? | yes | `""` when no station is selected | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3fb24` (fallback constant `@0x3d3fb08`, store call `@0x3d3fb2c`) |
| `electricity_strategy` | object | yes | `{"mode": 1}` | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3fb80` (map `<String, int>` `@0x3d3fb5c` with key `mode` `@0x3d3fb48`, Smi 1 from raw 2 at `@0x3d3fb54`) |

One element of `peak_sessions` (map of seven pairs, array length raw 28 at `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f6e8`; the same code builds one session):

| field | type | required | example | source |
|---|---|---|---|---|
| `id` | int (Smi, w) | yes | `0` (zero register) | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f6f4` (store `@0x3d3f700`) |
| `name` | string | yes | `"session1"` | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f704` (constant `@0x3d3f70c`) |
| `start_time` | string | yes | `"<year>-01-01 00:00:00"` | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f718` (string interpolation with `DateUtil::getCurrentYear` `@0x3d3f724`) |
| `end_time` | string | yes | `"<year>-12-01 00:00:00"` | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f784` (interpolation, `getCurrentYear` `@0x3d3f790`) |
| `type` | int (Smi, w) | yes | `1` (raw immediate 2) | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f7f0` (constant `@0x3d3f7f8`, store `@0x3d3f7fc`) |
| `accuracy` | int (unboxed, x) | yes | `<accuracy>` | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f800` (`LoadField` `@0x3d3f810`, `BoxInt64Instr` `@0x3d3f814`) |
| `peak_valley_prices` | list | yes | one price entry (below) | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f850` (growable list `<Map<String, Object>>`) |

One element of `peak_valley_prices` (seven pairs, array length raw 28 at `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f860`):

| field | type | required | example | source |
|---|---|---|---|---|
| `id` | int (Smi, w) | yes | `0` (zero register) | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f86c` (store `@0x3d3f878`) |
| `buy` | number | yes | `<price>` | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f87c` (value from `num.parse`, call `@0x3d3f8a8`) |
| `energy_unit` | string | yes | `"/kWh"` | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f8d8` (constant `@0x3d3f8e4`) |
| `start_time_period` | string | yes | `"00:00"` | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f8f0` (constant `@0x3d3f8fc`) |
| `end_time_period` | string | yes | `"00:00"` | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f908` (constant `@0x3d3f914`) |
| `peak_type` | int (Smi, w) | yes | `1` (raw immediate 2) | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f920` (constant `@0x3d3f92c`) |
| `day_type` | int (Smi, w) | yes | `2` (raw immediate 4) | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f934` (constant `@0x3d3f940`) |

Types read in the second pass (traced 2026-10-20): `time` is the result of `DateUtil.getCurrentTime`, declared `static String` (`base_service/util/date_util.dart @0x249c254`..`@0x249c324`), a `formatDate` call with the pieces `yyyy`, `-`, `mm`, `-`, `dd`, ` `, `HH`, `:`, `nn`, `:`, `ss` of the `date_format` package, i.e. text of the form `2026-10-20 14:05:09`; `buy` is the result of `num.parse` (`a17b1_fixed_rate_logic.dart @0x3d3f8a8`), a `num`, so a JSON number; `sn` is the String `field_6b` getter of the device object or `""` (fallback `@0x3d3fab8`). `station_id` (`field_1f` or `""`) has no declared type. For `dealUtilityRatePlanData` the caller `A17B1PeakValleyPriceDiffSecondaryEditLogic::sendPeakValleyData` (`charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley_price_diff_secondary_edit/a17b1_peak_valley_price_diff_secondary_edit_logic.dart @0x3d3a2a4`) applies the router-type rule of [get_world_monetary_unit](get_world_monetary_unit.md#request) (`sn` from `field_83.field_6b` when `devicePush`, `@0x3d3a2fc`..`@0x3d3a31c`; `station_id` from `field_1f` when `sitePush`, `@0x3d3a33c`..`@0x3d3a344`), shows the loading dialog (`@0x3d3a390`) and calls `dealUtilityRatePlanData` (`@0x3d3a3d0`) with the session list built in the same logic.

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed in `dealUtilityRatePlanData`: the closure passed as `complete` (`charging/http/http_request_repository_impl.dart @0x2268374`) forwards its argument to a stored callback. For `savePlanPrice` the success closure (`charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3fc1c`) calls `setMode` (`@0x3d3fc64`), refreshes the station data (`getSystemInfo` `@0x3d3fd00`) and leaves the page with a `FixedRateUpdateModel` result (`@0x3d3fd08`); it reads no response key.

## Response

No response key is read by either sender (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by `dealUtilityRatePlanData`; `<...>` are placeholders, not captured values)

```json
{
  "peak_sessions": [],
  "station_id": "<station_id>",
  "sn": "<sn>",
  "accuracy": 5
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `dealUtilityRatePlanData` @0x3d0377c (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart`: `savePlanPrice` @0x3d3f658 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::dealUtilityRatePlanData`
- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart::sendPeakValleyData`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley_price_diff_secondary_edit/a17b1_peak_valley_price_diff_secondary_edit_logic.dart::sendPeakValleyData`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart::save`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of the parameter-backed keys (`peak_sessions` content of `dealUtilityRatePlanData`, `station_id`, `sn`, `time`, `buy`): the literals name no value type. — traced 2026-10-20: `time` (string), `buy` (number) and `sn` (string) are typed under Request; `station_id` and the content of `peak_sessions` for `dealUtilityRatePlanData` stay untyped (two-hop not readable: `a17b1_peak_valley_price_diff_secondary_edit_logic.dart @0x3d3a344`)
- Why `savePlanPrice` sends one session starting on 1 January and ending on 1 December of the current year with a single price and `peak_type` 1: the constants are read (`charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x3d3f744`, `@0x3d3f7a8`); the server's reading of them is not known from the app.
- What `type` 1, `peak_type` 1, `day_type` 2 and `electricity_strategy.mode` 1 select: constants only. — reclassified: server (2026-10-20: the app sends these as constants and names none of them; the meaning is decided by the server)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
