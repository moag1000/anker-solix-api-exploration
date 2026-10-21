> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# IoT-Kit channel inventory (`akiot.*`)

This page lists every `akiot.*` identifier that the Flutter side of App 3.24.3 hands to, or receives from, the native IoT-Kit SDK, and says which of them are new compared with App 3.18.0. It is an inventory: it records which identifier exists, in which direction it travels, where the Dart code uses it and which argument keys the Dart caller sets. What the native SDK does with an identifier is not in the Dart dump and is therefore not documented here.

Closest template: [../docs/templates/model.md](../docs/templates/model.md) (Purpose, Dart class + file, a fact table, Changed since 3.18.0, Known unknowns). The Fields and Produced/Consumed sections are replaced by the transport and inventory sections below, because there is no JSON model.

## Contents

1. [Purpose](#purpose)
2. [Transport: one method channel, three event channels](#transport-one-method-channel-three-event-channels)
3. [Reading the inventory](#reading-the-inventory)
4. [Channel inventory](#channel-inventory)
5. [Strings in the pool that are not channels](#strings-in-the-pool-that-are-not-channels)
6. [Changed since 3.18.0](#changed-since-3180)
7. [Related pages](#related-pages)
8. [Known unknowns](#known-unknowns)

## Purpose

The Dart layer never calls the native IoT-Kit SDK through one method channel per feature. It calls one method channel with a string identifier (`akiot.<group>.<name>`) and a parameter map, and it receives SDK events as `(identifier, payload)` pairs on an event channel. This page is the owner of that identifier list, so other pages can say "goes through `akiot.device.invoke_action`" and link here instead of repeating the list. Tag: `asm-traced`.

## Transport: one method channel, three event channels

Tag: `asm-traced`. Everything below is in `ak_iot_kit_flutter/src/ak_iot_kit_flutter.dart`, class `AkIotKitFlutter`.

| element | name on the wire | site |
|---|---|---|
| method channel | `ak_iot_kit_flutter` (standard method codec) | pool object `pp+0xc468` |
| `handle` | `invokeMethod("handle", {identifier, param})` | function `@0x21c3d8c`, `invokeMethod` call `@0x21c3e28` |
| `handleWithProgress` | `invokeMethod("handleWithProgress", {identifier, param, transID})` | function `@0x24e1888`, `invokeMethod` call `@0x24e1998` |
| event channel, results and notifications | `ak_iot_kit_flutter_receiver_event`, each event carries `identifier` (String) and `payload` (`Map<String, dynamic>`) | `ak_iot_kit_flutter.dart`: `receiveBroadcastStream` `@0x21c47b4`; keys read at `@0x21d19f8` and `@0x21d1a54`; handed to `AKIoTEventReceiver.receive` (`base_service/ak_iot_kit/event_receiver.dart @0x21d1ad0`) at `@0x21d1ab4` |
| event channel, progress | `ak_iot_kit_flutter_handle_progress_event`, correlated by `transID` | `ak_iot_kit_flutter.dart`: `receiveBroadcastStream` `@0x221ac18`; `transID` read at `@0x221add0` |
| event channel, SDK log | `ak_iot_kit_flutter_log_event` (levels debug, error, verbose, warning) | `ak_iot_kit_flutter.dart`: `receiveBroadcastStream` `@0x49e07a4` |

The same Dart class (`ak_iot_kit_flutter.dart`) owns eight further plain method names that are not `akiot.*` identifiers: `loginAnkerCloud` (`@0x273dea4`), `logout` (`@0x273e808`), `isLogin` (`@0x273e920`), `updateConfig` (`@0x273ea74`), `getSDKVersion` (`@0x4034f2c`), `updateParams` (`@0x4050414`), `setEventReceiver` (`@0x49e05b4`) and `initSDK` (`@0x49e06e8`). They are listed only so the reader knows the method channel carries more than `handle`.

Most Dart call sites do not use `AkIotKitFlutter` directly. They call `AKIoTKitManagerImpl.handle` (`base_service/ak_iot_kit/ak_iot_kit_manager_impl.dart @0x21c3a94`) or `AKIoTKitManagerImpl.handleWithProgress` (`@0x2ac6dd8`), which the [SDK senders page](../api/sdk_senders.md#the-common-envelope) describes for the HTTP case. A few sites call `AkIotKitFlutter.handle` directly (for example `akiot.cloud_api` in `station_home/src/http/station_api_client.dart @0x2a444b8`).

The app contains no `setMethodCallHandler` on this channel. Native-to-Dart traffic arrives only through the event channels above, so the direction column below never says "method-call callback".

## Reading the inventory

- Identifier set: the `"akiot.<...>"` strings of the 3.24.3 object pool (`pp.txt`), reduced to those that are channels (see [Strings in the pool that are not channels](#strings-in-the-pool-that-are-not-channels)). The 3.18.0 set comes from the 3.18.0 `pp.txt` and is used only for the `since` column.
- Direction `app→SDK` means the string is passed as the identifier of `AKIoTKitManagerImpl.handle` (or `handleWithProgress`) at the cited site. Direction `SDK→app event` means the string is either matched against the incoming `identifier` in `AKIoTEventReceiver.receive` or used as the key of `AkIotEventManager.register` / `remove` (`base_service/ak_iot_kit/ak_iot_event_manager.dart`), which is the Dart-side subscription for that event identifier.
- Call site: the first site of the stated kind, written `file @0xADDR (function)`, where the address is the instruction that loads the identifier string. `N more` counts the other sites that load the same string anywhere in the dump (for the common identifiers, several of them are the same call made from different feature modules).
- Args: the string keys that the Dart sender function loads before the call, in the function that holds the cited site. Values and types are not read; no integer literal is read for this page, so the Smi rule of [../METHODOLOGY.md](../METHODOLOGY.md#smi-rule-reading-numbers-from-blutter-output) does not enter into any row. For event identifiers the payload is a map whose keys are not traced here.
- Tag: every row is `asm-traced` (a traced Dart site exists in 3.24.3). A row would be `string-only` if the identifier appeared in the pool without a site; no channel is in that state.

## Channel inventory

Tag: `asm-traced`. 90 channels in 3.24.3, 22 of them new. Rows are sorted by identifier; the new ones are in bold in the `since` column.

| channel | direction | Dart call site | since | args keys set by the Dart sender | tag |
|---|---|---|---|---|---|
| `akiot.ble.connect_device` | app→SDK `handle` | `charging/ble/sdk_handler/sdk_ble_device_connector.dart @0x348dcfc` (`connect`) | 3.18.0 | `bleMac`, `bleName`, `timeOut` | asm-traced |
| `akiot.ble.disconnect_device` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/basic_command.dart @0x244e3e4` (`disconnectDevice`); 1 more | 3.18.0 | `bleMac` | asm-traced |
| `akiot.ble.set_ble_state` | app→SDK `handle` | `charging/ui/page/home/home_page.dart @0x2b9a184` (`_handleBluetoothState`) | 3.18.0 | `switchState` | asm-traced |
| `akiot.ble.stop_connect_device` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/basic_command.dart @0x23ed760` (`stopConnectDevice`) | 3.18.0 | none visible | asm-traced |
| `akiot.ble.write_characteristic` | app→SDK `handle` | `charging/ble/sdk_handler/sdk_ble_operation.dart @0x22700c0` (`_writeCommand`) | 3.18.0 | `bleMac`, `data` | asm-traced |
| `akiot.cloud_api` | app→SDK `handle` | `ev_charger/src/ev_charger/page/home/schedule_charge/network/ schedule_network.dart @0x284f780` (`_requestHttp`); 72 more | 3.18.0 | `path`, `method`, `param` (envelope owned by [sdk_senders.md](../api/sdk_senders.md#the-common-envelope)) | asm-traced |
| `akiot.device.accessory.bind` | app→SDK `handle` | `oe_a7320/src/oe_a7320/network/range_extender_ble.dart @0x2ae1260` (`bindDevice`) | 3.18.0 | `deviceSn`, `accessoryBleMac`, `bleMac`, `addressType`, `devicePn`, `oilEngineSystemID` | asm-traced |
| `akiot.device.accessory.unbind` | app→SDK `handle` | `oe_a7320/src/oe_a7320/network/range_extender_ble.dart @0x3851b98` (`unbind`) | 3.18.0 | `deviceSn`, `accessoryBleMac`, `bleMac` | asm-traced |
| `akiot.device.connection_status` | app→SDK `handle` | `ota_kit/src/controllers/batch_device_ota_controller.dart @0x3630628` (`_correctOfflineStateForCachedOtaDevices`); 1 more | 3.18.0 | `deviceSn`, `bleMac` | asm-traced |
| `akiot.device.external_field_changed` | SDK→app event (`AkIotEventManager.register`) | `device/src/station_setting/controller/common_grid_param/grid_param_command_capability.dart @0x2a51c0c` (`watchGridCode`); 9 more | **new in 3.24.3** | event `payload` map (not read) | asm-traced |
| `akiot.device.fetch_device_fault_info` | app→SDK `handle` | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2c67324` (`getUserFloatingFaultInfo`); 1 more | 3.18.0 | `deviceSn` | asm-traced |
| `akiot.device.fetch_device_info` | SDK→app event (matched in `AKIoTEventReceiver.receive`) | `base_service/ak_iot_kit/event_receiver.dart @0x21d1c14` (`receive`) | 3.18.0 | event `payload` map (not read) | asm-traced |
| `akiot.device.fetch_device_info_v2` | SDK→app event (matched in `AKIoTEventReceiver.receive`) | `base_service/ak_iot_kit/event_receiver.dart @0x21d1c3c` (`receive`) | **new in 3.24.3** | event `payload` map (not read) | asm-traced |
| `akiot.device.get_external_field` | app→SDK `handle` | `device/src/station_setting/controller/common_grid_param/grid_param_command_capability.dart @0x2a52c68` (`[closure] Future<int?> <anonymous closure>`); 4 more | **new in 3.24.3** | `deviceSn`, `category`, plus `forceRefresh` at one site | asm-traced |
| `akiot.device.get_sub_version_list` | app→SDK `handle` | `ota_kit/src/providers/sub_package_info_provider_v2.dart @0x497b3e4` (`_fetchFromAkiotkit`) | **new in 3.24.3** | `deviceSn` | asm-traced |
| `akiot.device.invoke_action` | app→SDK `handle` | `settings/src/sdk/command/settings_command.dart @0x2283da4` (`[closure] Future<IoTAKResult<dynamic>> <anonymous closure>`); 138 more | 3.18.0 | `id` (action name), `deviceSn`, `param` | asm-traced |
| `akiot.device.is_ota_in_progress` | app→SDK `handle` | `ota_kit/src/services/ota_remote_status_service.dart @0x2ecf5d8` (`checkOTAInProgress`) | **new in 3.24.3** | `snList` | asm-traced |
| `akiot.device.monitor_ota` | app→SDK `handleWithProgress` | `ota_kit/src/strategies/batch_ota_strategy.dart @0x362e74c` (`reattachToRunningOTA`) | **new in 3.24.3** | `snList`, `timeOut` | asm-traced |
| `akiot.device.monitor_ota_progress` | app→SDK `handleWithProgress` | `ota_kit/src/services/ota_sdk_service.dart @0x2ecb97c` (`monitorOTAProgress`) | **new in 3.24.3** | `deviceSn`, `timeOut` | asm-traced |
| `akiot.device.notification_events` | SDK→app event (`AkIotEventManager.register`) ; SDK→app event (matched in `AKIoTEventReceiver.receive`) | `settings/src/common/page/italy_self_test/italy_self_test_new_controller.dart @0x3618b00` (`onInit`); 36 more | 3.18.0 | event `payload` map (not read) | asm-traced |
| `akiot.device.read_property` | app→SDK `handle` | `ats_ax170/src/sdk/command/ax170_command.dart @0x35013dc` (`readBatteryPackInfo`); 1 more | 3.18.0 | `id` (property name), `deviceSn`, `param`, plus `bleMac`, `reservedBits` at one site | asm-traced |
| `akiot.device.reconnect_device` | app→SDK `handleWithProgress` | `base_service/ak_iot_kit/business/basic/command/basic_command.dart @0x4804748` (`reconnectDevice`) | 3.18.0 | `bleMac`, `timeOut`, `connectTimeOut`, `trigger_way`, `bluetoothPwd` | asm-traced |
| `akiot.device.remove_user_floating_fault_info` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/msg_command.dart @0x483d4e8` (`removeUserFloatingFaultInfo`) | 3.18.0 | `deviceSn`, `faultIds` | asm-traced |
| `akiot.device.send_ble_ota_progress` | app→SDK `handle` | `ota_kit/src/services/ota_sdk_service.dart @0x49805ac` (`pushProgressToDevice`) | **new in 3.24.3** | `deviceSn`, `progress` | asm-traced |
| `akiot.device.send_report_heart_cmd` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/basic_command.dart @0x358ba28` (`sendReportHeartCmd`) | 3.18.0 | `deviceSn` | asm-traced |
| `akiot.device.set_device_encrypt_key` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/basic_command.dart @0x2633ec8` (`setDeviceEncryptKey`) | 3.18.0 | `bleMac`, `encryptType`, `encryptKey`, `encryptIv` | asm-traced |
| `akiot.device.set_device_negotiated` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/basic_command.dart @0x2633bc4` (`setNegotiated`) | 3.18.0 | `bleMac`, `isNegotiation` | asm-traced |
| `akiot.device.set_wifi_connection_status` | app→SDK `handle` | `device_bind/src/device_bind/wifi_connect/wifi_connect_logic.dart @0x392d8e4` (`[closure] Future<void> <anonymous closure>`) | **new in 3.24.3** | `deviceSn`, `wifiOnline` | asm-traced |
| `akiot.device.setup_devices` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/basic_command.dart @0x244e9c0` (`setUpDevices`) | 3.18.0 | `data` | asm-traced |
| `akiot.device.start_ota` | app→SDK `handle` and `handleWithProgress` | `ota_kit/src/strategies/batch_ota_strategy.dart @0x362fd34` (`_callBatchOTAApi`); 4 more | 3.18.0 | caller-dependent: `devices`, `timeOut` (batch); `deviceSn`, `otaType`, `subDeviceSn` (combined OTA); the per-device strategies build a larger `otaUpdateData` map | asm-traced |
| `akiot.device.stop_reconnect_device` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/basic_command.dart @0x23ed6e4` (`stopReconnectDevice`) | 3.18.0 | `bleMac` | asm-traced |
| `akiot.device.unbind_device` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/basic_command.dart @0x2816168` (`unBindCloudDevice`) | 3.18.0 | `deviceSn` | asm-traced |
| `akiot.device.user_fault_alarm` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/msg_command.dart @0x2214788` (`userFaultAlarm`) | 3.18.0 | `deviceSn`, `pn`, `typeId`, `tlvPayload`, `compositeSystemId`, `otherPayload` | asm-traced |
| `akiot.device.write_property` | app→SDK `handle` | `ats_ax170/src/sdk/command/ax170_command.dart @0x3753728` (`setSystemParams`); 1 more | 3.18.0 | `id` (property name), `deviceSn`, `param`, plus `bleMac` | asm-traced |
| `akiot.ems.get_ems_mode` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/ems_command.dart @0x22bde68` (`getEmsMode`) | 3.18.0 | `identifier_id`, `scenario_type`, `region_type` | asm-traced |
| `akiot.ems.set_ems_mode` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/ems_command.dart @0x31b9c2c` (`setEmsMode`) | 3.18.0 | `identifier_id`, `region_type`, `scenario_type`, `mode_type`, `is_off_grid`, `sub_mode`, `battery_reserve`, `use_time` | asm-traced |
| `akiot.energy.fetch_site_fault_info` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/msg_command.dart @0x22fdf70` (`getSiteFloatingFaultInfo`); 1 more | 3.18.0 | `stationId`, `allSnList` | asm-traced |
| `akiot.energy.get_backup_records` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/station_command.dart @0x2ad38c4` (`getBackupRecord`) | 3.18.0 | `station_id`, `page_num`, `page_size` | asm-traced |
| `akiot.energy.platform_co2_ranking` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/station_command.dart @0x233d1c0` (`getCO2Ranking`) | **new in 3.24.3** | `siteId` | asm-traced |
| `akiot.energy.platform_energy_analysis` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/station_command.dart @0x2333848` (`getEnergyAnalysis`) | 3.18.0 | `site_id`, `type`, `device_type`, `start_time`, `end_time`, `custom_branch`, `device_sn`, `sub_device_infos` | asm-traced |
| `akiot.energy.platform_energy_filter_tree` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/station_command.dart @0x2ca1384` (`getEnergyFilterTree`) | **new in 3.24.3** | `site_id`, `date_type`, `start_time`, `end_time` | asm-traced |
| `akiot.energy.platform_get_site_scene` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/station_command.dart @0x2327d38` (`getSiteScene`) | 3.18.0 | `site_id` | asm-traced |
| `akiot.energy.remove_site_floating_fault_info` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/msg_command.dart @0x4285f94` (`removeSiteFloatingFaultInfo`) | 3.18.0 | `stationId`, `faultIds` | asm-traced |
| `akiot.energy.set_device_attrs` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/station_command.dart @0x3292dd8` (`setDeviceAttrs`) | **new in 3.24.3** | built by the single caller `system_a17e2_flow_chart_logic.dart @0x3292d4c`: `device_sn` and `attributes` holding `load_port_name` (keys at `@0x3292ccc`, `@0x3292cf0`, `@0x3292c98`) | asm-traced |
| `akiot.initflow.get_multiple_devices_wifi_info` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/init_flow_command.dart @0x27b9010` (`getMultipleDevicesWifiInfo`) | 3.18.0 | `device_list` | asm-traced |
| `akiot.initflow.initflow_opening_params` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/init_flow_command.dart @0x29d0848` (`getInitflowOpeningParams`) | 3.18.0 | `product_codes`, `op_type`, `use_mock_data` | asm-traced |
| `akiot.initflow.platform_add_site_devices` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/init_flow_command.dart @0x241b710` (`addSiteDevices`) | 3.18.0 | `site_id`, `combination_type`, `device_list` | asm-traced |
| `akiot.initflow.platform_create_site` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/init_flow_command.dart @0x27b7c24` (`createPlatformSite`) | 3.18.0 | `combination_type`, `main_product_codes`, `site_name`, `site_img`, `device_list` | asm-traced |
| `akiot.initflow.platform_delete_site` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/init_flow_command.dart @0x4250f5c` (`deleteSite`) | 3.18.0 | `site_id` | asm-traced |
| `akiot.initflow.platform_delete_site_devices` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/station_command.dart @0x299f59c` (`[closure] Future<IoTAKResult<dynamic>> <anonymous closure>`) | 3.18.0 | `site_id`, `device_sn`, `combination_type` | asm-traced |
| `akiot.initflow.platform_delete_wired_devices` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/station_command.dart @0x2dd391c` (`[closure] Future<IoTAKResult<dynamic>> <anonymous closure>`) | **new in 3.24.3** | `site_id`, `hardware_info` | asm-traced |
| `akiot.initflow.platform_get_addable_site_list` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/init_flow_command.dart @0x2abe6dc` (`getAddableSiteList`) | 3.18.0 | `product_code`, `device_sn`, `count`, `check_site_with_x8312` | asm-traced |
| `akiot.initflow.platform_get_site_addable_devices_by_type` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/init_flow_command.dart @0x2300960` (`getSiteAddableDevicesByType`) | 3.18.0 | `site_id`, `combination_type` | asm-traced |
| `akiot.initflow.platform_set_device_init_status` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/init_flow_command.dart @0x3246670` (`setDeviceInitComplete`); 3 more | 3.18.0 | `deviceSn`, `init_status` | asm-traced |
| `akiot.initflow.platform_set_site_init_status` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/init_flow_command.dart @0x324632c` (`setSiteAttr`) | 3.18.0 | `site_id`, `init_status` | asm-traced |
| `akiot.mqtt.connect_mqtt` | app→SDK `handle` | `charging/mqtt/business/mqtt_serve.dart @0x24081e8` (`startConnect`) | 3.18.0 | none visible | asm-traced |
| `akiot.mqtt.disconnect_mqtt` | app→SDK `handle` | `charging/mqtt/base/sdk_imp_mqtt_manager.dart @0x48258c0` (`disconnect`) | 3.18.0 | none visible | asm-traced |
| `akiot.mqtt.get_client_id` | app→SDK `handle` | `charging/mqtt/base/sdk_imp_mqtt_manager.dart @0x273e10c` (`requestClientId`) | 3.18.0 | none visible | asm-traced |
| `akiot.mqtt.get_mqtt_connection_status` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/basic_command.dart @0x220758c` (`getMqttConnectionStatus`) | 3.18.0 | none visible | asm-traced |
| `akiot.mqtt.publish_message` | app→SDK `handle` | `charging/mqtt/base/sdk_imp_mqtt_manager.dart @0x48257e8` (`sendMessage`) | 3.18.0 | `topic`, `message` | asm-traced |
| `akiot.mqtt.subscribe_topic` | app→SDK `handle` | `charging/mqtt/base/sdk_imp_mqtt_manager.dart @0x481bf70` (`subscribeOnTopic`) | 3.18.0 | `topicList` | asm-traced |
| `akiot.mqtt.unsubscribe_topic` | app→SDK `handle` | `charging/mqtt/base/sdk_imp_mqtt_manager.dart @0x4816798` (`unSubscribeOnTopic`) | 3.18.0 | `topicList` | asm-traced |
| `akiot.opening.installer_authorize_devices_mqtt` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/init_flow_command.dart @0x32475ec` (`authorizeDevicesMqtt`) | **new in 3.24.3** | `system_id`, `device_sns` | asm-traced |
| `akiot.opening.installer_bind_main_device` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/init_flow_command.dart @0x2abe5e0` (`bindMainDeviceToInstallerSystem`) | **new in 3.24.3** | `system_id`, `pn`, `device_sn` | asm-traced |
| `akiot.opening.installer_get_bind_device_info` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/init_flow_command.dart @0x2ac46a8` (`getBindDeviceInfo`) | **new in 3.24.3** | `system_id` | asm-traced |
| `akiot.opening.installer_system_commission` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/init_flow_command.dart @0x32476ac` (`installerSystemCommission`) | **new in 3.24.3** | `system_id` | asm-traced |
| `akiot.pairing.activate_device_ethernet` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/basic_command.dart @0x3515e8c` (`checkEthernet`) | 3.18.0 | `bleMac` | asm-traced |
| `akiot.pairing.activate_device_wifi` | app→SDK `handleWithProgress` | `base_service/ak_iot_kit/business/basic/command/basic_command.dart @0x2e1bc40` (`bindDeviceWithWifi`) | 3.18.0 | `bleMac`, `wifiSSID`, `wifiPwd`, `bluetoothPwd` | asm-traced |
| `akiot.pairing.activate_multi_device_wifi` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/init_flow_command.dart @0x27be5c4` (`bindDeviceWithWifiList`); 4 more | 3.18.0 | `deviceMacList`, `wifiSSID`, `wifiPwd`, `timeOut`, `deviceInfoList` | asm-traced |
| `akiot.pairing.activate_multi_pro_device_wifi` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/init_flow_command.dart @0x27be7c4` (`bindProDeviceWithWifiList`); 2 more | **new in 3.24.3** | `deviceMacList`, `wifiSSID`, `wifiPwd`, `ownerUid`, `timeZoneID`, `systemId`, `timeOut`, `deviceInfoList` | asm-traced |
| `akiot.pairing.ble_bind_device` | app→SDK `handleWithProgress` | `base_service/ak_iot_kit/business/basic/command/basic_command.dart @0x2ac6db8` (`bindDevices`) | 3.18.0 | `deviceName`, `bluetoothPwd`, `bleMac`, `trigger_way` | asm-traced |
| `akiot.pairing.fetch_relate_belong` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/basic_command.dart @0x27442bc` (`fetchRelateBelong`) | 3.18.0 | `deviceSn` | asm-traced |
| `akiot.pairing.get_wifi_list` | app→SDK `handleWithProgress` | `base_service/ak_iot_kit/business/basic/command/basic_command.dart @0x2e16bf4` (`scanWifiList`) | 3.18.0 | `bleMac` | asm-traced |
| `akiot.pairing.pro_activate_device_wifi` | app→SDK `handleWithProgress` | `base_service/ak_iot_kit/business/basic/command/basic_command.dart @0x2e1bdb8` (`proBindDeviceWithWifi`) | **new in 3.24.3** | `bleMac`, `wifiSSID`, `wifiPwd`, `bluetoothPwd`, `ownerUid`, `timeZoneID`, `systemId` | asm-traced |
| `akiot.pairing.pro_ble_bind_device` | app→SDK `handleWithProgress` | `base_service/ak_iot_kit/business/basic/command/basic_command.dart @0x2ac7418` (`bindDevicesForPro`) | **new in 3.24.3** | `deviceName`, `bluetoothPwd`, `bleMac`, `trigger_way`, `ownerUid`, `bindType`, `systemId` | asm-traced |
| `akiot.pairing.scan_devices` | app→SDK `handleWithProgress` | `base_service/ak_iot_kit/business/basic/command/basic_command.dart @0x3922504` (`scanDevices`); 1 more | 3.18.0 | `pnCodeList` | asm-traced |
| `akiot.pairing.stop_scan_devices` | app→SDK `handle` | `base_service/ak_iot_kit/business/basic/command/basic_command.dart @0x2446ac8` (`stopScanDevices`) | 3.18.0 | none visible | asm-traced |
| `akiot.product.fetch_kvconfig` | app→SDK `handle` | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x29e3288` (`fetchEvChargerKVConfig`); 3 more | 3.18.0 | `pnCode`, `key`, `sku` (one site: `custom_fields`, `fromCloud`) | asm-traced |
| `akiot.receive.ble_connect` | SDK→app event (matched in `AKIoTEventReceiver.receive`) | `base_service/ak_iot_kit/event_receiver.dart @0x21d1b24` (`receive`) | 3.18.0 | event `payload` map (not read) | asm-traced |
| `akiot.receive.ble_data` | SDK→app event (matched in `AKIoTEventReceiver.receive`) | `base_service/ak_iot_kit/event_receiver.dart @0x21d1b4c` (`receive`) | 3.18.0 | event `payload` map (not read) | asm-traced |
| `akiot.receive.device_fault_info` | SDK→app event (`AkIotEventManager.register`) | `business_common/msg/site_msg_banner_controller.dart @0x35325d8` (`_initializeController`); 4 more | 3.18.0 | event `payload` map (not read) | asm-traced |
| `akiot.receive.mqtt_connect` | SDK→app event (matched in `AKIoTEventReceiver.receive`) | `base_service/ak_iot_kit/event_receiver.dart @0x21d1b74` (`receive`) | 3.18.0 | event `payload` map (not read) | asm-traced |
| `akiot.receive.mqtt_data` | SDK→app event (`AkIotEventManager.register`) ; SDK→app event (matched in `AKIoTEventReceiver.receive`) | `balcony/src/ae100/home/ae100_home_logic.dart @0x3502558` (`onInit`); 2 more | 3.18.0 | event `payload` map (not read) | asm-traced |
| `akiot.receive.mqtt_online` | SDK→app event (matched in `AKIoTEventReceiver.receive`) | `base_service/ak_iot_kit/event_receiver.dart @0x21d1b9c` (`receive`) | 3.18.0 | event `payload` map (not read) | asm-traced |
| `akiot.receive.ocpp_service_switching` | SDK→app event (matched in `AKIoTEventReceiver.receive`) | `base_service/ak_iot_kit/event_receiver.dart @0x21d1bec` (`receive`) | 3.18.0 | event `payload` map (not read) | asm-traced |
| `akiot.receive.smart_charging_update` | SDK→app event (`AkIotEventManager.register`) | `ev_charger/src/ev_charger/page/home/a5190_home_logic.dart @0x3508004` (`_initRealTimeData`); 1 more | 3.18.0 | event `payload` map (not read) | asm-traced |
| `akiot.receive.station_scene_bind_event` | SDK→app event (`AkIotEventManager.register`) | `micro_hes/src/a17e2/station/home/base_station_logic.dart @0x3521f2c` (`_initMqttSceneInfoListener`); 5 more | **new in 3.24.3** | event `payload` map (not read) | asm-traced |
| `akiot.receive.station_scene_info` | SDK→app event (`AkIotEventManager.register`) ; SDK→app event (matched in `AKIoTEventReceiver.receive`) | `ak_soft_ems/aiems/aiems_strategy_controller.dart @0x363a830` (`_registerMqttSceneInfoListener`); 9 more | 3.18.0 | event `payload` map (not read) | asm-traced |
| `akiot.receive.usb_connect` | SDK→app event (matched in `AKIoTEventReceiver.receive`) | `base_service/ak_iot_kit/event_receiver.dart @0x21d1d48` (`receive`) | **new in 3.24.3** | event `payload` map (not read) | asm-traced |
| `akiot.track.event` | app→SDK `handle` | `base_service/sensors_data/sensors_data_util.dart @0x22046b8` (`[closure] Null <anonymous closure>`); 2 more | 3.18.0 | `eventName`, `properties`, `product_code`, `device_sn` | asm-traced |

Notes on rows that are not a single plain call:

- `akiot.cloud_api` has 73 sites: 71 through `AKIoTKitManagerImpl.handle` and 2 through `AkIotKitFlutter.handle`, from 19 files. The envelope and the sender list are owned by [../api/sdk_senders.md](../api/sdk_senders.md); which of these calls are encrypted is owned by [../api/encryption.md](../api/encryption.md#which-calls-are-encrypted). This page adds nothing to either.
- `akiot.device.invoke_action` has 139 sites in 53 files: 121 through `handle`, 17 inside the transaction-configuration maps (`s1_s2/src/s1_s2_transation_config.dart` 9, `charging/ui/page/device/a1782/utils/pps_transation_config.dart` 7, `as200/src/as200_transation_config.dart` 1; the role of these map entries is not traced) and 1 string comparison in `base_service/ak_iot_kit/transaction/transactionlock_interceptor.dart @0x221cd60`. The action name travels in the `id` argument (for example `action_set_power_limit_country_code` at `settings/src/sdk/command/settings_command.dart @0x2283da4`); the action names are owned by the device and endpoint pages, not here.
- `akiot.device.read_property` and `akiot.device.write_property` use the same `id` / `deviceSn` / `param` shape as `invoke_action`; the property or action name is the `id` value.
- `akiot.pairing.activate_multi_device_wifi` and `akiot.pairing.activate_multi_pro_device_wifi` are also compared as strings in `device/src/station_setting/controller/common_station_wifi/page/connect_wifi_controller.dart` (`_normalizeDeployResultIdentifier`, `@0x2ac0a24` and `@0x2ac0a48`), and `activate_multi_pro_device_wifi` also in `wifi_deploy_timeout.dart @0x2ac2324`. These sites normalise or compare a result identifier; what the native side reports back is not traced.
- `akiot.device.start_ota` is called both through `handle` (`charging/ui/page/device/anker_ota/combine_progress_ota_page/combine_progress_ota_logic.dart @0x406db5c`) and through `handleWithProgress` (`ota_kit/src/strategies/batch_ota_strategy.dart @0x362fd34` and the `OTASDKServiceImpl.startOTAWithProgress` wrapper `ota_kit/src/services/ota_sdk_service.dart @0x4982e78`).
- `akiot.device.fetch_device_info` and `akiot.device.fetch_device_info_v2` sit in the `akiot.device.*` group but are only matched as incoming event identifiers in `AKIoTEventReceiver.receive` (`event_receiver.dart @0x21d1c14` and `@0x21d1c3c`), so they are SDK→app events despite the group name. `akiot.device.external_field_changed` is likewise an event key, not a request; its request-side partner is `akiot.device.get_external_field`.

## Strings in the pool that are not channels

Tag: `asm-traced`. Nine pool strings start with `akiot.` but are not channel identifiers. Eight are an identifier followed by one trailing space and are loaded as the first part of a string interpolation (log or message text), not passed to `handle`: `akiot.ble.connect_device ` (`charging/ble/sdk_handler/sdk_ble_device_connector.dart @0x348dd3c`), and the same pattern for `akiot.ble.disconnect_device `, `akiot.ble.set_ble_state `, `akiot.mqtt.get_client_id `, `akiot.mqtt.publish_message ` (`charging/mqtt/base/sdk_imp_mqtt_manager.dart @0x48256b0`), `akiot.mqtt.subscribe_topic `, `akiot.mqtt.unsubscribe_topic ` and `akiot.receive.ble_connect ` (`base_service/ak_iot_kit/event_receiver.dart @0x2216f14`). The ninth, `akiot.device_system.`, is a prefix loaded into a string interpolation in `charging/impl/station_home_sdk_port.dart @0x234c290`. The eight trailing-space strings exist in 3.18.0 as well; `akiot.device_system.` is the one pool string that is new in 3.24.3 without being a channel. All nine are excluded from the counts below.

## Changed since 3.18.0

Tag: `asm-traced` for the 3.24.3 side; the 3.18.0 side is the pool-string diff only (see [../METHODOLOGY.md](../METHODOLOGY.md#sources-and-priority)).

| | 3.18.0 count | 3.24.3 count | new count | removed count | tag |
|---|---|---|---|---|---|
| `akiot.*` channels | 68 | 90 | 22 | 0 | asm-traced |
| of which `akiot.device.*` | 19 | 28 | 9 | 0 | asm-traced |

Pool strings starting with `akiot.`: 76 in 3.18.0, 99 in 3.24.3, 23 added, 0 removed; subtracting the nine non-channel strings (eight in both versions plus the new prefix `akiot.device_system.`) gives 68 and 90.

The 22 new channels, by group:

| group | count | new channels | tag |
|---|---|---|---|
| `akiot.device.*` | 9 | `external_field_changed`, `fetch_device_info_v2`, `get_external_field`, `get_sub_version_list`, `is_ota_in_progress`, `monitor_ota`, `monitor_ota_progress`, `send_ble_ota_progress`, `set_wifi_connection_status` | asm-traced |
| `akiot.energy.*` | 3 | `platform_co2_ranking`, `platform_energy_filter_tree`, `set_device_attrs` | asm-traced |
| `akiot.initflow.*` | 1 | `platform_delete_wired_devices` | asm-traced |
| `akiot.opening.*` (new group) | 4 | `installer_authorize_devices_mqtt`, `installer_bind_main_device`, `installer_get_bind_device_info`, `installer_system_commission` | asm-traced |
| `akiot.pairing.*` | 3 | `activate_multi_pro_device_wifi`, `pro_activate_device_wifi`, `pro_ble_bind_device` | asm-traced |
| `akiot.receive.*` | 2 | `station_scene_bind_event`, `usb_connect` | asm-traced |

Readings that follow from the table, not separate facts: the OTA group (`monitor_ota`, `monitor_ota_progress`, `is_ota_in_progress`, `get_sub_version_list`, `send_ble_ota_progress`) is called only from `ota_kit/`; the four `opening.*` channels are called only from `init_flow_command.dart`, the Dart wrapper for the installer flow; the `pro_*` pairing channels sit next to their non-pro counterparts in `basic_command.dart` and carry extra keys such as `ownerUid` and `systemId`. `akiot.pairing.activate_device_ethernet` is present in 3.18.0 already (pool string in the 3.18.0 `pp.txt`) and is therefore not new. No channel was removed: the 3.24.3 pool contains every 3.18.0 channel string, and each still has a traced site.

The 3.18.0 count of 19 `akiot.device.*` identifiers agrees with the figure in the old [../CHANGELOG.md](../CHANGELOG.md) (19 `akiot.device.*` strings); nothing else in the older root pages listed the other groups.

## Related pages

Tag: untagged by design (no API fact).

- [../api/sdk_senders.md](../api/sdk_senders.md): the HTTP senders that use `akiot.cloud_api`, the envelope and the path C sender list.
- [../api/encryption.md](../api/encryption.md): which `akiot.cloud_api` calls are encrypted.
- [../METHODOLOGY.md](../METHODOLOGY.md): tags, Smi rule and citation format.

## Known unknowns

Tag: untagged by design (no API fact).

- The native SDK is not in the Dart dump. What each identifier does natively, its return type and its error codes are unknown from this evidence.
- Argument values and types: only the string keys loaded by the Dart sender are listed. The one caller-built map, `akiot.energy.set_device_attrs`, is documented in the channel table (single caller, keys `device_sn` and `attributes`); the value types of the other channels are known only as far as the sender functions list them.
- Event payload layouts for all `SDK→app event` rows are not traced here; the per-event handlers in `event_receiver.dart` (`handleUsbConnectEvent`, `handleFetchSceneInfoEvent`, `handleMqttDataEvent` and others) are the starting point. — traced 2026-10-20: not traced in this pass (about two dozen handlers).
- The role of the 17 `akiot.device.invoke_action` entries in the `*_transation_config.dart` maps and of the identifier comparisons in `connect_wifi_controller.dart` and `wifi_deploy_timeout.dart` is not traced. — traced 2026-10-20: not traced in this pass.
- Whether the 3.18.0 channels kept the same argument keys was not compared; the `since` column rests on pool-string presence only. — traced 2026-10-20: not compared; it needs the 3.18.0 sender functions side by side.
- The connection between these channels and BLE, MQTT or cloud availability on a device is not established here. In particular, nothing on this page implies that a BLE identifier works as a cloud fallback.
