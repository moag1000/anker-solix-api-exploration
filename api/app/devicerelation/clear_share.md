> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# clear_share

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/app/devicerelation/clear_share`, method: not extracted by the inventory <!-- TODO -->; string-only: `base_service/view/general_setting/remove_device_controller.dart @0x2816d4c`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `base_service/view/general_setting/remove_device_controller.dart @0x2816cb0` |
| `member_type` | ? | ? | ? | `base_service/view/general_setting/remove_device_controller.dart @0x2816cb0` |

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

- `base_service/view/general_setting/remove_device_controller.dart`: `_clearShareDevice` @0x2816cb0 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `balcony/src/ae100/settings/ae100_remove_device_controller.dart::_handleDeviceRemoval`
- `base_service/view/general_setting/remove_device_controller.dart::_handleDeviceRemoval`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
