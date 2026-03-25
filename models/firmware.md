# Firmware / OTA — Response Models

> 9 models

## BatchDeviceModel

Source: `base:bean/model/firmware_update/batch_device_model.dart`

```
current_version, device_type, file_md5, file_path, rom_version_name
```

## CheckUpgradeRecordModel

Source: `model/device_auto_upgrade.dart`

```
alias_name, auto_upgrade, child_upgrade_records, device_list, device_name,
device_pn, device_sn, icon, is_record, last_version, main_switch, site_id,
sub_device_list, upgrade_desc, upgrade_record_list, upgrade_record_type,
upgrade_time, upgrade_type, upgrade_version
```

## DeviceAutoUpGradDisposition

Source: `model/device_auto_upgrade.dart`

```
alias_name, auto_upgrade, child_upgrade_records, device_list, device_name,
device_pn, device_sn, icon, is_record, last_version, main_switch, site_id,
sub_device_list, upgrade_desc, upgrade_record_list, upgrade_record_type,
upgrade_time, upgrade_type, upgrade_version
```

## FirmwareUpdateModel

Source: `model/firmware_update_model.dart`

```
change_log, device_type, file_md5, file_path, file_size, force_upgrade,
introduction, is_forced, md5, needUpdate, need_Update, packages, parent_sn, pn,
rom_version_name, size, sn, sub_packages, url, version
```

## OTAUpdateStatus

Source: `model/get_ota_update_status.dart`

```
available, current_version, device_list, device_pn, device_sn,
display_installation, display_model_name, img_url, install_mode, is_ota_update,
need_installation, need_retry, retry_interval, solar_sn
```

## OtaUpdateModel

Source: `base:bean/model/ota_update_model.dart`

```
children, current_version, device_type, file_md5, file_path, full_package,
is_forced, rom_version_name
```

## SaveCompatibleSolarModel

Source: `model/get_ota_update_status.dart`

```
available, current_version, device_list, device_pn, device_sn,
display_installation, display_model_name, img_url, install_mode, is_ota_update,
need_installation, need_retry, retry_interval, solar_sn
```

## ThirdOtaInfoModel

Source: `ui/page/device/anker_ota/base/third_ota_info_model.dart`

```
ota_status
```

## UpgradeRecordModel

Source: `model/device_auto_upgrade.dart`

```
alias_name, auto_upgrade, child_upgrade_records, device_list, device_name,
device_pn, device_sn, icon, is_record, last_version, main_switch, site_id,
sub_device_list, upgrade_desc, upgrade_record_list, upgrade_record_type,
upgrade_time, upgrade_type, upgrade_version
```

