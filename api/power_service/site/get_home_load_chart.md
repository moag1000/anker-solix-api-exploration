> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_home_load_chart

## Purpose

<!-- TODO -->

## Upstream name

`home_load_chart` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/site/get_home_load_chart`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x28cced0`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x28cce04` |
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x28cce04` |

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

- `charging/http/http_request_repository_impl.dart`: `getSiteHomeLoadChat` @0x28cce04 (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::getSiteHomeLoadChat`, `charging/ui/page/device/a17c1/energy_plan/energy_plan_logic.dart::getSiteHomeLoadChatDate`, `charging/ui/page/device/main/sitation_energy_mian/energy_home/controller/energy_home_controller.dart::getSiteHomeLoadChatDate`, `charging/ui/page/device/main/sitation_energy_system/station_home_settings/merge_system_energy/merge_system_energy_plan_logic.dart::getSiteHomeLoadChatDate`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
