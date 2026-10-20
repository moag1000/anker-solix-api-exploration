> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# getPvStatus

## Purpose

Reads the PV status of one or more A5140 devices for the device home page and the device list (caller chain `A5140HomeLogic::_isOffline`, `DeviceMainLogic::getDeviceList`, `HttpRequestController::getPvStatus`, in `data/endpoints.json`) (asm-traced).

## Upstream name

`get_device_pv_status` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /charging_pv_svc/getPvStatus` (asm-traced): URL string `@0x2446fe0`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x2446fd8`, in `HttpRequestControllerImpl::getPvStatus` (`charging/http/http_request_repository_impl.dart @0x2446f1c`), sent through `HttpRequestControllerImpl::encryptionRequestHttp` (the closures are positional arguments, argument descriptor `@0x2446ffc` names no option) (`@0x2447000`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) One sender, one key. The map literal has the type arguments `<String, String>` (`charging/http/http_request_repository_impl.dart @0x2446f94`), so the value is a string; it is stored without a guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `sns` | string | yes | `"<sns>"` | `charging/http/http_request_repository_impl.dart @0x2446f80` (value store `@0x2446f90`, parameter) |

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::A5140DeviceStatus`, linked as [`A5140DeviceStatus`](../../models/pps.md#a5140devicestatus), parsed by `A5140DeviceStatus.fromJson` at `charging/http/http_request_repository_impl.dart @0x2447134` in the success closure `@0x24470d0`.

## Response

(asm-traced) Top-level keys of `A5140DeviceStatus` (`data/models.json`, `charging::A5140DeviceStatus`): `pvStatuses` (List?). The closure logs the data and forwards the parsed model.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "sns": "<sns>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getPvStatus` @0x2446f1c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getPvStatus`
- `charging/ui/page/device/a5140/a5140home/a5140home_logic.dart::_isOffline`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::getDeviceList`

Call sites (grep of the asm, traced 2026-10-20): `getPvStatus` is called from `A5140homeController::_isOffline` (`charging/ui/page/device/a5140/a5140home/a5140home_logic.dart @0x34d0450`) and `DeviceMainLogic::_onGetDeviceListFailed` (`charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x228a828`).

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the string `sns` carries when several devices are queried (a joined list or a single serial): the value is a `String` by the literal type; how the callers join it was not read. — traced 2026-10-20: the callers are `A5140homeController::_isOffline` and `DeviceMainLogic::_onGetDeviceListFailed`; how they join the serial numbers was not read
- The element structure of `pvStatuses`: owned by the model page.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
