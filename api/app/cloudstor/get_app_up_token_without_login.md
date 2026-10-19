> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_app_up_token_without_login

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/app/cloudstor/get_app_up_token_without_login`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a2345/a2345_media_ability/custom_crop_controller.dart @0x2d9088c`
(literal also at 3 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "unknown (URL literal only, no `*Http*` call)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `File not exists: ` | ? | ? | ? | `charging/ui/page/device/a2345/a2345_media_ability/custom_crop_controller.dart @0x2d90620` |

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

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
