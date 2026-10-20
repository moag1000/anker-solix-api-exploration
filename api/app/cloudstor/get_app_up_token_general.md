> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_app_up_token_general

## Purpose

Obtains an upload token for a file the logged-in user uploads (app log, BLE log, feedback attachment, cropped image, bill-analysis file); senders: `UploadLogLogic::requestUpToken`, `DeviceLogsLogic::_uploadBleFile`, `BillAnalysisUploadService::_getUploadToken` and, for the crop and feedback screens, `HttpRequestControllerImpl::getAppUpTokenGeneral` (asm-traced, caller chain in `data/endpoints.json`). The login-state variant is `get_app_up_token_without_login`.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/cloudstor/get_app_up_token_general` (asm-traced), same URL and method object `Method.post` (pool entry `pp+0xa7e0`) in these senders:

- `BillAnalysisUploadService::_getUploadToken` (`anka_agent/services/bill_analysis_upload_service.dart @0x2bf3c84`): URL `@0x2bf3f58`, method object `@0x2bf3f50`, sent through `encryptionRequestHttpByGHttpRequest` (`@0x2bf3f88`).
- `DeviceLogsLogic::_uploadBleFile` (`charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x31334c8`): URL `@0x313367c`, method object `@0x3133674`, sent through `encryptionRequestHttp` (`@0x31336a0`).
- `UploadLogLogic::requestUpToken` (`charging/ui/page/user/upload_log/upload_log_logic.dart @0x46b06d0`): URL `@0x46b0ad8`, method object `@0x46b0ad0`, sent through `encryptionRequestHttp` (`@0x46b0afc`).
- `HttpRequestControllerImpl::getAppUpTokenGeneral` (`charging/http/http_request_repository_impl.dart @0x2d90ae4`): the URL is a parameter chosen by the callers (`custom_crop_controller.dart @0x2d90880`, `feedback_logic.dart @0x312097c`, `@0x3121440`, `crop_logic.dart @0x33138c0`); method object `@0x2d90c5c`, sent through `encryptionRequestHttp` (`@0x2d90c90`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Union over the senders. The body map has type arguments `<String, Object>` in two senders (`charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133630`, `anka_agent/services/bill_analysis_upload_service.dart @0x2bf3ed0`) and `<String, dynamic>` in `getAppUpTokenGeneral` (`charging/http/http_request_repository_impl.dart @0x2d90c1c`); neither is evidence of a value type.

| field | type | required | example | source |
|---|---|---|---|---|
| `file_name` | ? | yes | `"app_log_upload.log"` (constant in `UploadLogLogic::requestUpToken`; a parameter or field elsewhere) | `anka_agent/services/bill_analysis_upload_service.dart @0x2bf3e34` (value store `@0x2bf3e44`) |
| `content_type` | string | yes | `"binary/octet-stream"` (constant in three senders) | `anka_agent/services/bill_analysis_upload_service.dart @0x2bf3e48` (constant `@0x2bf3e5c`) |
| `file_size` | int (unboxed, x) | yes | ? | `anka_agent/services/bill_analysis_upload_service.dart @0x2bf3e60` (value boxed by `BoxInt64Instr` `@0x2bf3e70`; the same boxing in `charging/http/http_request_repository_impl.dart @0x2d90bb8`; the BLE and app-log senders were not decoded for it) |
| `disable_ssl` | bool | yes | `false` | `anka_agent/services/bill_analysis_upload_service.dart @0x2bf3eac` (constant `@0x2bf3eb8`) |
| `type` | int (Smi, w) | yes | `50` in the bill-analysis sender (raw 100 `@0x2bf3ec8`), `7` in the BLE-log and app-log senders (raw 14, `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133608`, `charging/ui/page/user/upload_log/upload_log_logic.dart @0x46b0a60`) | `anka_agent/services/bill_analysis_upload_service.dart @0x2bf3ec0` (value store `@0x2bf3ecc`); in `getAppUpTokenGeneral` the value is a parameter tagged by `lsl` (`charging/http/http_request_repository_impl.dart @0x2d90c14`) |

The bill-analysis sender also sends a header `user_id` (a `<String, String>` map `@0x2bf3dac` built only when the stored user id is not empty, `cbz` `@0x2bf3d88`); it is a header, not a body field.

In the feedback screen the `type` argument next to the URL is the raw 6 (logged-in branch, `charging/ui/page/user/feedback/feedback_logic.dart @0x312097c`..`@0x3120984`) or 7 (other branch, `@0x3120994`); because `getAppUpTokenGeneral` tags its `type` from an unboxed int, I read these as 6 and 7 (my reading, the register was not followed to the call).

Senders that derive the file values (traced 2026-10-20): `FeedbackLogic::upLoadSingleFile` (`charging/ui/page/user/feedback/feedback_logic.dart @0x31211e0`) takes the file name as the last element of the file path cut at `"/"` (`@0x31213d4`..`@0x31213e8`, `last` list getter), so a String, and the size from an awaited `length()` of the file (`@0x31213fc`..`@0x3121414`, `LoadInt32Instr` `@0x3121470`), so an integer; it passes `5` of `6` or `7` as `type` (`@0x3121448`, `@0x3121458`, raw 6 and 7 are the values given above) and the URL literal of the with-login or without-login call. `UploadLogLogic::requestUpToken` sends the constant `"app_log_upload.log"`. The BLE-log sender `_uploadBleFile` (`charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x31334c8`) reads `file_name` from a parameter slot (`field_13` of its context, `@0x3133598`..`@0x31335a8`) and `file_size` from a field of a file object (`@0x31335b4`..`@0x31335c8`); neither slot has a declared type in the asm.

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::GetUpToken` (`data/models.json`, no page under `models/`), parsed by `GetUpToken.fromJson` at `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x3133768` (closure `@0x3133710`) and at `charging/ui/page/user/upload_log/upload_log_logic.dart @0x46b5ae0` (closure `@0x46b5aa8`). `getAppUpTokenGeneral` forwards the response value to its caller unparsed (`charging/http/http_request_repository_impl.dart @0x2268374`, `ClosureCall` `@0x22683a8`); the bill-analysis sender returns a `Map<String, dynamic>?` (`anka_agent/services/bill_analysis_upload_service.dart @0x2bf3cac`) and its parse was not read.

What the callers read (traced 2026-10-20, app side): the bill-analysis flow `BillAnalysisUploadService::uploadFile` (`anka_agent/services/bill_analysis_upload_service.dart @0x2bf2e84`) awaits `_getUploadToken` (`@0x2bf2f48`), then reads the keys `uptoken` (`@0x2bf2f7c`, again `@0x2bf30f0`, cast to String) and `key_prefix` (`@0x2bf2fa8`) of the returned map and calls `_putToS3` (`@0x2bf307c`), which turns the text into a URI and opens an HTTP PUT with the file bytes (`parse` `@0x2bf3514`, `putUrl` `@0x2bf3520`, content type and length set `@0x2bf3554`, `@0x2bf3560`); on success it logs the `keyPrefix` and an `accessUrl`. The feedback closures (`feedback_logic.dart @0x3120c90`, `@0x3120d08`, `@0x31215f4`, `@0x312166c`) and the crop closure (`charging/ui/page/device/a2345/a2345_media_ability/custom_crop_controller.dart @0x2d90dd0`, `@0x2d90e44`) read the same two keys `uptoken` and `key_prefix`. The role of `uptoken` in the three flows is the same text (app side: the bill-analysis flow uses it as the target of the PUT).

## Response

Top-level keys of `GetUpToken` (`data/models.json`, `charging::GetUpToken`): `uptoken` (String?), `key_prefix` (String?). The two keys are the upload credential and the object key prefix by name only (string-only for the meaning).

## Example request/response

Request, synthesized (decrypted body as built by `BillAnalysisUploadService::_getUploadToken`; `<...>` are placeholders, not captured values)

```json
{
  "file_name": "<file_name>",
  "content_type": "binary/octet-stream",
  "file_size": "<int>",
  "disable_ssl": false,
  "type": 50
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

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

3.18.0: present. 3.24.3: present. since: <=3.18.0. Parameter delta in `tools/out/diff_3.18.0_3.24.3.md`: added `user_id` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `file_name` in the senders that pass a parameter or field, and of `file_size` in the BLE-log and app-log senders (`file_size` is `LoadField`/`LoadInt32Instr`-derived there, not decoded). — attempted 2026-10-20 (two-hop not readable for the BLE-log, crop and bill-analysis senders: `_uploadBleFile` `device_logs_logic.dart @0x3133598`, `@0x31335b4`; the feedback sender is typed under Request)
- Which `type` values mean which upload kind (7 for logs, 50 for bill analysis, 6 and 7 from the feedback screen): the server's table is not visible.
- What the credential is used for (the upload target, expiry): not read here. — reclassified: server (2026-10-20: the app does not show the upload target or its expiry; they are not derivable here)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
