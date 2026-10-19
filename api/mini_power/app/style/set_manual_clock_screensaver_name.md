> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# set_manual_clock_screensaver_name

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/mini_power/v1/app/style/set_manual_clock_screensaver_name`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x3e22a40`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3e22940` |
| `screensaver_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3e22940` |
| `name` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3e22940` |

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

- `charging/http/http_request_repository_impl.dart`: `editA2345CustomClockScreenSaversName` @0x3e22940 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from: `charging/http/http_request_repository.dart::editA2345CustomClockScreenSaversName`, `charging/ui/page/device/a2345/a2345custom_clock/a2345custom_clock_logic.dart::_saveScreenName`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
