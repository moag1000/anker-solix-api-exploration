> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# check_update

## Purpose

Checks the cloud for a newer firmware (OTA) version of a station; five senders in the OTA and settings logic classes (`A5101MqttLogic::checkOtaVersion`, `A5101FirmwareUpdateLogic::checkOtaVersion`, `startCheckOtaVersion`, `restartCheckOtaVersion` and `HomeSettingLogic::checkOtaVersion`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/check_update` (asm-traced): URL string at `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x479df04`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x479defc`, in `A5101MqttLogic::checkOtaVersion` (`charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x479de70`), sent through `requestHttp` (`@0x479df20`).

Same URL and method object in the other sender(s) read:

- `A5101FirmwareUpdateLogic::checkOtaVersion` (`charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x28dd70c`): URL string `@0x28dd824`, method object `Method.post` (`pp+0xa7e0`) at `@0x28dd81c`, sent through `requestHttp` (`@0x28dd848`).
- `A5101FirmwareUpdateLogic::restartCheckOtaVersion` (`charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x28dcf20`): URL string `@0x28dd034`, method object `Method.post` (`pp+0xa7e0`) at `@0x28dd02c`, sent through `requestHttp` (`@0x28dd050`).
- `A5101FirmwareUpdateLogic::startCheckOtaVersion` (`charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x28da980`): URL string `@0x28daadc`, method object `Method.post` (`pp+0xa7e0`) at `@0x28daad4`, sent through `requestHttp` (`@0x28dab04`).
- `HomeSettingLogic::checkOtaVersion` (`charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart @0x292d4d4`): URL string `@0x292d5e0`, method object `Method.post` (`pp+0xa7e0`) at `@0x292d5d8`, sent through `requestHttp` (`@0x292d5fc`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `A5101MqttLogic::checkOtaVersion` (`charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart`, call `@0x479df20`, argument list `@0x479df18`), `A5101FirmwareUpdateLogic::checkOtaVersion` (`charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart`, call `@0x28dd848`, argument list `@0x28dd840`), `A5101FirmwareUpdateLogic::restartCheckOtaVersion` (`charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart`, call `@0x28dd050`, argument list `@0x28dd048`), `A5101FirmwareUpdateLogic::startCheckOtaVersion` (`charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart`, call `@0x28dab04`, argument list `@0x28daafc`), `HomeSettingLogic::checkOtaVersion` (`charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart`, call `@0x292d5fc`, argument list `@0x292d5f4`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `A5101MqttLogic::checkOtaVersion` (`charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x479decc`, 1 key); `A5101FirmwareUpdateLogic::checkOtaVersion` (`charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x28dd7d4`, 1 key); `A5101FirmwareUpdateLogic::restartCheckOtaVersion` (`charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x28dcff8`, 1 key); `A5101FirmwareUpdateLogic::startCheckOtaVersion` (`charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x28daa8c`, 1 key); `HomeSettingLogic::checkOtaVersion` (`charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart @0x292d5a8`, 1 key). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `stationId` | string | yes | `"<stationId>"` | `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x479deb0`; `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x28dd750`; `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x28dcf74`; `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x28daa08`; `charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart @0x292d564` |

Value source of `stationId` (app side, traced 2026-10-20): in `A5101MqttLogic` it is `field_97` (`charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x479deb0`), set by `updateDeviceStationId` (`@0x479dca4`) from `FamilyMainPageLogic::_changeDevice` (`charging/ui/page/family/family_main_page_logic.dart @0x479d134`), which passes `field_7` of the value of an `Rx` field (offset 451, `@0x479d0f4`..`@0x479d110`) of the family page logic or the empty string; the class behind that `Rx` is not named in the asm, so the format of the string is not visible. The other four senders were not followed.

## `param_type`/`cmd`

n/a

## Response model (link)

- `charging::A5101OtaCheckUpdateModel`, parsed by `A5101OtaCheckUpdateModel.fromJson` at `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x479df8c` (success closure `@0x479df3c`, `bl` target `[package:charging/model/a5101/a5101_ota_check_update_model.dart]`).
- Also parsed by `A5101OtaCheckUpdateModel.fromJson` at `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x28dd960` (success closure `@0x28dd928`, `bl` target `[package:charging/model/a5101/a5101_ota_check_update_model.dart]`).
- Also parsed by `A5101OtaCheckUpdateModel.fromJson` at `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x28dd0ec` (success closure `@0x28dd06c`, `bl` target `[package:charging/model/a5101/a5101_ota_check_update_model.dart]`).
- Also parsed by `A5101OtaCheckUpdateModel.fromJson` at `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x28dac14` (success closure `@0x28dabdc`, `bl` target `[package:charging/model/a5101/a5101_ota_check_update_model.dart]`).
- Also parsed by `A5101OtaCheckUpdateModel.fromJson` at `charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart @0x292d668` (success closure `@0x292d618`, `bl` target `[package:charging/model/a5101/a5101_ota_check_update_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::A5101OtaCheckUpdateModel`): `device_type` (String?), `rom_version_name` (String?), `current_version` (String?), `introduction` (String?), `upgrade_flag` (int?), `force_upgrade` (bool?), `full_package` (FullPackage?), `pop` (bool?), `children` (unknown), `delay` (int?), `left_time` (int?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "stationId": "<stationId>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`. The compare `cmp w0, #0xc8` in the failure closure of `A5101FirmwareUpdateLogic::checkOtaVersion` (`charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x28dd8ac`) tests a status value read through `value()` (`@0x28dd8a8`), not the response code.

## Callers in app

- `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart`: `checkOtaVersion` @0x479de70 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart`: `checkOtaVersion` @0x28dd70c (requestHttp; encrypted: default-true (requestHttp) — verify); `restartCheckOtaVersion` @0x28dcf20 (requestHttp; encrypted: default-true (requestHttp) — verify); `startCheckOtaVersion` @0x28da980 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart`: `checkOtaVersion` @0x292d4d4 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/util/demosite_util_impl.dart`: `DemoSiteUtilImpl` @0x4a33a6c (URL literal only, no `*Http*` call)

Called from:

- `charging/boostrap_impl.dart::DIInit`
- `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart::updateDeviceStationId`
- `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart::bottomButtonTap`
- `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart::onReady`
- `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart::resetDevice`
- `charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart::didPopNext`
- `charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart::onReady`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The `stationId` of the senders other than `A5101MqttLogic` (the firmware-update and home-setting logic classes): the source chain was not followed — traced 2026-10-20, see Request for the `A5101MqttLogic` chain.
- Which of the five senders the app uses first on a fresh settings visit: only the call sites were read. — reclassified: device test row 151 (traced 2026-10-20: the five senders sit in separate page logic classes, `a5101_mqtt_logic.dart`, `a5101_firmware_update_logic.dart` (three) and `home_setting_logic.dart`, so the order is the order of user navigation, not fixed in the asm)
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
