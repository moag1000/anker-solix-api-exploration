> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_charging_device

## Purpose

Reads the A1340 charging devices: `A1340chargeDeviceLogic::getA1340ChargeDeviceListForOther` and `A1340homeLogic::_getA1340ChargeDeviceListForOther` call `getChargingDeviceRequest`.

## Upstream name

`charging_devices` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/site/get_charging_device` (asm-traced): URL string at `http_request_repository_impl.dart @0x286b044`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x286b03c`, in `HttpRequestControllerImpl::getChargingDeviceRequest` (`http_request_repository_impl.dart @0x286afb8`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is an empty map literal (`ldr x16, [THR, #0xa8]` empty array `@0x286affc`, `Map._fromLiteral` `@0x286b004`); the builder contains no `[]=` call, so no key is added. The map goes to `encryptionRequestHttp` (`@0x286b064`).

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::A1340ChargingDeviceData` (`data/models.json` key; fields on [`models/pps.md`](../../../models/pps.md#a1340chargingdevicedata)), parsed in the success closure `http_request_repository_impl.dart @0x286b080` by `A1340ChargingDeviceData.fromJson`.

## Response

Top-level keys of the model (from `data/models.json`): `device_list` (List, nullable) and `guide_txt` (String, nullable).

## Example request/response

Request, synthesized

```json
{}
```

Response keys: see Response; no capture.

## Errors seen

None traced: the builder passes the `postJML` failure template (`@0x226824c`) to the callers' failure callbacks, which were not read. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getChargingDeviceRequest` @0x286afb8 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getChargingDeviceRequest`
- `charging/ui/page/device/a1340/a1340charge_device/a1340charge_device_logic.dart::getA1340ChargeDeviceListForOther`
- `charging/ui/page/device/a1340/a1340home/a1340home_logic.dart::_getA1340ChargeDeviceListForOther`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta. The model `A1340ChargingDeviceData` is `≤3.18.0` in `data/models.json`.

## Known unknowns

- The element class of `device_list` (the model keeps it as an untyped `List`).
- Failure handling in the two callers was not read.

## Device-tested by

none
