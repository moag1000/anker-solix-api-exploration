> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# EV charger vehicle models

## Purpose

Carries the vehicles of an account (list, detail) as the EV charger app shows and edits them, and the schedule-charge view of the same vehicles.

## Dart class + file

`EvListModel` (`ev_charger/src/ev_charger/model/vehicle_model.dart`); `EvListInfoModel` (`ev_charger/src/ev_charger/model/vehicle_model.dart`); `VehicleModel` (`ev_charger/src/ev_charger/model/vehicle_model.dart`); `ScheduleVehicleModel` (`ev_charger/src/ev_charger/page/home/schedule_charge/models/schedule_vehicle_model.dart`); `VehicleDetail` (`ev_charger/src/ev_charger/page/home/schedule_charge/models/schedule_vehicle_model.dart`). `fromJson` addresses are under each class below.

## Fields

Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Dart types and nullability come from `tools/model_fields.py` (`data/models.json`); an "of `X`" note is the list element class read from the `<X>` type argument next to the key. The top-level answer classes are registered in `AnkerJsonUtils.initAnkerModelSerializable` (`ev_charger_json_factory.internal.dart @0x45ab020`, see [../api/sdk_senders.md](../api/sdk_senders.md#response-typing-and-the-model-registry)); where a top-level class lists `data` as its first field, that field is the wrapper: if `json["data"]` is a String, `fromJson` decodes it with `jsonDecode`, otherwise the map itself is read.

### EvListModel

Answer of `get_vehicle_list` (charging session and vehicle pages).

`fromJson` `vehicle_model.dart @0x45abe7c`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `data` | `String` (wrapper, decoded as described above) | yes | ≤3.18.0 | `vehicle_model.dart @0x45abeb8` |
| `vehicle_list` | `unknown` of `EvListInfoModel` | ? | ≤3.18.0 | `vehicle_model.dart @0x45abfd8` |

### EvListInfoModel

One vehicle in `EvListModel.vehicle_list`.

`fromJson` `vehicle_model.dart @0x45ab7ac`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `vehicle_id` | `String?` | yes | ≤3.18.0 | `vehicle_model.dart @0x45ab7cc` |
| `brand` | `String?` | yes | ≤3.18.0 | `vehicle_model.dart @0x45ab854` |
| `model` | `String?` | yes | ≤3.18.0 | `vehicle_model.dart @0x45ab8dc` |
| `vehicle_name` | `String?` | yes | ≤3.18.0 | `vehicle_model.dart @0x45ab964` |
| `productive_year` | `num` | no | ≤3.18.0 | `vehicle_model.dart @0x45ab9ec` |
| `is_default_vehicle` | `bool?` | yes | ≤3.18.0 | `vehicle_model.dart @0x45aba98` |
| `is_smart_charging` | `bool?` | yes | ≤3.18.0 | `vehicle_model.dart @0x45abb04` |
| `is_connected_to_enodeapi` | `bool?` | yes | ≤3.18.0 | `vehicle_model.dart @0x45abb70` |
| `update_time` | `num?` | yes | ≤3.18.0 | `vehicle_model.dart @0x45abbdc` |
| `soc` | `num?` | yes | ≤3.18.0 | `vehicle_model.dart @0x45abc9c` |
| `battery_capacity` | `num?` | yes | ≤3.18.0 | `vehicle_model.dart @0x45abd5c` |

### VehicleModel

Answer of `get_vehicle_detail`; also the shape the app sends back to `update_vehicle` (`toJson`).

`fromJson` `vehicle_model.dart @0x32227f0`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `data` | `String` (wrapper, decoded as described above) | yes | ≤3.18.0 | `vehicle_model.dart @0x3222810` |
| `vehicle_name` | `String?` | yes | ≤3.18.0 | `vehicle_model.dart @0x32228fc` |
| `brand` | `String?` | yes | ≤3.18.0 | `vehicle_model.dart @0x3222984` |
| `model` | `String?` | yes | ≤3.18.0 | `vehicle_model.dart @0x3222a0c` |
| `productive_year` | `num?` | yes | ≤3.18.0 | `vehicle_model.dart @0x3222a94` |
| `battery_capacity` | `num?` | yes | ≤3.18.0 | `vehicle_model.dart @0x3222b54` |
| `ac_max_charging_power` | `num?` | yes | ≤3.18.0 | `vehicle_model.dart @0x3222c10` |
| `energy_consumption_per_100km` | `num?` | yes | ≤3.18.0 | `vehicle_model.dart @0x3222ccc` |
| `enode_vehicle_id` | `String?` | yes | ≤3.18.0 | `vehicle_model.dart @0x3222d88` |
| `vehicle_id` | `String?` | yes | ≤3.18.0 | `vehicle_model.dart @0x3222e10` |

### ScheduleVehicleModel

Answer of `get_vehicle_list` as parsed by the schedule-charge feature (`ScheduleNetwork.getVehicleList`).

`fromJson` `schedule_vehicle_model.dart @0x284ed3c`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `vehicle_list` | `Iterable` of `VehicleDetail` | no | ≤3.18.0 | `schedule_vehicle_model.dart @0x284ed60` |

### VehicleDetail

One vehicle in `ScheduleVehicleModel.vehicle_list`.

`fromJson` `schedule_vehicle_model.dart @0x284f1d0`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `vehicle_id` | `String?` | yes | ≤3.18.0 | `schedule_vehicle_model.dart @0x284f1fc` |
| `vehicle_name` | `String?` | yes | ≤3.18.0 | `schedule_vehicle_model.dart @0x284f25c` |
| `brand` | `String?` | yes | ≤3.18.0 | `schedule_vehicle_model.dart @0x284f2bc` |
| `model` | `String?` | yes | ≤3.18.0 | `schedule_vehicle_model.dart @0x284f31c` |
| `productive_year` | `int?` | yes | ≤3.18.0 | `schedule_vehicle_model.dart @0x284f37c` |
| `is_default_vehicle` | `bool?` | yes | ≤3.18.0 | `schedule_vehicle_model.dart @0x284f3d8` |
| `is_smart_charging` | `bool?` | yes | ≤3.18.0 | `schedule_vehicle_model.dart @0x284f434` |
| `is_connected_to_enodeapi` | `bool?` | yes | ≤3.18.0 | `schedule_vehicle_model.dart @0x284f490` |
| `update_time` | `int?` | yes | ≤3.18.0 | `schedule_vehicle_model.dart @0x284f4ec` |
| `battery_capacity` | `num?` | yes | ≤3.18.0 | `schedule_vehicle_model.dart @0x284f548` |
| `soc` | `int?` | yes | ≤3.18.0 | `schedule_vehicle_model.dart @0x284f608` |

## Produced by

- [`get_vehicle_list`](../api/power_service/app/vehicle/get_vehicle_list.md): `EvListModel` (command-map sender) and `ScheduleVehicleModel` (`ScheduleNetwork` sender)
- [`get_vehicle_detail`](../api/power_service/app/vehicle/get_vehicle_detail.md): `VehicleModel`
- [`update_vehicle`](../api/power_service/app/vehicle/update_vehicle.md) and [`add_vehicle`](../api/power_service/app/vehicle/add_vehicle.md): accept the keys of `VehicleModel.toJson` (see the endpoint pages)

## Consumed by

Vehicle list, vehicle edit and add-vehicle pages of the `ev_charger` package and the schedule-charge driving plan (see "Callers in app" of the endpoint pages); field-level use is not traced.

## Changed since 3.18.0

All classes are present in 3.18.0 (`since` column); no key is new in 3.24.3 and the tool reports no removed keys.

## Known unknowns

- `productive_year`, `battery_capacity` and the other `num` fields are `num` in Dart; the wire type (integer or decimal) is not known.
- The `toJson` of `VehicleModel` has nine keys (`vehicle_name`, `brand`, `model`, `productive_year`, `battery_capacity`, `ac_max_charging_power`, `energy_consumption_per_100km`, `enode_vehicle_id`, `vehicle_id`; `vehicle_model.dart @0x2ab4d98` to `@0x2ab4e5c`); which of them the server requires is not known.
- `enode_vehicle_id` and `is_connected_to_enodeapi` suggest a link to the Enode vehicle API; the flow that sets them is not traced.
