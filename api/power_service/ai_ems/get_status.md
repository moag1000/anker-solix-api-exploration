> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_status

## Purpose

Reads the AI-EMS mode status of a site (status, result text and remaining time) for the A17C1 home, the AI-mode study/success pages and the station energy system page (callers `A17c1homeLogic::getAiModeStatus`, `AiModeStudyLogic::getAiModeStatus`, `AiModeSuccessLogic::getAiModeStatus`, `StationEnergySystemLogic::getAiModeStatus`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`get_ai_ems_status` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/ai_ems/get_status` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x23a0c48`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x23a0c40`, in `HttpRequestControllerImpl::getAiModeStatusRequest` (`charging/http/http_request_repository_impl.dart @0x23a0ba0`), sent through `encryptionRequestHttp` (`@0x23a0c70`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) The body is one map literal of 1 pair (`AllocateArray`, raw `r2 = 4` at `@0x23a0be0`, so 2 slots) with type arguments `<String, String>` at `@0x23a0bfc`, so every value is typed in the literal; all keys are stored unconditionally.

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | string | yes | `"<site_id>"` | `charging/http/http_request_repository_impl.dart @0x23a0be8` |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`AiModeStatusModel`](../../../models/other.md#aimodestatusmodel), parsed by `AiModeStatusModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x23a0d3c`

## Response

(asm-traced) All keys belong to the model page; this endpoint adds no wrapper fields of its own in the code read.

- `AiModeStatusModel` top-level keys (`data/models.json`, `charging::AiModeStatusModel`): `status` (int?), `result` (String?), `left_time` (int?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "site_id": "<site_id>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getAiModeStatusRequest` @0x23a0ba0 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getAiModeStatusRequest`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::getAiModeStatus`
- `charging/ui/page/device/a17c5/ai_mode_condition/ai_mode_condition_logic.dart::setHomeLoadSiteParam`
- `charging/ui/page/device/a17c5/ai_mode_success/ai_mode_success_logic.dart::getAiModeStatus`
- `charging/ui/page/device/main/sitation_energy_system/ai_mode_study/ai_mode_study_logic.dart::getAiModeStatus`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::getAiModeStatus`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/power_usage_scenario_logic.dart::getAiModeStatus`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the numeric `status` values and the `result` strings mean: the model stores them as `int?` and `String?` and this page does not trace their readers.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
