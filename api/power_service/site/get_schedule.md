> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_schedule

## Purpose

Reads the strategy schedule of a site: the A17C1 cost-savings page and the station energy system (`getSchedule`), the A17E2 home controller (`_updateInfo` / `_updateEmsModeData`), the mode-tip logic and the AI-EMS request (`requestSiteSchedule`) send `site_id` through three senders.

## Upstream name

`get_forecast_schedule` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/site/get_schedule` (asm-traced) at the senders that load a `Method` object next to the URL string (pool entry `pp+0xa7e0`, `Method.post`):

- `HttpRequestControllerImpl::getSiteSchedule` (`http_request_repository_impl.dart @0x23a6010`): URL string `@0x23a60c4`, method object `Method.post` (`pp+0xa7e0`) `@0x23a60bc`.
- `A17E2HomeController::_updateEmsModeData` (`a17e2_home_controller.dart @0x355e0b0`): URL string `@0x355e298`, method object `Method.post` (`pp+0xa7e0`) `@0x355e290`.

The third sender `EmsServiceImpl::getSiteSchedule` (`ems_service_impl.dart @0x22d7594`) calls `HttpHelper::getDataFromService` (`@0x22d76d4`) with the URL `"/power_service/v1/site/get_schedule"` (`@0x22d76c4`) and no method argument; the helper (`http_helper.dart @0x22ba2bc`) substitutes the `Method` pool object `pp+0xa7e0` (`Method.post`) when the method is null (`cmp w1, NULL` `@0x22ba378`, `Instance_Method` `@0x22ba380`), so that sender posts too.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

All three senders type their map, so the value is a String (or null where `String?`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | string | yes | `"<site_id>"` | `HttpRequestControllerImpl::getSiteSchedule` (`http_request_repository_impl.dart @0x23a6010`): `<String, String>` (`@0x23a6078`), key `@0x23a6064`, store `@0x23a6074`; `A17E2HomeController::_updateEmsModeData` (`a17e2_home_controller.dart @0x355e0b0`): `<String, String?>` (`@0x355e260`), key `@0x355e24c`, store `@0x355e25c` (from `getSiteIdByDeviceSn` `@0x355e210`); `EmsServiceImpl::getSiteSchedule`: `<String, String>` (`@0x22d7680`), key `@0x22d766c`, store `@0x22d767c`; this sender returns without a request when the id is empty (`cbnz w1` `@0x22d75ec`) |

## `param_type`/`cmd`

n/a

## Response model (link)

Per sender. `getSiteSchedule` (repository): `charging::SiteScheduleModel` (`data/models.json` key; fields on [`models/other.md`](../../../models/other.md#siteschedulemodel)), parsed in the success closure `http_request_repository_impl.dart @0x23a6108` (`SiteScheduleModel.fromJson` resolves to `charging/model/site_schedule_model.dart`). `EmsServiceImpl::getSiteSchedule`: `base_service::SiteScheduleModel` (`data/models.json` key, no model page), parsed in `ems_service_impl.dart @0x22d77b0` (resolves to `base_service/bean/model/schedule/site_schedule_model.dart`; invalid data logs `"getSiteSchedule: invalid response data"`). `A17E2HomeController::_updateEmsModeData`: no model; the success closure `a17e2_home_controller.dart @0x355e5c0` reads the key `status` (`@0x355e670`) and compares it with 1, 2 and 3 (32-bit compares `cmp w0, #2` `@0x355e6a0`, `#4` `@0x355e6a8`, `#6` `@0x355e6b0`, tagged, so 1, 2, 3) before setting a value.

## Response

Top-level keys of `charging::SiteScheduleModel` (from `data/models.json`): `status` (int), `remain_energy` (`RemainEnergyInfo`), `negative_price` (Iterable), `push_time` (String). The `base_service::SiteScheduleModel` of 3.24.3 adds `current_strategy` (`CurrentStrategy`). The A17E2 sender reads `status` only.

## Example request/response

Request, synthesized

```json
{"site_id": "<site_id>"}
```

Response keys: see Response; no capture.

## Errors seen

None traced. The failure callbacks (`ems_service_impl.dart @0x22d76f0`, forwarding templates in the repository) log or forward the code; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `ak_soft_ems/ems_service_impl.dart`: `getSiteSchedule` @0x22d7594 (URL literal only, no `*Http*` call; sender `HttpHelper::getDataFromService` (`ak_soft_ems/http/http_helper.dart @0x22ba2bc`) (HTTP helper wrapper), called from the same function; resolved from the URL literal at `ak_soft_ems/ems_service_impl.dart @0x22d76c4` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `charging/http/http_request_repository_impl.dart`: `getSiteSchedule` @0x23a6010 (encryptionRequestHttp; encrypted: true)
- `micro_hes/src/a17e2/home/a17e2_home_controller.dart`: `_updateEmsModeData` @0x355e0b0 (encryptionRequestHttp; encrypted: true)

Called from:

- `ak_soft_ems/aiems/api/ai_ems_request.dart::requestSiteSchedule`
- `charging/http/http_request_repository.dart::getSiteSchedule`
- `charging/ui/page/device/a17c1/cost_savings/cost_savings_logic.dart::getSchedule`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::getSchedule`
- `micro_hes/src/a17e2/home/a17e2_home_controller.dart::_updateInfo`
- `micro_hes/src/common_business/basic_station/module/mode_tip/mode_tip_logic.dart::getSchedule`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`. In 3.24.3 two model classes exist: `charging::SiteScheduleModel` (`≤3.18.0`) and `base_service::SiteScheduleModel` (new in 3.24.3, with the extra key `current_strategy`).

## Known unknowns

- Which of the two `SiteScheduleModel` shapes the server returns: the repository sender parses the `charging` class, the EMS service parses the `base_service` class; both read the same URL.
- What the `status` values 1, 2 and 3 mean to the A17E2 home controller: only the compares are read.
- Failure handling of the repository sender's callers was not read.

## Device-tested by

none
