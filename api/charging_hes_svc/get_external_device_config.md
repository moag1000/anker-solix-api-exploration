> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_external_device_config

## Purpose

Loads the configuration of external devices (heat pump, diesel, EV charger entries) for the device manager (`DeviceManagerLogic::getExternalDeviceList`, called from `onReady`, `didPopNext`, `pushPage` and `addHeatPump`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_external_device_config` (asm-traced): URL string at `charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart @0x28dfe3c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x28dfe34`, in `DeviceManagerLogic::getExternalDeviceList` (`charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart @0x28dfd20`), sent through `requestHttp` (`@0x28dfe64`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `DeviceManagerLogic::getExternalDeviceList` (`charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart`, call `@0x28dfe64`, argument list `@0x28dfe5c`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String?>` read at the cited address, so every value is a String: `DeviceManagerLogic::getExternalDeviceList` (`charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart @0x28dfdf0`, 2 keys). No key is behind a null guard. The `String?` value type allows a null value for a key; the key itself is stored unconditionally.

| field | type | required | example | source |
|---|---|---|---|---|
| `stationId` | string | yes | `"<stationId>"` | `charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart @0x28dfd9c` |
| `pn` | string | yes | `"<pn>"` | `charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart @0x28dfdb8` |

Source of `pn` (traced 2026-10-20): `getExternalDeviceList` loads it from the logic field `field_8f` (`LoadField` `@0x28dfdac`, stored into the argument array `@0x28dfdb4`); the `DeviceManagerLogic` constructor sets that field (`charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart @0x41264e0`) to `value?.field_7` of an observable of `A5101StationLogic` (obtained with `getA5101StationController` `@0x412649c`, null test `@0x41264b4`) with the fallback `""` (`@0x41264d8`), so a missing value is sent as the empty string. (The earlier note `field_d3` at `@0x28dfde4` is a different field, loaded for the callback.)

## `param_type`/`cmd`

n/a

## Response model (link)

- `charging::ExternalDeviceConfigModel`, parsed by `ExternalDeviceConfigModel.fromJson` at `charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart @0x28dfeb8` (success closure `@0x28dfe80`, `bl` target `[package:charging/model/a5101/external_device_config_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::ExternalDeviceConfigModel`): `deviceConfig` (unknown).

Structure behind `deviceConfig` (traced 2026-10-20): `ExternalDeviceConfigModel.fromJson` (`charging/model/a5101/external_device_config_model.dart @0x28e0358`) builds a list with the type argument `<DeviceConfig>` (`@0x28e03c4`) and parses each element with `DeviceConfig.fromJson` (call `@0x28e0798`, function `@0x28e082c`), which reads `deviceType` (cast `int?` `@0x28e0898`, `field_7`) and `isAdd` (cast `int?` `@0x28e0920`, `field_b`); the class also has the text fields `icon`, `title` and `description` that `fromJson` does not read.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "stationId": "<stationId>",
  "pn": "<pn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart`: `getExternalDeviceList` @0x28dfd20 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart::addHeatPump`
- `charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart::didPopNext`
- `charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart::onReady`
- `charging/ui/page/device/a5101/setting/device_manager/device_manager_logic.dart::pushPage`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
