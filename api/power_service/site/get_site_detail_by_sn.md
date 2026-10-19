> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_site_detail_by_sn

## Purpose

Reverse lookup: given a device serial number, returns the site that holds the device (site id, name, image, site type, member devices with their feature relations); the EV charger load-balancing screens use it to find the station a charger is linked to.

## Upstream name

`site_detail_by_sn` (upstream-confirmed, `api/apitypes.py` line 107; upstream comment: "needs owner, {\"device_sn\": deviceSn}, site_info from site list response").

## Method+URL

`POST /power_service/v1/site/get_site_detail_by_sn` (asm-traced). Sender: `AKIotEVChargeCommand.getEvChargerSiteInfo` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x27e6e08`). The path literal has no leading slash (`@0x27e6e60`), the method is the string `"POST"` (`@0x27e6e78`), and the map keys `path`, `method`, `param` are stored at `@0x27e6e58`, `@0x27e6e6c`, `@0x27e6e84`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x27e6f08`, call `@0x27e6f18`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../sdk_senders.md](../../sdk_senders.md#the-common-envelope), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, String>` map of one pair (`r2 = 4`, `@0x27e6e94`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `<device sn>` | `ev_charge_command.dart @0x27e6e9c` |

This is the "which site is this device in" lookup. Upstream confirms the body and notes that the answer carries `site_info` in the shape of the site list entries and that the call needs the owner account.

## `param_type`/`cmd`

n/a

## Response model (link)

`EvChargerSiteInfoModel` ([../../../models/ev_charger_device_models.md](../../../models/ev_charger_device_models.md#evchargersiteinfomodel)), taken from the type argument of `handle<EvChargerSiteInfoModel>` (ev_charge_command.dart `@0x27e6ef8`)

## Response

The SDK result is typed `IoTAKResult<EvChargerSiteInfoModel>`; the keys are on the model page. The wrapper `data` of `EvChargerSiteInfoModel.fromJson` is described there. The caller reads the result type before using the data.

| field | type | required | example | source |
|---|---|---|---|---|
| `data` | String (JSON text) or map | no |  | `ev_charger_site_info_model.dart @0x45b03a0` |
| `site_info` | object (`SiteInfo`) | no | `{ "site_id": "...", "site_name": "...", "site_device_list": [ ... ] }` | `ev_charger_site_info_model.dart @0x45b0498`; keys of `SiteInfo` (`site_id`, `site_name`, `site_img`, `device_type_list`, `ms_type`, `power_site_type`, `is_allow_delete`, `support_device_models`, `current_site_device_models`, `site_device_list`) and `SiteDevice` on [models/ev_charger_device_models.md](../../../models/ev_charger_device_models.md#evchargersiteinfomodel) |

## Example request/response

Request, synthesized

```json
{ "device_sn": "<device sn>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- `LoadBalancingLogic.getConnectInfo` (`ev_charger/src/ev_charger/page/home/load_balancing/load_balancing_logic.dart @0x27e656c`)
- `EvSelectStationLogic.getLinkedStationInfo` (`ev_charger/src/ev_charger/page/home/load_balancing/select_station/evselect_station_logic.dart @0x3965018`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x83020`); the sender function has no literal difference between 3.18.0 and 3.24.3 (`tools/cmp_since.py`: ordered string, integer and type literals compared; branch logic not compared). Not new in 3.24.3: the inventory learned URL literals without a leading slash, which made the URL visible. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- The EV charger app is the only sender found; whether other apps or screens of this APK send the URL is not known (the pool string is shared, the inventory finds one sender).
- Whether the call works for a member account (upstream: needs owner) is not recorded here.
- No response was captured.

## Device-tested by

none
