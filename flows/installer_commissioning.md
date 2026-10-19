> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# Installer commissioning (initial setup of an installer system)

How the installer build of the app ("Anker Pros", package name `anker.pros`) commissions a system: the initial setup page fetches the step list, binds the main device to an installer system, provisions the Wi-Fi, authorises the devices for MQTT, runs the firmware update card, and finally commissions the system. Most calls go through the AK IoT kit (`akiot.initflow.*`, `akiot.opening.*`, `akiot.pairing.*`), so the app shows no Dart-level HTTP request for them; the endpoints that do appear in Dart are on [charging_hes_installer_svc](../api/charging_hes_installer_svc/README.md#commissioning-session-and-firmware). The kit channel names and parameters are owned by [../reference/iot_kit_channels.md](../reference/iot_kit_channels.md). The installer pages are new in 3.24.3 and have no rows in the old FLOWS.md audit.

## Trigger (UI action)

The installer opens the initial setup page of a system (`InitialSetupController`, `Initial_setup_controller.dart`); its start-up runs `onReady`, `_supportRecordElectrician`, `_initStepHandlers` and `fetchSetupSteps` (`Initial_setup_controller.dart @0x29c9a88`, `@0x29c9a90`, `@0x29c9a98`, `@0x29c9aa0`). How the installer reaches this page (navigation from the installer home) was not traced. The installer variant of the whole app is selected by the static flag `isProApp` (`base_service/api_url.dart`, set once from the package name `anker.pros`: [charging_hes_installer_svc](../api/charging_hes_installer_svc/README.md#variant-selector-installer-app-versus-consumer-app)).

## Preconditions

- Installer sign-in: the identity dialog verifies the installer account with [passport_login](../api/charging_hes_installer_svc/passport_login.md) (`IdentityAuthView.installerLogin`); its answer is only a success flag. The dialog is also reachable from consumer settings pages, so it is not a proof that the app runs as the installer variant.
- A system id: the installer paths test a non-null system id (`field_5f` in `select_scene_controller.dart @0x2abdfb8`; `field_5b` of the setup controller in `Initial_setup_controller.dart @0x3243c18`). Without it the consumer variants run.
- The main device serial and product number are known (`getMainDeviceSn` at `Initial_setup_controller.dart @0x29c9b80`, `getMainDevicePn` at `@0x29c9cb8`).

## Steps

| # | actor | action | owner page link | asm citation |
|---|---|---|---|---|
| 1 | app | `fetchSetupSteps` asks the kit for the opening parameters of the product: identifier `akiot.initflow.initflow_opening_params` with `product_codes`, `op_type`, `use_mock_data`. A failure keeps the page in its error state; a late answer after the page closed is dropped. | [iot_kit_channels](../reference/iot_kit_channels.md) | `Initial_setup_controller.dart @0x29c9ce8` (call), `@0x29c9d3c` (page closed test), `@0x29c9dc8` (error log) |
| 2 | app | Decodes the `data` text with `InitSetupModel.fromJson` and filters the steps with the business-side callback `shouldShowSetupStep`. The step enum `SetupStep` has the members `connectNet`, `addDevice`, `firmwareUpgrade`, `settings`, `selfCheck`, `renameDevice`, `customCard`, `ats1And2SubCircuit` and `offGridPortConfirm`. | this page | `Initial_setup_controller.dart @0x29c9ec4`, `@0x29c9f20`; `@0x29cf96c` |
| 3 | installer | Selects the scene; the select-scene controller binds the main device to the installer system: log text "call the installer create-station interface: systemId=..., pn=..., deviceSn=..." and the kit call `bindMainDeviceToInstallerSystem` (identifier `akiot.opening.installer_bind_main_device`, `system_id`, `pn`, `device_sn`). The BLE connect logic of the device bind module calls the same function. | [iot_kit_channels](../reference/iot_kit_channels.md) | `select_scene_controller.dart @0x2abdfb0` (function), `@0x2abe048` (log), `@0x2abe1c8` (call); `ble_connect_logic.dart @0x3513dfc` |
| 4 | installer | Add device step: the platform-appoint page lists third-party platforms (for example Shelly) from the installer service, sending the app id `anker_pros` and the system id. | [list](../api/charging_hes_installer_svc/v2/app/third/platform/list.md) | `platform_appoint_add_device_controller.dart @0x24e0548`, `@0x350b6d8` |
| 5 | app | Connect network step: `SyncWifiCommand.deployWifiList` uses the installer variant when the system id string is non-empty (`bindProDeviceWithWifiList`, identifier `akiot.pairing.activate_multi_pro_device_wifi` with `deviceMacList`, `wifiSSID`, `wifiPwd`, `ownerUid`, `timeZoneID`, `systemId`, `timeOut`, `deviceInfoList`) and otherwise the consumer call `bindDeviceWithWifiList`. | [iot_kit_channels](../reference/iot_kit_channels.md) | `sync_wifi_command.dart @0x27be430`, `@0x27be438`, `@0x27be448`, `@0x27be460` |
| 6 | app | Device sync: `InstallerDeviceSyncManager.syncDeviceInfoBySystemId` (called from the setup controller callbacks and from the BLE connect logic) runs `_syncDeviceInfoInternal`, which reads the bound devices with `getBindDeviceInfo` (identifier `akiot.opening.installer_get_bind_device_info`, `system_id`). The event bus message `codeRefreshDevice` triggers the same sync, ignored if the last run was under 1000 ms ago. | [iot_kit_channels](../reference/iot_kit_channels.md) | `installer_device_sync_manager.dart @0x3246ca4` (`getBindDeviceInfo`), `@0x3246ba8`, `@0x3246bb0` (1000 ms test), `@0x3246c48` (call); `Initial_setup_controller.dart @0x32477ac`, `@0x32478e4`; `ble_connect_logic.dart @0x3513618` |
| 7 | app | MQTT authorisation: `authorizeDevicesMqtt` (identifier `akiot.opening.installer_authorize_devices_mqtt`, `system_id`, `device_sns`) logs the system id and the devices and reports success (`设备MQTT授权成功`) or failure. | [iot_kit_channels](../reference/iot_kit_channels.md) | `installer_device_sync_manager.dart @0x3247424`, `@0x324747c`, `@0x32474a8`, `@0x32474c8` |
| 8 | installer | Firmware step: `FirmwareUpgradeController.checkDeviceUpdate` asks the installer service for updates of a batch of devices with the system id; the upgrade itself is [ota_monitor.md](ota_monitor.md)'s subject. | [check_update](../api/charging_hes_installer_svc/v2/ota/batch/check_update.md) | `firmware_upgrade_controller.dart @0x2b0932c`, `@0x2b0d200`, `@0x2b09bb8` |
| 9 | installer | Settings, self-check and rename steps (cards `settings`, `selfCheck`, `renameDevice`); their requests are not part of this page. | this page | `Initial_setup_controller.dart @0x29cf96c` (step filter) |
| 10 | installer | Finishes the setup: `sendSetupFinish` takes the installer branch when the system id is non-null, shows the loading overlay and calls `installerSystemCommission` (identifier `akiot.opening.installer_system_commission`, `system_id`). | [iot_kit_channels](../reference/iot_kit_channels.md) | `Initial_setup_controller.dart @0x3243bd8`, `@0x3243c18`, `@0x3243c4c`, `@0x3243c70` |
| 11 | app | Result of step 10: on success it calls `InstallerDeviceSyncManager.getSiteDetail` with two callbacks that both run `syncDeviceInfoBySystemId` again, and returns. On any other result it shows the toast `commonNetWorkErrorFix`. | this page | `Initial_setup_controller.dart @0x3243c88`, `@0x3243c94`, `@0x3243cd0`, `@0x3243d04`, `@0x324789c`, `@0x3247764` |
| 12 | app | Consumer branch of `sendSetupFinish` (system id null) for contrast: for the device setup types `singleDeviceUse` and `singleDeviceUseWithoutWifi` it sets the device init status (`setDeviceInitComplete`, identifier `akiot.initflow.platform_set_device_init_status`); then fires the UI message 580, refreshes the device list with `getDevicesList`, waits 500 ms and closes the page. | [iot_kit_channels](../reference/iot_kit_channels.md) | `Initial_setup_controller.dart @0x3243d2c`, `@0x3243dc8`, `@0x3244030`, `@0x324409c`, `@0x32440b8`, `@0x32440cc` |

## Side effects

- The installer branch of step 11 does not fire message 580 or close the page in `sendSetupFinish` itself (it returns after `getSiteDetail`); the callbacks of step 11 and the sync manager take over.
- `InstallerDeviceSyncManager` is a singleton: its sync and the authorisation run for every page that triggers `codeRefreshDevice`, not only the setup page.
- Step 5 changes the Wi-Fi configuration of the devices and ties them to the system id and the owner uid.

## Timing (delays/polling)

- The refresh event is rate-limited to one sync per 1000 ms: `difference` of two timestamps compared with `cmp x2, #0x3e8` (`installer_device_sync_manager.dart @0x3246ba8`, `@0x3246bb0`; the raw 0x3e8 is an unboxed millisecond count, so 1000).
- 500 ms: pool `Duration` `pp+0x5378` with `off_8` 0x7a120 = 500,000 microseconds before `closePage` on the consumer branch (`Initial_setup_controller.dart @0x32440b8`; a pool object value, not a register immediate).
- Wi-Fi provisioning has a `timeOut` argument chosen in the connect-net controller; its value was not read.

## Failure paths

- Opening parameters not returned: the page logs `getInitflowOpeningParams error` (`Initial_setup_controller.dart @0x29c9dc8`) and does not build the steps.
- `installerSystemCommission` fails: toast `commonNetWorkErrorFix` (step 11); the setup stays open.
- MQTT authorisation fails: logged (`设备MQTT授权失败`), no retry in this function. Error codes: [errors](../api/errors.md).
- `getBindDeviceInfo` fails: `_syncDeviceInfoInternal` continues with an empty list (`installer_device_sync_manager.dart @0x3246ce0`).

## Since/changed

All `akiot.opening.*` channels, the pro Wi-Fi channel `akiot.pairing.activate_multi_pro_device_wifi` and `InstallerDeviceSyncManager` are new in 3.24.3 ([iot_kit_channels](../reference/iot_kit_channels.md)). `SetupStep` and the consumer branch exist in 3.18.0 in some form; no 3.18.0 comparison was made for them.

## Known unknowns

- What the native kit sends for the four `akiot.opening.*` identifiers (the HTTP endpoints behind them are not visible in Dart) and what `installerSystemCommission` changes on the server.
- How the installer reaches the setup page and how the system id (`field_5b`, `field_5f`) is first obtained.
- The bodies of the callbacks of step 11 beyond the second sync, and the navigation after a successful commission.
- The order in which the step cards run for a given product (`_changeSetupStepStates`, `_stepStateMap`) and which steps the filter drops for which product.
- Whether the installer endpoints ([passport_login](../api/charging_hes_installer_svc/passport_login.md) and the others) are used in the consumer build.
