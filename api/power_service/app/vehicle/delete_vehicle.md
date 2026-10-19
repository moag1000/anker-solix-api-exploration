> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# delete_vehicle

## Purpose

Deletes one vehicle from the account.

## Upstream name

`vehicle_delete` (upstream-confirmed, `api/apitypes.py` line 160; upstream comment: no comment on this entry).

## Method+URL

`POST /power_service/v1/app/vehicle/delete_vehicle` (asm-traced). Sender: `AKIotEVChargeCommand.deleteEv` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x398389c`). The path literal has no leading slash (`@0x3983924`), the method is the string `"POST"` (`@0x398393c`), and the map keys `path`, `method`, `param` are stored at `@0x398391c`, `@0x3983930`, `@0x3983948`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x3983970`, call `@0x3983980`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#the-common-envelope), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, String>` map of one pair (`r2 = 4`, `@0x39838c0`).

| field | type | required | example | source |
|---|---|---|---|---|
| `vehicle_id` | String | yes | `<vehicle id>` | `ev_charge_command.dart @0x39838c8` |

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

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `VehicleEditLogic._doDelete` (`ev_charger/src/ev_charger/page/vehicle/vehicle_edit_logic.dart @0x3983734`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x819d0`); the sender function has the same sequence of string, integer and type literals in 3.18.0 (compared with a throwaway script, not committed). Not new in 3.24.3: the Task 3.1b inventory change (slashless URL literals) made the URL visible, nothing changed in the app. 3.24.3: present, unchanged. since: ≤3.18.0.

## Known unknowns

- What happens to orders that reference the deleted vehicle is not known.

## Device-tested by

none
