> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_charge_order_stats

## Purpose

Reads the charging statistics of an EV charger for a date range (energy, duration, count, cost, CO2, per-period buckets) for the statistics chart.

## Upstream name

`get_device_charge_order_stats` (upstream-confirmed, `api/apitypes.py` line 148; upstream comment: "works as member, date_type[week month year all], show EV_charger stats, {\"device_sn\":deviceSn,\"date_type\":\"all\",\"start_date\":\"\",\"end_date\":\"\"}").

## Method+URL

`POST /power_service/v1/app/order/get_charge_order_stats` (asm-traced). Sender: `AKIotEVChargeCommand.getChargeSessionChartModel` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x29a0f44`). The path literal has no leading slash (`@0x29a0fa8`), the method is the string `"POST"` (`@0x29a0fc0`), and the map keys `path`, `method`, `param` are stored at `@0x29a0fa0`, `@0x29a0fb4`, `@0x29a0fcc`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x29a1094`, call `@0x29a10a4`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#the-common-envelope), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, String>` map of four pairs (`r2 = 16`, `@0x29a0fdc`); all values are Strings.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `<device sn>` | `ev_charge_command.dart @0x29a0fe4` (the argument, `@0x29a0ff0`) |
| `start_date` | String | yes | `2026-10-01` | `ev_charge_command.dart @0x29a0ff8` (the argument, `@0x29a1004`) |
| `end_date` | String | yes | `2026-10-19` | `ev_charge_command.dart @0x29a100c` (the argument, `@0x29a1018`) |
| `date_type` | String | yes | `"month"` | `ev_charge_command.dart @0x29a1020`; String; the name field (object offset 0x10, `LoadField r2 = r1->field_f`, `@0x29a1030`) of a `ChartDateType` enum instance. The pool holds five instances: `day` (`pp+0xa67b8`), `week` (`pp+0xa6898`), `month` (`pp+0xa6888`), `year` (`pp+0xa6890`), `all` (`pp+0xa6ea8`) (`pp.txt`) |

The caller `ChargerChartController.refreshChart` (`ev_charger/src/ev_charger/page/home/charge_sessions/charger_chart_controller.dart`) maps the selected chart tab (an unboxed integer field at object offset 0x53, `@0x2999f40`) to the enum instance: 0 gives `week` (`@0x2999f6c`, pool `pp+0xa6898`), 1 gives `month` (`@0x2999f78`, `pp+0xa6888`), 2 gives `year` (`@0x2999f8c`, `pp+0xa6890`), any other value gives `all` (`@0x2999f98`, `pp+0xa6ea8`); `day` is not selected there. This matches the upstream list `week month year all`. The end date comes from `getEndParamDate` (`@0x2999f30`); the date format of `start_date` and `end_date` is not shown in the sender.

## `param_type`/`cmd`

n/a

## Response model (link)

`ChargerSessionChartModel` ([../../../../models/ev_charger_session_models.md](../../../../models/ev_charger_session_models.md#chargersessionchartmodel)), taken from the type argument of `handle<ChargerSessionChartModel>` (ev_charge_command.dart `@0x29a1084`)

## Response

The SDK result is typed `IoTAKResult<ChargerSessionChartModel>`; the keys are on the model page. The wrapper `data` of `ChargerSessionChartModel.fromJson` is described there. The caller reads the result type before using the data.

| field | type | required | example | source |
|---|---|---|---|---|
| `data` | String (JSON text) or map | no |  | `charger_session_chart_model.dart @0x45ae90c` |
| `total_stats`, `date_list` | see model page | no |  | [../../../../models/ev_charger_session_models.md](../../../../models/ev_charger_session_models.md#chargersessionchartmodel) |

## Example request/response

Request, synthesized

```json
{ "device_sn": "<device sn>", "start_date": "2026-10-01", "end_date": "2026-10-19", "date_type": "month" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `ChargerChartHttpRepository.fetchChargeOrderStats` (`ev_charger/src/ev_charger/page/home/charge_sessions/repository/charger_chart_http_repository.dart @0x299a080`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x83c90`); the sender function has the same sequence of string, integer and type literals in 3.18.0 (compared with a throwaway script, not committed). Not new in 3.24.3: the Task 3.1b inventory change (slashless URL literals) made the URL visible, nothing changed in the app. 3.24.3: present, unchanged. since: ≤3.18.0.

## Known unknowns

- The date format of `start_date`/`end_date` and the unit of the amounts in the answer are not shown in the sender or the model.
- Whether the server accepts `day` (the enum has it, the chart does not send it) is not known.

## Device-tested by

none
