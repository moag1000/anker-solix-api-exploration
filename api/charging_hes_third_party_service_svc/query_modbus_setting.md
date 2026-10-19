> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# query_modbus_setting

## Purpose

Reads the Modbus (third-party control) configuration of one device or site: which Modbus variants the device supports (TCP, RTU), which one is enabled, the RTU slave id, the device IP address and port, and links to the Home Assistant and Homey guides.

## Upstream name

`none` (no upstream name): `api/apitypes.py` has no key for this URL.

## Method+URL

`POST /charging_hes_third_party_service_svc/query_modbus_setting` (asm-traced): URL string `pp+0xb7608` at `home_assistant_logic.dart @0x38db8f4`, method object `Method.post` (pool entry `pp+0xa7e0`, `off_10: "post"`) at `@0x38db8ec`, in `HomeAssistantLogic::requestData` (`home_assistant_logic.dart @0x38db78c`). The two other senders use the same URL and method object (`communication_setting_menu_controller.dart @0x2cd4d50`, `a17x8setting_logic.dart @0x2cd4ee8`).

## Encrypted?

Yes (asm-traced): all three senders call `HttpServiceImpl::encryptionRequestHttp` (`home_assistant_logic.dart @0x38db91c`, `communication_setting_menu_controller.dart @0x2cd4d78`, `a17x8setting_logic.dart` `requestData` at `@0x2cd4e10`). The scheme is described in `api/encryption.md`. The request is sent without the loading overlay (`showLoading: false`, `home_assistant_logic.dart @0x38db904`).

## Request

The body holds exactly one key: the site id when the page was opened in a site context, otherwise the device serial number. Each sender allocates a one-pair map literal (raw `r2 = 4`, i.e. 2 slots, 1 key/value pair, `home_assistant_logic.dart @0x38db7ec` and `@0x38db85c`).

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | String | one of `siteId` / `sn` | `"<site_id>"` | `home_assistant_logic.dart @0x38db7f8` (sent when the route argument `isSite` is `true`, `@0x38db7cc`; value from `StationDeviceManager::getSiteIdByDeviceSn(deviceSn)`, `@0x38db810`); `communication_setting_menu_controller.dart @0x2cd4c4c` (station id of the menu, when its `isSite` flag is set, `@0x2cd4c34`) |
| `sn` | String | one of `siteId` / `sn` | `"<device_sn>"` | `home_assistant_logic.dart @0x38db864` (route argument `deviceSn`, `@0x38db874`); `communication_setting_menu_controller.dart @0x2cd4ca8`; `a17x8setting_logic.dart @0x2cd4e10` (always `sn`, the smart plug's serial number) |

The key names are camelCase (`siteId`, not `site_id`).

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no `fromJson` model exists. Every caller keeps the response as a raw `Map` (type test against `Map` in the success closures `home_assistant_logic.dart @0x38db9d8`, `communication_setting_menu_controller.dart @0x2cd513c`) and reads keys from it with `[]`.

## Response

Fields the app reads from the success payload. Types are what the reading code requires: a `bool` cast throws on anything else, a value that is only printed is shown with `toString()`.

| field | type | required | example | source |
|---|---|---|---|---|
| `tcpSupport` | bool | yes for the menu (cast) | `true` | `communication_setting_menu_controller.dart @0x2cd5270` (cast to `bool`), `home_assistant_logic.dart @0x35eafec`; shows the Modbus TCP card (`home_assistant_page.dart @0x38d9648`) |
| `rtuSupport` | bool | yes if `tcpSupport` is not `true` (cast) | `true` | `communication_setting_menu_controller.dart @0x2cd52d8`, `home_assistant_logic.dart @0x35eb044`; shows the Modbus RTU card (`home_assistant_page.dart @0x38d9664`) |
| `modbusStatus` | int | no (null is read as 0) | `1` | `home_assistant_logic.dart @0x35eae98`; `== 1` sets the TCP switch (raw `2` pushed as a tagged argument to `==`, `@0x35eaec4`, so 1), `== 2` sets the RTU switch (raw `4`, `@0x35eaf2c`, so 2); any other value leaves both off. Same values as the request field of [set_modbus_setting](set_modbus_setting.md#request). |
| `rtuId` | int or String (printed) | no | `1` | `home_assistant_logic.dart @0x35eaf68`, shown via `toString()` in the RTU id field; an empty text falls back to the string literal `"1"` (`@0x35eafd4`) |
| `tcpIp` | String | no | `"<device_ip>"` | `home_assistant_logic.dart @0x38dbba0`; empty or `"0.0.0.0"` (string literal, `@0x38dbc08`) counts as "no IP yet" and is displayed as `"--"` (`getTcpIpFormat`, `@0x38dc60c`) |
| `tcpPort` | any (printed) | no | `"<port>"` | `home_assistant_page.dart @0x38d9b58` |
| `rtuBand` | any (printed) | no | `"<baud_rate>"` | `home_assistant_page.dart @0x38d9ba4` (shown under the label `baudRate`) |
| `helpH5Url` | String | no | `"<url>"` | `home_assistant_logic.dart @0x35eb09c`; opened by the "Home Assistant" guide card (`home_assistant_page.dart @0x38d8b4c`) |
| `homeyH5Url` | String | no | `"<url>"` | `home_assistant_logic.dart @0x35eb128`; opened by the "Homey" guide card (`home_assistant_page.dart @0x38d8c4c`) |

The settings menu "Third-Party Control Settings" is shown only when `tcpSupport` or `rtuSupport` is `true` (`communication_setting_menu_controller.dart @0x2cd5330`; same rule for the smart plug, `a17x8setting_logic.dart @0x2cd50b4`). How the app uses these fields end to end is on [../../flows/modbus_setup.md](../../flows/modbus_setup.md); which products have the menu is on [../../devices/modbus.md](../../devices/modbus.md).

## Example request/response

Request, synthesized (decrypted body, device context)

```json
{"sn": "<device_sn>"}
```

Response, synthesized (shape only, built from the Response table; placeholder values; no captured response exists)

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "tcpSupport": true,
    "rtuSupport": true,
    "modbusStatus": 1,
    "rtuId": 1,
    "tcpIp": "<device_ip>",
    "tcpPort": "<port>",
    "rtuBand": "<baud_rate>",
    "helpH5Url": "<url>",
    "homeyH5Url": "<url>"
  }
}
```

## Errors seen

None recorded. On failure the home assistant page only logs `getCommunicationSettingInfo fail:<code> ---- <msg>` (`home_assistant_logic.dart @0x38db984`) and continues; the settings menus log the same text (shared closure `a17x8setting_logic.dart @0x2cd4d98`, also used by `communication_setting_menu_controller.dart @0x2cd4d28`) and leave the menu hidden. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `HomeAssistantLogic::requestData` (`home_assistant_logic.dart @0x38db78c`), called only from `_retryFetchIp` (`@0x38db6c0`) while the user switches Modbus TCP on and the IP is not known yet; see [../../flows/modbus_setup.md](../../flows/modbus_setup.md). UI: "Third-party control" page (route `/homeAssistantPage`).
- `CommunicationSettingMenuController::requestData` (`communication_setting_menu_controller.dart @0x2cd4c00`), called from `onInit` (`@0x3679c74`, `@0x3679c80`, and from the `ever` listener `@0x3679cdc`) and again after the page returns (closure `@0x2cd4be4`). UI: device, station and advanced settings, menu "Third-Party Control Settings" (title key `threePartyControlSettings`, `@0x4154870`). The response map is handed to the page as route argument `data` (`@0x2cd481c`).
- `A17x8settingLogic::requestData` (`a17x8setting_logic.dart @0x2cd4e10`), called from `onInit` (`@0x3466110`) and after the page returns (closure of `tapEnterHA`, `@0x3dded7c`). UI: smart plug (A17X8) settings; the response map becomes route argument `data` (`@0x3ddea9c`).

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 pool). 3.24.3: new.

## Known unknowns

- Whether the success callback receives the whole envelope or only its `data` object; the table assumes `data`, as for the other encrypted endpoints. The envelope handling in `HttpServiceImpl` was not re-traced for this page.
- The real types of `tcpPort` and `rtuBand` (the app only prints them) and the value range of `modbusStatus` beyond 0, 1 and 2.
- Whether the server answers for every device, or only for products that support Modbus (the menu hides itself when both support flags are `false`).
- Whether `siteId` and `sn` may be sent together.

## Device-tested by

none
