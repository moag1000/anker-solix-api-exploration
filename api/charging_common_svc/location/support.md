> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# support

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_common_svc/location/support`, method: not extracted by the inventory <!-- TODO -->; string-only: `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a2fbe8`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `business_type` | ? | ? | ? | `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a2fa38` |
| `identifier_type` | ? | ? | ? | `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a2fa38` |
| `identifier_id` | ? | ? | ? | `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a2fa38` |

Rows are the union over 2 senders; `source` is the first sender that sets the key.

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

- `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart`: `getSupportLocation` @0x2a2fa38 (encryptionRequestHttp; encrypted: true)
- `charging/http/http_request_repository_impl.dart`: `getLocationSupport` @0x2892e34 (encryptionRequestHttp; encrypted: true)

Called from: `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart::goToMap`, `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart::onReady`, `charging/http/http_request_repository.dart::getLocationSupport`, `charging/ui/page/device/a17c5/ai_mode_condition/ai_mode_condition_logic.dart::getSupportLocation`, `charging/ui/page/device/main/sitation_energy_system/station_home_settings/station_home_settings_logic.dart::getSupportLocation`, `charging/ui/page/device/main/sitation_energy_system/station_home_settings/system_info/system_info_logic.dart::getSupportLocation`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
