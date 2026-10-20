> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_url

## Purpose

Resolves a short URL of a clock screensaver image into the real image URL (callers `_getRealUrl` in the small-charging-platform clock-style logic and clock-style manage logic) (asm-traced for the caller chain in `data/endpoints.json`; the resolving is inferred from the key `short_url` and the function name `getA2345CustomClockScreenSaversRealUrl`, string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /mini_power/v1/app/style/get_url` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x26c8bac`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x26c8ba4`, in `HttpRequestControllerImpl::getA2345CustomClockScreenSaversRealUrl` (`charging/http/http_request_repository_impl.dart @0x26c8af0`), sent through `requestHttp` (`@0x26c8bd4`).

## Encrypted?

encrypted: `true` (asm-traced). `HttpRequestControllerImpl::requestHttp` declares `needEncryption = true` as its default (`charging/http/http_request_repository_impl.dart @0x2264944`) and this sender's argument descriptor names only `fail` and `showLoading` (`@0x26c8bcc`), so the default applies; the request then takes the decorator path described in `api/encryption.md`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced for the store, `?` where the value is not typed) `HttpRequestControllerImpl::getA2345CustomClockScreenSaversRealUrl` (`charging/http/http_request_repository_impl.dart @0x26c8af0`) stores one key, `short_url`, unconditionally in a map literal with type arguments `<String, dynamic>` (`@0x26c8b64`), which does not type the value; it comes from a parameter.

| field | type | required | example | source |
|---|---|---|---|---|
| `short_url` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x26c8b50` (parameter, not typed by the builder) |

## `param_type`/`cmd`

n/a

## Response model (link)

Not read: the sender's success closure `charging/http/http_request_repository_impl.dart @0x2268374` forwards its argument to the stored callback unread (`ClosureCall` `@0x22683a8`); the two callers' success callbacks (`_getRealUrl` in `clock_style_logic.dart` and `clock_style_manage_logic.dart`) were not decoded, so no key is confirmed.

## Response

No response key is confirmed read (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "short_url": "<?>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. The failure closure `charging/http/http_request_repository_impl.dart @0x26c8be8` logs the code and message (`exeError`) and passes both on to the stored callback unread. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getA2345CustomClockScreenSaversRealUrl` @0x26c8af0 (requestHttp; encrypted: true, `needEncryption` default)

Called from:

- `small_charging_platform/src/screen_setting/clock_style/custom_screensaver/page/clock_style_manage_logic.dart::_getRealUrl`
- `small_charging_platform/src/screen_setting/clock_style/page/clock_style_logic.dart::_getRealUrl`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `short_url`: a parameter stored into a `<String, dynamic>` literal; the callers' argument type was not read.
- The response shape (which key holds the real URL): the callers' callbacks were not decoded.
- Header stays `string-only` because the type of `short_url` and the response model are missing.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
