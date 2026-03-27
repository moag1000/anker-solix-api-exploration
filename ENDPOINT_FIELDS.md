# Endpoint → Request Fields → Response Model

> Direct answer to: 'What JSON field names are used per API endpoint?'
> Request params from decompiled function calls. Response models from `fromJson` in same scope.
> Fields without `?` are always sent. Fields with `?` are conditional.

## `update_relate_device_info`
`/app/devicemanage/update_relate_device_info`

- **updateDeviceInfo**(`device_sn?, ble_mac, product_code, device_name, main_sw_version, sec_sw_version`)

## `relate_device`
`/app/devicerelation/relate_device`

- **deviceBind**(`device_sn?, product_code, device_name, bt_ble_id, bt_ble_mac, firmware_version, wifi_name, parent_device_sn, parent_device_pn`) → **DeviceModel**

## `un_relate_and_unbind_device`
`/app/devicerelation/un_relate_and_unbind_device`

- **iotDeviceUnbind**(`device_sn?, bt_ble_mac, parent_device_sn, parent_device_pn`)
- **deviceUnbind**(`bt_ble_mac?, device_sn, unbind_type`)

## `up_alias_name`
`/app/devicerelation/up_alias_name`

- **updateDeviceName**(`device_sn?, device_mac, alias_name`)

## `add_feedback`
`/app/help/add_feedback`

- **postFeedback**(`attachment_key_prefixs?, device_name, product_number, device_sn, user_name, user_email, message_content, type, device_mac, subject, purchase_channel, order_number?`)

## `check`
`/app/help/app_versions/check`

- **checkUpdateForApp**(`version?`) → **AppUpdateModel**

## `nps`
`/app/help/banner/nps`

- **getNpsSurveyList**(`*(none extracted)*`) → **BannerModel**

## `banners`
`/app/help/banners`

- **getBanners**(`region?`) → **BannerModel**

## `dst`
`/app/help/dst`

- **getDaylightSavingTime**(`city?`)
- **getCloudCurrentTimezone**(`city?`)

## `list`
`/app/help/dynamic/config/list`

- **getCustomerServicePhoneList**(`*(none extracted)*`) → **CustomerServicePhoneInfos**

## `faqs`
`/app/help/faqs`

- **getFaqs**(`*(none extracted)*`) → **FaqModel**

## `handle_survey_popup`
`/app/help/handle_survey_popup`

- **handleSurveyPopup**(`banner_id?, handle_type`)

## `manual_list`
`/app/help/manual_list`

- **getUserManualsDeviceList**(`*(none extracted)*`) → **UserManualsModel**

## `product_tutorial_search`
`/app/help/product_tutorial_search`

- **searchUserManualsDeviceDataList**(`*(none extracted)*`) → **SearchUserManualsModel**

## `scan_code_white_list`
`/app/help/scan_code_white_list`

- **scanodeWhiteListReq**(`*(none extracted)*`) → **UrlWhiteListModel**

## `check_update`
`/app/ota/batch/check_update`

- **checkBatchOTAUpdateWifi**(`*(none extracted)*`) → **BatchDeviceModel**

## `register_push_token`
`/app/push/register_push_token`

- **uploadDeviceToken**(`is_notification_enable?, token`)

## `support`
`/charging_common_svc/location/support`

- **getLocationSupport**(`business_type?, identifier_type, identifier_id`) → **SupportLocation**

## `get_configs`
`/charging_energy_service/get_configs`

- **getSiteConfigs**(`station_id?, param_types`)

## `get_device_infos`
`/charging_energy_service/get_device_infos`

- **getDeviceInfos**(`sns?`) → **DeviceInfosModel**

## `get_error_infos`
`/charging_energy_service/get_error_infos`

- **getErrorInfos**(`sn_errors?`) → **ErrorInfosModel**

## `get_installation_inspection`
`/charging_energy_service/get_installation_inspection`

- **getInstallation**(`sn?`) → **SceneInfo**

## `get_rom_versions`
`/charging_energy_service/get_rom_versions`

- **checkFirmwareWifi**(`main_sn?, device_rom_versions`) → **FirmwareUpdateModel**

## `get_wifi_info`
`/charging_energy_service/get_wifi_info`

- **getWifiInfoOf17B1**(`sn?`) → **WifiInfoModel**

## `preprocess_utility_rate_plan`
`/charging_energy_service/preprocess_utility_rate_plan`

- **dealUtilityRatePlanData**(`peak_sessions?`)

## `sync_installation_inspection`
`/charging_energy_service/sync_installation_inspection`

- **syncInstallation**(`sn?, page, errors`)

## `adjust_station_price_unit`
`/charging_hes_svc/adjust_station_price_unit`

- **changePriceUnit**(`station_id?, price_unit`)

## `check_function`
`/charging_hes_svc/check_function`

- **checkFunction**(`station_id?`) → **CheckFunctionModel**

## `deal_share_data`
`/charging_hes_svc/deal_share_data`

- **agreeOrRefuseVppDisclaimer**(`sn?, action`)

## `device_command`
`/charging_hes_svc/device_command`

- **sendDeviceCommand**(`station_id?, main_sn, time, electricity_strategy?, add_diesel?, screen_setting?, utility_rate_plan?, ack_peak_valley?, advanced_setting, heat_pump_setting?, accuracy?, cls_reset, off_grid_switching, evcharger_setting?, version?`)

## `get_aiems_profit`
`/charging_hes_svc/get_aiems_profit`

- **queryLargeChargerAiEmsProfit**(`*(none extracted)*`) → **LargeChargerAiEmsProfit**

## `get_auto_disaster_prepare_detail`
`/charging_hes_svc/get_auto_disaster_prepare_detail`

- **getAutoDisasterPrepareDetail**(`station_id?, unix, near_field?`) → **AutoDisasterDetailModel**

## `get_auto_disaster_prepare_status`
`/charging_hes_svc/get_auto_disaster_prepare_status`

- **getAutoDisasterPrepareStatus**(`station_id?`) → **AutoDisasterPrepareStatusModel**

## `get_current_disaster_prepare_details`
`/charging_hes_svc/get_current_disaster_prepare_details`

- **getCurrentDisasterPrepareDetails**(`*(none extracted)*`) → **DisasterPrepareDetailsModel**

## `get_device_command`
`/charging_hes_svc/get_device_command`

- **getDeviceCommand**(`station_id?, accuracy`) → **A5101DeviceCommandModel**

## `get_device_product_info`
`/charging_hes_svc/get_device_product_info`

- **getHesDeviceIcons**(`*(none extracted)*`) → **HesProductsInfoModel**

## `get_heat_pump_plan_json`
`/charging_hes_svc/get_heat_pump_plan_json`

- **getHeatPumpTimePlan**(`heat_pump_plan?`)

## `get_hes_dev_info`
`/charging_hes_svc/get_hes_dev_info`

- **getHesDeviceList**(`*(none extracted)*`) → **A5101DeviceListModel**

## `get_install_info`
`/charging_hes_svc/get_install_info`

- **getDeviceInstallAddress**(`*(none extracted)*`) → **A5101InstallAddressModel**

## `get_installer_info`
`/charging_hes_svc/get_installer_info`

- **getInstallerInfo**(`*(none extracted)*`) → **A5101InstallInformationModel**

## `get_station_config_and_status`
`/charging_hes_svc/get_station_config_and_status`

- **getA5101StationConfigDetail**(`station_id?`) → **A5101StationGridConfigModel**

## `get_user_bind_and_not_in_station_evchargers`
`/charging_hes_svc/get_user_bind_and_not_in_station_evchargers`

- **getX1BindUserUnbindChargerList**(`*(none extracted)*`) → **A5101EvChargerListModel**

## `get_vpp_check_code`
`/charging_hes_svc/get_vpp_check_code`

- **getVppInfo**(`station_id?, get_code, current_version`) → **VppInfoModel**

## `get_vpp_service_policy_by_agg_user`
`/charging_hes_svc/get_vpp_service_policy_by_agg_user`

- **getVppDisclaimer**(`current_version?`)

## `quit_auto_disaster_prepare`
`/charging_hes_svc/quit_auto_disaster_prepare`

- **quitAutoDisasterPrepare**(`station_id?, unix, far_field?`) → **AutoDisasterQuitPrepareModel**

## `restart_peak_session`
`/charging_hes_svc/restart_peak_session`

- **deleteAndRestartPeakValley**(`station_id?, far_field_model`)

## `update_wifi_config`
`/charging_hes_svc/update_wifi_config`

- **updateWiFiConfig**(`ssid?, sn, rssi, encryption`)

## `get_station_evchargers`
`/charging_hes_svc/get_station_evchargers`

- **getX1BindChargerList**(`station_id?`)

## `set_station_evchargers`
`/charging_hes_svc/set_station_evchargers`

- **bindUnX1Charger**(`stationId?, evChargers, deleteFlag?, forceBindFlag?`)
  - ⚠️ Uses **camelCase** field names (unlike most API endpoints)

## `get_system_running_time`
`/charging_hes_svc/get_system_running_time`

- **getDeviceRunTime**(`station_id?`)

## `get_world_monetary_unit`
`/charging_hes_svc/get_world_monetary_unit`

- **getPriceUnits**(`station_id?`)

## `update_hes_utility_rate_plan`
`/charging_hes_svc/update_hes_utility_rate_plan`

- **updatePeakAndValley**(`siteId?, peakValleyPriceSeason`)
  - ⚠️ Uses **camelCase** field names
  - This is a HES-specific endpoint, NOT a `set_site_device_param` wrapper

## `user_event_alarm`
`/charging_hes_svc/user_event_alarm`

- **reportHesEvents**(`station_id?, pn, language, event`) → **A5101EventsSetModel**

## `user_fault_alarm`
`/charging_hes_svc/user_fault_alarm`

- **sendDeviceReport**(`station_id?`)

## `getPvStatus`
`/charging_pv_svc/getPvStatus`

- **getPvStatus**(`sns?`) → **A5140DeviceStatus**

## `selectUserTieredElecPrice`
`/charging_pv_svc/selectUserTieredElecPrice`

- **selectUserTieredElecPrice**(`sn?`) → **CurrencyElecModel**

## `add_charging_mode`
`/mini_power/v1/app/charging/add_charging_mode`

- **addCustomChargeMode**(`device_sn?, name, number, total_power, max_total_power, auto_exit, has_charge_protocol, power_settings?`)

## `delete_charging_mode`
`/mini_power/v1/app/charging/delete_charging_mode`

- **deleteCustomChargeMode**(`id?`)

## `get_charging_mode_list`
`/mini_power/v1/app/charging/get_charging_mode_list`

- **getCustomChargeModeList**(`device_sn?`) → **A2345CustomModeList**

## `update_charging_mode`
`/mini_power/v1/app/charging/update_charging_mode`

- **updateCustomChargeMode**(`id?, name, total_power, max_total_power, auto_exit, has_charge_protocol, power_settings?`)

## `get_easter_egg_trigger_list`
`/mini_power/v1/app/egg/get_easter_egg_trigger_list`

- **getEasterEggRecord**(`device_sn?`) → **EasterEggTiggerRecordModel**

## `report_easter_egg_trigger_status`
`/mini_power/v1/app/egg/report_easter_egg_trigger_status`

- **addEasterEggStatusRecord**(`device_sn?, egg_type, report_time?`)

## `get_day_power_data`
`/mini_power/v1/app/power/get_day_power_data`

- **getDayPowerData**(`device_model?, device_sn, date`) → **DayPowerModel**

## `get_charging_device_identity_new_status`
`/mini_power/v1/app/setting/get_charging_device_identity_new_status`

- **getA2687StandardChargingDeviceModelIdentityStatus**(`device_sn?, charging_device_identity_new_status?`)

## `get_charging_device_identity_status_default_true`
`/mini_power/v1/app/setting/get_charging_device_identity_status_default_true`

- **getA2345DeviceIdentityStatus**(`device_sn?, status?`)

## `get_device_setting`
`/mini_power/v1/app/setting/get_device_setting`

- **getCustomChargeModeSetting**(`device_sn?, charging_mode_status?, compatibility_status, charging_device_identity_status`)

## `get_port_remarks`
`/mini_power/v1/app/setting/get_port_remarks`

- **getPortRemarks**(`device_sn?`)

## `get_power_range_support_protocols`
`/mini_power/v1/app/setting/get_power_range_support_protocols`

- **getPowerSupportProtocols**(`device_model?`) → **PowerRangeProtocolsResponse**

## `get_protocol_status`
`/mini_power/v1/app/setting/get_protocol_status`

- **getA2687ProtocolAgreementStatus**(`device_sn?`) → **A2687ProtocolAgreementModel**

## `set_charging_device_identity_new_status`
`/mini_power/v1/app/setting/set_charging_device_identity_new_status`

- **setA2687StandardChargingDeviceModelIdentityStatus**(`device_sn?, charging_device_identity_new_status`)

## `set_charging_device_identity_status`
`/mini_power/v1/app/setting/set_charging_device_identity_status`

- **setA2687ChargingDeviceModelIdentityStatus**(`device_sn?, charging_device_identity_status`)

## `set_charging_device_identity_status_default_true`
`/mini_power/v1/app/setting/set_charging_device_identity_status_default_true`

- **setA2345DeviceIdentityStatus**(`device_sn?, charging_device_identity_status_default_true`)

## `set_charging_mode_status`
`/mini_power/v1/app/setting/set_charging_mode_status`

- **saveCustomChargeModeSetting**(`device_sn?, charging_mode_status`)

## `set_compatibility_status`
`/mini_power/v1/app/setting/set_compatibility_status`

- **saveCompatibilityStatusSetting**(`device_sn?, compatibility_status`)

## `set_mode_sub_status`
`/mini_power/v1/app/setting/set_mode_sub_status`

- **setA2687ModeSubStatus**(`device_sn?, mode, protocol_key, status`)

## `set_port_remark`
`/mini_power/v1/app/setting/set_port_remark`

- **setPortRemark**(`device_sn?, port_name, remark`)

## `set_protocol_status`
`/mini_power/v1/app/setting/set_protocol_status`

- **setA2687ProtocolAgreementStatus**(`device_sn?, protocol_status`)

## `add_manual_clock_screensavers`
`/mini_power/v1/app/style/add_manual_clock_screensavers`

- **addA2345CustomClockScreenSavers**(`sn?, img_url, hash_code`)

## `delete_manual_clock_screensavers`
`/mini_power/v1/app/style/delete_manual_clock_screensavers`

- **deleteA2345CustomClockScreenSavers**(`id?`)

## `get_clock_screensavers`
`/mini_power/v1/app/style/get_clock_screensavers`

- **getScreenSaversByCategory**(`product_code?`)
- **getA2345ClockScreenSavers**(`product_code?`)

## `get_manual_clock_screensavers`
`/mini_power/v1/app/style/get_manual_clock_screensavers`

- **getA2345CustomClockScreenSavers**(`sn?`)

## `get_url`
`/mini_power/v1/app/style/get_url`

- **getA2345CustomClockScreenSaversRealUrl**(`short_url?`)

## `set_manual_clock_screensaver_name`
`/mini_power/v1/app/style/set_manual_clock_screensaver_name`

- **editA2345CustomClockScreenSaversName**(`sn?, screensaver_id, name?`)

## `get_status`
`/power_service/v1/ai_ems/get_status`

- **getAiModeStatusRequest**(`site_id?`) → **AiModeStatusModel**

## `profit`
`/power_service/v1/ai_ems/profit`

- **getAiEmsProfit**(`site_id?, start_time, end_time, type`) → **AiEmsProfitModel**

## `get_popup`
`/power_service/v1/app/after_sale/get_popup`

- **queryA17Y0Popup**(`site_id?`)

## `check_upgrade_record`
`/power_service/v1/app/check_upgrade_record`

- **checkUpgradeRecord**(`device_sn?, type, device_sns?`) → **CheckUpgradeRecordModel**

## `check_third_sn`
`/power_service/v1/app/compatible/check_third_sn`

- **checkThirdSN**(`device_model?, device_sn, brand_id`) → **OTAUpdateStatus**

## `confirm_permissions_settings`
`/power_service/v1/app/compatible/confirm_permissions_settings`

- **getConfirmPermissionsSettingsApi**(`device_model?, confirm_type`) → **BrandModel**

## `get_compatible_process`
`/power_service/v1/app/compatible/get_compatible_process`

- **checkSolarForceUpdateState**(`solar_sn?, solarbank_sn`) → **CheckSolarForceUpdateModel**

## `get_confirm_permissions`
`/power_service/v1/app/compatible/get_confirm_permissions`

- **getConfirmPermissionsApi**(`device_model?`) → **ConfirmModel**

## `get_installation`
`/power_service/v1/app/compatible/get_installation`

- **getInstallationApi**(`solarbank_sn?, site_id?`) → **SaveCompatibleSolarModel**

## `get_ota_info`
`/power_service/v1/app/compatible/get_ota_info`

- **getThirdOtaInfo**(`solar_bank_sn?, solar_sn`) → **ThirdOtaInfoModel**

## `get_ota_update`
`/power_service/v1/app/compatible/get_ota_update`

- **getThirdOtaStatus**(`device_sn?, insert_sn`) → **OTAUpdateStatus**

## `installation_popup`
`/power_service/v1/app/compatible/installation_popup`

- **getIncompatiblePopupApi**(`site_id?`)

## `save_compatible_solar`
`/power_service/v1/app/compatible/save_compatible_solar`

- **saveCompatibleSolarApi**(`*(none extracted)*`) → **SaveCompatibleSolarModel**

## `save_ota_complete_status`
`/power_service/v1/app/compatible/save_ota_complete_status`

- **saveThirdOtaInfo**(`solarbank_sn?, ota_complete_status`)

## `set_installation`
`/power_service/v1/app/compatible/set_installation`

- **setInstallationApi**(`install_mode?, site_id?, is_save, solarbank_sn?`)

## `set_ota_update`
`/power_service/v1/app/compatible/set_ota_update`

- **setThirdOta**(`device_sn?, solar_pn, insert_sn, rollback_install_mode`)

## `get_device_attrs`
`/power_service/v1/app/device/get_device_attrs`

- **getDeviceAttrsInfo**(`*(none extracted)*`) → **DeviceAttributes**
- **getDeviceAttrs**(`device_sn?, attributes, enable_0w_v2?`) → **DevicePowerLimit**
- **getTouElectricAttrs**(`device_sn?, attributes`) → **TouDeviceAttrsModel**

## `get_device_home_load`
`/power_service/v1/app/device/get_device_home_load`

- **getDeviceHomeLoadPort**(`device_sn?`) → **StationModel**
- **getDeviceHomeLoadRes**(`device_sn?`) → **SiteHomeLoadModel**
- **get17C1DeviceHomeLoadPort**(`device_sn?, param_type, device_pn`) → **A17C1DeviceHomeLoadData**

## `get_device_income`
`/power_service/v1/app/device/get_device_income`

- **getTOUChartStatistics**(`device_sn?, type, start_time`) → **TouBenifitsModel**

## `get_mes_device_info`
`/power_service/v1/app/device/get_mes_device_info`

- **getDeviceLaserSn**(`device_sn?`)

## `get_relate_belong`
`/power_service/v1/app/device/get_relate_belong`

- **getDeviceBindInfo**(`device_sn?`)

## `remove_param_config_key`
`/power_service/v1/app/device/remove_param_config_key`

- **removeParamConfigKey**(`site_id?, device_sn, remove_key, use_time`)

## `set_device_attrs`
`/power_service/v1/app/device/set_device_attrs`

> **Nesting confirmed by upstream**: All additional fields (`switch_0w`, `pv_power_limit`,
> `power_limit`, `ac_power_limit`, `tag`, `init_status`, etc.) go **inside** the `attributes`
> dict. Upstream pattern: `{"device_sn": "...", "attributes": {"pv_power_limit": 800, "switch_0w": 0}}`

- **setDevicePowerOptionsReq**(`device_sn?, attributes{power_limit?, ac_power_limit?, pv_power_limit?}`)
- **setDeviceGameStatus**(`device_sn?, attributes{init_status}`)
- **setTouElectricAttrs**(`device_sn?, attributes{pps_use_time}`)
- **getCurrencySetDeviceAttrs**(`device_sn?, attributes{currency}`)
- **setSolarName**(`device_sn?, device_pn, attributes`)
- **setDeviceFeedGridSwitch**(`device_sn?, attributes{switch_0w}`)
- **setDevicePvPowerOptionsReq**(`device_sn?, attributes{pv_power_limit}`)
- **setLocationTag**(`device_sn?, attributes{tag}`)
- **setPpsSolarName**(`device_sn?, device_pn, attributes`)

## `set_device_home_load`
`/power_service/v1/app/device/set_device_home_load`

- **setDeviceHomeLoadRes**(`site_id?, device_sn, home_load_data`)
  - ⚠️ Upstream confirms `site_id` is sent in request body (not just device_sn)
- **set17C1DeviceHomeLoadRes**(`device_sn?, mode_type, custom_rate_plan?, home_load_data?`)

## `get_annual_report`
`/power_service/v1/app/get_annual_report`

- **getAnnualReport**(`*(none extracted)*`) → **Post2024Model**

## `get_auto_upgrade`
`/power_service/v1/app/get_auto_upgrade`

- **getAutoUpgrade**(`*(none extracted)*`) → **DeviceAutoUpGradDisposition**

## `get_relate_and_bind_devices`
`/power_service/v1/app/get_relate_and_bind_devices`

- **getDevicesList**(`*(none extracted)*`) → **DeviceModel**

## `get_relate_device_fittings`
`/power_service/v1/app/get_relate_device_fittings`

- **getRelateAccessory**(`device_sn?`) → **DeviceModel**

## `get_token_by_userid`
`/power_service/v1/app/get_token_by_userid`

- **getAccessTokenByUserID**(`user_id?`)

## `get_upgrade_record`
`/power_service/v1/app/get_upgrade_record`

- **getUpgradeRecord**(`type?, device_sn`) → **UpgradeRecordModel**

## `get_user_op_shelly_status`
`/power_service/v1/app/get_user_op_shelly_status`

- **checkIsGrantedDeviceChanged**(`token?`)

## `get_invited_list`
`/power_service/v1/app/share_site/get_invited_list`

- **getInviteMember**(`site_id?, status`) → **SiteInviteMemberModel**

## `shelly_ctrl_device`
`/power_service/v1/app/shelly_ctrl_device`

- **changeShellyDeviceStatus**(`device_sn?, op_type, toggle, value`)

## `list`
`/power_service/v1/app/third/platform/list`

- **getThirdPartyPlatformList**(`app_id?, anker_power`) → **ThirdPartyPlatformInfoModel**

## `upgrade_event_report`
`/power_service/v1/app/upgrade_event_report`

- **getReportBleUpgrade**(`device_sn?, device_pn, device_type, upgrade_type, after_version, before_version, upgrade_time, site_id`)

## `upgrade_event_reports`
`/power_service/v1/app/upgrade_event_reports`

- **getReportsBleUpgrade**(`upgrade_even_device_infos?`)

## `check`
`/power_service/v1/app/whitelist/feature/check`

- **getWhiteListStatusRes**(`check_list?, feature_code, product_code`)

## `get_list`
`/power_service/v1/currency/get_list`

- **getCurrencyGetList**(`country?`) → **CurrencyInfo**

## `price_detail`
`/power_service/v1/dynamic_price/price_detail`

- **getDynamicPriceDetail**(`company?, area, date, device_sn`) → **DynamicPriceDetailModel**

## `support_option`
`/power_service/v1/dynamic_price/support_option`

- **getDynamicPriceSupportOption**(`site_id?, device_pn`) → **DynamicPriceCountryAreaModel**

## `get_message`
`/power_service/v1/get_message`

- **getMessage**(`last_time?, device_sns?, limit?, message_type, last_msg_id?`) → **MsgHttpModel**

## `get_message_not_disturb`
`/power_service/v1/get_message_not_disturb`

- **getMessageDisturb**(`*(none extracted)*`) → **MsgDisturbHttpModel**

## `message_not_disturb`
`/power_service/v1/message_not_disturb`

- **setEvChargerPushMessage**(`disturb_scenes`)
  - `disturb_scenes` is a nested object: `{"stop_charging": true, "start_charging": true, "paused_charging": true, "paused_car_charging": true, "restore_charging": true, "smart_charging": true, "boost_charging": true}`
  - Structurally inferred from toJson() decompilation (DisturbScenesHttpModel)
- **setMessageDisturb**(`start_time?, end_time?, disturb_switch?`)

## `can_create_site`
`/power_service/v1/site/can_create_site`

- **checkCanCreateSite**(`*(none extracted)*`) → **CanCreateSiteModel**

## `co2_ranking`
`/power_service/v1/site/co2_ranking`

- **queryRankingInfo**(`site_id?`) → **RankEntity**

## `create_site`
`/power_service/v1/site/create_site`

- **createSiteRequest**(`site_name?, site_img, solar_list, pps_list?, solarbank_list?, home_backup_system_list?, powerpanel_list?, grid_list?, solarbank_pps_list?, smartplug_list?, combiner_box_list?, charging_pile_list?`) → **CreateSiteResponseModel**

## `get_addable_site_list`
`/power_service/v1/site/get_addable_site_list`

- **getAddableSiteList**(`device_sn?, device_model`) → **A17B1AddableSiteModel**

## `get_charging_device`
`/power_service/v1/site/get_charging_device`

- **getChargingDeviceRequest**(`*(none extracted)*`) → **A1340ChargingDeviceData**

## `get_comb_addable_sites`
`/power_service/v1/site/get_comb_addable_sites`

- **getDeviceJoinSiteList**(`devices?`)

## `get_home_load_chart`
`/power_service/v1/site/get_home_load_chart`

- **getSiteHomeLoadChat**(`site_id?, device_sn`) → **HomeLoadChat**

## `get_power_limit`
`/power_service/v1/site/get_power_limit`

- **getSitePowerLimit**(`site_id?`) → **StationPowerLimitModel**

## `get_scen_info`
`/power_service/v1/site/get_scen_info`

- **querySceneInfo**(`site_id?`)

## `get_schedule`
`/power_service/v1/site/get_schedule`

- **getSiteSchedule**(`site_id?`) → **SiteScheduleModel**
- **queryBasicStatus**(`site_id?`) → **SiteScheduleModel**

## `get_site_detail`
`/power_service/v1/site/get_site_detail`

- **getStationDetail**(`site_id?`) → **DeviceListModel**
- **getGreenPPSSiteDetail**(`site_id?`) → **GreenPPSSiteDetailModel**
- **getRemainPluginsDetails**(`site_id?`)

## `get_site_device_param`
`/power_service/v1/site/get_site_device_param`

- **getSafetySocParams**(`site_id?, param_type`) → **GetSiteDeviceParamResponse**
- **getCombineBoxListData**(`site_id?, param_type`) → **CombineBoxEntity**
- **getThreePvParam**(`site_id?, param_type, cmd`) → **SiteDeviceParamData**
- **getStationCountryCode**(`site_id?, param_type`)
- **getSitePeakTimeDeviceParam**(`site_id?, param_type`) → **PeakTimeModel**
- **get17C1SiteDeviceParam**(`site_id?, param_type, cmd, device_sn, parallel_type?`) → **SiteConsumptionStrategyModel**
- **getSiteDeviceParam**(`site_id?, param_type`) → **SiteHomeLoadModel**
- **getSiteEnablePeakDeviceParam**(`site_id?, param_type`)
- **getSiteLowerLimitDeviceParam**(`site_id?, param_type`)
- **getSiteGreenModeDeviceParam**(`site_id?, param_type`)

## `get_site_list`
`/power_service/v1/site/get_site_list`

- **getUserSiteList**(`*(none extracted)*`) → **UserSiteListModel**

## `get_site_price`
`/power_service/v1/site/get_site_price`

- **getSitePriceRequest**(`site_id?, accuracy`) → **SitePriceModel**

## `get_site_rules`
`/power_service/v1/site/get_site_rules`

- **getSiteRules**(`*(none extracted)*`) → **A17B1SiteRules**

## `get_wifi_info_list`
`/power_service/v1/site/get_wifi_info_list`

- **getSiteWifiInfoRequest**(`*(none extracted)*`) → **SiteWifiInfoModel**

## `list_user_devices`
`/power_service/v1/site/list_user_devices`

- **getUserPPSDevice**(`device_models?`) → **UserSiteDevicePPSModel**

## `local_net`
`/power_service/v1/site/local_net`

- **selfCheckNetwork**(`list?`)

## `set_site_device_param`
`/power_service/v1/site/set_site_device_param`

- **set17C1SiteDeviceParam**(`site_id?, param_type, cmd, device_sn, param_data?`)
- **setSafetySocParams**(`cmd?, site_id, param_type, param_data`)
- **setSiteDeviceParam**(`site_id?, param_type, cmd, param_data`)
- **setStationCountryCode**(`site_id?, param_type, cmd, param_data`)
- **setDynamicPrice**(`site_id?, param_type, cmd, param_data`)
- **setThreePvInstallSwitch**(`site_id?, param_type, cmd, param_data`)
- **setSiteDevicePowerLimit**(`site_id?, param_type, cmd, param_data`)
  - ⚠️ `power_limit`, `limit`, `limit_real` are **inside** the JSON-encoded `param_data` string, not top-level fields
  - Actual `param_data`: `"{\"power_limit\":{\"limit\":3600,\"limit_real\":3600}}"`

## `shift_power_site_type`
`/power_service/v1/site/shift_power_site_type`

- **shiftPowerSite**(`site_id?, power_site_type`)

## `update_site_devices`
`/power_service/v1/site/update_site_devices`

- **updateSiteDevices**(`site_id?, pps_list`)

## `update_site_price`
`/power_service/v1/site/update_site_price`

- **updateSitePriceRequest**(`site_id?, price, site_co2?, site_price_unit?, price_type?, current_mode?, accuracy?, dynamic_price?`)
  - `dynamic_price` is a nested object (when `price_type="dynamic"`):
    `{"country": "...", "company": "Nordpool", "area": "GER", "pct": float?, "adjust_coef": float?}`

---

## Endpoints confirmed by upstream but missing from APK extraction

### `set_power_cutoff`
`/power_service/v1/app/compatible/set_power_cutoff`

- **set_power_cutoff**(`device_sn, cutoff_data_id`)
  - Upstream-confirmed: sets min SOC via cutoff_data_id from `get_power_cutoff` response
  - Note: Deprecated for SB1, but still functional

### `set_aps_power`
`/charging_pv_svc/set_aps_power`

- **set_device_pv_power**(`sn, power`)
  - Upstream-confirmed: sets standalone inverter power limit in W

---

## Nesting corrections from toJson() analysis (460 classes scanned)

### param_data inner fields (SetSiteDeviceParamData::toJson)
The `param_data` JSON string can contain: `id, soc, switch_0w, enable_0w, feed-in_power_limit, third_part_pv_setting`
- ⚠️ `feed-in_power_limit` uses a **HYPHEN** (not underscore!)
- `enable_0w_change` exists in the GET response but not in SET

### home_load_data inner fields (HomeRangesModel::toJson)
```json
{"id": 0, "turn_on": true, "start_time": "00:00", "end_time": "24:00",
 "power_setting_mode": 1, "charge_priority": 80, "priority_discharge_switch": 0,
 "appliance_loads": [{"name": "...", "power": 100, "number": 1, "id": 0}],
 "device_power_loads": [{"device_sn": "...", "power": 50}]}
```

### set_device_attrs Attributes inner fields (Attributes::toJson in soc_model.dart)
Full list of fields that go INSIDE `attributes`:
```
region_power_limit, power_limit_option, power_limit_option_real, user_power_limit,
legal_power_limit, ip_region, regulation_code, region_microinverter_limit,
rssi, feeder0w, switch_0w, pv_power_limit_option, pv_power_limit, enable_0w
```

### disturb_scenes is NESTED (DisturbScenesHttpModel::toJson)
```json
{"disturb_scenes": {"stop_charging": true, "start_charging": true, ...}}
```
The boolean fields are INSIDE `disturb_scenes`, not at the same level.

### SiteConsumptionStrategyModel (17C1 schedule response/request)
Additional fields: `reserved_soc`, `ai_ems: {status}`, `exceed_alarm` (in plan ranges)

### FeatureSwitch flags (SceneInfo response)
New flags: `enable_aiems_v2, grid_to_ev, meter_self_testing, power_limit_status, power_saving_mode`

---

## Statistics

- 148 endpoints from `http_request_repository_impl.dart` (initial extraction)
- +95 endpoints from device-specific logic files (see `endpoints/device_specific.md`)
- = **~243 total endpoints** across 10+ API service prefixes
- 460 toJson() classes scanned for nesting analysis
- 91 endpoints with identified response models
- 6 new API service prefixes discovered

---

148 endpoints. 90 with identified response models.
