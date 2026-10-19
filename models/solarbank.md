# Solarbank (A17C0-C5) — Response Models

> **Numbers under review (2026-10-19):** integers on this page that came from decompiled code were read without Smi decoding and may be 2× too large. Verified values: see docs/audit/models.md; corrected facts live on their owner pages (docs/STRUCTURE.md).

> 5 models

## A17C1DeviceHomeLoadData

Source: `model/site_home_load_model.dart`

```
advancedModeMinLoad, applianceLoads, appliance_loads, chargePriority,
charge_priority, current_home_load, default_charge_priority, default_home_load,
devicePowerLoads, device_power_loads, device_sn, display_advanced_mode,
display_priority_discharge_tips, endTime, end_time, home_load_data, id,
is_charge_priority, is_show_install_mode, is_show_priority_discharge,
is_zero_output_tips, last_select_mode, max_load, min_load, name, number,
parallel_display, parallel_home_load, power, powerSettingMode,
power_setting_mode, priorityDischargeSwitch, priority_discharge_switch,
priority_discharge_upgrade_devices, ranges, schedule_mode, site_id, startTime,
start_time, step, switch, turnOn, turn_on
```

## GetSiteDeviceParamResponse

Corrected 2026-10-19 (App 3.24.3): `GetSiteDeviceParamResponse`, `SiteDeviceParamData`, `SiteSocItem` and `FeedTimes` are owned by [`models/get_site_device_param_response.md`](get_site_device_param_response.md).

Source: `model/site_setting/get_site_device_param_model.dart`

*(no fields extracted)*

## SiteConsumptionStrategyModel

Source: `model/site_consumption_strategy_model.dart`

```
ai_ems, blend_plan, custom_rate_plan, data_auth, default_home_load, end_time,
exceed_alarm, index, max_load, min_load, mode_type, power, ranges,
reserved_soc, start_time, status, step, week
```

## SiteDeviceParamData

Corrected 2026-10-19 (App 3.24.3): owned by [`models/get_site_device_param_response.md`](get_site_device_param_response.md); this section is outdated.

Source: `model/site_setting/get_site_device_param_model.dart`

*(no fields extracted)*

## SiteHomeLoadModel

Source: `model/site_home_load_model.dart`

```
advancedModeMinLoad, applianceLoads, appliance_loads, chargePriority,
charge_priority, current_home_load, default_charge_priority, default_home_load,
devicePowerLoads, device_power_loads, device_sn, display_advanced_mode,
display_priority_discharge_tips, endTime, end_time, home_load_data, id,
is_charge_priority, is_show_install_mode, is_show_priority_discharge,
is_zero_output_tips, last_select_mode, max_load, min_load, name, number,
parallel_display, parallel_home_load, power, powerSettingMode,
power_setting_mode, priorityDischargeSwitch, priority_discharge_switch,
priority_discharge_upgrade_devices, ranges, schedule_mode, site_id, startTime,
start_time, step, switch, turnOn, turn_on
```

