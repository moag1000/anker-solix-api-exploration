> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_model_years

## Purpose

<!-- TODO -->

## Upstream name

`get_vehicle_model_years` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/app/get_model_years`, method: not extracted by the inventory <!-- TODO -->; string-only: `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6b018`

## Encrypted?

encrypted: "unknown (URL literal only, no `*Http*` call)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `brand_name` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6af74` |
| `model_name` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6af74` |
| `path` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6af74` |
| `method` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6af74` |
| `param` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6af74` |

## `param_type`/`cmd`

n/a

## Response model (link)

<!-- TODO -->

## Response

<!-- TODO -->

## Example request/response

<!-- TODO -->

## Errors seen

`api/errors.md`: <!-- TODO -->

## Callers in app

- `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart`: `getEvYearList` @0x2c6af74 (URL literal only, no `*Http*` call; sends in the same function (`AKIoTKitManagerImpl::handle`); resolved from the URL literal at `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c6b018` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

Called from:

- `ev_charger/src/ev_charger/page/vehicle/vehicle_edit_logic.dart::getYearList`
- `ev_charger/src/ev_charger/page/vehicle/widgets/add_vehicle_controller.dart::getYearListIfNeed`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
