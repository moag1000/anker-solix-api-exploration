> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# co2_ranking

## Purpose

Reads the CO2 ranking card of a site: `StationEnergySystemLogic::getRankingInfo` (`station_energy_system_logic.dart @0x23a8cf8`) calls `queryRankingInfo`.

## Upstream name

`get_co2_ranking` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/site/co2_ranking` (asm-traced): URL string at `http_request_repository_impl.dart @0x23a8ea8`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x23a8ea0`, in `HttpRequestControllerImpl::queryRankingInfo` (`http_request_repository_impl.dart @0x23a8df8`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is a 1-pair map literal typed `<String, dynamic>` built in `queryRankingInfo` (`http_request_repository_impl.dart @0x23a8df8`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | yes | | key `charging/http/http_request_repository_impl.dart @0x23a8e4c`, value store `@0x23a8e5c` (parameter at `fp-0x10`); the caller passes `field_7` of an Rx value after a null check (`station_energy_system_logic.dart @0x23a8d38`..`@0x23a8d44`), no default |

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::RankEntity` (`data/models.json` key; fields on [`models/other.md`](../../../models/other.md#rankentity)), parsed in the builder's success closure `http_request_repository_impl.dart @0x23a8eec` by `RankEntity.fromJson`.

## Response

Top-level keys of the model (from `data/models.json`): `tree` (String), `show` (bool), `ranking` (String), `co2` (String), `level` (`Level`), `content` (String). `Level` (`charging/ui/page/device/main/sitation_energy_system/rank/RankEntity.dart`, `Level.fromJson` `@0x23a92e0`, `data/models.json`, `charging::Level`) has the keys `tree` (num, nullable) and `bubble` (num, nullable).

## Example request/response

Request, synthesized (type of `site_id` unresolved)

```json
{"site_id": "<site_id>"}
```

Response keys: see Response; no capture.

## Errors seen

None traced. The caller's failure callback `station_energy_system_logic.dart @0x23a9468` loads the code and message but no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `queryRankingInfo` @0x23a8df8 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::queryRankingInfo`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::getRankingInfo`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta. The model `RankEntity` is `≤3.18.0` in `data/models.json`.

## Known unknowns

- Type of `site_id`: the value is `field_7` of an Rx object with no default (`@0x23a8d38`); the object class was not followed. Header stays string-only.

## Device-tested by

none
