> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# report_data

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v2/device/report_data`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x2603778`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x26031c4` |
| `data_type` | ? | ? | ? | `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x26031c4` |
| `data.soc` | ? | ? | ? | `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x26031c4` |
| `report_time` | ? | ? | ? | `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x26031c4` |

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

- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart`: `_uploadLowBatteryWarning` @0x26031c4 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::onMessageDispatch`

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
