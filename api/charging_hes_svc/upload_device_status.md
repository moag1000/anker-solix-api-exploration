> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

Removed in 3.24.3 — present in 3.18.0 only

# upload_device_status

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/upload_device_status`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/family/family_main_page_logic.dart @0x1aa2e28`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | ? | ? | `charging/ui/page/family/family_main_page_logic.dart @0x1aa2cb4` |
| `sn` | ? | ? | ? | `charging/ui/page/family/family_main_page_logic.dart @0x1aa2cb4` |
| `local_time` | ? | ? | ? | `charging/ui/page/family/family_main_page_logic.dart @0x1aa2cb4` |
| `time_stamp` | ? | ? | ? | `charging/ui/page/family/family_main_page_logic.dart @0x1aa2cb4` |
| `status` | ? | ? | ? | `charging/ui/page/family/family_main_page_logic.dart @0x1aa2cb4` |

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

- `charging/ui/page/family/family_main_page_logic.dart`: `reportDeviceState` @0x1aa2cb4 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: absent (removed). since: ≤3.18.0.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
