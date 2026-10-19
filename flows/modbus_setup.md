> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# Modbus setup (third-party control)

How the app turns Modbus TCP or Modbus RTU on or off for a device and sets the RTU slave id, from the settings menu "Third-Party Control Settings" to the cloud request. Which products have the menu, the Bluetooth action, the EV charger variant and the UI texts are owned by [../devices/modbus.md](../devices/modbus.md); payloads are owned by [query_modbus_setting](../api/charging_hes_third_party_service_svc/query_modbus_setting.md) and [set_modbus_setting](../api/charging_hes_third_party_service_svc/set_modbus_setting.md). This page copies none of them.

## Trigger (UI action)

On the third-party control page (`HomeAssistantPage`, route `/homeAssistantPage`) the user flips the Modbus TCP or the Modbus RTU switch. The switch handler is the closure `home_assistant_page.dart @0x38dc638` (created in `HomeAssistantPage::buildCard`, `@0x38d9598`); it calls `HomeAssistantLogic::checkConnectionEnvironment` (`@0x38dc704`) and `HomeAssistantLogic::riskControlToast` (`@0x38dc75c`). A second trigger is saving a new RTU id in the edit dialog (closure `home_assistant_logic.dart @0x38dc360`, dialog opened from `home_assistant_page.dart @0x38da834`).

The page is opened from:

- device, station or advanced settings, menu "Third-Party Control Settings": `CommunicationSettingMenuController::onTapMenu` (`communication_setting_menu_controller.dart @0x2cd46d8`, navigation at `@0x2cd4924`);
- smart plug (A17X8) settings: `A17x8settingLogic::tapEnterHA` (`a17x8setting_logic.dart @0x3dde9b0`, navigation at `@0x3ddebcc`).

## Preconditions

- Logged-in account; the product has the menu (list on [../devices/modbus.md](../devices/modbus.md#pn-marketing-name-generationfamily)), and [query_modbus_setting](../api/charging_hes_third_party_service_svc/query_modbus_setting.md#response) returned `tcpSupport` or `rtuSupport` as `true`; otherwise the menu stays hidden (`communication_setting_menu_controller.dart @0x2cd5330`).
- The menu does not open for a device that has joined a site when it is opened outside the site's settings; the app shows the toast `addedToStationSetting` instead (`enterPort`, `communication_setting_menu_controller.dart @0x2cd4a88`; toast at `@0x2cd47bc`). Accessories always pass (`isAccessory`, `@0x2cd4aac`).
- Modbus TCP needs the device online on Wi-Fi. Modbus RTU and the RTU id need either device Wi-Fi or a local (Bluetooth) connection from the phone to the device. Full table: [../devices/modbus.md](../devices/modbus.md#preconditions-and-the-risk-dialog). Bluetooth is used only to configure a device without Wi-Fi; it is not a fallback for the cloud, and the cloud request is sent in every case.

## Steps

| # | actor | action | owner page link | asm citation |
|---|---|---|---|---|
| 1 | app | The settings menu controller sends `query_modbus_setting` (`siteId` in a site context, else `sn`) when it is created. | [query_modbus_setting](../api/charging_hes_third_party_service_svc/query_modbus_setting.md#request) | `communication_setting_menu_controller.dart @0x3679c80`, request at `@0x2cd4d78` |
| 2 | cloud | Answers; the fields the app reads are on the endpoint page. How the server derives them is not known (server side). | [query_modbus_setting](../api/charging_hes_third_party_service_svc/query_modbus_setting.md#response) | untagged by design (no app-side fact) |
| 3 | app | Keeps the answer and shows the menu if `tcpSupport` or `rtuSupport` is `true`. | [query_modbus_setting](../api/charging_hes_third_party_service_svc/query_modbus_setting.md#response) | `communication_setting_menu_controller.dart @0x2cd523c`, `@0x2cd5330` |
| 4 | user | Taps "Third-Party Control Settings". | [devices/modbus.md](../devices/modbus.md#third-party-control-cloud) | `communication_setting_menu_controller.dart @0x2cd46d8` |
| 5 | app | Opens `/homeAssistantPage` with the arguments `data` (the query answer), `isWifiOnline`, `deviceSn`, `productCode`, `isConnected`, `isSite`. | [devices/modbus.md](../devices/modbus.md#third-party-control-cloud) | `communication_setting_menu_controller.dart @0x2cd481c` to `@0x2cd4924` |
| 6 | app | `onInit` sets the TCP and RTU switches from `modbusStatus`, the RTU id text from `rtuId`, card visibility from the support flags, the guide links from `helpH5Url` / `homeyH5Url`, and caches the switch state. | [query_modbus_setting](../api/charging_hes_third_party_service_svc/query_modbus_setting.md#response) | `home_assistant_logic.dart @0x35eaa34` (reads at `@0x35eae98` to `@0x35eb128`, cache at `@0x35eb1c0` to `@0x35eb1ec`) |
| 7 | user | Flips the TCP or the RTU switch (or saves a new RTU id, step 7b). | [devices/modbus.md](../devices/modbus.md#third-party-control-cloud) | `home_assistant_page.dart @0x38dc638` |
| 7b | user, app | RTU id: the edit dialog accepts digits only and enables Save only for a valid id (rule on the endpoint page). Save closes the dialog and continues at step 8 with the RTU path. | [set_modbus_setting](../api/charging_hes_third_party_service_svc/set_modbus_setting.md#request) | `home_assistant_logic.dart @0x38dabc0` (check), `@0x38dc3c0`, `@0x38dc400` |
| 8 | app | Checks the connection: TCP needs device Wi-Fi; RTU uses Wi-Fi, else the local connection (sets `isBluetooth`), else stops with a toast. | [devices/modbus.md](../devices/modbus.md#preconditions-and-the-risk-dialog) | `home_assistant_logic.dart @0x38dbf30` |
| 9 | app, user | When switching on for the first time on this page, shows the Modbus risk dialog; Cancel ends the flow, Confirm continues. | [devices/modbus.md](../devices/modbus.md#preconditions-and-the-risk-dialog) | `home_assistant_logic.dart @0x38dc778` (confirm closure `@0x38dc92c`, cancel closure `@0x38dc8d4`) |
| 10 | app | Applies the switch in the page: the chosen variant takes the new value, the other one is switched off. Calls `openSwichRequest(isTcp)`. | [devices/modbus.md](../devices/modbus.md#third-party-control-cloud) | `home_assistant_page.dart @0x38dca30` to `@0x38dcaa0`, call at `@0x38dcb00` |
| 11 | app, device | Only if `isBluetooth` is set (RTU, device Wi-Fi offline): shows the loading overlay and sends the IoT kit action `action_ha_communication_setting` to the device; any result other than success ends the flow (Failure paths). | [devices/modbus.md](../devices/modbus.md#bluetooth-path-iot-kit-action) | `home_assistant_logic.dart @0x38dae6c` (branch), `@0x38daeb0` (send), `@0x38daf04` (result check) |
| 12 | app | Only for TCP, and only if the known IP is empty or `"0.0.0.0"`: shows the loading overlay and re-reads `query_modbus_setting` until an IP is known, at most three times (Timing). The answer replaces the page data, so IP and port update. | [query_modbus_setting](../api/charging_hes_third_party_service_svc/query_modbus_setting.md#callers-in-app) | `home_assistant_logic.dart @0x38daf84` (check), `@0x38dafc4` (call), `@0x38db5b4` (`_retryFetchIp`) |
| 13 | app | Sends the setting to the cloud with `set_modbus_setting` (new `modbusStatus`; the RTU path adds `rtuId`); what the server does with it is not verified. The request is sent even when step 12 found no IP. | [set_modbus_setting](../api/charging_hes_third_party_service_svc/set_modbus_setting.md#request) | `home_assistant_logic.dart @0x38db018` (TCP), `@0x38db0a0` (RTU), request at `@0x38db270` |
| 14 | cloud | Receives the setting; what the server does with it (store, push to the device) is not known (server side). | [set_modbus_setting](../api/charging_hes_third_party_service_svc/set_modbus_setting.md#known-unknowns) | untagged by design (no app-side fact) |
| 15 | app | Success: updates the RTU id display, commits the new switch state as the cached state. Failure: see Failure paths. | [set_modbus_setting](../api/charging_hes_third_party_service_svc/set_modbus_setting.md#response) | `home_assistant_logic.dart @0x38db384`, `statusCheck` at `@0x38dbc38` via `home_assistant_page.dart @0x38dcbb0` |
| 16 | user, app | Leaving the page makes the settings menu query again (step 1), so the menu reflects the server's current answer. | [query_modbus_setting](../api/charging_hes_third_party_service_svc/query_modbus_setting.md#callers-in-app) | `communication_setting_menu_controller.dart @0x2cd4958` (`then`), closure `@0x2cd4be4` |

For the smart plug, steps 1 to 5 run in `A17x8settingLogic` instead (`requestData` at `a17x8setting_logic.dart @0x2cd4e10`, page opened at `@0x3ddebcc` with `productCode` `"A17X8"`); steps 6 to 16 are the same.

The EV charger switch on its "Integrations" page is a different flow: one property write to the charger, no cloud request, no risk dialog. It is described on [../devices/modbus.md](../devices/modbus.md#ev-charger-modbus-tcp-device-properties) (`setModbusTcpStatus`, `integrations_setting_logic.dart @0x3972cfc`).

## Side effects

- Analytics events: `AN_App_thirdpartycontrol_show` when the page opens (`home_assistant_logic.dart @0x35eb230`), `AN_App_thirdpartycontrol_modbusTCP_click` / `AN_App_thirdpartycontrol_modbusRTU_click` when a switch is turned on (`home_assistant_page.dart @0x38dc6a4`, `@0x38dc6cc`), `AN_App_thirdpartycontrol_card_click` for a guide card (`home_assistant_logic.dart @0x38d94c4`).
- The risk confirmation is remembered only in the page object (`home_assistant_logic.dart @0x38dc960`); it is asked again after the page is reopened.
- On the Bluetooth path the device has already received the new setting before the cloud request. If the cloud request then fails, the page reverts the switch although the device may have applied it.
- Turning one variant on switches the other one off in the page (step 10). On failure `statusCheck` restores only the variant that was requested (`home_assistant_logic.dart @0x38dbc60` for TCP, `@0x38dbc84` for RTU), so the other switch can stay off on screen until the page is reloaded.
- Step 12 replaces the whole page data with the newest query answer (`home_assistant_logic.dart @0x38dbae0`).

## Timing (delays/polling)

- `_retryFetchIp` (`home_assistant_logic.dart @0x38db5b4`): at most 3 attempts (loop counter compared with `cmp x0, #3`, unboxed, `@0x38db5f4`, so 3). Before every attempt except the first (`cmp x0, #0`, unboxed, `@0x38db610`) it waits for the constant `Duration` `pp+0x18ac0`, `off_8: int(0x1e8480)` = 2,000,000 microseconds = 2 s (a pool object value, not a register immediate, so the Smi rule does not apply; awaited at `@0x38db634`). Each attempt waits for the query callback, success or failure (completer completed in the closure `@0x38dbb1c`). The loop ends early as soon as `tcpIp` is non-empty and not `"0.0.0.0"` (`@0x38db740`, `@0x38db75c`). Worst case: 2 waits of 2 s plus 3 request round trips.
- No polling: the page does not re-read the state after `set_modbus_setting`.

## Failure paths

UI texts for the toast keys below are listed on [../devices/modbus.md](../devices/modbus.md#ui-texts). Error codes are catalogued in `api/errors.md`; no code is evaluated by this flow.

- Device Wi-Fi offline, Modbus TCP requested: toast `modbuswifiOfflinetoast`, nothing is sent (`home_assistant_logic.dart @0x38dbff4`).
- Device Wi-Fi offline and no local connection, RTU requested: toast `deviceWifiOfflineDialogTitle`, nothing is sent (`home_assistant_logic.dart @0x38dc0cc`).
- Risk dialog cancelled: nothing changes (closure `home_assistant_logic.dart @0x38dc8d4`, ignored in `home_assistant_page.dart @0x38dc9f8`).
- Invalid RTU id: the dialog shows `exceedTheLimit` and keeps Save disabled (`home_assistant_logic.dart @0x38dac48`, `@0x38daca0`).
- Bluetooth action not successful: loading dismissed, switch restored, toast `modbusBluethFaildTips`; the cloud request is not sent (`home_assistant_logic.dart @0x38daf14` to `@0x38daf68`).
- No IP after three attempts (step 12): no message; the request in step 13 is sent anyway and the page shows `"--"` for the IP (`getTcpIpFormat`, `home_assistant_logic.dart @0x38dc60c`).
- `set_modbus_setting` fails (any code): toast `requestTimeout`, switch and RTU id restored to the cached values (`home_assistant_logic.dart @0x38db2dc`, `statusCheck` `@0x38dbc38`).
- `query_modbus_setting` fails: logged only; the menu stays hidden, or step 12 counts it as an attempt without an IP (`home_assistant_logic.dart @0x38db93c`).
- Menu blocked for a site member opened from device settings: toast `addedToStationSetting` (`communication_setting_menu_controller.dart @0x2cd47bc`).
- EV charger variant: a failed property write shows `failed` and reloads the values; a lost Modbus link (error bit 32 of `errorCodeArray`) shows `evModbusConnectTips`. Both are described on [../devices/modbus.md](../devices/modbus.md#ev-charger-modbus-tcp-device-properties).

## Known unknowns

- Whether the cloud pushes `set_modbus_setting` to the device on the cloud path, and how long the device needs before Modbus TCP answers on the reported IP and port.
- Why the app re-reads the IP before (not after) enabling Modbus TCP; a plausible reading is that the device reports its IP only while online, but this is not verified.
- Whether the server rejects a TCP enable when no IP is known.
- How the IoT kit carries `action_ha_communication_setting` over Bluetooth (owner: [../devices/modbus.md](../devices/modbus.md#known-unknowns)).
