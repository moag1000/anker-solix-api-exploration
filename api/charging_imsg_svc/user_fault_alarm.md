> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# user_fault_alarm

## Purpose

Sends the fault bit array of an EV charger to the message service together with the device serial, product code, a fixed type id and the local time; the fault-info widget of the charger home screen calls it when it parses fault info (the name suggests it raises or records a fault alarm for the user).

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /charging_imsg_svc/user_fault_alarm` (asm-traced). Sender: `AKIotEVChargeCommand.userFaultAlarm` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x2c67d64`). The path literal has no leading slash (`@0x2c67dc4`), the method is the string `"POST"` (`@0x2c67ddc`), and the map keys `path`, `method`, `param` are stored at `@0x2c67dbc`, `@0x2c67dd0`, `@0x2c67de8`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x2c67f3c`, call `@0x2c67f4c`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../sdk_senders.md](../sdk_senders.md#the-common-envelope), background: [../encryption.md](../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, Object>` map of six pairs (`r2 = 24`, `@0x2c67df8`).

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | String | yes | `<device sn>` | `ev_charge_command.dart @0x2c67e04` (third argument; the caller passes the serial from the widget's device object, `a5190_fault_info_widget.dart @0x2c67ce8`) |
| `subSn` | String | yes | `<device sn>` | `ev_charge_command.dart @0x2c67e18` (the same third argument as `sn`, stored again, `@0x2c67e24`) |
| `pn` | String | yes | `A5191` | `ev_charge_command.dart @0x2c67e28` (second argument; the caller passes the product code field of the device object, `a5190_fault_info_widget.dart @0x2c67d14`; the example PN is a placeholder) |
| `bitArray` | list of int | yes | `[0, 0]` | `ev_charge_command.dart @0x2c67e3c` (first argument; the caller builds a list of integers from the fault words with `listToInt` in a loop over pairs, `a5190_fault_info_widget.dart @0x2c67bd8`) |
| `typeId` | int | yes (constant) | `1026` | `ev_charge_command.dart @0x2c67e50`; raw `2052` at `@0x2c67e5c`, stored with `stur w16`, a Smi, so 1026 (`tools/smi.py`) |
| `localTime` | String | yes | `"2026-10-19 14:30"` | `ev_charge_command.dart @0x2c67e64`; `DateFormat("yyyy-MM-dd HH:mm").format(DateTime.now())` (pattern `@0x2c67e78`, `DateTime` object with `isUtc` false `@0x2c67e94`, `format` `@0x2c67ebc`): local time, minute resolution |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): `handle` is called without a type argument.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "sn": "<device sn>", "subSn": "<device sn>", "pn": "<pn>", "bitArray": [0, 0], "typeId": 1026, "localTime": "2026-10-19 14:30" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../errors.md).

## Callers in app

- `_A5190FaultInfoWidgetState._userFaultAlarm` (`ev_charger/src/ev_charger/page/home/widget/a5190_fault_info_widget.dart @0x2c67d38`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0xf0b00`); the sender function has no literal difference between 3.18.0 and 3.24.3 (`tools/cmp_since.py`: ordered string, integer and type literals compared; branch logic not compared). Not new in 3.24.3: the inventory learned URL literals without a leading slash, which made the URL visible. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- The server-side effect (a stored alarm, a push message or both) is not known; the keys use camelCase (`subSn`, `bitArray`, `typeId`, `localTime`) unlike most other bodies.
- What a bit in `bitArray` means (fault code table) is not decoded here.
- No response was captured.

## Device-tested by

none
