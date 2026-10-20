> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# reset_charging_device

## Purpose

Saves the list of A1340 charging devices that are not on the screen display: `A1340chargeDeviceManagerLogic::setOtherDevice` (`a1340charge_device_manager_logic.dart @0x3c00688`) calls `resetChargingDevice`.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/site/reset_charging_device` (asm-traced): URL string at `http_request_repository_impl.dart @0x3c0081c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3c00814`, in `HttpRequestControllerImpl::resetChargingDevice` (`http_request_repository_impl.dart @0x3c0079c`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The builder `resetChargingDevice` (`http_request_repository_impl.dart @0x3c0079c`) has no map literal; the caller builds a 1-pair map typed `<String, List<A1340ChargingDeviceModel>>` (type arguments `@0x3c006e4`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_list` | list | yes | | key `@0x3c006c8`, value store `@0x3c006e0` (`field_97` of the logic object, a list of `A1340ChargingDeviceModel` by the map type) |

## `param_type`/`cmd`

n/a

## Response model (link)

None: the response body is not parsed. The caller's callbacks `a1340charge_device_manager_logic.dart @0x3c008a4` and `@0x3c00858` call `_saveDataFinish` with `true` and contain no `fromJson` call; the builder's own success template `@0x261b9a0` forwards a constant `true`.

## Response

No response key is read by the app.

## Example request/response

Request, synthesized (the elements are `A1340ChargingDeviceModel` objects serialized by the HTTP layer)

```json
{"device_list": ["<A1340ChargingDeviceModel objects>"]}
```

Response: none parsed.

## Errors seen

None traced. The caller's callbacks end in `_saveDataFinish`; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `resetChargingDevice` @0x3c0079c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::resetChargingDevice`
- `charging/ui/page/device/a1340/a1340charge_device_manager/a1340charge_device_manager_logic.dart::setOtherDevice`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- The JSON keys of an `A1340ChargingDeviceModel` element (its `toJson` was not followed).
- Whether the server replaces or merges the list: not derivable from the app.

## Device-tested by

none
