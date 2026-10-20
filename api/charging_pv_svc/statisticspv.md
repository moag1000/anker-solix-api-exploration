> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# statisticsPv

## Purpose

Loads the PV generation statistics (curve, energy, money) for a period on the A5140, A5150 and green-power chart pages (callers `ChartHttpReposity::getPvStatistics`, `A5150HomeHttpReposity::getPvStatistics`, `A5150SolarDetailsReposity::getSolarStatistics`, `ChartHttpReposity::getGreenPvStatistics`) (string-only: inferred from the function names, no caller chain is in `data/endpoints.json`).

## Upstream name

`get_device_pv_statistics` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /charging_pv_svc/statisticsPv` (asm-traced) at four senders, all through the mixin `encryptionRequestHttp` of `HttpRequestController` with the options `cacheKey`, `isAIotErrorCode`, `isLogResponse`, `showDefaultError`, `success` (and `fail` in the first):

- `ChartHttpReposity::getPvStatistics` (`charging/ui/page/device/a5140/a5140charts/chart_http_reposity.dart @0x3036204`): URL string `@0x30363e4`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x30363dc`, call `@0x3036420`.
- `A5150HomeHttpReposity::getPvStatistics` (`charging/ui/page/device/a5150/homePage/a5150_http_reposity.dart @0x303d01c`): URL `@0x303d1e4`, `Method.post` `@0x303d1dc`, call `@0x303d218`.
- `A5150SolarDetailsReposity::getSolarStatistics` (`charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x2933314`): URL `@0x2933500`, `Method.post` `@0x29334f8`, call `@0x2933534`.
- `ChartHttpReposity::getGreenPvStatistics` (`charging/ui/page/device/greenpower/charts/chart_http_repository.dart @0x23fec04`): URL `@0x23feee0`, `Method.post` `@0x23feed8`, call `@0x23fef14`.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: the third sender's types are not read) Three senders use `<String, String?>` literals (`charging/ui/page/device/a5140/a5140charts/chart_http_reposity.dart @0x3036398`, `charging/ui/page/device/a5150/homePage/a5150_http_reposity.dart @0x303d1b0`, `charging/ui/page/device/greenpower/charts/chart_http_repository.dart @0x23feeac`), so their values are strings (each may be null); `getSolarStatistics` uses `<String, Object?>` (`charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x29334cc`), which names no value type. All keys are stored without a guard. The table gives the type per sender where they differ.

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | string (`getPvStatistics` x2, `getGreenPvStatistics`); ? (`getSolarStatistics`) | yes | `"<sn>"` | `charging/ui/page/device/a5140/a5140charts/chart_http_reposity.dart @0x303633c` (value store `@0x303634c`); `charging/ui/page/device/a5150/homePage/a5150_http_reposity.dart @0x303d154`; `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x2933418`; `charging/ui/page/device/greenpower/charts/chart_http_repository.dart @0x23fedd8` |
| `type` | string (three senders); ? (`getSolarStatistics`) | yes | `"<type>"` | `charging/ui/page/device/a5140/a5140charts/chart_http_reposity.dart @0x3036350` (value store `@0x303635c`); `charging/ui/page/device/a5150/homePage/a5150_http_reposity.dart @0x303d168`; `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x2933498`; `charging/ui/page/device/greenpower/charts/chart_http_repository.dart @0x23fee10` |
| `start` | string (three senders); ? (`getSolarStatistics`) | yes | `"<start>"` | `charging/ui/page/device/a5140/a5140charts/chart_http_reposity.dart @0x3036360` (value store `@0x303636c`); `charging/ui/page/device/a5150/homePage/a5150_http_reposity.dart @0x303d178`; `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x293342c`; `charging/ui/page/device/greenpower/charts/chart_http_repository.dart @0x23fee44` |
| `end` | string (three senders); ? (`getSolarStatistics`) | yes | `"<end>"` | `charging/ui/page/device/a5140/a5140charts/chart_http_reposity.dart @0x3036370` (value store `@0x303637c`); `charging/ui/page/device/a5150/homePage/a5150_http_reposity.dart @0x303d188`; `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x293343c`; `charging/ui/page/device/greenpower/charts/chart_http_repository.dart @0x23fee78` |
| `version` | string | yes | `"1"` | `charging/ui/page/device/a5140/a5140charts/chart_http_reposity.dart @0x3036380` (constant `@0x303638c`); `charging/ui/page/device/a5150/homePage/a5150_http_reposity.dart @0x303d198` (constant `@0x303d1a4`); not sent by the other two senders |
| `siteId` | string in `getGreenPvStatistics`; ? in `getSolarStatistics` | yes | `"<site_id>"` | `charging/ui/page/device/greenpower/charts/chart_http_repository.dart @0x23fed80` (value from a field, `LoadField` `@0x23fed90`); `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x2933404`; not sent by the other two senders |
| `dcPort` | int (unboxed, x) | yes | `<dc_port>` | `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x293344c` (`BoxInt64Instr` `@0x293345c`); `getSolarStatistics` only |

## `param_type`/`cmd`

n/a

## Response model (link)

Three classes, one per sender pair (no `models/` pages):

- `charging/model/a5140_device_info::PvStatisticsModel`, parsed by `PvStatisticsModel.fromJson` at `charging/ui/page/device/a5140/a5140charts/chart_http_reposity.dart @0x3037324` (success closure `@0x30372ec`; cached entry at `@0x30362fc`).
- `charging::SolarStatisticsModel`, parsed by `SolarStatisticsModel.fromJson` at `charging/ui/page/device/a5150/homePage/a5150_http_reposity.dart @0x303d278` (closure `@0x303d22c`; cached entry `@0x303d114`) and at `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart @0x293470c` (closure `@0x293468c`).
- `charging/model/green_energy::PvStatisticsModel`, parsed by `PvStatisticsModel.fromJson` at `charging/ui/page/device/greenpower/charts/chart_http_repository.dart @0x23ff7e0` (closure `@0x23ff794`; cached entry `@0x23fed14`).

## Response

(string-only: three different shapes) Top-level keys from `data/models.json`:

- `charging/model/a5140_device_info::PvStatisticsModel`: `curve` (type not named), `energy` (type not named), `solarGeneraion` (num?), `energyUnit` (String?), `moneyUnit` (String?), `money` (num?), `high` (num?), `low` (num?).
- `charging::SolarStatisticsModel`: `curve` (List?), `energy` (List?), `energyUnit` (type not named), `solarGeneraion` (int?), `money` (int?), `moneyUnit` (type not named), `generationTime` (int?), `maxPower` (int?).
- `charging/model/green_energy::PvStatisticsModel`: `solarGeneraion` (num?), `money` (num?), `energyUnit` (String?), `loadPercent` (String?), `ppsPercent` (String?), `moneyUnit` (String?), `curve` (List?), `energy` (List?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "sn": "<sn>",
  "type": "<type>",
  "start": "<start>",
  "end": "<end>",
  "version": "1"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a5140/a5140charts/chart_http_reposity.dart`: `getPvStatistics` @0x3036204 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/a5150/homePage/a5150_http_reposity.dart`: `getPvStatistics` @0x303d01c (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/a5150/solarDetails/a5150_solar_details_http_repository.dart`: `getSolarStatistics` @0x2933314 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/greenpower/charts/chart_http_repository.dart`: `getGreenPvStatistics` @0x23fec04 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `siteId`, `sn`, `start`, `end` and `type` in `getSolarStatistics`: the literal `<String, Object?>` names no value type.
- Which `type` values (period names) and date formats the callers pass: the callers of the four functions were not found in the call index.
- Whether the server answers the three shapes from one handler or distinguishes the senders by `version`/`dcPort`/`siteId`: not known from the app.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
