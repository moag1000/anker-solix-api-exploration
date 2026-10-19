> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# ota

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/ota`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x347c124`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `stationId` | ? | ? | ? | `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x42ea618` |
| `delay` | ? | ? | ? | `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x42ea618` |

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

- `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart`: `sendSetTimeOta` @0x42ea618 (requestHttp; encrypted: default-true (requestHttp) — verify); `sendStartOtaUpdate` @0x347bee8 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart::_parseMinSoc`
- `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart::onInit`
- `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart::showChooseTimerView`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
