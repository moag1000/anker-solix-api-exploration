> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# delete_charging_device

## Purpose

Deletes an A1340 charging device: `A1340chargeDeviceLogic::_deleteA1340ChargeDeviceForOther` (`a1340charge_device_logic.dart @0x3bfad98`) calls `deleteChargingDevice` with the device model's JSON.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/site/delete_charging_device` (asm-traced): URL string at `http_request_repository_impl.dart @0x3bfaf0c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3bfaf04`, in `HttpRequestControllerImpl::deleteChargingDevice` (`http_request_repository_impl.dart @0x3bfae8c`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The builder `deleteChargingDevice` (`http_request_repository_impl.dart @0x3bfae8c`) contains no map literal and forwards the body its caller passes to `encryptionRequestHttp` (`@0x3bfaf34`). The caller passes the result of `toJson()` of its parameter object (`charging/ui/page/device/a1340/a1340charge_device/a1340charge_device_logic.dart @0x3bfade0`).

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

Keys (asm-traced): `A1340ChargingDeviceModel::toJson` (`charging/model/a1340_device_info/a1340_charging_device_model.dart @0x286b424`) writes eight keys unconditionally into one map literal (`AllocateArray r2 = 32` `@0x286b448`, `<String, dynamic>` `@0x286b514`): the value of each key is the model field stored unchanged, so the types are the declared field types of `A1340ChargingDeviceModel.fromJson` (`data/models.json`, `charging::A1340ChargingDeviceModel`, `charging/model/a1340_device_info/a1340_charging_device_model.dart @0x286b5fc`). The caller `A1340chargeDeviceLogic._deleteA1340ChargeDeviceForOther` (`charging/ui/page/device/a1340/a1340charge_device/a1340charge_device_logic.dart @0x3bfade0`) passes the result of `toJson()` of its parameter object to `deleteChargingDevice` (`@0x3bfae1c`); that the parameter is an `A1340ChargingDeviceModel` is taken from the page of the sibling endpoints, the asm names no class at this call.

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::A1340ChargingDeviceData` (`data/models.json` key; fields on [`models/pps.md`](../../../models/pps.md#a1340chargingdevicedata)), parsed in the builder's success closure `http_request_repository_impl.dart @0x286b080` by `A1340ChargingDeviceData.fromJson` (shared closure code, pool `pp+0xcae80`); the caller's own success callback `a1340charge_device_logic.dart @0x3bfafc0` logs `"不在屏显上的充电设备-删除: "`, removes an element and updates the UI.

## Response

Top-level keys of the model (from `data/models.json`): `device_list` (List, nullable) and `guide_txt` (String, nullable).

## Example request/response

Request: the keys of `A1340ChargingDeviceModel.toJson()` (table above); no synthesized body is given.

Response keys: see Response; no capture.

## Errors seen

None traced. The caller's failure callback `a1340charge_device_logic.dart @0x3bfaf50` logs `"不在屏显上的充电设备-删除失败: "`, calls `exeError()` and shows a message; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `deleteChargingDevice` @0x3bfae8c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::deleteChargingDevice`
- `charging/ui/page/device/a1340/a1340charge_device/a1340charge_device_logic.dart::_deleteA1340ChargeDeviceForOther`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- Type of `new_battery_capacity` (declared `unknown` in the model) and the class of the object whose `toJson` the caller uses (`charging/ui/page/device/a1340/a1340charge_device/a1340charge_device_logic.dart @0x3bfade0`) — attempted 2026-10-20 (two-hop not readable: the model declares no type for `new_battery_capacity` and the call names no class. Header stays string-only)
- Whether the server answers with the remaining device list: the success callback of the caller does not read its argument (`removes` a local element), while the builder parses an `A1340ChargingDeviceData`.

## Device-tested by

none
