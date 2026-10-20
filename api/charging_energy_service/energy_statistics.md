> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# energy_statistics

## Purpose

Loads the chart data (power, energy and totals per period) of the station home page (caller `StationHttpReposity::getChartStatistics`) (string-only: inferred from the model and function names, no caller chain is in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_energy_service/energy_statistics` (asm-traced): URL string `@0x24390dc`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x24390d4`, in `StationHttpReposity::getChartStatistics` (`charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x2438ee4`), sent through the mixin `HttpRequestMixin::requestHttp` (`@0x243911c`) with the options `cacheKey`, `debounceMills`, `isAIotErrorCode`, `isLogResponse`, `loopSeconds`, `showDefaultError` and `success` (argument descriptor `@0x2439114`). The function first reads a cache entry (`getCache` `@0x2438f70`) and, when it holds a value, parses it without sending (`@0x2438fb8`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: six field types are not read) One sender. The map literal has the type arguments `<String, Object?>` (`charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x24390a8`), which name no value type; seven pairs (array length raw 28 at `@0x2439014`, so 14 slots), all stored without a guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | ? | yes | `"<site_id>"` | `charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x243901c` (value store `@0x243902c`, parameter) |
| `productCode` | string | yes | `""` | `charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x2439030` (constant empty string `@0x2439040`) |
| `sourceType` | ? | yes | `"<source_type>"` | `charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x2439044` (value from a field, `LoadField` `@0x2439054`, store `@0x243905c`) |
| `dateType` | ? | yes | `"<date_type>"` | `charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x2439060` (store `@0x2439070`) |
| `start` | ? | yes | `"<start>"` | `charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x2439074` (store `@0x2439080`) |
| `end` | ? | yes | `"<end>"` | `charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x2439084` (parameter, store `@0x2439090`) |
| `global` | ? | yes | `<global>` | `charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x2439094` (parameter, store `@0x24390a4`) |

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::StationStatisticsModel` (no `models/` page), parsed by `StationStatisticsModel.fromJson` at `charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x243c034` in the success closure `@0x243bfe8` (and at `@0x2438fb8` for a cached entry); the closure then logs the model (`_prettyLog` `@0x243c040`) and post-processes it with `_dealStationChartModel` (`@0x243c054`).

## Response

(string-only: the post-processing is not followed) Top-level keys of `StationStatisticsModel` (`data/models.json`, `charging::StationStatisticsModel`): `power` (List?), `powerUnit` (String?), `chargeLevel` (List?), `energy` (List?), `energyUnit` (String?), `totalEnergy` (String?), `totalEnergyUnit` (String?), `totalImportedEnergy` (String?), `totalImportedEnergyUnit` (String?), `totalExportedEnergy` (String?), `totalExportedEnergyUnit` (String?), `aggregates` (List?), `hasDiesel` (bool?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "siteId": "<site_id>",
  "productCode": "",
  "sourceType": "<source_type>",
  "dateType": "<date_type>",
  "start": "<start>",
  "end": "<end>",
  "global": "<global>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/station/mixin/station_chart_http_reposity.dart`: `getChartStatistics` @0x2438ee4 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `siteId`, `sourceType`, `dateType`, `start`, `end` and `global`: parameters and a field of the mixin class; the literal `<String, Object?>` names no value type.
- Which values `dateType`, `sourceType` and `global` take: the callers of `getChartStatistics` are not in the call index of this page and were not found.
- The meaning of the request options (`cacheKey`, `loopSeconds`, `debounceMills`): passed as options of the mixin function, not body keys; the values were not decoded.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
