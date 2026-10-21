> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# ack_utility_rate_plan

## Purpose

Acknowledges the utility rate plan of an A17B1 station after the user confirmed it (callers `ElectricitySceneLogic::ackUtilityRatePlan` and `A17B1PeakValleyPriceDiffSecondaryEditLogic::ackUtilityRatePlan`) (string-only: inferred from the caller names, the chain is not in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_energy_service/ack_utility_rate_plan` (asm-traced): URL string `@0x26ead00`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x26eacf8`, in `HttpRequestControllerImpl::ackUtilityRatePlanData` (`charging/http/http_request_repository_impl.dart @0x26eabe0`), sent through `HttpRequestControllerImpl::requestHttp` (`@0x26ead30`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: both field types are not read) One sender. The map literal has the type arguments `<String, dynamic>` (`charging/http/http_request_repository_impl.dart @0x26eac40`), which name no value type. Each key is added only when its parameter is non-null and non-empty.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | optional | `"<station_id>"` | `charging/http/http_request_repository_impl.dart @0x26eac78` (guard: `cmp w3, NULL` `@0x26eac5c`, length test `cbz` `@0x26eac68`; the map store is the call at `@0x26eac80`) |
| `sn` | ? | optional | `"<sn>"` | `charging/http/http_request_repository_impl.dart @0x26eacb4` (guard: `cmp w3, NULL` `@0x26eac94`, length test `cbz` `@0x26eaca0`; store call `@0x26eacbc`) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed in this wrapper: the closure passed as `complete` (`charging/http/http_request_repository_impl.dart @0x24044f0`) calls a stored callback with its argument when the callback is non-null (`@0x240451c`, `ClosureCall` `@0x240452c`) and reads no key. Whether the callers' callbacks parse the body was not followed.

## Response

No response key is read by the wrapper (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "sn": "<sn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `ackUtilityRatePlanData` @0x26eabe0 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::ackUtilityRatePlanData`
- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart::ackUtilityRatePlan`
- `charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley_price_diff_secondary_edit/a17b1_peak_valley_price_diff_secondary_edit_logic.dart::ackUtilityRatePlan`

Callbacks and values (traced 2026-10-20, app side): `A17B1ElectricitySceneLogic::ackUtilityRatePlan` (`charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart @0x26ea9f0`) passes a `complete` closure (`@0x26eae04`) that calls `syncGoHome` (`@0x26eae30`); the call sends `station_id` from `field_c3` of the logic (`@0x26eaa44`). `A17B1PeakValleyPriceDiffSecondaryEditLogic::ackUtilityRatePlan` (`charging/ui/page/device/a17b1/device_setting/utility_rate_plan/peak_valley_price_diff_secondary_edit/a17b1_peak_valley_price_diff_secondary_edit_logic.dart @0x2745814`) applies the router-type rule of [get_world_monetary_unit](get_world_monetary_unit.md#request) (`sn` from `field_6b` of the device object when `devicePush`, `@0x27458ac`; `station_id` from `field_1f` when `sitePush`, `@0x27458d4`), its success closure (`@0x27459bc`) calls `syncSiteConfig` (`@0x2745a34`, see [sync_config](sync_config.md)) and fires an event, and its failure closure (`@0x2745960`) dismisses the loading dialog and shows the message (`dismiss` `@0x2745994`, `show` `@0x27459a0`).

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `station_id` and `sn`: both come from parameters of the wrapper (`charging/http/http_request_repository_impl.dart @0x26eac60`); the map literal names no value type. — attempted 2026-10-20 (`sn` is the String serial getter `field_6b` where it comes from a device object, see Callers in app; `station_id` is `field_c3` / `field_1f` of the logics with no declared type, two-hop not readable: `electricity_scene_logic.dart @0x26eaa44`, `a17b1_peak_valley_price_diff_secondary_edit_logic.dart @0x27458d4`)
- What the server stores when the call carries neither key (both are optional).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
