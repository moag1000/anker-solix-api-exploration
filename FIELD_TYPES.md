# Field Types and Examples

> Cross-referenced from Blutter decompilation (B), thomluther's API examples (U),
> and MQTT field mappings (M). Types marked with `?` are inferred from naming
> conventions, not from actual data.

**234** fields with type information or cross-source confirmation.

| Field | Type | Example | Sources |
|-------|------|---------|--------|
| `ac_input_limit` | int | 1200 | U+M |
| `ac_input_power_unit` | string | "1200W" | U |
| `ac_power_limit` | int | 1200 | U |
| `accuracy` | int | 2 | U |
| `adjust_coef` | null | null | U |
| `advanced_mode_min_load` | int | 0 | U |
| `ae100_info` | null | null | U |
| `alias_name` | string | "E1600 0W Output Switch" | B+U |
| `all_power_limit` | int | 0 | U |
| `appliance_loads` | array | [ | B+U |
| `area` | string | "GER" | U |
| `area_info` | array | [ | U |
| `area_name` | string | "GER" | U |
| `battery_power` | string | "75" | B+U+M |
| `bind_site_status` | string | "1" | B+U |
| `blend_plan` | null | null | B+U |
| `brand_id` | string | "3a9930f5-74ef-4e41-a797-04e6b33d3f0f" | B+U |
| `bt_ble_id` | string | "" | U |
| `bt_ble_mac` | string | "FC1CEA253CDB" | U |
| `bubble` | int | 2 | U |
| `bws_surplus` | int | 0 | U |
| `callback_url` | string | "https://ankerpower-api-eu.anker.com/cloud/powerse | U |
| `category` | string | "Balcony Solar Power System" | B+U |
| `change_log` | string | "" | B+U |
| `charge` | bool | false | U |
| `charge_priority` | int | 0 | B+U |
| `charging_power` | string | "" | U |
| `charging_status` | string | "" | U+M |
| `child_upgrade_records` | null | null | B+U |
| `children` | array | [ | B+U |
| `co2` | string | "33.46" | U |
| `company` | string | "Nordpool" | U |
| `company_info` | array | [ | U |
| `content` | string | "Shelly\u662f\u4e00\u5bb6\u4e13\u6ce8\u4e8e\u667a\ | B+U |
| `countries` | string | "DE,AT,FR,IT" | U |
| `country` | string | "DE" | U |
| `country_info` | array | [ | U |
| `create_time` | int | 0 | B+U |
| `currency` | string | "\u20ac" | B+U |
| `currencyUnit` | string | "€" | U |
| `currency_list` | array | [ | U |
| `current_home_load` | string | "300W" | B+U |
| `current_mode` | int | 7 | U |
| `current_power` | int | 0 | U |
| `current_version` | string | "EZ1 2.0.5" | B+U |
| `custom_rate_plan` | array | [ | B+U |
| `default_charge_priority` | int | 0 | B+U |
| `default_home_load` | int | 200 | B+U |
| `device_img` | string | "https://public-aiot-fra-prod.s3.dualstack.eu-cent | B+U |
| `device_info` | array | [ | U |
| `device_list` | null | null | B+U |
| `device_msg` | bool | false | U |
| `device_name` | string | "Solarbank E1600" | B+U |
| `device_pn` | string | "" | B+U+M |
| `device_power_loads` | array | [ | B+U |
| `device_sn` | string | "9JVB42LJK8J0P5RY" | B+U+M |
| `device_sw_version` | string | "v1.4.4" | U |
| `device_type` | string | "A17C1_esp32" | B+U |
| `device_type_list` | array | [ | B+U |
| `display_advanced_mode` | int | 0 | B+U |
| `display_priority_discharge_tips` | int | 0 | B+U |
| `enable_0w` | int | 0 | U |
| `enable_0w_change` | bool | false | U |
| `end_month` | int | 3 | U |
| `end_time` | string | "06:30" | B+U |
| `energy` | float | 66.15 | B+U |
| `energyUnit` | string | "kWh" | B+U |
| `energy_key` | string | "energy_value" | U |
| `error_code` |  | — | B+M |
| `exceed_alarm` | bool | false | B+U |
| `file_md5` | string | "578ac26febb55ee55ffe9dc6819b6c4a" | B+U |
| `file_path` | string | "https://public-aiot-fra-prod.s3.dualstack.eu-cent | B+U |
| `file_size` | int | 1270256 | B+U |
| `force_upgrade` | bool | false | B+U |
| `from` | string | "00:00" | U |
| `generate_power` | string | "" | U |
| `has_manual` | bool | false | U |
| `has_unread_msg` | bool | false | U |
| `home_img` | string | "" | U |
| `home_load_data` | string | "{\"ranges\":[
        {\"id\":0,\"start_time\":\" | B+U |
| `home_name` | string | "Home" | U |
| `icon` | string | "" | B+U |
| `imgUrl` | string | "https://public-aiot-fra-prod.s3.dualstack.eu-cent | U |
| `img_url` | string | "https://public-aiot-fra-prod.s3.dualstack.eu-cent | B+U |
| `index` | int | 0 | B+U |
| `is_allow_delete` | bool | false | B+U |
| `is_charge_priority` | int | 0 | B+U |
| `is_forced` | bool | false | B+U |
| `is_ota_update` | bool | true | B+U |
| `is_passive` | string | "wifi_online" | U |
| `is_record` | bool | true | B+U |
| `is_same` | bool | false | U |
| `is_selected` | int | 1 | U |
| `is_show_install_mode` | int | 1 | B+U |
| `is_show_priority_discharge` | int | 0 | B+U |
| `is_zero_output_tips` | int | 1 | B+U |
| `last_version` | string | "v1.4.4" | B+U |
| `left_time` | int | 78451 | B+U |
| `legal_limit` | int | 800 | U |
| `legal_power_limit` | int | 800 | B+U |
| `limit` | int | 350 | U |
| `limit_real` | int | 350 | U |
| `link_time` | int | 1707127936 | U |
| `logo` | string | "https://public-aiot-fra-prod.s3.dualstack.eu-cent | B+U |
| `main_version` | string | "" | B+U |
| `manual_backup` | null | null | B+U |
| `max_load` | int | 800 | B+U+M |
| `md5` | string | "" | B+U |
| `min_load` | int | 100 | B+U+M |
| `mode` |  | — | B+M |
| `mode_type` | int | 3 | B+U |
| `model_img` | string | "https://public-aiot-ore-qa.s3.us-west-2.amazonaws | B+U |
| `ms_type` | int | 0 | B+U |
| `msg` | string | "success!" | U |
| `needUpdate` | bool | false | B+U |
| `need_retry` | bool | true | B+U |
| `need_update` | bool | false | U |
| `net_guideline` | string | "<div style=\"margin-bottom:12px;\"><font face=\"D | B+U |
| `net_img_url` | string | "https://public-aiot-fra-prod.s3.dualstack.eu-cent | B+U |
| `number` | int | 1 | B+U |
| `offline` | bool | false | B+U |
| `ota_complete_status` | int | 2 | B+U |
| `ota_status` | int | 1 | U |
| `output_cutoff_data` |  | — | B+M |
| `output_power` | string | "" | U+M |
| `p_code` | string | "A17C13Z1" | B+U |
| `p_codes` | array | [] | B+U |
| `parallel_display` | bool | false | B+U |
| `parallel_home_load` | string | "" | B+U |
| `parallel_type` | string | "Single" | U |
| `param_data` | string | "{\"ranges\":[
        {\"id\":0,\"start_time\":\" | U |
| `pct` | null | null | U |
| `photovoltaic_power` | string | "" | U+M |
| `power` | int | 169 | B+U+M |
| `powerConfig` | string | "800W" | U |
| `powerPopUpFlag` | int | 0 | U |
| `power_limit` | int | 800 | U |
| `power_limit_option` | null | null | B+U |
| `power_limit_option_real` | null | null | B+U |
| `power_setting_mode` | int | 1 | B+U |
| `power_site_type` | int | 0 | B+U |
| `power_unit` | string | "" | B+U |
| `powerpanel_list` | array | [] | B+U |
| `pps_list` | array | [] | B+U |
| `pps_status` | int | 0 | U |
| `pre_version` | string | "v1.4.4" | U |
| `preset_manual_backup_end` | int | 0 | U |
| `preset_manual_backup_start` | int | 0 | U |
| `price` | float | 0.4 | B+U |
| `price_type` | string | "dynamic" | U |
| `priority_discharge_switch` | int | 0 | B+U |
| `priority_discharge_upgrade_devices` | string | "" | B+U |
| `process_skip_type` | int | 1 | U |
| `product_code` | string | "A17Y0" | B+U |
| `product_component` | string | "" | U |
| `products` | array | [ | B+U |
| `productsInfo` | array | [ | U |
| `pvStatuses` | array | [ | B+U |
| `pv_power_limit` | int | 3600 | B+U |
| `ranges` | array | [ | B+U |
| `ranking` | string | "999+" | U |
| `reductionCo2` | int | 66 | U |
| `reductionCo2Unit` | string | "kg" | U |
| `relate_type` | array | [ | U |
| `release_time` | string | "13:00" | U |
| `retain_load` | string | "0W" | U |
| `retry_interval` | int | 2000 | B+U |
| `rom_version_name` | string | "v0.1.5.1" | B+U |
| `rssi` | string | "-74" | B+U |
| `saveMoney` | int | 0 | U |
| `saveMoneyUnit` | string | "\u20ac" | U |
| `schedule_mode` |  | — | B+M |
| `show` | bool | true | B+U |
| `site_co2` | int | 0 | U |
| `site_id` | string | "efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c" | B+U |
| `site_img` | string | "" | B+U |
| `site_list` | array | [ | U |
| `site_name` | string | "BKW" | B+U |
| `site_price_unit` | string | "\u20ac" | U |
| `size` | int | 0 | B+U |
| `soc` | int | 10 | B+U |
| `soc_list` | array | [ | U |
| `solar_brand` | string | "ANKER" | U |
| `solar_list` | array | [] | B+U |
| `solar_model` | string | "A5140" | B+U |
| `solar_model_name` | string | "MI60 Microinverter" | B+U |
| `solar_sn` | string | "" | B+U |
| `solarbank_list` | array | [ | B+U |
| `start_month` | int | 1 | B+U |
| `start_time` | string | "00:00" | B+U |
| `statistics` | array | [ | B+U |
| `step` | int | 0 | B+U |
| `sub_current_version` | string | "" | U |
| `switch` | bool | true | B+U |
| `switch_0w` | int | 0 | B+U |
| `symbol` | string | "$" | U |
| `system_msg` | bool | false | U |
| `tag` | string | "shelly" | B+U |
| `tag_code` | string | "ITG_AIN2" | U |
| `temperature` |  | — | B+M |
| `tieredElecPrices` | array | [ | U |
| `timestamp` | int | 1708277846 | B+U |
| `today_avg_price` | string | "87.04" | U |
| `today_price_trend` | array | [ | U |
| `tomorrow_avg_price` | string | "71.69" | U |
| `tomorrow_price_trend` | array | [ | U |
| `topology_type` | string | "1" | U |
| `total` | string | "" | B+U |
| `total_battery_power` | string | "0.00" | U |
| `total_charging_power` | string | "0.00" | U |
| `total_output_power` | string | "0.00" | U |
| `total_photovoltaic_power` | string | "0" | U |
| `tree` | string | "1.6" | U |
| `turn_on` | bool | true | B+U |
| `unit` | string | "\u20ac" | B+U |
| `update_infos` | array | [ | U |
| `updated_time` | string | "" | U |
| `upgrade_desc` | string | "" | B+U |
| `upgrade_record_list` | array | [ | B+U |
| `upgrade_time` | string | "2024-02-29 12:38:23" | B+U |
| `upgrade_type` | string | "1" | B+U |
| `upgrade_version` | string | "v1.5.6" | B+U |
| `url` | string | "" | B+U |
| `use_time` | null | null | B+U |
| `version_type` | int | 3 | U |
| `week` | array | [ | B+U |
| `weekday` | array | [ | U |
| `weekday_price` | array | [ | U |
| `weekend` | array | [ | U |
| `weekend_price` | array | [ | U |
| `wifi_name` | string | "" | B+U+M |
| `wifi_online` | bool | false | U |
| `wifi_signal` | string | "48" | B+U+M |
| `wireless_type` | string | "" | B+U |
