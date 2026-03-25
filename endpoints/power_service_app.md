# Power Service App

> 17 function calls, 17 unique endpoints

## `/power_service/v1/app/after_sale/check_popup`

- **checkDevicePopUpApi**(`devices`)

## `/power_service/v1/app/after_sale/get_popup`

- **queryA17Y0Popup**(`site_id`)

## `/power_service/v1/app/check_upgrade_record`

- **checkUpgradeRecord**(`device_sn, attributes`) → `CheckUpgradeRecordModel`

## `/power_service/v1/app/get_annual_report`

- **getAnnualReport**(`*(no params extracted)*`) → `Post2024Model`

## `/power_service/v1/app/get_auto_upgrade`

- **getAutoUpgrade**(`*(no params extracted)*`) → `DeviceAutoUpGradDisposition`

## `/power_service/v1/app/get_phonecode_list`

- **sharePhoneCode**(`*(no params extracted)*`)

## `/power_service/v1/app/get_relate_and_bind_devices`

- **getDevicesList**(`device_model, confirm_type`) → `DeviceModel`

## `/power_service/v1/app/get_relate_device_fittings`

- **getRelateAccessory**(`*(no params extracted)*`) → `DeviceModel`

## `/power_service/v1/app/get_token_by_userid`

- **getAccessTokenByUserID**(`*(no params extracted)*`)

## `/power_service/v1/app/get_upgrade_record`

- **getUpgradeRecord**(`email`) → `UpgradeRecordModel`

## `/power_service/v1/app/get_user_op_shelly_status`

- **checkIsGrantedDeviceChanged**(`user_id`)

## `/power_service/v1/app/set_auto_upgrade`

- **setAutoUpgrade**(`*(no params extracted)*`)

## `/power_service/v1/app/shelly_ctrl_device`

- **changeShellyDeviceStatus**(`device_sn, device_pn, attributes`)

## `/power_service/v1/app/third/platform/list`

- **getThirdPartyPlatformList**(`station_id, unix, far_field`) → `ThirdPartyPlatformInfoModel`

## `/power_service/v1/app/upgrade_event_report`

- **getReportBleUpgrade**(`upgrade_even_device_infos`)

## `/power_service/v1/app/upgrade_event_reports`

- **getReportsBleUpgrade**(`bt_ble_mac, device_sn, unbind_type`)

## `/power_service/v1/app/whitelist/feature/check`

- **getWhiteListStatusRes**(`*(no params extracted)*`)

