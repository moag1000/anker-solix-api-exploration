> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Flows

This directory holds step traces of user-visible actions (`<name>.md`), each a sequence of links to the endpoint, param_type, MQTT or BLE owner pages that carry the facts. Flow pages contain no payload copies. Their section order follows [../docs/templates/flow.md](../docs/templates/flow.md).

## Pages

Tag is the status-header tag of the page (the lowest tag among its facts, see [../METHODOLOGY.md](../METHODOLOGY.md#confidence-tags)).

| page | flow | tag | owners linked |
|---|---|---|---|
| [system_output_limit.md](system_output_limit.md) | system output limit (param_type 19) | asm-traced | [set_site_device_param](../api/power_service/site/set_site_device_param.md), [get_power_limit](../api/power_service/site/get_power_limit.md), [verify_unlock_default_power_code](../api/devicecontrol/device/verify_unlock_default_power_code.md) |
| [encrypted_request.md](encrypted_request.md) | encrypted request | asm-traced | [encryption](../api/encryption.md) |
| [modbus_setup.md](modbus_setup.md) | Modbus setup (third-party control) | asm-traced | [query_modbus_setting](../api/charging_hes_third_party_service_svc/query_modbus_setting.md), [set_modbus_setting](../api/charging_hes_third_party_service_svc/set_modbus_setting.md), [modbus](../devices/modbus.md) |
| [solarbank2_schedule.md](solarbank2_schedule.md) | Solarbank 2 schedule (param_type 6, opcode 005e) | asm-traced | [set_site_device_param](../api/power_service/site/set_site_device_param.md), [param_types](../api/param_types.md), [set_device_home_load](../api/power_service/app/device/set_device_home_load.md), [mqtt/a17c1](../mqtt/a17c1.md#005e-setbackpower-settacticstime-setpeakvalley) |
| [ev_charger_start_charging.md](ev_charger_start_charging.md) | EV charger start charging (A5190) | asm-traced | [iot_kit_channels](../reference/iot_kit_channels.md) |
| [ev_charger_setup_and_sessions.md](ev_charger_setup_and_sessions.md) | EV charger lifecycle: setup after binding, RFID cards, vehicles, charging orders, OCPP server (A5190 / A5191) | asm-traced | [get_device_cards](../api/power_service/rfid/get_device_cards.md), [get_vehicle_list](../api/power_service/app/vehicle/get_vehicle_list.md), [get_charging_order_list](../api/power_service/app/order/get_charging_order_list.md), [get_ocpp_info](../api/power_service/app/get_ocpp_info.md), [devices/ev_charger](../devices/ev_charger.md) |
| [anka_assistant.md](anka_assistant.md) | Anka AI assistant (entry button, chat page, settings) | asm-traced | [smart_service](../api/smart_service/README.md), [anka_agent_models](../models/anka_agent_models.md) |
| [smart_plug_countdown_timer.md](smart_plug_countdown_timer.md) | smart plug countdown timer (007e) | asm-traced | [mqtt/a17x8](../mqtt/a17x8.md#007e-setcountdowncmd), [ble/protocol](../ble/protocol.md#stacks-and-send-routing) |
| [smart_plug_schedule.md](smart_plug_schedule.md) | smart plug schedule (007c) | asm-traced | [mqtt/a17x8](../mqtt/a17x8.md#007c-settimingcmd), [ble/protocol](../ble/protocol.md#stacks-and-send-routing) |
| [solarbank_power_limit_change.md](solarbank_power_limit_change.md) | Solarbank power limit change (0080) | asm-traced | [set_device_attrs](../api/power_service/app/device/set_device_attrs.md), [mqtt/a17c1](../mqtt/a17c1.md#0080-setdevicepowerlimit) |
| [solarbank_soc_reserve_change.md](solarbank_soc_reserve_change.md) | Solarbank SOC reserve change (0067) | asm-traced | [set_power_cutoff](../api/power_service/app/compatible/set_power_cutoff.md), [get_power_cutoff](../api/power_service/app/compatible/get_power_cutoff.md), [soc_setting_param](../models/soc_setting_param.md), [mqtt/a17c1](../mqtt/a17c1.md#0067-setsoc) |
| [solarbank_toggle_grid_export.md](solarbank_toggle_grid_export.md) | Solarbank grid export (switch_0w) and off-grid switch | asm-traced | [set_device_attrs](../api/power_service/app/device/set_device_attrs.md), [get_device_attrs](../api/power_service/app/device/get_device_attrs.md), [mqtt/a17c1](../mqtt/a17c1.md#0073-setoffgridswitch) |
| [solarbank_temperature_unit.md](solarbank_temperature_unit.md) | Solarbank temperature unit (0050) | asm-traced | [mqtt/a17c1](../mqtt/a17c1.md#0050-settempunit) |
| [smart_plug_relay_toggle.md](smart_plug_relay_toggle.md) | smart plug relay toggle (007a) | asm-traced | [mqtt/a17x8](../mqtt/a17x8.md#007a-setrelayswitchcmd) |
| [pps_ac_output_toggle.md](pps_ac_output_toggle.md) | PPS AC output toggle (A1770) | asm-traced | [ble/a1770](../ble/a1770.md) |
| [a5101_work_mode_change.md](a5101_work_mode_change.md) | A5101 HES work mode change | asm-traced | [device_command](../api/charging_hes_svc/device_command.md), [ble/a5101](../ble/a5101.md) |
| [a5101_storm_guard.md](a5101_storm_guard.md) | A5101 HES storm guard (disaster preparedness) | asm-traced | [device_command](../api/charging_hes_svc/device_command.md), [get_current_disaster_prepare_details](../api/charging_hes_svc/get_current_disaster_prepare_details.md), [mqtt/a5101](../mqtt/a5101.md) |
| [site_price_configuration.md](site_price_configuration.md) | site price configuration (fixed price) | asm-traced | [update_site_price](../api/power_service/site/update_site_price.md), [set_device_attrs](../api/power_service/app/device/set_device_attrs.md), [device_command](../api/charging_hes_svc/device_command.md) |
| [a5101_battery_reserve.md](a5101_battery_reserve.md) | A5101 HES battery reserve | asm-traced | [device_command](../api/charging_hes_svc/device_command.md), [ble/a5101](../ble/a5101.md) |
| [diy_unlock.md](diy_unlock.md) | DIY legal power limit unlock | asm-traced | [verify_unlock_default_power_code](../api/devicecontrol/device/verify_unlock_default_power_code.md), [station_power_limit](../models/station_power_limit.md) |
| [installer_commissioning.md](installer_commissioning.md) | installer commissioning (initial setup) | asm-traced | [charging_hes_installer_svc](../api/charging_hes_installer_svc/README.md), [iot_kit_channels](../reference/iot_kit_channels.md) |
| [ota_monitor.md](ota_monitor.md) | OTA monitor (re-attach to a running update) | asm-traced | [iot_kit_channels](../reference/iot_kit_channels.md) |

## From the old FLOWS.md

The old `FLOWS.md` was a 3.18.0 reference with known Smi errors (see the Errata in [../CHANGELOG.md](../CHANGELOG.md)); it is deleted. Its 14 flows live on the pages below, as listed in the migration map of [../docs/STRUCTURE.md](../docs/STRUCTURE.md).

| old flow | page |
|---|---|
| 1 Solarbank 2 Schedule | [solarbank2_schedule.md](solarbank2_schedule.md) |
| 2 EV Charger Start Charging | [ev_charger_start_charging.md](ev_charger_start_charging.md) |
| 3 Smart Plug Countdown Timer | [smart_plug_countdown_timer.md](smart_plug_countdown_timer.md) |
| 4 Smart Plug Schedule | [smart_plug_schedule.md](smart_plug_schedule.md) |
| 5 Solarbank Power Limit Change | [solarbank_power_limit_change.md](solarbank_power_limit_change.md) |
| 6 Solarbank SOC Reserve Change | [solarbank_soc_reserve_change.md](solarbank_soc_reserve_change.md) |
| 7 Solarbank Toggle Grid Export | [solarbank_toggle_grid_export.md](solarbank_toggle_grid_export.md) |
| 8 Solarbank Temperature Unit | [solarbank_temperature_unit.md](solarbank_temperature_unit.md) |
| 9 Smart Plug Relay Toggle | [smart_plug_relay_toggle.md](smart_plug_relay_toggle.md) |
| 10 PPS AC Output Toggle | [pps_ac_output_toggle.md](pps_ac_output_toggle.md) |
| 11 A5101 HES Work Mode Change | [a5101_work_mode_change.md](a5101_work_mode_change.md) |
| 12 A5101 HES Storm Guard | [a5101_storm_guard.md](a5101_storm_guard.md) |
| 13 Site Price Configuration | [site_price_configuration.md](site_price_configuration.md) |
| 14 A5101 Battery Reserve | [a5101_battery_reserve.md](a5101_battery_reserve.md) |

## Audit row numbers

Flow pages cite the verdict rows of [../docs/audit/FLOWS.md](../docs/audit/FLOWS.md) as "audit row N". N counts the data rows of that table from the top: row 1 is the `"cmd": 246` row for the param_type 6 schedule, row 71 the last summary row (file line N + 14). The 71 rows are 26 OK, 24 WRONG, 8 CHANGED-IN-3.24.3, 7 NOT-FROM-ASM and 6 UNVERIFIABLE.

Not here: payload, field or opcode definitions; those live with their owners, see [../docs/STRUCTURE.md](../docs/STRUCTURE.md).
