> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# adjust_station_price_unit

## Purpose

Writes the price unit (currency) of a station when the user switches it on the fixed-rate plan page (`FixedRateLogic::switchPriceUnit`, through `HttpRequestControllerImpl::changePriceUnit`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/adjust_station_price_unit` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3ecfa20`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3ecfa18`, in `HttpRequestControllerImpl::changePriceUnit` (`charging/http/http_request_repository_impl.dart @0x3ecf954`), sent through `requestHttp` (`@0x3ecfa48`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::changePriceUnit` (`charging/http/http_request_repository_impl.dart`, call `@0x3ecfa48`, argument list `@0x3ecfa40`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `HttpRequestControllerImpl::changePriceUnit` (`charging/http/http_request_repository_impl.dart @0x3ecf9d4`, 2 keys). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | string | yes | `"<station_id>"` | `charging/http/http_request_repository_impl.dart @0x3ecf9ac` |
| `price_unit` | string | yes | `"<price_unit>"` | `charging/http/http_request_repository_impl.dart @0x3ecf9c0` |

## `param_type`/`cmd`

n/a

## Response model (link)

no `fromJson`: the success closure (`charging/http/http_request_repository_impl.dart @0x3ecfb0c`) reads the single key `price_unit` from the response map (key `@0x3ecfb38`, lookup call `@0x3ecfb58`, cast to `String?` `@0x3ecfb88`) and wraps it in a `PriceUnitModel` (`@0x3ecfb98`) that it hands to the stored callback (`ClosureCall` `@0x3ecfbbc`). `PriceUnitModel` has no row in `data/models.json`.

## Response

(asm-traced) One key is read by the app: `price_unit` (String?). Nothing else of the response body is used.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "price_unit": "<price_unit>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`. The failure closure (`charging/http/http_request_repository_impl.dart @0x3ecfa64`) logs the code and message and calls `exeError` without comparing the code.

## Callers in app

- `base_service/api_url.dart`: `adjustStationPriceUnit` @0x29ae7dc (URL literal only, no `*Http*` call; sender `ElectricityUsageHelper::changeCurrencyUnit` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x29ae5f0`), reached through callers `ElectricityUsageHelper::changeCurrencyUnit` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x29ae5f0`); resolved from the URL literal at `base_service/api_url.dart @0x29ae7f4` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `charging/http/http_request_repository_impl.dart`: `changePriceUnit` @0x3ecf954 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::changePriceUnit`
- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart::switchPriceUnit`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The set of currency strings the server accepts or returns for `price_unit`: the app passes the value through from a parameter.
- What the server does when the station has no fixed-rate plan: no response key other than `price_unit` is read.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
