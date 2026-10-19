> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# remove_user_floating_fault_info

## Purpose

Dismisses ("closes") one or more floating fault messages of an EV charger on the app's home screen by serial number and fault ids.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /charging_imsg_svc/remove_user_floating_fault_info` (asm-traced). Sender: `AKIotEVChargeCommand.removeUserFloatingFaultInfo` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x3219f88`). The path literal has no leading slash (`@0x3219fe4`), the method is the string `"POST"` (`@0x3219ffc`), and the map keys `path`, `method`, `param` are stored at `@0x3219fdc`, `@0x3219ff0`, `@0x321a008`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x321a098`, call `@0x321a0a8`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../sdk_senders.md](../sdk_senders.md#the-common-envelope), background: [../encryption.md](../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, Object>` map of two pairs (`r2 = 8`, `@0x321a018`).

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | String | yes | `<device sn>` | `ev_charge_command.dart @0x321a020` |
| `faultIds` | list (element type not shown) | yes | `[ 1 ]` | `ev_charge_command.dart @0x321a034`; second argument, passed through unchanged |

The caller is `closeErrorMsg` of the fault-info widget; the type of the ids (`A5190FaultInfoModel` rows carry an integer `id`, `a5190_fault_info_model.dart @0x2705ca0`) is inferred, not traced.

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): `handle` is called without a type argument.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "sn": "<device sn>", "faultIds": [1] }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `_A5190FaultInfoWidgetState.closeErrorMsg` (`ev_charger/src/ev_charger/page/home/widget/a5190_fault_info_widget.dart @0x3219f20`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0xf0ac0`); the sender function has the same sequence of string, integer and type literals in 3.18.0 (compared with a throwaway script, not committed). Not new in 3.24.3: the Task 3.1b inventory change (slashless URL literals) made the URL visible, nothing changed in the app. 3.24.3: present, unchanged. since: ≤3.18.0.

## Known unknowns

- The type of the elements of `faultIds` is not read in the sender (UNCONFIRMED integer ids).
- Whether the fault is only hidden in the app or cleared server-side is not known.

## Device-tested by

none
