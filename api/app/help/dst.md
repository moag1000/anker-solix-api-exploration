> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# dst

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/app/help/dst`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x286bcb8`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `city` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x33c8864` |

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

- `charging/http/http_request_repository_impl.dart`: `getCloudCurrentTimezone` @0x33c8864 (requestHttp; encrypted: default-true (requestHttp) — verify); `getDaylightSavingTime` @0x286bbe8 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getCloudCurrentTimezone`
- `charging/http/http_request_repository.dart::getDaylightSavingTime`
- `charging/ui/page/device/a1340/a1340home/a1340home_logic.dart::_getDst`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::didChangeAppLifecycleState`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::onInit`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
