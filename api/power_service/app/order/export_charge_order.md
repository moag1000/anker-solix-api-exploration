> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# export_charge_order

## Purpose

Asks the cloud for a file of the charging orders of an EV charger in a date range; the answer carries the file URL and name for the app's export action.

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (line 293, docstring list of endpoints "neither implemented nor explored"); the comment there (no comment on this entry) is the upstream author's note, not a test result.

## Method+URL

`POST /power_service/v1/app/order/export_charge_order` (asm-traced). Sender: `AKIotEVChargeCommand.fetchExportChargeOrderUrl` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x3956700`). The path literal has no leading slash (`@0x3956764`), the method is the string `"POST"` (`@0x395677c`), and the map keys `path`, `method`, `param` are stored at `@0x395675c`, `@0x3956770`, `@0x3956788`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x3956850`, call `@0x3956860`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#the-common-envelope), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, String>` map of four pairs (`r2 = 16`, `@0x3956798`), the same four keys as [get_charge_order_stats](get_charge_order_stats.md#request).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `<device sn>` | `ev_charge_command.dart @0x39567a0` |
| `start_date` | String | yes | `2026-10-01` | `ev_charge_command.dart @0x39567b4` |
| `end_date` | String | yes | `2026-10-19` | `ev_charge_command.dart @0x39567c8` |
| `date_type` | String | yes | `"month"` | `ev_charge_command.dart @0x39567dc`; `ChartDateType` name, `LoadField` `@0x39567ec` |

## `param_type`/`cmd`

n/a

## Response model (link)

`A5190ExportChargeOrderModel` ([../../../../models/ev_charger_session_models.md](../../../../models/ev_charger_session_models.md#a5190exportchargeordermodel)), taken from the type argument of `handle<A5190ExportChargeOrderModel>` (ev_charge_command.dart `@0x3956840`)

## Response

The SDK result is typed `IoTAKResult<A5190ExportChargeOrderModel>`; the keys are on the model page. The wrapper `data` of `A5190ExportChargeOrderModel.fromJson` is described there. The caller reads the result type before using the data.

| field | type | required | example | source |
|---|---|---|---|---|
| `data` | String (JSON text) or map | no |  | `A5190_export_charge_order_Model.dart @0x45b183c` |
| `file_url`, `file_name` | String? | no |  | `A5190_export_charge_order_Model.dart @0x45b1928`, `@0x45b19b0`; [../../../../models/ev_charger_session_models.md](../../../../models/ev_charger_session_models.md#a5190exportchargeordermodel) |

## Example request/response

Request, synthesized

```json
{ "device_sn": "<device sn>", "start_date": "2026-10-01", "end_date": "2026-10-19", "date_type": "month" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `ChargerChartHttpRepository.fetchExportChargeOrderUrl` (`ev_charger/src/ev_charger/page/home/charge_sessions/repository/charger_chart_http_repository.dart @0x39565b4`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x83f98`); the sender function has the same sequence of string, integer and type literals in 3.18.0 (compared with a throwaway script, not committed). Not new in 3.24.3: the Task 3.1b inventory change (slashless URL literals) made the URL visible, nothing changed in the app. 3.24.3: present, unchanged. since: ≤3.18.0.

## Known unknowns

- The file format behind `file_url` (CSV, PDF, ...) and how long the URL stays valid are not known.
- No response was captured.

## Device-tested by

none
