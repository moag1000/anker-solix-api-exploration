> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# delete_vehicle

## Purpose

<!-- TODO -->

## Upstream name

`vehicle_delete` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/app/vehicle/delete_vehicle`, method: not extracted by the inventory <!-- TODO -->; string-only: `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x3983924`

## Encrypted?

encrypted: "unknown (URL literal only, no `*Http*` call)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `vehicle_id` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x398389c` |
| `path` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x398389c` |
| `method` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x398389c` |
| `param` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x398389c` |

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

- `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart`: `deleteEv` @0x398389c (URL literal only, no `*Http*` call)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
