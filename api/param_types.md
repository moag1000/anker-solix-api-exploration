> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# param_types

Master table of the `param_type` values sent to [`set_site_device_param`](power_service/site/set_site_device_param.md) (and read with `get_site_device_param`). This page owns the `param_type` and `cmd` values; the request and `param_data` structure of each type lives on the endpoint page.

The rows list every member of the upstream enum `SolixParmType` (`api/apitypes.py`, upstream-confirmed). Only row 19 is re-verified against App 3.24.3 so far; all other cells are pending Task 3.4. Values from the old documentation are deliberately not carried over, because several of its `cmd` numbers were raw Smi values (twice the real value; see [../METHODOLOGY.md](../METHODOLOGY.md#smi-rule-reading-numbers-from-blutter-output)).

| param_type | upstream name (apitypes.py SolixParmType) | set function | get function | cmd (decoded, citation) | param_data keys | GET model | tag |
|---|---|---|---|---|---|---|---|
| 4 | `SOLARBANK_SCHEDULE` | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | `upstream-confirmed` (name only) |
| 6 | `SOLARBANK_2_SCHEDULE` | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | `upstream-confirmed` (name only) |
| 9 | `SOLARBANK_SCHEDULE_ENFORCED` | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | `upstream-confirmed` (name only) |
| 12 | `SOLARBANK_TARIFF_SCHEDULE` | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | `upstream-confirmed` (name only) |
| 13 | `SOLARBANK_AUTHORIZATIONS` | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | `upstream-confirmed` (name only) |
| 16 | `SOLARBANK_POWERDOCK` | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | `upstream-confirmed` (name only) |
| 18 | `SOLARBANK_STATION` | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | `upstream-confirmed` (name only) |
| 19 | `SOLARBANK_POWER_LIMIT` | `HttpRequestControllerImpl::setSiteDevicePowerLimit` (`http_request_repository_impl.dart @0x4355750`; `"19"` is a string literal at `@0x43558ac`) | none: the app has no get call for type 19; the current state is read with [`get_power_limit`](power_service/site/get_power_limit.md) (`getSitePowerLimit`, `http_request_repository_impl.dart @0x2378fb4`) | **123**: raw 246 (`mov x16, #0xf6`) at `http_request_repository_impl.dart @0x43558c4`, stored 32-bit (`stur w16`) at `@0x43558c8`, Smi, 246 / 2 = 123 | `display_type`, `power_limit.limit`, `power_limit.limit_real` (structure and values on [set_site_device_param](power_service/site/set_site_device_param.md#usage-param_type-19-system-output-power-limit)) | [`StationPowerLimitModel`](../models/station_power_limit.md) (via `get_power_limit`) | `asm-traced` |
| 26 | `SOLARBANK_3RD_PARTY_PV` | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | pending Task 3.4 | `upstream-confirmed` (name only) |

Notes:

- `apitypes.py` also carries the commented-out members `SOLARBANK_EV_CHARGER = "23"` and `SOLARBANK_BACKUP = "33"`. They are not part of the enum and are not listed; Task 3.4 decides whether the app uses them.
- The upstream library sends `cmd` 17 for every type through `set_device_parm()` (`api/schedule.py`, default argument `command: int = 17`). For type 19 the app sends 123 (row above). Whether the server accepts both is not known yet; it will be recorded in [../METHODOLOGY.md](../METHODOLOGY.md#known-server-tolerances) once tested.
- 3.18.0 already sent `cmd` 123 for type 19 (3.18.0 `http_request_repository_impl.dart`, raw 246 at `@0x327ff20`, stored 32-bit at `@0x327ff24`).
