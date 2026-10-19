> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

Removed in 3.24.3 — present in 3.18.0 only

# get_screensaver_img_url

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/mini_power/v1/app/style/get_screensaver_img_url`, method: not extracted by the inventory <!-- TODO -->; string-only: `small_charging_platform/src/screen_setting/clock_style/page/clock_style_logic.dart @0x2550134`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `id` | ? | ? | ? | `small_charging_platform/src/screen_setting/clock_style/page/clock_style_logic.dart @0x2550030` |
| `type` | ? | ? | ? | `small_charging_platform/src/screen_setting/clock_style/page/clock_style_logic.dart @0x2550030` |

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

- `small_charging_platform/src/screen_setting/clock_style/page/clock_style_logic.dart`: `getScreensaverImgUrl` @0x2550030 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: absent (removed). since: ≤3.18.0.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
