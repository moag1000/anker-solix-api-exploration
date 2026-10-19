> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# product_accessories

## Purpose

<!-- TODO -->

## Upstream name

`get_product_accessories` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/product_accessories`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x33cb248`

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

- `charging/http/http_request_repository_impl.dart`: `getProductAccessories` @0x33cb1c8 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getProductAccessories`
- `charging/ui/page/device/a17c0/a17c0accessory/add_accessory/a17c0add_accessory_logic.dart::onInit`
- `charging/ui/page/device/a17c0/a17c0home/a17c0home_logic.dart::onInit`
- `charging/ui/page/device/anker_ota/a17y0_ble_ota/a17y0_ota_logic.dart::onInit`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::_initLogic`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
