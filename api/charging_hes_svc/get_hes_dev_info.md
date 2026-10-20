> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_hes_dev_info

## Purpose

Loads the device list of a HES site for the SN-number page (`SnNumberLogic::_getSnList` through `HttpRequestControllerImpl::getHesDeviceList`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_hes_dev_info` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x28e5e70`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x28e5e68`, in `HttpRequestControllerImpl::getHesDeviceList` (`charging/http/http_request_repository_impl.dart @0x28e5dc0`), sent through `requestHttp` (`@0x28e5e98`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::getHesDeviceList` (`charging/http/http_request_repository_impl.dart`, call `@0x28e5e98`, argument list `@0x28e5e90`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `HttpRequestControllerImpl::getHesDeviceList` (`charging/http/http_request_repository_impl.dart @0x28e5e28`, 1 key). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | string | yes | `"<siteId>"` | `charging/http/http_request_repository_impl.dart @0x28e5e14` |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`A5101DeviceListModel`](../../models/hes.md#a5101devicelistmodel), parsed by `A5101DeviceListModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x28e5fb8` (success closure `@0x28e5f5c`, `bl` target `[package:charging/model/a5101/a5101_device_list_model/a5101_device_list_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::A5101DeviceListModel`): `ats` (SubDevInfo?), `results` (List?), `ecuDevices` (SubDevInfo?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "siteId": "<siteId>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getHesDeviceList` @0x28e5dc0 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getHesDeviceList`
- `charging/ui/page/device/a5101/setting/sn_number/sn_number_logic.dart::_getSnList`

SN page order (traced 2026-10-20): `SnNumberLogic::_getSnList` (`charging/ui/page/device/a5101/setting/sn_number/sn_number_logic.dart @0x28e5c84`) calls `getHesDeviceList` (`@0x28e5d58`) with the site id; the result is processed by `_dealResultWithList` and `_dealDeviceList`, which end in `_updateDeviceImgData` (`@0x28e6ebc`, function `@0x2788bb0`). That function collects the `SubDevInfo` lists (`addAll` `@0x2788c80`), flattens them to a `List<String>` (`expand` `@0x2788ca8`, `toList` `@0x2788cb4`) and awaits `DeviceImgController::deviceImgMap` (`@0x2788ce0`, function `charging/ui/page/device/a5101/setting/sn_number/device_img_controller.dart @0x27891c8`), which sends [get_device_pn_info](get_device_pn_info.md). So on this page the device-pn call is made after this call returns.

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
