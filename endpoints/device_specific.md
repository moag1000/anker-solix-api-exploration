# Device-Specific Endpoints

> Endpoints discovered in device logic files, NOT in `http_request_repository_impl.dart`.
> These are called directly from device UI/logic code and were missed in the initial extraction.
>
> **Device tags**: `[A5190]` = EV Charger, `[A7320]` = Generator/Oil Engine,
> `[A5101]` = HES/X1, `[A5140]` = Solarbank/PV, `[A5150]` = ECU/MI,
> `[A17B1]` = System, `[A1782]` = Station, `[AX170]` = ATS Station,
> `[A17EX]` = Micro HES, `[AE100]` = Balcony
>
> **Priority** (based on community demand in thomluther/ha-anker-solix issues):
>
> | Priority | Devices | Community Issues | Rationale |
> |----------|---------|-----------------|-----------|
> | **P1 — Core** | Solarbank 2/3 (A17C1/C5), Smart Plug (A17X8), Smart Meter | 70+ | Largest user base (EU balcony solar) |
> | **P2 — High demand** | EV Charger (A5191), E10 Home Backup (A17E1), X1 HES (A5101) | 20+ | Actively requested, growing user base |
> | **P3 — Niche** | PPS (F3800/C1000/C2000), Generator (A7320), Prime Charger (A2345) | 15+ | Legitimate demand, fewer users |
> | **P4 — Low demand** | EverFrost Cooler, standalone Microinverter, AIOT, Anka AI | 1-2 | Minimal demand or covered via parent device |
>
> All Anker Solix devices are consumer products. X1 HES requires certified installer
> but is owned by end users. No purely commercial/industrial devices exist in the lineup.

---

## EV Charger Endpoints `[A5190]` — P2

### Vehicle Management
- `/power_service/v1/app/vehicle/get_vehicle_list` — **getEvList**
- `/power_service/v1/app/vehicle/add_vehicle` — **addEv**(`user_vehicle_info`)
- `/power_service/v1/app/vehicle/delete_vehicle` — **deleteEv**(`vehicle_id`)
- `/power_service/v1/app/vehicle/set_default` — **setDefaultEv**(`vehicle_id`)
- `/power_service/v1/app/vehicle/get_vehicle_detail` — **getEvDetail**(`vehicle_id`)
- `/power_service/v1/app/vehicle/update_vehicle` — **updateEv**
- `/power_service/v1/app/vehicle/set_charging_vehicle` — **setChargingVehicle**(`vehicle_id`)
- `/power_service/v1/app/get_brand_list` — **getEvBrandList**
- `/power_service/v1/app/get_model_list` — **getEvVersionList**
- `/power_service/v1/app/get_model_years` — **getEvYearList**
- `/power_service/v1/app/get_models` — **getEvModelList**

### Charging Sessions / Orders
- `/power_service/v1/app/order/get_charge_order_stats_list` — **getChargerSessionOrderList**(`order_status`)
- `/power_service/v1/app/order/get_charge_order_stats` — **getChargeSessionChartModel**
- `/power_service/v1/app/order/export_charge_order` — **fetchExportChargeOrderUrl**
- `/power_service/v1/app/order/get_charging_order_sec_preview` — **getSessionsOrderSecPreview**(`order_id`)
- `/power_service/v1/app/order/get_charging_order_detail` — **getSessionsDetail**
- `/power_service/v1/app/order/get_charging_order_list` — **getChargeSessions**(`order_status`)
- `/power_service/v1/app/order/get_charging_order_sec_detail` — **getSessionsOrderSecDetail**(`order_id`)
- `/power_service/v1/app/order/delete_charging_order` — **deleteChargingSession**(`order_id`) [SET]

### RFID Card Management
- `/power_service/v1/rfid/save_device_card` — **saveDeviceCard** [SET]
- `/power_service/v1/rfid/get_device_cards` — **getDeviceCards**
- `/power_service/v1/rfid/delete_device_card` — **deleteDeviceCard** [SET]

### Device Groups
- `/power_service/v1/app/group/get_group_devices` — **getGroupDevices**(`sub_sn`)
- `/power_service/v1/app/group/save_group_devices` — **saveGroupDevices** [SET]
- `/power_service/v1/app/group/force_save_group_devices` — **forceSaveGroupDevices** [SET]
- `/power_service/v1/app/group/replace_group_devices` — **updateGroupDevices** [SET]
- `/power_service/v1/app/group/delete_group_devices` — **deleteGroupDevices** [SET]

### OCPP
- `/power_service/v1/app/get_ocpp_endpoint_list` — **getOcppEndpointList**
- `/power_service/v1/app/get_ocpp_info` — **getOcppInfo**(`device_sn, address`)

### Security
- `/power_service/v1/device/get_tamper_records` — **getSecurityLogs**
- `/power_service/v1/site/get_site_detail_by_sn` — **getEvChargerSiteInfo**(`device_sn`)

### Sharing
- `/app/devicerelation/get_shared_device` — **getDeviceShareList**(`device_sn, status`)
- `/app/devicerelation/ignore_invite` — **ignoreInvite**(`invite_id, device_sn, recevicer_user_id, invites, is_inviter`) [SET]
- `/app/devicerelation/confirm_invite` — **confirmInvite**(`invites, invite_id, device_sn`) [SET]
- `/app/devicerelation/device_invite` — **deviceInvite**(`email, phone, phone_code, nick_name, invites, member_type, device_sn`) [SET]
- `/app/devicerelation/update_share` — **deleteDeviceShareMember**(`user_id, devices{device_sn, sub_devices}, is_delete, member_type`) [SET]

### HES Integration
- `/charging_hes_svc/set_evcharger_station_feature` — **setEvChargerStationFeature** [SET]
- `/charging_hes_svc/share_device/invite_installer_member` — **shareDeviceInstallerInvite**(`installerEmail, deviceSnList`) [SET]
- `/charging_hes_svc/share_device/get_installer_invited_list` — **getDeviceShareInstallerList**(`deviceSn`)
- `/charging_hes_svc/share_device/delete_installer_inviting_member` — **deleteInstallerInvite**(`installerUserId, deviceSn`) [SET]

### Fault/Messaging
- `/charging_imsg_svc/user_fault_alarm` — **userFaultAlarm** [SET]
- `/charging_imsg_svc/remove_user_floating_fault_info` — **removeUserFloatingFaultInfo** [SET]

---

## Generator / Oil Engine Endpoints `[A7320]` — P3

### Extender System CRUD
- `/power_service/v1/app/add_extender_system` — **addExtenderSystem** [SET]
- `/power_service/v1/app/del_extender_system` — **delExtenderSystem** [SET]
- `/power_service/v1/app/get_extender_system_list` — **getExtenderSystemList**
- `/power_service/v1/app/get_extender_system_detail` — **getExtenderSystemDetail**
- `/power_service/v1/app/set_extender_system_name` — **setExtenderSystemName** [SET]
- `/power_service/v1/app/update_extender_system_strategy` — **updateExtenderSystemStrategy** [SET]
- `/power_service/v1/app/get_extender_system_pn_ota` — **getExtenderSystemPnOta**
- `/power_service/v1/app/get_strategy_last_record` — **getStrategyLastRecord**

### Extender System Devices
- `/power_service/v1/app/add_extender_system_device_list` — **addExtenderSystemDeviceList** [SET]
- `/power_service/v1/app/batch_add_extender_system_device` — **batchAddExtenderSystemDevice** [SET]
- `/power_service/v1/app/batch_del_extender_system_device` — **batchDelExtenderSystemDevice** [SET]
- `/power_service/v1/app/get_device_bind_details` — **getDeviceBindDetails**
- `/power_service/v1/app/set_extender_system_cumulative_data` — **setExtenderSystemCumulativeData** [SET]
- `/power_service/v1/app/get_extender_system_cumulative_data` — **getExtenderSystemCumulativeData**

### Oil Engine Maintenance
- `/power_service/v1/app/set_oil_consumption_reminder_plan` — **setOilConsumptionReminderPlan** [SET]
- `/power_service/v1/app/get_oil_consumption_reminder_plan_details` — **getOilConsumptionReminderPlanDetails**
- `/power_service/v1/app/set_oil_consumption_reminder_switch` — **setOilConsumptionReminderSwitch** [SET]
- `/power_service/v1/app/set_oil_machine_exercise_plan` — **setOilMachineExercisePlan** [SET]
- `/power_service/v1/app/start_oil_machine_exercise` — **startOilMachineExercise** [SET]
- `/power_service/v1/app/switch_exercise_mode` — **switchExerciseMode** [SET]
- `/power_service/v1/app/get_device_exercise_details` — **getDeviceExerciseDetails**
- `/power_service/v1/app/get_device_last_exercise_log` — **getDeviceLastExerciseLog**
- `/power_service/v1/app/get_device_exercise_log` — **getDeviceExerciseLog**

### Parts Maintenance
- `/power_service/v1/app/get_parts_maintenance_plan` — **getPartsMaintenancePlan**
- `/power_service/v1/app/set_parts_maintenance_plan` — **setPartsMaintenancePlan** [SET]
- `/power_service/v1/app/get_parts_maintenance_logs` — **getPartsMaintenanceLogs**
- `/power_service/v1/app/batch_maintain_oil_engine_parts` — **batchMaintainOilEngineParts** [SET]
- `/power_service/v1/app/set_maintain_parts_ignore_reminders` — **setMaintainPartsIgnoreReminders** [SET]
- `/power_service/v1/app/set_maintain_parts_notice_switch` — **setMaintainPartsNoticeSwitch** [SET]

---

## HES / X1 Endpoints `[A5101]` — P2

- `/charging_hes_svc/get_device_card_details` — **getDeviceDetails**(`station_id, device_type, device_sn`)
- `/charging_hes_svc/get_device_card_list` — **getDeviceCardList**
- `/charging_hes_svc/get_system_profit_detail` — **getSystemProfitDetail**
- `/charging_hes_svc/check_device_bluetooth_password` — **checkBluetoothPassword**
- `/charging_hes_svc/device_self_check` — **deviceSelfCheck** [SET]
- `/charging_hes_svc/get_device_self_check` — **getDeviceSelfCheck**
- `/charging_hes_svc/get_external_device_config` — **getExternalDeviceConfig**
- `/charging_hes_svc/get_system_device_time` — **getSystemDeviceTime**
- `/charging_hes_svc/get_electric_utility_and_electric_plan_list` — **getElectricUtilityAndPlanList**
- `/charging_hes_svc/get_tou_price_plan_detail` — **getTouPricePlanDetail**
- `/charging_hes_svc/get_utility_rate_plans` — **getUtilityRatePlans**
- `/charging_hes_svc/authorize_aiems` — **authorizeAiems** [SET]
- `/charging_hes_svc/enable_aiems_mode` — **enableAiemsMode** [SET]
- `/charging_hes_svc/start` — **remoteStart** [SET]
- `/charging_hes_svc/get_device_pn_info` — **getDevicePnInfo**
- `/charging_hes_svc/get_wifi_info` — **getWifiInfo**
- `/charging_hes_svc/get_energy_statistics` — **getEnergyStatistics**
- `/charging_hes_svc/download_energy_statistics` — **downloadEnergyStatistics**
- `/charging_hes_svc/check_update` — **checkUpdate**
- `/charging_hes_svc/cancel_pop` — **cancelPop** [SET]
- `/charging_hes_svc/update_device_info_by_app` — **updateDeviceInfoByApp** [SET]
- `/charging_hes_svc/ota` — **hesOta** [SET]
- `/charging_hes_svc/get_back_up_history` — **getBackUpHistory**
- `/charging_hes_svc/sync_back_up_history` — **syncBackUpHistory** [SET]
- `/charging_hes_svc/get_system_running_info` — **getSystemRunningInfo**
- `/charging_hes_svc/report_device_data` — **reportDeviceData** [SET]
- `/charging_hes_svc/get_conn_net_tips` — **getConnNetTips**
- `/charging_hes_svc/get_site_mi_list` — **getSiteMiList**
- `/charging_hes_svc/get_user_fault_info` — **getUserFaultInfo**
- `/charging_hes_svc/remove_user_fault_info` — **removeUserFaultInfo** [SET]
- `/charging_hes_svc/upload_device_status` — **uploadDeviceStatus** [SET]

---

## Dynamic Pricing Endpoints (cross-device) — P2

- `/charging_hes_dynamic_price_svc/get_area_by_code` — **getAreaByCode**
- `/charging_hes_dynamic_price_svc/get_price_company` — **getPriceCompany**
- `/charging_hes_dynamic_price_svc/get_third_jump_url` — **getThirdJumpUrl**
- `/charging_hes_dynamic_price_svc/save_dynamic_price` — **saveDynamicPrice**(`setMode, sn?, siteId?`) [SET]
- `/charging_hes_dynamic_price_svc/save_time_of_use` — **saveTimeOfUse**(`setMode, touType, sn?, siteId?`) [SET]
- `/charging_hes_dynamic_price_svc/get_price` — **getPrice**

---

## Disaster Preparedness / Storm Guard Endpoints (cross-device) — P2

- `/charging_disaster_prepared/get_site_device_disaster` — **getDisaster**
- `/charging_disaster_prepared/get_site_device_disaster_status` — **getDisasterStatus**
- `/charging_disaster_prepared/get_support_func` — **getSupportFunc**
- `/charging_disaster_prepared/set_site_device_disaster` — **setDisaster** [SET]
- `/charging_disaster_prepared/quit_disaster_prepare` — **quitDisasterPrepare** [SET]
- `/charging_disaster_prepared/clear` — **clearDisaster** [SET] `[A1782]`

---

## Location Management (cross-device) — P3

- `/charging_common_svc/location/set` — **locationSet** [SET]
- `/charging_common_svc/location/get` — **locationGet**

---

## Anka AI Agent — not relevant for HA integration

> App-internal AI chat feature, no device control or energy data value.

- `/smart_service/v1/app/anka/get_entry_config` — **getEntryConfig**
- `/smart_service/v1/app/anka/get_menu_config` — **getMenuConfig**
- `/smart_service/v1/app/anka/set_entry_switch` — **setEntrySwitch** [SET]
- `/app/ai/anka` — **ankaChatApi** [SET]

---

## v2 API Endpoints — P3

- `/power_service/v2/site/platform_energy_analysis_options` — **platformEnergyAnalysisOptions** `[AX170]`
- `/power_service/v2/app/get_custom_branch_icon` — **getCustomBranchIcon** `[AX170]`
- `/power_service/v2/app/set_device_pv_name` — **setDevicePvName** [SET] `[AX170]`
- `/power_service/v2/platform_get_pn_region_code` — **getPnRegionCode** `[A17EX]`
- `/power_service/v2/app/get_hardware_relation` — **getHardwareRelation**

---

## AIOT System (separate API platform) — not relevant for HA integration

> Marketing popup system for in-app promotions. No device or energy data.

> Uses different auth/encryption (Openudid header, no standard encryption)

- `/app/news/get_popups` — **getAIOTPopupListApi** → `AIOTPopupModel`
- `/app/news/popup_record` — **reportAIOTPopupApi**(`popup_id, popup_name, popup_type`) [SET]

---

## Other Utility Endpoints — P3/P4

- `/power_service/v1/site/energy_analysis` — **energyAnalysis** `[A1782]`
- `/power_service/v1/site/site_data_check` — **siteDataCheck**
- `/power_service/v1/site/site_data_exported` — **siteDataExported**
- `/power_service/v1/app/after_sale/check_sn` — **afterSalesCheckSn**
- `/power_service/v1/app/after_sale/mark_sn` — **afterSaleMarkSn**(`after_sale_type=2, device_sns, mark_type=2`) [SET]
- `/power_service/v1/app/share_site/anonymous_join_site` — **anonymousJoinSite**
- `/power_service/v1/app/user/get_user_params` — **getUserParams** `[A5190]`
- `/power_service/v1/app/user/set_user_params` — **setUserParams** [SET] `[A5190]`
- `/power_service/v1/dynamic_price/check_adjust` — **checkAdjust**
- `/charging_pv_svc/getPvTotalStatistics` — **getPvTotalStatistics** `[A5140]`
- `/charging_pv_svc/statisticsPv` — **statisticsPv** `[A5140]`
- `/charging_pv_svc/getMiStatus` — **getMiStatus** `[A5150]`
- `/charging_hes_svc/get_mi_layout` — **getMiLayout** `[A5150]`
- `/charging_energy_service/get_utility_rate_plan` — **getUtilityRatePlan** `[A17B1]`
- `/charging_energy_service/get_sns` — **getSns** `[A17B1]`
- `/charging_energy_service/energy_statistics` — **energyStatistics**
- `/charging_energy_service/get_system_running_info` — **getSystemRunningInfo**
- `/charging_energy_service/report_device_data` — **reportDeviceData** [SET]
