> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_models

## Purpose

Reads the list of vehicle models for a brand in the EV charger vehicle forms (callers `VehicleEditLogic::getModelList`, `AddVehicleController::getModelListIfNeed`; builder `AKIotEVChargeCommand::getEvModelList`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`get_vehicle_brand_models` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/get_models` (asm-traced): the command map `{"path", "method", "param"}` built in `AKIotEVChargeCommand::getEvModelList` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6b2b4`) holds the path string at `@0x2c6b33c` and the method string `"POST"` at `@0x2c6b354`; it is passed to the SDK handler `akiot.cloud_api` (`handle`, `@0x2c6b3a0`).

## Encrypted?

encrypted: "unknown (URL literal only, no `*Http*` call)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) The builder `AKIotEVChargeCommand::getEvModelList` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6b2b4`) first builds the parameter literal `<String, dynamic>` (`@0x2c6b2f4`) with the keys below (values are parameters of the builder), then wraps it as `param` in the command map `{"path", "method", "param"}`.

| field | type | required | example | source |
|---|---|---|---|---|
| `brand_name` | ? | yes | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6b2e0` |

## `param_type`/`cmd`

n/a

## Response model (link)

- `ev_charger::EvModelListModel`. The command passes the type argument `<EvModelListModel>` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6b380`) to the SDK handler call; the SDK parses the body outside the code read here.

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `EvModelListModel` top-level keys (`data/models.json`, `ev_charger::EvModelListModel`): `data` (String), `model_list` (unknown).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "brand_name": "<?>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart`: `getEvModelList` @0x2c6b2b4 (URL literal only, no `*Http*` call; sends in the same function (`AKIoTKitManagerImpl::handle`); resolved from the URL literal at `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6b33c` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

Called from:

- `ev_charger/src/ev_charger/page/vehicle/vehicle_edit_logic.dart::getModelList`
- `ev_charger/src/ev_charger/page/vehicle/widgets/add_vehicle_controller.dart::getModelListIfNeed`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `brand_name` (parameters of the builder; the literal is `<String, dynamic>`).
- How the SDK handler turns the body into `EvModelListModel`: the handler is not in the asm tree read; only the type argument is read here.
- Encryption: the call is made by the command map directly to the SDK handler (path C, `api/encryption.md`); the "Encrypted?" line above is the inventory default.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
