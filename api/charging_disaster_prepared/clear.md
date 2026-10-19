> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

Removed in 3.24.3 — present in 3.18.0 only

# clear

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_disaster_prepared/clear`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a1782/a1782_setting/menu_controller/a1782_restore_default_controller.dart @0x366d61c`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `identifier_id` | ? | ? | ? | `charging/ui/page/device/a1782/a1782_setting/menu_controller/a1782_restore_default_controller.dart @0x366d558` |
| `type` | ? | ? | ? | `charging/ui/page/device/a1782/a1782_setting/menu_controller/a1782_restore_default_controller.dart @0x366d558` |

Rows are the union over 2 senders; `source` is the first sender that sets the key.

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

- `charging/ui/page/device/a1782/a1782_setting/menu_controller/a1782_restore_default_controller.dart`: `clearDisasterPreparednessInfo` @0x366d558 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart`: `clearDisasterPreparednessInfo` @0x1f4a208 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: absent (removed). since: ≤3.18.0.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
