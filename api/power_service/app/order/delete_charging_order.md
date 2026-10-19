> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# delete_charging_order

## Purpose

Deletes one charging order of an EV charger from the account's history.

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (line 294, docstring list of endpoints "neither implemented nor explored"); the comment there (no comment on this entry) is the upstream author's note, not a test result.

## Method+URL

`POST /power_service/v1/app/order/delete_charging_order` (asm-traced). Sender: `AKIotEVChargeCommand.deleteChargingSession` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x395b4e4`). The path literal has no leading slash (`@0x395b540`), the method is the string `"POST"` (`@0x395b558`), and the map keys `path`, `method`, `param` are stored at `@0x395b538`, `@0x395b54c`, `@0x395b564`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x395b5f4`, call `@0x395b604`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#the-common-envelope), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, String>` map of two pairs (`r2 = 8`, `@0x395b574`).

| field | type | required | example | source |
|---|---|---|---|---|
| `order_id` | String | yes | `<order id>` | `ev_charge_command.dart @0x395b57c` |
| `device_sn` | String | yes | `<device sn>` | `ev_charge_command.dart @0x395b590` |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): `handle` is called without a type argument (`stp x16, NULL`, `@0x395b5f0`); no model is parsed.

## Response

The sender returns the untyped `IoTAKResult`; the caller listed below receives it. What the answer body contains is not read by this sender.

## Example request/response

Request, synthesized

```json
{ "order_id": "<order id>", "device_sn": "<device sn>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `SessionsDetailLogic._performDeleteSession` (`ev_charger/src/ev_charger/page/home/charge_sessions/sessions_detail/sessions_detail_logic.dart @0x395b15c`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x83520`); the sender function has no literal difference between 3.18.0 and 3.24.3 (`tools/cmp_since.py`: ordered string, integer and type literals compared; branch logic not compared). Not new in 3.24.3: the inventory learned URL literals without a leading slash, which made the URL visible. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- Whether the deletion is permanent and whether a charger-side record also disappears is not known.
- How the caller reacts to a failure result was not read.

## Device-tested by

none
