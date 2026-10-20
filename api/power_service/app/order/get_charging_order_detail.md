> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_charging_order_detail

## Purpose

Reads one charging order of an EV charger in detail: start and end, energy, cost, assigned vehicle, state-of-charge curve, price curve and power points.

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (line 290, docstring list of endpoints "neither implemented nor explored"); the comment there ("Data points for charts of order, also vehicle details {\"device_sn\": deviceSn, \"order_id\": orderId}") is the upstream author's note, not a test result.

## Method+URL

`POST /power_service/v1/app/order/get_charging_order_detail` (asm-traced). Sender: `AKIotEVChargeCommand.getSessionsDetail` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x2aad688`). The path literal has no leading slash (`@0x2aad6e4`), the method is the string `"POST"` (`@0x2aad6fc`), and the map keys `path`, `method`, `param` are stored at `@0x2aad6dc`, `@0x2aad6f0`, `@0x2aad708`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x2aad7b8`, call `@0x2aad7c8`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#the-common-envelope), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, Object>` map of two pairs (`r2 = 8`, `@0x2aad718`).

| field | type | required | example | source |
|---|---|---|---|---|
| `transaction_id` | int | yes | `1` | `ev_charge_command.dart @0x2aad724`; the argument is boxed with `BoxInt64Instr` (`@0x2aad734`), unboxed int64 |
| `device_sn` | String | yes | `<device sn>` | `ev_charge_command.dart @0x2aad74c` |

Upstream's comment sends `{"device_sn", "order_id"}` for this URL; the app sends `transaction_id` (an integer) and `device_sn`, and no `order_id`. Whether the server also accepts `order_id` is not tested here. The same integer `transaction_id` is the order handle that [set_charging_vehicle](../vehicle/set_charging_vehicle.md) uses.

## `param_type`/`cmd`

n/a

## Response model (link)

`A5190SessionsDetailModel` ([../../../../models/ev_charger_session_models.md](../../../../models/ev_charger_session_models.md#a5190sessionsdetailmodel)), taken from the type argument of `handle<A5190SessionsDetailModel>` (ev_charge_command.dart `@0x2aad7a8`)

## Response

The SDK result is typed `IoTAKResult<A5190SessionsDetailModel>`; the keys are on the model page. The wrapper `data` of `A5190SessionsDetailModel.fromJson` is described there. The caller reads the result type before using the data.

| field | type | required | example | source |
|---|---|---|---|---|
| `data` | String (JSON text) or map | no |  | `a5190_sessions_detail_model.dart @0x36f969c` |
| `order_id`, `transaction_id`, `charge_vehicle_info`, `charge_soc_info`, `charge_tou_info`, `data_point`, ... | see model page | no |  | [../../../../models/ev_charger_session_models.md](../../../../models/ev_charger_session_models.md#a5190sessionsdetailmodel) |

## Example request/response

Request, synthesized

```json
{ "transaction_id": 1, "device_sn": "<device sn>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `A5190HomeLogic._getOrderCostAndUpdateUI` (`ev_charger/src/ev_charger/page/home/a5190_home_logic.dart @0x3393718`)
- `SessionsDetailLogic.getSessionsDetail` (`ev_charger/src/ev_charger/page/home/charge_sessions/sessions_detail/sessions_detail_logic.dart @0x2aac7a0`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x83688`); the sender function has no literal difference between 3.18.0 and 3.24.3 (`tools/cmp_since.py`: ordered string, integer and type literals compared; branch logic not compared). Not new in 3.24.3: the inventory learned URL literals without a leading slash, which made the URL visible. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- Where the app takes the integer `transaction_id` from (the order list rows carry both `order_id` and, in the statistics list, `transaction_id`) is not traced in the sender. — traced 2026-10-20: in `A5190HomeLogic._getOrderCostAndUpdateUI` (`ev_charger/src/ev_charger/page/home/a5190_home_logic.dart @0x3393694`) `transaction_id` is the function's own unboxed integer parameter (zero test `cbnz x2` `@0x33936d0`); that function is called from `_listenSmartChargingUpdate` (`@0x3393610`), `_listenRealTimeData` (`@0x33943cc`), two closures (`@0x350a7f0`, `@0x39490c8`) and `onRefresh` (`@0x43b1e20`), and the value they pass was not read; `SessionsDetailLogic.getSessionsDetail` (`ev_charger/src/ev_charger/page/home/charge_sessions/sessions_detail/sessions_detail_logic.dart @0x2aac6f0`) is called from `onReady` (`@0x2aac2cc`) and `SessionsDetailPage.changeChargingVehicle` (`ev_charger/src/ev_charger/page/home/charge_sessions/sessions_detail/sessions_detail_page.dart @0x3959b44`)
- Whether the server accepts upstream's `order_id` form is not known (the app does not send it).

## Device-tested by

none
