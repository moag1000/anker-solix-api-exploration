> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# delete_site_devices

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/site/delete_site_devices`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x30c5f30`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys found by the extractor. <!-- TODO -->

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

- `charging/http/http_request_repository_impl.dart`: `deleteSitePPSRequest` @0x30c5eb0 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::deleteSitePPSRequest`
- `charging/ui/page/device/a17c0/remove_station_devices/remove_station_devices_logic.dart::deleteSiteDevice`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/add_devices/add_devices_logic.dart::deleteGroup`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/manage_devices/manage_devices_logic.dart::deleteSiteDevice`
- `charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart::deleteSitePPS`
- `charging/ui/page/green_energy/site/site_logic.dart::_deleteGroupDevices`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
