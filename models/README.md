> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Models

This directory holds response and request model pages, one per class or group, which own the field lists. The 13 legacy group pages are rebuilt in place per the migration map; classes that already have a dedicated page are owned by that page and the legacy section carries a pointer.

Not here: which endpoint returns a model (see [../api/README.md](../api/README.md)); owner map in [../docs/STRUCTURE.md](../docs/STRUCTURE.md); the `param_type` to model mapping in [../api/param_types.md](../api/param_types.md).

## Dedicated model pages (template layout)

- [a5190_device_info.md](a5190_device_info.md): `A5190DeviceInfo`, the EV charger device state (Modbus TCP keys only).
- [combine_box_entity.md](combine_box_entity.md): `CombineBoxEntity`, combiner box serial and image (`param_type` 16).
- [dynamic_price_company_model.md](dynamic_price_company_model.md): `DynamicPriceCompanyModel` and its provider classes, the answer of `get_price_company` (installer service).
- [dynamic_price_server_model.md](dynamic_price_server_model.md): `ThirdJumpModel`, `SaveDynamicPriceResponse` and `FlatpeakSetting`, the Tibber/Flatpeak setup answers.
- [electricity_price_model.md](electricity_price_model.md): `ElectricityPriceModel`, `TouPrice` and `DynamicPrice`, the answer of `get_price` (installer service).
- [feed_grid_setting_param.md](feed_grid_setting_param.md): `FeedGridSettingParam` and `FeedTimes`, two variants for `param_type` 28 and 18.
- [feed_net_work_limit_entity.md](feed_net_work_limit_entity.md): `FeedNetWorkLimitEntity`, the cached UI state of the old feed-limit page.
- [get_site_device_param_response.md](get_site_device_param_response.md): `GetSiteDeviceParamResponse`, `SiteDeviceParamData`, `SiteSocItem`, `FeedTimes` and the request object `SetSiteDeviceParamData` (`param_type` 18, 26).
- [grid_code_model.md](grid_code_model.md): `GridCodeModel`, the region and grid code catalogue (`platform_get_pn_region_code`).
- [grid_overload_auto_reduce_param.md](grid_overload_auto_reduce_param.md): `GridOverloadAutoReduceParam` (`param_type` 37).
- [grid_param_setting_info.md](grid_param_setting_info.md): `GridParamSettingInfo`, the grid code settings (`platform_get_user_region_param`).
- [heat_pump_param.md](heat_pump_param.md): `HeatPumpParam` and `Params` (`param_type` 24).
- [hw_feed_grid_setting_param.md](hw_feed_grid_setting_param.md): `HwFeedGridSettingParam`, hardware anti-backflow (`param_type` 31).
- [income_detail_model.md](income_detail_model.md): `IncomeDetailModel` and `A17e2BenifitsModel`, the answer of `platform_get_site_savings`.
- [location_support_country_code.md](location_support_country_code.md): `LocationSupportCountryCode` and its container `LocationSupportFunc` (location feature, not `param_type` 20).
- [meter_energy_analysis_model.md](meter_energy_analysis_model.md): `MeterEnergyAnalysisModel`, the AE1X0 meter history chart (`v2/device/energy_analysis`).
- [peak_shaving_setting_param.md](peak_shaving_setting_param.md): `PeakShavingSettingParam` (`param_type` 30).
- [peak_time_model.md](peak_time_model.md): `PeakTimeModel` and `Data`, the peak-time plan (`param_type` 2).
- [s1_s2_charger_session_chart_model.md](s1_s2_charger_session_chart_model.md): `S1S2ChargerSessionChartModel`, the S1/S2 charge-session chart (`v2/device/energy_analysis`).
- [scene_info_model.md](scene_info_model.md): `SceneInfoModel`, the IoT kit scene document (`platform_get_site_scene`).
- [site_device_param_response.md](site_device_param_response.md): `SiteDeviceParamResponse`, the TOU response of the electricity-price module (`param_type` 6).
- [site_sn_relation_list.md](site_sn_relation_list.md): `SiteSnRelationList`, the answer of `get_hardware_relation`.
- [soc_setting_param.md](soc_setting_param.md): `SocSettingParam`, SOC limits (`param_type` 27).
- [soc_settings.md](soc_settings.md): `SocSettings`, the SOC limits reported by the device through the IoT kit (not a cloud response).
- [station_power_limit.md](station_power_limit.md): `StationPowerLimitModel` and its element classes (`get_power_limit`).
- [utility_rate_plans_response.md](utility_rate_plans_response.md): `UtilityRatePlansResponse`, the answer of `get_utility_rate_plans` in the new TOU flow.
- [weather_models.md](weather_models.md): `WeatherApiResult` and `WeatherResponseData`, the answer of `get_weather`.

## Legacy group pages (to be rebuilt)

- [account.md](account.md): account and site-member models (`UserModel`, `IotUserModel`, `UserSiteListModel`, ...).
- [charger.md](charger.md): charger models (`A2345CustomModeList`, `PowerRangeProtocolsResponse`, ...).
- [connectivity.md](connectivity.md): Wi-Fi and installation models (`WifiInfoModel`, `SiteWifiInfoModel`, ...).
- [device.md](device.md): device list models (`DeviceModel`, `DeviceListModel`, `DeviceInfosModel`).
- [energy.md](energy.md): energy scene models (`SceneInfo`, `GreenPPSSiteDetailModel`, ...).
- [firmware.md](firmware.md): firmware and OTA models (`FirmwareUpdateModel`, `OtaUpdateModel`, ...).
- [hes.md](hes.md): HES / X1 models (`A5101DeviceCommandModel`, `A5101DeviceListModel`, ...).
- [other.md](other.md): models without a group (`StationModel`, `SiteScheduleModel`, `BannerModel`, ...); `CombineBoxEntity` and `PeakTimeModel` moved out.
- [power.md](power.md): `DevicePowerLimit` (the `StationPowerLimitModel` section points to its dedicated page).
- [pps.md](pps.md): portable power station models (`A1340ChargingDeviceData`, `A5140DeviceStatus`).
- [pricing.md](pricing.md): tariff and price models (`SitePriceModel`, `DynamicPriceDetailModel`, ...).
- [products.md](products.md): product catalogue models (`BrandModel`, `ProductCategoriesModel`, `ConfirmModel`).
- [solarbank.md](solarbank.md): Solarbank schedule models (`SiteHomeLoadModel`, `SiteConsumptionStrategyModel`, ...); `GetSiteDeviceParamResponse` and `SiteDeviceParamData` moved out.
