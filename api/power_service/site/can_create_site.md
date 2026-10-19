> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# can_create_site

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/site/can_create_site`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x2902200`
(literal also at 1 more site(s) in `data/endpoints.json`)

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

- `charging/http/http_request_repository_impl.dart`: `checkCanCreateSite` @0x2902144 (encryptionRequestHttp; encrypted: true); `createSiteHomeRequest` @0x290487c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::checkCanCreateSite`
- `charging/http/http_request_repository.dart::createSiteHomeRequest`
- `charging/ui/page/device/main/station_device_home/station_main_page/station_main_page_logic.dart::checkCanCreateStation`
- `charging/ui/page/green_energy/site/site_logic.dart::_deleteGroupDevices`
- `charging/ui/page/green_energy/site/site_logic.dart::createSiteHome`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
