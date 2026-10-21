> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# energy_analysis

## Purpose

Reads the energy chart data of one device for a time range: the S1/S2 charge-session chart (power and energy per period) and the history chart of the AE1X0 meter (import and export per phase).

## Upstream name

`none` for this URL (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (line 349) and knows the older site-level `energy_analysis` key (`power_service/v1/site/energy_analysis`, line 114), a different endpoint.

## Method+URL

`POST /power_service/v2/device/energy_analysis` (asm-traced). Two groups of senders: the S1/S2 command `S1S2DeviceCommand.getChargeSessionChartModel` (`s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2991c18`; the path literal has no leading slash, `"power_service/v2/device/energy_analysis"`, `@0x2991c7c`, method `"POST"` `@0x2991c94`) and `Ae1x0MeterChartLogic.requestChartData` (`third_device/src/module/ae1x0/history/widget/meter_chart_logic.dart @0x2ca26f8`; URL literal `@0x2ca2ba8`, `Method.post` pool entry `pp+0xa7e0`, `@0x2ca2ba0`). The EV-charger command `AKIotEVChargeCommand.getChargeSessionChartModel` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x29a0f44`) is a separate sender whose URL is not this one (not described here).

## Encrypted?

Two paths. S1/S2 sender: direct SDK call, path C of [encryption.md](../../../encryption.md#which-calls-are-encrypted) (`s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2991d74`, identifier `akiot.cloud_api`, map `path`, `method`, `param`). AE1X0 sender: `encryptionRequestHttp` (`third_device/src/module/ae1x0/history/widget/meter_chart_logic.dart @0x2ca2bcc`) without `needEncryption`, so the default `true` applies; whether it goes through the SDK is decided at run time. The inventory flag `encrypted: false` on the S1/S2 row only means that no `*Http*` wrapper is called.

## Request

S1/S2 sender (`param` map literal, four pairs, `r2 = 16`, `@0x2991cb0`):

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `"<device sn>"` | `s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2991cb8` |
| `start_time` | String | yes | `"2026-10"` | `s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2991ccc`; function argument; the caller `_fetchFromServer` (`s1_s2/src/page/charge_sessions/repository/charger_chart_http_repository.dart @0x2990f58`) cuts the date string with `substring(0, n)` depending on the chart date type: raw `14` (`@0x299104c`) and raw `8` (`@0x2991094`), pushed as call arguments (`str x16, [SP]` at `@0x2991050`, `@0x2991098`; `tools/smi.py` cannot decode an argument push) (tagged), so 7 and 4 characters, consistent with `yyyy-MM` and `yyyy` (inference, the date format itself is not decoded) |
| `end_time` | String | yes | `"2026-10"` | `s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2991ce0`; function argument, cut the same way |
| `type` | string | yes | `"month"` | `s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2991cf4`; the map is typed `<String, String>` (`@0x2991d0c`); the value is the field at offset 0xf (`@0x2991d00`) of the first argument, a `ChartDateType` enum instance: `_fetchFromServer` compares that argument with `ChartDateType` instances (`s1_s2/src/page/charge_sessions/repository/charger_chart_http_repository.dart @0x2990fc0` to `@0x2991030`) and passes it on (`@0x29910cc`); offset 0xf is the name (`off_10`) of `day` (`objs.txt Obj!ChartDateType@4210741`), `week` (`objs.txt Obj!ChartDateType@4210721`), `month` (`objs.txt Obj!ChartDateType@4210701`) or `year` (`objs.txt Obj!ChartDateType@42106e1`) |

AE1X0 sender (`Map<String, String?>`, five pairs, `r2 = 20`, `third_device/src/module/ae1x0/history/widget/meter_chart_logic.dart @0x2ca2974`; every value is read from the chart parameter map that `getChartParams()` (`@0x2ca2878`) returns, keys `device_sn`, `start`, `end`, `phase`, `type`):

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String? | yes | `"<device sn>"` | `third_device/src/module/ae1x0/history/widget/meter_chart_logic.dart @0x2ca2980` |
| `start_time` | String? | yes | not decoded | `@0x2ca29e0` (read from key `start`) |
| `end_time` | String? | yes | not decoded | `@0x2ca2a3c` (read from key `end`) |
| `phase` | String? | yes | not decoded | `@0x2ca2a98` |
| `type` | String? | yes | not decoded | `@0x2ca2af8` |

The AE1X0 sender also writes `phase` and `device_sn` into the parameter map itself first (`@0x2ca28b4`, `@0x2ca2930`).

## `param_type`/`cmd`

n/a

## Response model (link)

AE1X0 meter: `MeterEnergyAnalysisModel` ([../../../../models/meter_energy_analysis_model.md](../../../../models/meter_energy_analysis_model.md)), `fromJson` called at `third_device/src/module/ae1x0/history/widget/meter_chart_logic.dart @0x2ca2fc8`. S1/S2: `S1S2ChargerSessionChartModel` (`s1_s2/src/page/charge_sessions/model/charger_session_chart_model.dart`, `fromJson @0x2993490`; keys `data`, `pps_total`, `energy_unit`, `power_unit`, `update_time`, `data_trend`, with the element classes `DataTrend` and `PpsTotal`, [../../../../models/s1_s2_charger_session_chart_model.md](../../../../models/s1_s2_charger_session_chart_model.md)), called at `s1_s2/src/page/charge_sessions/repository/charger_chart_http_repository.dart @0x2991e24`.

## Response

All fields live in the two model pages (wrapper `code`, `msg`, `data` as in [encryption.md](../../../encryption.md#response-handling-and-error-codes)). The S1/S2 SDK result carries the chart document inside `data` as in [energy_options](energy_options.md#response) (JSON text or map; not re-traced here).

## Example request/response

Request, synthesized (S1/S2 sender)

```json
{ "path": "power_service/v2/device/energy_analysis", "method": "POST",
  "param": { "device_sn": "<device sn>", "start_time": "2026-10", "end_time": "2026-10", "type": "<chart type>" } }
```

Response: no captured response; the key lists are on the model pages.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or logs it; the shared transport codes are in [encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `S1S2DeviceCommand.getChargeSessionChartModel` (`s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2991c18`) called by `_fetchFromServer` (`s1_s2/src/page/charge_sessions/repository/charger_chart_http_repository.dart @0x2990f58`, call `@0x29910cc`): the S1/S2 charge-session chart page (package `s1_s2`).
- `Ae1x0MeterChartLogic.requestChartData` (`third_device/src/module/ae1x0/history/widget/meter_chart_logic.dart @0x2ca26f8`), called from `ae1x0_history_page.dart` (`didPop`), `meter_chart_widget.dart` (`build`, `initState`) and `ae1x0_home_logic.dart` (`_updateWifiSignal`): the history page of the AE1X0 meter (package `third_device`).

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 pool as a code-referenced URL; see the inventory row `since`). 3.24.3: present (new). since: 3.24.3. Both response models are new in 3.24.3 (`MeterEnergyAnalysisModel`, `S1S2ChargerSessionChartModel`).

## Known unknowns

- The value domain of `type` and `phase` in the AE1X0 sender: the values come from the map returned by `getChartParams()` (`third_device/src/module/ae1x0/history/widget/meter_chart_logic.dart @0x2ca2878`), which the chart widget fills; the S1/S2 `type` is traced in Request. — traced 2026-10-20: the AE1X0 chart widget that fills the parameter map was not followed
- Whether both device families return the same layout is not known; the two models differ.
- Server behaviour is not known.

## Device-tested by

none
