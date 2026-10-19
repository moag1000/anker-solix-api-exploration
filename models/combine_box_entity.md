> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# CombineBoxEntity

## Purpose

Carries the combiner box (power dock, AE100) of a site, as returned by `get_site_device_param` with `param_type` 16: the serial number and the image URL.

## Dart class + file

`CombineBoxEntity`, `charging/ui/page/device/main/sitation_energy_system/station_home_settings/manage_devices/CombineBoxEntity.dart` (package `charging`), fromJson `@0x237adb0`.

## Fields

Column `since`: `≤3.18.0` means the key is present in 3.18.0 (earlier versions not checked).

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `AE100` | `String?` | yes | ≤3.18.0 | `CombineBoxEntity.dart @0x237add4` |
| `id_img` | `String?` | yes | ≤3.18.0 | `CombineBoxEntity.dart @0x237ae40` |

The keys match the upstream-confirmed example (`api/schedule.py` lines 224-226, `SOLARBANK_POWERDOCK`).

## Produced by

[`get_site_device_param`](../api/power_service/site/get_site_device_param.md) with `param_type` 16: `getCombineBoxListData` (`http_request_repository_impl.dart @0x237a9e0`), success closure `@0x237aaf0` (reads `param_data`, `jsonDecode` `@0x237ac14`, `CombineBoxEntity.fromJson` `@0x237ac40`). The device is set with [`set_site_device_param`](../api/power_service/site/set_site_device_param.md) (`setCombineBoxDevice`, body `{"AE100": "<serial>"}`; see [param_types.md](../api/param_types.md)).

## Consumed by

`getCombinerBoxInfo` (`a17c1setting_logic.dart @0x3453c38`), `getCombineBoxList` (`manage_devices_logic.dart @0x3fc37f0`) and `station_energy_system_logic.dart` (call `@0x23757f4`). Field-level use is not traced.

## Changed since 3.18.0

No key added or removed (same two keys in 3.18.0).

## Known unknowns

- Whether the response can hold more than one combiner box (the function name says list; the model has no list field).
