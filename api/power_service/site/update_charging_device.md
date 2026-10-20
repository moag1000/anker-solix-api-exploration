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
| (keys of the passed object's `toJson()`) | ? | | | caller `a1340add_device_logic.dart::updateChargeDevice` (not read) |

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::A1340ChargingDeviceData` (`data/models.json` key; fields on [`models/pps.md`](../../../models/pps.md#a1340chargingdevicedata)), parsed in the builder's success closure `http_request_repository_impl.dart @0x286b080` by `A1340ChargingDeviceData.fromJson` (shared closure code).

## Response

Top-level keys of the model (from `data/models.json`): `device_list` (List, nullable) and `guide_txt` (String, nullable).

## Example request/response

Request: the key set comes from the caller's `toJson()`, not read here; no synthesized body is given.

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

- The request keys and types (the caller `updateChargeDevice` was not read). Header stays string-only.
- Whether the update body equals the add body of [add_charging_device](add_charging_device.md).

## Device-tested by

none
