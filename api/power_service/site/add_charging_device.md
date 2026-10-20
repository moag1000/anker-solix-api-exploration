> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# add_charging_device

## Purpose

Adds an A1340 charging device: `A1340addDeviceLogic::addChargeDevice` (`a1340add_device_logic.dart @0x3bf3fa0`) builds an `A1340ChargingDeviceModel` from the add-device form and calls `addChargingDevice`.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/site/add_charging_device` (asm-traced): URL string at `http_request_repository_impl.dart @0x3bf4304`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3bf42fc`, in `HttpRequestControllerImpl::addChargingDevice` (`http_request_repository_impl.dart @0x3bf4284`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The builder `addChargingDevice` (`http_request_repository_impl.dart @0x3bf4284`) contains no map literal; it forwards the body map that its caller passes to `encryptionRequestHttp` (`@0x3bf432c`). The caller builds an `A1340ChargingDeviceModel` object (`@0x3bf3fe0`) from form fields (a trimmed text field `@0x3bf3fd8`, an Rx value `@0x3bf4000`, and a number parsed either as a double `@0x3bf4058` or an int `@0x3bf40d0`, chosen by a bool flag `@0x3bf4034`); the keys of the sent map are written by the model's `toJson()`, which was not followed.

| field | type | required | example | source |
|---|---|---|---|---|
| (keys of `A1340ChargingDeviceModel.toJson()`) | ? | | | caller `a1340add_device_logic.dart @0x3bf3fa0`; the model class is not decoded for this page |

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::A1340ChargingDeviceData` (`data/models.json` key; fields on [`models/pps.md`](../../../models/pps.md#a1340chargingdevicedata)), parsed in the builder's success closure `http_request_repository_impl.dart @0x286b080` by `A1340ChargingDeviceData.fromJson` (closure shared with [get_charging_device](get_charging_device.md); pool `pp+0xcaa90`). The caller's own success callback `a1340add_device_logic.dart @0x3bf43b8` loads its argument once for the log string `"充电设备-增加: "` and calls `GetNavigation.back`.

## Response

Top-level keys of the model (from `data/models.json`): `device_list` (List, nullable) and `guide_txt` (String, nullable).

## Example request/response

Request: the key set comes from `A1340ChargingDeviceModel.toJson()`, not read here; no synthesized body is given.

Response keys: see Response; no capture.

## Errors seen

None traced. The caller's failure callback `a1340add_device_logic.dart @0x3bf4348` logs `"充电设备-新增: "` and shows a message; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `addChargingDevice` @0x3bf4284 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::addChargingDevice`
- `charging/ui/page/device/a1340/a1340add_device/a1340add_device_logic.dart::addChargeDevice`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- The request keys and their types: they are written by `A1340ChargingDeviceModel.toJson()` (not followed). Header stays string-only.
- Whether the answer (`A1340ChargingDeviceData`) is the full device list after the add or only the new device: the app only logs it.

## Device-tested by

none
