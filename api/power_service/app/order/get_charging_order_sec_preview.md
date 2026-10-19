> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_charging_order_sec_preview

## Purpose

Reads a page of preview blocks of the second-level power points of one charging order of an EV charger (the overview that selects which block to zoom into).

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (line 292, docstring list of endpoints "neither implemented nor explored"); the comment there ("may need real EV_Charger? {\"order_id\": orderId}") is the upstream author's note, not a test result.

## Method+URL

`POST /power_service/v1/app/order/get_charging_order_sec_preview` (asm-traced). Sender: `AKIotEVChargeCommand.getSessionsOrderSecPreview` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x35f2d18`). The path literal has no leading slash (`@0x35f2d78`), the method is the string `"POST"` (`@0x35f2d90`), and the map keys `path`, `method`, `param` are stored at `@0x35f2d70`, `@0x35f2d84`, `@0x35f2d9c`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x35f2e74`, call `@0x35f2e84`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#the-common-envelope), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, Object>` map of four pairs (`r2 = 16`, `@0x35f2dac`).

| field | type | required | example | source |
|---|---|---|---|---|
| `order_id` | String | yes | `<order id>` | `ev_charge_command.dart @0x35f2db8` |
| `page_num` | int | yes | `1` | `ev_charge_command.dart @0x35f2dcc`; boxed with `BoxInt64Instr` (`@0x35f2ddc`), unboxed int64 |
| `page_size` | int | yes (constant) | `20` | `ev_charge_command.dart @0x35f2df4`; raw `40` at `@0x35f2e00`, `stur w16`, a Smi, so 20 (`tools/smi.py`) |
| `device_sn` | String | yes | `<device sn>` | `ev_charge_command.dart @0x35f2e08` |

Upstream's comment lists only `order_id`; the app sends the four keys above.

## `param_type`/`cmd`

n/a

## Response model (link)

`A5190SessionsOrderSecPreview` ([../../../../models/ev_charger_session_models.md](../../../../models/ev_charger_session_models.md#a5190sessionsordersecpreview)), taken from the type argument of `handle<A5190SessionsOrderSecPreview>` (ev_charge_command.dart `@0x35f2e64`)

## Response

The SDK result is typed `IoTAKResult<A5190SessionsOrderSecPreview>`; the keys are on the model page. The wrapper `data` of `A5190SessionsOrderSecPreview.fromJson` is described there. The caller reads the result type before using the data.

| field | type | required | example | source |
|---|---|---|---|---|
| `data` | String (JSON text) or map | no |  | `a5190_sessions_order_sec_preview.dart @0x45b1acc` |
| `page_num`, `order_id`, `list`, `page_size`, `total` | see model page | no |  | [../../../../models/ev_charger_session_models.md](../../../../models/ev_charger_session_models.md#a5190sessionsordersecpreview) |

## Example request/response

Request, synthesized

```json
{ "order_id": "<order id>", "page_num": 1, "page_size": 20, "device_sn": "<device sn>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `SecondPowerLogic.getSessionsOrderSecPreview` (`ev_charger/src/ev_charger/page/home/charge_sessions/second_power/second_power_logic.dart @0x35f2cd0`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x83ae0`); the sender function has no literal difference between 3.18.0 and 3.24.3 (`tools/cmp_since.py`: ordered string, integer and type literals compared; branch logic not compared). Not new in 3.24.3: the inventory learned URL literals without a leading slash, which made the URL visible. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- What a `list` block represents (its `start_time` and `power_unit` only are modelled) is not decoded; the actual power values arrive from [get_charging_order_sec_detail](get_charging_order_sec_detail.md).

## Device-tested by

none
