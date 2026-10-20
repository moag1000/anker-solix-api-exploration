> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# adjust_station_price_unit

## Purpose

Changes the price unit (currency) of an A17B1 station's rate plan (callers `A17B1PeakValleyLogic::switchPriceUnit` and `A17B1FixedRateLogic::switchPriceUnit` through `HttpRequestControllerImpl::changeA17B1PriceUnit`) (string-only: inferred from the caller names, the chain is not in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_energy_service/adjust_station_price_unit` (asm-traced): URL string `@0x2fa7460`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x2fa7458`, in `HttpRequestControllerImpl::changeA17B1PriceUnit` (`charging/http/http_request_repository_impl.dart @0x2fa73e0`), sent through `HttpRequestControllerImpl::requestHttp` (`@0x2fa7488`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: the body is built by the callers and no field type is read) The wrapper builds no keys; it forwards the map its caller passes. The only caller read, the closure in `A17B1PeakValleyLogic` (`charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley/a17b1_peak_valley_logic.dart @0x2fa7dc4`), builds a `<String, dynamic>` literal (`@0x2fa7e1c`), which names no value type. The second caller, `A17B1FixedRateLogic::switchPriceUnit`, was not read.

| field | type | required | example | source |
|---|---|---|---|---|
| `price_unit` | ? | yes | `"<currency symbol>"` | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley/a17b1_peak_valley_logic.dart @0x2fa7e08` (value store `@0x2fa7e18`, parameter) |
| `sn` | ? | optional | `"<sn>"` | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley/a17b1_peak_valley_logic.dart @0x2fa7e8c` (guard: `cmp w0, NULL` `@0x2fa7e3c` and a compare with `Instance_JumpPeakRouterType` `@0x2fa7e54`) |
| `station_id` | ? | optional | `"<station_id>"` | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley/a17b1_peak_valley_logic.dart @0x2fa7edc` (guard: `cmp w0, NULL` `@0x2fa7ea4` and the same router-type compare `@0x2fa7ebc`) |

Router-type rule and the second caller (traced 2026-10-20): `A17B1PeakValleyLogic::switchPriceUnit` adds `sn` when the router type is `devicePush` (compare `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley/a17b1_peak_valley_logic.dart @0x2fa7e54`, value `field_13`, key store `@0x2fa7e8c`) and `station_id` when it is `sitePush` (`@0x2fa7ebc`, `field_1f`, `@0x2fa7edc`); the instances are explained in [get_world_monetary_unit](get_world_monetary_unit.md#request). `A17B1FixedRateLogic::switchPriceUnit` (`charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart`) builds the same body: `sn` from `field_13.field_6b` when the type is `devicePush` (compare `@0x2fa72a4`, key `@0x2fa72dc`) and `station_id` from `field_1f` when it is `sitePush` (`@0x2fa72fc`, key `@0x2fa731c`), added with `[]=` to a map that already holds `price_unit`.

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed as a model: the success closure of `changeA17B1PriceUnit` (`charging/http/http_request_repository_impl.dart @0x2fa754c`) reads the key `price_unit` (`@0x2fa7578`, tested as `String?`, `@0x2fa75c8`..`@0x2fa75d4`), builds an `A17B1PriceUnitModel` with it (allocation `@0x2fa75d8`, store `@0x2fa75e4`) and passes that to the caller's callback (`ClosureCall` `@0x2fa75fc`).

## Response

Key read by the closure: `price_unit` (String?). No other key is read.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "price_unit": "<currency symbol>",
  "sn": "<sn>",
  "station_id": "<station_id>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `changeA17B1PriceUnit` @0x2fa73e0 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::changeA17B1PriceUnit`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley/a17b1_peak_valley_logic.dart::switchPriceUnit`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart::switchPriceUnit`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `price_unit`, `sn` and `station_id`: values of the caller's parameters and fields (`charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley/a17b1_peak_valley_logic.dart @0x2fa7e18`); the literal names no value type. — attempted 2026-10-20 (two-hop not readable: `switchPriceUnit` (`charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x2fa7364`), `switchPriceUnit` (`charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley/a17b1_peak_valley_logic.dart @0x2fa7f24`) pass slots or fields of their own frames; no literal or declared type in the argument setups)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
