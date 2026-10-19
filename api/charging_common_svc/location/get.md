> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_common_svc/location/get`, method: not extracted by the inventory <!-- TODO -->; string-only: `ak_iot_common_charging/src/weather/weather_impl.dart @0x2b11f9c`
(literal also at 4 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `identifier_type` | ? | ? | ? | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2b11f18` |
| `identifier_id` | ? | ? | ? | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2b11f18` |
| `business_type` | ? | ? | ? | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2b11f18` |

Rows are the union over 5 senders; `source` is the first sender that sets the key.

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

- `ak_iot_common_charging/src/weather/weather_impl.dart`: `fetchSavedLocation` @0x2b11f18 (request; encrypted: default-true (requestHttp) — verify)
- `electricity_price/components/dynamic_price/setting/electricty_place_smart_logic.dart`: `onReady` @0x298f620 (encryptionRequestHttp; encrypted: true)
- `electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart`: `refreshLocation` @0x2c152a0 (request; encrypted: default-true (requestHttp) — verify)
- `micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart`: `_fetchLocation` @0x2e8cf84 (encryptionRequestHttp; encrypted: true)
- `unity/src/main/weather/weather_manager.dart`: `fetchDefaultLocation` @0x451c05c (encryptionRequestHttp; encrypted: true)

Called from:

- `electricity_price/components/dynamic_price/setting/electricty_place_smart_view.dart::_refreshAutoDisasterLocation`
- `electricity_price/components/dynamic_price/setting/electricty_place_smart_view.dart::_updateAutoDisasterLocation`
- `electricity_price/components/dynamic_price/util/place_selection_helper.dart::_loadInitialPlace`
- `electricity_price/components/dynamic_price/util/place_selection_helper.dart::_loadSelectedPlace`
- `micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart::beginTapFlow`
- `station_home/src/weather/weather_service.dart::_fetchWeatherData`
- `unity/src/main/weather/weather_display_view.dart::_navigateToPlaceSelectionView`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
