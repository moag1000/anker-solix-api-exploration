> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# StationPowerLimitModel

## Purpose

Carries the station power limit state of a site as returned by `get_power_limit`: selectable output limits, the legal limit, per-device and AE100 info, and the settings of the "DIY" unlock prompt.

## Dart class + file

All four classes live in `station_power_limit_model.dart` (package `charging`, directory `ui/page/device/main/sitation_energy_system/station_home_settings/station_power_limit/`).

| class | role | fromJson |
|---|---|---|
| `StationPowerLimitModel` | response object | `@0x2379150` |
| `PowerLimitOption` | element of `power_limit_option` | `@0x237a428` |
| `DeviceInfo` | element of `device_info` | `@0x237a59c` |
| `Ae100Info` | value of `ae100_info` | `@0x237a18c` |

## Fields

Column `since`: `≤3.18.0` means the key is present in 3.18.0 (earlier versions not checked); `3.24.3` means the key is absent in 3.18.0 and present in 3.24.3 (versions in between not checked). Column `nullable`: `yes` where the asm casts to a nullable type or checks for null; `no` where it casts to a non-nullable type (a missing key would fail the cast).

### StationPowerLimitModel

Keys in `fromJson` order. Each value is read with `[]` and cast as listed; the parsed values are stored into fields 0x7 to 0x37 in the same order (`@0x237987c` to `@0x23798e4`).

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `site_id` | `String?` | yes | ≤3.18.0 | `station_power_limit_model.dart @0x23791d0` (cast `@0x2379220`) |
| `ac_input_power_unit` | `String?` | yes | ≤3.18.0 | `station_power_limit_model.dart @0x2379234` (cast `@0x2379284`) |
| `ac_input_power` | `int?` | yes | 3.24.3 | `station_power_limit_model.dart @0x2379298` (cast `@0x23792e4`) |
| `legal_power_limit` | `int?` | yes | ≤3.18.0 | `station_power_limit_model.dart @0x23792f8` (cast `@0x2379344`) |
| `parallel_type` | `String?` | yes | ≤3.18.0 | `station_power_limit_model.dart @0x2379358` (cast `@0x23793a8`) |
| `ae100_info` | `Ae100Info?` (from `Map<String, dynamic>`) | yes (null check `@0x23793e0`) | ≤3.18.0 | `station_power_limit_model.dart @0x23793bc`, parsed by `Ae100Info.fromJson` at `@0x2379438` |
| `device_info` | `List<DeviceInfo>` (from `List?`) | no (null or missing gives an empty list, `@0x2379544`) | ≤3.18.0 | `station_power_limit_model.dart @0x237944c` (cast `@0x237949c`) |
| `legal_limit` | `int?` | yes | ≤3.18.0 | `station_power_limit_model.dart @0x237955c` (cast `@0x23795a8`) |
| `power_limit_option` | `List<PowerLimitOption>` (from `List?`) | no (null or missing gives an empty list, `@0x23796b4`) | ≤3.18.0 | `station_power_limit_model.dart @0x23795bc` (cast `@0x237960c`) |
| `exceed_alarm` | `bool?` | yes | ≤3.18.0 | `station_power_limit_model.dart @0x23796f8` (cast `@0x2379744`) |
| `unlock_default_power_type` | `int?` | yes | 3.24.3 | `station_power_limit_model.dart @0x2379758` (cast `@0x23797a4`) |
| `unlock_pop_content` | `String?` | yes | 3.24.3 | `station_power_limit_model.dart @0x23797b8` (cast `@0x2379808`) |
| `unlock_pop_image` | `String?` | yes | 3.24.3 | `station_power_limit_model.dart @0x237981c` (cast `@0x237986c`) |

### PowerLimitOption

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `limit` | `int` | no | ≤3.18.0 | `station_power_limit_model.dart @0x237a454` (cast `@0x237a490`), stored unboxed (`@0x237a514`) |
| `limit_real` | `int` | no | ≤3.18.0 | `station_power_limit_model.dart @0x237a4ac` (cast `@0x237a4e8`), stored unboxed (`@0x237a528`) |

### DeviceInfo

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `device_sn` | `String` | no | ≤3.18.0 | `station_power_limit_model.dart @0x237a5c8` (cast `@0x237a608`) |
| `device_pn` | `String` | no | ≤3.18.0 | `station_power_limit_model.dart @0x237a628` (cast `@0x237a668`) |
| `device_name` | `String` | no | ≤3.18.0 | `station_power_limit_model.dart @0x237a688` (cast `@0x237a6c8`) |
| `device_img` | `String` | no | ≤3.18.0 | `station_power_limit_model.dart @0x237a6e8` (cast `@0x237a728`) |
| `status` | `int` | no | ≤3.18.0 | `station_power_limit_model.dart @0x237a748` (cast `@0x237a784`) |
| `ac_input_limit` | `dynamic`, stored as the String `"<value>W"` | yes (null becomes 0, i.e. `"0W"`; raw 0 at `@0x237a7bc`, the same under the Smi rule) | ≤3.18.0 | `station_power_limit_model.dart @0x237a7a0`, formatted at `@0x237a808` |

`DeviceInfo.fromJson` also sets two fields that are not read from JSON: the String `"Auto"` (`@0x237a850`) and `false` (`@0x237a85c`).

### Ae100Info

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `device_sn` | `String` | no | ≤3.18.0 | `station_power_limit_model.dart @0x237a1b8` (cast `@0x237a1f8`) |
| `device_pn` | `String` | no | ≤3.18.0 | `station_power_limit_model.dart @0x237a218` (cast `@0x237a258`) |
| `device_name` | `String` | no | ≤3.18.0 | `station_power_limit_model.dart @0x237a278` (cast `@0x237a2b8`) |
| `device_img` | `String` | no | ≤3.18.0 | `station_power_limit_model.dart @0x237a2d8` (cast `@0x237a318`) |
| `status` | `int` | no | ≤3.18.0 | `station_power_limit_model.dart @0x237a334` (cast `@0x237a370`) |

## Produced by

[`get_power_limit`](../api/power_service/site/get_power_limit.md), success closure `http_request_repository_impl.dart @0x23790e0`.

## Consumed by

Station power limit page, `StationPowerLimitLogic` success closure of `_getStationPowerLimit` (`station_power_limit_logic.dart @0x28cacc4`) and the output power picker:

- `legal_limit` (null becomes 0, `@0x28cad98`) is stored as the threshold above which the DIY unlock prompt appears (`@0x28cad88`); see [../flows/system_output_limit.md](../flows/system_output_limit.md).
- `legal_power_limit` is formatted as `"<value>W"` and stored as the displayed current output limit (`@0x28cadec`); the picker parses it back as the slider start value.
- `exceed_alarm` (null becomes `false`) is stored at `@0x28cae74`.
- `power_limit_option` is mapped to the strings `"<limit>W"` by `_updatePowerLimitList` (`@0x28cba8c`, closure `@0x28cbb88`); the last entry becomes the slider maximum.
- `unlock_default_power_type`, `unlock_pop_image` and `unlock_pop_content` are read when the DIY prompt is built (`@0x435536c`, `@0x4355428`, `@0x4355478`).
- `device_info` is used by `_calibrateDeviceStatus` (`@0x28cb60c`).

The A17C1 energy plan page (`EnergyPlanLogic::getStationPowerLimit`, `energy_plan_logic.dart`) also requests this model; its use there is not traced.

## Changed since 3.18.0

Compared with 3.18.0 `StationPowerLimitModel.fromJson` (3.18.0 `station_power_limit_model.dart @0x1a56c9c`, 9 keys):

- added: `ac_input_power`
- added: `unlock_default_power_type`
- added: `unlock_pop_content`
- added: `unlock_pop_image`

No key was removed. `PowerLimitOption`, `DeviceInfo` and `Ae100Info` read the same keys with the same casts in both versions.

## Known unknowns

- The difference in meaning between `legal_power_limit` and `legal_limit`. By usage, `legal_power_limit` seeds the displayed current output limit and `legal_limit` is the prompt threshold; the server-side definition is not known.
- The meaning and unit of `ac_input_power` (not read by the station power limit page).
- The value set of `unlock_default_power_type`: the app maps 1 and 2 to two prompt variants and everything else to a third, see [../flows/system_output_limit.md](../flows/system_output_limit.md); which values the server sends is not known.
- The value set of `parallel_type` and `DeviceInfo.status`.
