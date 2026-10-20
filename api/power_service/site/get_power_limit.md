> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_power_limit

## Purpose

Reads the station power limit state of a site: the selectable output limits, the legal limit, the per-device list and, since 3.24.3, the settings of the "DIY" unlock prompt.

## Upstream name

`get_site_power_limit` is the `API_ENDPOINTS` key in `api/apitypes.py`; the library method is `AnkerSolixApi.get_power_limit(siteId, fromFile)` in `api/api.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/site/get_power_limit` (asm-traced): URL string at `http_request_repository_impl.dart @0x2379094`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x237908c`, in `HttpRequestControllerImpl::getSitePowerLimit` (`http_request_repository_impl.dart @0x2378fb4`).

## Encrypted?

Yes (asm-traced): sent through `HttpRequestControllerImpl::encryptionRequestHttp` (`http_request_repository_impl.dart @0x23790c4`). The scheme is described in `api/encryption.md`.

## Request

The body starts as a one-pair map literal (2 slots, raw `r2 = 4`, `@0x2379008`) holding `site_id`; `app_ability` is added afterwards with `[]=` (`@0x2379048` to `@0x2379050`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | String | yes | `"<site_id>"` | `http_request_repository_impl.dart @0x2379010` (value from parameter r5) |
| `app_ability` | object (`Map<String, dynamic>`) | sent by the app | `{"site_power_limit": true}` | `http_request_repository_impl.dart @0x2379048` (value from parameter r2); both callers pass the map literal `{"site_power_limit": true}`: `station_power_limit_logic.dart @0x28cac40`/`@0x28cac4c` and `energy_plan_logic.dart @0x28caa50`/`@0x28caa5c` |

The upstream library sends only `site_id` (`api/api.py`, `get_power_limit()`), so `app_ability` is not required for a response; what it changes is not known (see Known unknowns).

## `param_type`/`cmd`

n/a

## Response model (link)

[`StationPowerLimitModel`](../../../models/station_power_limit.md), parsed in the success closure at `http_request_repository_impl.dart @0x23790e0` by `StationPowerLimitModel.fromJson` (`@0x2379110`).

## Response

All fields of the response object belong to the model page; this endpoint adds no wrapper fields of its own.

| field | type | required | example | source |
|---|---|---|---|---|
| (model fields) | see [`StationPowerLimitModel`](../../../models/station_power_limit.md) | | | `station_power_limit_model.dart @0x2379150` |

## Example request/response

Request, synthesized (decrypted body as built by `getSitePowerLimit`)

```json
{"site_id": "<site_id>", "app_ability": {"site_power_limit": true}}
```

Response, synthesized (keys from `StationPowerLimitModel.fromJson`; values are placeholders, not a capture)

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "site_id": "<site_id>",
    "ac_input_power_unit": "1200W",
    "ac_input_power": 1200,
    "legal_power_limit": 800,
    "parallel_type": "<parallel_type>",
    "ae100_info": null,
    "device_info": [],
    "legal_limit": 800,
    "power_limit_option": [{"limit": 800, "limit_real": 800}],
    "exceed_alarm": false,
    "unlock_default_power_type": 0,
    "unlock_pop_content": "",
    "unlock_pop_image": ""
  }
}
```

## Errors seen

None recorded. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `StationPowerLimitLogic::_getStationPowerLimit` (`station_power_limit_logic.dart @0x28cab4c`, call at `@0x28cac9c`), run from `StationPowerLimitLogic::onInit` (`@0x34b0bdc`) when the station power limit page opens; it returns early when the site id is empty (`@0x28cab98`). Flow: [../../../flows/system_output_limit.md](../../../flows/system_output_limit.md).
- `EnergyPlanLogic::getStationPowerLimit` (`energy_plan_logic.dart`, call at `@0x28caaac`), A17C1 energy plan page.
- `HttpRequestController` interface stub (`http_request_repository.dart @0x2378f8c`).

## Since/changed

3.18.0: the model parsed 9 keys (3.18.0 `station_power_limit_model.dart @0x1a56c9c`). 3.24.3: 13 keys; `ac_input_power`, `unlock_default_power_type`, `unlock_pop_content` and `unlock_pop_image` are new. Details on [the model page](../../../models/station_power_limit.md#changed-since-3180).

## Who gets the output-limit page (app gate)

Tag: asm-traced, app side only: this section says what the app shows, not what the server returns or accepts for a site. This section owns the gate rule; other pages link here.

The station power limit page (`/stationPowerLimit`, with the type-19 output slider of [set_site_device_param](set_site_device_param.md#usage-param_type-19-system-output-power-limit)) is reached from the entry row of the Station Home Settings page. The row is visible when `_isGridConnectedPowerVisible` is true (`station_home_settings_page.dart @0x3fef9ec..0x3fefa28`): condition 1 alone, or conditions 2, 3 and 4 together.

| # | condition | compare (width) | citation |
|---|---|---|---|
| 1 | `power_site_type == 18` (`t_18`, AE100 Power Dock) | `cmp w1, #0x24`, 32-bit Smi field, so 18 | `station_home_settings_logic.dart @0x28b2aa0` |
| 2 | `power_site_type == 12` (`t_12`, A17C5 SB3 Pro) | `cmp w1, #0x18`, 32-bit Smi field, so 12 | `station_home_settings_logic.dart @0x28b2e28` |
| 3 | the site's solarbank list contains pn `"A17C5"` | string compare, no integer | `station_energy_system_logic.dart @0x2377b98` |
| 4a | `legal_power_limit > 0` in the `get_power_limit` response | `cmp x2, #0`, 64-bit unboxed value after the Smi check, so 0; the field is field_13 = `legal_power_limit` by the `toJson` pairing | closure `station_energy_system_logic.dart @0x237a91c`; `station_power_limit_model.dart @0x23799c0..0x23799d4` |
| 4b | or the site has `has_combiner_box` (route argument `hasCombinerBox`) | boolean | `station_home_settings_page.dart @0x3fefa04` |

- The row is shown but not tappable unless `solarBankIsEnabled()` and `isMultiDeviceSettingsEnabled()` hold and `energySystemAvailable()` is true (`station_home_settings_page.dart @0x3fef604..0x3fef684`).
- The deeplink `/stationPowerLimit` opens the page with no guard (`station_power_limit_handler.dart @0x45e8d60`).
- The request carries `app_ability: {"site_power_limit": true}` (see Request, same fact, not repeated). No response key named `support_*`, `is_support*` or `feature*` gates the page (asm-traced for absence in the traced functions). If `power_limit_option` is empty the output picker does nothing (`station_power_limit_logic.dart @0x4354fc8`).
- Names: `power_site_type` 12 and 18 are `SolixSiteType.t_12` and `t_18` in upstream `api/apitypes.py` (upstream-confirmed); table in [../../../reference/enums.md](../../../reference/enums.md#power_site_type-upstream-solixsitetype).
- Consequence, app side: a site of the SB2 types (`t_5` A17C1, `t_10` A17C3, `t_11` A17C2) never shows the row (these values are compared elsewhere, see the [enums table](../../../reference/enums.md#power_site_type-upstream-solixsitetype); not in this gate); SB2 devices behind an AE100 dock (type 18) do reach the page. The app never sends type 19 for SB2; this proves nothing about the server.

### Per-device AC input limit flag (`supportAcLimit`)

Tag: asm-traced, app side. The flag decides the AC input limit shown per device row on the station power limit page; it is not a response key.

- Field: `DeviceInfo` field_27 (bool). `DeviceInfo.fromJson` sets it to `false` (`station_power_limit_model.dart @0x237a85c`); it is not read from JSON (the key `"supportAcLimit"` appears only in the app's own `toJson`, `@0x237a0dc`). The only writer is the `device_info` mapping closure `station_power_limit_logic.dart @0x28cb19c`, through `copyWith`.
- Rule 1 (pn list): when `device_pn` (DeviceInfo field_b) equals `"AE103"`, `"A17E2"` or `"AE111"` (string compares `@0x28cb1f0`, `@0x28cb218`, `@0x28cb244`) the flag is set to true if it was false (`copyWith(supportAcLimit: true)` `@0x28cb278`).
- Rule 2 (device value): for every other pn the flag is taken from the connected device object, `HomeDeviceManager.getDeviceBySn(device_sn)` (`@0x28cb2c0`) followed by a getter call (`@0x28cb2e8`); a missing device or null gives false (`@0x28cb2f8`). The app logs it as `mqtt_isSupportAcLimit`. When the value differs from the stored flag the row gets `copyWith(inputPower: flag ? ac_input_limit text : "1200W", supportAcLimit: flag)` (`@0x28cb3f8..0x28cb41c`, string `"1200W"` `@0x28cb408`).
- Reader: `_buildDeviceRow` stores `!supportAcLimit` (`eor x3, x2, #0x10`, `station_power_limit_view.dart @0x4357650`) as a row flag together with `status == 0` (`@0x4357658`); the effect of that flag on the row was not read.
- Source of the getter value: not resolvable, see Known unknowns.

## Known unknowns

- What `app_ability: {"site_power_limit": true}` changes in the server response compared with the upstream request that omits it.
- Whether the server requires the encrypted request path for this endpoint (the upstream library uses the plain path).
- Which `power_site_type` a given site carries is server data (scene info). The gate compares only 12 and 18; the other compares in the app are listed in the [enums table](../../../reference/enums.md#power_site_type-upstream-solixsitetype). The `where()` closure of `solarBankIsEnabled` (non-AE100 branch, `station_energy_system_logic.dart @0x23984a8`) was not decoded.
- The MQTT or attribute key behind `supportAcLimit` for pns other than AE103, A17E2 and AE111: not resolvable. The value comes from a dynamic getter call on the object `getDeviceBySn` returns (`station_power_limit_logic.dart @0x28cb2e0..0x28cb2e8` and the second call `@0x28cb330..0x28cb33c`, log label `mqtt_acPowerLimit`); the call goes through an unlinked switchable-call pool entry (`[pp+0xc59f8]`, `UnlinkedCall`), which carries no selector name. No function or getter named `*AcLimit*`, `*SupportAc*` or `*AcPowerLimit*` exists in the asm tree (grep of `asm` returns only the model/logic files and the log-label strings `a17c5_acLimit_` and `a17c2_acLimit_` at `a17c5_device_commands.dart @0x4862fb0` and `a17c2_device_commands.dart @0x4860954`), so the device class that answers is not identified.
- Whether an A17C0 appears in the `device_info` list of a site-level answer (not derivable from the app; backlog row 120 in [../../../docs/DEVICE_TEST_BACKLOG.md](../../../docs/DEVICE_TEST_BACKLOG.md)).
- The response fields are not a support indicator: an SB1 (A17C0) returns the same fields as newer devices (device-tested, see below) yet cannot set an output limit.

## Device-tested by

Source: [anker-solix-api-exploration issue #1](https://github.com/moag1000/anker-solix-api-exploration/issues/1), comment of 2026-10-19T23:20Z (community report; client and firmware not recorded).

| who | device | request | result | date | source |
|---|---|---|---|---|---|
| thomluther | SB1 (A17C0), firmware not recorded | `get_power_limit` | returns the same fields as newer devices; the device cannot set an output limit | 2026-10-19 | [issue #1](https://github.com/moag1000/anker-solix-api-exploration/issues/1) |
