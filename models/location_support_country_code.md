> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# LocationSupportCountryCode

## Purpose

Carries one supported country of the location feature (an app country code and the matching Google code); it belongs to the location support response, not to the `param_type` 20 country code of `get_site_device_param`.

## Dart class + file

`LocationSupportCountryCode`, `device/src/station_setting/controller/common_station_location/location_util_mixin.dart` (package `device`), fromJson `@0x3671878`. The class is the element type of `LocationSupportFunc.support_country_code` (`LocationSupportFunc.fromJson` `@0x367161c`: key `support_country_code` `@0x3671690`, element list built with type argument `@0x3671750`, `LocationSupportCountryCode.fromJson` called at `@0x36717d8`).

## Fields

The class does not exist in 3.18.0 (no class of this name in the 3.18.0 asm), so every key is `3.24.3`.

### LocationSupportCountryCode

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `code` | `String?` | yes | 3.24.3 | `location_util_mixin.dart @0x3671894` |
| `google_code` | `String?` | yes | 3.24.3 | `location_util_mixin.dart @0x36718f4` |

### LocationSupportFunc (the container)

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `support_auto_disaster` | `bool?` | yes | 3.24.3 | `location_util_mixin.dart @0x3671638` |
| `support_country_code` | `List<LocationSupportCountryCode>` (the extractor reports `int` for the first read, `@0x367173c`; the elements are parsed at `@0x36717d8`) | yes | 3.24.3 | `location_util_mixin.dart @0x3671690` |

## Produced by

Not linked to an endpoint: the request of the location feature is made by `LocationFetchedData._request` (`location_util_mixin.dart @0x2cbae54`) and the URL is not a literal in that function, so the rule "model to endpoint only through a same-function URL literal" does not give a link. The inventory lists `/charging_common_svc/location/support` ([support](../api/charging_common_svc/location/support.md)) as a candidate source; the asm does not support it: that URL is parsed with `SupportLocation` (key `country_code`), not with `LocationSupportFunc`. `get_site_device_param` with `param_type` 20 (see [param_types.md](../api/param_types.md)) does not produce this model: its GET response is read as a single `country_code` String.

## Consumed by

The location pages of the station settings (`LocationFetchedData.refreshData`, `location_util_mixin.dart @0x3672640`); field use is not traced.

## Changed since 3.18.0

New in 3.18.0 to 3.24.3: the class and its container `LocationSupportFunc` do not exist in the 3.18.0 asm.

## Known unknowns

- Which endpoint fills `LocationSupportFunc`: not decided — traced 2026-10-20: the URL literal `/charging_common_svc/location/support` appears at two sites and both parse a different container, `SupportLocation` (key `country_code`; `charging/http/http_request_repository_impl.dart @0x2892f0c` with `SupportLocation.fromJson` `@0x2892f88`, and `ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a2fbe8`), whose keys differ from the keys of `LocationSupportFunc` (`support_auto_disaster`, `support_country_code`); `location_util_mixin.dart` contains no URL literal and no `LocationFetchedData` construction appears outside that file in the dump, so the candidate named in Produced by is not supported by the asm.
- Whether `code` is the ISO 3166 alpha-2 code that is written as `country_code` in `param_type` 20 (see [param_types.md](../api/param_types.md)); not verified.
