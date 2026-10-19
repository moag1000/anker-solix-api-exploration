> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_self_check_config

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/device_svc/v1/get_self_check_config`, method: not extracted by the inventory <!-- TODO -->; string-only: `flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart @0x2ad1184`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys found by the extractor. <!-- TODO -->

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

- `flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart`: `_loadCloudSelfCheckConfig` @0x2ad0f98 (encryptionRequestHttp; encrypted: true)
- `flutter_charging_beginning/beginning/state_cards/self_check/self_check_fail_controller.dart`: `loadCloudSelfCheckConfig` @0x2ad2054 (encryptionRequestHttp; encrypted: true)

Called from:

- `flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart::onReady`
- `flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart::selfCheck`
- `flutter_charging_beginning/beginning/state_cards/self_check/self_check_fail_controller.dart::onReady`
- `flutter_charging_beginning/beginning/state_cards/self_check/self_check_fail_page.dart::_buildFailView`

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
