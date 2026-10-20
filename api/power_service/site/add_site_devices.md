> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# add_site_devices

## Purpose

Adds devices to a site: the device-joining flows (A1782 AC params and electricity scene, A17B1 select-devices and scene, A17C1 open process, join-system, WiFi-config success, add-devices progress, station home info and the EV charger station selection) call `multiAddDeviceInfo`, or `AKIotEVChargeCommand::addSiteDevice` through the IoT kit.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/site/add_site_devices` (asm-traced): URL string at `http_request_repository_impl.dart @0x26f705c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x26f7054`, in `HttpRequestControllerImpl::multiAddDeviceInfo` (`http_request_repository_impl.dart @0x26f6f78`).

The IoT-kit sender `AKIotEVChargeCommand::addSiteDevice` (`ev_charge_command.dart @0x3964400`) puts the path `"power_service/v1/site/add_site_devices"` (`@0x39644a4`, no leading slash), the string literal `"POST"` (`@0x39644bc`) and a `param` map into a command map for `akIoTKitManager.handle` (`@0x3964500`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The repository builder `multiAddDeviceInfo` (`http_request_repository_impl.dart @0x26f6f78`) has no map literal; each of its 13 callers builds its own body. Key sets read in the callers (value types are field reads and parameters, not read):

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | yes | | `ACParamsSettingsLogic::next` (`ac_params_settings_logic.dart`, key `@0x3cd0f4c`), A1782 scene closure (`a1782_electricity_scene_logic.dart`, key `@0x28d3fec`), A17B1 scene closure (key `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart @0x3d07f18`), A17C1 `OpenProcessLogic` `next`/`join`/`mainDeviceJoin` (keys `charging/ui/page/device/a17c1/open_process/open_process_logic.dart @0x3db2688`, `@0x3db451c`, `@0x3db6e84`), `JoinSystemLogic::join` (`charging/ui/page/device/connect/create_join_device_to_system/join_system/join_system_logic.dart @0x3f23f04`), `ZxConfigWifiSucceesLogic::addDeviceToStation` (`charging/ui/page/device/connect/zx_config_wifi_success/zx_config_wifi_succees_logic.dart @0x26f6bf8`), `StationHomeInfoLogic::addSitePPS` (`charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart @0x279f684`) |
| lists | ? | varies | | `solarbank_pps_list`, `grid_list`, `solar_list`, `pps_list`, `solarbank_list`, `powerpanel_list`, `smartplug_list`, `combiner_box_list`: one to four of them per caller (for example `solarbank_pps_list` `charging/ui/page/device/a1782/station/ac_params_settings/ac_params_settings_logic.dart @0x3cd0f68`, `grid_list` `@0x3cd0fe4`, `solar_list` `charging/ui/page/device/a17b1/a17b1electricity_scene/electricity_scene_logic.dart @0x3d07f34`, `pps_list` `charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart @0x279f6d8`) |
| `app_ability` | object | optional | | key `charging/http/http_request_repository_impl.dart @0x26f7018` in `multiAddDeviceInfo` (function `@0x26f6f78`); the callers pass it as the named argument `app_ability` (call descriptor `charging/ui/page/device/a17c1/open_process/open_process_logic.dart @0x3db273c`); the maps `{site_power_limit: true}` built in `OpenProcessLogic` (key `@0x3db26dc`, literal `true` `@0x3db26e8`), `JoinSystemLogic` (`charging/ui/page/device/connect/create_join_device_to_system/join_system/join_system_logic.dart @0x3f24024`) and `AddDevicesProgressLogic` (`charging/ui/page/device/main/sitation_energy_system/station_home_settings/add_devices_progress/add_devices_progress_logic.dart @0x34a5dec`); the key `app_ability` itself was not located in these callers |
| `site_id` | ? | yes | | key `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x3964434` of the IoT-kit sender `addSiteDevice`: `param` map typed `<String, dynamic>` (`@0x396445c`), value store `@0x3964444` (parameter at `fp-0x10`) |
| `charging_pile_list` | ? | yes | | IoT-kit sender: key `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x3964448`, value store `@0x3964458` (parameter at `fp-0x8`) |

## `param_type`/`cmd`

n/a

## Response model (link)

Not determined. The repository builder passes forwarding templates (`rx_workers.dart @0x228e574`, `http_request_repository_impl.dart @0x2375ad8`); the callers' callbacks were read for `ACParamsSettingsLogic::next` only (`ac_params_settings_logic.dart @0x3cd10b4`: logs `加入电站成功`, refreshes the site list; no `fromJson`). The extractor's `EmsModeModel` attribution was not confirmed.

## Response

Not determined (see Response model).

## Example request/response

Request, synthesized (key set of the AC-params caller; types unresolved)

```json
{"site_id": "<site_id>", "solarbank_pps_list": "<list>", "grid_list": "<list>"}
```

Response: not determined.

## Errors seen

None traced. The callbacks read (`ac_params_settings_logic.dart @0x3cd10b4`, the failure closure `zx_config_wifi_succees_logic.dart @0x26f70a0` that logs `加入电站失败`) compare no code; the other callers' callbacks were not read. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `multiAddDeviceInfo` @0x26f6f78 (encryptionRequestHttp; encrypted: true)
- `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart`: `addSiteDevice` @0x3964400 (URL literal only, no `*Http*` call; sends in the same function (`AKIoTKitManagerImpl::handle`); resolved from the URL literal at `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x39644a4` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

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
- `ev_charger/src/ev_charger/page/home/load_balancing/select_station/evselect_station_logic.dart::_executeAddSiteDevice`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- Value types of every key (parameters and field reads in 13 callers). Header stays string-only. — attempted 2026-10-20 (two-hop not readable: 13 callers build the body with parameters and field reads (named keys seen: `site_id`, `grid_list`, `solarbank_list`, `pps_list`, `solar_list`, `powerpanel_list`, `smartplug_list`, `combiner_box_list`, `site_power_limit`, `devices`); no declared types or defaults were read in this pass. Header stays string-only)
- Which callers send `app_ability` and with which keys: only the `{site_power_limit: true}` maps were located. — traced 2026-10-20: the key `site_power_limit` is loaded at `OpenProcessLogic.next` (`charging/ui/page/device/a17c1/open_process/open_process_logic.dart @0x3db2744`), `.join` (`@0x3db45f0`), `.mainDeviceJoin` (`@0x3db6f84`) and in `AddDevicesProgressLogic` (`charging/ui/page/device/main/sitation_energy_system/station_home_settings/add_devices_progress/add_devices_progress_logic.dart @0x34a5e6c`); the map around `app_ability` was not decoded
- The response handling beyond the AC-params caller. — traced 2026-10-20: not decoded in this pass (response handling of ten callers); the reason given in the bullet stands

## Device-tested by

none
