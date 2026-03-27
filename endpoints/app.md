# App

> 20 function calls, 18 unique endpoints
>
> **Source**: Regenerated from ENDPOINT_FIELDS.md (authoritative reference)
>
> **HA relevance**: Device bind/unbind and OTA are relevant. Help/FAQ, feedback,
> banners, manuals, and push token endpoints are **not relevant** for HA integration
> (app UI and support features only).

## `/app/devicemanage/update_relate_device_info`

- **updateDeviceInfo**(`device_sn?, ble_mac, product_code, device_name, main_sw_version, sec_sw_version`)

## `/app/devicerelation/relate_device`

- **deviceBind**(`device_sn?, product_code, device_name, bt_ble_id, bt_ble_mac, firmware_version, wifi_name, parent_device_sn, parent_device_pn`) → `DeviceModel`

## `/app/devicerelation/un_relate_and_unbind_device`

- **iotDeviceUnbind**(`device_sn?, bt_ble_mac, parent_device_sn, parent_device_pn`)
- **deviceUnbind**(`bt_ble_mac?, device_sn, unbind_type`)

## `/app/devicerelation/up_alias_name`

- **updateDeviceName**(`device_sn?, device_mac, alias_name`)

## `/app/help/add_feedback`

- **postFeedback**(`attachment_key_prefixs?, device_name, product_number, device_sn, user_name, user_email, message_content, type, device_mac, subject, purchase_channel, order_number?`)

## `/app/help/app_versions/check`

- **checkUpdateForApp**(`version?`) → `AppUpdateModel`

## `/app/help/banner/nps`

- **getNpsSurveyList**(`*(none extracted)*`) → `BannerModel`

## `/app/help/banners`

- **getBanners**(`region?`) → `BannerModel`

## `/app/help/dst`

- **getDaylightSavingTime**(`city?`)
- **getCloudCurrentTimezone**(`city?`)

## `/app/help/dynamic/config/list`

- **getCustomerServicePhoneList**(`*(none extracted)*`) → `CustomerServicePhoneInfos`

## `/app/help/faqs`

- **getFaqs**(`*(none extracted)*`) → `FaqModel`

## `/app/help/handle_survey_popup`

- **handleSurveyPopup**(`banner_id?, handle_type`)

## `/app/help/manual_list`

- **getUserManualsDeviceList**(`*(none extracted)*`) → `UserManualsModel`

## `/app/help/product_tutorial_search`

- **searchUserManualsDeviceDataList**(`*(none extracted)*`) → `SearchUserManualsModel`

## `/app/help/scan_code_white_list`

- **scanodeWhiteListReq**(`*(none extracted)*`) → `UrlWhiteListModel`

## `/app/help/xtest/data`

- **postJML**(`*(no params extracted)*`)

## `/app/ota/batch/check_update`

- **checkBatchOTAUpdateWifi**(`*(none extracted)*`) → `BatchDeviceModel`

## `/app/push/register_push_token`

- **uploadDeviceToken**(`is_notification_enable?, token`)
