> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# add_vehicle

## Purpose

Adds one or more vehicles to the account (the add-vehicle wizard of the EV charger app).

## Upstream name

`vehicle_add` (upstream-confirmed, `api/apitypes.py` line 158; upstream comment: "add vehicles to account, {\"user_vehicle_info\": [{\"vehicle_name\": \"MyCar\",\"brand\": \"Audi\",\"model\": \"eTron\",\"productive_year\": 2024}]}").

## Method+URL

`POST /power_service/v1/app/vehicle/add_vehicle` (asm-traced). Sender: `AKIotEVChargeCommand.addEv` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x3983e74`). The path literal has no leading slash (`@0x3983efc`), the method is the string `"POST"` (`@0x3983f14`), and the map keys `path`, `method`, `param` are stored at `@0x3983ef4`, `@0x3983f08`, `@0x3983f20`. This is the only literal of the command class with a leading slash (`"/power_service/v1/app/vehicle/add_vehicle"`).

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x3983f48`, call `@0x3983f58`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#the-common-envelope), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a map of one pair, `user_vehicle_info`, whose value is the sender's argument (`r2 = 4`, `@0x3983e98`).

| field | type | required | example | source |
|---|---|---|---|---|
| `user_vehicle_info` | list of map | yes | `[ { "vehicle_name": "MyCar", "brand": "Audi", "model": "eTron", "productive_year": 2024 } ]` | `ev_charge_command.dart @0x3983ea0`; the caller `VehicleEditLogic.saveOnTap` builds it by mapping an observable list through a closure and `toList` (`vehicle_edit_logic.dart @0x3983a9c` to `@0x3983ac8`, `addEv` call `@0x3983ae0`) |

The element keys are most probably the nine keys of `VehicleModel.toJson` (`vehicle_name`, `brand`, `model`, `productive_year`, `battery_capacity`, `ac_max_charging_power`, `energy_consumption_per_100km`, `enode_vehicle_id`, `vehicle_id`; [model page](../../../../models/ev_charger_vehicle_models.md#vehiclemodel)); the closure body was not read (UNCONFIRMED). Upstream sends four of them.

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): `handle` is called without a type argument (`stp x16, NULL`); the caller only compares the result type with an `AKResultType` instance (`vehicle_edit_logic.dart @0x3983b24` to `@0x3983b2c`) and then returns to the list page (`@0x3983b40`) or shows a failure toast (`@0x3983b88`).

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "user_vehicle_info": [ { "vehicle_name": "MyCar", "brand": "Audi", "model": "eTron", "productive_year": 2024 } ] }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `VehicleEditLogic.saveOnTap` (`ev_charger/src/ev_charger/page/vehicle/vehicle_edit_logic.dart @0x3983ae0`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x819f8 (with the leading slash)`); the sender function has the same sequence of string, integer and type literals in 3.18.0 (compared with a throwaway script, not committed). Not new in 3.24.3: the Task 3.1b inventory change (slashless URL literals) made the URL visible, nothing changed in the app. 3.24.3: present, unchanged. since: ≤3.18.0.

## Known unknowns

- The element map of `user_vehicle_info` is built by a closure whose body was not read; the key set is inferred from `VehicleModel.toJson` and from upstream.
- Which keys the server requires is not known.

## Device-tested by

none
