> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# update_charging_device

## Purpose

Updates an A1340 charging device: `A1340addDeviceLogic::updateChargeDevice` (`a1340add_device_logic.dart`) calls `updateChargingDevice`.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/site/update_charging_device` (asm-traced): URL string at `http_request_repository_impl.dart @0x3bf4a54`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3bf4a4c`, in `HttpRequestControllerImpl::updateChargingDevice` (`http_request_repository_impl.dart @0x3bf49d4`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The builder `updateChargingDevice` (`http_request_repository_impl.dart @0x3bf49d4`) has no map literal and forwards the body its caller passes to `encryptionRequestHttp`; the body is built from the add-device form like [add_charging_device](add_charging_device.md) (an `A1340ChargingDeviceModel` and its `toJson()`), which was not followed for this caller.

| field | type | required | example | source |
|---|---|---|---|---|
| `charging_device_id` | int (declared `int?`) | yes (key always written, value may be null) | | key `charging/model/a1340_device_info/a1340_charging_device_model.dart @0x286b450` |
| `device_name` | string (declared `String?`) | yes (key always written, value may be null) | | key `0x286b46c` |
| `device_type` | string (declared `String?`) | yes (key always written, value may be null) | | key `0x286b484` |
| `battery_capacity` | int (declared `int?`) | yes (key always written, value may be null) | | key `0x286b49c` |
| `new_battery_capacity` | ? (declared `unknown`) | yes (key always written, value may be null) | | key `0x286b4b4` |
| `battery_uint` | string (declared `String?`) | yes (key always written, value may be null) | | key `0x286b4cc` |
| `battery_health` | int (declared `int?`) | yes (key always written, value may be null) | | key `0x286b4e4` |
| `update_flag` | bool (declared `bool?`) | yes (key always written, value may be null) | | key `0x286b4fc` |

Keys (asm-traced): `A1340ChargingDeviceModel::toJson` (`charging/model/a1340_device_info/a1340_charging_device_model.dart @0x286b424`) writes eight keys unconditionally into one map literal (`AllocateArray r2 = 32` `@0x286b448`, `<String, dynamic>` `@0x286b514`): the value of each key is the model field stored unchanged, so the types are the declared field types of `A1340ChargingDeviceModel.fromJson` (`data/models.json`, `charging::A1340ChargingDeviceModel`, `charging/model/a1340_device_info/a1340_charging_device_model.dart @0x286b5fc`). The caller `A1340addDeviceLogic.updateChargeDevice` (`charging/ui/page/device/a1340/a1340add_device/a1340add_device_logic.dart @0x3bf4948`) passes the model object to `updateChargingDevice` and calls `toJson` only for a log line (`@0x3bf48d0`, label "设备修改参数json==" `@0x3bf48c0`), so the table holds the keys of the model's `toJson`; how the HTTP layer turns the object into the body is not visible in the Dart code read.

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::A1340ChargingDeviceData` (`data/models.json` key; fields on [`models/pps.md`](../../../models/pps.md#a1340chargingdevicedata)), parsed in the builder's success closure `http_request_repository_impl.dart @0x286b080` by `A1340ChargingDeviceData.fromJson` (shared closure code).

## Response

Top-level keys of the model (from `data/models.json`): `device_list` (List, nullable) and `guide_txt` (String, nullable).

## Example request/response

Request: the keys of `A1340ChargingDeviceModel.toJson()` (table above); no synthesized body is given.

Response keys: see Response; no capture.

## Errors seen

None traced: the builder passes the `postJML` failure template (`@0x226824c`); the caller's failure callback was not read. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `updateChargingDevice` @0x3bf49d4 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::updateChargingDevice`
- `charging/ui/page/device/a1340/a1340add_device/a1340add_device_logic.dart::updateChargeDevice`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- Whether the HTTP layer serialises the passed `A1340ChargingDeviceModel` object with its `toJson` (the caller passes the object; `charging/ui/page/device/a1340/a1340add_device/a1340add_device_logic.dart @0x3bf4948`) — attempted 2026-10-20 (two-hop not readable: the serialisation happens after `encryptionRequestHttp` in the SDK handler, outside the asm tree. Header stays string-only)
## Device-tested by

none
