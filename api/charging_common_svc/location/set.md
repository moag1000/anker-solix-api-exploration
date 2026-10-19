> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# set

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_common_svc/location/set`, method: not extracted by the inventory <!-- TODO -->; string-only: `ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb1184`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `identifier_type` | ? | ? | ? | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb0ef0` |
| `identifier_id` | ? | ? | ? | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb0ef0` |
| `business_type` | ? | ? | ? | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb0ef0` |
| `latitude` | ? | ? | ? | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb0ef0` |
| `longitude` | ? | ? | ? | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb0ef0` |
| `place_id` | ? | ? | ? | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb0ef0` |
| `formatted_address` | ? | ? | ? | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb0ef0` |
| `country_code` | ? | ? | ? | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb0ef0` |
| `display_name` | ? | ? | ? | `ak_iot_common_charging/src/weather/weather_impl.dart @0x2bb0ef0` |
| `location` | ? | ? | ? | `electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart @0x2c142c0` |

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

- `ak_iot_common_charging/src/weather/weather_impl.dart`: `saveLocation` @0x2bb0ef0 (request; encrypted: default-true (requestHttp) — verify)
- `electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart`: `_setLocation` @0x2c142c0 (request; encrypted: default-true (requestHttp) — verify)

Called from:

- `electricity_price/components/dynamic_price/util/local_auto_disaster_feature.dart::pushToMap`
- `station_home/src/weather/weather_service.dart::syncLocation`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
