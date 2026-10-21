> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# product_accessories

## Purpose

Loads the accessory product catalogue: `A17c0addAccessoryLogic::onInit`, `A17c0homeLogic::onInit`, `A17y0OtaLogic::onInit` and `DeviceMainLogic::_initLogic` call `getProductAccessories`, which caches the list.

## Upstream name

`get_product_accessories` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`GET /power_service/v1/product_accessories` (asm-traced): URL string at `http_request_repository_impl.dart @0x33cb248`, method object `Method.get` (pool entry `pp+0x340e8`) at `@0x33cb240`, in `HttpRequestControllerImpl::getProductAccessories` (`http_request_repository_impl.dart @0x33cb1c8`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is an empty map literal (`ldr x16, [THR, #0xa8]` empty array `@0x33cb200`, `Map._fromLiteral` `@0x33cb208`); the builder contains no `[]=` call, so no key is added. The map goes to `encryptionRequestHttp` (`@0x33cb270`). The call is a GET, so the empty map is the `data` argument of a GET.

## `param_type`/`cmd`

n/a

## Response model (link)

`base_service::ProductInfoModel` (`data/models.json` key, no model page), one object per list element. The success closure `http_request_repository_impl.dart @0x33cb28c` casts the response to `List` (`r0 = List()` `@0x33cb2e8`), maps the elements with the closure `product_categories_model.dart @0x22f9680` (`ProductInfoModel.fromJson` `@0x22f96a8`), then calls a dispatch-table call without a printed selector (`@0x33cb350`, expected `toList`) and stores the result with `setProductAccessories` (`@0x33cb388`).

## Response

The response data is a JSON list. Keys of one element (from `data/models.json`): `img_url` (String), `name` (String), `net_guideline` (String), `net_img_url` (String), `product_code` (String), `ble_img_url` (String), `p_codes` (List), `conn_confirm_model` (int), `conn_confirm_img` (String), `conn_confirm_tips` (String), `custom_fields` (`CustomFieldsModel`), all nullable.

## Example request/response

Request, synthesized (GET, empty `data`)

```json
{}
```

Response: a list of the elements above; no capture.

## Errors seen

None traced. The builder has no failure callback of its own in the resolved list (the call passes no printed failure closure); no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getProductAccessories` @0x33cb1c8 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getProductAccessories`
- `charging/ui/page/device/a17c0/a17c0accessory/add_accessory/a17c0add_accessory_logic.dart::onInit`
- `charging/ui/page/device/a17c0/a17c0home/a17c0home_logic.dart::onInit`
- `charging/ui/page/device/anker_ota/a17y0_ble_ota/a17y0_ota_logic.dart::onInit`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::_initLogic`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta. The model `ProductInfoModel` is `≤3.18.0` in `data/models.json`.

## Known unknowns

- That the dispatch-table call after `map()` is `toList` is the expectation; its selector is not named by Blutter (the list is passed to `setProductAccessories`). — traced 2026-10-20: the same unnamed selector (`GDT[cid_x0 + 0x3506a]`) follows `map()` in several senders of this app and Blutter prints no name for it
- Which products the server includes for an account: not derivable from the app.

## Device-tested by

none
