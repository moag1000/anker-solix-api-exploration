> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Page type: device · Owner page: this page

# Solarbank — A17C0, A17C1, A17C2, A17C3, A17C5

Row numbers ("audit row N") count the table rows of [../docs/audit/devices.md](../docs/audit/devices.md) from the top; this page consumes rows 1 to 35. Method, tags and the Smi rule: [../METHODOLOGY.md](../METHODOLOGY.md). Payloads, commands and field maps live on the owner pages linked below; this page keeps the product overview and the device-test record. The finished Gen 3 page is [a17c5.md](a17c5.md).

## PN, marketing name, generation/family

| PN | marketing name | generation / role | source |
|---|---|---|---|
| `A17C0` | Solarbank E1600 | Gen 1 | upstream-confirmed (old page; names are product names, not asm facts) |
| `A17C1` | Solarbank 2 E1600 Pro | Gen 2, flagship | upstream-confirmed |
| `A17C2` | Solarbank 2 E1600 AC | Gen 2, AC-coupled | upstream-confirmed |
| `A17C3` | Solarbank 2 E1600 Plus | Gen 2, budget | upstream-confirmed |
| `A17C5` | Solarbank 3 E2700 Pro | Gen 3, bidirectional | upstream-confirmed, see [a17c5.md](a17c5.md) |

Consumer balcony solar, sold on anker.com and Amazon EU. Product codes are classified in [../reference/enums.md](../reference/enums.md). This is the largest user base of the repository (more than 70 upstream issues, audit row 34 NOT-FROM-ASM) and the most actively developed device category of the upstream integration.

## Features matrix

| feature | API (link) | MQTT (link) | BLE (link) | device-tested? |
|---|---|---|---|---|
| schedule (`param_type` of the 17C1 schedule) | [set_site_device_param](../api/power_service/site/set_site_device_param.md), [get_site_device_param](../api/power_service/site/get_site_device_param.md), table [param_types](../api/param_types.md); flow: [solarbank2_schedule](../flows/solarbank2_schedule.md) | [a17c1](../mqtt/a17c1.md) | [ble/a17c1.md](../ble/a17c1.md) | upstream-confirmed (upstream library), no record here |
| system output power limit, SB1 (`A17C0`) | none (asm-traced, absence: the A17C0 UI and BLE trees hold no `power_limit`, `set_device_attrs`, `get_power_limit` or `PowerSliderView` code; its settings offer device name, temperature unit, firmware, safety SoC, micro-inverter brand, installation method, WiFi deploy, accessories and an energy plan of time-slot home-load targets, which is not an output limit: `a17c0setting_view.dart`, `a17c0energy_plan_logic.dart @0x3f66860`) | none | none | yes, negative: thomluther, 2026-10-19, SB1 cannot set an output limit though `get_power_limit` returns the same fields as for newer devices (firmware not recorded; [issue #1](https://github.com/moag1000/anker-solix-api-exploration/issues/1)) |
| system output power limit, SB2 (`A17C1`, `A17C3`, `A17C2`) | `set_device_attrs` attribute `power_limit` ([set_device_attrs](../api/power_service/app/device/set_device_attrs.md)); no `param_type` 18 or 19 in the A17C1 settings tree (asm-traced, absence); picker decision tree: [solarbank_power_limit_change](../flows/solarbank_power_limit_change.md#output-picker-decision-tree); the type-19 slider page is reachable only behind an AE100 dock, see [the app gate](../api/power_service/site/get_power_limit.md#who-gets-the-output-limit-page-app-gate) | `0080` [setDevicePowerLimit](../mqtt/a17c1.md#0080-setdevicepowerlimit), `setDevicePowerLimit` (a17c1_device_controller.dart @0x2277580) | [ble/a17c1.md](../ble/a17c1.md) | reported by thomluther, 2026-10-19 (device-tested, as reported; wire detail not recorded): SB2 supports neither `param_type` 18 nor 19, the limit goes via MQTT plus an attribute call; see [owner](../api/power_service/site/set_site_device_param.md#device-tested-by) |
| system output power limit, SB3 (`A17C5`, `param_type` 19) | [set_site_device_param](../api/power_service/site/set_site_device_param.md) (`SOLARBANK_POWER_LIMIT`); flows: [system_output_limit](../flows/system_output_limit.md), gate: [get_power_limit](../api/power_service/site/get_power_limit.md#who-gets-the-output-limit-page-app-gate) | unknown, see [a17c5.md](a17c5.md) | unknown | yes, only for values from `power_limit_option` unless `display_type` 1 is sent; see [owner](../api/power_service/site/set_site_device_param.md#device-tested-by) |
| safety SOC / reserve | [set_site_device_param](../api/power_service/site/set_site_device_param.md); flow: [solarbank_soc_reserve_change](../flows/solarbank_soc_reserve_change.md) | `0067` [setSoc](../mqtt/a17c1.md#0067-setsoc), `setSoc` (a17c1_device_controller.dart @0x3d95578) | [ble/a17c1.md](../ble/a17c1.md) | yes: mqtt_monitor, A17C1 FW 1.0.6.10 |
| temperature unit | none | `0050` [setTempUnit](../mqtt/a17c1.md#0050-settempunit), `setTempUnit` (a17c1_device_controller.dart @0x3d98ffc); flow: [solarbank_temperature_unit](../flows/solarbank_temperature_unit.md) | [ble/a17c1.md](../ble/a17c1.md) | yes: mqtt_monitor, A17C1 FW 1.0.6.10 |
| usage mode | [set_site_device_param](../api/power_service/site/set_site_device_param.md); values: [enums](../reference/enums.md#solarbank-usage-mode-upstream) | `005e` [setBackPower, setTacticsTime, setPeakValley](../mqtt/a17c1.md#005e-setbackpower-settacticstime-setpeakvalley), sites in a17c1_device_controller.dart @0x288b284, @0x281aadc, @0x428b0f4 | [ble/a17c1.md](../ble/a17c1.md) | yes: mqtt_monitor, usage modes 1 and 3 only |
| AC socket / off-grid switch | none | `0073` [setOffGridSwitch](../mqtt/a17c1.md#0073-setoffgridswitch), `setOffGridSwitch` (a17c1_device_controller.dart @0x3d79d44) | [ble/a17c1.md](../ble/a17c1.md) | no (upstream only) |
| grid export (`0080` fields, `setDevicePowerLimit` in a17c1_device_controller.dart @0x2277580) | [set_device_attrs](../api/power_service/app/device/set_device_attrs.md); flow: [solarbank_toggle_grid_export](../flows/solarbank_toggle_grid_export.md) | `0080` [setDevicePowerLimit](../mqtt/a17c1.md#0080-setdevicepowerlimit) | [ble/a17c1.md](../ble/a17c1.md) | no (upstream only) |
| inverter type (A17C0 only) | none | `0068` `setMicroInversionModel` (a17C0_device_controller.dart @0x261d4c8), see [a17c0](../mqtt/a17c0.md#setters-0050-005e-0067-0068-0071) | [ble/a17c0.md](../ble/a17c0.md) | no |
| light mode (A17C1) | none | `0068` [setDeviceLightMode](../mqtt/a17c1.md#0068-setdevicelightmode) (upstream-confirmed `CMD_SB_LIGHT_MODE`) | [ble/a17c1.md](../ble/a17c1.md) | no |
| max load | none | `005a`, no app builder, see [a17c1](../mqtt/a17c1.md#opcodes-without-a-confirmed-app-builder-005a-0069) | none | yes: mqtt_monitor, A17C1 FW 1.0.6.10 (upstream-confirmed; audit row 24 UNVERIFIABLE for the app side) |
| third-party PV | [set_site_device_param](../api/power_service/site/set_site_device_param.md) (cloud) | `0085`, cloud-driven, upstream-confirmed only; see [upstream_commands](../mqtt/upstream_commands.md) | none | no |

All other features: unknown (not researched for this page).

## Commands, fields and values consumed from the audit

Tag: asm-traced unless stated.

- The `param_type` list (1, 2, 3, 5, 6, 18, 19, 20, 23, 26) is a table of string literals in the request map, not Smi values (audit rows 1 to 10 NOT-FROM-ASM). The old table is replaced by the owner: [../api/param_types.md](../api/param_types.md). The example payloads of types 6 and 18 (audit rows 11 to 13) are owned by the same page and by [set_site_device_param](../api/power_service/site/set_site_device_param.md); `"mode_type": 3` is `ModeTypeCustom` (pool object, `AiModeEnum`, audit row 11; value table in [../reference/enums.md](../reference/enums.md)). The `feed-in_power_limit` key is spelled with a hyphen, not an underscore (old page, upstream-confirmed).
- `param_type` 19 (power limit): the app and the upstream library send different `cmd` values (`http_request_repository_impl.dart` `setSiteDevicePowerLimit` @0x43558c4, audit row 14); the values and the acceptance status are owned by [../api/param_types.md](../api/param_types.md) and [the endpoint page](../api/power_service/site/set_site_device_param.md). The old section "Corrected 2026-10-19" is superseded by those pages.
- Opcodes (pool lists `[0, 0x..]`, real bytes, audit rows 22 to 28), all in `a17c1_device_controller.dart` unless stated: `0050` temperature unit (`setTempUnit` @0x3d98ffc), `0067` power cutoff (`setSoc` @0x3d95578), `005e` usage mode (`setTacticsTime` @0x288b284, `setBackPower` @0x281aadc, `setPeakValley` @0x428b0f4), `0073` AC socket (`setOffGridSwitch` @0x3d79d44), `0080` grid export (`setDevicePowerLimit` @0x2277580). `0068` inverter type is `a17C0_device_controller.dart` `setMicroInversionModel` @0x261d4c8.
- `0068` fields `a5` brand, `a6` model, `a7` minimum load and `a8` maximum load: the keys of `setMicroInversionModel` in `a17C0_device_controller.dart` are 330, 332, 334, 336 halved (@0x261cf54, @0x261cfbc, @0x261d020, @0x261d0a8; audit row 31). This is the A17C0 reading. On A17C1 the app binds `0068` to the light function, so the old page's "Inverter Type" label is right only for A17C0 (see [../mqtt/a17c1.md](../mqtt/a17c1.md#0068-setdevicelightmode)). The binding of `a5` to brand, `a6` to model, `a7` to minimum load and `a8` to maximum load is not traced: the audit confirms the tag numbers only, and [../mqtt/a17c0.md](../mqtt/a17c0.md) lists the meanings as unknown (see its Known unknowns).
- `0080` fields: only `a2` to `a6` of `setDevicePowerLimit` were confirmed by the FLOWS and BLE audits; `a9` (key 338) was not found (audit row 30 UNVERIFIABLE).
- `005a` (max load) and `0085` (third-party PV) have no builder in the app (audit rows 24 and 29 UNVERIFIABLE); they are known from upstream and mqtt_monitor only. Their field names (`a2` max_load, `a3` max_load_type; `a2` on or off) are upstream (audit rows 32 and 33).
- Usage mode values (`smartmeter` 1 to `time_slot` 8) are upstream's `SolarbankUsageMode`, not an app enum (audit rows 15 to 21 NOT-FROM-ASM); the table is owned by [../reference/enums.md](../reference/enums.md#solarbank-usage-mode-upstream).

### Attributes of `set_device_attrs` (upstream-confirmed)

Upstream's `set_device_attributes` and the station helpers in `api/api.py` write these keys inside `{"device_sn": ..., "attributes": {...}}` (audit row 35 NOT-FROM-ASM; field list: [../api/power_service/app/device/set_device_attrs.md](../api/power_service/app/device/set_device_attrs.md)).

| field | meaning | tag |
|---|---|---|
| `pv_power_limit` | PV input limit (W) | upstream-confirmed (`api.py`, `set_device_attributes` docstring) |
| `ac_power_limit` | AC input limit (W) | upstream-confirmed |
| `power_limit` | AC output limit (W) | upstream-confirmed |
| `switch_0w` | grid export: 0 allow, 1 block (`0 if grid_export else 1`) | upstream-confirmed |
| `enable_0w` | zero-feed-in enable | upstream-confirmed |

## Response models

[../models/solarbank.md](../models/solarbank.md) (`SiteConsumptionStrategyModel`, `A17C1DeviceHomeLoadData`), [../models/power.md](../models/power.md) (`StationPowerLimitModel`) and [../models/](../models/README.md) for `GetSiteDeviceParamResponse`.

## MQTT abbreviated status fields

Status keys of the A17B1 system context (`soc`, `bp`, `pp`, `gp`, `lp`, `op`, `mps`, the `p2bp` family and so on) are owned by [../mqtt/a17b1.md](../mqtt/a17b1.md); the Solarbank 2 status tags by [../mqtt/a17c1_status.md](../mqtt/a17c1_status.md). The old key table was a copy and is removed here.

## Known firmware notes

- The device test of the SET commands ran on A17C1 FW 1.0.6.10 only. Whether other firmware or the other PNs accept the same opcodes is unknown. See [../mqtt/a17c1.md](../mqtt/a17c1.md).
- Acceptance of the 3.24.3 `cmd` for the power limit versus the upstream value, and which firmware accepts free 10 W values: [owner page](../api/power_service/site/set_site_device_param.md#known-unknowns).

## Known unknowns

Tag: untagged by design (no API fact).

- `005a` and `0085`: the app has no builder — checked 2026-10-20: the pool holds 119 opcode lists of the form `[0, x]` and none is `[0, 0x5a]` or `[0, 0x85]`, and the strings `"005a"`, `"005A"` and `"0085"` are not in the pool (grep of `pp.txt` and `const [0, 0x5a]` over the asm root: 0 hits); only upstream and mqtt_monitor know them (audit rows 24, 29, 32).
- `0080` field `a9` (`export_limit`) is not in `setDevicePowerLimit`: confirmed 2026-10-20, the builder (`a17c1_device_controller.dart setDevicePowerLimit @0x2276e48`) uses the raw tag keys 324, 326, 328, 330, 332, 334 and 336, which are `a2` to `a8`, and no key 338 (`a9`); the field names `a6` `disable_switch` and the `005e` `a2` mode range (1 to 8) are upstream's (audit rows 33).
- Meaning of the attribute keys `feeder0w`, `pv_power_limit_option` and `user_power_limit` named on the old page: not found in the upstream `api/api.py` lines checked; no owner yet.
- Which of the five PNs accept each opcode: only A17C1 is device-tested.
- Open test requests for these products: [../docs/DEVICE_TEST_BACKLOG.md](../docs/DEVICE_TEST_BACKLOG.md).

## Device-tested by

- A17C1, FW 1.0.6.10, mqtt_monitor: `0050`, `0067`, `005a`, `005e` (usage modes 1 and 3 only). Client version, tester name and date are not recorded in the old page (audit row 34).
- Power limit on A17C5: see [a17c5.md](a17c5.md) and the [owner page](../api/power_service/site/set_site_device_param.md#device-tested-by).
