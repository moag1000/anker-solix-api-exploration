> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_sns

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_energy_service/get_sns`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a17b1/check_update/check_update_logic.dart @0x36dd76c`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `main_sn` | ? | ? | ? | `charging/ui/page/device/a17b1/check_update/check_update_logic.dart @0x36dd6a0` |
| `macs` | ? | ? | ? | `charging/ui/page/device/a17b1/check_update/check_update_logic.dart @0x36dd6a0` |

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

- `charging/ui/page/device/a17b1/check_update/check_update_logic.dart`: `getDeviceSnByMac` @0x36dd6a0 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/device/a17b1/check_update/check_update_logic.dart::matchDeviceMac`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
