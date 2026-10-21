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
| `peak_sessions` | `List<Map<String, dynamic>>` | no | 3.24.3 | `utility_rate_plans_response.dart @0x487920c`; copied with `List.from` typed `<Map<String, dynamic>>` (`@0x48792ec`); an empty growable list when the value is not a list (`@0x4879300`) |
| `price_unit` | `String` | no (default `"$"`) | 3.24.3 | `utility_rate_plans_response.dart @0x4879320`; `fromJson` replaces a missing or null value with the string `"$"` (`@0x487933c`) |

The element maps of `peak_sessions` are kept as raw maps (their keys are not read in `fromJson`). The same key appears as `peak_sessions` in the request of the TOU save call that the new flow sends through [edit_system_strategy](../api/charging_hes_installer_svc/edit_system_strategy.md) (`large_tou_repository.dart @0x4884dc4`), so the element layout is probably shared; that is not traced here.

## Produced by

[`get_utility_rate_plans`](../api/charging_hes_installer_svc/get_utility_rate_plans.md): `TouHttpService.getUtilityRatePlans` (`tou_http_service.dart @0x48790cc`) passes the closure `UtilityRatePlansResponse.fromJson` to `HttpHelper.request` (`@0x4879170`); the factory body is at `utility_rate_plans_response.dart @0x48791c8`.

## Consumed by

`LargeTouRepository` (`electricity_price/components/tou/impl_v2/repository/large_tou_repository.dart`, call `@0x4878f8c`). Field-level use is not traced.

## Changed since 3.18.0

The whole class is new in 3.24.3 (`since` 3.24.3 on both keys). Other senders of the same URL do not use this class and read single keys from the raw map; see the endpoint page.

## Known unknowns

- The keys inside each `peak_sessions` map are not traced (the model keeps raw maps). — traced 2026-10-20: `large_tou_repository.dart` (the consumer, call `@0x4878f8c`) loads only the two string keys `peak_sessions` and `price_unit`; the keys inside each element map are read in other files that use the key `peak_sessions` (for example `tou_plan_logic.dart`, `general_price_setting.dart`, `electricity_usage_helper.dart`), whose read sites were not followed.
- The `"$"` default means a missing unit renders as a dollar sign even for non-dollar sites; whether the server always sends the key is not known.
