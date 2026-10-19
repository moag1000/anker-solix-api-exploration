> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# price_detail

## Purpose

<!-- TODO -->

## Upstream name

`get_dynamic_price_details` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/dynamic_price/price_detail`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x26e3db4`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `company` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x26e3cbc` |
| `area` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x26e3cbc` |
| `date` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x26e3cbc` |
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x26e3cbc` |

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

- `charging/http/http_request_repository_impl.dart`: `getDynamicPriceDetail` @0x26e3cbc (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/feature/utilitiy_rate_plan/dynamic_price/detail/dynamic_price_detail_logic.dart::requestDynamicPriceDetail`
- `charging/http/http_request_repository.dart::getDynamicPriceDetail`
- `charging/impl/http_service_impl.dart::getDynamicPriceDetail`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
