> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Models

This directory holds response and request model pages, one per class or group, which own the field lists. The 13 legacy group pages are rebuilt in place per the migration map; classes that already have a dedicated page are owned by that page and the legacy section carries a pointer.

Not here: which endpoint returns a model (see [../api/README.md](../api/README.md)); owner map in [../docs/STRUCTURE.md](../docs/STRUCTURE.md); the `param_type` to model mapping in [../api/param_types.md](../api/param_types.md).

## Dedicated model pages (template layout)

- [a5190_device_info.md](a5190_device_info.md): `A5190DeviceInfo`, the EV charger device state (Modbus TCP keys only).
- [combine_box_entity.md](combine_box_entity.md): `CombineBoxEntity`, combiner box serial and image (`param_type` 16).
- [feed_grid_setting_param.md](feed_grid_setting_param.md): `FeedGridSettingParam` and `FeedTimes`, two variants for `param_type` 28 and 18.
- [feed_net_work_limit_entity.md](feed_net_work_limit_entity.md): `FeedNetWorkLimitEntity`, the cached UI state of the old feed-limit page.
- [get_site_device_param_response.md](get_site_device_param_response.md): `GetSiteDeviceParamResponse`, `SiteDeviceParamData`, `SiteSocItem`, `FeedTimes` and the request object `SetSiteDeviceParamData` (`param_type` 18, 26).
- [grid_overload_auto_reduce_param.md](grid_overload_auto_reduce_param.md): `GridOverloadAutoReduceParam` (`param_type` 37).
- [heat_pump_param.md](heat_pump_param.md): `HeatPumpParam` and `Params` (`param_type` 24).
- [hw_feed_grid_setting_param.md](hw_feed_grid_setting_param.md): `HwFeedGridSettingParam`, hardware anti-backflow (`param_type` 31).
- [location_support_country_code.md](location_support_country_code.md): `LocationSupportCountryCode` and its container `LocationSupportFunc` (location feature, not `param_type` 20).
- [peak_shaving_setting_param.md](peak_shaving_setting_param.md): `PeakShavingSettingParam` (`param_type` 30).
- [peak_time_model.md](peak_time_model.md): `PeakTimeModel` and `Data`, the peak-time plan (`param_type` 2).
- [site_device_param_response.md](site_device_param_response.md): `SiteDeviceParamResponse`, the TOU response of the electricity-price module (`param_type` 6).
- [soc_setting_param.md](soc_setting_param.md): `SocSettingParam`, SOC limits (`param_type` 27).
- [soc_settings.md](soc_settings.md): `SocSettings`, the SOC limits reported by the device through the IoT kit (not a cloud response).
- [station_power_limit.md](station_power_limit.md): `StationPowerLimitModel` and its element classes (`get_power_limit`).

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
