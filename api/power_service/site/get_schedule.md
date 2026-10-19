> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_schedule

## Purpose

<!-- TODO -->

## Upstream name

`get_forecast_schedule` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/site/get_schedule`, method: not extracted by the inventory <!-- TODO -->; string-only: `ak_soft_ems/ems_service_impl.dart @0x22d76c4`
(literal also at 2 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `ak_soft_ems/ems_service_impl.dart @0x22d7594` |

Rows are the union over 3 senders; `source` is the first sender that sets the key.

## `param_type`/`cmd`

n/a

## Response model (link)

<!-- TODO -->

## Response

<!-- TODO -->

## Example request/response

<!-- TODO -->

## Errors seen

`api/errors.md`: <!-- TODO -->

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

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
