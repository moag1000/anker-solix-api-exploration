# Mini Power

> 28 function calls, 27 unique endpoints
>
> **Source**: Regenerated from ENDPOINT_FIELDS.md (authoritative reference)
>
> **HA relevance**: Charging mode and power data endpoints are relevant.
> Screen saver/clock customization and easter egg endpoints are **not relevant**
> for HA integration (cosmetic app features).

## `/mini_power/v1/app/charging/add_charging_mode`

- **addCustomChargeMode**(`device_sn?, name, number, total_power, max_total_power, auto_exit, has_charge_protocol, power_settings?`)

## `/mini_power/v1/app/charging/delete_charging_mode`

- **deleteCustomChargeMode**(`id?`)

## `/mini_power/v1/app/charging/get_charging_mode_list`

- **getCustomChargeModeList**(`device_sn?`) → `A2345CustomModeList`

## `/mini_power/v1/app/charging/update_charging_mode`

- **updateCustomChargeMode**(`id?, name, total_power, max_total_power, auto_exit, has_charge_protocol, power_settings?`)

## `/mini_power/v1/app/egg/get_easter_egg_trigger_list`

- **getEasterEggRecord**(`device_sn?`) → `EasterEggTiggerRecordModel`

## `/mini_power/v1/app/egg/report_easter_egg_trigger_status`

- **addEasterEggStatusRecord**(`device_sn?, egg_type, report_time?`)

## `/mini_power/v1/app/power/get_day_power_data`

- **getDayPowerData**(`device_model?, device_sn, date`) → `DayPowerModel`

## `/mini_power/v1/app/setting/get_charging_device_identity_new_status`

- **getA2687StandardChargingDeviceModelIdentityStatus**(`device_sn?, charging_device_identity_new_status?`)

## `/mini_power/v1/app/setting/get_charging_device_identity_status_default_true`

- **getA2345DeviceIdentityStatus**(`device_sn?, status?`)

## `/mini_power/v1/app/setting/get_device_setting`

- **getCustomChargeModeSetting**(`device_sn?, charging_mode_status?, compatibility_status, charging_device_identity_status`)

## `/mini_power/v1/app/setting/get_port_remarks`

- **getPortRemarks**(`device_sn?`)

## `/mini_power/v1/app/setting/get_power_range_support_protocols`

- **getPowerSupportProtocols**(`device_model?`) → `PowerRangeProtocolsResponse`

## `/mini_power/v1/app/setting/get_protocol_status`

- **getA2687ProtocolAgreementStatus**(`device_sn?`) → `A2687ProtocolAgreementModel`

## `/mini_power/v1/app/setting/set_charging_device_identity_new_status`

- **setA2687StandardChargingDeviceModelIdentityStatus**(`device_sn?, charging_device_identity_new_status`)

## `/mini_power/v1/app/setting/set_charging_device_identity_status`

- **setA2687ChargingDeviceModelIdentityStatus**(`device_sn?, charging_device_identity_status`)

## `/mini_power/v1/app/setting/set_charging_device_identity_status_default_true`

- **setA2345DeviceIdentityStatus**(`device_sn?, charging_device_identity_status_default_true`)

## `/mini_power/v1/app/setting/set_charging_mode_status`

- **saveCustomChargeModeSetting**(`device_sn?, charging_mode_status`)

## `/mini_power/v1/app/setting/set_compatibility_status`

- **saveCompatibilityStatusSetting**(`device_sn?, compatibility_status`)

## `/mini_power/v1/app/setting/set_mode_sub_status`

- **setA2687ModeSubStatus**(`device_sn?, mode, protocol_key, status`)

## `/mini_power/v1/app/setting/set_port_remark`

- **setPortRemark**(`device_sn?, port_name, remark`)

## `/mini_power/v1/app/setting/set_protocol_status`

- **setA2687ProtocolAgreementStatus**(`device_sn?, protocol_status`)

## `/mini_power/v1/app/style/add_manual_clock_screensavers`

- **addA2345CustomClockScreenSavers**(`sn?, img_url, hash_code`)

## `/mini_power/v1/app/style/delete_manual_clock_screensavers`

- **deleteA2345CustomClockScreenSavers**(`id?`)

## `/mini_power/v1/app/style/get_clock_screensavers`

- **getScreenSaversByCategory**(`product_code?`)
- **getA2345ClockScreenSavers**(`product_code?`)

## `/mini_power/v1/app/style/get_manual_clock_screensavers`

- **getA2345CustomClockScreenSavers**(`sn?`)

## `/mini_power/v1/app/style/get_url`

- **getA2345CustomClockScreenSaversRealUrl**(`short_url?`)

## `/mini_power/v1/app/style/set_manual_clock_screensaver_name`

- **editA2345CustomClockScreenSaversName**(`sn?, screensaver_id, name?`)
