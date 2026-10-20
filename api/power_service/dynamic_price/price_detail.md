> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# price_detail

## Purpose

Reads the dynamic electricity price of a day for a provider and area: `DynamicPriceDetailLogic::requestDynamicPriceDetail` (`dynamic_price_detail_logic.dart`) calls `getDynamicPriceDetail`.

## Upstream name

`get_dynamic_price_details` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/dynamic_price/price_detail` (asm-traced): URL string at `http_request_repository_impl.dart @0x26e3db4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x26e3dac`, in `HttpRequestControllerImpl::getDynamicPriceDetail` (`http_request_repository_impl.dart @0x26e3cbc`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is a 4-pair map literal typed `<String, String>` (type arguments `@0x26e3d68`), so every value is a String or non-null String as the static type says; the builder is `getDynamicPriceDetail` (`http_request_repository_impl.dart @0x26e3cbc`).

| field | type | required | example | source |
|---|---|---|---|---|
| `company` | string | yes | `"<company>"` | key `@0x26e3d18`, value store `@0x26e3d28` (parameter at `fp-0x18`) |
| `area` | string | yes | `"<area>"` | key `@0x26e3d2c`, value store `@0x26e3d3c` (parameter at `fp-0x10`) |
| `date` | string | yes | `"<date>"` | key `@0x26e3d40`, value store `@0x26e3d50` (parameter at `fp-0x20`) |
| `device_sn` | string | yes | `"<device_sn>"` | key `@0x26e3d54`, value store `@0x26e3d64` (parameter at `fp-0x28`) |

## `param_type`/`cmd`

n/a

## Response model (link)

`base_service::DynamicPriceDetailModel` (`data/models.json` key; fields on [`models/pricing.md`](../../../models/pricing.md#dynamicpricedetailmodel)), parsed in the success closure `http_request_repository_impl.dart @0x26e3e00` by `DynamicPriceDetailModel.fromJson`.

## Response

Top-level keys of the model (from `data/models.json`): `release_time` (String), `currency` (String), `today_avg_price` (String), `tomorrow_avg_price` (String), `today_price_trend` and `tomorrow_price_trend` (element type not resolved there).

## Example request/response

Request, synthesized (decrypted body as built by `getDynamicPriceDetail`)

```json
{"company": "<company>", "area": "<area>", "date": "<date>", "device_sn": "<device_sn>"}
```

Response keys: see Response; no capture.

## Errors seen

None traced. The builder's failure callback is the `postJML` template `@0x226824c` that forwards to the caller's callback; the callers' callbacks were not read. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getDynamicPriceDetail` @0x26e3cbc (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/feature/utilitiy_rate_plan/dynamic_price/detail/dynamic_price_detail_logic.dart::requestDynamicPriceDetail`
- `charging/http/http_request_repository.dart::getDynamicPriceDetail`
- `charging/impl/http_service_impl.dart::getDynamicPriceDetail`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta. The model `DynamicPriceDetailModel` is `≤3.18.0` in `data/models.json`.

## Known unknowns

- Format of `date` and the set of `company`/`area` values: the builder passes the parameters through; the value set is server side (see [support_option](support_option.md) for the lists the app can fetch).
- Failure handling in the callers of `getDynamicPriceDetail` was not read.

## Device-tested by

none
