> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# join_site

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/share_site/join_site`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x2607644`

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

- `charging/http/http_request_repository_impl.dart`: `joinSite` @0x26075c0 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::joinSite`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::shareSiteMembersDialog`
- `charging/ui/page/message/messageSystemDetail/message_system_detail_logic.dart::shareSiteJoin`
- `charging/ui/page/message/messageSystemDetail/message_system_detail_logic.dart::shareSiteRefuse`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
