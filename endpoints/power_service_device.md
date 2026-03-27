# Power Service Device

> 21 function calls, 8 unique endpoints
>
> **Source**: Regenerated from ENDPOINT_FIELDS.md (authoritative reference)

## `/power_service/v1/app/device/get_device_attrs`

- **getDeviceAttrsInfo**(`*(none extracted)*`) → `DeviceAttributes`
- **getDeviceAttrs**(`device_sn?, attributes, enable_0w_v2?`) → `DevicePowerLimit`
- **getTouElectricAttrs**(`device_sn?, attributes`) → `TouDeviceAttrsModel`

## `/power_service/v1/app/device/get_device_home_load`

- **getDeviceHomeLoadPort**(`device_sn?`) → `StationModel`
- **getDeviceHomeLoadRes**(`device_sn?`) → `SiteHomeLoadModel`
- **get17C1DeviceHomeLoadPort**(`device_sn?, param_type, device_pn`) → `A17C1DeviceHomeLoadData`

## `/power_service/v1/app/device/get_device_income`

- **getTOUChartStatistics**(`device_sn?, type, start_time`) → `TouBenifitsModel`

## `/power_service/v1/app/device/get_mes_device_info`

- **getDeviceLaserSn**(`device_sn?`)

## `/power_service/v1/app/device/get_relate_belong`

- **getDeviceBindInfo**(`device_sn?`)

## `/power_service/v1/app/device/remove_param_config_key`

- **removeParamConfigKey**(`site_id?, device_sn, remove_key, use_time`)

## `/power_service/v1/app/device/set_device_attrs`

> **Nesting confirmed**: All additional fields go **inside** `attributes` dict.
> Upstream: `{"device_sn": "...", "attributes": {"pv_power_limit": 800, "switch_0w": 0}}`

- **setDevicePowerOptionsReq**(`device_sn?, attributes{power_limit?, ac_power_limit?, pv_power_limit?}`)
- **setDeviceGameStatus**(`device_sn?, attributes{init_status}`)
- **setTouElectricAttrs**(`device_sn?, attributes{pps_use_time}`)
- **getCurrencySetDeviceAttrs**(`device_sn?, attributes{currency}`)
- **setSolarName**(`device_sn?, device_pn, attributes`)
- **setDeviceFeedGridSwitch**(`device_sn?, attributes{switch_0w}`)
- **setDevicePvPowerOptionsReq**(`device_sn?, attributes{pv_power_limit}`)
- **setLocationTag**(`device_sn?, attributes{tag}`)
- **setPpsSolarName**(`device_sn?, device_pn, attributes`)

## `/power_service/v1/app/device/set_device_home_load`

- **setDeviceHomeLoadRes**(`site_id?, device_sn, home_load_data`)
- **set17C1DeviceHomeLoadRes**(`device_sn?, mode_type, custom_rate_plan?, home_load_data?`)
