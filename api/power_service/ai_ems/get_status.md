> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_status

## Purpose

<!-- TODO -->

## Upstream name

`get_ai_ems_status` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/ai_ems/get_status`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x23a0c48`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x23a0ba0` |

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

- `charging/http/http_request_repository_impl.dart`: `getAiModeStatusRequest` @0x23a0ba0 (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::getAiModeStatusRequest`, `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::getAiModeStatus`, `charging/ui/page/device/a17c5/ai_mode_condition/ai_mode_condition_logic.dart::setHomeLoadSiteParam`, `charging/ui/page/device/a17c5/ai_mode_success/ai_mode_success_logic.dart::getAiModeStatus`, `charging/ui/page/device/main/sitation_energy_system/ai_mode_study/ai_mode_study_logic.dart::getAiModeStatus`, `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::getAiModeStatus`, `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/power_usage_scenario_logic.dart::getAiModeStatus`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
