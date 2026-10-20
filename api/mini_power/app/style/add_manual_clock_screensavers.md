> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# add_manual_clock_screensavers

## Purpose

Registers a user-made clock screensaver image for an A2345 charger after the image was uploaded (callers `addCustomClockScreenSavers` in the A2345 clock-style logic and the A2345 custom-clock logic) (asm-traced for the caller chain in `data/endpoints.json`; the upload step is inferred from the key names `img_url` and `hash_code`, string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /mini_power/v1/app/style/add_manual_clock_screensavers` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3e19d98`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3e19d90`, in `HttpRequestControllerImpl::addA2345CustomClockScreenSavers` (`charging/http/http_request_repository_impl.dart @0x3e19ca0`), sent through `requestHttp` (`@0x3e19dc0`).

## Encrypted?

encrypted: `true` (asm-traced). `HttpRequestControllerImpl::requestHttp` declares `needEncryption = true` as its default (`charging/http/http_request_repository_impl.dart @0x2264944`) and this sender's argument descriptor names only `fail` and `showLoading` (`@0x3e19db8`), so the default applies; the request then takes the decorator path described in `api/encryption.md`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced for the stores, `?` where the value is not typed) `HttpRequestControllerImpl::addA2345CustomClockScreenSavers` (`charging/http/http_request_repository_impl.dart @0x3e19ca0`) stores three keys unconditionally in a map literal with type arguments `<String, dynamic>` (`@0x3e19d50`), which types no value; all three come from parameters.

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3e19d14` (parameter, not typed by the builder) |
| `img_url` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3e19d28` (parameter, not typed by the builder) |
| `hash_code` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3e19d3c` (parameter, not typed by the builder) |

## `param_type`/`cmd`

n/a

## Response model (link)

Not read: the sender's success closure `charging/http/http_request_repository_impl.dart @0x2268374` forwards its argument to the stored callback unread (`ClosureCall` `@0x22683a8`); the callers' success callbacks (`addCustomClockScreenSavers` in `a2345clock_style_logic.dart` and `a2345custom_clock_logic.dart`) were not decoded.

## Response

No response key is confirmed read (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "sn": "<?>",
  "img_url": "<?>",
  "hash_code": "<?>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. The failure closure `charging/http/http_request_repository_impl.dart @0x3e19dd4` logs the code and message (`exeError`) and passes both on to the stored callback unread. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `addA2345CustomClockScreenSavers` @0x3e19ca0 (requestHttp; encrypted: true, `needEncryption` default)

Called from:

- `charging/http/http_request_repository.dart::addA2345CustomClockScreenSavers`
- `charging/ui/page/device/a2345/a2345clock_style/a2345clock_style_logic.dart::addCustomClockScreenSavers`
- `charging/ui/page/device/a2345/a2345custom_clock/a2345custom_clock_logic.dart::addCustomClockScreenSavers`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `sn`, `img_url` and `hash_code`: parameters stored into a `<String, dynamic>` literal; the callers' argument types were not read. — attempted 2026-10-20 (two-hop not readable: both callers `addCustomClockScreenSavers` pass slots of their own frames, `charging/ui/page/device/a2345/a2345custom_clock/a2345custom_clock_logic.dart @0x3e383bc`..`@0x3e383cc` and `charging/ui/page/device/a2345/a2345clock_style/a2345clock_style_logic.dart @0x3e19bdc`..`@0x3e19bec`)
- Which hash `hash_code` is (algorithm and input) and how `img_url` is obtained: the callers were not decoded.
- Whether and how the answer is used: the callers' success callbacks were not read.
- Header stays `string-only` because the field types and the response handling are missing. — rechecked 2026-10-20: still true; the typing attempts are recorded on the bullets of this section
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
