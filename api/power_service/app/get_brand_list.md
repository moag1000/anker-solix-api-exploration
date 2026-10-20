> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_brand_list

## Purpose

Reads the list of vehicle brands for the add-vehicle flow of the EV charger (caller `AddVehicleController::getBrandListIfNeed`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`get_vehicle_brands` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/get_brand_list` (asm-traced): the command map `{"path", "method", "param"}` built in `AKIotEVChargeCommand::getEvBrandList` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6b5a4`) holds the path string at `@0x2c6b608` and the method string `"POST"` at `@0x2c6b620`; it is passed to the SDK handler `akiot.cloud_api` (`handle`, `@0x2c6b66c`).

## Encrypted?

encrypted: "unknown (URL literal only, no `*Http*` call)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) No request fields: the `param` value of the command map is the empty map literal (`THR::empty_array`, `Map._fromLiteral` at `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6b5c8`).

## `param_type`/`cmd`

n/a

## Response model (link)

`ev_charger::EvBrandListModel` (`data/models.json` key; no models page): the command passes the type argument `<EvBrandListModel>` to the SDK handler call (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6b64c`, `handle` `@0x2c6b66c`); the SDK parses the body outside the code read here.

## Response

(asm-traced) `EvBrandListModel` top-level keys (`data/models.json`): `data` (String), `brand_list` (unknown).

## Example request/response

Request, synthesized: `param` is the empty object.

```json
{"path": "/power_service/v1/app/get_brand_list", "method": "POST", "param": {}}
```

Response: not synthesized (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart`: `getEvBrandList` @0x2c6b5a4 (URL literal only, no `*Http*` call; sends in the same function (`AKIoTKitManagerImpl::handle`); resolved from the URL literal at `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6b608` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

Called from:

- `ev_charger/src/ev_charger/page/vehicle/widgets/add_vehicle_controller.dart::getBrandListIfNeed`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- How the SDK handler turns the body into `EvBrandListModel`: the handler is not in the asm tree read; only the type argument is read here.
- Encryption: the call is made by the command map directly to the SDK handler (path C, `api/encryption.md`); the "Encrypted?" line above is the inventory default.

## Device-tested by

none
