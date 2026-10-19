> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# check_device_bluetooth_password

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/check_device_bluetooth_password`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a5101/setting/italy_selfcheck/italy_selfcheck_request.dart @0x3ea1bdc`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | ? | ? | `charging/ui/page/device/a5101/setting/italy_selfcheck/italy_selfcheck_request.dart @0x3ea18d4` |
| `pn` | ? | ? | ? | `charging/ui/page/device/a5101/setting/italy_selfcheck/italy_selfcheck_request.dart @0x3ea18d4` |
| `sn` | ? | ? | ? | `charging/ui/page/device/a5101/setting/italy_selfcheck/italy_selfcheck_request.dart @0x3ea18d4` |
| `p_secret` | ? | ? | ? | `charging/ui/page/device/a5101/setting/italy_selfcheck/italy_selfcheck_request.dart @0x3ea18d4` |
| `salt` | ? | ? | ? | `charging/ui/page/device/a5101/setting/italy_selfcheck/italy_selfcheck_request.dart @0x3ea18d4` |

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

- `charging/ui/page/device/a5101/setting/italy_selfcheck/italy_selfcheck_request.dart`: `checkDeviceBluetoothPassword` @0x3ea18d4 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
