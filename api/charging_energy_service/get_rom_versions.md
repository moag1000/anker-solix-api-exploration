> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_rom_versions

## Purpose

Checks for new firmware of an A17B1 station and its sub-devices over Wi-Fi (callers `FirmwareLogic::otaPageResumedCheck`, `FirmwareLogic::requestOTA`, `A17b1DeviceSettingLogic::checkOtaVersion`, `HomeSettingLogic::checkOtaVersion` through `HttpRequestControllerImpl::checkFirmwareWifi`) (string-only: inferred from the caller names, the chain is not in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_energy_service/get_rom_versions` (asm-traced): URL string `@0x25fadd8`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x25fadd0`, in `HttpRequestControllerImpl::checkFirmwareWifi` (`charging/http/http_request_repository_impl.dart @0x25facf0`), sent through `HttpRequestControllerImpl::requestHttp` (`@0x25fae00`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: both field types are not read) One sender. The map literal has the type arguments `<String, Object>` (`charging/http/http_request_repository_impl.dart @0x25fad8c`), which name no value type; both keys are stored without a guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `main_sn` | string | yes | `"<main_sn>"` | `charging/http/http_request_repository_impl.dart @0x25fad64` (value store `@0x25fad74`, parameter). One-hop caller evidence: `A17b1DeviceSettingLogic::checkOtaVersion` passes `deviceModel.value.field_6b` (`charging/ui/page/device/a17b1/device_setting/a17b1device_setting_logic.dart @0x26ed278`, call `@0x26ed2c4`); `deviceModel` is declared `late Rx<A17B1AnkerDevice>` (same file, class listing, offset 0xb4) and offset 0x6b of `AnkerDevice` is the getter `String dyn:get:deviceSn` (`base_service/device/anker_device.dart @0x22053d4`, load `@0x22053d8`); `A17B1AnkerDevice` reaches `AnkerDevice` through a mixin application (`charging/ble/device/A17B1/a17b1_anker_device.dart`, class header) |
| `device_rom_versions` | ? | yes | `<device_rom_versions>` | `charging/http/http_request_repository_impl.dart @0x25fad78` (value store `@0x25fad88`, parameter) |

## `param_type`/`cmd`

n/a

## Response model (link)

[`FirmwareUpdateModel`](../../models/firmware.md#firmwareupdatemodel), parsed by `FirmwareUpdateModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x25fae44` in the success closure `@0x25fae14`.

## Response

(asm-traced for the model) Top-level keys of `FirmwareUpdateModel` (`data/models.json`, `charging::FirmwareUpdateModel`): `packages` (Iterable), `sub_packages` (Iterable).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "main_sn": "<main_sn>",
  "device_rom_versions": "<device_rom_versions>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `checkFirmwareWifi` @0x25facf0 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::checkFirmwareWifi`
- `charging/ui/page/device/a17b1/a17b1firmware/firmware_logic.dart::otaPageResumedCheck`
- `charging/ui/page/device/a17b1/a17b1firmware/firmware_logic.dart::requestOTA`
- `charging/ui/page/device/a17b1/device_setting/a17b1device_setting_logic.dart::checkOtaVersion`
- `charging/ui/page/device/a17b1/home_setting/home_setting_logic.dart::checkOtaVersion`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `device_rom_versions`: the caller passes the result of `A17B1AnkerDevice::getSubPackageList` (`charging/ui/page/device/a17b1/device_setting/a17b1device_setting_logic.dart @0x26ed218`), whose return type is not shown (`_`, no info); the literal `<String, Object>` names no value type. `main_sn` is typed from one caller only; the other three callers (`FirmwareLogic` twice, `HomeSettingLogic`) were not read.
- Where the `packages` entries come from and which fields they carry: owned by [models/firmware.md](../../models/firmware.md#firmwareupdatemodel).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
