> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# check_update

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_installer_svc/v2/ota/batch/check_update`, method: not extracted by the inventory <!-- TODO -->; string-only: `flutter_charging_beginning/beginning/state_cards/firmware_upgrade/firmware_upgrade_controller.dart @0x2b0d2a4`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "unknown (URL literal only, no `*Http*` call)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `path` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/firmware_upgrade/firmware_upgrade_controller.dart @0x2b0d200` |
| `method` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/firmware_upgrade/firmware_upgrade_controller.dart @0x2b0d200` |
| `param` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/firmware_upgrade/firmware_upgrade_controller.dart @0x2b0d200` |

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

- `flutter_charging_beginning/beginning/state_cards/firmware_upgrade/firmware_upgrade_controller.dart`: `<anonymous closure> in FirmwareUpgradeController::checkDeviceUpdate` @0x2b0d200 (URL literal only, no `*Http*` call); `<anonymous closure> in FirmwareUpgradeController::checkUpgradeViaMultiDeploy` @0x2b0f898 (URL literal only, no `*Http*` call)

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
