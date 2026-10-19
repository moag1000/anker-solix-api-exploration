> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# product_categories

## Purpose

<!-- TODO -->

## Upstream name

`get_product_categories` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/product_categories`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x2619a98`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys found by the extractor. <!-- TODO -->

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

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
