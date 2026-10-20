> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# handle_survey_popup

## Purpose

Reports what the user did with a survey popup banner and asks whether another popup follows; sent by `DeviceMainLogic::bannerClick` (`charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/help/handle_survey_popup` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x4699934`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x469992c`, in `HttpRequestControllerImpl::handleSurveyPopup` (`charging/http/http_request_repository_impl.dart @0x4699864`), sent through `encryptionRequestHttp` (`@0x4699954`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `banner_id` | int (Smi, w) | yes | ? | `charging/http/http_request_repository_impl.dart @0x46998bc` (value store `@0x46998cc`) |
| `handle_type` | int (Smi, w) | yes | ? | `charging/http/http_request_repository_impl.dart @0x46998d0` (value store `@0x46998e4`) |

Both values are ints: the map literal has type arguments `<String, int?>` (`@0x46998e8`); `handle_type` is the tagged result of an unboxed int (`lsl` `@0x46998e0`), stored with a 32-bit store. `banner_id` is the 32-bit store of a parameter.

## `param_type`/`cmd`

n/a

## Response model (link)

no top-level model: the success closure (`charging/http/http_request_repository_impl.dart @0x4699970`, argument typed `Map<String, dynamic>`) reads the key `has_popup` (`@0x469999c`) as `bool?` (`@0x46999e4`), builds a `SurveyPopupModel` (`@0x46999f4`, constructed from the value, not parsed with `fromJson`) and passes it to the callback (`ClosureCall` `@0x4699a20`).

## Response

(asm-traced) One key is read from the top level of the response: `has_popup` (bool, nullable).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "banner_id": "<banner_id>",
  "handle_type": "<handle_type>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender, its closures or the caller functions read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `handleSurveyPopup` @0x4699864 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::handleSurveyPopup`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::bannerClick`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What `handle_type` values mean (shown, closed, answered): the caller's argument was not decoded.
- The fields of `SurveyPopupModel` and what the callback does with it: only the constructor call was read.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
