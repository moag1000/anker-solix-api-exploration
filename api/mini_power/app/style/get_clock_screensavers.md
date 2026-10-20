> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_clock_screensavers

## Purpose

Loads the network clock and screensaver theme categories offered for a charger model (callers: the A2345 clock-style and clock-display logic `getCategoryClockScreenSavers`, the A1782 screen-theme logic and the A25x7 screensaver logic `_updateNetworkThemeList` / `_updateNetworkThemeCategory`, and the small-charging-platform clock-style logic `_getNetworkClockScreenSavers`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`charger_get_screensavers` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /mini_power/v1/app/style/get_clock_screensavers` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x28ade0c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x28ade04`, in `HttpRequestControllerImpl::getA2345ClockScreenSavers` (`charging/http/http_request_repository_impl.dart @0x28add4c`), sent through `requestHttp` (`@0x28ade34`).

Same URL and method object in the other sender(s) read:

- `POST /mini_power/v1/app/style/get_clock_screensavers` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x29deaac`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x29deaa4`, in `HttpRequestControllerImpl::getScreenSaversByCategory` (`charging/http/http_request_repository_impl.dart @0x29de9f4`), sent through `encryptionRequestHttp` (`@0x29dead4`).

## Encrypted?

encrypted: `true` (asm-traced) for both senders. `getA2345ClockScreenSavers` calls `HttpRequestControllerImpl::requestHttp`, whose default `needEncryption = true` (`charging/http/http_request_repository_impl.dart @0x2264944`) applies because the argument descriptor names only `fail` and `showLoading` (`@0x28ade2c`); `getScreenSaversByCategory` calls `encryptionRequestHttp` (`@0x29dead4`), which forwards with `needEncryption` defaulting to true (`api/encryption.md`). Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) Two senders store one key, `product_code`, unconditionally. `HttpRequestControllerImpl::getScreenSaversByCategory` (`charging/http/http_request_repository_impl.dart @0x29de9f4`) uses a map literal with type arguments `<String, String>` (`@0x29dea60`, key `@0x29dea4c`), so the value is a String. `HttpRequestControllerImpl::getA2345ClockScreenSavers` (`charging/http/http_request_repository_impl.dart @0x28add4c`, key `@0x28addb0`) uses `<String, dynamic>` (`@0x28addc4`), which does not type the value on its own.

| field | type | required | example | source |
|---|---|---|---|---|
| `product_code` | string | yes | `"<product_code>"` | `charging/http/http_request_repository_impl.dart @0x28addb0` (map literal `<String, String>` in the second sender, `charging/http/http_request_repository_impl.dart @0x29dea60`; the first sender stores it in a `<String, dynamic>` literal `@0x28addc4`) |

## `param_type`/`cmd`

n/a

## Response model (link)

- `charging::CategoryClockThemeContainer` and `charging::ScreenSaverThemeCategoryList` (`data/models.json`; no page under `models/`), parsed by the callers (see Response). Neither sender parses the response itself.

## Response

Both senders hand the response to the caller's callback unread (`charging/http/http_request_repository_impl.dart @0x2268374` forwards its argument, `ClosureCall` `@0x22683a8`). The callers parse it:

- `charging::CategoryClockThemeContainer` (`data/models.json`), parsed by `CategoryClockThemeContainer.fromJson` in the success callbacks of the first sender's callers: `charging/ui/page/device/a2345/a2345clock_style/a2345clock_style_logic.dart` (`getCategoryClockScreenSavers` `@0x28adc34`, call `@0x28adca8`, callback closure `@0x28ae1ec`, `fromJson` `@0x28ae264`) and `charging/ui/page/device/a2345/a2345clock_display/a2345clock_display_logic.dart` (`getCategoryClockScreenSavers` `@0x28d75f8`, call `@0x28d7678`, callback closure `@0x28d7978`, `fromJson` `@0x28d79cc`).
- `charging::ScreenSaverThemeCategoryList` (`data/models.json`), parsed by `ScreenSaverThemeCategoryList.fromJson` in the success callbacks of the second sender's callers: `charging/ui/page/device/a1782/screen_saver/screen_theme_setting/screen_theme_setting_logic.dart` (`_updateNetworkThemeList` `@0x29de820`, call `@0x29de9c8`, callback closure `@0x29df740`, `fromJson` `@0x29df804`), `charging/ui/page/device/a25x7/a25x7screensaver_style/a25x7screensaver_style_logic.dart` (`_updateNetworkThemeCategory` `@0x29e105c`, call `@0x29e1138`, callback closure `@0x29e06b0`, `fromJson` `@0x29e06f8`) and `charging/ui/page/device/a25x7/a25x7screensaver/a25x7screensaver_logic.dart` (`_updateNetworkThemeList` `@0x353b0a4`, call `@0x353b180`, callback closure `@0x353b5c8`, `fromJson` `@0x353b5f8`).
- No model class in the sixth caller: `small_charging_platform/src/screen_setting/clock_style/page/clock_style_logic.dart` (`_getNetworkClockScreenSavers` `@0x2a79850`, call `@0x2a7993c` of the first sender, callback closure `@0x2a79dc8`) reads the key `category` (`@0x2a79df4`) and maps it with `_mapNetworkCategory` (`@0x2a79fe4`).

Top-level keys (`data/models.json`): `charging::CategoryClockThemeContainer` has `category` (field type not extracted); `charging::ScreenSaverThemeCategoryList` has `category` (`List?`).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "product_code": "<product_code>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the senders or the closures read for this page. The first sender's failure closure (`charging/http/http_request_repository_impl.dart @0x28ade48`) logs code and message (`exeError`) and passes both on unread; the second sender's failure closure is `@0x226824c` (forwards both arguments). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getA2345ClockScreenSavers` @0x28add4c (requestHttp; encrypted: true, `needEncryption` default); `getScreenSaversByCategory` @0x29de9f4 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getA2345ClockScreenSavers`
- `charging/ui/page/device/a1782/screen_saver/screen_theme_setting/screen_theme_setting_logic.dart::_updateNetworkThemeList`
- `charging/ui/page/device/a2345/a2345clock_display/a2345clock_display_logic.dart::getCategoryClockScreenSavers`
- `charging/ui/page/device/a2345/a2345clock_style/a2345clock_style_logic.dart::getCategoryClockScreenSavers`
- `charging/ui/page/device/a25x7/a25x7screensaver/a25x7screensaver_logic.dart::_updateNetworkThemeList`
- `charging/ui/page/device/a25x7/a25x7screensaver_style/a25x7screensaver_style_logic.dart::_updateNetworkThemeCategory`
- `small_charging_platform/src/screen_setting/clock_style/page/clock_style_logic.dart::_getNetworkClockScreenSavers`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `product_code` in the first sender: its `<String, dynamic>` literal does not type it; the String type is proven only by the second sender's `<String, String>` literal, and the callers' argument types were not read.
- Which `product_code` values the callers pass (device model codes); the callers were not decoded for it.
- The element shape of `category`: the field type is `unknown` for `CategoryClockThemeContainer` in `data/models.json`; the models were not read for this page.
- Why two models exist for one URL (different device families call different senders); the server answer for the two families was not compared.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
