> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# adjust_station_price_unit

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/adjust_station_price_unit`, method: not extracted by the inventory <!-- TODO -->; string-only: `base_service/api_url.dart @0x29ae7f4`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3ecf954` |
| `price_unit` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3ecf954` |

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

- `base_service/api_url.dart`: `adjustStationPriceUnit` @0x29ae7dc (URL literal only, no `*Http*` call; sender `ElectricityUsageHelper::changeCurrencyUnit` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x29ae5f0`), reached through callers `ElectricityUsageHelper::changeCurrencyUnit` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x29ae5f0`); resolved from the URL literal at `base_service/api_url.dart @0x29ae7f4` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `charging/http/http_request_repository_impl.dart`: `changePriceUnit` @0x3ecf954 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::changePriceUnit`
- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart::switchPriceUnit`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
