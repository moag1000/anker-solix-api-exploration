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
| `img_url` | string | yes |  | `charging/http/http_request_repository_impl.dart @0x3e19d28` (parameter, not typed by the builder) |
| `hash_code` | string | yes |  | `charging/http/http_request_repository_impl.dart @0x3e19d3c` (parameter, not typed by the builder) |

Caller values (traced 2026-10-20, app side): `A2345CustomClockLogic::handleEditedImage` (`charging/ui/page/device/a2345/a2345custom_clock/a2345custom_clock_logic.dart @0x3e38100`, parameters: the URL returned by the cloud upload and the local image path) logs both (`上传返回的图片URL: `, `本地图片路径: `), requires both texts to be non-empty (length fields `field_7`, `cbz`/`cbnz` `@0x3e381cc`..`@0x3e381dc`; otherwise it shows the text `uploadToTheCloudFailed`, `@0x3e381f8`), computes `calculateFileCRC32` for the local file (`@0x3e38218`, awaited, cast to `String` `@0x3e38254`..`@0x3e38260`) and calls the sender with the URL as `img_url`, the CRC-32 text as `hash_code` and `field_6b` of the selected device object as `sn` (`@0x3e38384`, call `@0x3e383cc`). So `img_url` is the cloud-storage URL of the uploaded image (see [get_app_up_token_general](../../../app/cloudstor/get_app_up_token_general.md)) and `hash_code` is the CRC-32 checksum of the image file as a String, not a cryptographic hash. The other caller (`a2345clock_style_logic.dart @0x3e19b18`) has the same shape, not decoded further.

## `param_type`/`cmd`

n/a

## Response model (link)

Not read: the sender's success closure `charging/http/http_request_repository_impl.dart @0x2268374` forwards its argument to the stored callback unread (`ClosureCall` `@0x22683a8`); the callers' success callbacks (`addCustomClockScreenSavers` in `a2345clock_style_logic.dart` and `a2345custom_clock_logic.dart`) were not decoded.

## Response

No response key is confirmed read (see Response model).

What the caller reads (traced 2026-10-20, app side): the success closure of `A2345CustomClockLogic::handleEditedImage` (`a2345custom_clock_logic.dart @0x3e384a0`) logs the answer (`服务器返回数据: `, `@0x3e384f0`), tests that it is a `Map` (`@0x3e38568`), reads the key `id` (`@0x3e38590`), converts it to text (`@0x3e385d0`) and passes it to `_appendNewThemeByFetch` (`@0x3e385f8`), sets a flag in the logic (`field_ab` `@0x3e3860c`) and posts an event on the event bus with `action: add` and the device serial number (`@0x3e38654`..`@0x3e3868c`); the failure closure (`@0x3e383e8`) logs `添加自定义屏保失败: ` (`@0x3e38428`) and shows `uploadToTheCloudFailed` (`@0x3e38468`).

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
- Header stays `string-only` because the field types and the response handling are missing. — rechecked 2026-10-20: still true; the typing attempts are recorded on the bullets of this section
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
