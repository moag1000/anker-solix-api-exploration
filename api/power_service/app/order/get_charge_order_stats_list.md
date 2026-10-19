> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_charge_order_stats_list

## Purpose

Reads the individual charging orders of an EV charger inside a date range and a status filter, a page at a time (the "sessions" list behind the statistics chart).

## Upstream name

`get_device_charge_order_stats_list` (upstream-confirmed, `api/apitypes.py` line 149; upstream comment: "works as member, date_type[week month year all], order_Status unknown, {\"device_sn\":deviceSn,\"order_status\":1,\"date_type\":\"all\",\"start_date\":\"\",\"end_date\":\"\",\"page\":0,\"page_size\":10}").

## Method+URL

`POST /power_service/v1/app/order/get_charge_order_stats_list` (asm-traced). Sender: `AKIotEVChargeCommand.getChargerSessionOrderList` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x29a2ef8`). The path literal has no leading slash (`@0x29a2f64`), the method is the string `"POST"` (`@0x29a2f7c`), and the map keys `path`, `method`, `param` are stored at `@0x29a2f5c`, `@0x29a2f70`, `@0x29a2f88`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x29a30cc`, call `@0x29a30dc`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#the-common-envelope), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, Object>` map of seven pairs (`r2 = 28` for the body array, `@0x29a2f98`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `<device sn>` | `ev_charge_command.dart @0x29a2fa4` |
| `start_date` | String | yes | `2026-10-01` | `ev_charge_command.dart @0x29a2fb8` |
| `end_date` | String | yes | `2026-10-19` | `ev_charge_command.dart @0x29a2fcc` |
| `date_type` | String | yes | `"month"` | `ev_charge_command.dart @0x29a2fe0`; the name of a `ChartDateType` instance, as on [get_charge_order_stats](get_charge_order_stats.md#request) |
| `order_status` | int | yes | `1` | `ev_charge_command.dart @0x29a2ffc`; the argument is an integer (Smi-tagged with `lsl x1, x0, #1`, `@0x29a300c`), not a constant |
| `page` | int | yes | `1` | `ev_charge_command.dart @0x29a3014`; the argument is boxed with `BoxInt64Instr` (`@0x29a3024`), unboxed int64 |
| `page_size` | int | yes (constant) | `15` | `ev_charge_command.dart @0x29a3060`; raw `30` at `@0x29a306c`, stored with `stur w16`, a Smi, so 15 (`tools/smi.py`) |

The key is `page` here (not `page_num` as in [get_charging_order_list](get_charging_order_list.md)); upstream also sends `page` (starting at 0) and a `page_size` of 10. The app fixes the page size at 15. The status filter values are not decoded; the caller supplies the value (not traced).

## `param_type`/`cmd`

n/a

## Response model (link)

`ChargerSessionOrderListModel` ([../../../../models/ev_charger_session_models.md](../../../../models/ev_charger_session_models.md#chargersessionorderlistmodel)), taken from the type argument of `handle<ChargerSessionOrderListModel>` (ev_charge_command.dart `@0x29a30bc`)

## Response

The SDK result is typed `IoTAKResult<ChargerSessionOrderListModel>`; the keys are on the model page. The wrapper `data` of `ChargerSessionOrderListModel.fromJson` is described there. The caller reads the result type before using the data.

| field | type | required | example | source |
|---|---|---|---|---|
| `data` | String (JSON text) or map | no |  | `charger_session_order_list_model.dart @0x45af744` |
| `page`, `page_size`, `total`, `start_use_time`, `order_list` | see model page | no |  | [../../../../models/ev_charger_session_models.md](../../../../models/ev_charger_session_models.md#chargersessionorderlistmodel) |

## Example request/response

Request, synthesized

```json
{ "device_sn": "<device sn>", "start_date": "2026-10-01", "end_date": "2026-10-19", "date_type": "month", "order_status": 1, "page": 1, "page_size": 15 }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `ChargeSessionsExceptionLogic.getChargeListSessions` (`ev_charger/src/ev_charger/page/home/charge_sessions/charge_sessions_exception_logic.dart @0x2aabfc8`)
- `ChargerChartHttpRepository.fetchChargeOrderList` (`ev_charger/src/ev_charger/page/home/charge_sessions/repository/charger_chart_http_repository.dart @0x29a2978`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x83ca8`); the sender function has no literal difference between 3.18.0 and 3.24.3 (`tools/cmp_since.py`: ordered string, integer and type literals compared; branch logic not compared). Not new in 3.24.3: the Task 3.1b inventory change (slashless URL literals) made the URL visible. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- The values of `order_status` and whether `page` is 0-based (upstream sends 0) or 1-based are not decoded from the sender.
- How this list differs from [get_charging_order_list](get_charging_order_list.md) for the server (both list orders) is not known.

## Device-tested by

none
