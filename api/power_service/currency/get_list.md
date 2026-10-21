> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_list

## Purpose

Reads the currency list: `AppCurrencyProcessListController::getUnitCurrency`, `CurrencyProcessListController::getUnitCurrency`, `CurrencyUnitManager::_requestFromServer`, `HesFixedPriceLogic::commonGetCurrency`, `ElectricityPriceServiceImpl::getDefaultUnit` and `PpsTouSetting::getDefaultCurrencyByCountry` call `getCurrencyGetList`; `A17EXElectricityPriceLogic::_fetchCurrencyFromServer` sends the same URL.

## Upstream name

`get_currency_list` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/currency/get_list` (asm-traced) at the senders that load a `Method` object next to the URL string (pool entry `pp+0xa7e0`, `Method.post`):

- `HttpRequestControllerImpl::getCurrencyGetList` (`http_request_repository_impl.dart @0x29ad540`): URL string `@0x29ad624`, method object `Method.post` (`pp+0xa7e0`) `@0x29ad61c`.
- `A17EXElectricityPriceLogic::_fetchCurrencyFromServer` (`a17ex_electricity_price_logic.dart @0x35fdabc`): URL string `@0x35fdbec`, method object `Method.post` (`pp+0xa7e0`) `@0x35fdbe4`.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Both senders send one key spelled `counrty` (sic) in a map typed `<String, String>`, so the value is a String.

| field | type | required | example | source |
|---|---|---|---|---|
| `counrty` | string | yes | `"US"` | key `http_request_repository_impl.dart @0x29ad5c4` in the repository sender `getCurrencyGetList` (function `@0x29ad540`): value store `@0x29ad5d4`, type arguments `@0x29ad5d8`; the value is the current region's `field_7` with the string `"US"` as null fallback (`@0x29ad5a4`) |
| `counrty` | string | yes | `"country"` | key `a17ex_electricity_price_logic.dart @0x35fdb88` in the A17EX sender (function `@0x35fdabc`): value the literal string `"country"` (`@0x35fdb94`, not a country code), store `@0x35fdb9c`, type arguments `@0x35fdba0` |

## `param_type`/`cmd`

n/a

## Response model (link)

`base_service::CurrencyInfo` (`data/models.json` key; fields on [`models/pricing.md`](../../../models/pricing.md#currencyinfo)), parsed by `CurrencyInfo.fromJson` in the success closures `http_request_repository_impl.dart @0x29ad668` and `a17ex_electricity_price_logic.dart @0x35fdca4`.

## Response

Top-level keys of the model (from `data/models.json`): `currency_list` (element type not resolved there) and `default_currency` (`DefaultCurrency`).

## Example request/response

Request, synthesized (decrypted body of the repository sender)

```json
{"counrty": "US"}
```

Response keys: see Response; no capture.

## Errors seen

None traced. The failure callbacks (`app_currency_process_list_controller.dart @0x2fa9690`, `currency_unit_mgr.dart @0x3938d64`, `a17ex_electricity_price_logic.dart @0x35fdc30` and others) log or forward the code; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getCurrencyGetList` @0x29ad540 (encryptionRequestHttp; encrypted: true)
- `micro_hes/src/a17ex/home/components/electricity_price/a17ex_electricity_price_logic.dart`: `_fetchCurrencyFromServer` @0x35fdabc (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/common_bussiness/currency/app_currency_process_list_controller.dart::getUnitCurrency`
- `charging/http/http_request_repository.dart::getCurrencyGetList`
- `charging/impl/http_service_impl.dart::getCurrencyGetList`
- `micro_hes/src/a17ex/home/components/electricity_price/a17ex_electricity_price_logic.dart::getSPList`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta. The model `CurrencyInfo` is `≤3.18.0` in `data/models.json`.

## Known unknowns

- Whether the server reads the misspelled key `counrty` (both app senders use it); the library's behaviour for `country` is not known.
- Whether the literal value `"country"` of the A17EX sender is intentional: it is a string constant at `@0x35fdb94`, not a variable. — reclassified: server (not visible in the app: nothing in the code says whether the constant is intended)
- The element structure of `currency_list`. — reclassified: server (not visible in the app: the model keeps the items untyped)

## Device-tested by

none
