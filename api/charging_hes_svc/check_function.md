> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# check_function

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/check_function`, method: not extracted by the inventory <!-- TODO -->; string-only: `base_service/api_url.dart @0x2349c68`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x28e7e58` |

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

- `base_service/api_url.dart`: `checkFunction` @0x2349c50 (URL literal only, no `*Http*` call; sender found through callers: `A17E2StationLogic::_checkVppFunction` (`micro_hes/src/a17e2/station/home/a17e2_station_logic.dart @0x2349388`) via `A17E2StationLogic::_checkVppFunction` (`micro_hes/src/a17e2/station/home/a17e2_station_logic.dart @0x2349388`); also `PowerUsageScenarioController::checkVppFunction`)
- `charging/http/http_request_repository_impl.dart`: `checkFunction` @0x28e7e58 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::checkFunction`
- `charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart::_checkNemFunction`
- `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::getLatestSystemFunction`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
