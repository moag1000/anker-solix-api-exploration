> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_charging_order_sec_detail

## Purpose

Reads the second-level power points of one charging order of an EV charger from a start time on (the zoomed power chart of the order).

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (line 291, docstring list of endpoints "neither implemented nor explored"); the comment there ("may need real EV_Charger? {\"order_id\": orderId,\"start_time\": <timestamp>}") is the upstream author's note, not a test result.

## Method+URL

`POST /power_service/v1/app/order/get_charging_order_sec_detail` (asm-traced). Sender: `AKIotEVChargeCommand.getSessionsOrderSecDetail` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x35f23fc`). The path literal has no leading slash (`@0x35f245c`), the method is the string `"POST"` (`@0x35f2474`), and the map keys `path`, `method`, `param` are stored at `@0x35f2454`, `@0x35f2468`, `@0x35f2480`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x35f2544`, call `@0x35f2554`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#the-common-envelope), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, Object>` map of three pairs (`r2 = 12`, `@0x35f2490`).

| field | type | required | example | source |
|---|---|---|---|---|
| `order_id` | String | yes | `<order id>` | `ev_charge_command.dart @0x35f249c` |
| `start_time` | int | yes | `1760000000` | `ev_charge_command.dart @0x35f24b0`; boxed with `BoxInt64Instr` (`@0x35f24c0`), unboxed int64; unit not shown (upstream: `<timestamp>`) |
| `device_sn` | String | yes | `<device sn>` | `ev_charge_command.dart @0x35f24d8` |

Upstream's comment lists only `order_id` and `start_time`; the app also sends `device_sn`.

## `param_type`/`cmd`

n/a

## Response model (link)

`A5190SessionsOrderSecDetail` ([../../../../models/ev_charger_session_models.md](../../../../models/ev_charger_session_models.md#a5190sessionsordersecdetail)), taken from the type argument of `handle<A5190SessionsOrderSecDetail>` (ev_charge_command.dart `@0x35f2534`)

## Response

The SDK result is typed `IoTAKResult<A5190SessionsOrderSecDetail>`; the keys are on the model page. The wrapper `data` of `A5190SessionsOrderSecDetail.fromJson` is described there. The caller reads the result type before using the data.

| field | type | required | example | source |
|---|---|---|---|---|
| `data` | String (JSON text) or map | no |  | `a5190_sessions_order_sec_detail.dart @0x45b25f0` |
| `order_id`, `power_points`, `power_unit`, `start_time` | see model page | no |  | [../../../../models/ev_charger_session_models.md](../../../../models/ev_charger_session_models.md#a5190sessionsordersecdetail) |

## Example request/response

Request, synthesized

```json
{ "order_id": "<order id>", "start_time": 1760000000, "device_sn": "<device sn>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `SecondPowerLogic.getSessionsOrderSecDetail` (`ev_charger/src/ev_charger/page/home/charge_sessions/second_power/second_power_logic.dart @0x35f23b4`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0xf0780`); the sender function has no literal difference between 3.18.0 and 3.24.3 (`tools/cmp_since.py`: ordered string, integer and type literals compared; branch logic not compared). Not new in 3.24.3: the inventory learned URL literals without a leading slash, which made the URL visible. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- The unit of `start_time` (seconds or milliseconds) is not shown by the sender; upstream says only `<timestamp>`.

## Device-tested by

none
