> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# energy_analysis

## Purpose

Reads the energy statistics chart of a site or device: the A1782 station chart (`A1782ChartHttpReposity::getChartStatistics`), the PPS chart (`ChartHttpReposity::getGreenPPsStatistics`) and the common station chart (`StationChartHttpReposity::getStationEnergyStatistics`) each send their own body to this URL.

## Upstream name

`energy_analysis` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/site/energy_analysis` (asm-traced) in every sender listed here; each sender loads the URL string and the method object (pool entry `pp+0xa7e0`, `Method.post`) in one call setup:

- `A1782ChartHttpReposity::getChartStatistics` (`chart_http_repository.dart @0x2370b5c`): URL string `@0x2370ff8`, method object `Method.post` (`pp+0xa7e0`) `@0x2370ff0`.
- `ChartHttpReposity::getGreenPPsStatistics` (`chart_http_repository.dart @0x23ff9fc`): URL string `@0x23ffc68`, method object `Method.post` (`pp+0xa7e0`) `@0x23ffc60`.
- `StationChartHttpReposity::getStationEnergyStatistics` (`station_chart_http_reposity.dart @0x230db24`): URL string `@0x230df60`, method object `Method.post` (`pp+0xa7e0`) `@0x230df58`.

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Three senders. The A1782 and PPS senders type their maps `<String, String?>` (pool `pp+0x8cb8`), so every value is a String or null.

Sender `A1782ChartHttpReposity::getChartStatistics` (`a1782/station/station_main_page/chart/chart_http_repository.dart @0x2370b5c`): 7 pairs (`AllocateArray r2 = 28` `@0x2370f2c`), type arguments `@0x2370fc4`.

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | string | yes | `"<site_id>"` | key `@0x2370f34`, value store `@0x2370f44` |
| `type` | string | yes | `"<type>"` | key `@0x2370f48`, value store `@0x2370f5c` (`ArrayLoad r1 = r2[0]`) |
| `device_sn` | string | yes | `"<device_sn>"` | key `@0x2370f60`, value store `@0x2370f70` |
| `device_type` | string | yes | `"<device_type>"` | key `@0x2370f74`, value store `@0x2370f84` |
| `start_time` | string | yes | `"<start_time>"` | key `@0x2370f88`, value store `@0x2370f98` |
| `end_time` | string | yes | `"<end_time>"` | key `@0x2370f9c`, value store `@0x2370fac` |
| `phase` | string | yes | `"<phase>"` | key `@0x2370fb0`, value store `@0x2370fc0` |

Sender `ChartHttpReposity::getGreenPPsStatistics` (`greenpower/charts/chart_http_repository.dart @0x23ff9fc`): 6 pairs, type arguments `@0x23ffc34`.

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | string | yes | `"<site_id>"` | key `@0x23ffac8`, value store `@0x23ffaf8` |
| `device_sn` | string | yes | `"<device_sn>"` | key `@0x23ffb20`, value store `@0x23ffb34` |
| `type` | string | yes | `"<type>"` | key `@0x23ffb58`, value store `@0x23ffb68` |
| `start_time` | string | yes | `"<start_time>"` | key `@0x23ffb8c`, value store `@0x23ffba0` |
| `device_type` | string | yes | `"<device_type>"` | key `@0x23ffbc4`, value store `@0x23ffbd8` |
| `end_time` | string | yes | `"<end_time>"` | key `@0x23ffbfc`, value store `@0x23ffc10` |

Sender `StationChartHttpReposity::getStationEnergyStatistics` (`common_view/charts/station_chart_http_reposity.dart @0x230db24`): 7 pairs typed `<String, dynamic>` (`AllocateArray r2 = 28` `@0x230dd74`, type arguments `@0x230df00`), so the value types are not given by the map.

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | yes | | key `@0x230dd80`, value store `@0x230dda4` (`field_7` of an Rx value) |
| `device_sn` | ? | yes | | key `@0x230ddcc`, value store `@0x230dde0` |
| `type` | ? | yes | | key `@0x230de04`, value store `@0x230de1c` (`field_23` of a parameter object) |
| `start_time` | ? | yes | | key `@0x230de40`, value store `@0x230de58` (`field_1b` of the parameter object) |
| `device_type` | ? | yes | | key `@0x230de7c`, value store `@0x230de90` |
| `enable_third_party_pv` | int (Smi, w) | yes | `1` | key `@0x230deb4`, `r16 = 2` `@0x230dec0` + store `@0x230dec4`, tagged, so 1 |
| `end_time` | ? | yes | | key `@0x230dec8`, value store `@0x230dedc` |
| `battery_type` | ? | optional | | `[]=` `@0x230df34`, key `@0x230df2c`; added only when a length field is non-zero (`cbz` `@0x230df1c`, `LoadField field_7` `@0x230df18`) |

## `param_type`/`cmd`

n/a

## Response model (link)

Per sender. A1782 sender: `charging::A1782StatisticsModel` (`data/models.json` key, no model page), parsed in the success closure `chart_http_repository.dart @0x2372d20` by `A1782StatisticsModel.fromJson`. PPS sender: `charging::PpsStatisticsModel` (`data/models.json` key, no model page), parsed in the success closure `greenpower/charts/chart_http_repository.dart @0x23ffcac` by `PpsStatisticsModel.fromJson`. Station sender: not determined; its callback `station_chart_http_reposity.dart @0x2323cac` hands the response to `_onGetStationEnergyStatistics` (not read).

## Response

Top-level keys of `A1782StatisticsModel` (from `data/models.json`): `power`, `charge_trend`, `charge_level` (Lists), `power_unit`, `charge_total`, `charge_unit`, `discharge_total`, `discharge_unit` (Strings), `statistics` (List), `solar_to_battery_total`, `grid_to_battery_total`, `third_solar_to_battery_total`, `sop_grid_to_battery_total`, `battery_to_home_total`, `total_energy_unit`, `grid_to_home_total`, `home_usage_total` (Strings), `pps_list` (List).

Top-level keys of `PpsStatisticsModel`: `power`, `charge_trend`, `charge_level` (Lists), `power_unit`, `charge_total`, `charge_unit`, `discharge_total`, `discharge_unit`, `charging_pre`, `electricity_pre`, `others_pre` (Strings), `statistics` (List).

## Example request/response

Request, synthesized (A1782 sender; values are placeholders)

```json
{"site_id": "<site_id>", "type": "<type>", "device_sn": "<device_sn>", "device_type": "<device_type>", "start_time": "<start_time>", "end_time": "<end_time>", "phase": "<phase>"}
```

Responses: keys listed under Response; no capture.

## Errors seen

None traced. The A1782 sender's success closure has no code compare; the failure callbacks were not read for the three senders. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a1782/station/station_main_page/chart/chart_http_repository.dart`: `getChartStatistics` @0x2370b5c (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/ui/page/device/greenpower/charts/chart_http_repository.dart`: `getGreenPPsStatistics` @0x23ff9fc (encryptionRequestHttp; encrypted: true)
- `common_view/charts/station_chart_http_reposity.dart`: `getStationEnergyStatistics` @0x230db24 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta. The models `A1782StatisticsModel` and `PpsStatisticsModel` are `≤3.18.0` in `data/models.json`.

## Known unknowns

- Types of the station sender's keys (the map is `<String, dynamic>`; values are Rx and parameter reads). Header stays string-only.
- The station sender's response handling (`_onGetStationEnergyStatistics`, not read).
- Which `type` and `device_type` values select which chart: the senders pass them through.
- Failure handling of the three senders was not read.

## Device-tested by

none
