> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# popup_record

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/app/news/popup_record`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/aiot/aiot_http_request_repository_impl.dart @0x2618470`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `popup_id` | ? | ? | ? | `charging/http/aiot/aiot_http_request_repository_impl.dart @0x2618388` |
| `popup_name` | ? | ? | ? | `charging/http/aiot/aiot_http_request_repository_impl.dart @0x2618388` |
| `popup_type` | ? | ? | ? | `charging/http/aiot/aiot_http_request_repository_impl.dart @0x2618388` |

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

- `charging/http/aiot/aiot_http_request_repository_impl.dart`: `reportAIOTPopupApi` @0x2618388 (aiotPlatformRequestHttp; encrypted: default-true (requestHttp) — verify)

Called from: `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::getAIOTPopupList`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
