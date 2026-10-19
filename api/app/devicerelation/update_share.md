> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# update_share

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/app/devicerelation/update_share`, method: not extracted by the inventory <!-- TODO -->; string-only: `ev_charger/src/ev_charger/page/home/setting/device_share_members/network/device_share_network.dart @0x430ba68`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `ev_charger/src/ev_charger/page/home/setting/device_share_members/network/device_share_network.dart @0x430b8e4` |
| `sub_devices` | ? | ? | ? | `ev_charger/src/ev_charger/page/home/setting/device_share_members/network/device_share_network.dart @0x430b8e4` |
| `is_delete` | ? | ? | ? | `ev_charger/src/ev_charger/page/home/setting/device_share_members/network/device_share_network.dart @0x430b8e4` |
| `member_type` | ? | ? | ? | `ev_charger/src/ev_charger/page/home/setting/device_share_members/network/device_share_network.dart @0x430b8e4` |

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

- `ev_charger/src/ev_charger/page/home/setting/device_share_members/network/device_share_network.dart`: `deleteDeviceShareMember` @0x430b8e4 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
