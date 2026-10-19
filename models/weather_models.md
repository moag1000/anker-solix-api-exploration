> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# WeatherApiResult and WeatherResponseData

## Purpose

Carries the weather answer of `get_weather`: weather type, temperature and its unit, and a timestamp; the Unity variant adds the sunrise and sunset timestamps.

## Dart class + file

`WeatherApiResult` (`fromJson @0x2b117a8`, file `ak_iot_contract/src/weather/weather_models.dart`, package `ak_iot_contract`, used by the station home) and `WeatherResponseData` (`fromJson @0x22e5598`, file `unity/src/main/weather/weather_response_model.dart`, package `unity`).

## Fields

Column `since`: `≤3.18.0` means the key is present in 3.18.0 (earlier versions not checked), `3.24.3` means first seen in 3.24.3. Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Nullability and Dart types come from `tools/model_fields.py` (`data/models.json`); `unknown` means the extractor could not resolve the element type.

### WeatherApiResult

`fromJson` `weather_models.dart @0x2b117a8`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `weather_type` | `int?` | yes | 3.24.3 | `weather_models.dart @0x2b117d4` |
| `temperature` | `num?` | yes | 3.24.3 | `weather_models.dart @0x2b11860` |
| `temperature_type` | `int?` | yes | 3.24.3 | `weather_models.dart @0x2b11910` |
| `timestamp` | `int?` | yes | 3.24.3 | `weather_models.dart @0x2b11998` |

### WeatherResponseData

`fromJson` `weather_response_model.dart @0x22e5598`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `weather_type` | `int?` | yes | 3.24.3 | `weather_response_model.dart @0x22e55c4` |
| `temperature` | `num?` | yes | 3.24.3 | `weather_response_model.dart @0x22e5644` |
| `temperature_type` | `int?` | yes | 3.24.3 | `weather_response_model.dart @0x22e56f4` |
| `timestamp` | `int?` | yes | 3.24.3 | `weather_response_model.dart @0x22e5774` |
| `sunrise_timestamp` | `num?` | yes | 3.24.3 | `weather_response_model.dart @0x22e57f8` |
| `sunset_timestamp` | `num?` | yes | 3.24.3 | `weather_response_model.dart @0x22e5894` |

## Produced by

[`get_weather`](../api/power_service/app/get_weather.md): `WeatherApiResult.fromJson` at `ak_iot_common_charging/src/weather/weather_impl.dart @0x2b1177c`; `WeatherResponseData.fromJson` at `unity/src/main/weather/weather_manager.dart @0x22e4c5c` and `@0x22e5050`.

## Consumed by

The station home weather widget and the Unity weather manager; field-level use is not traced.

## Changed since 3.18.0

Both classes are new in 3.24.3.

## Known unknowns

- The weather type codes, the `temperature_type` values and whether `timestamp` is in seconds or milliseconds are not decoded.
