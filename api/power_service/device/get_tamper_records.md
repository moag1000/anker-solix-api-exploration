> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_tamper_records

## Purpose

Reads the tamper-proof (security) log of an EV charger, a page at a time; the security logs screen of the charger settings uses it.

## Upstream name

`get_tamper_records` (upstream-confirmed, `api/apitypes.py` line 164; upstream comment: "needs owner, not sure what it does, {\"device_sn\": deviceSn, \"page_num\": 1, \"page_size\": 10}").

## Method+URL

`POST /power_service/v1/device/get_tamper_records` (asm-traced). Sender: `AKIotEVChargeCommand.getSecurityLogs` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x2a3da00`). The path literal has no leading slash (`@0x2a3da5c`), the method is the string `"POST"` (`@0x2a3da74`), and the map keys `path`, `method`, `param` are stored at `@0x2a3da54`, `@0x2a3da68`, `@0x2a3da80`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x2a3db44`, call `@0x2a3db54`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../sdk_senders.md](../../sdk_senders.md#the-common-envelope), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, Object>` map of three pairs (`r2 = 12`, `@0x2a3da90`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `<device sn>` | `ev_charge_command.dart @0x2a3da9c` |
| `page_num` | int | yes | `1` | `ev_charge_command.dart @0x2a3dab0`; boxed with `BoxInt64Instr` (`@0x2a3dac0`), unboxed int64 |
| `page_size` | int | yes (constant) | `20` | `ev_charge_command.dart @0x2a3dad8`; raw `40` at `@0x2a3dae4`, `stur w16`, a Smi, so 20 (`tools/smi.py`) |

Upstream confirms the three keys (with a page size of 10); the app fixes the page size at 20. The call belongs to the tamper-proof feature: the neighbouring menu entry `SecurityLogsMenuController` has a function `requestTamperProofConfig` (`ev_charger/src/ev_charger/page/home/setting/menu_controller/security_logs_controller.dart @0x368dd1c`) that fetches the charger KV config (`tamper_proof` is one of its keys).

## `param_type`/`cmd`

n/a

## Response model (link)

`A5190SecurityLogsModel` ([../../../models/ev_charger_device_models.md](../../../models/ev_charger_device_models.md#a5190securitylogsmodel)), taken from the type argument of `handle<A5190SecurityLogsModel>` (ev_charge_command.dart `@0x2a3db34`)

## Response

The SDK result is typed `IoTAKResult<A5190SecurityLogsModel>`; the keys are on the model page. The wrapper `data` of `A5190SecurityLogsModel.fromJson` is described there. The caller reads the result type before using the data.

| field | type | required | example | source |
|---|---|---|---|---|
| `data` | String (JSON text) or map | no |  | `a5190_security_logs_model.dart @0x45b36bc` |
| `page_size`, `total`, `page_num`, `records` | see model page | no | `records[]`: `content`, `create_time` | `a5190_security_logs_model.dart @0x45b37a8`, `@0x45b3830`, `@0x45b38b8`, `@0x45b3940`; [models/ev_charger_device_models.md](../../../models/ev_charger_device_models.md#a5190securitylogsmodel) |

## Example request/response

Request, synthesized

```json
{ "device_sn": "<device sn>", "page_num": 1, "page_size": 20 }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `SecurityLogsLogic.getSecurityLogs` (`ev_charger/src/ev_charger/page/home/setting/security_logs/security_logs_logic.dart @0x2a3d9b8`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x81ae0`); the sender function has the same sequence of string, integer and type literals in 3.18.0 (compared with a throwaway script, not committed). Not new in 3.24.3: the Task 3.1b inventory change (slashless URL literals) made the URL visible, nothing changed in the app. 3.24.3: present, unchanged. since: ≤3.18.0.

## Known unknowns

- The content strings and the time unit of `create_time` are not shown in the model.
- Upstream notes that the call needs the owner account; whether a shared member is rejected is not recorded here.

## Device-tested by

none
