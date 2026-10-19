> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# delete_manual_clock_screensavers

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/mini_power/v1/app/style/delete_manual_clock_screensavers`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x3e21000`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3e20f2c` |

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

- `charging/http/http_request_repository_impl.dart`: `deleteA2345CustomClockScreenSavers` @0x3e20f2c (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from: `charging/http/http_request_repository.dart::deleteA2345CustomClockScreenSavers`, `charging/ui/page/device/a2345/a2345custom_clock/a2345custom_clock_logic.dart::deleteCustomClockScreenSavers`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
