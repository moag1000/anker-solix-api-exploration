> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_app_up_token_without_login

## Purpose

Obtains an upload token when no user is logged in (feedback attachments, cropped images); the callers choose this URL instead of `get_app_up_token_general` and pass it to `HttpRequestControllerImpl::getAppUpTokenGeneral` (asm-traced for the call sites, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/cloudstor/get_app_up_token_without_login` (asm-traced for the sender): the URL literal is loaded by four call sites and passed as the URL parameter of `HttpRequestControllerImpl::getAppUpTokenGeneral` (`charging/http/http_request_repository_impl.dart @0x2d90ae4`), which uses the method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2d90c5c` and sends through `encryptionRequestHttp` (`@0x2d90c90`). The call sites:

- `CustomCropController::uploadCroppedImage` (`charging/ui/page/device/a2345/a2345_media_ability/custom_crop_controller.dart @0x2d9088c`): chosen when the header map has no key `user_id` (`containsKey` `@0x2d90878`, branch `@0x2d9087c`), else `get_app_up_token_general`.
- `FeedbackLogic` (`charging/ui/page/user/feedback/feedback_logic.dart @0x312098c`, `@0x3121450`): chosen when a state flag is false (`tbnz` `@0x3120978`).
- `CropLogic::_uploadCroppedImage` (`small_charging_platform/src/screen_setting/clock_style/custom_screensaver/page/crop_logic.dart @0x33138cc`).

## Encrypted?

encrypted: `true` for the sender `getAppUpTokenGeneral` (`encryptionRequestHttp`, `charging/http/http_request_repository_impl.dart @0x2d90c90`); scheme and header rules: `api/encryption.md`. The inventory flag "unknown" came from the URL literal sitting in callers that make no `*Http*` call themselves.

## Request

The body is built by `getAppUpTokenGeneral` (`charging/http/http_request_repository_impl.dart @0x2d90ae4`, map literal `<String, dynamic>` `@0x2d90c1c`, not evidence of a value type):

| field | type | required | example | source |
|---|---|---|---|---|
| `file_name` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x2d90b7c` (value from a parameter, `@0x2d90b8c`) |
| `content_type` | string | yes | `"binary/octet-stream"` | `charging/http/http_request_repository_impl.dart @0x2d90b90` (constant `@0x2d90ba4`) |
| `file_size` | int (unboxed, x) | yes | ? | `charging/http/http_request_repository_impl.dart @0x2d90ba8` (value boxed by `BoxInt64Instr` `@0x2d90bb8`) |
| `disable_ssl` | bool | yes | `false` | `charging/http/http_request_repository_impl.dart @0x2d90bf4` (constant `@0x2d90c04`) |
| `type` | int (Smi, w) | yes | ? | `charging/http/http_request_repository_impl.dart @0x2d90c08` (value from an unboxed int parameter, tagged by `lsl` `@0x2d90c14`, stored `@0x2d90c18`) |

The sender also passes a `header` map (named argument `charging/http/http_request_repository_impl.dart @0x2d90c88`) built by the callers (for example `CustomCropController` in `charging/ui/page/device/a2345/a2345_media_ability/custom_crop_controller.dart` builds one with the keys `teminal_id`, `@0x2d90858`, and `user_id`, `@0x2d90870`), not a body field.

## `param_type`/`cmd`

n/a

## Response model (link)

not resolved (string-only): the success closure of `getAppUpTokenGeneral` (`charging/http/http_request_repository_impl.dart @0x2268374`) forwards the response value to the caller's callback (`ClosureCall` `@0x22683a8`) without a `fromJson`; the four callers' own parse was not read. The sibling endpoint `get_app_up_token_general` parses `charging::GetUpToken` (keys `uptoken`, `key_prefix`) in two other senders.

## Response

Not listed: the callers' parse of the value was not read (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by `getAppUpTokenGeneral`; `<...>` are placeholders, not captured values)

```json
{
  "file_name": "<file_name>",
  "content_type": "binary/octet-stream",
  "file_size": "<int>",
  "disable_ssl": false,
  "type": "<int>"
}
```

Response: not synthesized; no capture exists for this endpoint.

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a2345/a2345_media_ability/custom_crop_controller.dart`: `uploadCroppedImage` @0x2d90620 (URL literal only, no `*Http*` call; sender `HttpRequestControllerImpl::getAppUpTokenGeneral` (`charging/http/http_request_repository_impl.dart @0x2d90ae4`), a callee called after the URL load in the same function; resolved from the URL literal at `charging/ui/page/device/a2345/a2345_media_ability/custom_crop_controller.dart @0x2d9088c` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `charging/ui/page/user/feedback/feedback_logic.dart`: `<anonymous closure> in FeedbackLogic::clickSubmit` @0x31208a4 (URL literal only, no `*Http*` call; no sender within 3 caller levels); `upLoadSingleFile` @0x31211e0 (URL literal only, no `*Http*` call; sender `HttpRequestControllerImpl::getAppUpTokenGeneral` (`charging/http/http_request_repository_impl.dart @0x2d90ae4`), a callee called after the URL load in the same function; resolved from the URL literal at `charging/ui/page/user/feedback/feedback_logic.dart @0x3121450` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `small_charging_platform/src/screen_setting/clock_style/custom_screensaver/page/crop_logic.dart`: `_uploadCroppedImage` @0x3313658 (URL literal only, no `*Http*` call; caller walk reaches a deduplicated mixin function absent from the dump (UNCONFIRMED))

Called from:

- `charging/ui/page/device/a2345/a2345_media_ability/custom_crop_widget.dart::_cropImage`
- `charging/ui/page/user/feedback/feedback_logic.dart::clickSubmit`
- `charging/ui/page/user/feedback/feedback_logic.dart::upLoadSingleFile`
- `small_charging_platform/src/screen_setting/clock_style/custom_screensaver/page/crop_logic.dart::_retryUpload`
- `small_charging_platform/src/screen_setting/clock_style/custom_screensaver/page/crop_logic.dart::cropImage`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The response keys for this variant: the sender forwards the value and the callers' parse was not read; the sibling endpoint returns `uptoken` and `key_prefix`.
- Type of `file_name` and the values of `type` per call site (the feedback screen loads raw 6 and 7 next to the URL, `charging/ui/page/user/feedback/feedback_logic.dart @0x312097c`, `@0x3120994`).
- Whether the server accepts this URL with an `Openudid`/terminal id header only (the callers add `teminal_id`): the headers are built per caller.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
