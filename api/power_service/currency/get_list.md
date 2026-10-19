> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_list

## Purpose

<!-- TODO -->

## Upstream name

`get_currency_list` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/currency/get_list`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x29ad624`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `counrty` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x29ad540` |

Rows are the union over 2 senders; `source` is the first sender that sets the key.

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

- `charging/http/http_request_repository_impl.dart`: `getCurrencyGetList` @0x29ad540 (encryptionRequestHttp; encrypted: true)
- `micro_hes/src/a17ex/home/components/electricity_price/a17ex_electricity_price_logic.dart`: `_fetchCurrencyFromServer` @0x35fdabc (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/common_bussiness/currency/app_currency_process_list_controller.dart::getUnitCurrency`
- `charging/http/http_request_repository.dart::getCurrencyGetList`
- `charging/impl/http_service_impl.dart::getCurrencyGetList`
- `micro_hes/src/a17ex/home/components/electricity_price/a17ex_electricity_price_logic.dart::getSPList`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
