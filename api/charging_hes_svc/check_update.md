> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# check_update

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/check_update`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x479df04`
(literal also at 5 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `stationId` | ? | ? | ? | `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x479de70` |

Rows are the union over 5 senders; `source` is the first sender that sets the key.

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

- `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart`: `checkOtaVersion` @0x479de70 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart`: `checkOtaVersion` @0x28dd70c (requestHttp; encrypted: default-true (requestHttp) — verify); `restartCheckOtaVersion` @0x28dcf20 (requestHttp; encrypted: default-true (requestHttp) — verify); `startCheckOtaVersion` @0x28da980 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart`: `checkOtaVersion` @0x292d4d4 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/util/demosite_util_impl.dart`: `DemoSiteUtilImpl` @0x4a33a6c (URL literal only, no `*Http*` call)

Called from: `charging/boostrap_impl.dart::DIInit`, `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart::updateDeviceStationId`, `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart::bottomButtonTap`, `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart::onReady`, `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart::resetDevice`, `charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart::didPopNext`, `charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart::onReady`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
