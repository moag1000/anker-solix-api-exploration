> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# support

## Purpose

Asks which locations (country codes) the AI-mode / dynamic-price features support for a site (callers `EmsAiModeConditionLogic::getSupportLocation` and `HttpRequestControllerImpl::getLocationSupport`; UI callers `EmsAiModeConditionLogic::onReady`, `AiModeConditionLogic::getSupportLocation`, `StationHomeSettingsLogic::getSupportLocation`) (string-only: inferred from the caller names, the chain is not in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_common_svc/location/support` (asm-traced).

- `EmsAiModeConditionLogic::getSupportLocation` (`ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a2fa38`): URL string `@0x2a2fbe8`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x2a2fbe0`, sent through `HttpServiceImpl::encryptionRequestHttp` (`@0x2a2fc10`).
- `HttpRequestControllerImpl::getLocationSupport` (`charging/http/http_request_repository_impl.dart @0x2892e34`): URL `@0x2892f0c`, `Method.post` (`pp+0xa7e0`) `@0x2892f04`, `encryptionRequestHttp` `@0x2892f34`.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: one field type is not read) Both senders build the same three keys in a `<String, Object>` literal (`ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a2fb88`, `charging/http/http_request_repository_impl.dart @0x2892ec0`), which names no value type; the two integer keys are typed from their stored immediates.

| field | type | required | example | source |
|---|---|---|---|---|
| `business_type` | int (Smi, w) | yes | `2` (raw immediate 4, 32-bit store) | `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a2fb44` (value store `@0x2a2fb54`); `charging/http/http_request_repository_impl.dart @0x2892e84` (store `@0x2892e94`) |
| `identifier_type` | int (Smi, w) | yes | `2` (raw immediate 4, 32-bit store) | `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a2fb58` (store `@0x2a2fb68`); `charging/http/http_request_repository_impl.dart @0x2892e98` (store `@0x2892ea8`) |
| `identifier_id` | ? | yes | `"<site_id>"` | `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a2fb6c` (`LoadField` `@0x2a2fb7c`, store `@0x2a2fb84`); `charging/http/http_request_repository_impl.dart @0x2892eac` (parameter, store `@0x2892ebc`) |

## `param_type`/`cmd`

n/a

## Response model (link)

- `ak_soft_ems::SupportLocation`, parsed by `SupportLocation.fromJson` at `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a2fd38` (success closure `@0x2a2fd00`) in `EmsAiModeConditionLogic::getSupportLocation`.
- `charging::SupportLocation`, parsed by `SupportLocation.fromJson` at `charging/http/http_request_repository_impl.dart @0x2892f88` (success closure `@0x2892f50`) in `HttpRequestControllerImpl::getLocationSupport`.
- No `models/` page documents the class fields; [models/other.md](../../../models/other.md#supportlocation) holds a stub whose key (`code`) differs from the key list of `data/models.json` below (owned by that page, not changed here).

## Response

Top-level keys of both classes (`data/models.json`, `ak_soft_ems::SupportLocation` and `charging::SupportLocation`): `country_code` (type not named by the extractor). Neither sender adds a wrapper field in the closures read.

## Example request/response

Request, synthesized (decrypted body as built by `HttpRequestControllerImpl::getLocationSupport`; `<...>` are placeholders, not captured values)

```json
{
  "business_type": 2,
  "identifier_type": 2,
  "identifier_id": "<site_id>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the senders or closures read for this page (the failure closure `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a2fc30` logs the code and shows a toast). Code meanings are owned by `api/errors.md`.

## Callers in app

- `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart`: `getSupportLocation` @0x2a2fa38 (encryptionRequestHttp; encrypted: true)
- `charging/http/http_request_repository_impl.dart`: `getLocationSupport` @0x2892e34 (encryptionRequestHttp; encrypted: true)

Called from:

- `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart::goToMap`
- `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart::onReady`
- `charging/http/http_request_repository.dart::getLocationSupport`
- `charging/ui/page/device/a17c5/ai_mode_condition/ai_mode_condition_logic.dart::getSupportLocation`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/station_home_settings_logic.dart::getSupportLocation`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/system_info/system_info_logic.dart::getSupportLocation`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `identifier_id`: a field value (`ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a2fb7c`) or a parameter; the declared type is not visible.
- What `business_type` 2 and `identifier_type` 2 select on the server: the app stores them as constants only.
- The type of `country_code` in `SupportLocation` (the extractor lists it as unknown) and whether the answer is a list or a single value.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
