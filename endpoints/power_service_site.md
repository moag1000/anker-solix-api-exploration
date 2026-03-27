# Power Service Site

> 51 function calls, 31 unique endpoints
>
> **Source**: Regenerated from ENDPOINT_FIELDS.md (authoritative reference)

## `/power_service/v1/site/add_charging_device`

- **addChargingDevice**(`site_id?, ev_charger, device_sn`)

## `/power_service/v1/site/add_site_devices`

- **multiAddDeviceInfo**(`site_id?, devices`)

## `/power_service/v1/site/can_create_site`

- **checkCanCreateSite**(`*(none extracted)*`) → `CanCreateSiteModel`
- **createSiteHomeRequest**(`type?, device_sn`)

## `/power_service/v1/site/co2_ranking`

- **queryRankingInfo**(`site_id?`) → `RankEntity`

## `/power_service/v1/site/create_site`

- **createSiteRequest**(`site_name?, site_img, solar_list, pps_list?, solarbank_list?, home_backup_system_list?, powerpanel_list?, grid_list?, solarbank_pps_list?, smartplug_list?, combiner_box_list?, charging_pile_list?`) → `CreateSiteResponseModel`

## `/power_service/v1/site/delete_charging_device`

- **deleteChargingDevice**(`site_id?, device_sn?`)

## `/power_service/v1/site/delete_site`

- **deleteSite**(`site_id?`)

## `/power_service/v1/site/delete_site_devices`

- **deleteSitePPSRequest**(`site_id?, device_sn`)

## `/power_service/v1/site/get_addable_site_list`

- **getAddableSiteList**(`device_sn?, device_model`) → `A17B1AddableSiteModel`

## `/power_service/v1/site/get_charging_device`

- **getChargingDeviceRequest**(`*(none extracted)*`) → `A1340ChargingDeviceData`

## `/power_service/v1/site/get_comb_addable_sites`

- **getDeviceJoinSiteList**(`devices?`)

## `/power_service/v1/site/get_home_load_chart`

- **getSiteHomeLoadChat**(`site_id?, device_sn`) → `HomeLoadChat`

## `/power_service/v1/site/get_power_limit`

- **getSitePowerLimit**(`site_id?`) → `StationPowerLimitModel`

## `/power_service/v1/site/get_scen_info`

- **querySceneInfo**(`site_id?`)

## `/power_service/v1/site/get_schedule`

- **getSiteSchedule**(`site_id?`) → `SiteScheduleModel`
- **queryBasicStatus**(`site_id?`) → `SiteScheduleModel`

## `/power_service/v1/site/get_site_detail`

- **getStationDetail**(`site_id?`) → `DeviceListModel`
- **getGreenPPSSiteDetail**(`site_id?`) → `GreenPPSSiteDetailModel`
- **getRemainPluginsDetails**(`site_id?`)

## `/power_service/v1/site/get_site_device_param`

- **getSafetySocParams**(`site_id?, param_type`) → `GetSiteDeviceParamResponse`
- **getCombineBoxListData**(`site_id?, param_type`) → `CombineBoxEntity`
- **getThreePvParam**(`site_id?, param_type, cmd`) → `SiteDeviceParamData`
- **getStationCountryCode**(`site_id?, param_type`)
- **getSitePeakTimeDeviceParam**(`site_id?, param_type`) → `PeakTimeModel`
- **get17C1SiteDeviceParam**(`site_id?, param_type, cmd, device_sn, parallel_type?`) → `SiteConsumptionStrategyModel`
- **getSiteDeviceParam**(`site_id?, param_type`) → `SiteHomeLoadModel`
- **getSiteEnablePeakDeviceParam**(`site_id?, param_type`)
- **getSiteLowerLimitDeviceParam**(`site_id?, param_type`)
- **getSiteGreenModeDeviceParam**(`site_id?, param_type`)

## `/power_service/v1/site/get_site_list`

- **getUserSiteList**(`*(none extracted)*`) → `UserSiteListModel`

## `/power_service/v1/site/get_site_price`

- **getSitePriceRequest**(`site_id?, accuracy`) → `SitePriceModel`

## `/power_service/v1/site/get_site_rules`

- **getSiteRules**(`*(none extracted)*`) → `A17B1SiteRules`

## `/power_service/v1/site/get_wifi_info_list`

- **getSiteWifiInfoRequest**(`*(none extracted)*`) → `SiteWifiInfoModel`

## `/power_service/v1/site/list_user_devices`

- **getUserPPSDevice**(`device_models?`) → `UserSiteDevicePPSModel`

## `/power_service/v1/site/local_net`

- **selfCheckNetwork**(`list?`)

## `/power_service/v1/site/reset_charging_device`

- **resetChargingDevice**(`site_id?, device_sn?`)

## `/power_service/v1/site/set_device_feature`

- **setRemainPluginStatus**(`site_id?, smart_plug?`)

## `/power_service/v1/site/set_site_device_param`

- **set17C1SiteDeviceParam**(`site_id?, param_type, cmd, device_sn, param_data?`)
- **setSafetySocParams**(`cmd?, site_id, param_type, param_data`)
- **setSiteDeviceParam**(`site_id?, param_type, cmd, param_data`)
- **setStationCountryCode**(`site_id?, param_type, cmd, param_data`)
- **setDynamicPrice**(`site_id?, param_type, cmd, param_data`)
- **setThreePvInstallSwitch**(`site_id?, param_type, cmd, param_data`)
- **setSiteDevicePowerLimit**(`site_id?, param_type, cmd, param_data`)
  - ⚠️ `power_limit`, `limit`, `limit_real` are **inside** the JSON-encoded `param_data` string

## `/power_service/v1/site/shift_power_site_type`

- **shiftPowerSite**(`site_id?, power_site_type`)

## `/power_service/v1/site/update_charging_device`

- **updateChargingDevice**(`site_id?, device_sn?`)

## `/power_service/v1/site/update_site`

- **updateSiteNameInfoRequest**(`site_id?, site_name?, site_img?`)

## `/power_service/v1/site/update_site_devices`

- **updateSiteDevices**(`site_id?, pps_list`)

## `/power_service/v1/site/update_site_price`

- **updateSitePriceRequest**(`site_id?, price, site_co2?, site_price_unit?, price_type?, current_mode?, accuracy?, dynamic_price?`)
  - `dynamic_price` nested: `{"country": "...", "company": "Nordpool", "area": "GER", "pct": float?, "adjust_coef": float?}`
