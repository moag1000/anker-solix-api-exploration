> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_weather

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/get_weather`, method: not extracted by the inventory <!-- TODO -->; string-only: `ak_iot_common_charging/src/weather/weather_impl.dart @0x2b11640`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `latitude` | ? | ? | ? | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2b11570` |
| `longitude` | ? | ? | ? | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2b11570` |

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

- `ak_iot_common_charging/src/weather/weather_impl.dart`: `fetchWeather` @0x2b11570 (request; encrypted: default-true (requestHttp) — verify)
- `unity/src/main/weather/weather_manager.dart`: `_fetchWeatherFromAPI` @0x22e46b8 (encryptionRequestHttp; encrypted: true)

Called from:

- `station_home/src/weather/weather_service.dart::_fetchWeatherFromCoordinates`
- `unity/src/main/weather/weather_manager.dart::fetchWeatherDataWithCoordinates`

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
