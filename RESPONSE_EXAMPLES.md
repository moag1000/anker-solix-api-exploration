# Response Examples from thomluther's API

> These are **real API response examples** documented in thomluther's code.
> They show the actual JSON structure returned by the Anker API.
> Extracted from api.py, schedule.py, apibase.py (71 examples).

## `check_upgrade_record`

```json
{"is_record": true,"device_list": [{ "device_sn": "9JVB42LJK8J0P5RY","device_name": "","icon": "","last_version": "v1.4.4","device_pn": ""}
```
Source: `api.py`

## `device_pv_energy_daily`

```json
{"2023-09-29": {"date": "2023-09-29", "solar_production": "1.21"}
```
Source: `energy.py`

```json
{"date": "2023-09-30", "solar_production": "3.07"}
```
Source: `energy.py`

## `energy_daily`

```json
{"2023-09-29": {"date": "2023-09-29", "solar_production": "1.21", "battery_discharge": "0.47", "battery_charge": "0.56"}
```
Source: `energy.py`

```json
{"date": "2023-09-30", "solar_production": "3.07", "battery_discharge": "1.06", "battery_charge": "1.39"}
```
Source: `energy.py`

## `get_ai_ems_runtime`

```json
{"status": 0,"result": "fail","left_time": 78451}
```
Source: `api.py`

## `get_co2_ranking`

```json
{"show": true,"ranking": "999+","co2": "33.46","tree": "1.6","content": "Not to be underestimated","level": { "tree": 2,"bubble": 2}
```
Source: `apibase.py`

## `get_compatible_info`

```json
{"ota_complete_status": 2,"process_skip_type": 1,"solar_info": { "solar_sn": "","solar_brand": "ANKER","solar_model": "A5140","brand_id": "3a9930f5-74ef-4e41-a797-04e6b33d3f0f", "model_img": "https://...
```
Source: `api.py`

## `get_currency_list`

```json
{"currency_list": [ {"symbol": "$","name": "AUD, CAD, USD"}
```
Source: `apibase.py`

```json
{"symbol": "\u20ac","name": "EUR"}
```
Source: `apibase.py`

## `get_device_attributes`

```json
{"device_sn": "9JVB42LJK8J0P5RY","attributes": {"pv_power_limit": 3600, "ac_power_limit": 1200, "rssi": "-74"}
```
Source: `api.py`

## `get_device_charge_order_stats`

```json
{"total_stats": {"charge_unit": "kWh","charge_total": 146.354,"charge_time": 325555,"charge_count": 7,"cost": 12.05,"cost_unit": "\u00a3", "cost_saving": 23.32,"co2_saving": 54.187,"co2_saveing_unit":...
```
Source: `energy.py`

```json
{"date_number": 1,"date_range": {"start_date": "2026-02-01","end_date": "2026-02-01"}
```
Source: `energy.py`

## `get_device_fittings`

```json
{"data": [{ "device_sn": "ZDL32D6A3HKXUTN1","product_code": "A17Y0","device_name": "E1600 0W Output Switch","alias_name": "E1600 0W Output Switch", "img_url": "https://public-aiot-fra-prod.s3.dualstac...
```
Source: `api.py`

## `get_device_load`

```json
{"site_id": "efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c", "home_load_data": "{\"ranges\":[ {\"id\":0,\"start_time\":\"00:00\",\"end_time\":\"08:30\",\"turn_on\":true,\"appliance_loads\":[{\"id\":0,\"name\":...
```
Source: `schedule.py`

## `get_device_parm`

```json
{"param_data": "{\"ranges\":[ {\"id\":0,\"start_time\":\"00:00\",\"end_time\":\"08:30\",\"turn_on\":true,\"appliance_loads\":[{\"id\":0,\"name\":\"Benutzerdefiniert\",\"power\":300,\"number\":1}
```
Source: `schedule.py`

```json
{"param_data":"{\"mode_type\":3,\"custom_rate_plan\":[ {\"index\":0,\"week\":[0,6],\"ranges\":[ {\"start_time\":\"00:00\",\"end_time\":\"24:00\",\"power\":110}
```
Source: `schedule.py`

## `get_device_pv_price`

```json
{"currencyUnit": "€","tieredElecPrices": [ {"from": "00:00","to": "23:59","price": 0.4}
```
Source: `api.py`

## `get_device_pv_status`

```json
{"pvStatuses": [{"sn": "JJY4QAVAFKT9","power": 169,"status": 1}
```
Source: `api.py`

## `get_device_pv_total_statistics`

```json
{"energy": 66.15, "energyUnit": "kWh", "reductionCo2": 66, "reductionCo2Unit": "kg", "saveMoney": 0, "saveMoneyUnit": "\u20ac", "powerConfig": "800W", "powerPopUpFlag": 0}
```
Source: `api.py`

## `get_dynamic_prices`

```json
{"release_time":"13:00","today_price_trend":[ {"time":"00:00","price":"81.76"}
```
Source: `apibase.py`

```json
{"time":"01:00","price":"75.31"}
```
Source: `apibase.py`

## `get_hes_platforms_list`

```json
{"productsInfo": [ {"category": "Balcony Solar Power System","code": "A5140","name": "MI60 Microinverter", "imgUrl": "https://public-aiot-fra-prod.s3.dualstack.eu-central-1.amazonaws.com/anker-power/p...
```
Source: `apibase.py`

```json
{"category": "Balcony Solar Power System","code": "A17C1","name": "Solarbank 2 E1600 Pro", "imgUrl": "https://public-aiot-fra-prod.s3.dualstack.eu-central-1.amazonaws.com/anker-power/public/product/20...
```
Source: `apibase.py`

## `get_homepage`

```json
{"site_list":[{"site_id":"efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c","site_name":"BKW","site_img":"","device_type_list":[3],"ms_type":0,"power_site_type":0,"is_allow_delete":false}
```
Source: `api.py`

```json
{"device_pn":"","device_sn":"9JVB42LJK8J0P5RY","device_name":"Solarbank E1600", "device_img":"https://public-aiot-fra-prod.s3.dualstack.eu-central-1.amazonaws.com/anker-power/public/product/anker-powe...
```
Source: `api.py`

## `get_message_unread`

```json
{"has_unread_msg": false,"system_msg": false,"device_msg": false}
```
Source: `apibase.py`

## `get_ota_batch`

```json
{"update_infos": [{"device_sn": "9JVB42LJK8J0P5RY","need_update": false,"upgrade_type": 0,"lastPackage": { "product_code": "","product_component": "","version": "","is_forced": false,"md5": "","url": ...
```
Source: `apibase.py`

```json
{"needUpdate": false,"device_type": "A17C1_esp32","rom_version_name": "v0.1.5.1","force_upgrade": false,"full_package": { "file_path": "https://public-aiot-fra-prod.s3.dualstack.eu-central-1.amazonaws...
```
Source: `apibase.py`

## `get_ota_info`

```json
{"ota_status": 3,"current_version": "EZ1 2.0.5","timestamp": 1708277846,"version_type": 3}
```
Source: `api.py`

## `get_ota_update`

```json
{"is_ota_update": true,"need_retry": true,"retry_interval": 2000,"device_list": null}
```
Source: `api.py`

## `get_power_limit`

```json
{"device_pn": "A17C5","device_sn": "9JVB42LJK8J0P5RY","device_name": "Solarbank 3", "device_img": "https://public-aiot-fra-prod.s3.dualstack.eu-central-1.amazonaws.com/anker-power/public/product/2025/...
```
Source: `api.py`

```json
{"limit": 350,"limit_real": 350}
```
Source: `api.py`

## `get_price_providers`

```json
{"country_info": [ {"country": "DE","company_info": [ {"company": "Nordpool","area_info": [ {"area": "GER","area_name": "GER"}
```
Source: `apibase.py`

## `get_product_platforms_list`

```json
{"p_code": "A17C13Z1","img_url": "https://public-aiot-fra-prod.s3.dualstack.eu-central-1.amazonaws.com/anker-power/public/banner/2024/05/24/iot-admin/SC9Wa8mzqhkLFMjt/picl_A17C1_normal.png"}
```
Source: `apibase.py`

```json
{"p_code": "A17C1IZ1","img_url": "https://public-aiot-fra-prod.s3.dualstack.eu-central-1.amazonaws.com/anker-power/public/banner/2024/05/24/iot-admin/SC9Wa8mzqhkLFMjt/picl_A17C1_normal.png"}
```
Source: `apibase.py`

## `get_scene_info`

```json
{"home_info":{"home_name":"Home","home_img":"","charging_power":"0.00","power_unit":"W"}
```
Source: `apibase.py`

```json
{"pps_list":[],"total_charging_power":"0.00","power_unit":"W","total_battery_power":"0.00","updated_time":"","pps_status":0}
```
Source: `apibase.py`

## `get_site_price`

```json
{"site_id": "efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c","price": 0.4,"site_co2": 0,"site_price_unit": "\u20ac"}
```
Source: `apibase.py`

```json
{"site_id": "efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c","price": 0.29,"site_co2": 0,"site_price_unit": "\u20ac", "price_type": "dynamic", "current_mode": 7, "use_time": null, "dynamic_price": { "country": ...
```
Source: `apibase.py`

## `get_solar_info`

```json
{"brand_id": "3a9930f5-74ef-4e41-a797-04e6b33d3f0f","solar_brand": "ANKER","solar_model": "A5140","solar_sn": "","solar_model_name": "MI60 Microinverter"}
```
Source: `api.py`

## `get_third_platforms_list`

```json
{"name": "3EM","img_url": "https://public-aiot-fra-prod.s3.dualstack.eu-central-1.amazonaws.com/anker-power/public/banner/2024/08/29/iot-admin/5lyJ9NmYG5pD7NIA/3em.png", "index": 0,"product_code": "SH...
```
Source: `apibase.py`

```json
{"name": "Pro 3EM","img_url": "https://public-aiot-fra-prod.s3.dualstack.eu-central-1.amazonaws.com/anker-power/public/banner/2024/09/02/iot-admin/I8dV8ONUfEm4iXSc/3em%20pro.png", "index": 0,"product_...
```
Source: `apibase.py`

## `get_upgrade_record`

```json
{"device_sn": "9JVB42LJK8J0P5RY", "site_id": "", "upgrade_record_list": [ {"upgrade_time": "2024-02-29 12:38:23","upgrade_version": "v1.5.6","pre_version": "v1.4.4","upgrade_type": "1","upgrade_desc":...
```
Source: `api.py`

```json
{"upgrade_time": "2023-12-29 10:23:06","upgrade_version": "v1.4.4","pre_version": "v0.0.6.6","upgrade_type": "1","upgrade_desc": "", "device_sn": "9JVB42LJK8J0P5RY","device_name": "9JVB42LJK8J0P5RY","...
```
Source: `api.py`

## `get_wifi_list`

```json
{"wifi_name": "wifi-network-1","wifi_signal": "48","device_sn": "7SKIVRGPK8XC2ROB","rssi": "","offline": false}
```
Source: `apibase.py`

## `param_type_13`

```json
{"param_data":"{\"step\":5,\"ai_ems\":null,\"max_load\":1200,\"min_load\":null,\"data_auth\":true,\"mode_type\":null, \"blend_plan\":null,\"custom_rate_plan\":null,\"default_home_load\":null}
```
Source: `schedule.py`

## `param_type_16`

```json
{"param_data":"{\"AE100\":\"7X297LBE75Z0BU4LE\", \"id_img\":\"https://public-aiot-fra-prod.s3.dualstack.eu-central-1.amazonaws.com/anker-power/public/product/2025/06/24/iot-admin/6eBAql2OBqMlGG1W/2025...
```
Source: `schedule.py`

## `param_type_18`

```json
{"param_data": {"soc_list": [{"id": 1,"is_selected": 1,"soc": 10}
```
Source: `schedule.py`

## `param_type_23`

```json
{"param_data": "{\"switch\": 0}
```
Source: `schedule.py`

## `param_type_26`

```json
{"param_data": "{\"third_part_pv_setting\": 1, \"show_third_party_pv_panel\": 1}
```
Source: `schedule.py`

## `param_type_4`

```json
{"param_data": "{\"ranges\":[ {\"id\":0,\"start_time\":\"00:00\",\"end_time\":\"08:30\",\"turn_on\":true,\"appliance_loads\":[{\"id\":0,\"name\":\"Benutzerdefiniert\",\"power\":300,\"number\":1}
```
Source: `schedule.py`

## `param_type_6`

```json
{"param_data":"{\"mode_type\":3,\"custom_rate_plan\":[ {\"index\":0,\"week\":[0,6],\"ranges\":[ {\"start_time\":\"00:00\",\"end_time\":\"24:00\",\"power\":110}
```
Source: `schedule.py`

```json
{"index": 0,"week": [0,6],"ranges": [ {"start_time": "00:00","end_time": "24:00","power": 110}
```
Source: `schedule.py`

```json
{rate_plan_name: new_rate_plan}
```
Source: `schedule.py`

## `param_type_9`

```json
{"param_data":"{\"price_type\":\"dynamic\", \"use_time\":[{\"sea\":{\"start_month\":1,\"end_month\":12}
```
Source: `schedule.py`

## `set_device_attributes`

```json
{"pv_power_limit": 3600, "ac_power_limit": 1200, "power_limit": 800}
```
Source: `api.py`

## `set_device_load`

```json
{"ranges":[' '{"id":0,"start_time":"00:00","end_time":"06:30","turn_on":true,"appliance_loads":[{"id":0,"name":"Benutzerdefiniert","power":300,"number":1}
```
Source: `schedule.py`

```json
{"device_sn":"9JVB42LJK8J0P5RY","power":150}
```
Source: `schedule.py`

## `set_device_parm`

```json
{"param_data": '{"ranges":[' '{"id":0,"start_time":"00:00","end_time":"08:30","turn_on":true,"appliance_loads":[{"id":0,"name":"Benutzerdefiniert","power":300,"number":1}
```
Source: `schedule.py`

```json
{"id":0,"start_time":"08:30","end_time":"17:00","turn_on":false,"appliance_loads":[{"id":0,"name":"Benutzerdefiniert","power":100,"number":1}
```
Source: `schedule.py`

## `set_device_pv_power`

```json
{"sn": "E071000XXXXX","power": 800}
```
Source: `api.py`

## `set_device_pv_price`

```json
{"sn": "E071000XXXXX","currencyUnit": "€","tieredElecPrices": [ {"from": "00:00","to": "23:59","price": 0.40}
```
Source: `api.py`

## `set_home_load`

```json
{"ranges":[ {"id":0,"start_time":"00:00","end_time":"08:30","turn_on":true,"appliance_loads":[{"id":0,"name":"Benutzerdefiniert","power":300,"number":1}
```
Source: `schedule.py`

```json
{"id":0,"start_time":"08:30","end_time":"17:00","turn_on":false,"appliance_loads":[{"id":0,"name":"Benutzerdefiniert","power":100,"number":1}
```
Source: `schedule.py`

## `set_sb2_home_load`

```json
{"index": 0,"week": [0,6],"ranges": [ {"start_time": "00:00","end_time": "24:00","power": 110}
```
Source: `schedule.py`

```json
{"index": 1,"week": [1,2,3,4,5],"ranges": [ {"start_time": "00:00","end_time": "08:00","power": 100}
```
Source: `schedule.py`

## `set_sb2_use_time`

```json
{"mode_type":3, "custom_rate_plan":[{"index":0,"week":[0,1,2,3,4,5,6],"ranges":[{"start_time":"00:00","end_time":"24:00","power":0}
```
Source: `schedule.py`

```json
{"sea":{"start_month":1,"end_month":3}
```
Source: `schedule.py`

## `set_site_price`

```json
{"site_id": 'efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c', "price": 0.325, "site_price_unit": "\u20ac", "site_co2": 0, "accuracy": 5}
```
Source: `apibase.py`

```json
{"site_id": 'efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c', "price": 0.325, "site_price_unit": "\u20ac", "site_co2": 0, "price_type": "dynamic", "dynamic_price": { "country": "DE", "company": "Nordpool", "are...
```
Source: `apibase.py`

