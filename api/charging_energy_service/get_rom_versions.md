> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_rom_versions

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_energy_service/get_rom_versions`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x25fadd8`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `main_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x25facf0` |
| `device_rom_versions` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x25facf0` |

## `param_type`/`cmd`

n/a

## Response model (link)

<!-- TODO -->

## Response

<!-- TODO -->

## Example request/response

<!-- TODO -->

## Errors seen

`api/errors.md`: <!-- TODO -->

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `checkFirmwareWifi` @0x25facf0 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from: `charging/http/http_request_repository.dart::checkFirmwareWifi`, `charging/ui/page/device/a17b1/a17b1firmware/firmware_logic.dart::otaPageResumedCheck`, `charging/ui/page/device/a17b1/a17b1firmware/firmware_logic.dart::requestOTA`, `charging/ui/page/device/a17b1/device_setting/a17b1device_setting_logic.dart::checkOtaVersion`, `charging/ui/page/device/a17b1/home_setting/home_setting_logic.dart::checkOtaVersion`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
