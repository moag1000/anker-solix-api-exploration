> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# set_charging_vehicle

## Purpose

Assigns a vehicle to a running or finished charging order of an EV charger (the "change vehicle" action of the session screens).

## Upstream name

`vehicle_set_charging` (upstream-confirmed, `api/apitypes.py` line 161; upstream comment: " needs EV_Charger device, {\"vehicle_id\": vehicleId, \"device_sn\": deviceSn, \"transaction_id\": 1}").

## Method+URL

`POST /power_service/v1/app/vehicle/set_charging_vehicle` (asm-traced). Sender: `AKIotEVChargeCommand.setChargingVehicle` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x3948e9c`). The path literal has no leading slash (`@0x3948efc`), the method is the string `"POST"` (`@0x3948f14`), and the map keys `path`, `method`, `param` are stored at `@0x3948ef4`, `@0x3948f08`, `@0x3948f20`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x3948fe8`, call `@0x3948ff8`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#the-common-envelope), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, Object>` map of three pairs (`r2 = 12`, `@0x3948f30`).

| field | type | required | example | source |
|---|---|---|---|---|
| `transaction_id` | int | yes | `1` | `ev_charge_command.dart @0x3948f3c`; the argument is boxed with `BoxInt64Instr` (`@0x3948f4c`), unboxed int64 |
| `device_sn` | String | yes | `<device sn>` | `ev_charge_command.dart @0x3948f64` |
| `vehicle_id` | String | yes | `<vehicle id>` | `ev_charge_command.dart @0x3948f78`; a null argument is replaced by the empty string (`cmp w0, NULL` `@0x3948f88`, `r0 = ""` `@0x3948f90`) |

The same integer `transaction_id` is what [get_charging_order_detail](../order/get_charging_order_detail.md) sends. Sending an empty `vehicle_id` is how the app clears the assignment (inferred from the null-to-empty-string replacement; not confirmed).

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): `handle` is called without a type argument.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "transaction_id": 1, "device_sn": "<device sn>", "vehicle_id": "<vehicle id>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `A5190HomeLogic.changeChargingVehicle` (`ev_charger/src/ev_charger/page/home/a5190_home_logic.dart @0x3948bac`)
- `SessionsDetailLogic.changeChargingVehicle` (`ev_charger/src/ev_charger/page/home/charge_sessions/sessions_detail/sessions_detail_logic.dart @0x3959ce0`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x836b8`); the sender function has the same sequence of string, integer and type literals in 3.18.0 (compared with a throwaway script, not committed). Not new in 3.24.3: the Task 3.1b inventory change (slashless URL literals) made the URL visible, nothing changed in the app. 3.24.3: present, unchanged. since: ≤3.18.0.

## Known unknowns

- Whether an empty `vehicle_id` really clears the assignment is not confirmed.
- Upstream says the call needs an EV charger device; the server-side error for a missing one is not recorded.

## Device-tested by

none
