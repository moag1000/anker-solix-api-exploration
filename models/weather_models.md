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

Value sets (traced 2026-10-20): `WeatherApiResult.fromJson` converts `weather_type` with `WeatherType.fromValue` (`ak_iot_contract/src/weather/weather_models.dart @0x2b11844`, function `@0x2b11b04`) and `temperature_type` with `TemperatureUnit.fromValue` (`@0x2b11980`, function `@0x2b11a5c`); `WeatherResponseData.fromJson` does the same with its own copies (`unity/src/main/weather/weather_response_model.dart @0x22e5614` and `@0x22e5744`). Wire values from the object dump (`off_14`): `WeatherType` 1 `sunny`, 2 `cloudy`, 3 `rainy`, 4 `stormy`, 5 `snowy`, 6 `thunderstorm` (contract objects `objs.txt Obj!WeatherType@4217041` sunny, `objs.txt Obj!WeatherType@42170e1` cloudy, `objs.txt Obj!WeatherType@42170c1` rainy, `objs.txt Obj!WeatherType@42170a1` stormy, `objs.txt Obj!WeatherType@4217081` snowy, `objs.txt Obj!WeatherType@4217061` thunderstorm; unity copy `objs.txt Obj!WeatherType@38f4821` sunny, `objs.txt Obj!WeatherType@38f4801` cloudy, `objs.txt Obj!WeatherType@38f47e1` rainy, `objs.txt Obj!WeatherType@38f47c1` stormy, `objs.txt Obj!WeatherType@38f47a1` snowy, `objs.txt Obj!WeatherType@38f4781` thunderstorm); `TemperatureUnit` 1 `celsius` (label `°C`) and 2 `fahrenheit` (label `°F`) (objects `objs.txt Obj!TemperatureUnit@4216fe1`, `objs.txt Obj!TemperatureUnit@4216fc1`; unity copy `objs.txt Obj!TemperatureUnit@38f4761`, `objs.txt Obj!TemperatureUnit@38f4741`). The enum indices are 0 to 5 and 0 to 1; the wire values are index plus one. Binding of a package to an object id: the dump has four pairs of objects named `TemperatureUnit` (`objs.txt Obj!TemperatureUnit@38f4741` and `objs.txt Obj!TemperatureUnit@38f4761` unity values 1 and 2, the contract pair above, `objs.txt Obj!TemperatureUnit@38f6601` and `objs.txt Obj!TemperatureUnit@38f6621` with only a label `℃`/`℉`, and `objs.txt Obj!TemperatureUnit@38f8de1` and `objs.txt Obj!TemperatureUnit@38f8e01` with the values 0 and 1); the id on this page is the one in the `[pp+..] Obj!Class@id` operand of the `fromValue` asm of the named package (for example `Obj!TemperatureUnit@38f4761` at `weather_response_model.dart` line 167 of the asm), not a guess from the class name. Unit of the timestamps: `DayNightType._fromLocationAndTime` multiplies the integer by 1000 before `TZDateTime.fromMillisecondsSinceEpoch` (`unity/src/main/weather/day_night_type.dart @0x22e3de8`, `@0x22ea000`), so the timestamps that reach the day or night decision are seconds.

## Produced by

[`get_weather`](../api/power_service/app/get_weather.md): `WeatherApiResult.fromJson` at `ak_iot_common_charging/src/weather/weather_impl.dart @0x2b1177c`; `WeatherResponseData.fromJson` at `unity/src/main/weather/weather_manager.dart @0x22e4c5c` and `@0x22e5050`.

## Consumed by

The station home weather widget and the Unity weather manager; field-level use is not traced.

## Changed since 3.18.0

Both classes are new in 3.24.3.

## Known unknowns

None open after the trace of 2026-10-20.
