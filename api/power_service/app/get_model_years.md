> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_model_years

## Purpose

Reads the list of production years for a vehicle brand and model in the EV charger vehicle forms (callers `VehicleEditLogic::getYearList`, `AddVehicleController::getYearListIfNeed`; builder `AKIotEVChargeCommand::getEvYearList`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`get_vehicle_model_years` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/get_model_years` (asm-traced): the command map `{"path", "method", "param"}` built in `AKIotEVChargeCommand::getEvYearList` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6af74`) holds the path string at `@0x2c6b018` and the method string `"POST"` at `@0x2c6b030`; it is passed to the SDK handler `akiot.cloud_api` (`handle`, `@0x2c6b07c`).

## Encrypted?

Direct SDK call, path C (asm-traced): the command function builds the map `{path, method, param}` and calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6b07c`) and no `*Http*` wrapper, so the inventory flag `encrypted: unknown` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../sdk_senders.md](../../sdk_senders.md#the-common-envelope), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)).

## Request

(asm-traced) The builder `AKIotEVChargeCommand::getEvYearList` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6af74`) first builds the parameter literal `<String, dynamic>` (`@0x2c6afd0`) with the keys below (values are parameters of the builder), then wraps it as `param` in the command map `{"path", "method", "param"}`.

| field | type | required | example | source |
|---|---|---|---|---|
| `brand_name` | string | yes | | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6afa8` |
| `model_name` | string | yes | | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6afbc` |

Typing (two-hop, asm-traced): in `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` the builder `getEvYearList` takes two untyped parameters (`SetupParameters(dynamic _ ...)` `@0x2c6af80`). Its caller `VehicleEditLogic.getYearList` (`ev_charger/src/ev_charger/page/vehicle/vehicle_edit_logic.dart @0x43e2a44`, `@0x43e2a58`) replaces a null brand and a null model by the String literal `""`, so both are strings.

## `param_type`/`cmd`

n/a

## Response model (link)

- `ev_charger::EvYearListModel`. The command passes the type argument `<EvYearListModel>` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6b05c`) to the SDK handler call; the SDK parses the body outside the code read here.

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `EvYearListModel` top-level keys (`data/models.json`, `ev_charger::EvYearListModel`): `data` (String), `year_list` (unknown).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "brand_name": "<brand_name>",
  "model_name": "<model_name>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `VehicleEditLogic.getYearList` (`ev_charger/src/ev_charger/page/vehicle/vehicle_edit_logic.dart @0x43e2a5c`)
- `AddVehicleController.getYearListIfNeed` (`ev_charger/src/ev_charger/page/vehicle/widgets/add_vehicle_controller.dart @0x2c6adfc`)
- `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart`: `getEvYearList` @0x2c6af74 (URL literal only, no `*Http*` call; sends in the same function (`AKIoTKitManagerImpl::handle`); resolved from the URL literal at `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6b018` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

Called from:

- `ev_charger/src/ev_charger/page/vehicle/vehicle_edit_logic.dart::getYearList`
- `ev_charger/src/ev_charger/page/vehicle/widgets/add_vehicle_controller.dart::getYearListIfNeed`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- How the SDK handler turns the body into `EvYearListModel`: the handler is not in the asm tree read; only the type argument is read here. — reclassified: server (the parser is in the native SDK handler, outside the asm tree)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
