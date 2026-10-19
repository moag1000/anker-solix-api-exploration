> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_clock_screensavers

## Purpose

<!-- TODO -->

## Upstream name

`charger_get_screensavers` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/mini_power/v1/app/style/get_clock_screensavers`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x28ade0c`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `product_code` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x28add4c` |

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

- `charging/http/http_request_repository_impl.dart`: `getA2345ClockScreenSavers` @0x28add4c (requestHttp; encrypted: default-true (requestHttp) — verify); `getScreenSaversByCategory` @0x29de9f4 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getA2345ClockScreenSavers`
- `charging/ui/page/device/a1782/screen_saver/screen_theme_setting/screen_theme_setting_logic.dart::_updateNetworkThemeList`
- `charging/ui/page/device/a2345/a2345clock_display/a2345clock_display_logic.dart::getCategoryClockScreenSavers`
- `charging/ui/page/device/a2345/a2345clock_style/a2345clock_style_logic.dart::getCategoryClockScreenSavers`
- `charging/ui/page/device/a25x7/a25x7screensaver/a25x7screensaver_logic.dart::_updateNetworkThemeList`
- `charging/ui/page/device/a25x7/a25x7screensaver_style/a25x7screensaver_style_logic.dart::_updateNetworkThemeCategory`
- `small_charging_platform/src/screen_setting/clock_style/page/clock_style_logic.dart::_getNetworkClockScreenSavers`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
