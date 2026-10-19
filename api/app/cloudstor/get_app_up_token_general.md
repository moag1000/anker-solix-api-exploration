> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_app_up_token_general

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/app/cloudstor/get_app_up_token_general`, method: not extracted by the inventory <!-- TODO -->; string-only: `anka_agent/services/bill_analysis_upload_service.dart @0x2bf3f58`
(literal also at 6 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `user_id` | ? | ? | ? | `anka_agent/services/bill_analysis_upload_service.dart @0x2bf3c84` |
| `file_name` | ? | ? | ? | `anka_agent/services/bill_analysis_upload_service.dart @0x2bf3c84` |
| `content_type` | ? | ? | ? | `anka_agent/services/bill_analysis_upload_service.dart @0x2bf3c84` |
| `file_size` | ? | ? | ? | `anka_agent/services/bill_analysis_upload_service.dart @0x2bf3c84` |
| `disable_ssl` | ? | ? | ? | `anka_agent/services/bill_analysis_upload_service.dart @0x2bf3c84` |
| `type` | ? | ? | ? | `anka_agent/services/bill_analysis_upload_service.dart @0x2bf3c84` |
| `File not exists: ` | ? | ? | ? | `charging/ui/page/device/a2345/a2345_media_ability/custom_crop_controller.dart @0x2d90620` |

Rows are the union over 4 senders; `source` is the first sender that sets the key.

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

- `anka_agent/services/bill_analysis_upload_service.dart`: `_getUploadToken` @0x2bf3c84 (encryptionRequestHttpByGHttpRequest; encrypted: true)
- `charging/ui/page/device/a2345/a2345_media_ability/custom_crop_controller.dart`: `uploadCroppedImage` @0x2d90620 (URL literal only, no `*Http*` call; sender `HttpRequestControllerImpl::getAppUpTokenGeneral` (`charging/http/http_request_repository_impl.dart @0x2d90ae4`), a callee called after the URL load in the same function; resolved from the URL literal at `charging/ui/page/device/a2345/a2345_media_ability/custom_crop_controller.dart @0x2d90880` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `charging/ui/page/user/feedback/feedback_logic.dart`: `<anonymous closure> in FeedbackLogic::clickSubmit` @0x31208a4 (URL literal only, no `*Http*` call; no sender within 3 caller levels); `upLoadSingleFile` @0x31211e0 (URL literal only, no `*Http*` call; sender `HttpRequestControllerImpl::getAppUpTokenGeneral` (`charging/http/http_request_repository_impl.dart @0x2d90ae4`), a callee called after the URL load in the same function; resolved from the URL literal at `charging/ui/page/user/feedback/feedback_logic.dart @0x3121440` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart`: `_uploadBleFile` @0x31334c8 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/user/upload_log/upload_log_logic.dart`: `requestUpToken` @0x46b06d0 (encryptionRequestHttp; encrypted: true)
- `small_charging_platform/src/screen_setting/clock_style/custom_screensaver/page/crop_logic.dart`: `_uploadCroppedImage` @0x3313658 (URL literal only, no `*Http*` call; caller walk reaches a deduplicated mixin function absent from the dump (UNCONFIRMED))

Called from:

- `anka_agent/services/bill_analysis_upload_service.dart::uploadFile`
- `charging/ui/page/device/a2345/a2345_media_ability/custom_crop_widget.dart::_cropImage`
- `charging/ui/page/user/feedback/feedback_logic.dart::clickSubmit`
- `charging/ui/page/user/feedback/feedback_logic.dart::upLoadSingleFile`
- `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart::_uploadByStyle`
- `charging/ui/page/user/upload_log/upload_log_logic.dart::uploadAppLog`
- `small_charging_platform/src/screen_setting/clock_style/custom_screensaver/page/crop_logic.dart::_retryUpload`
- `small_charging_platform/src/screen_setting/clock_style/custom_screensaver/page/crop_logic.dart::cropImage`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
