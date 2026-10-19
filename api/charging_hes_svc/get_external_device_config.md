> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_external_device_config

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/get_external_device_config`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart @0x28dfe3c`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `stationId` | ? | ? | ? | `charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart @0x28dfd20` |
| `pn` | ? | ? | ? | `charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart @0x28dfd20` |

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

- `charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart`: `getExternalDeviceList` @0x28dfd20 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart::addHeatPump`
- `charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart::didPopNext`
- `charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart::onReady`
- `charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart::pushPage`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
