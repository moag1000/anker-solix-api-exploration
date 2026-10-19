> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# record_device_command

## Purpose

Records a command that the app sent to an AX170 (ATS) device so that the cloud keeps a history; the traced sender records the update of a branch circuit record with the device serial, a command type and the command data.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /devicecontrol/v1/app/record_device_command` (asm-traced): path literal `"devicecontrol/v1/app/record_device_command"` (no leading slash) at `ats_ax170/src/sdk/command/ax170_command.dart @0x2f43804`, method `"POST"` (`@0x2f4381c`), in the SDK closure `@0x2f437a4` created by `AKIotAX170Command.updateBranchRecord` (`@0x2f43550`, static).

## Encrypted?

Direct SDK call (asm-traced), path C of [encryption.md](../../encryption.md#which-calls-are-encrypted): `the closure of `updateBranchRecord`` builds the map `path`, `method`, `param` and passes it to `akIoTKitManager.handle` with the identifier `akiot.cloud_api` (`ats_ax170/src/sdk/command/ax170_command.dart @0x2f43868`). The decorator tests are not involved; encryption and headers are native to the SDK. The inventory flag `encrypted: false` only means that no `*Http*` wrapper is called.

## Request

`updateBranchRecord` builds the `param` map; the closure wraps it in `path`, `method`, `param` (`r2 = 12`, `@0x2f437f0`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `"<device sn>"` | `ats_ax170/src/sdk/command/ax170_command.dart @0x2f43684`; function argument |
| `command_type` | int | yes | not decoded | `@0x2f43698`; function argument, an unboxed int boxed at `@0x2f436a8` (no literal at this site; the callers pass the value) |
| `command_data` | String | yes | `"{\"id\":1,\"status\":1}"` | `@0x2f43750`; JSON text (`jsonEncode`, `@0x2f43744`) of a map with the keys `id` (`@0x2f43704`) and `status` (`@0x2f43718`) built from two function arguments; when the two arguments are absent the app sends the empty string (`@0x2f4376c`) |

The example values of `id` and `status` are placeholders.

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model is parsed; the SDK result is returned to the caller unread.

## Response

The closure returns the SDK result (`Future<IoTAKResult<dynamic>>`) unchanged; no response field is read in this function.

## Example request/response

Request, synthesized

```json
{ "path": "devicecontrol/v1/app/record_device_command", "method": "POST",
  "param": { "device_sn": "<device sn>", "command_type": 1, "command_data": "{\"id\":1,\"status\":1}" } }
```

Response: no captured response.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or logs it; the shared transport codes are in [encryption.md](../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `AKIotAX170Command.updateBranchRecord` (`ats_ax170/src/sdk/command/ax170_command.dart @0x2f43550`), called from `ats_load_status_dialog_controller.dart` (call `@0x2f43508`), `ax170_home_logic.dart` (`@0x2f444cc`) and `backup_strategy_controller.dart` (`@0x2f43a34`, `@0x38115a4`): the ATS load status dialog, the AX170 home page and the branch circuit backup strategy page (package `ats_ax170`).

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 pool as a code-referenced URL; see the inventory row `since`). 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- The values of `command_type` and the meaning of `id` and `status` are not decoded; the three callers pass different values.
- Whether other device families record commands through this endpoint is not known (only the AX170 sender exists in 3.24.3).
- Server behaviour is not known.

## Device-tested by

none
