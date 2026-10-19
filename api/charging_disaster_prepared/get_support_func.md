> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_support_func

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_disaster_prepared/get_support_func`, method: not extracted by the inventory <!-- TODO -->; string-only: `unity/src/main/weather/weather_manager.dart @0x451d8cc`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `type` | ? | ? | ? | `unity/src/main/weather/weather_manager.dart @0x451d6dc` |
| `identifier_id` | ? | ? | ? | `unity/src/main/weather/weather_manager.dart @0x451d6dc` |

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

- `unity/src/main/weather/weather_manager.dart`: `fetchSupportCountryCodes` @0x451d6dc (encryptionRequestHttp; encrypted: true)

Called from: `unity/src/main/weather/weather_display_view.dart::_navigateToPlaceSelectionView`

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
