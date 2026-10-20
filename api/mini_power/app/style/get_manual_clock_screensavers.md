> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_manual_clock_screensavers

## Purpose

Loads the user-made clock screensavers of an A2345 charger for the clock-display, clock-style and custom-clock pages (callers `_loadCustomScreensavers`, `_refreshCustomScreensaversData`, `_refreshCustomThemeUrl`, `_refreshCustomCategoryData`, `getCustomClockScreenSavers`, `initCustomizeCategoryThemeData`, `_appendNewThemeByFetch` and `getA2345CustomClockScreenSaversData`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /mini_power/v1/app/style/get_manual_clock_screensavers` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x276bba0`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x276bb98`, in `HttpRequestControllerImpl::getA2345CustomClockScreenSavers` (`charging/http/http_request_repository_impl.dart @0x276bae4`), sent through `requestHttp` (`@0x276bbc8`).

## Encrypted?

encrypted: `true` (asm-traced). `HttpRequestControllerImpl::requestHttp` declares `needEncryption = true` as its default (`charging/http/http_request_repository_impl.dart @0x2264944`) and this sender's argument descriptor names only `fail` and `showLoading` (`@0x276bbc0`), so the default applies; the request then takes the decorator path described in `api/encryption.md`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced for the store, `?` where the value is not typed) `HttpRequestControllerImpl::getA2345CustomClockScreenSavers` (`charging/http/http_request_repository_impl.dart @0x276bae4`) stores one key, `sn`, unconditionally in a map literal with type arguments `<String, dynamic>` (`@0x276bb58`), which does not type the value; it comes from a parameter.

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x276bb44` (parameter, not typed by the builder) |

Value of `sn` (traced 2026-10-20, app side): `getA2345CustomClockScreenSaversData` passes `field_6b` of the value of an observable device holder (`field_b3`, `charging/ui/page/device/a2345/a2345custom_clock/a2345custom_clock_logic.dart @0x28b08d4`..`@0x28b08e0`), the same device serial getter as the `device_sn` of the other endpoints (see [add_manual_clock_screensavers](add_manual_clock_screensavers.md#request)); `sn` is therefore the device serial number, only the key name differs.

## `param_type`/`cmd`

n/a

## Response model (link)

Not read: the sender's success closure `charging/http/http_request_repository_impl.dart @0x2268374` forwards its argument to the stored callback unread (`ClosureCall` `@0x22683a8`); the callers' success callbacks (eight callers in the A2345 clock-display, clock-style and custom-clock logic classes) were not decoded, so no model or key is confirmed.

## Response

No response key is confirmed read (see Response model).

Parse by one caller (traced 2026-10-20, app side): the success closure of `A2345CustomClockLogic::getA2345CustomClockScreenSaversData` (`charging/ui/page/device/a2345/a2345custom_clock/a2345custom_clock_logic.dart @0x28b09d0`, sender call `@0x28b0920`) logs the answer (`返回数据: `, `@0x28b0a14`), reads the key `list` (`@0x28b0a40`, checked as `List`, `@0x28b0b08`) and for each element (checked as `Map<String, dynamic>`, `@0x28b0c00`) the keys `name` (`@0x28b0c40`), `id` (`@0x28b0d48`, turned into text), `img_url` (`String?`, `@0x28b0dc0`..`@0x28b0e18`), `short_url` (`String?`, `@0x28b0e38`..`@0x28b0e90`) and `hash_code` (`String`, `@0x28b0eac`..`@0x28b0f00`); it logs `获取到 … 个自定义屏保` ("got N custom screen savers", my translation, `@0x28b1118`). The other seven callers were not decoded; the keys above are the ones this caller reads.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "sn": "<?>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. The failure closure `charging/http/http_request_repository_impl.dart @0x276bbdc` logs the code and message (`exeError`) and passes both on to the stored callback unread. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getA2345CustomClockScreenSavers` @0x276bae4 (requestHttp; encrypted: true, `needEncryption` default)

Called from:

- `charging/http/http_request_repository.dart::getA2345CustomClockScreenSavers`
- `charging/ui/page/device/a2345/a2345clock_display/a2345clock_display_logic.dart::_loadCustomScreensavers`
- `charging/ui/page/device/a2345/a2345clock_display/a2345clock_display_logic.dart::_refreshCustomScreensaversData`
- `charging/ui/page/device/a2345/a2345clock_display/a2345clock_display_logic.dart::_refreshCustomThemeUrl`
- `charging/ui/page/device/a2345/a2345clock_style/a2345clock_style_logic.dart::_refreshCustomCategoryData`
- `charging/ui/page/device/a2345/a2345clock_style/a2345clock_style_logic.dart::getCustomClockScreenSavers`
- `charging/ui/page/device/a2345/a2345clock_style/a2345clock_style_logic.dart::initCustomizeCategoryThemeData`
- `charging/ui/page/device/a2345/a2345custom_clock/a2345custom_clock_logic.dart::_appendNewThemeByFetch`
- `charging/ui/page/device/a2345/a2345custom_clock/a2345custom_clock_logic.dart::getA2345CustomClockScreenSaversData`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `sn`: a parameter stored into a `<String, dynamic>` literal; the callers' argument type was not read. — attempted 2026-10-20 (two-hop not readable: the five call sites pass a slot of the caller frame (`charging/ui/page/device/a2345/a2345custom_clock/a2345custom_clock_logic.dart @0x28b0918`, `@0x3e3879c`; `charging/ui/page/device/a2345/a2345clock_style/a2345clock_style_logic.dart @0x28ad6bc`, `@0x28ad724`))
- Header stays `string-only` because the type of `sn` and the response model are missing. — rechecked 2026-10-20: still true; the typing attempts are recorded on the bullets of this section
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
