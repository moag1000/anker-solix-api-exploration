# Required vs Optional Fields per API Endpoint

> Derived from conditional branching patterns in decompiled Dart code.
> Fields marked **required** are always included in the request body.
> Fields marked `?` have a conditional branch before assignment — likely optional or context-dependent.
> Endpoints with *(no params extracted)* pass parameters via object construction not visible as strings.
> This analysis may have false positives/negatives due to compiler optimizations.
>
> **Known limitation:** `site_id` and `device_sn` are marked as `?` (optional) in most endpoints.
> This is a systematic artifact — unrelated branch instructions before these fields cause false positives.
> In practice, `site_id` and `device_sn` are almost always required. Treat them as required unless
> the endpoint documentation explicitly says otherwise.

## `/app/devicemanage/update_relate_device_info`

**updateDeviceInfo**
- Required: `ble_mac, product_code, device_name, main_sw_version, sec_sw_version`
- Optional: `device_sn`

## `/app/devicerelation/relate_device`

**deviceBind**
- Required: `product_code, device_name, bt_ble_id, bt_ble_mac, firmware_version, wifi_name, parent_device_sn, parent_device_pn`
- Optional: `device_sn`

## `/app/devicerelation/un_relate_and_unbind_device`

**iotDeviceUnbind**
- Required: `bt_ble_mac, parent_device_sn, parent_device_pn`
- Optional: `device_sn`

**deviceUnbind**
- Required: `device_sn, unbind_type`
- Optional: `bt_ble_mac`

## `/app/devicerelation/up_alias_name`

**updateDeviceName**
- Required: `device_mac, alias_name`
- Optional: `device_sn`

## `/app/help/add_feedback`

**postFeedback**
- Required: `device_name, product_number, device_sn, user_name, user_email, message_content, type, device_mac, subject, purchase_channel`
- Optional: `attachment_key_prefixs, order_number`

## `/app/help/app_versions/check`

**checkUpdateForApp**
- Optional: `version`

## `/app/help/banner/nps`

**getNpsSurveyList** — *(no params extracted)*

## `/app/help/banners`

**getBanners**
- Optional: `region`

## `/app/help/dst`

**getDaylightSavingTime**
- Optional: `city`

**getCloudCurrentTimezone**
- Optional: `city`

## `/app/help/dynamic/config/list`

**getCustomerServicePhoneList** — *(no params extracted)*

## `/app/help/faqs`

**getFaqs** — *(no params extracted)*

## `/app/help/handle_survey_popup`

**handleSurveyPopup**
- Required: `handle_type`
- Optional: `banner_id`

## `/app/help/manual_list`

**getUserManualsDeviceList** — *(no params extracted)*

## `/app/help/product_tutorial_search`

**searchUserManualsDeviceDataList** — *(no params extracted)*

## `/app/help/scan_code_white_list`

**scanodeWhiteListReq** — *(no params extracted)*

## `/app/help/xtest/data`

**postJML** — *(no params extracted)*

## `/app/ota/batch/check_update`

**checkBatchOTAUpdateWifi** — *(no params extracted)*

## `/app/push/register_push_token`

**uploadDeviceToken**
- Required: `token`
- Optional: `is_notification_enable`

## `/charging_common_svc/location/support`

**getLocationSupport**
- Required: `identifier_type, identifier_id`
- Optional: `business_type`

## `/charging_energy_service/ack_utility_rate_plan`

**ackUtilityRatePlanData** — *(no params extracted)*

## `/charging_energy_service/adjust_station_price_unit`

**changeA17B1PriceUnit** — *(no params extracted)*

## `/charging_energy_service/get_configs`

**getSiteConfigs**
- Required: `param_types`
- Optional: `station_id`

## `/charging_energy_service/get_device_infos`

**getDeviceInfos**
- Optional: `sns`

## `/charging_energy_service/get_error_infos`

**getErrorInfos**
- Optional: `sn_errors`

## `/charging_energy_service/get_installation_inspection`

**getInstallation**
- Optional: `sn`

## `/charging_energy_service/get_rom_versions`

**checkFirmwareWifi**
- Required: `device_rom_versions`
- Optional: `main_sn`

## `/charging_energy_service/get_wifi_info`

**getWifiInfoOf17B1**
- Optional: `sn`

## `/charging_energy_service/get_world_monetary_unit`

**getA17B1PriceUnits** — *(no params extracted)*

## `/charging_energy_service/preprocess_utility_rate_plan`

**dealUtilityRatePlanData**
- Optional: `peak_sessions`

## `/charging_energy_service/restart_peak_session`

**restartPeakSession** — *(no params extracted)*

## `/charging_energy_service/sync_config`

**syncSiteConfig** — *(no params extracted)*

## `/charging_energy_service/sync_installation_inspection`

**syncInstallation**
- Required: `page, errors`
- Optional: `sn`

## `/charging_hes_svc/adjust_station_price_unit`

**changePriceUnit**
- Required: `price_unit`
- Optional: `station_id`

## `/charging_hes_svc/check_function`

**checkFunction**
- Optional: `station_id`

## `/charging_hes_svc/deal_share_data`

**agreeOrRefuseVppDisclaimer**
- Required: `action`
- Optional: `sn`

## `/charging_hes_svc/device_command`

**sendDeviceCommand**
- Required: `main_sn, time, advanced_setting, cls_reset, off_grid_switching`
- Optional: `station_id, electricity_strategy, add_diesel, screen_setting, utility_rate_plan, ack_peak_valley, heat_pump_setting, accuracy, evcharger_setting, version`

## `/charging_hes_svc/get_aiems_profit`

**queryLargeChargerAiEmsProfit** — *(no params extracted)*

## `/charging_hes_svc/get_auto_disaster_prepare_detail`

**getAutoDisasterPrepareDetail**
- Required: `unix`
- Optional: `station_id, near_field`

## `/charging_hes_svc/get_auto_disaster_prepare_status`

**getAutoDisasterPrepareStatus**
- Optional: `station_id`

## `/charging_hes_svc/get_current_disaster_prepare_details`

**getCurrentDisasterPrepareDetails** — *(no params extracted)*

## `/charging_hes_svc/get_device_command`

**getDeviceCommand**
- Required: `accuracy`
- Optional: `station_id`

## `/charging_hes_svc/get_device_product_info`

**getHesDeviceIcons** — *(no params extracted)*

## `/charging_hes_svc/get_heat_pump_plan_json`

**getHeatPumpTimePlan**
- Optional: `heat_pump_plan`

## `/charging_hes_svc/get_hes_dev_info`

**getHesDeviceList** — *(no params extracted)*

## `/charging_hes_svc/get_install_info`

**getDeviceInstallAddress** — *(no params extracted)*

## `/charging_hes_svc/get_installer_info`

**getInstallerInfo** — *(no params extracted)*

## `/charging_hes_svc/get_station_config_and_status`

**getA5101StationConfigDetail**
- Optional: `station_id`

## `/charging_hes_svc/get_station_evchargers`

**getX1BindChargerList** — *(no params extracted)*

## `/charging_hes_svc/get_system_running_time`

**getDeviceRunTime** — *(no params extracted)*

## `/charging_hes_svc/get_user_bind_and_not_in_station_evchargers`

**getX1BindUserUnbindChargerList** — *(no params extracted)*

## `/charging_hes_svc/get_vpp_check_code`

**getVppInfo**
- Required: `get_code, current_version`
- Optional: `station_id`

## `/charging_hes_svc/get_vpp_service_policy_by_agg_user`

**getVppDisclaimer**
- Optional: `current_version`

## `/charging_hes_svc/get_world_monetary_unit`

**getPriceUnits** — *(no params extracted)*

## `/charging_hes_svc/quit_auto_disaster_prepare`

**quitAutoDisasterPrepare**
- Required: `unix`
- Optional: `station_id, far_field`

## `/charging_hes_svc/restart_peak_session`

**deleteAndRestartPeakValley**
- Required: `far_field_model`
- Optional: `station_id`

## `/charging_hes_svc/set_station_evchargers`

**bindUnX1Charger** — *(no params extracted)*

## `/charging_hes_svc/update_hes_utility_rate_plan`

**updatePeakAndValley** — *(no params extracted)*

## `/charging_hes_svc/update_wifi_config`

**updateWiFiConfig**
- Required: `sn, rssi, encryption`
- Optional: `ssid`

## `/charging_hes_svc/user_event_alarm`

**reportHesEvents**
- Required: `pn, language, event`
- Optional: `station_id`

## `/charging_hes_svc/user_fault_alarm`

**sendDeviceReport** — *(no params extracted)*

## `/charging_pv_svc/getPvStatus`

**getPvStatus**
- Optional: `sns`

## `/charging_pv_svc/selectUserTieredElecPrice`

**selectUserTieredElecPrice**
- Optional: `sn`

## `/charging_pv_svc/updateUserTieredElecPrice`

**updateUserTieredElecPrice** — *(no params extracted)*

## `/mini_power/v1/app/charging/add_charging_mode`

**addCustomChargeMode**
- Required: `name, number, total_power, max_total_power, auto_exit, has_charge_protocol`
- Optional: `device_sn, power_settings`

## `/mini_power/v1/app/charging/delete_charging_mode`

**deleteCustomChargeMode**
- Optional: `id`

## `/mini_power/v1/app/charging/get_charging_mode_list`

**getCustomChargeModeList**
- Optional: `device_sn`

## `/mini_power/v1/app/charging/update_charging_mode`

**updateCustomChargeMode**
- Required: `name, total_power, max_total_power, auto_exit, has_charge_protocol`
- Optional: `id, power_settings`

## `/mini_power/v1/app/egg/get_easter_egg_trigger_list`

**getEasterEggRecord**
- Optional: `device_sn`

## `/mini_power/v1/app/egg/report_easter_egg_trigger_status`

**addEasterEggStatusRecord**
- Required: `egg_type`
- Optional: `device_sn, report_time`

## `/mini_power/v1/app/power/get_day_power_data`

**getDayPowerData**
- Required: `device_sn, date`
- Optional: `device_model`

## `/mini_power/v1/app/setting/get_charging_device_identity_new_status`

**getA2687StandardChargingDeviceModelIdentityStatus**
- Optional: `device_sn, charging_device_identity_new_status`

## `/mini_power/v1/app/setting/get_charging_device_identity_status_default_true`

**getA2345DeviceIdentityStatus**
- Optional: `device_sn, status`

## `/mini_power/v1/app/setting/get_device_setting`

**getCustomChargeModeSetting**
- Required: `compatibility_status, charging_device_identity_status`
- Optional: `device_sn, charging_mode_status`

## `/mini_power/v1/app/setting/get_port_remarks`

**getPortRemarks**
- Optional: `device_sn`

## `/mini_power/v1/app/setting/get_power_range_support_protocols`

**getPowerSupportProtocols**
- Optional: `device_model`

## `/mini_power/v1/app/setting/get_protocol_status`

**getA2687ProtocolAgreementStatus**
- Optional: `device_sn`

## `/mini_power/v1/app/setting/set_charging_device_identity_new_status`

**setA2687StandardChargingDeviceModelIdentityStatus**
- Required: `charging_device_identity_new_status`
- Optional: `device_sn`

## `/mini_power/v1/app/setting/set_charging_device_identity_status`

**setA2687ChargingDeviceModelIdentityStatus**
- Required: `charging_device_identity_status`
- Optional: `device_sn`

## `/mini_power/v1/app/setting/set_charging_device_identity_status_default_true`

**setA2345DeviceIdentityStatus**
- Required: `charging_device_identity_status_default_true`
- Optional: `device_sn`

## `/mini_power/v1/app/setting/set_charging_mode_status`

**saveCustomChargeModeSetting**
- Required: `charging_mode_status`
- Optional: `device_sn`

## `/mini_power/v1/app/setting/set_compatibility_status`

**saveCompatibilityStatusSetting**
- Required: `compatibility_status`
- Optional: `device_sn`

## `/mini_power/v1/app/setting/set_mode_sub_status`

**setA2687ModeSubStatus**
- Required: `mode, protocol_key, status`
- Optional: `device_sn`

## `/mini_power/v1/app/setting/set_port_remark`

**setPortRemark**
- Required: `port_name, remark`
- Optional: `device_sn`

## `/mini_power/v1/app/setting/set_protocol_status`

**setA2687ProtocolAgreementStatus**
- Required: `protocol_status`
- Optional: `device_sn`

## `/mini_power/v1/app/style/add_manual_clock_screensavers`

**addA2345CustomClockScreenSavers**
- Required: `img_url, hash_code`
- Optional: `sn`

## `/mini_power/v1/app/style/delete_manual_clock_screensavers`

**deleteA2345CustomClockScreenSavers**
- Optional: `id`

## `/mini_power/v1/app/style/get_clock_screensavers`

**getScreenSaversByCategory**
- Optional: `product_code`

**getA2345ClockScreenSavers**
- Optional: `product_code`

## `/mini_power/v1/app/style/get_manual_clock_screensavers`

**getA2345CustomClockScreenSavers**
- Optional: `sn`

## `/mini_power/v1/app/style/get_url`

**getA2345CustomClockScreenSaversRealUrl**
- Optional: `short_url`

## `/mini_power/v1/app/style/set_manual_clock_screensaver_name`

**editA2345CustomClockScreenSaversName**
- Required: `screensaver_id`
- Optional: `sn, name`

## `/power_service/v1/add_message`

**addMessage** — *(no params extracted)*

## `/power_service/v1/ai_ems/get_status`

**getAiModeStatusRequest**
- Optional: `site_id`

## `/power_service/v1/ai_ems/profit`

**getAiEmsProfit**
- Required: `start_time, end_time, type`
- Optional: `site_id`

## `/power_service/v1/app/after_sale/check_popup`

**checkDevicePopUpApi** — *(no params extracted)*

## `/power_service/v1/app/after_sale/get_popup`

**queryA17Y0Popup**
- Optional: `site_id`

## `/power_service/v1/app/check_upgrade_record`

**checkUpgradeRecord**
- Required: `type, type, type`
- Optional: `device_sn, device_sns`

## `/power_service/v1/app/compatible/check_third_sn`

**checkThirdSN**
- Required: `device_sn, brand_id`
- Optional: `device_model`

## `/power_service/v1/app/compatible/confirm_permissions_settings`

**getConfirmPermissionsSettingsApi**
- Required: `confirm_type`
- Optional: `device_model`

## `/power_service/v1/app/compatible/get_compatible_process`

**checkSolarForceUpdateState**
- Required: `solarbank_sn`
- Optional: `solar_sn`

## `/power_service/v1/app/compatible/get_confirm_permissions`

**getConfirmPermissionsApi**
- Optional: `device_model`

## `/power_service/v1/app/compatible/get_installation`

**getInstallationApi**
- Optional: `solarbank_sn, site_id`

## `/power_service/v1/app/compatible/get_ota_info`

**getThirdOtaInfo**
- Required: `solar_sn`
- Optional: `solar_bank_sn`

## `/power_service/v1/app/compatible/get_ota_update`

**getThirdOtaStatus**
- Required: `insert_sn`
- Optional: `device_sn`

## `/power_service/v1/app/compatible/installation_popup`

**getIncompatiblePopupApi**
- Optional: `site_id`

## `/power_service/v1/app/compatible/save_compatible_solar`

**saveCompatibleSolarApi** — *(no params extracted)*

## `/power_service/v1/app/compatible/save_ota_complete_status`

**saveThirdOtaInfo**
- Required: `ota_complete_status`
- Optional: `solarbank_sn`

## `/power_service/v1/app/compatible/set_installation`

**setInstallationApi**
- Required: `is_save, install_mode, is_save`
- Optional: `install_mode, site_id, solarbank_sn`

## `/power_service/v1/app/compatible/set_ota_update`

**setThirdOta**
- Required: `solar_pn, insert_sn, rollback_install_mode`
- Optional: `device_sn`

## `/power_service/v1/app/device/get_device_attrs`

**getDeviceAttrs**
- Required: `attributes`
- Optional: `device_sn, enable_0w_v2`

**getTouElectricAttrs**
- Required: `attributes`
- Optional: `device_sn`

## `/power_service/v1/app/device/get_device_home_load`

**getDeviceHomeLoadPort**
- Optional: `device_sn`

**getDeviceHomeLoadRes**
- Optional: `device_sn`

**get17C1DeviceHomeLoadPort**
- Required: `param_type, device_pn`
- Optional: `device_sn`

## `/power_service/v1/app/device/get_device_income`

**getTOUChartStatistics**
- Required: `type, start_time`
- Optional: `device_sn`

## `/power_service/v1/app/device/get_mes_device_info`

**getDeviceLaserSn**
- Optional: `device_sn`

## `/power_service/v1/app/device/get_relate_belong`

**getDeviceBindInfo**
- Optional: `device_sn`

## `/power_service/v1/app/device/remove_param_config_key`

**removeParamConfigKey**
- Required: `device_sn, remove_key, use_time`
- Optional: `site_id`

## `/power_service/v1/app/device/set_device_attrs`

**setDevicePowerOptionsReq**
- Required: `attributes`
- Optional: `device_sn`

**setDeviceGameStatus**
- Required: `attributes, init_status`
- Optional: `device_sn`

**setTouElectricAttrs**
- Required: `attributes, pps_use_time`
- Optional: `device_sn`

**getCurrencySetDeviceAttrs**
- Required: `attributes, currency`
- Optional: `device_sn`

**setSolarName**
- Required: `device_pn, attributes`
- Optional: `device_sn`

**setDeviceFeedGridSwitch**
- Required: `attributes, switch_0w`
- Optional: `device_sn`

**setDevicePvPowerOptionsReq**
- Required: `attributes, pv_power_limit`
- Optional: `device_sn`

**setLocationTag**
- Required: `attributes, tag`
- Optional: `device_sn`

**setPpsSolarName**
- Required: `device_pn, attributes`
- Optional: `device_sn`

## `/power_service/v1/app/device/set_device_home_load`

**setDeviceHomeLoadRes**
- Required: `home_load_data`
- Optional: `device_sn`

**set17C1DeviceHomeLoadRes**
- Required: `mode_type`
- Optional: `device_sn, custom_rate_plan, home_load_data`

## `/power_service/v1/app/get_annual_report`

**getAnnualReport** — *(no params extracted)*

## `/power_service/v1/app/get_auto_upgrade`

**getAutoUpgrade** — *(no params extracted)*

## `/power_service/v1/app/get_phonecode_list`

**sharePhoneCode** — *(no params extracted)*

## `/power_service/v1/app/get_relate_and_bind_devices`

**getDevicesList** — *(no params extracted)*

## `/power_service/v1/app/get_relate_device_fittings`

**getRelateAccessory**
- Optional: `device_sn`

## `/power_service/v1/app/get_token_by_userid`

**getAccessTokenByUserID**
- Optional: `user_id`

## `/power_service/v1/app/get_upgrade_record`

**getUpgradeRecord**
- Required: `device_sn`
- Optional: `type`

## `/power_service/v1/app/get_user_op_shelly_status`

**checkIsGrantedDeviceChanged**
- Optional: `token`

## `/power_service/v1/app/set_auto_upgrade`

**setAutoUpgrade** — *(no params extracted)*

## `/power_service/v1/app/share_site/delete_inviting_member`

**deleteInviteMember** — *(no params extracted)*

## `/power_service/v1/app/share_site/delete_site_member`

**deleteSiteMember** — *(no params extracted)*

## `/power_service/v1/app/share_site/get_invited_list`

**getInviteMember**
- Required: `status`
- Optional: `site_id`

## `/power_service/v1/app/share_site/invite_member`

**inviteMemberSite** — *(no params extracted)*

## `/power_service/v1/app/share_site/join_site`

**joinSite** — *(no params extracted)*

## `/power_service/v1/app/shelly_ctrl_device`

**changeShellyDeviceStatus**
- Required: `op_type, toggle, value`
- Optional: `device_sn`

## `/power_service/v1/app/third/platform/list`

**getThirdPartyPlatformList**
- Required: `anker_power`
- Optional: `app_id`

## `/power_service/v1/app/upgrade_event_report`

**getReportBleUpgrade**
- Required: `device_pn, device_type, upgrade_type, after_version, before_version, upgrade_time, site_id`
- Optional: `device_sn`

## `/power_service/v1/app/upgrade_event_reports`

**getReportsBleUpgrade**
- Optional: `upgrade_even_device_infos`

## `/power_service/v1/app/whitelist/feature/check`

**getWhiteListStatusRes**
- Required: `feature_code, product_code`
- Optional: `check_list`

## `/power_service/v1/currency/get_list`

**getCurrencyGetList**
- Optional: `counrty`

## `/power_service/v1/del_message`

**delMessage** — *(no params extracted)*

## `/power_service/v1/dynamic_price/check_available`

**postHasChangeCountry** — *(no params extracted)*

## `/power_service/v1/dynamic_price/price_detail`

**getDynamicPriceDetail**
- Required: `area, date, device_sn`
- Optional: `company`

## `/power_service/v1/dynamic_price/support_option`

**getDynamicPriceSupportOption**
- Required: `device_pn`
- Optional: `site_id`

## `/power_service/v1/get_all_service_config`

**getAllQaEnvConfig** — *(no params extracted)*

## `/power_service/v1/get_message`

**getMessage**
- Required: `message_type`
- Optional: `last_time, device_sns, limit, last_msg_id`

## `/power_service/v1/get_message_not_disturb`

**getMessageDisturb** — *(no params extracted)*

## `/power_service/v1/get_message_sn_list`

**getMessageSnList** — *(no params extracted)*

## `/power_service/v1/get_message_unread`

**getMessageUnread** — *(no params extracted)*

## `/power_service/v1/message_not_disturb`

**setEvChargerPushMessage**
- Required: `start_charging, stop_charging, paused_charging, paused_car_charging, restore_charging, smart_charging, boost_charging`
- Optional: `disturb_scenes`

**setMessageDisturb**
- Optional: `start_time, end_time, disturb_switch`

## `/power_service/v1/product_accessories`

**getProductAccessories** — *(no params extracted)*

## `/power_service/v1/product_categories`

**getProductCategories** — *(no params extracted)*

## `/power_service/v1/read_message`

**setMessageRead** — *(no params extracted)*

## `/power_service/v1/site/add_charging_device`

**addChargingDevice** — *(no params extracted)*

## `/power_service/v1/site/add_site_devices`

**multiAddDeviceInfo** — *(no params extracted)*

## `/power_service/v1/site/can_create_site`

**checkCanCreateSite** — *(no params extracted)*

## `/power_service/v1/site/co2_ranking`

**queryRankingInfo**
- Optional: `site_id`

## `/power_service/v1/site/create_site`

**createSiteRequest**
- Required: `site_img, solar_list`
- Optional: `site_name, pps_list, solarbank_list, home_backup_system_list, powerpanel_list, grid_list, solarbank_pps_list, smartplug_list, combiner_box_list, charging_pile_list`

## `/power_service/v1/site/delete_charging_device`

**deleteChargingDevice** — *(no params extracted)*

## `/power_service/v1/site/delete_site`

**deleteSite** — *(no params extracted)*

## `/power_service/v1/site/delete_site_devices`

**deleteSitePPSRequest** — *(no params extracted)*

## `/power_service/v1/site/get_addable_site_list`

**getAddableSiteList**
- Required: `device_model, device_model`
- Optional: `device_sn`

## `/power_service/v1/site/get_charging_device`

**getChargingDeviceRequest** — *(no params extracted)*

## `/power_service/v1/site/get_comb_addable_sites`

**getDeviceJoinSiteList**
- Optional: `devices`

## `/power_service/v1/site/get_home_load_chart`

**getSiteHomeLoadChat**
- Required: `device_sn`
- Optional: `site_id`

## `/power_service/v1/site/get_power_limit`

**getSitePowerLimit**
- Optional: `site_id`

## `/power_service/v1/site/get_scen_info`

**querySceneInfo**
- Optional: `site_id`

## `/power_service/v1/site/get_schedule`

**getSiteSchedule**
- Optional: `site_id`

**queryBasicStatus**
- Optional: `site_id`

## `/power_service/v1/site/get_site_detail`

**getStationDetail**
- Optional: `site_id`

**getGreenPPSSiteDetail**
- Optional: `site_id`

**getRemainPluginsDetails**
- Optional: `site_id`

## `/power_service/v1/site/get_site_device_param`

**getSafetySocParams**
- Required: `param_type`
- Optional: `site_id`

**getCombineBoxListData**
- Required: `param_type`
- Optional: `site_id`

**getThreePvParam**
- Required: `param_type, cmd`
- Optional: `site_id`

**getStationCountryCode**
- Required: `param_type`
- Optional: `site_id`

**getSitePeakTimeDeviceParam**
- Required: `param_type`
- Optional: `site_id`

**get17C1SiteDeviceParam**
- Required: `param_type, cmd, device_sn`
- Optional: `site_id, parallel_type`

**getSiteDeviceParam**
- Required: `param_type`
- Optional: `site_id`

**getSiteEnablePeakDeviceParam**
- Required: `param_type`
- Optional: `site_id`

**getSiteLowerLimitDeviceParam**
- Required: `param_type`
- Optional: `site_id`

**getSiteGreenModeDeviceParam**
- Required: `param_type`
- Optional: `site_id`

## `/power_service/v1/site/get_site_list`

**getUserSiteList** — *(no params extracted)*

## `/power_service/v1/site/get_site_price`

**getSitePriceRequest**
- Required: `accuracy`
- Optional: `site_id`

## `/power_service/v1/site/get_site_rules`

**getSiteRules** — *(no params extracted)*

## `/power_service/v1/site/get_wifi_info_list`

**getSiteWifiInfoRequest** — *(no params extracted)*

## `/power_service/v1/site/list_user_devices`

**getUserPPSDevice**
- Optional: `device_models`

## `/power_service/v1/site/local_net`

**selfCheckNetwork**
- Optional: `list`

## `/power_service/v1/site/reset_charging_device`

**resetChargingDevice** — *(no params extracted)*

## `/power_service/v1/site/set_device_feature`

**setRemainPluginStatus** — *(no params extracted)*

## `/power_service/v1/site/set_site_device_param`

**set17C1SiteDeviceParam**
- Required: `param_type, cmd, device_sn`
- Optional: `site_id, param_data`

**setSafetySocParams**
- Required: `site_id, param_type, param_data`
- Optional: `cmd`

**setSiteDeviceParam**
- Required: `param_type, cmd, param_data`
- Optional: `site_id`

**setStationCountryCode**
- Required: `param_type, cmd, param_data`
- Optional: `site_id`

**setDynamicPrice**
- Required: `param_type, cmd, param_data`
- Optional: `site_id`

**setThreePvInstallSwitch**
- Required: `param_type, cmd, param_data`
- Optional: `site_id`

**setSiteDevicePowerLimit**
- Required: `limit, param_type, cmd, param_data`
- Optional: `power_limit, limit_real, site_id`

## `/power_service/v1/site/shift_power_site_type`

**shiftPowerSite**
- Required: `power_site_type`
- Optional: `site_id`

## `/power_service/v1/site/update_charging_device`

**updateChargingDevice** — *(no params extracted)*

## `/power_service/v1/site/update_site`

**updateSiteNameInfoRequest** — *(no params extracted)*

## `/power_service/v1/site/update_site_devices`

**updateSiteDevices**
- Required: `pps_list`
- Optional: `site_id`

## `/power_service/v1/site/update_site_price`

**updateSitePriceRequest**
- Required: `price`
- Optional: `site_id, site_co2, site_price_unit, price_type, current_mode, accuracy`

