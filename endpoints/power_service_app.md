# Power Service App

> 17 function calls, 17 unique endpoints
>
> **Source**: Regenerated from ENDPOINT_FIELDS.md (authoritative reference)

## `/power_service/v1/app/after_sale/check_popup`

- **checkDevicePopUpApi**(`*(no params in ENDPOINT_FIELDS.md)*`)

## `/power_service/v1/app/after_sale/get_popup`

- **queryA17Y0Popup**(`site_id?`)

## `/power_service/v1/app/check_upgrade_record`

- **checkUpgradeRecord**(`device_sn?, type, device_sns?`) → `CheckUpgradeRecordModel`

## `/power_service/v1/app/get_annual_report`

- **getAnnualReport**(`*(none extracted)*`) → `Post2024Model`

## `/power_service/v1/app/get_auto_upgrade`

- **getAutoUpgrade**(`*(none extracted)*`) → `DeviceAutoUpGradDisposition`

## `/power_service/v1/app/get_phonecode_list`

- **sharePhoneCode**(`*(no params in ENDPOINT_FIELDS.md)*`)

## `/power_service/v1/app/get_relate_and_bind_devices`

- **getDevicesList**(`*(none extracted)*`) → `DeviceModel`

## `/power_service/v1/app/get_relate_device_fittings`

- **getRelateAccessory**(`device_sn?`) → `DeviceModel`

## `/power_service/v1/app/get_token_by_userid`

- **getAccessTokenByUserID**(`user_id?`)

## `/power_service/v1/app/get_upgrade_record`

- **getUpgradeRecord**(`type?, device_sn`) → `UpgradeRecordModel`

## `/power_service/v1/app/get_user_op_shelly_status`

- **checkIsGrantedDeviceChanged**(`token?`)

## `/power_service/v1/app/set_auto_upgrade`

- **setAutoUpgrade**(`*(no params in ENDPOINT_FIELDS.md)*`)

## `/power_service/v1/app/shelly_ctrl_device`

- **changeShellyDeviceStatus**(`device_sn?, op_type, toggle, value`)

## `/power_service/v1/app/third/platform/list`

- **getThirdPartyPlatformList**(`app_id?, anker_power`) → `ThirdPartyPlatformInfoModel`

## `/power_service/v1/app/upgrade_event_report`

- **getReportBleUpgrade**(`device_sn?, device_pn, device_type, upgrade_type, after_version, before_version, upgrade_time, site_id`)

## `/power_service/v1/app/upgrade_event_reports`

- **getReportsBleUpgrade**(`upgrade_even_device_infos?`)

## `/power_service/v1/app/whitelist/feature/check`

- **getWhiteListStatusRes**(`check_list?, feature_code, product_code`)
