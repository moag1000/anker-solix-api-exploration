> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_charging_order_list

## Purpose

Reads a page of charging orders of an EV charger; the app's home screen calls it with page size 1 to show the most recent order (energy, duration, cost).

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (line 289, docstring list of endpoints "neither implemented nor explored"); the comment there ("may need member EV_Charger, Get all orders in range, {\"device_sn\": deviceSn, \"start_time\": \"2026-02-09\"}") is the upstream author's note, not a test result.

## Method+URL

`POST /power_service/v1/app/order/get_charging_order_list` (asm-traced). Sender: `AKIotEVChargeCommand.getChargeSessions` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x3394738`). The path literal has no leading slash (`@0x3394790`), the method is the string `"POST"` (`@0x33947a8`), and the map keys `path`, `method`, `param` are stored at `@0x3394788`, `@0x339479c`, `@0x33947b4`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x339489c`, call `@0x33948ac`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#the-common-envelope), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, Object>` map of six pairs (`r2 = 12`, `@0x3394778` for the envelope, `r2 = 24`, `@0x33947c4` for the body). Only `device_sn` comes from the caller; the other five values are constants of the function.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `<device sn>` | `ev_charge_command.dart @0x33947cc` (value: the argument, `@0x33947d8`) |
| `start_time` | String | yes (constant) | `""` | `ev_charge_command.dart @0x33947e0` (empty string `@0x33947ec`) |
| `end_time` | String | yes (constant) | `""` | `ev_charge_command.dart @0x33947f4` (empty string `@0x3394800`) |
| `order_status` | int | yes (constant) | `3` | `ev_charge_command.dart @0x3394808`; raw `6` at `@0x3394814`, stored with `stur w16` into the array, a Smi, so 3 (`tools/smi.py`) |
| `page_num` | int | yes (constant) | `1` | `ev_charge_command.dart @0x339481c`; raw `2` at `@0x3394828`, `stur w16`, so 1 |
| `page_size` | int | yes (constant) | `1` | `ev_charge_command.dart @0x3394830`; raw `2` at `@0x339483c`, `stur w16`, so 1 |

Upstream sends only `device_sn` and a date string `start_time` (`api/apitypes.py` line 289 comment). The app's constant `order_status` 3 with page size 1 is the "latest order" query of the home card; other callers of the same endpoint were not found, so the app never sends a real date range or larger page here.

## `param_type`/`cmd`

n/a

## Response model (link)

`A5190ChargeSessionsModel` ([../../../../models/ev_charger_session_models.md](../../../../models/ev_charger_session_models.md#a5190chargesessionsmodel)), taken from the type argument of `handle<A5190ChargeSessionsModel>` (ev_charge_command.dart `@0x339488c`)

## Response

The SDK result is typed `IoTAKResult<A5190ChargeSessionsModel>`; the keys are on the model page. The wrapper `data` of `A5190ChargeSessionsModel.fromJson` is described there. The caller reads the result type before using the data.

| field | type | required | example | source |
|---|---|---|---|---|
| `data` | String (JSON text) or map | no | `"{...}"` | `a5190_charge_sessions_model.dart @0x45b2b6c`; decoded by `jsonDecode` when it is a String (`@0x45b2c40`) |
| `list`, `page_size`, `page_num`, `total_count` | see model page | no |  | [../../../../models/ev_charger_session_models.md](../../../../models/ev_charger_session_models.md#a5190chargesessionsmodel) |

## Example request/response

Request, synthesized

```json
{ "device_sn": "<device sn>", "start_time": "", "end_time": "", "order_status": 3, "page_num": 1, "page_size": 1 }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `A5190HomeLogic._getChargeSessions` (`ev_charger/src/ev_charger/page/home/a5190_home_logic.dart @0x33946f0`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0xbe580`); the sender function has no literal difference between 3.18.0 and 3.24.3 (`tools/cmp_since.py`: ordered string, integer and type literals compared; branch logic not compared). Not new in 3.24.3: the inventory learned URL literals without a leading slash, which made the URL visible. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- The values of `order_status` are not decoded (3 is what the home card sends; upstream also notes them as unknown).
- Whether the server honours `start_time`/`end_time` as dates, and whether `page_num` is 1-based, is not tested.
- No response was captured; the response layout is the model's `fromJson`, not a server sample.

## Device-tested by

none
