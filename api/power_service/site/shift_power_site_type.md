> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# shift_power_site_type

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/site/shift_power_site_type`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x238c88c`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x238c7c4` |
| `power_site_type` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x238c7c4` |

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

- `charging/http/http_request_repository_impl.dart`: `shiftPowerSite` @0x238c7c4 (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::shiftPowerSite`, `charging/ui/page/device/a17c0/remove_station_devices/remove_station_devices_logic.dart::shiftC1toC0`, `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::checkC1ToC0Station`, `charging/ui/page/device/main/sitation_energy_system/station_home_settings/manage_devices/manage_devices_logic.dart::checkC1ToC0Station`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
