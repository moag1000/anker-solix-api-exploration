> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# self_check_report

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/devicecontrol/v1/app/self_check_report`, method: not extracted by the inventory <!-- TODO -->; string-only: `flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart @0x2acd760`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart @0x2acd180` |
| `device_sn` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart @0x2acd180` |
| `self_check_status` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart @0x2acd180` |
| `fail_code` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart @0x2acd180` |
| `capability` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart @0x2acd180` |
| `start_time` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart @0x2acd180` |
| `end_time` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart @0x2acd180` |

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

- `flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart`: `_reportSelfCheckResult` @0x2acd180 (encryptionRequestHttp; encrypted: true)

Called from:

- `flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart::selfCheck`

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
