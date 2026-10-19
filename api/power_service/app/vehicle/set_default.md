> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# set_default

## Purpose

Marks one vehicle as the default vehicle of the account (the vehicle assumed for new charging orders).

## Upstream name

`vehicle_set_default` (upstream-confirmed, `api/apitypes.py` line 162; upstream comment: "set vehicle id as default, {\"vehicle_id\": vehicleId}").

## Method+URL

`POST /power_service/v1/app/vehicle/set_default` (asm-traced). Sender: `AKIotEVChargeCommand.setDefaultEv` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x3984aec`). The path literal has no leading slash (`@0x3984b74`), the method is the string `"POST"` (`@0x3984b8c`), and the map keys `path`, `method`, `param` are stored at `@0x3984b6c`, `@0x3984b80`, `@0x3984b98`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x3984bc0`, call `@0x3984bd0`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#the-common-envelope), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, String>` map of one pair (`r2 = 4`, `@0x3984b10`).

| field | type | required | example | source |
|---|---|---|---|---|
| `vehicle_id` | String | yes | `<vehicle id>` | `ev_charge_command.dart @0x3984b18` |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): `handle` is called without a type argument.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "vehicle_id": "<vehicle id>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `VehicleListLogic.setDefaultOnTap` (`ev_charger/src/ev_charger/page/vehicle/vehicle_list_logic.dart @0x3984a24`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x818c0`); the sender function has no literal difference between 3.18.0 and 3.24.3 (`tools/cmp_since.py`: ordered string, integer and type literals compared; branch logic not compared). Not new in 3.24.3: the inventory learned URL literals without a leading slash, which made the URL visible. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- How "default" is used by the server (for example for automatic vehicle assignment of new orders) is not known; the answer carries `is_default_vehicle` per vehicle.

## Device-tested by

none
