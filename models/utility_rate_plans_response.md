> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# UtilityRatePlansResponse

## Purpose

Carries the utility rate plan of a large (HES) station in the new time-of-use flow: the list of peak sessions and the price unit, as returned by `get_utility_rate_plans`.

## Dart class + file

`UtilityRatePlansResponse`, file `electricity_price/components/tou/impl_v2/model/response_param/utility_rate_plans_response.dart` (package `electricity_price`), `fromJson` at `@0x48791e0`.

## Fields

Column `since`: `3.24.3` means the key was first seen in 3.24.3 (the class does not exist in the 3.18.0 asm). The `source` address is the string load of the JSON key inside `fromJson` and was re-read in the asm.

### UtilityRatePlansResponse

`fromJson` `utility_rate_plans_response.dart @0x48791e0`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `peak_sessions` | `List` | no | 3.24.3 | `utility_rate_plans_response.dart @0x487920c` |
| `price_unit` | `String` | yes | 3.24.3 | `utility_rate_plans_response.dart @0x4879320` |

The element type of `peak_sessions` is not resolved by the extractor. The same key appears as `peak_sessions` in the request of the TOU save call that the new flow sends through [edit_system_strategy](../api/charging_hes_installer_svc/edit_system_strategy.md) (`large_tou_repository.dart @0x4884dc4`), so the element layout is shared with that request; it is not traced here.

## Produced by

[`get_utility_rate_plans`](../api/charging_hes_installer_svc/get_utility_rate_plans.md): `TouHttpService.getUtilityRatePlans` (`tou_http_service.dart @0x48790cc`) passes the closure `UtilityRatePlansResponse.fromJson` to `HttpHelper.request` (`@0x4879170`); the factory body is at `utility_rate_plans_response.dart @0x48791c8`.

## Consumed by

`LargeTouRepository` (`electricity_price/components/tou/impl_v2/repository/large_tou_repository.dart`, call `@0x4878f8c`). Field-level use is not traced.

## Changed since 3.18.0

The whole class is new in 3.24.3 (`since` 3.24.3 on both keys). Other senders of the same URL do not use this class and read single keys from the raw map; see the endpoint page.

## Known unknowns

- The element structure of `peak_sessions` is not traced.
- `price_unit` is nullable; what the app does when it is missing is not traced.
