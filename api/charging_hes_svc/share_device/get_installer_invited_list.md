> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_installer_invited_list

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/share_device/get_installer_invited_list`, method: not extracted by the inventory <!-- TODO -->; string-only: `ev_charger/src/ev_charger/page/home/setting/device_share_members/network/device_share_network.dart @0x2aaf3f8`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `deviceSn` | ? | ? | ? | `ev_charger/src/ev_charger/page/home/setting/device_share_members/network/device_share_network.dart @0x2aaf398` |

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

- `ev_charger/src/ev_charger/page/home/setting/device_share_members/network/device_share_network.dart`: `getDeviceShareInstallerList` @0x2aaf398 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
