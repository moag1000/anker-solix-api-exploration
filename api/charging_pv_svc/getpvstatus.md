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

Value of `sns` (traced 2026-10-20, app side): `A5140homeController::_isOffline` passes one serial, the `deviceSn` getter (`field_6b`) of its device object (`field_63`) (`charging/ui/page/device/a5140/a5140home/a5140home_logic.dart @0x34d0408`, `@0x34d0410`, call `@0x34d0450`); `DeviceMainLogic::_onGetDeviceListFailed` joins a non-empty list of serials with the separator `","` (`join`, `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x228a7c4`..`@0x228a7d8`, empty-list guard `cbz` `@0x228a7bc`, call `@0x228a828`). So `sns` is one serial or a comma-separated list of serials.

Value of `sns` (traced 2026-10-20, app side): `A5140homeController::_isOffline` passes one serial, the `deviceSn` getter (`field_6b`) of its device object (`field_63`) (`charging/ui/page/device/a5140/a5140home/a5140home_logic.dart @0x34d0408`, `@0x34d0410`, call `@0x34d0450`); `DeviceMainLogic::_onGetDeviceListFailed` joins a non-empty list of serials with the separator `","` (`join`, `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x228a7c4`..`@0x228a7d8`, empty-list guard `cbz` `@0x228a7bc`, call `@0x228a828`). So `sns` is one serial or a comma-separated list of serials.

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::A5140DeviceStatus`, linked as [`A5140DeviceStatus`](../../models/pps.md#a5140devicestatus), parsed by `A5140DeviceStatus.fromJson` at `charging/http/http_request_repository_impl.dart @0x2447134` in the success closure `@0x24470d0`.

## Response

(asm-traced) Top-level keys of `A5140DeviceStatus` (`data/models.json`, `charging::A5140DeviceStatus`): `pvStatuses` (List?). The closure logs the data and forwards the parsed model.

Element layout of `pvStatuses` (traced 2026-10-20, app side): `A5140DeviceStatus.fromJson` reads `pvStatuses` as `List?` and maps it to `List<PvStatus>` (`charging/model/a5140_device_info/a5140_device_status.dart @0x244718c`, cast `@0x24471dc`, element closure `@0x24474e4`, `PvStatus.fromJson` `@0x244751c`); each element has `sn` (`String?`, key `@0x2447560`, cast `@0x24475a0`), `power` (`num?`, key `@0x24475c0`, cast `@0x24475fc`) and `status` (`int?`, key `@0x2447668`, cast `@0x24476a4`). The model page [pps.md](../../models/pps.md) lists the same names without types.

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

- Meaning of `pvStatuses` elements for the server: not shown — see Response for the layout read by the app (traced 2026-10-20)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
