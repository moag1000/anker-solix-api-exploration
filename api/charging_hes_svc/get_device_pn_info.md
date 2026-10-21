> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_device_pn_info

## Purpose

Reads product numbers and images for a list of device serial numbers (`SnPnDataModel`) for the SN-number page (`DeviceImgController::getDevicePnInfo`; the success closure logs `SnNumberLogic 根据设备sn列表获取设备pn等信息 成功`, "get the pn of the devices from the sn list, success", my translation); the only recorded caller is the dependency registration `DIInit` (string-only: no caller chain in `data/endpoints.json`, inferred from the builder name).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_device_pn_info` (asm-traced): URL string at `charging/ui/page/device/a5101/setting/sn_number/device_img_controller.dart @0x2789580`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2789578`, in `DeviceImgController::getDevicePnInfo` (`charging/ui/page/device/a5101/setting/sn_number/device_img_controller.dart @0x2789468`), sent through `requestHttp` (`@0x27895a8`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `DeviceImgController::getDevicePnInfo` (`charging/ui/page/device/a5101/setting/sn_number/device_img_controller.dart`, call `@0x27895a8`, argument list `@0x27895a0`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

`DeviceImgController::getDevicePnInfo` (`charging/ui/page/device/a5101/setting/sn_number/device_img_controller.dart @0x2789468`) stores 2 keys in a map literal with type arguments `<String, Object>` (`@0x2789534`), which do not type the values; both values are stored as received (`@0x278951c`, `@0x2789530`). The builder returns `Future<List<SnPnModel>?>` (`@0x2789490`). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | yes | ? | `charging/ui/page/device/a5101/setting/sn_number/device_img_controller.dart @0x278950c` |
| `sns` | ? | yes | ? | `charging/ui/page/device/a5101/setting/sn_number/device_img_controller.dart @0x2789520` |

## `param_type`/`cmd`

n/a

## Response model (link)

- `charging::SnPnDataModel`, parsed by `SnPnDataModel.fromJson` at `charging/ui/page/device/a5101/setting/sn_number/device_img_controller.dart @0x2789674` (success closure `@0x278962c`, `bl` target `[package:charging/model/a5101/sn_pn_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::SnPnDataModel`): `pnInfos` (unknown).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "sns": "<sns>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`. The failure closure logs a fixed text (`charging/ui/page/device/a5101/setting/sn_number/device_img_controller.dart @0x27895ec`) and completes the future (`@0x2789610`) without comparing the code.

## Callers in app

- `charging/ui/page/device/a5101/setting/sn_number/device_img_controller.dart`: `getDevicePnInfo` @0x2789468 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/util/demosite_util_impl.dart`: `DemoSiteUtilImpl` @0x4a33a6c (URL literal only, no `*Http*` call)

Called from:

- `charging/boostrap_impl.dart::DIInit`

Call sites (traced 2026-10-20): `getDevicePnInfo` is called from `DeviceImgController::deviceImgMap` (`charging/ui/page/device/a5101/setting/sn_number/device_img_controller.dart @0x27891c8`), an `async` function returning `Map<String, DeviceImgInfo>` (`InitAsync` `@0x27891b0`).

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The type of `sns`: the parameter may be a list or a joined text; the call site was not decoded. — attempted 2026-10-20 (two-hop not readable: the only caller `DeviceImgController::deviceImgMap` (`charging/ui/page/device/a5101/setting/sn_number/device_img_controller.dart @0x27891c8`) forwards its own two parameters, `SetupParameters` `@0x2789194`)
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
