> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_back_up_history

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/get_back_up_history`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart @0x28ef610`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | ? | ? | `charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart @0x28ef504` |

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

- `charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart`: `getBackupHistoryListFromNet` @0x28ef504 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/util/demosite_util_impl.dart`: `DemoSiteUtilImpl` @0x4a33a6c (URL literal only, no `*Http*` call)

Called from:

- `charging/boostrap_impl.dart::DIInit`
- `charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart::onReady`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
