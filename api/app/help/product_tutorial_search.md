> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# product_tutorial_search

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/app/help/product_tutorial_search`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x291a65c`

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

- `charging/http/http_request_repository_impl.dart`: `searchUserManualsDeviceDataList` @0x291a52c (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::searchUserManualsDeviceDataList`, `charging/ui/page/device/main/station_device_home/StationUsermanuals/station_usermanuals_logic.dart::_getDevicesList`, `charging/ui/page/user/userManuals/searchDeviceUserManuals/search_device_user_manuals_logic.dart::searchDeviceNameList`, `charging/ui/page/user/userManuals/searchDeviceUserManuals/search_device_user_manuals_logic.dart::searchDeviceUserManualsList`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
