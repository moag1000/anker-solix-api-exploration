> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# delete_installer_inviting_member

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/share_device/delete_installer_inviting_member`, method: not extracted by the inventory <!-- TODO -->; string-only: `ev_charger/src/ev_charger/page/home/setting/device_share_members/network/device_share_network.dart @0x430a048`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `installerUserId` | ? | ? | ? | `ev_charger/src/ev_charger/page/home/setting/device_share_members/network/device_share_network.dart @0x4309fd0` |
| `deviceSn` | ? | ? | ? | `ev_charger/src/ev_charger/page/home/setting/device_share_members/network/device_share_network.dart @0x4309fd0` |

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

- `ev_charger/src/ev_charger/page/home/setting/device_share_members/network/device_share_network.dart`: `deleteInstallerInvite` @0x4309fd0 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
