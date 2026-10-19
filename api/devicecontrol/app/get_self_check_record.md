> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_self_check_record

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/devicecontrol/v1/app/get_self_check_record`, method: not extracted by the inventory <!-- TODO -->; string-only: `flutter_charging_beginning/beginning/state_cards/self_check/new_system_test_controller.dart @0x2aca6d8`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/self_check/new_system_test_controller.dart @0x2aca588` |
| `device_sn` | ? | ? | ? | `flutter_charging_beginning/beginning/state_cards/self_check/new_system_test_controller.dart @0x2aca588` |

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

- `flutter_charging_beginning/beginning/state_cards/self_check/new_system_test_controller.dart`: `_fetchSelfCheckRecord` @0x2aca588 (encryptionRequestHttp; encrypted: true)
- `flutter_charging_beginning/beginning/state_cards/self_check/self_check_fail_controller.dart`: `_fetchSelfCheckRecord` @0x2ad2f1c (encryptionRequestHttp; encrypted: true)

Called from:

- `flutter_charging_beginning/beginning/state_cards/self_check/new_system_test_controller.dart::onReady`
- `flutter_charging_beginning/beginning/state_cards/self_check/self_check_fail_controller.dart::onReady`

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
