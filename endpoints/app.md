# App

> 20 function calls, 18 unique endpoints

## `/app/devicemanage/update_relate_device_info`

- **updateDeviceInfo**(`company, area, date, device_sn`)

## `/app/devicerelation/relate_device`

- **deviceBind**(`check_list, feature_code, product_code`) → `DeviceModel`

## `/app/devicerelation/un_relate_and_unbind_device`

- **iotDeviceUnbind**(`device_sn`)
- **deviceUnbind**(`sn`)

## `/app/devicerelation/up_alias_name`

- **updateDeviceName**(`peak_sessions`)

## `/app/help/add_feedback`

- **postFeedback**(`*(no params extracted)*`)

## `/app/help/app_versions/check`

- **checkUpdateForApp**(`app_id, anker_power`) → `AppUpdateModel`

## `/app/help/banner/nps`

- **getNpsSurveyList**(`device_sn, attributes, init_status`) → `BannerModel`

## `/app/help/banners`

- **getBanners**(`*(no params extracted)*`) → `BannerModel`

## `/app/help/dst`

- **getDaylightSavingTime**(`device_sn`)
- **getCloudCurrentTimezone**(`station_id`)

## `/app/help/dynamic/config/list`

- **getCustomerServicePhoneList**(`*(no params extracted)*`) → `CustomerServicePhoneInfos`

## `/app/help/faqs`

- **getFaqs**(`station_id`) → `FaqModel`

## `/app/help/handle_survey_popup`

- **handleSurveyPopup**(`*(no params extracted)*`)

## `/app/help/manual_list`

- **getUserManualsDeviceList**(`site_id`) → `UserManualsModel`

## `/app/help/product_tutorial_search`

- **searchUserManualsDeviceDataList**(`city`) → `SearchUserManualsModel`

## `/app/help/scan_code_white_list`

- **scanodeWhiteListReq**(`device_sn`) → `UrlWhiteListModel`

## `/app/help/xtest/data`

- **postJML**(`*(no params extracted)*`)

## `/app/ota/batch/check_update`

- **checkBatchOTAUpdateWifi**(`device_sn, type, start_time`) → `BatchDeviceModel`

## `/app/push/register_push_token`

- **uploadDeviceToken**(`ab, mode`) → `RegionHostModel`

