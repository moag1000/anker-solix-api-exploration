> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_auto_upgrade

## Purpose

Reads the automatic firmware-upgrade setting of the account for the firmware updates page (callers `FirmwareUpdatesLogic::getDeviceAutoUpGradMessage`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`get_auto_upgrade` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/get_auto_upgrade` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x2914494`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x291448c`, in `HttpRequestControllerImpl::getAutoUpgrade` (`charging/http/http_request_repository_impl.dart @0x2914404`), sent through `encryptionRequestHttp` (`@0x29144c4`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) No request fields: the body argument is the empty map literal (`THR::empty_array`, `Map._fromLiteral`) at `charging/http/http_request_repository_impl.dart @0x2914454`.

## `param_type`/`cmd`

n/a

## Response model (link)

- [`DeviceAutoUpGradDisposition`](../../../models/firmware.md#deviceautoupgraddisposition), parsed by `DeviceAutoUpGradDisposition.fromJson` at `charging/http/http_request_repository_impl.dart @0x2914518`

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `DeviceAutoUpGradDisposition` top-level keys (`data/models.json`, `charging::DeviceAutoUpGradDisposition`): `main_switch` (bool?), `device_list` (List).

## Example request/response

Request, synthesized: the body is the empty object.

```json
{}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getAutoUpgrade` @0x2914404 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getAutoUpgrade`
- `charging/ui/page/user/firmware_updates/firmware_updates_page/firmware_updates_logic.dart::getDeviceAutoUpGradMessage`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the server stores per account or per device for the setting (the companion write is [set_auto_upgrade](set_auto_upgrade.md)).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
