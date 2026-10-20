> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_world_monetary_unit

## Purpose

Loads the list of currencies (price units) for the A17B1 rate-plan screens (callers `A17B1PeakValleyLogic::getCurrency`, `A17B1FixedRateLogic::getCurrency`, `A17B1PeakValleyPriceDiffSecondaryEditLogic::getCurrency` through `HttpRequestControllerImpl::getA17B1PriceUnits`) (string-only: inferred from the caller names, the chain is not in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_energy_service/get_world_monetary_unit` (asm-traced): URL string `@0x28be994`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x28be98c`, in `HttpRequestControllerImpl::getA17B1PriceUnits` (`charging/http/http_request_repository_impl.dart @0x28be914`), sent through `HttpRequestControllerImpl::requestHttp` (`@0x28be9bc`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: both field types are not read) The wrapper builds no keys: its `data` argument is its own parameter (`ldur x16, [fp, #-0x10]` `charging/http/http_request_repository_impl.dart @0x28be9a0`). The three callers build a `<String, dynamic>` literal (`charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley/a17b1_peak_valley_logic.dart @0x28be798`, `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x28c07ac`, `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley_price_diff_secondary_edit/a17b1_peak_valley_price_diff_secondary_edit_logic.dart @0x28bee94`), which names no value type, and add two keys, each behind a compare with `Instance_JumpPeakRouterType`.

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | ? | optional | `"<sn>"` | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley/a17b1_peak_valley_logic.dart @0x28be80c` (guard compare `@0x28be7d4`); `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x28c0824`; `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley_price_diff_secondary_edit/a17b1_peak_valley_price_diff_secondary_edit_logic.dart @0x28bef0c` |
| `station_id` | ? | optional | `"<station_id>"` | `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley/a17b1_peak_valley_logic.dart @0x28be85c` (guard compare `@0x28be83c`); `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x28c0864`; `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley_price_diff_secondary_edit/a17b1_peak_valley_price_diff_secondary_edit_logic.dart @0x28bef4c` |

Which key a request carries (traced 2026-10-20, app side; owner of this rule for the A17B1 rate-plan pages): the enum `JumpPeakRouterType` has two instances, `sitePush` (index 0, `objs.txt Obj!JumpPeakRouterType@420c961`) and `devicePush` (index 1, `objs.txt Obj!JumpPeakRouterType@420c981`). In the three callers the key `sn` is added only when the screen's router type is `devicePush` (compare `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley/a17b1_peak_valley_logic.dart @0x28be7d4`, value `field_6b` of a device object, `@0x28be7f4`; `a17b1_fixed_rate_logic.dart @0x28c07ec`, `field_6b`; `a17b1_peak_valley_price_diff_secondary_edit_logic.dart @0x28beed4`, `field_6b`), and `station_id` only when it is `sitePush` (`@0x28be83c`, `@0x28c0844`, `@0x28bef2c`, value `field_1f`, key store `@0x28be85c`). Because the enum has only these two instances, a request carries exactly one of the two keys, the one matching how the screen was opened (site or device); `field_6b` is the device serial-number getter (see [get_hes_dev_info](../charging_hes_svc/get_hes_dev_info.md)), so `sn` is the device serial and `station_id` the site id of the page. The key is stored even when its source is null: with a null device object `r3 = Null` (`@0x28be7ec`) and the `[]=` store still follows (`r2 = "sn"` `@0x28be80c`, `@0x28be814`), so the request then carries `"sn": null` (null on the wire, key present); the `station_id` branch stores `field_1f` without a null test (`@0x28be848`..`@0x28be864`). A key is absent only when the screen state object itself is null (`cmp w0, NULL` `@0x28be824`) or the router type matches neither instance.

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed through a model class: the success closure of the wrapper (`charging/http/http_request_repository_impl.dart @0x28be9d8`) reads the key `price_units` (`@0x28bea40`), requires a `List` (`@0x28beaa0`) and builds one `A17B1PriceUnits` per element (allocation `@0x28beb98`) from the element keys `price_unit` (`@0x28beb38`, tested as `String?` `@0x28beb88`) and `is_default` (`@0x28bebb0`, tested as `bool?` `@0x28bebf8`).

## Response

Keys read by the closure: `price_units` (list); per element `price_unit` (String?) and `is_default` (bool?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "sn": "<sn>",
  "station_id": "<station_id>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getA17B1PriceUnits` @0x28be914 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getA17B1PriceUnits`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley/a17b1_peak_valley_logic.dart::getCurrency`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley_price_diff_secondary_edit/a17b1_peak_valley_price_diff_secondary_edit_logic.dart::getCurrency`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart::getCurrency`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `sn` and `station_id`: values loaded from fields (`charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley/a17b1_peak_valley_logic.dart @0x28be7f4`) of the caller; the literals name no value type. — attempted 2026-10-20 (two-hop not readable: `getCurrency` (`charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley_price_diff_secondary_edit/a17b1_peak_valley_price_diff_secondary_edit_logic.dart @0x28bef94`), `getCurrency` (`charging/ui/page/device/a17b1/device_setting/utility_rate_plan/rate_plan_structure/fixed_rate/a17b1_fixed_rate_logic.dart @0x28c08ac`), `getCurrency` (`charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley/a17b1_peak_valley_logic.dart @0x28be8a4`) pass slots or fields of their own frames; no literal or declared type in the argument setups)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
