> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# update_vehicle

## Purpose

Changes the details of one vehicle of the account (name, brand, model, year, battery capacity, AC charging power, consumption).

## Upstream name

`vehicle_update` (upstream-confirmed, `api/apitypes.py` line 159; upstream comment: "update any vehicle detail, {\"vehicle_id\": vehicleId, \"vehicle_name\": \"MyCar\",\"brand\": \"Audi\",\"model\": \"eTron\",\"productive_year\": 2024, \"battery_capacity\": 80, \"ac_max_charging_power\": 11, \"energy_consumption_per_100km\": 18}").

## Method+URL

`POST /power_service/v1/app/vehicle/update_vehicle` (asm-traced). Sender: `AKIotEVChargeCommand.updateEv` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x2cf9cb0`). The path literal has no leading slash (`@0x2cf9d04`), the method is the string `"POST"` (`@0x2cf9d1c`), and the map keys `path`, `method`, `param` are stored at `@0x2cf9cfc`, `@0x2cf9d10`, `@0x2cf9d28`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x2cf9d50`, call `@0x2cf9d60`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#the-common-envelope), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is the map passed to the command function unchanged (`ev_charge_command.dart @0x2cf9d34`). The caller `VehicleEditLogic.updateEv` (`ev_charger/src/ev_charger/page/vehicle/vehicle_edit_logic.dart @0x43e1be0`) builds it from `VehicleModel.fromJson`, `copyWithEv` (`@0x43e1c54`) and `VehicleModel.toJson` (`@0x43e1c5c`), then sets `vehicle_id` with `[]=` (key `@0x43e1c8c`, call `@0x43e1c94`). The keys are therefore those of `VehicleModel.toJson` (`vehicle_model.dart @0x2ab4d98` to `@0x2ab4e5c`):

| field | type | required | example | source |
|---|---|---|---|---|
| `vehicle_id` | String | yes | `<vehicle id>` | `vehicle_edit_logic.dart @0x43e1c8c` (set last, overwrites the value from `toJson`; `vehicle_model.dart @0x2ab4e5c`) |
| `vehicle_name` | String? | no | `MyCar` | `vehicle_model.dart @0x2ab4d98` |
| `brand` | String? | no | `Audi` | `vehicle_model.dart @0x2ab4db4` |
| `model` | String? | no | `eTron` | `vehicle_model.dart @0x2ab4dcc` |
| `productive_year` | num? | no | `2024` | `vehicle_model.dart @0x2ab4de4` |
| `battery_capacity` | num? | no | `80` | `vehicle_model.dart @0x2ab4dfc` |
| `ac_max_charging_power` | num? | no | `11` | `vehicle_model.dart @0x2ab4e14` |
| `energy_consumption_per_100km` | num? | no | `18` | `vehicle_model.dart @0x2ab4e2c` |
| `enode_vehicle_id` | String? | no | `null` | `vehicle_model.dart @0x2ab4e44` |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): `handle` is called without a type argument; after the call the editor pops to the edit page and reloads the vehicle with `getVehicleDetail` (`vehicle_edit_logic.dart @0x43e1d30`, `@0x43e1d58`) when the result type is the success instance.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "vehicle_id": "<vehicle id>", "vehicle_name": "MyCar", "brand": "Audi", "model": "eTron", "productive_year": 2024, "battery_capacity": 80, "ac_max_charging_power": 11, "energy_consumption_per_100km": 18 }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- an anonymous closure in `VehicleEditLogic` (`ev_charger/src/ev_charger/page/vehicle/vehicle_edit_logic.dart @0x2cf9b08`)
- `VehicleEditLogic.updateEv` (`ev_charger/src/ev_charger/page/vehicle/vehicle_edit_logic.dart @0x43e1ccc`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0xbde88`); the sender function has no literal difference between 3.18.0 and 3.24.3 (`tools/cmp_since.py`: ordered string, integer and type literals compared; branch logic not compared). Not new in 3.24.3: the Task 3.1b inventory change (slashless URL literals) made the URL visible. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- Whether `toJson` writes `null` for unset fields or leaves the keys out was not read.
- The `num` fields may be sent as integers or decimals; not known.

## Device-tested by

none
