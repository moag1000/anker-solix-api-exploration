> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_vehicle_list

## Purpose

Lists the vehicles of the account (name, brand, model, year, default flag, smart-charging flag, battery capacity, state of charge); the EV charger app shows them in the vehicle list and the vehicle picker, and the schedule-charge feature parses the same answer.

## Upstream name

`get_user_vehicles` (upstream-confirmed, `api/apitypes.py` line 156; upstream comment: "list of vehicles with details for account").

## Method+URL

`POST /power_service/v1/app/vehicle/get_vehicle_list` (asm-traced). Two senders: `AKIotEVChargeCommand.getEvList` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x2ab3ebc`; path literal `@0x2ab3f94`, `"POST"` `@0x2ab3fac`) and `ScheduleNetwork.getVehicleList` (`ev_charger/src/ev_charger/page/home/schedule_charge/network/ schedule_network.dart @0x284eb78`; path literal `@0x284ec28`, passed to `_requestHttp` at `@0x284ec30`). The file name of the second sender has a leading space (`%20` in the asm path).

## Encrypted?

Both senders are direct SDK calls, path C (asm-traced): `getEvList` calls `handle` with `akiot.cloud_api` (`ev_charge_command.dart @0x2ab3fe8`, call `@0x2ab3ff8`); `ScheduleNetwork._requestHttp` does the same (`schedule_network.dart @0x284f780`, call `@0x284f790`). The inventory row of the schedule sender says `encrypted: false` with a note about a plain `requestHttp` callee; that note does not apply, the callee goes straight to the SDK (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#schedulenetwork_requesthttp), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

Both senders build a `<String, ...>` map whose only possible key is `device_sn`: it is added only when the optional named argument `deviceSn` is not null (`getEvList`: `ev_charge_command.dart` `SetupParameters` `@0x2ab3ec8`, null check `@0x2ab3f30`, key `@0x2ab3f44`; `ScheduleNetwork.getVehicleList`: `schedule_network.dart @0x284ebfc`, key `@0x284ec10`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | no | `<device sn>` | `ev_charge_command.dart @0x2ab3f44` (`getEvList`), `ev_charger/src/ev_charger/page/home/schedule_charge/network/ schedule_network.dart @0x284ec10` (schedule sender); omitted when the argument is null |

Without the key the app lists the account's vehicles; with the key the app passes the serial of the charger whose vehicle list it shows.

## `param_type`/`cmd`

n/a

## Response model (link)

`EvListModel` ([../../../../models/ev_charger_vehicle_models.md](../../../../models/ev_charger_vehicle_models.md#evlistmodel)) for `getEvList` (type argument `@0x2ab3fd8`); `ScheduleVehicleModel` ([../../../../models/ev_charger_vehicle_models.md](../../../../models/ev_charger_vehicle_models.md#schedulevehiclemodel)) for the schedule sender (`ScheduleVehicleModel.fromJson` call `@0x284ed1c`).

## Response

`getEvList` returns `IoTAKResult<EvListModel>`. The schedule sender reads the SDK result itself: it checks the result type (`@0x284ec48` to `@0x284ec50`), takes the key `data` of the result (`@0x284ec60`), decodes it with `jsonDecode` when it is a String (`@0x284ecc8`) and passes the map to `ScheduleVehicleModel.fromJson`; a null map becomes an empty map (`@0x284ecfc`). Failures are turned into a schedule exception (`@0x284ed28`).

| field | type | required | example | source |
|---|---|---|---|---|
| `vehicle_list` | list of `EvListInfoModel` / `VehicleDetail` | no | `[ { ... } ]` | `vehicle_model.dart @0x45abfd8` (`EvListModel`); `schedule_vehicle_model.dart @0x284ed60` (`ScheduleVehicleModel`); element keys on the model page [../../../../models/ev_charger_vehicle_models.md](../../../../models/ev_charger_vehicle_models.md#evlistinfomodel) |

## Example request/response

Request, synthesized

```json
{}
```

Request, synthesized (with a charger)

```json
{ "device_sn": "<device sn>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `EvChargerVehicleListLogic.getVehicleList` (`ev_charger/src/ev_charger/page/home/widget/vehicle_list/ev_charger_vehicle_list_logic.dart @0x2ab3be0`)
- `VehicleEditLogic.fillDefaultEvName` (`ev_charger/src/ev_charger/page/vehicle/vehicle_edit_logic.dart @0x2ab4f20`)
- `VehicleListLogic.refreshList` (`ev_charger/src/ev_charger/page/vehicle/vehicle_list_logic.dart @0x2ab97a0`)
- `DrivingPlanDataChange.mergeFromVehicleList` (`ev_charger/src/ev_charger/page/home/schedule_charge/tools/driving_plan_data_change.dart @0x284e8e4`), through `ScheduleNetwork.getVehicleList`
- `SessionsDetailPage._showVehicleListDialog` (`ev_charger/src/ev_charger/page/home/charge_sessions/sessions_detail/sessions_detail_page.dart @0x39596c0`), through `ScheduleNetwork.getVehicleList`

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x818b8`); the sender function has no literal difference between 3.18.0 and 3.24.3 (`tools/cmp_since.py`: ordered string, integer and type literals compared; branch logic not compared). Not new in 3.24.3: the Task 3.1b inventory change (slashless URL literals) made the URL visible. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- Whether the server filters the vehicle list by `device_sn` or ignores the key is not known.
- No response was captured.

## Device-tested by

none
