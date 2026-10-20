> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# nps

## Purpose

Loads the NPS survey banners shown on the discover page and the device home; sent by `UserDiscoverLogic::getNpsBannerData` and `DeviceMainLogic::getNpsBannerData` (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/help/banner/nps` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x22a7c18`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x22a7c10`, in `HttpRequestControllerImpl::getNpsSurveyList` (`charging/http/http_request_repository_impl.dart @0x22a7b88`), sent through `encryptionRequestHttp` (`@0x22a7c40`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No body field: the sender builds an empty map literal (`Map._fromLiteral` `charging/http/http_request_repository_impl.dart @0x22a7bd8`, no key store before it).

## `param_type`/`cmd`

n/a

## Response model (link)

no top-level model: the success closure (`charging/http/http_request_repository_impl.dart @0x22a7c5c`, argument typed `Map<String, dynamic>`) reads the key `banners` (`@0x22a7cac`, lookup `@0x22a7cb4`) as `List?` (`@0x22a7cec`) and parses each element with [`BannerModel`](../../../../models/other.md#bannermodel).fromJson (`@0x22a7e1c`, call target `#0x22a7ee8`, `charging/model/banner_model.dart`); a missing list is logged as `get nps survey response data is null` (`@0x22a7d44`) and the callback gets an empty result. The callback receives the list of `BannerModel` (`ClosureCall` `@0x22a7ebc`).

## Response

(asm-traced) One key is read from the top level of the response: `banners` (list). Keys of `charging::BannerModel` (`data/models.json`): `img_url` (String?), `content` (String?), `banner_id` (int?), `category` (int?), `img_url_home` (String?), `img_url_device` (String?).

## Example request/response

Request: no body fields are built (see Request). Response: not synthesized; no capture exists for this endpoint.

## Errors seen

none traced: no numeric error code is compared in the sender, its closures or the caller functions read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getNpsSurveyList` @0x22a7b88 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getNpsSurveyList`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::getNpsBannerData`
- `charging/ui/page/user/discover/user_discover_logic.dart::getNpsBannerData`

Answer path (app side, traced 2026-10-20): the survey popup is answered through `DeviceMainLogic::bannerClick`, which calls `handleSurveyPopup` with `handle_type` 1 directly and 2 in a dialog closure; the values and addresses are on [../handle_survey_popup.md](../handle_survey_popup.md#request).

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What distinguishes an NPS banner from the `banners` of the sibling endpoint `banners` (the same model is parsed): the server selects by URL; the model has `category` and `banner_id` but their values were not read.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
