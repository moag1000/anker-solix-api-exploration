# Power Service Compatible

> **Numbers under review (2026-10-19):** integers on this page that came from decompiled code were read without Smi decoding and may be 2× too large. Verified values: see docs/audit/endpoints.md; corrected facts live on their owner pages (docs/STRUCTURE.md).

> 12 function calls, 12 unique endpoints
>
> **Source**: Regenerated from ENDPOINT_FIELDS.md (authoritative reference)

## `/power_service/v1/app/compatible/check_third_sn`

- **checkThirdSN**(`device_model?, device_sn, brand_id`) → `OTAUpdateStatus`

## `/power_service/v1/app/compatible/confirm_permissions_settings`

- **getConfirmPermissionsSettingsApi**(`device_model?, confirm_type`) → `BrandModel`

## `/power_service/v1/app/compatible/get_compatible_process`

- **checkSolarForceUpdateState**(`solar_sn?, solarbank_sn`) → `CheckSolarForceUpdateModel`

## `/power_service/v1/app/compatible/get_confirm_permissions`

- **getConfirmPermissionsApi**(`device_model?`) → `ConfirmModel`

## `/power_service/v1/app/compatible/get_installation`

- **getInstallationApi**(`solarbank_sn?, site_id?`) → `SaveCompatibleSolarModel`

## `/power_service/v1/app/compatible/get_ota_info`

- **getThirdOtaInfo**(`solar_bank_sn?, solar_sn`) → `ThirdOtaInfoModel`

## `/power_service/v1/app/compatible/get_ota_update`

- **getThirdOtaStatus**(`device_sn?, insert_sn`) → `OTAUpdateStatus`

## `/power_service/v1/app/compatible/installation_popup`

- **getIncompatiblePopupApi**(`site_id?`)

## `/power_service/v1/app/compatible/save_compatible_solar`

- **saveCompatibleSolarApi**(`*(none extracted)*`) → `SaveCompatibleSolarModel`

## `/power_service/v1/app/compatible/save_ota_complete_status`

- **saveThirdOtaInfo**(`solarbank_sn?, ota_complete_status`)

## `/power_service/v1/app/compatible/set_installation`

- **setInstallationApi**(`install_mode?, site_id?, is_save, solarbank_sn?`)

## `/power_service/v1/app/compatible/set_ota_update`

- **setThirdOta**(`device_sn?, solar_pn, insert_sn, rollback_install_mode`)

## `/power_service/v1/app/compatible/set_power_cutoff`

- **set_power_cutoff**(`device_sn, cutoff_data_id`)
  - Upstream-confirmed: sets min SOC via `cutoff_data_id` from `get_power_cutoff` response
