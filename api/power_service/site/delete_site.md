> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# delete_site

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/site/delete_site`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x30c5424`

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

- `charging/http/http_request_repository_impl.dart`: `deleteSite` @0x30c53a0 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::deleteSite`
- `charging/ui/page/device/a17b1/system_info/system_info_logic.dart::deleteSiteRes`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/system_info/system_info_logic.dart::deleteSiteRes`
- `charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart::deleteSiteRes`
- `charging/ui/page/user/share_site/home_center/home_center_logic.dart::deleteSiteRes`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
