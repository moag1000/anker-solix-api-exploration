> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Page type: device · Owner page: this page

# Home Power Panel (A17B1)

## Contents

1. [PN, marketing name, generation/family](#pn-marketing-name-generationfamily)
2. [Features matrix](#features-matrix)
3. [Communication channels](#communication-channels)
4. [Cloud API service layers](#cloud-api-service-layers)
5. [Mode and EMS enums](#mode-and-ems-enums)
6. [Backup and disaster mode control](#backup-and-disaster-mode-control)
7. [BLE battery reserve command](#ble-battery-reserve-command)
8. [Device command control](#device-command-control)
9. [App structure (Dart)](#app-structure-dart)
10. [Python API implementation (upstream)](#python-api-implementation-upstream)
11. [Since/changed](#sincechanged)
12. [Known firmware notes](#known-firmware-notes)
13. [Known unknowns](#known-unknowns)
14. [Device-tested by](#device-tested-by)

Row numbers ("audit row N") count the table rows of [../docs/audit/devices.md](../docs/audit/devices.md) from the top; this page consumes rows 75 to 122. Method, tags and the Smi rule: [../METHODOLOGY.md](../METHODOLOGY.md). Payload and field facts live on the owner pages linked below.

## PN, marketing name, generation/family

`A17B1`, SOLIX Home Power Panel, the gateway of the SOLIX F3800 battery system. Upstream device type `powerpanel` (`SolixDeviceType.POWERPANEL`), site type `t_4`; the virtual capacity inherits from A1790 (F3800), 3840 Wh per unit (upstream-confirmed, `powerpanel.py`; audit row 75 NOT-FROM-ASM). Upstream issues: [ha-anker-solix #480](https://github.com/thomluther/ha-anker-solix/issues/480) and #447 (audit row 122 NOT-FROM-ASM). Product codes: [../reference/enums.md](../reference/enums.md).

## Features matrix

| feature | API (link) | MQTT (link) | BLE (link) | device-tested? |
|---|---|---|---|---|
| status (power flow, SOC, per-battery data) | [get_system_running_info](../api/charging_hes_svc/get_system_running_info.md) and the energy service | [JSON status 0500, 0502, 0503, 0505](../mqtt/a17b1.md#0500-0502-0503-0505-json-status-messages) (message ids upstream-confirmed) | none | no |
| backup and disaster mode | [charging_disaster_prepared](../api/charging_disaster_prepared/README.md), [device_command](../api/charging_hes_svc/device_command.md) | none | none | no |
| EMS mode, electricity strategy, off-grid switching | [device_command](../api/charging_hes_svc/device_command.md), [get_device_command](../api/charging_hes_svc/get_device_command.md); model [A5101DeviceCommandModel](../models/hes.md#a5101devicecommandmodel) | none | none | no |
| battery reserve (`scp`) | `syncSiteConfig` over HTTP (persists the value) | none | [ble/a17b1.md](../ble/a17b1.md) | no |
| realtime trigger (`0057`) | none | [0057](../mqtt/a17b1.md#0057-realtime-trigger) (upstream-confirmed binding) | not found in the A17B1 controller | no |

## Communication channels

| channel | support | details | tag |
|---|---|---|---|
| MQTT status | read-only | JSON inside the `a2` field of the messages 0500, 0502, 0503 and 0505, not binary TLV; topic and field map: [../mqtt/a17b1.md](../mqtt/a17b1.md) | upstream-confirmed (`mqttmap.py` lines 5807 to 5826) |
| MQTT commands | none | the `A17B1` group of upstream's `mqttmap.py` carries only the status messages, `0601` and `0057`; the old "zero entries in `mqttcmdmap.py`" is consistent | upstream-confirmed |
| BLE | minimal | the controller is a dual stack, ZX BLE plus MQTT transformer; commands: [../ble/a17b1.md](../ble/a17b1.md). The old claim "only Realtime Trigger (0x0057) plus EV charger commands" is not an asm fact: no `[0, 0x57]` list exists in the A17B1 controller (see Known unknowns) | asm-traced |
| Cloud API | primary | three service layers, below | upstream-confirmed |

The panel is controlled through the cloud API; MQTT delivers status only. BLE is disabled while WiFi is active, so BLE is never a live fallback for the cloud path.

## Cloud API service layers

Three service prefixes serve the panel (audit row 80 NOT-FROM-ASM, prose). The old endpoint counts (12+, 28+, 5+) were prose counts and are removed (audit rows 77 to 79); the directories list every endpoint page.

| service | purpose | pages |
|---|---|---|
| `charging_energy_service/` | energy data, configs, rate plans, firmware | [api/charging_energy_service](../api/README.md) |
| `charging_hes_svc/` | device commands, station config, EV charger binding | [api/charging_hes_svc](../api/charging_hes_svc/README.md) |
| `charging_disaster_prepared/` | backup and disaster mode control (auto and manual) | [api/charging_disaster_prepared](../api/charging_disaster_prepared/README.md) |

## Mode and EMS enums

The enum tables of the old page are owned by [../reference/enums.md](../reference/enums.md) and removed here.

- Home Power System `ModeState` (11 members, indices 0 to 10, no wire value): [enums, ModeState](../reference/enums.md#modestate) (audit rows 82 to 92, pool objects, OK).
- `EmsModeType` API values (selfConsumption, manualPowerBackup, timeOfUse, onlyBackupPower, severeWeatherMode, offGrid; the field `off_14` of the pool object): [enums, Energy, mode and price enums](../reference/enums.md#energy-mode-and-price-enums) (audit rows 93 to 98, OK). The `Index` column of the old table moved in 3.24.3, so only the API value is stable: see "Since/changed".
- The state fields of the MQTT JSON (`m`, `gs`, `bs`, `ps`, `soc`, `cp`) and their meanings are upstream's (audit row 81 NOT-FROM-ASM); owner [../mqtt/a17b1.md](../mqtt/a17b1.md).

## Backup and disaster mode control

Detail of every call: [../api/charging_disaster_prepared/README.md](../api/charging_disaster_prepared/README.md); step trace of the 3.24.3 values: [../docs/audit/charging_disaster_prepared.md](../docs/audit/charging_disaster_prepared.md).

Two independent modes can be active together: auto disaster (server-side weather alerts, `auto_disaster_switch`) and manual disaster (user picks a time window, `manual_disaster_switch` plus `manual_disaster_detail` with Unix timestamps). Reading and quitting: [get_site_device_disaster](../api/charging_disaster_prepared/get_site_device_disaster.md), [get_support_func](../api/charging_disaster_prepared/get_support_func.md), [quit_disaster_prepare](../api/charging_disaster_prepared/quit_disaster_prepare.md).

### Manual request values (3.24.3)

Tag: asm-traced. All sites are in `ak_soft_ems/manual_power_backup/manual_power_backup_logic.dart`.

- `type`: 1 or 2, computed from a bit test (raw 4 or 2 stored with `stur w`; @0x25ecd1c to @0x25ecd28; audit row 102). Upstream sends `type` 2 for the power-panel site (`apitypes.py` comment on `get_site_device_disaster`, upstream-confirmed).
- `manual_disaster_switch`: the JSON boolean `true`, not the integer 1 (`r16 = true`, @0x25ecd50; audit row 189 of the X1 section, see [x1_hes_e10.md](x1_hes_e10.md)).
- `manual_disaster_detail.disaster_type`: 2 (raw 4 stored with `stur w` into the map slot, @0x25ecd80; audit rows 100 and 106).
- `start_time` and `end_time` are Unix seconds (audit row 101 NOT-FROM-ASM: the old numbers 1712160000 and 1712246400 were an example, not constants).
- The quit request in 3.24.3 hardcodes its own `disaster_type` (2 in `showSevereWeatherModeDialog`, 1 in `showManualBackupModeDialog`); see the [charging_disaster_prepared audit](../docs/audit/charging_disaster_prepared.md).

### Models (class sizes)

Tag: asm-traced. Sizes are class-header values, not Smi immediates (audit rows 103, 104, 106).

| class | size | file | note |
|---|---|---|---|
| `DisasterSetting` | 0x30, extends `ChangeNotifier` | `device_disaster_model.dart` | fields `auto_disaster_switch`, `manual_disaster_switch`, `disaster_details` (class header) |
| `DisasterStatus` (IoT kit) | 0xc | `device_disaster_model.dart` | two classes carry this name; the old page's 0x1c belongs to the station-mixin class in `auto_disaster.dart` |
| `DisasterStatus` (station mixin) | 0x1c | `auto_disaster.dart` | same three keys: `auto_disaster_status`, `manual_disaster_status`, `current_disaster_detail` |
| `DisasterPrepareDetail` | 0x10 (3.18.0: 0xc) | see [../models/hes.md](../models/hes.md#disasterpreparedetailsmodel) | 7 JSON keys; `disaster_type` is 2 for the manual request (`manual_power_backup_logic.dart` @0x25ecd80) |

## BLE battery reserve command

Separate from the disaster system. Over BLE, `sendA17B1Command()` sends the command named `"scp"` (set cycle percent) with the battery reserve value (0 to 100, old page, not audited); the app then persists it with `syncSiteConfig()` over HTTP. The string `"scp"` is still in the 3.24.3 object pool (`[pp+0x979b0]`; 3.18.0: `[pp+0x757f8]`) and is used in `system_policy_logic.dart` and `electricity_scene_logic.dart` (audit row 107). The command frame: [../ble/a17b1.md](../ble/a17b1.md).

## Device command control

`electricity_strategy` and `off_grid_switching` are nested objects of `device_command`; their field lists are owned by [../models/hes.md](../models/hes.md#a5101devicecommandmodel) and [device_command](../api/charging_hes_svc/device_command.md). The old example values (`conserve_percent` 20, `off_grid_enable` 1, `off_grid_sensitivity` 3) were examples (audit row 110 NOT-FROM-ASM); `mode` 1 is `EmsModeType.selfConsumption` (`off_14` of the pool object `[pp+0x6aee0]`, audit row 109).

## App structure (Dart)

Tag: asm-traced (file and class names). Paths under `charging/ui/page/`.

| page | path | purpose |
|---|---|---|
| A17B1HomePage | `device/a17b1/device_home/` | main device view |
| A17B1SystemPolicyLogic | `device/a17b1/system_policy/` | backup and disaster strategy |
| A17B1ManualBackupPowerLogic | `device/a17b1/device_setting/manual_backup_power/` | manual backup config |
| A17B1ElectricitySceneLogic | `device/a17b1/a17b1electricity_scene/` | electricity management |
| A17B1SystemTestLogic | `device/a17b1/a17b1system_test/` | diagnostics |
| A17B1FirmwareLogic | `device/a17b1/a17b1firmware/` | OTA updates |
| A17B1SelectDevicesLogic | `device/a17b1/a17b1select_devices/` | device binding |
| A17b1StationLogic, A17B1AutoDisasterMixin | `station/A17b1/` | station overview, auto disaster handling |
| AutoDisasterSetting, ManualDisasterSetting | `station/view/auto_disaster/` | auto and manual disaster config |

BLE device files in `charging/ble/device/A17B1/`: `a17b1_anker_device.dart` (core device abstraction), `a17b1_device_commands.dart` (static command parsing), `a17b1_device_controller.dart` (dual protocol, ZX BLE plus MQTT), `mqtt_set_order_model.dart` (MQTT command serialization). The command architecture (`sendA17B1Command()` assembles `messageId`, `config`, `cmdId`, `data`; `handleMQTTDeviceResponse()` and `handleZXProtocolDeviceResponse()` for responses) is described in [../ble/a17b1.md](../ble/a17b1.md).

## Python API implementation (upstream)

Tag: upstream-confirmed. `AnkerSolixPowerpanelApi` in `api/powerpanel.py` of thomluther/anker-solix-api. The old page gave method line numbers for a 1452-line file; the local checkout (17d85d0, 2026-03-27) has 1574 lines and the numbers no longer match, so they are removed (audit rows 111 to 120 NOT-FROM-ASM).

Methods: `_update_dev()` (device data consolidation, A17B1 to A1790 capacity mapping), `update_sites()`, `update_site_details()`, `update_device_energy()`, `get_system_running_info()`, `get_avg_power_from_energy()` (5-minute average power from multi-source energy), `energy_statistics()` (hes, solar, home, grid, pps, diesel), `energy_daily()`, `extract_energy()`.

`API_CHARGING_ENDPOINTS` in `apitypes.py` lines 205 to 218 has 12 entries in the current checkout (audit row 121): `get_error_info`, `get_system_running_info`, `energy_statistics`, `get_rom_versions`, `get_device_info`, `get_wifi_info`, `get_installation_inspection`, `get_utility_rate_plan`, `report_device_data`, `get_configs`, `get_sns`, `get_monetary_units`.

## Since/changed

| item | old page (3.18.0 reading) | 3.24.3 |
|---|---|---|
| manual `disaster_type` in the request | 4 | 2 (`manual_power_backup_logic.dart` @0x25ecd80; the old page said 4) |
| `DisasterPrepareDetail.disaster_type` | "4 = manual" | 2 (same site @0x25ecd80) |
| BLE opcodes "0x233 response, 0x45a dismiss" | listed as BLE opcodes | not BLE opcodes, both are unboxed 64-bit ints so the numbers are right: 563 (0x233) is fired as a `MessageEvent` in `a17b1_device_controller.dart` @0x3b4a000 and compared (`cmp x0,#0x233`) in `back_power_logic.dart` @0x26e31d4, where the branch leads to `_dealWithBleResponse`; 1114 (0x45a) is fired in `request_timeout_util.dart` @0x33d6238 and compared (`cmp x0,#0x45a`) in `back_power_logic.dart` @0x26e3214, where the branch calls `GetExtension.dismiss` |
| `EmsModeType` `Index` column 0..5 | indices of six members | indices moved: 3.24.3 added `normalMode` (`power_usage_scenario_controller.dart` @0x37aec0c), `customMode`, `timeSlot` and `smartMode`, see [enums](../reference/enums.md#energy-mode-and-price-enums); use the API value |
| `"scp"` pool offset | `[pp+0x757f8]` | `[pp+0x979b0]` (string unchanged) |
| `DisasterStatus` size | 0x1c | 0xc for the IoT-kit class, 0x1c for the station-mixin class |

Audit rows in table order: 100 and 106 (WRONG), 108 (WRONG), 99 (CHANGED), 107 (CHANGED), 104 (OK, two classes with one name).

## Known firmware notes

- No firmware is recorded for any statement on this page.

## Known unknowns

Tag: untagged by design (no API fact).

- The meaning of `auto_disaster_status` and `manual_disaster_status` equal to 0 ("inactive" in the old page): the keys are read (strings @0x22d6af0 and @0x22d6b48 in `device_disaster_model.dart`), the meaning is not an asm fact (audit row 105).
- Which A17B1 call path reaches the realtime trigger `0057`, if any (audit row 76).
- The old "Implementation gaps for ha-anker-solix" list (disaster service, `device_command` and `get_device_command` SET and GET, `check_function`, `get_configs` param types, `get_station_config_and_status`, six endpoints not implemented upstream) and the old `API_CHARGING_ENDPOINTS` "not implemented" names were not re-checked against the current upstream checkout (audit row 122 NOT-FROM-ASM); the endpoint strings named in them appear in `apitypes.py` lines 430 to 485 of the checkout.
- The old list of EMS strategy mode strings (`self_consumption`, `manual_backup`, `peak_shaving`, `custom_mode`, `time_of_use`, `smart`, `dynamic`, `fixed`) was not audited; the numeric values are in the `EmsModeType` enum.
- Open test requests for this product: [../docs/DEVICE_TEST_BACKLOG.md](../docs/DEVICE_TEST_BACKLOG.md).

## Device-tested by

none
