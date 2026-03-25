# Mini Power

> 28 function calls, 27 unique endpoints

## `/mini_power/v1/app/charging/add_charging_mode`

- **addCustomChargeMode**(`device_sn, protocol_status`)

## `/mini_power/v1/app/charging/delete_charging_mode`

- **deleteCustomChargeMode**(`sn`)

## `/mini_power/v1/app/charging/get_charging_mode_list`

- **getCustomChargeModeList**(`device_sn`) → `A2345CustomModeList`

## `/mini_power/v1/app/charging/update_charging_mode`

- **updateCustomChargeMode**(`device_sn, name, number, total_power, max_total_power, auto_exit, has_charge_protocol, power_settings`)

## `/mini_power/v1/app/egg/get_easter_egg_trigger_list`

- **getEasterEggRecord**(`ssid, sn, rssi, encryption`) → `EasterEggTiggerRecordModel`

## `/mini_power/v1/app/egg/report_easter_egg_trigger_status`

- **addEasterEggStatusRecord**(`device_sn, port_name, remark`)

## `/mini_power/v1/app/power/get_day_power_data`

- **getDayPowerData**(`*(no params extracted)*`) → `DayPowerModel`

## `/mini_power/v1/app/setting/get_charging_device_identity_new_status`

- **getA2687StandardChargingDeviceModelIdentityStatus**(`charging_device_identity_new_status, device_sn`)

## `/mini_power/v1/app/setting/get_charging_device_identity_status_default_true`

- **getA2345DeviceIdentityStatus**(`status`)

## `/mini_power/v1/app/setting/get_device_setting`

- **getCustomChargeModeSetting**(`charging_mode_status, compatibility_status, charging_device_identity_status`)

## `/mini_power/v1/app/setting/get_port_remarks`

- **getPortRemarks**(`device_sn`)

## `/mini_power/v1/app/setting/get_power_range_support_protocols`

- **getPowerSupportProtocols**(`device_sn`) → `PowerRangeProtocolsResponse`

## `/mini_power/v1/app/setting/get_protocol_status`

- **getA2687ProtocolAgreementStatus**(`id`) → `A2687ProtocolAgreementModel`

## `/mini_power/v1/app/setting/set_charging_device_identity_new_status`

- **setA2687StandardChargingDeviceModelIdentityStatus**(`*(no params extracted)*`)

## `/mini_power/v1/app/setting/set_charging_device_identity_status`

- **setA2687ChargingDeviceModelIdentityStatus**(`device_sn, charging_device_identity_new_status`)

## `/mini_power/v1/app/setting/set_charging_device_identity_status_default_true`

- **setA2345DeviceIdentityStatus**(`device_sn, compatibility_status`)

## `/mini_power/v1/app/setting/set_charging_mode_status`

- **saveCustomChargeModeSetting**(`heat_pump_plan`)

## `/mini_power/v1/app/setting/set_compatibility_status`

- **saveCompatibilityStatusSetting**(`device_sn, charging_mode_status`)

## `/mini_power/v1/app/setting/set_mode_sub_status`

- **setA2687ModeSubStatus**(`id, name, total_power, max_total_power, auto_exit, has_charge_protocol, power_settings`)

## `/mini_power/v1/app/setting/set_port_remark`

- **setPortRemark**(`device_sn, charging_device_identity_status_default_true`)

## `/mini_power/v1/app/setting/set_protocol_status`

- **setA2687ProtocolAgreementStatus**(`device_sn, charging_device_identity_status`)

## `/mini_power/v1/app/style/add_manual_clock_screensavers`

- **addA2345CustomClockScreenSavers**(`id`)

## `/mini_power/v1/app/style/delete_manual_clock_screensavers`

- **deleteA2345CustomClockScreenSavers**(`sn, screensaver_id, name`)

## `/mini_power/v1/app/style/get_clock_screensavers`

- **getScreenSaversByCategory**(`device_model`)
- **getA2345ClockScreenSavers**(`*(no params extracted)*`)

## `/mini_power/v1/app/style/get_manual_clock_screensavers`

- **getA2345CustomClockScreenSavers**(`short_url`)

## `/mini_power/v1/app/style/get_url`

- **getA2345CustomClockScreenSaversRealUrl**(`device_sn`)

## `/mini_power/v1/app/style/set_manual_clock_screensaver_name`

- **editA2345CustomClockScreenSaversName**(`device_sn, egg_type, report_time`)

