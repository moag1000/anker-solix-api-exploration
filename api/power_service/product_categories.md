> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# product_categories

## Purpose

Loads the product category catalogue: `A5150DeployWifiLogic::_getApGuideImageFromCloud`, `ScanLogic::onInit`, `ScanAppointDeviceLogic::onInit` and `DeviceMainLogic` (`_initLogic`, `onMessageDispatch`, `pullToRefresh`) call `getProductCategories`, which caches the categories.

## Upstream name

`get_product_categories` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`GET /power_service/v1/product_categories` (asm-traced): URL string at `http_request_repository_impl.dart @0x2619a98`, method object `Method.get` (pool entry `pp+0x340e8`) at `@0x2619a90`, in `HttpRequestControllerImpl::getProductCategories` (`http_request_repository_impl.dart @0x2619a10`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is an empty map literal (`ldr x16, [THR, #0xa8]` empty array `@0x2619a50`, `Map._fromLiteral` `@0x2619a58`); the builder contains no `[]=` call, so no key is added. The map goes to `encryptionRequestHttp` (`@0x2619ac0`). The call is a GET, so the empty map is the `data` argument of a GET.

## `param_type`/`cmd`

n/a

## Response model (link)

`base_service::ProductCategoriesModel` (`data/models.json` key; fields on [`models/products.md`](../../models/products.md#productcategoriesmodel)), one object per list element. The success closure `http_request_repository_impl.dart @0x2619adc` casts the response to `List`, maps the elements with the closure `sp_util_impl.dart @0x22f93e8` (`ProductCategoriesModel.fromJson` `@0x22f9410`), then stores the result with `setProductCategories` (`@0x2619bd8`) and updates the product-info cache (`invalidateProductInfoCache` `@0x2619bdc`, `updateProductCategories` `@0x2619c08`).

## Response

The response data is a JSON list. Keys of one element (from `data/models.json`): `img_url` (String), `name` (String), `products` (List; the closure `product_categories_model.dart @0x22f9680` inside `ProductCategoriesModel.fromJson` maps its elements with `ProductInfoModel.fromJson` `@0x22f96a8`, keys on [product_accessories](product_accessories.md)), all nullable.

## Example request/response

Request, synthesized (GET, empty `data`)

```json
{}
```

Response: a list of the elements above; no capture.

## Errors seen

None traced. The call passes no printed failure closure of its own; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getProductCategories` @0x2619a10 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getProductCategories`
- `charging/impl/http_service_impl.dart::getProductCategories`
- `charging/ui/page/device/a5150/wifiConfig/a5150_deploy_wifi_logic.dart::_getApGuideImageFromCloud`
- `charging/ui/page/device/connect/scan_logic.dart::onInit`
- `charging/ui/page/device/main/sitation_energy_system/scan_appoint_device/scan_appoint_device_logic.dart::onInit`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::_initLogic`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::onMessageDispatch`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::pullToRefresh`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta. The model `ProductCategoriesModel` is `≤3.18.0` in `data/models.json`.

## Known unknowns

- The model lists `products` as an untyped `List`; the element class `ProductInfoModel` is read from the mapping closure named in Response.
- Which categories the server returns per account or country: not derivable from the app.

## Device-tested by

none
