# Dart → JSON → Python Field Name Mapping

> **3.18.0 reference, superseded (2026-10-19).** Owner pages on 3.24.3: [data/models.json](data/models.json), [models/README.md](models/README.md), [GLOSSARY.md](GLOSSARY.md). This file is deleted in Task 4.9; its audit table is docs/audit/field_docs.md.

> Maps the Dart camelCase property names (from Blutter decompilation) to their
> snake_case JSON equivalents. Where thomluther's library uses a different name,
> the Python name is shown in the third column.

**35** cross-referenced camelCase↔snake_case pairs found in the same source files.

| Dart (camelCase) | JSON (snake_case) | In thomluther's mqttmap? |
|-----------------|-------------------|-------------------------|
| `applianceLoads` | `appliance_loads` | — |
| `chargePriority` | `charge_priority` | — |
| `countryCode` | `country_code` | — |
| `deviceId` | `device_id` | — |
| `deviceName` | `device_name` | — |
| `devicePn` | `device_pn` | YES |
| `devicePowerLoads` | `device_power_loads` | — |
| `deviceSn` | `device_sn` | YES |
| `endTime` | `end_time` | — |
| `greenMode` | `green_mode` | — |
| `httpUserAgent` | `http_user_agent` | — |
| `localTime` | `local_time` | — |
| `phoneBrand` | `phone_brand` | — |
| `phoneModel` | `phone_model` | — |
| `phoneName` | `phone_name` | — |
| `powerSettingMode` | `power_setting_mode` | — |
| `ppsList` | `pps_list` | — |
| `priceUnit` | `price_unit` | — |
| `priorityDischargeSwitch` | `priority_discharge_switch` | — |
| `productCode` | `product_code` | — |
| `siteId` | `site_id` | — |
| `siteName` | `site_name` | — |
| `solarList` | `solar_list` | — |
| `solarModel` | `solar_model` | — |
| `startTime` | `start_time` | — |
| `stationId` | `station_id` | — |
| `sysType` | `sys_type` | — |
| `sysVersion` | `sys_version` | — |
| `turnOn` | `turn_on` | — |
| `userId` | `user_id` | — |
| `wifiBSSID` | `wifi_bssid` | — |
| `wifiName` | `wifi_name` | YES |
| `wifiPwd` | `wifi_pwd` | — |
| `wifiSSID` | `wifi_ssid` | — |
| `xAppKey` | `x_app_key` | — |
