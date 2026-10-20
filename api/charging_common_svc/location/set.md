> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# set

## Purpose

Saves the location a user picked for a site (callers `LocalAutoDisasterFeature::_setLocation`, reached from `LocalAutoDisasterFeature::pushToMap`, and `ChargingWeatherHttpAdapter::saveLocation`, reached from `WeatherService::syncLocation`) (string-only: the caller names come from the page's caller list, the chain is not in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_common_svc/location/set` (asm-traced).

- `LocalAutoDisasterFeature::_setLocation` (`electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart @0x2c142c0`): URL string `@0x2c143e4`, sent through `HttpHelper::request` (`@0x2c14404`) without a `method` argument (argument descriptor `@0x2c14400`); `HttpHelper::request` substitutes `Method.post` (pool entry `pp+0xa7e0`) for a null `method` (`electricity_price/components/electricity_price_common/http/http_helper.dart @0x2c14630`).
- `ChargingWeatherHttpAdapter::saveLocation` (`ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb0ef0`): URL `@0x2bb1184`, sent through `StationApiClient::request` (`@0x2bb118c`), which puts the string `"POST"` under the envelope key `method` (`station_home/src/http/station_api_client.dart @0x2a4445c`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: several field types are not read) Two senders, three keys in common. Both map literals have the type arguments `<String, dynamic>` (`electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart @0x2c143c4`, `ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb1174`), which name no value type.

| field | type | required | example | source |
|---|---|---|---|---|
| `identifier_type` | int (Smi, w) in `saveLocation`; int (unboxed, x) in `_setLocation` | yes | `2` (`saveLocation`: raw immediate 4, 32-bit store) | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb0f30` (value store `@0x2bb0f40`, constant `@0x2bb0f3c`); `electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart @0x2c1430c` (`LoadField` `@0x2c1431c`, `BoxInt64Instr` `@0x2c14320`, store `@0x2c14334`) |
| `identifier_id` | ? | yes | `"<site_id>"` | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb0f44` (parameter, store `@0x2bb0f54`); `electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart @0x2c14338` (`LoadField` `@0x2c14344`, store `@0x2c1434c`) |
| `business_type` | int (Smi, w) | yes | `0` in `saveLocation` (zero register stored) | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb0f58` (store `@0x2bb0f64`); `electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart @0x2c1438c` stores 0 or 1 (class-id compare against 4696 `@0x2c143a4`, shifted to a Smi `@0x2c143bc`, store `@0x2c143c0`) |
| `latitude` | string | yes | `"<latitude>"` | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb0f68` (store `@0x2bb0f70`); the value is the result of `_Double::toString` (`@0x2bb0fac`) |
| `longitude` | string | yes | `"<longitude>"` | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb0fdc` (store `@0x2bb0fe4`); `_Double::toString` (`@0x2bb1020`) |
| `place_id` | ? | yes | `""` when the field is null | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb1050` (store `@0x2bb1058`); the constant `""` replaces a null field (`@0x2bb1070`) |
| `formatted_address` | ? | yes | `""` when the field is null | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb109c` (store `@0x2bb10a4`); fallback `@0x2bb10b8` |
| `country_code` | ? | yes | `""` when the field is null | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb10e4` (store `@0x2bb10ec`); fallback `@0x2bb1100` |
| `display_name` | ? | yes | `""` when the field is null | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb112c` (store `@0x2bb1134`); fallback `@0x2bb1148` |
| `location` | object | yes | seven-key map (see below) | `electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart @0x2c14350` (call `@0x2c1435c`, store `@0x2c14364`; `_setLocation` only) |

`saveLocation` sends nine flat keys (array length raw 36 at `ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb0f24`, so 18 slots). `_setLocation` sends four keys, `identifier_type`, `identifier_id`, `location`, `business_type` (array length raw 16 at `electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart @0x2c142fc`, so 8 slots). The value of `location` is the map literal built by `CloudPlace::json` (`electricity_price/components/dynamic_price/model/cloud_location.dart @0x2c14ae0`, `<String, dynamic>` `@0x2c14bfc`) with the keys `longitude`, `latitude`, `country_code`, `place_id`, `display_name`, `formatted_address`, `post_code`.

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app as a model: `ChargingWeatherHttpAdapter::saveLocation` turns the result into a bool by comparing its class id (`cmp x1, #0x1c5` and `csel`, `ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb11ac`, `@0x2bb11b8`); `LocalAutoDisasterFeature::_setLocation` reads only the success flag of the returned object (`LoadField` `field_b`, `electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart @0x2c14414`) and the code field on failure (`field_13`, `@0x2c14428`).

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by `ChargingWeatherHttpAdapter::saveLocation`; `<...>` are placeholders, not captured values)

```json
{
  "identifier_type": 2,
  "identifier_id": "<site_id>",
  "business_type": 0,
  "latitude": "<latitude>",
  "longitude": "<longitude>",
  "place_id": "",
  "formatted_address": "",
  "country_code": "",
  "display_name": ""
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

`LocalAutoDisasterFeature::_setLocation` throws the failure code of the returned object, or -1 when it is null (`electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart @0x2c14438`, `@0x2c1446c`); no numeric code is compared. Code meanings are owned by `api/errors.md`.

## Callers in app

- `ak_iot_common_charging/src/weather/weather_impl.dart`: `saveLocation` @0x2bb0ef0 (request; encrypted: default-true (requestHttp) — verify)
- `electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart`: `_setLocation` @0x2c142c0 (request; encrypted: default-true (requestHttp) — verify)

Called from:

- `electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart::pushToMap`
- `station_home/src/weather/weather_service.dart::syncLocation`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. Params changed: added `country_code`, `display_name`, `formatted_address`, `latitude`, `longitude`, `place_id` (`tools/out/diff_3.18.0_3.24.3.md`, string-level diff; the six keys are the flat keys of the `saveLocation` literal in 3.24.3).

## Known unknowns

- Types of `identifier_id`, `place_id`, `formatted_address`, `country_code` and `display_name`: parameter or field values; the asm shows only the `""` fallback for a null. — attempted 2026-10-20 (two-hop not readable: `syncLocation` (`station_home/src/weather/weather_service.dart @0x2bb0ec8`), an anonymous closure (`electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart @0x2c1413c`) pass slots or fields of their own frames; no literal or declared type in the argument setups)
- Which values other callers could pass for `identifier_type` and `business_type`: `_setLocation` stores a field value for the first and a class-id-dependent 0 or 1 for the second (`electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart @0x2c143a4`).
- Why `_setLocation` nests the place under `location` while `saveLocation` sends its parts flat: both reach the same URL; which shape the server accepts is not known from the app.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
