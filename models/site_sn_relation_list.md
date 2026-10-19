> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# SiteSnRelationList

## Purpose

Carries the answer of `get_hardware_relation`: a list of entries that tie device serial numbers to the sites they belong to.

## Dart class + file

`SiteSnRelationList` (`fromJson @0x22a67f8`), `SiteSnRelationInfoMap` (`@0x22a697c`) and `SiteSnRelationItem` (`@0x22a6b0c`), file `base_service/ak_iot_kit/business/basic/model/station_device_relation.dart` (package `base_service`). The same file also holds `DeviceRelationRemoteEvent` (`@0x33c95b8`, keys `pn`, `sn`, `site_id`, `site_name`, `related_pn`, `related_sn`, `related_site_id`, `related_site_name`, `status`), a push-event class that is not part of this answer.

## Fields

Column `since`: `≤3.18.0` means the key is present in 3.18.0 (earlier versions not checked), `3.24.3` means first seen in 3.24.3. Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Nullability and Dart types come from `tools/model_fields.py` (`data/models.json`); `unknown` means the extractor could not resolve the element type.

### SiteSnRelationList

`fromJson` `station_device_relation.dart @0x22a67f8`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `list` | `List` | no | ≤3.18.0 | `station_device_relation.dart @0x22a6820` |

### SiteSnRelationInfoMap

`fromJson` `station_device_relation.dart @0x22a697c`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `sn_site_infos` | `List` | no | ≤3.18.0 | `station_device_relation.dart @0x22a69a4` |

### SiteSnRelationItem

`fromJson` `station_device_relation.dart @0x22a6b0c`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `site_id` | `String?` | yes | ≤3.18.0 | `station_device_relation.dart @0x22a6b38` |
| `site_name` | `String?` | yes | ≤3.18.0 | `station_device_relation.dart @0x22a6b98` |
| `pn` | `String?` | yes | ≤3.18.0 | `station_device_relation.dart @0x22a6bf8` |
| `sn` | `String?` | yes | ≤3.18.0 | `station_device_relation.dart @0x22a6c58` |
| `is_main` | `bool?` | yes | ≤3.18.0 | `station_device_relation.dart @0x22a6cb4` |

The element type of `list` is `SiteSnRelationInfoMap` and that of `sn_site_infos` is `SiteSnRelationItem` by name and file (the list parse was not traced).

## Produced by

[`get_hardware_relation`](../api/power_service/v2/app/get_hardware_relation.md): `SiteSnRelationList.fromJson` at `base_service/ak_iot_kit/business/basic/model/station_device_relation.dart @0x22a4bcc` in the success closure `@0x22a4ab8` of `DeviceRelationMgr.requestHardwareRelation`.

## Consumed by

`DeviceRelationMgr` stores the parsed list in `relationInfoList` (`@0x22a4bd8`); consumers of that field were not traced.

## Changed since 3.18.0

No key was added or removed between 3.18.0 and 3.24.3 (all keys `≤3.18.0`); the endpoint itself exists in 3.18.0.

## Known unknowns

- Upstream saw an empty list for its test account; the contents for accounts with several sites are not documented.
