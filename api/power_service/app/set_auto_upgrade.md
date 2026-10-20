> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# set_auto_upgrade

## Purpose

Writes the automatic firmware-upgrade setting of the account from the firmware updates page (caller `FirmwareUpdatesLogic::setDeviceAutoMessage`; builder `HttpRequestControllerImpl::setAutoUpgrade`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`set_auto_upgrade` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/set_auto_upgrade` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x404af94`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x404af8c`, in `HttpRequestControllerImpl::setAutoUpgrade` (`charging/http/http_request_repository_impl.dart @0x404af14`), sent through `encryptionRequestHttp` (`@0x404afb4`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) `HttpRequestControllerImpl::setAutoUpgrade` (`charging/http/http_request_repository_impl.dart @0x404af14`) receives the body map as a parameter (`fp-0x10`, passed as the data slot `@0x404afa0`) and builds none. The caller `FirmwareUpdatesLogic` passes a value read through `value()` from a model field (`charging/ui/page/user/firmware_updates/firmware_updates_page/firmware_updates_logic.dart @0x404ae68`); the keys of that body were not decoded.

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the closures passed are `charging/http/http_request_repository_impl.dart @0x261b9a0` (calls the stored callback with `true`, `@0x261b9cc`) and the call has no named argument (`r4 = const [0x1, 0x6, 0x6, 0x6, null]` at `@0x404afb0`); no `fromJson` or response key is read.

## Response

No response key is read.

## Example request/response

Request: the body is built by the caller and was not decoded, so no example is given.

Response: no keys are read by the app.

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `setAutoUpgrade` @0x404af14 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::setAutoUpgrade`
- `charging/ui/page/user/firmware_updates/firmware_updates_page/firmware_updates_logic.dart::setDeviceAutoMessage`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The request keys: the body is a parameter built in `FirmwareUpdatesLogic::setDeviceAutoMessage`; the companion read is [get_auto_upgrade](get_auto_upgrade.md) (`DeviceAutoUpGradDisposition`), which suggests the same model, but that is not read here.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
