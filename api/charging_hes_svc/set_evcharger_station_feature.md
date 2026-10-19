> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# set_evcharger_station_feature

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/set_evcharger_station_feature`, method: not extracted by the inventory <!-- TODO -->; string-only: `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x39605b8`

## Encrypted?

encrypted: "unknown (URL literal only, no `*Http*` call)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `evChargerSn` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x3960414` |
| `path` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x3960414` |
| `method` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x3960414` |
| `param` | ? | ? | ? | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x3960414` |

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

- `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart`: `setEvChargerHesStationFeature` @0x3960414 (URL literal only, no `*Http*` call)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
