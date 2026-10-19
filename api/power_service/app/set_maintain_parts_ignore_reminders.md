> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# set_maintain_parts_ignore_reminders

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/set_maintain_parts_ignore_reminders`, method: not extracted by the inventory <!-- TODO -->; string-only: `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x39ff1bc`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x39fefe8` |
| `item_id` | ? | ? | ? | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x39fefe8` |
| `item_name` | ? | ? | ? | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x39fefe8` |
| `maintenance_items` | ? | ? | ? | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x39fefe8` |
| `ignore_reminders` | ? | ? | ? | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x39fefe8` |

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

- `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart`: `setMaintainPartsIgnoreRemindersRequest` @0x39fefe8 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
