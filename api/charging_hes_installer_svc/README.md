> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# charging_hes_installer_svc

Service index for the URL prefix `/charging_hes_installer_svc/`. Each endpoint page is the single owner of its request, response and tags; a skeleton page (status "skeleton", purpose TODO) carries only what `data/endpoints.json` knows and has `Confidence: string-only` until a human reads the asm. Upstream keys are `API_ENDPOINTS` keys of `api/apitypes.py`.

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/charging_hes_installer_svc/adjust_station_price_unit`](adjust_station_price_unit.md) | Tells the cloud to change the price unit (currency) of a station's electricity prices; the app sends the station id and the new unit and reads nothing from the answer. | - | owner |
| [`/charging_hes_installer_svc/authorize_aiems`](authorize_aiems.md) | Authorizes the AI EMS (AI energy management) of a site in the cloud; the app sends the site id and, on success, marks the site as authorized and closes the current page. | - | owner |
| [`/charging_hes_installer_svc/check_function`](check_function.md) | Asks the cloud whether the EMS (energy management) function of a system is switched off (`ems_disable`); the app uses the answer to update the VPP (virtual power plant) state of the station home screen. | - | owner |
| [`/charging_hes_installer_svc/edit_system_strategy`](edit_system_strategy.md) | Sends a device command that edits the system strategy of a large (HES) station; the only traced sender, the new TOU flow, uses it to save the peak sessions and the price unit of a time-of-use plan. | - | owner |
| [`/charging_hes_installer_svc/enable_aiems_mode`](enable_aiems_mode.md) | Switches the AI EMS mode (the "smart mode" of a large HES system) on for a site; on success the app opens the smart-mode start-success page. | - | owner |
| [`/charging_hes_installer_svc/get_area_by_code`](get_area_by_code.md) | Looks up the price area (Octopus group id) that belongs to an area code of a site; the dynamic-price provider page uses it to find the matching Octopus region. | - | owner |
| [`/charging_hes_installer_svc/get_history_setting`](get_history_setting.md) | Reads the history of the TOU (time-of-use) schedule settings of a large (HES) station, i.e. which price mode was last set; the price settings pages use it to decide whether a manual or an automatic TOU mode is already configured. | - | owner |
| [`/charging_hes_installer_svc/get_price`](get_price.md) | Reads the price table of a site for one provider: the time-of-use price seasons or the dynamic hourly prices of today and tomorrow; the price preview and time-slot pages use it to draw the prices. | - | owner |
| [`/charging_hes_installer_svc/get_price_company`](get_price_company.md) | Reads the list of dynamic-price and time-slot providers (companies) available for a product or site, with the provider the user has already selected; it is the first call of the dynamic-price and time-of-use setup pages. | - | owner |
| [`/charging_hes_installer_svc/get_system_strategy`](get_system_strategy.md) | Reads the current system strategy of a site from the cloud; the AI mode condition screen uses only its `electricity_strategy.isAuthorizeAIEms` flag to learn whether the AI EMS is already authorized. | - | owner |
| [`/charging_hes_installer_svc/get_third_jump_url`](get_third_jump_url.md) | Asks the cloud for the URL of the third-party authorization page of a dynamic-price provider (Tibber or Flatpeak) together with a wait time and an aggregation frequency; the app opens the URL so the user can connect the provider account. | - | owner |
| [`/charging_hes_installer_svc/get_utility_rate_plans`](get_utility_rate_plans.md) | Reads the utility rate plan of a large (HES) station: the price source type, the fixed rate or the peak/valley (time-of-use) price table, and, in the new TOU flow, the peak sessions and the price unit. | - | owner |
| [`/charging_hes_installer_svc/get_world_monetary_unit`](get_world_monetary_unit.md) | Reads the list of currencies (price units) that a site may use for its electricity prices; the app sends the site id and empty country and area filters. | - | owner |
| [`/charging_hes_installer_svc/passport_login`](passport_login.md) | Verifies the e-mail and password of an installer account in the identity-authentication dialog: the app sends the e-mail, the encrypted password and its client public key and only learns whether the check succeeded (no token is stored from the answer). | - | owner |
| [`/charging_hes_installer_svc/save_dynamic_price`](save_dynamic_price.md) | Saves the dynamic-price (or time-slot) configuration of a site for one provider: the app sends the provider name, the set/unset switch, the site or device id and the provider-specific parameter objects chosen on the setup pages. | - | owner |
| [`/charging_hes_installer_svc/save_time_of_use`](save_time_of_use.md) | Switches a site to a time-of-use (TOU) price plan: the app sends the on/off switch, the id of the site or device and the TOU type, and for the auto-TOU result page also the provider name and provider parameters. | - | owner |
| [`/charging_hes_installer_svc/v2/app/third/platform/list`](v2/app/third/platform/list.md) | Lists the third-party device platforms (for example Shelly) with their products that can be added to a system; in the installer flow the app asks the installer service instead of the consumer service and sends `app_id` `anker_pros`. | - | owner |
| [`/charging_hes_installer_svc/v2/ota/batch/check_update`](v2/ota/batch/check_update.md) | Asks the cloud for firmware updates for a batch of devices of a system; in the installer flow the app sends the batch to the installer service together with the `system_id`, otherwise to the consumer service. | - | owner |

Not here: MQTT or BLE facts (see [../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)), step-by-step flows ([../../flows/README.md](../../flows/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).

<!-- hand-written below: kept by tools/service_index.py -->
Service index for the URL prefix `/charging_hes_installer_svc/`, the installer-app ("Anker Pros") twin of parts of `/charging_hes_svc/` and `/charging_hes_dynamic_price_svc/`. Each endpoint page is the single owner of its request, response and tags. Upstream keys are `API_ENDPOINTS` keys of `api/apitypes.py`; none of the 18 URLs has one (see each page for the consumer twin). The five new response models of this service are [DynamicPriceCompanyModel](../../models/dynamic_price_company_model.md), [ElectricityPriceModel](../../models/electricity_price_model.md), [ThirdJumpModel and SaveDynamicPriceResponse](../../models/dynamic_price_server_model.md) and [UtilityRatePlansResponse](../../models/utility_rate_plans_response.md) (four pages, five main classes).

## Variant selector: installer app versus consumer app

The 3.24.3 app is one code base for two products. The static field `isProApp` (`base_service/api_url.dart`, field slot `LoadStaticField(0xad8)`) is initialized once by an async function (`@0x49ce97c`): it reads the package info (`PackageInfo.fromPlatform`, `@0x49ce9a0`) and calls a string method on the package-name field with the literal `"anker.pros"` (`@0x49ce9c0` to `@0x49ce9cc`; the method selector is not named by Blutter, by its shape and arguments it is a `contains`), then stores the result with `StoreStaticField` (`@0x49ce9dc`). The package name of this APK is `com.anker.charging` (the unpacked `AndroidManifest.xml` holds that string 17 times and no `anker.pros`), so in this APK the flag is false and the flag-gated getters return the consumer URLs. Dormancy is claimed only for the 15 flag-gated URLs of the table below; the installer build of the app was not available, so nothing is said about its runtime behaviour.

Where a getter chooses the URL, it reads the flag (`LoadStaticField(0xad8)`, then `tbnz w, #4`: bit 4 set means `false`, which jumps to the consumer string) and returns one of two pool strings. Some request bodies also depend on the flag (the installer variant uses `system_code` where the consumer variant uses `station_id`, and `priceUnit` where the consumer uses `price_unit`); each page lists what it traced.

| static getter (Dart name) | getter `@0xADDR` | page | consumer twin |
|---|---|---|---|
| `Api.checkFunction` | `base_service/api_url.dart @0x2349c50` | [check_function](check_function.md) | `/charging_hes_svc/check_function` |
| `Api.sendDeviceCommand` | `api_url.dart @0x249e524` | [edit_system_strategy](edit_system_strategy.md) | `/charging_hes_svc/device_command` |
| `Api.getHesUtilityRatePlans` | `api_url.dart @0x24a5d58` | [get_utility_rate_plans](get_utility_rate_plans.md) | `/charging_hes_svc/get_utility_rate_plans` |
| `Api.getPrice` | `api_url.dart @0x2554b74` | [get_price](get_price.md) | `/charging_hes_dynamic_price_svc/get_price` |
| `Api.getPriceCompany` | `api_url.dart @0x27bde38` | [get_price_company](get_price_company.md) | `/charging_hes_dynamic_price_svc/get_price_company` |
| `Api.getHistorySetting` | `api_url.dart @0x29a4950` | [get_history_setting](get_history_setting.md) | `/charging_hes_svc/get_history_setting` |
| `Api.getThirdJumpUrl` | `api_url.dart @0x29acc3c` | [get_third_jump_url](get_third_jump_url.md) | `/charging_hes_dynamic_price_svc/get_third_jump_url` |
| `Api.adjustStationPriceUnit` | `api_url.dart @0x29ae7dc` | [adjust_station_price_unit](adjust_station_price_unit.md) | `/charging_hes_svc/adjust_station_price_unit` |
| `Api.getPriceUnitsConfig` | `api_url.dart @0x29ae8dc` | [get_world_monetary_unit](get_world_monetary_unit.md) | `/charging_hes_svc/get_world_monetary_unit` |
| `Api.saveAutoTou` | `api_url.dart @0x2e82408` | [save_time_of_use](save_time_of_use.md) | `/charging_hes_dynamic_price_svc/save_time_of_use` |
| `Api.saveDynamicPrice` | `api_url.dart @0x2e82b34` | [save_dynamic_price](save_dynamic_price.md) | `/charging_hes_dynamic_price_svc/save_dynamic_price` |
| `Api.getAreaByCode` | `api_url.dart @0x41e4a70` | [get_area_by_code](get_area_by_code.md) | `/charging_hes_dynamic_price_svc/get_area_by_code` |
| `EmsApi.getDeviceCommand` | `ak_soft_ems/http/ems_api.dart @0x2a31618` | [get_system_strategy](get_system_strategy.md) | `/charging_hes_svc/get_device_command` |
| `EmsApi.enableAiEmsMode` | `ems_api.dart @0x379e6d0` | [enable_aiems_mode](enable_aiems_mode.md) | `/charging_hes_svc/enable_aiems_mode` |
| `EmsApi.authorizeAiEms` | `ems_api.dart @0x37a447c` | [authorize_aiems](authorize_aiems.md) | `/charging_hes_svc/authorize_aiems` |

Three endpoints are not selected by this flag, so their reachability in `com.anker.charging` is NOT determined: [passport_login](passport_login.md) is a literal URL sent by `IdentityAuthView.installerLogin`, which consumer settings pages open without an `isProApp` test (`settings/src/common/menu_controller/grid_param_menu_controller.dart @0x2cd5db8`, `charging/ui/page/device/main/sitation_energy_system/station_home_settings/advanced_setting/advanced_setting_logic.dart @0x3fabd84`); [v2/app/third/platform/list](v2/app/third/platform/list.md) and [v2/ota/batch/check_update](v2/ota/batch/check_update.md) choose by a system id that the commissioning page holds (route argument `systemId`, controller field), and send through the native SDK directly.

All 18 URLs are new in 3.24.3 (the 3.18.0 pool holds no `installer_svc` string); every consumer twin is in the 3.18.0 pool. The consumer twins are documented on their own pages under [../charging_hes_svc/README.md](../charging_hes_svc/README.md) and [../charging_hes_dynamic_price_svc/README.md](../charging_hes_dynamic_price_svc/README.md) (several are still skeletons); where the same sender code serves both URLs, the request keys are owned here.

## Commissioning, session and firmware

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/charging_hes_installer_svc/passport_login`](passport_login.md) | Verifies the e-mail and password of an installer account in the identity-authentication dialog: the app sends the e-mail, the encrypted password and its client public key and only learns whether the check succeeded (no token is stored from the answer). | - | owner |
| [`/charging_hes_installer_svc/v2/app/third/platform/list`](v2/app/third/platform/list.md) | Lists the third-party device platforms (for example Shelly) with their products that can be added to a system; in the installer flow the app asks the installer service instead of the consumer service and sends `app_id` `anker_pros`. | - | owner |
| [`/charging_hes_installer_svc/v2/ota/batch/check_update`](v2/ota/batch/check_update.md) | Asks the cloud for firmware updates for a batch of devices of a system; in the installer flow the app sends the batch to the installer service together with the `system_id`, otherwise to the consumer service. | - | owner |
| [`/charging_hes_installer_svc/check_function`](check_function.md) | Asks the cloud whether the EMS (energy management) function of a system is switched off (`ems_disable`); the app uses the answer to update the VPP (virtual power plant) state of the station home screen. | - | owner |

## AI EMS

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/charging_hes_installer_svc/authorize_aiems`](authorize_aiems.md) | Authorizes the AI EMS (AI energy management) of a site in the cloud; the app sends the site id and, on success, marks the site as authorized and closes the current page. | - | owner |
| [`/charging_hes_installer_svc/enable_aiems_mode`](enable_aiems_mode.md) | Switches the AI EMS mode (the "smart mode" of a large HES system) on for a site; on success the app opens the smart-mode start-success page. | - | owner |
| [`/charging_hes_installer_svc/get_system_strategy`](get_system_strategy.md) | Reads the current system strategy of a site from the cloud; the AI mode condition screen uses only its `electricity_strategy.isAuthorizeAIEms` flag to learn whether the AI EMS is already authorized. | - | owner |

## Tariffs and prices

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/charging_hes_installer_svc/get_utility_rate_plans`](get_utility_rate_plans.md) | Reads the utility rate plan of a large (HES) station: the price source type, the fixed rate or the peak/valley (time-of-use) price table, and, in the new TOU flow, the peak sessions and the price unit. | - | owner |
| [`/charging_hes_installer_svc/get_price_company`](get_price_company.md) | Reads the list of dynamic-price and time-slot providers (companies) available for a product or site, with the provider the user has already selected; it is the first call of the dynamic-price and time-of-use setup pages. | - | owner |
| [`/charging_hes_installer_svc/get_price`](get_price.md) | Reads the price table of a site for one provider: the time-of-use price seasons or the dynamic hourly prices of today and tomorrow; the price preview and time-slot pages use it to draw the prices. | - | owner |
| [`/charging_hes_installer_svc/get_area_by_code`](get_area_by_code.md) | Looks up the price area (Octopus group id) that belongs to an area code of a site; the dynamic-price provider page uses it to find the matching Octopus region. | - | owner |
| [`/charging_hes_installer_svc/get_third_jump_url`](get_third_jump_url.md) | Asks the cloud for the URL of the third-party authorization page of a dynamic-price provider (Tibber or Flatpeak) together with a wait time and an aggregation frequency; the app opens the URL so the user can connect the provider account. | - | owner |
| [`/charging_hes_installer_svc/get_history_setting`](get_history_setting.md) | Reads the history of the TOU (time-of-use) schedule settings of a large (HES) station, i.e. which price mode was last set; the price settings pages use it to decide whether a manual or an automatic TOU mode is already configured. | - | owner |
| [`/charging_hes_installer_svc/save_time_of_use`](save_time_of_use.md) | Switches a site to a time-of-use (TOU) price plan: the app sends the on/off switch, the id of the site or device and the TOU type, and for the auto-TOU result page also the provider name and provider parameters. | - | owner |
| [`/charging_hes_installer_svc/save_dynamic_price`](save_dynamic_price.md) | Saves the dynamic-price (or time-slot) configuration of a site for one provider: the app sends the provider name, the set/unset switch, the site or device id and the provider-specific parameter objects chosen on the setup pages. | - | owner |
| [`/charging_hes_installer_svc/get_world_monetary_unit`](get_world_monetary_unit.md) | Reads the list of currencies (price units) that a site may use for its electricity prices; the app sends the site id and empty country and area filters. | - | owner |
| [`/charging_hes_installer_svc/adjust_station_price_unit`](adjust_station_price_unit.md) | Tells the cloud to change the price unit (currency) of a station's electricity prices; the app sends the station id and the new unit and reads nothing from the answer. | - | owner |

## Device command

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/charging_hes_installer_svc/edit_system_strategy`](edit_system_strategy.md) | Sends a device command that edits the system strategy of a large (HES) station; the only traced sender, the new TOU flow, uses it to save the peak sessions and the price unit of a time-of-use plan. | - | owner |

Not here: MQTT or BLE facts (see [../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)), step-by-step flows ([../../flows/README.md](../../flows/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).
