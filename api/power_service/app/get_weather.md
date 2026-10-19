> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_weather

## Purpose

Reads the current weather for a position (latitude and longitude): the station home weather widget and the Unity (3D scene) weather manager each have their own caller and model.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /power_service/v1/app/get_weather` (asm-traced). Two senders: `ChargingWeatherHttpAdapter.fetchWeather` (`ak_iot_common_charging/src/weather/weather_impl.dart @0x2b11570`; URL literal `@0x2b11640`, called through `StationApiClient.request` `@0x2b11648`, which sets the method `"POST"`, `station_api_client.dart @0x2a4445c`) and `WeatherManager._fetchWeatherFromAPI` (`unity/src/main/weather/weather_manager.dart @0x22e46b8`; URL `@0x22e48d0`, `Method.post` pool entry `pp+0xa7e0`, `@0x22e48c8`).

## Encrypted?

`fetchWeather`: `StationApiClient.request`, which sends through the SDK handler with the identifier `akiot.cloud_api` (path C of [encryption.md](../../encryption.md#which-calls-are-encrypted); `station_home/src/http/station_api_client.dart @0x2a444c0`). `_fetchWeatherFromAPI`: `encryptionRequestHttp` (`unity/src/main/weather/weather_manager.dart @0x22e48f8`) with `showLoading` off, no `needEncryption`, default `true`; whether it goes through the SDK is decided at run time.

## Request

Map literal with two pairs in both senders.

| field | type | required | example | source |
|---|---|---|---|---|
| `latitude` | double | yes | `52.52` | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2b115b0` (boxed double stored at `@0x2b115ec`); `unity/src/main/weather/weather_manager.dart @0x22e4834` |
| `longitude` | double | yes | `13.405` | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2b115f0` (`@0x2b11628`); `unity/src/main/weather/weather_manager.dart @0x22e4848` |

The example coordinates are placeholders. The Unity sender logs `params: lat=..., lng=...` (`@0x22e4704`, `@0x22e4748`) and reports errors to the `U3DModule` channel (`@0x22e4794`).

## `param_type`/`cmd`

n/a

## Response model (link)

`WeatherApiResult` (station home path) and `WeatherResponseData` (Unity path), [../../../models/weather_models.md](../../../models/weather_models.md): `WeatherApiResult.fromJson` is called at `ak_iot_common_charging/src/weather/weather_impl.dart @0x2b1177c` inside `ChargingWeatherHttpAdapter._parseWeather` (`@0x2b116d0`), `WeatherResponseData.fromJson` at `unity/src/main/weather/weather_manager.dart @0x22e4c5c` and `@0x22e5050`.

## Response

`_parseWeather` reads the key `data` (`ak_iot_common_charging/src/weather/weather_impl.dart @0x2b11714`) and passes it to `WeatherApiResult.fromJson`; the Unity path parses with `WeatherResponseData.fromJson`. All fields are on the model page (wrapper `code`, `msg`, `data` as in [encryption.md](../../encryption.md#response-handling-and-error-codes)).

## Example request/response

Request, synthesized

```json
{ "latitude": 52.52, "longitude": 13.405 }
```

Response: no captured response; the key lists are on the model page.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or logs it; the shared transport codes are in [encryption.md](../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `ChargingWeatherHttpAdapter.fetchWeather` (`ak_iot_common_charging/src/weather/weather_impl.dart @0x2b11570`), called from `WeatherService._fetchWeatherFromCoordinates` (`station_home/src/weather/weather_service.dart`): the weather widget of the station home (package `station_home`).
- `WeatherManager._fetchWeatherFromAPI` (`unity/src/main/weather/weather_manager.dart @0x22e46b8`), called from `fetchWeatherDataWithCoordinates`: the Unity (3D scene) weather manager (package `unity`).

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 pool as a code-referenced URL; see the inventory row `since`). 3.24.3: present (new). since: 3.24.3. Both weather models are new in 3.24.3.

## Known unknowns

- The weather type codes and the unit of `temperature` (see `temperature_type`) are not decoded.
- Whether the server uses the account location or the sent coordinates is not known.
- Server behaviour is not known.

## Device-tested by

none
