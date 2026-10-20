> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_brand_list

## Purpose

Reads the list of vehicle brands for the add-vehicle flow of the EV charger (caller `AddVehicleController::getBrandListIfNeed`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`get_vehicle_brands` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/get_brand_list` (asm-traced): the command map `{"path", "method", "param"}` built in `AKIotEVChargeCommand::getEvBrandList` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6b5a4`) holds the path string at `@0x2c6b608` and the method string `"POST"` at `@0x2c6b620`; it is passed to the SDK handler `akiot.cloud_api` (`handle`, `@0x2c6b66c`).

## Encrypted?

Direct SDK call, path C (asm-traced): the command function builds the map `{path, method, param}` and calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6b66c`) and no `*Http*` wrapper, so the inventory flag `encrypted: unknown` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../sdk_senders.md](../../sdk_senders.md#the-common-envelope), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)).

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

- `AddVehicleController.getBrandListIfNeed` (`ev_charger/src/ev_charger/page/vehicle/widgets/add_vehicle_controller.dart @0x2c6b4b8`)
- `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart`: `getEvBrandList` @0x2c6b5a4 (URL literal only, no `*Http*` call; sends in the same function (`AKIoTKitManagerImpl::handle`); resolved from the URL literal at `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6b608` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

Called from:

- `ev_charger/src/ev_charger/page/vehicle/widgets/add_vehicle_controller.dart::getBrandListIfNeed`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Response model not fully read: it is named only by the type argument `<EvBrandListModel>` of the handler call; the SDK parser that builds it is not in the asm tree read, so this page stays string-only. — reclassified: server (the parser is in the native SDK handler, outside the asm tree)
- How the SDK handler turns the body into `EvBrandListModel`: the handler is not in the asm tree read; only the type argument is read here. — reclassified: server (the parser is in the native SDK handler, outside the asm tree)

## Device-tested by

none
