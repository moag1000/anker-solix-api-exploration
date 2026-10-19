> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_power_limit

## Purpose

Reads the station power limit state of a site: the selectable output limits, the legal limit, the per-device list and, since 3.24.3, the settings of the "DIY" unlock prompt.

## Upstream name

`get_site_power_limit` is the `API_ENDPOINTS` key in `api/apitypes.py`; the library method is `AnkerSolixApi.get_power_limit(siteId, fromFile)` in `api/api.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/site/get_power_limit` (asm-traced): URL string at `http_request_repository_impl.dart @0x2379094`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x237908c`, in `HttpRequestControllerImpl::getSitePowerLimit` (`http_request_repository_impl.dart @0x2378fb4`).

## Encrypted?

Yes (asm-traced): sent through `HttpRequestControllerImpl::encryptionRequestHttp` (`http_request_repository_impl.dart @0x23790c4`). The scheme is described in `api/encryption.md`.

## Request

The body starts as a one-pair map literal (2 slots, raw `r2 = 4`, `@0x2379008`) holding `site_id`; `app_ability` is added afterwards with `[]=` (`@0x2379048` to `@0x2379050`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | String | yes | `"<site_id>"` | `http_request_repository_impl.dart @0x2379010` (value from parameter r5) |
| `app_ability` | object (`Map<String, dynamic>`) | sent by the app | `{"site_power_limit": true}` | `http_request_repository_impl.dart @0x2379048` (value from parameter r2); both callers pass the map literal `{"site_power_limit": true}`: `station_power_limit_logic.dart @0x28cac40`/`@0x28cac4c` and `energy_plan_logic.dart @0x28caa50`/`@0x28caa5c` |

The upstream library sends only `site_id` (`api/api.py`, `get_power_limit()`), so `app_ability` is not required for a response; what it changes is not known (see Known unknowns).

## `param_type`/`cmd`

n/a

## Response model (link)

[`StationPowerLimitModel`](../../../models/station_power_limit.md), parsed in the success closure at `http_request_repository_impl.dart @0x23790e0` by `StationPowerLimitModel.fromJson` (`@0x2379110`).

## Response

All fields of the response object belong to the model page; this endpoint adds no wrapper fields of its own.

| field | type | required | example | source |
|---|---|---|---|---|
| (model fields) | see [`StationPowerLimitModel`](../../../models/station_power_limit.md) | | | `station_power_limit_model.dart @0x2379150` |

## Example request/response

Request, synthesized (decrypted body as built by `getSitePowerLimit`)

```json
{"site_id": "<site_id>", "app_ability": {"site_power_limit": true}}
```

Response, synthesized (keys from `StationPowerLimitModel.fromJson`; values are placeholders, not a capture)

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "site_id": "<site_id>",
    "ac_input_power_unit": "1200W",
    "ac_input_power": 1200,
    "legal_power_limit": 800,
    "parallel_type": "<parallel_type>",
    "ae100_info": null,
    "device_info": [],
    "legal_limit": 800,
    "power_limit_option": [{"limit": 800, "limit_real": 800}],
    "exceed_alarm": false,
    "unlock_default_power_type": 0,
    "unlock_pop_content": "",
    "unlock_pop_image": ""
  }
}
```

## Errors seen

None recorded. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `StationPowerLimitLogic::_getStationPowerLimit` (`station_power_limit_logic.dart @0x28cab4c`, call at `@0x28cac9c`), run from `StationPowerLimitLogic::onInit` (`@0x34b0bdc`) when the station power limit page opens; it returns early when the site id is empty (`@0x28cab98`). Flow: [../../../flows/system_output_limit.md](../../../flows/system_output_limit.md).
- `EnergyPlanLogic::getStationPowerLimit` (`energy_plan_logic.dart`, call at `@0x28caaac`), A17C1 energy plan page.
- `HttpRequestController` interface stub (`http_request_repository.dart @0x2378f8c`).

## Since/changed

3.18.0: the model parsed 9 keys (3.18.0 `station_power_limit_model.dart @0x1a56c9c`). 3.24.3: 13 keys; `ac_input_power`, `unlock_default_power_type`, `unlock_pop_content` and `unlock_pop_image` are new. Details on [the model page](../../../models/station_power_limit.md#changed-since-3180).

## Known unknowns

- What `app_ability: {"site_power_limit": true}` changes in the server response compared with the upstream request that omits it.
- Whether the server requires the encrypted request path for this endpoint (the upstream library uses the plain path).

## Device-tested by

none
