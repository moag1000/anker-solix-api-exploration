# Power Service Device

> 21 function calls, 8 unique endpoints

## `/power_service/v1/app/device/get_device_attrs`

- **getDeviceAttrsInfo**(`*(no params extracted)*`) → `DeviceAttributes`
- **getDeviceAttrs**(`cmd, site_id, param_type=18, param_data`) → `DevicePowerLimit`
- **getTouElectricAttrs**(`site_id, device_pn`) → `TouDeviceAttrsModel`

## `/power_service/v1/app/device/get_device_home_load`

- **getDeviceHomeLoadPort**(`device_sn, attributes, currency`) → `StationModel`
- **getDeviceHomeLoadRes**(`device_sn, device_model`) → `SiteHomeLoadModel`
- **get17C1DeviceHomeLoadPort**(`device_sn, mode_type, custom_rate_plan, home_load_data`) → `A17C1DeviceHomeLoadData`

## `/power_service/v1/app/device/get_device_income`

- **getTOUChartStatistics**(`site_id, param_type=2`) → `TouBenifitsModel`

## `/power_service/v1/app/device/get_mes_device_info`

- **getDeviceLaserSn**(`device_sn, device_pn, device_type, upgrade_type, after_version, before_version, upgrade_time, site_id`)

## `/power_service/v1/app/device/get_relate_belong`

- **getDeviceBindInfo**(`device_sn`)

## `/power_service/v1/app/device/remove_param_config_key`

- **removeParamConfigKey**(`device_sn, device_pn, attributes`)

## `/power_service/v1/app/device/set_device_attrs`

- **setDevicePowerOptionsReq**(`device_sn, attributes, enable_0w_v2`)
- **setDeviceGameStatus**(`region`)
- **setTouElectricAttrs**(`device_sn, ble_mac, product_code, device_name, main_sw_version, sec_sw_version`)
- **getCurrencySetDeviceAttrs**(`*(no params extracted)*`)
- **setSolarName**(`*(no params extracted)*`)
- **setDeviceFeedGridSwitch**(`device_sn, attributes, pv_power_limit`)
- **setDevicePvPowerOptionsReq**(`device_sn, attributes, tag`)
- **setLocationTag**(`sn, img_url, hash_code`)
- **setPpsSolarName**(`site_id, param_type=26, cmd, param_data`)

## `/power_service/v1/app/device/set_device_home_load`

- **setDeviceHomeLoadRes**(`device_sn`)
- **set17C1DeviceHomeLoadRes**(`device_sn, bt_ble_mac, parent_device_sn, parent_device_pn`)

