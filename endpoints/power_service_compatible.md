# Power Service Compatible

> 12 function calls, 12 unique endpoints

## `/power_service/v1/app/compatible/check_third_sn`

- **checkThirdSN**(`device_sn, insert_sn`) → `OTAUpdateStatus`

## `/power_service/v1/app/compatible/confirm_permissions_settings`

- **getConfirmPermissionsSettingsApi**(`sns`) → `BrandModel`

## `/power_service/v1/app/compatible/get_compatible_process`

- **checkSolarForceUpdateState**(`device_sn`) → `CheckSolarForceUpdateModel`

## `/power_service/v1/app/compatible/get_confirm_permissions`

- **getConfirmPermissionsApi**(`*(no params extracted)*`) → `ConfirmModel`

## `/power_service/v1/app/compatible/get_installation`

- **getInstallationApi**(`device_models`) → `SaveCompatibleSolarModel`

## `/power_service/v1/app/compatible/get_ota_info`

- **getThirdOtaInfo**(`device_sn, solar_pn, insert_sn, rollback_install_mode`) → `ThirdOtaInfoModel`

## `/power_service/v1/app/compatible/get_ota_update`

- **getThirdOtaStatus**(`device_mac`) → `OTAUpdateStatus`

## `/power_service/v1/app/compatible/installation_popup`

- **getIncompatiblePopupApi**(`solarbank_sn, site_id`)

## `/power_service/v1/app/compatible/save_compatible_solar`

- **saveCompatibleSolarApi**(`device_sn, param_type, device_pn`) → `SaveCompatibleSolarModel`

## `/power_service/v1/app/compatible/save_ota_complete_status`

- **saveThirdOtaInfo**(`device_model, device_sn, date`)

## `/power_service/v1/app/compatible/set_installation`

- **setInstallationApi**(`solarbank_sn, ota_complete_status`)

## `/power_service/v1/app/compatible/set_ota_update`

- **setThirdOta**(`install_mode, site_id, is_save, solarbank_sn`)

