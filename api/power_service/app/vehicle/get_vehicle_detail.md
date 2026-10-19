> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_vehicle_detail

## Purpose

Reads one vehicle of the account (name, brand, model, year, battery capacity, AC charging power, consumption, Enode id) for the vehicle edit page.

## Upstream name

`get_user_vehicle_details` (upstream-confirmed, `api/apitypes.py` line 157; upstream comment: "details for given vehicle id, {\"vehicle_id\": vehicleId}").

## Method+URL

`POST /power_service/v1/app/vehicle/get_vehicle_detail` (asm-traced). Sender: `AKIotEVChargeCommand.getEvDetail` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x2ab935c`). The path literal has no leading slash (`@0x2ab93e4`), the method is the string `"POST"` (`@0x2ab93fc`), and the map keys `path`, `method`, `param` are stored at `@0x2ab93dc`, `@0x2ab93f0`, `@0x2ab9408`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x2ab9438`, call `@0x2ab9448`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#the-common-envelope), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, String>` map of one pair (`r2 = 4`, `@0x2ab9380`).

| field | type | required | example | source |
|---|---|---|---|---|
| `vehicle_id` | String | yes | `<vehicle id>` | `ev_charge_command.dart @0x2ab9388` |

## `param_type`/`cmd`

n/a

## Response model (link)

`VehicleModel` ([../../../../models/ev_charger_vehicle_models.md](../../../../models/ev_charger_vehicle_models.md#vehiclemodel)), taken from the type argument of `handle<VehicleModel>` (ev_charge_command.dart `@0x2ab9428`)

## Response

The SDK result is typed `IoTAKResult<VehicleModel>`; the keys are on the model page. The wrapper `data` of `VehicleModel.fromJson` is described there. The caller reads the result type before using the data.

| field | type | required | example | source |
|---|---|---|---|---|
| `data` | String (JSON text) or map | no |  | `vehicle_model.dart @0x3222810` |
| `vehicle_name`, `brand`, `model`, `productive_year`, `battery_capacity`, `ac_max_charging_power`, `energy_consumption_per_100km`, `enode_vehicle_id`, `vehicle_id` | see model page | no |  | [../../../../models/ev_charger_vehicle_models.md](../../../../models/ev_charger_vehicle_models.md#vehiclemodel) |

## Example request/response

Request, synthesized

```json
{ "vehicle_id": "<vehicle id>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `VehicleEditLogic.getVehicleDetail` (`ev_charger/src/ev_charger/page/vehicle/vehicle_edit_logic.dart @0x2ab9278`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0xbde80`); the sender function has no literal difference between 3.18.0 and 3.24.3 (`tools/cmp_since.py`: ordered string, integer and type literals compared; branch logic not compared). Not new in 3.24.3: the inventory learned URL literals without a leading slash, which made the URL visible. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- No response was captured.

## Device-tested by

none
