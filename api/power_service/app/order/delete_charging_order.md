> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# delete_charging_order

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/order/delete_charging_order`, method: not extracted by the inventory <!-- TODO -->; string-only: `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x395b540`

## Encrypted?

encrypted: "unknown (URL literal only, no `*Http*` call)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `path` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x395b4e4` |
| `method` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x395b4e4` |
| `param.order_id` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x395b4e4` |
| `param.device_sn` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x395b4e4` |

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

- `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart`: `deleteChargingSession` @0x395b4e4 (URL literal only, no `*Http*` call)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
