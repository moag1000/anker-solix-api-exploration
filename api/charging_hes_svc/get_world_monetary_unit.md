> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_world_monetary_unit

## Purpose

Reads the list of currency units for a site (callers `HomeSettingLogic::_getCurrency`, `PeaksAndValleysLogic::fetchPriceUnits`, `SystemPolicyLogic::getCurrency`, `FixedRateLogic::getCurrency`, through `HttpRequestControllerImpl::getPriceUnits`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_world_monetary_unit` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x28e9a70`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x28e9a68`, in `HttpRequestControllerImpl::getPriceUnits` (`charging/http/http_request_repository_impl.dart @0x28e9994`), sent through `requestHttp` (`@0x28e9a98`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::getPriceUnits` (`charging/http/http_request_repository_impl.dart`, call `@0x28e9a98`, argument list `@0x28e9a90`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) `HttpRequestControllerImpl::getPriceUnits` (`charging/http/http_request_repository_impl.dart @0x28e9994`) stores 3 keys in one map literal with type arguments `<String, String?>` (`@0x28e9a24`), so the values are Strings (a null value is allowed for `siteId`). `countryCodes` and `areaCodes` are stored as the constant empty string (`@0x28e99f4`, `@0x28e9a08`); `siteId` comes from a parameter (`@0x28e9a1c`). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `countryCodes` | string | yes | `""` | `charging/http/http_request_repository_impl.dart @0x28e99e8` |
| `areaCodes` | string | yes | `""` | `charging/http/http_request_repository_impl.dart @0x28e99fc` |
| `siteId` | string | yes | `"<siteId>"` | `charging/http/http_request_repository_impl.dart @0x28e9a10` |

## `param_type`/`cmd`

n/a

## Response model (link)

read key by key, no `fromJson`: the success closure (`charging/http/http_request_repository_impl.dart @0x28e9ab4`) reads the key `priceUnits` (`@0x28e9b1c`, cast to `List` `@0x28e9b68`) and, for every element, the keys `priceUnit` (String?, `@0x28e9bf4`, cast `@0x28e9c50`), `isDefault` (bool?, `@0x28e9c6c`, cast `@0x28e9cc4`) and `name` (String?, `@0x28e9cd8`, cast `@0x28e9d30`) into a `PriceUnits` object (`@0x28e9c54`), collects them in a list (`@0x28e9adc`) and passes the list to the stored callback (`ClosureCall` `@0x28e9df4`). `PriceUnits` has no row in `data/models.json`.

## Response

(asm-traced) Response keys read by the app: `priceUnits` (List), and per element `priceUnit` (String?), `isDefault` (bool?) and `name` (String?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "countryCodes": "",
  "areaCodes": "",
  "siteId": "<siteId>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`. The compare `cmp x4, #0x3f` in the success closure (`charging/http/http_request_repository_impl.dart @0x28e9cb0`) is a class-id test for the `bool?` cast, not a response code.

## Callers in app

- `base_service/api_url.dart`: `getPriceUnitsConfig` @0x29ae8dc (URL literal only, no `*Http*` call; sender `ElectricityUsageHelper::getPriceUnits` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x29ae3f4`), reached through callers `ElectricityUsageHelper::getPriceUnits` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x29ae3f4`); resolved from the URL literal at `base_service/api_url.dart @0x29ae8f4` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `charging/http/http_request_repository_impl.dart`: `getPriceUnits` @0x28e9994 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getPriceUnits`
- `charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart::_getCurrency`
- `charging/ui/page/device/a5101/setting/peaksAndValleys/peaks_valleys_logic.dart::fetchPriceUnits`
- `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::getCurrency`
- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/fixed_rate/fixed_rate_logic.dart::getCurrency`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Why `countryCodes` and `areaCodes` are always empty: the builder stores the constant empty string for both; the server side filter is not known.
- Which element of the list the callers treat as the default unit: the callers were not read beyond their names.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
