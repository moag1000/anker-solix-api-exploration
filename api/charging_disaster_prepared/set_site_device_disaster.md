> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

3.24.3: string present in the object pool, no code reference found (present in 3.18.0 with a sender)

# set_site_device_disaster

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_disaster_prepared/set_site_device_disaster`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a1782/module_list/modules_logic.dart @0x1dc6248`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `type` | ? | ? | ? | `charging/ui/page/device/a1782/module_list/modules_logic.dart @0x1dc5f6c` |
| `identifier_id` | ? | ? | ? | `charging/ui/page/device/a1782/module_list/modules_logic.dart @0x1dc5f6c` |
| `auto_disaster_switch` | ? | ? | ? | `charging/ui/page/device/a1782/module_list/modules_logic.dart @0x1dc5f6c` |

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

- `charging/ui/page/device/a1782/module_list/modules_logic.dart`: `_updateAutoDisasterSwitch` @0x1dc5f6c (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: string present in the object pool, no code reference found. since: ≤3.18.0.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
