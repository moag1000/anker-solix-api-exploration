> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# support_option

## Purpose

Reads which dynamic-price countries, areas and providers a site supports: `DynamicPriceDetailLogic::getSupportOption` and `StationPriceModeLogic::requestCloud` call `getDynamicPriceSupportOption`.

## Upstream name

`get_dynamic_price_providers` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/dynamic_price/support_option` (asm-traced): URL string at `http_request_repository_impl.dart @0x28a47b8`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x28a47b0`, in `HttpRequestControllerImpl::getDynamicPriceSupportOption` (`http_request_repository_impl.dart @0x28a46e8`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is a 2-pair map literal typed `<String, String>` (type arguments `@0x28a476c`) built in `getDynamicPriceSupportOption` (`http_request_repository_impl.dart @0x28a46e8`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | string | yes | `"<site_id>"` | key `@0x28a4744`, value store `@0x28a4754` (parameter at `fp-0x28`) |
| `device_pn` | string | yes | `"<device_pn>"` | key `@0x28a4758`, value store `@0x28a4768` (parameter at `fp-0x18`) |

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::DynamicPriceCountryAreaModel` (`data/models.json` key; fields on [`models/pricing.md`](../../../models/pricing.md#dynamicpricecountryareamodel)), parsed in the success closure `http_request_repository_impl.dart @0x28a4804` by `DynamicPriceCountryAreaModel.fromJson`.

## Response

The model has the single top-level key `country_info` (element type not resolved in `data/models.json`).

## Example request/response

Request, synthesized (decrypted body as built by `getDynamicPriceSupportOption`)

```json
{"site_id": "<site_id>", "device_pn": "<device_pn>"}
```

## Errors seen

None traced. The builder's failure callback is the `postJML` template `@0x226824c`; the callers' callbacks were not read. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getDynamicPriceSupportOption` @0x28a46e8 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/feature/utilitiy_rate_plan/dynamic_price/detail/dynamic_price_detail_logic.dart::getSupportOption`
- `charging/feature/utilitiy_rate_plan/station_price_mode/station_price_mode_logic.dart::requestCloud`
- `charging/http/http_request_repository.dart::getDynamicPriceSupportOption`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta. The model `DynamicPriceCountryAreaModel` is `≤3.18.0` in `data/models.json`.

## Known unknowns

- The element structure of `country_info` (the model keeps it untyped). — reclassified: server (elements of an untyped list; the content is server data)
- Whether `site_id` may be empty for a device not yet in a site: the app passes whatever its caller holds. — reclassified: server (what the server accepts is not in the app)
- Failure handling in the callers was not read.

## Device-tested by

none
