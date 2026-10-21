> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get

## Purpose

Reads the saved or default weather/price location of a site (callers `ElectricityPlaceSmartLogic::onReady`, `LocalAutoDisasterFeature::refreshLocation`, `YesterdayEarningTipsLogic::_fetchLocation`, `WeatherManager::fetchDefaultLocation`, `ChargingWeatherHttpAdapter::fetchSavedLocation`; UI callers `ElectricityPlaceSmartView::_refreshAutoDisasterLocation`, `PlaceSelectionHelper::_loadInitialPlace`, `WeatherService::_fetchWeatherData`) (string-only: the caller names are in the page's caller list, the chain is not in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_common_svc/location/get` (asm-traced for the method at all five senders; the page stays string-only for other reasons, see Known unknowns).

- `ElectricityPlaceSmartLogic::onReady` (`electricity_price/components/dynamic_price/setting/electricty_place_smart_logic.dart @0x298f620`): URL string `@0x298f774`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x298f76c`, sent through `encryptionRequestHttp` (`@0x298f79c`).
- `YesterdayEarningTipsLogic::_fetchLocation` (`micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart @0x2e8cf84`): URL `@0x2e8d13c`, `Method.post` (`pp+0xa7e0`) `@0x2e8d134`, `encryptionRequestHttp` `@0x2e8d164`.
- `WeatherManager::fetchDefaultLocation` (`unity/src/main/weather/weather_manager.dart @0x451c05c`): URL `@0x451c258`, `Method.post` (`pp+0xa7e0`) `@0x451c250`, `encryptionRequestHttp` `@0x451c27c`.
- `LocalAutoDisasterFeature::refreshLocation` (`electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart @0x2c152a0`): URL `@0x2c15384`, sent through `HttpHelper::request` (`@0x2c153a4`) without a `method` argument (argument descriptor `@0x2c153a0`). `HttpHelper::request` (`electricity_price/components/electricity_price_common/http/http_helper.dart @0x2c1447c`) declares `method` as an optional named parameter with default null (`@0x2c14488`) and substitutes `Method.post` (`pp+0xa7e0`) for null (`electricity_price/components/electricity_price_common/http/http_helper.dart @0x2c14630`).
- `ChargingWeatherHttpAdapter::fetchSavedLocation` (`ak_iot_common_charging/src/weather/weather_impl.dart @0x2b11f18`): URL `@0x2b11f9c`, sent through `StationApiClient::request` (`@0x2b11fa4`), which puts the string `"POST"` under the envelope key `method` (`station_home/src/http/station_api_client.dart @0x2a4445c`) and hands the envelope to `AkIotKitFlutter::handle` (`station_home/src/http/station_api_client.dart @0x2a444c0`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: one field type is not read) Five senders build the same three keys in a map literal. Four use `<String, Object>` (`electricity_price/components/dynamic_price/setting/electricty_place_smart_logic.dart @0x298f728`, `micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart @0x2e8d0f0`, `unity/src/main/weather/weather_manager.dart @0x451c178`) or `<String, dynamic>` (`electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart @0x2c15358`, `ak_iot_common_charging/src/weather/weather_impl.dart @0x2b11f8c`), which name no value type, so only the two integer keys are typed, from their stored immediates.

| field | type | required | example | source |
|---|---|---|---|---|
| `identifier_type` | int (Smi, w) | yes | `2` (raw immediate 4, 32-bit store) | `electricity_price/components/dynamic_price/setting/electricty_place_smart_logic.dart @0x298f6f8` (value store `@0x298f708`, constant `@0x298f704`); same constant at `micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart @0x2e8d0b8`, `unity/src/main/weather/weather_manager.dart @0x451c140`, `ak_iot_common_charging/src/weather/weather_impl.dart @0x2b11f54`. `electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart @0x2c152e0` stores a field value instead (`LoadField` `@0x2c152f0`, `BoxInt64Instr` `@0x2c152f4`): int (unboxed, x) |
| `identifier_id` | ? | yes | `"<site_id>"` | `electricity_price/components/dynamic_price/setting/electricty_place_smart_logic.dart @0x298f70c` (value `LoadField` `@0x298f71c`, store `@0x298f724`); `ak_iot_common_charging/src/weather/weather_impl.dart @0x2b11f68` (parameter, store `@0x2b11f78`); `electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart @0x2c1530c` (`LoadField` `@0x2c15318`); `micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart @0x2e8d0cc`; `unity/src/main/weather/weather_manager.dart @0x451c154` |
| `business_type` | int (Smi, w) | yes | `0` (the zero register is stored, Smi 0) | `electricity_price/components/dynamic_price/setting/electricty_place_smart_logic.dart @0x298f6e8` (store `@0x298f6f4`); same at `micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart @0x2e8d0e0`, `unity/src/main/weather/weather_manager.dart @0x451c168`, `ak_iot_common_charging/src/weather/weather_impl.dart @0x2b11f7c`. `electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart @0x2c15324` stores 0 or 1: the compare `cmp x0, x17` with `r17 = 4696` (`@0x2c1533c`, `@0x2c15338`) selects `0` (`@0x2c15344`) or `1` (`@0x2c1534c`), shifted to a Smi (`lsl` `@0x2c15350`, store `@0x2c15354`) |

The `identifier_id` type is `?`: every sender stores a value loaded from a field or a parameter whose declared type the asm does not show.

## `param_type`/`cmd`

n/a

## Response model (link)

Different senders parse different classes (no page in `models/` exists for any of them):

- `refreshLocation`: `electricity_price::CommonLocationResponse`, parsed by `CommonLocationResponse.fromJson` at `electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart @0x2c15400` (closure `@0x2c153d8`).
- `ElectricityPlaceSmartLogic::onReady`: `electricity_price::CloudPlace`, parsed by `CloudPlace.fromJson` at `electricity_price/components/dynamic_price/setting/electricty_place_smart_logic.dart @0x298f95c` (success closure `@0x298f7b8`, applied to the value under the key `identifier_location`, read at `@0x298f80c`).
- `_fetchLocation`: no class; the success closure (`micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart @0x2e8d264`) reads `identifier_location` (`@0x2e8d2c8`), then `latitude` (`@0x2e8d2f8`) and `longitude` (`@0x2e8d3ac`) and converts both with `double.parse` (`@0x2e8d374`, `@0x2e8d428`).
- `fetchSavedLocation`: `_parseLocation` returns a `WeatherLocation?` (`ak_iot_common_charging/src/weather/weather_impl.dart @0x2b11fdc`); its body was not read.
- `fetchDefaultLocation`: the success closure was not read.

## Response

(string-only: not every sender's parser is read) Keys read by the closures above, and the top-level keys of the two classes from `data/models.json`:

- Envelope key `identifier_location` (object, read by `onReady` and `_fetchLocation`).
- `electricity_price::CloudPlace`: `longitude` (String), `latitude` (String), `country_code` (String), `place_id` (String?), `display_name` (String?), `post_code` (String?), `formatted_address` (String?).
- `electricity_price::CommonLocationResponse`: `default_location` (CloudPlace?), `identifier_location` (CloudPlace).

Parse of `identifier_location` / `default_location` (traced 2026-10-20, app side): `ChargingWeatherHttpAdapter::_parseLocation` (`ak_iot_common_charging/src/weather/weather_impl.dart @0x2b11ff4`) walks the two keys `identifier_location` and `default_location` (list `<String>` built at `@0x2b12020`), casts each value to `Map<String, dynamic>?` (`@0x2b12184`), and builds a `WeatherLocation` (`@0x2b122d8`): `latitude` and `longitude` are converted with `toString` and parsed as doubles (`_parse`, `@0x2b12224`, `@0x2b122b4`; empty string when null), `place_id`, `formatted_address`, `country_code` and `display_name` are null-safe `toString` values (key addresses `@0x2b122f4`, `@0x2b12360`, `@0x2b123cc`, `@0x2b12438`), so they stay `String?`.

## Example request/response

Request, synthesized (decrypted body as built by `onReady`; `<...>` are placeholders, not captured values)

```json
{
  "business_type": 0,
  "identifier_type": 2,
  "identifier_id": "<site_id>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the senders read for this page (`_fetchLocation` and `fetchDefaultLocation` only log the code of a failure closure). Code meanings are owned by `api/errors.md`.

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

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `identifier_id` at all five senders: a field or parameter value (`electricity_price/components/dynamic_price/setting/electricty_place_smart_logic.dart @0x298f71c`, `ak_iot_common_charging/src/weather/weather_impl.dart @0x2b11f74`, `electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart @0x2c15318`, `micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart @0x2e8d0d8`, `unity/src/main/weather/weather_manager.dart @0x451c160`) whose declared type is not visible. — traced 2026-10-20: two of the five are String; `electricty_place_smart_logic.dart` loads field `field_63` (`@0x298f71c`), whose stores are a `String` cast with `""` for null (`@0x34f029c`, `@0x34f0680`); `ems_ai_mode_condition_logic.dart` loads `field_4b` (`@0x2a2fb7c`), stored through a `String` cast (`@0x35682b8`). The `weather_impl.dart`, `local_auto_disaster_feature.dart` and `yesterday_earning_tips_view.dart` values come from parameters or fields whose type is not declared in the dump (`local_auto_disaster_feature.dart @0x2c15318` loads `field_7` of an untyped holder)
- What `business_type` 1 means: `refreshLocation` derives 0 or 1 from a class-id compare against 4696 (`electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart @0x2c15338`); which class that is, and what the server does with the value, was not decoded.
- The success closure of `WeatherManager::fetchDefaultLocation` was not read (the parser `_parseLocation` is described under Response) — traced 2026-10-20
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
