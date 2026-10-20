> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_energy_statistics

## Purpose

Reads the energy statistics for the chart pages (`A5101StatisticsModel`) through `ChartHttpReposity::getChartStatistics`; the builder first looks into a cache (`getCache` `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x23e57c0`) and logs `getPvStatistics` (string-only: no caller chain in `data/endpoints.json`, inferred from the builder name).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_energy_statistics` (asm-traced): URL string at `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x23e5a10`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x23e5a08`, in `ChartHttpReposity::getChartStatistics` (`charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x23e5710`), sent through `requestHttp` (`@0x23e5a50`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `ChartHttpReposity::getChartStatistics` (`charging/ui/page/device/a5101/charts/chart_http_repository.dart`, call `@0x23e5a50`, argument list `@0x23e5a48`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

`ChartHttpReposity::getChartStatistics` (`charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x23e5710`) stores 7 keys in a map literal with type arguments `<String, Object?>` (`@0x23e59dc`), which do not type the values; the values are parameters or fields (`@0x23e5944`..`@0x23e59d8`) stored as received, except `productCode`, which is the empty string when its parameter is null (`@0x23e5964`). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | ? | yes | ? | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x23e5938` |
| `productCode` | ? | yes | `""` when the parameter is null | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x23e594c` |
| `sourceType` | ? | yes | ? | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x23e5984` |
| `dateType` | ? | yes | ? | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x23e599c` |
| `start` | ? | yes | ? | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x23e59b4` |
| `end` | ? | yes | ? | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x23e59c0` |
| `global` | ? | yes | ? | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x23e59cc` |

## `param_type`/`cmd`

n/a

## Response model (link)

- `charging::A5101StatisticsModel`, parsed by `A5101StatisticsModel.fromJson` at `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x23e9810` (success closure `@0x23e97c4`, `bl` target `[package:charging/model/a5101/a5101_statistics_model/a5101_statistics_model.dart]`). The builder also serves the same model from a cache lookup (`getCache` `@0x23e57c0`, `checkMax` `@0x23e5810`) before it sends the request.

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::A5101StatisticsModel`): `power` (List?), `powerUnit` (String?), `chargeLevel` (List?), `energy` (List?), `energyUnit` (String?), `totalEnergy` (String?), `totalEnergyUnit` (String?), `totalImportedEnergy` (String?), `totalImportedEnergyUnit` (String?), `totalExportedEnergy` (String?), `totalExportedEnergyUnit` (String?), `aggregates` (List?), `totalForecastEnergy` (String?), `forecastPower` (List?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "siteId": "<siteId>",
  "productCode": "",
  "sourceType": "<sourceType>",
  "dateType": "<dateType>",
  "start": "<start>",
  "end": "<end>",
  "global": "<global>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a5101/charts/chart_http_repository.dart`: `getChartStatistics` @0x23e5710 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The types of all seven keys: the values are not converted in the builder.
- The named arguments `cacheKey`, `debounceMills`, `loopSeconds` and `showDefaultError` (argument list `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x23e5a48`) change how the HTTP layer repeats and caches the call; the layer was not read for them.
- No caller of `getChartStatistics` is recorded in `data/endpoints.json`.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
