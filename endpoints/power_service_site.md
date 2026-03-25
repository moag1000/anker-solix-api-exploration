# Power Service Site

> 51 function calls, 31 unique endpoints

## `/power_service/v1/site/add_charging_device`

- **addChargingDevice**(`*(no params extracted)*`)

## `/power_service/v1/site/add_site_devices`

- **multiAddDeviceInfo**(`device_model`)

## `/power_service/v1/site/can_create_site`

- **checkCanCreateSite**(`*(no params extracted)*`) → `CanCreateSiteModel`
- **createSiteHomeRequest**(`type, device_sn`)

## `/power_service/v1/site/co2_ranking`

- **queryRankingInfo**(`station_id, pn, language, event`) → `RankEntity`

## `/power_service/v1/site/create_site`

- **createSiteRequest**(`station_id`) → `CreateSiteResponseModel`

## `/power_service/v1/site/delete_charging_device`

- **deleteChargingDevice**(`*(no params extracted)*`)

## `/power_service/v1/site/delete_site`

- **deleteSite**(`*(no params extracted)*`)

## `/power_service/v1/site/delete_site_devices`

- **deleteSitePPSRequest**(`device_sn`)

## `/power_service/v1/site/get_addable_site_list`

- **getAddableSiteList**(`*(no params extracted)*`) → `A17B1AddableSiteModel`

## `/power_service/v1/site/get_charging_device`

- **getChargingDeviceRequest**(`city`) → `A1340ChargingDeviceData`

## `/power_service/v1/site/get_comb_addable_sites`

- **getDeviceJoinSiteList**(`product_code`)

## `/power_service/v1/site/get_home_load_chart`

- **getSiteHomeLoadChat**(`*(no params extracted)*`) → `HomeLoadChat`

## `/power_service/v1/site/get_power_limit`

- **getSitePowerLimit**(`site_id, param_type=16`) → `StationPowerLimitModel`

## `/power_service/v1/site/get_scen_info`

- **querySceneInfo**(`sn`)

## `/power_service/v1/site/get_schedule`

- **getSiteSchedule**(`site_id`) → `SiteScheduleModel`
- **queryBasicStatus**(`station_id, param_types`) → `SiteScheduleModel`

## `/power_service/v1/site/get_site_detail`

- **getStationDetail**(`device_mac, sub_package, sub_ota_way, force_version, device_type, sn`) → `OtaUpdateModel`
- **getGreenPPSSiteDetail**(`site_id, param_type=3`) → `GreenPPSSiteDetailModel`
- **getRemainPluginsDetails**(`site_id`)

## `/power_service/v1/site/get_site_device_param`

- **getSafetySocParams**(`site_id`) → `GetSiteDeviceParamResponse`
- **getCombineBoxListData**(`site_id, param_type=26, cmd`) → `CombineBoxEntity`
- **getThreePvParam**(`site_id, param_type=20`) → `SiteDeviceParamData`
- **getStationCountryCode**(`*(no params extracted)*`)
- **getSitePeakTimeDeviceParam**(`device_sn, attributes, pps_use_time`) → `PeakTimeModel`
- **get17C1SiteDeviceParam**(`site_id, price, site_co2, site_price_unit, price_type, current_mode, accuracy`) → `SiteConsumptionStrategyModel`
- **getSiteDeviceParam**(`site_id`) → `SiteHomeLoadModel`
- **getSiteEnablePeakDeviceParam**(`site_id, param_type=5`)
- **getSiteLowerLimitDeviceParam**(`site_id, param_type=1`)
- **getSiteGreenModeDeviceParam**(`counrty`)

## `/power_service/v1/site/get_site_list`

- **getUserSiteList**(`product_code`) → `UserSiteListModel`

## `/power_service/v1/site/get_site_price`

- **getSitePriceRequest**(`site_id`) → `SitePriceModel`

## `/power_service/v1/site/get_site_rules`

- **getSiteRules**(`*(no params extracted)*`) → `A17B1SiteRules`

## `/power_service/v1/site/get_wifi_info_list`

- **getSiteWifiInfoRequest**(`site_id, power_site_type`) → `SiteWifiInfoModel`

## `/power_service/v1/site/list_user_devices`

- **getUserPPSDevice**(`site_id`) → `UserSiteDevicePPSModel`

## `/power_service/v1/site/local_net`

- **selfCheckNetwork**(`site_id, param_type, cmd, param_data`)

## `/power_service/v1/site/reset_charging_device`

- **resetChargingDevice**(`device_sn, device_mac, alias_name`)

## `/power_service/v1/site/set_device_feature`

- **setRemainPluginStatus**(`*(no params extracted)*`)

## `/power_service/v1/site/set_site_device_param`

- **set17C1SiteDeviceParam**(`device_sn, attributes`)
- **setSafetySocParams**(`site_id`)
- **setSiteDeviceParam**(`*(no params extracted)*`)
- **setStationCountryCode**(`site_id, param_type`)
- **setDynamicPrice**(`device_sn, mode, protocol_key, status`)
- **setThreePvInstallSwitch**(`*(no params extracted)*`)
- **setSiteDevicePowerLimit**(`station_id, unix, near_field`)

## `/power_service/v1/site/shift_power_site_type`

- **shiftPowerSite**(`site_id, param_type, cmd, device_sn, param_data`)

## `/power_service/v1/site/update_charging_device`

- **updateChargingDevice**(`*(no params extracted)*`)

## `/power_service/v1/site/update_site`

- **updateSiteNameInfoRequest**(`attachment_key_prefixs, device_name, product_number, device_sn, user_name, user_email, message_content, type, device_mac, subject, purchase_channel, order_number`)

## `/power_service/v1/site/update_site_devices`

- **updateSiteDevices**(`station_id, far_field_model`)

## `/power_service/v1/site/update_site_price`

- **updateSitePriceRequest**(`*(no params extracted)*`)
- **postCloudSitePrice**(`phone_number, verify_code, access_token, third_party, client_secret_info, public_key, open_id`)

