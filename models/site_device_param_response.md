> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# SiteDeviceParamResponse

## Purpose

Carries the time-of-use (TOU) response of `get_site_device_param` for `param_type` 6 as read by the electricity-price module: the mode type, the TOU slot list and the unit.

## Dart class + file

`SiteDeviceParamResponse`, `electricity_price/components/tou/impl_v2/model/response_param/site_device_param_response.dart` (package `electricity_price`), fromJson `@0x4879640`; the static tear-off `SiteDeviceParamResponse.fromJson` (closure `@0x487960c`) is passed as the response converter of the request.

## Fields

Column `since`: the class does not exist in 3.18.0 (no class of this name in the 3.18.0 asm), so every key is `3.24.3`. The class reads `param_data` first (`@0x4879668`); when it is null the constructor returns an empty object (`@0x4879688`). `use_time`, `mode_type` and `unit` are then read through a helper call (`@0x4879698`, `@0x48796c4`, `@0x48797fc`) whose receiver was not traced, so whether they are keys of `param_data` or of the outer response is not established.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `param_data` | `dynamic` (only tested for null) | yes | 3.24.3 | `site_device_param_response.dart @0x4879668` |
| `use_time` | `List<Map<String, dynamic>>?` (copied with `List.from`, `@0x48797e8`) | yes | 3.24.3 | `site_device_param_response.dart @0x4879698` |
| `mode_type` | `int?` | yes | 3.24.3 | `site_device_param_response.dart @0x48796c4` |
| `unit` | `String?` | yes | 3.24.3 | `site_device_param_response.dart @0x48797fc` |

## Produced by

[`get_site_device_param`](../api/power_service/site/get_site_device_param.md) with `param_type` 6, sender `getSiteDeviceParam` in `electricity_price/components/tou/impl_v2/service/tou_http_service.dart` (`@0x4879544`): `"6"` at `@0x4879590`, `cmd` raw 246 at `@0x48795a8` (decoded 123 in [param_types.md](../api/param_types.md)), converter closure at `@0x48795d0`, call `request()` at `@0x48795f4`.

## Consumed by

The TOU module callers of `TouHttpService.getSiteDeviceParam`; which pages read `use_time`, `mode_type` and `unit` was not traced.

## Changed since 3.18.0

New class in 3.24.3. The 3.18.0 asm has neither a class `SiteDeviceParamResponse` nor a `TouHttpService` (the 3.18.0 type-6 literal sites are listed by count in [param_types.md](../api/param_types.md)).

## Known unknowns

- The receiver of the `use_time` / `mode_type` / `unit` reads (see Fields).
- The element structure of `use_time` (the upstream-confirmed example for the related type 12, `api/schedule.py` lines 210-220, has `use_time[]` with `sea`, `weekday`, `weekend`, `weekday_price`, `weekend_price`, `unit`, `is_same`; whether the same shape applies to type 6 is not verified).
