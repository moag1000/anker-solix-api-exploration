> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# support_option

## Purpose

<!-- TODO -->

## Upstream name

`get_dynamic_price_providers` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/dynamic_price/support_option`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x28a47b8`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x28a46e8` |
| `device_pn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x28a46e8` |

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

- `charging/http/http_request_repository_impl.dart`: `getDynamicPriceSupportOption` @0x28a46e8 (encryptionRequestHttp; encrypted: true)

Called from: `charging/feature/utilitiy_rate_plan/dynamic_price/detail/dynamic_price_detail_logic.dart::getSupportOption`, `charging/feature/utilitiy_rate_plan/station_price_mode/station_price_mode_logic.dart::requestCloud`, `charging/http/http_request_repository.dart::getDynamicPriceSupportOption`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
