> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# add_manual_clock_screensavers

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/mini_power/v1/app/style/add_manual_clock_screensavers`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x3e19d98`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3e19ca0` |
| `img_url` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3e19ca0` |
| `hash_code` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3e19ca0` |

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

- `charging/http/http_request_repository_impl.dart`: `addA2345CustomClockScreenSavers` @0x3e19ca0 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from: `charging/http/http_request_repository.dart::addA2345CustomClockScreenSavers`, `charging/ui/page/device/a2345/a2345clock_style/a2345clock_style_logic.dart::addCustomClockScreenSavers`, `charging/ui/page/device/a2345/a2345custom_clock/a2345custom_clock_logic.dart::addCustomClockScreenSavers`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
