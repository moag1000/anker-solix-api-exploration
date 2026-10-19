> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# add_site_devices

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/site/add_site_devices`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x26f705c`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys found by the extractor. <!-- TODO -->

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

- `charging/http/http_request_repository_impl.dart`: `multiAddDeviceInfo` @0x26f6f78 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::multiAddDeviceInfo`
- `charging/ui/page/device/a1782/station/ac_params_settings/ac_params_settings_logic.dart::next`
- `charging/ui/page/device/a1782/station/electricity_scene/a1782_electricity_scene_logic.dart::createSite`
- `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart::createSite`
- `charging/ui/page/device/a17b1/a17b1select_devices/a17b1select_devices_logic.dart::addDeviceToStation`
- `charging/ui/page/device/a17c1/open_process/open_process_logic.dart::join`
- `charging/ui/page/device/a17c1/open_process/open_process_logic.dart::mainDeviceJoin`
- `charging/ui/page/device/a17c1/open_process/open_process_logic.dart::next`
- `charging/ui/page/device/connect/create_join_device_to_system/join_system/join_system_logic.dart::join`
- `charging/ui/page/device/connect/zx_config_wifi_success/zx_config_wifi_succees_logic.dart::addDeviceToStation`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/add_devices_progress/add_devices_progress_logic.dart::multiAddDevices`
- `charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart::addSitePPS`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
