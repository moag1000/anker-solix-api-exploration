> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_system_running_info

## Purpose

Reads the running summary of an A17B1 station (connection state, total savings, carbon saved, total generation) for the station home page (caller `A17b1StationLogic::getSystemInfo`, which passes the success closure) (string-only: the caller name is in the page's caller list, no chain is in `data/endpoints.json`; the call itself is asm-traced).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_energy_service/get_system_running_info` (asm-traced): URL string `@0x2437dfc`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x2437df4`, in `StationHttpReposity::getSystemRunningInfo` (`charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x2437cc8`), sent through the mixin `HttpRequestMixin::requestHttp` (`@0x2437e30`; options `cacheKey`, `isAIotErrorCode`, `loopSeconds`, `showDefaultError`, `success`, descriptor `@0x2437e28`). The function stops with the log text `empty siteId` when the site id string is empty (`cbnz` `@0x2437d18`, string `@0x2437d1c`) and reads a cache entry first (`getCache` `@0x2437d68`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) One sender, one key. The map literal has the type arguments `<String, String>` (`charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x2437dc4`), so the value is a string; it is stored without a further guard after the empty test.

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | string | yes | `"<site_id>"` | `charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x2437db0` (value store `@0x2437dc0`, parameter) |

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::A17b1SystemInfoModel` (no `models/` page), parsed by `A17b1SystemInfoModel.fromJson` at `charging/ui/page/station/A17b1/a17b1_station_logic.dart @0x2437ea8` in the success closure `@0x2437e44` that `A17b1StationLogic::getSystemInfo` (`charging/ui/page/station/A17b1/a17b1_station_logic.dart @0x2437c00`) creates (`@0x2437c94`) and passes with the call `getSystemRunningInfo` (`@0x2437cac`).

## Response

(asm-traced) Top-level keys of `A17b1SystemInfoModel` (`data/models.json`, `charging::A17b1SystemInfoModel`): `connected` (bool?), `total_system_savings` (num?), `system_savings_price_unit` (String?), `save_carbon_footprint` (num?), `save_carbon_unit` (String?), `save_carbon_c` (num?), `total_system_power_generation` (num?), `system_power_generation_unit` (String?). The closure also stores the result in the station's reactive state and updates battery and MQTT state from it (`_updateA1790BatteryByA17B1Station`, `{A17S} @0x243807c`).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "siteId": "<site_id>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/station/mixin/station_chart_http_reposity.dart`: `getSystemRunningInfo` @0x2437cc8 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the request options mean (`loopSeconds`, `cacheKey`): they are arguments of the mixin function, not body keys; their values were not decoded.
- How the closure uses `connected` to decide a device's online state: only the log text `无connected字段` is read, the full logic was not followed.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
