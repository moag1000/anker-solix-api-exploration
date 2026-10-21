> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# banners

## Purpose

Loads the promotional banners for the user's region; sent by `HttpRequestControllerImpl::getBanners` (no UI caller beyond the repository interface in the inventory) (asm-traced for the sender; the screen that shows them is not in the caller chain, string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/help/banners` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x2608b50`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2608b48`, in `HttpRequestControllerImpl::getBanners` (`charging/http/http_request_repository_impl.dart @0x2608a60`), sent through `encryptionRequestHttp` (`@0x2608b70`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `region` | string | yes | `"<region>"` | `charging/http/http_request_repository_impl.dart @0x2608ab4` (value store `@0x2608adc`) |

The value is a String or null: the map literal has type arguments `<String, String?>` (`@0x2608b00`); it is the field of the region object returned by `getCurrentRegion` (`@0x2608ac8`, field load `@0x2608acc`).

Content of `region` (traced 2026-10-20, app side): `getCurrentRegion` is `DeviceUtil::getCurrentRegion` (`charging/util/device_util.dart @0x224fb50`; call `charging/http/http_request_repository_impl.dart @0x2608ac8`), which returns a `CountryModel` taken from the cached app region (`getAppRegionCache` `@0x224fbc0`) or, when none is cached, from the system region (`getCurrentSystemRegion` `@0x224fbd0`). The value sent is `field_7` of that object (`charging/http/http_request_repository_impl.dart @0x2608acc`), which `CountryModel.fromJson` (`base_service/bean/model/country_model.dart`) fills from the key `english` (further fields `chinese`, `abbr`, `spell`, `code`). So `region` is the English country name of the model, not the abbreviation; the default model in `SpHelper::getCurrentRegion` (`base_service/utils/sp_helper.dart @0x2450018`) shows the shape: English name `USA`, Chinese name, abbreviation `US`, spelling, code `1`.

## `param_type`/`cmd`

n/a

## Response model (link)

no top-level model: the success closure (`charging/http/http_request_repository_impl.dart @0x2608b8c`, argument typed `Map<String, dynamic>`) reads the key `banners` (`@0x2608bdc`, lookup `@0x2608be4`) as `List?` (`@0x2608c1c`) and parses each element with [`BannerModel`](../../../models/other.md#bannermodel).fromJson (`@0x2608d04`, call target `#0x22a7ee8`, `charging/model/banner_model.dart`); a missing list is logged as `get banners response data is null` (`@0x2608d98`). The callback receives the list (`ClosureCall` `@0x2608dc0`).

## Response

(asm-traced) One key is read from the top level of the response: `banners` (list). Keys of `charging::BannerModel` (`data/models.json`): `img_url` (String?), `content` (String?), `banner_id` (int?), `category` (int?), `img_url_home` (String?), `img_url_device` (String?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "region": "<region>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender, its closures or the caller functions read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getBanners` @0x2608a60 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getBanners`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::getBannerData`

Call sites (grep of the asm, traced 2026-10-20): `getBanners` is called from `DeviceMainLogic::getBannerData` (`charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x26089f0`).

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
