> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_parts_maintenance_logs

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/get_parts_maintenance_logs`, method: not extracted by the inventory <!-- TODO -->; string-only: `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x2ad611c`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `item_id` | ? | ? | ? | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x2ad5edc` |
| `item_name` | ? | ? | ? | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x2ad5edc` |
| `maintenance_items` | ? | ? | ? | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x2ad5edc` |
| `device_sn` | ? | ? | ? | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x2ad5edc` |
| `page` | ? | ? | ? | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x2ad5edc` |
| `page_size` | ? | ? | ? | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x2ad5edc` |

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

- `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart`: `getPartsMaintenanceLogsRequest` @0x2ad5edc (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
