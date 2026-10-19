> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# adjust_station_price_unit

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_energy_service/adjust_station_price_unit`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x2fa7460`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

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

- `charging/http/http_request_repository_impl.dart`: `changeA17B1PriceUnit` @0x2fa73e0 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::changeA17B1PriceUnit`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley/a17b1_peak_valley_logic.dart::switchPriceUnit`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart::switchPriceUnit`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
