> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# batch_maintain_oil_engine_parts

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/batch_maintain_oil_engine_parts`, method: not extracted by the inventory <!-- TODO -->; string-only: `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x3a02318`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `item_id` | ? | ? | ? | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x3a02130` |
| `item_name` | ? | ? | ? | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x3a02130` |
| `maintenance_items` | ? | ? | ? | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x3a02130` |
| `device_sn` | ? | ? | ? | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x3a06800` |
| `parts_maintenance_list` | ? | ? | ? | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x3a06800` |

Rows are the union over 2 senders; `source` is the first sender that sets the key.

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

- `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart`: `batchMaintainOilEnginePartsRequest` @0x3a02130 (encryptionRequestHttp; encrypted: true); `batchMaintainOilEnginePartsRequestList` @0x3a06800 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
