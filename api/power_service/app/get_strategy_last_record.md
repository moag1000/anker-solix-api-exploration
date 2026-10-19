> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_strategy_last_record

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/get_strategy_last_record`, method: not extracted by the inventory <!-- TODO -->; string-only: `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x360a744`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `extender_system_id` | ? | ? | ? | `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x360a6ac` |
| `strategy_type` | ? | ? | ? | `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x360a6ac` |

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

- `oe_a7320/src/oe_a7320/network/range_extender_network.dart`: `getStrategyLastRecord` @0x360a6ac (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
