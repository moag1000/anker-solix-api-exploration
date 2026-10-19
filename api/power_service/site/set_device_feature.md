> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# set_device_feature

## Purpose

Sets the feature relations (`rel_bizs`) of an EV charger inside a site; the EV charger app uses it when it adds a charger to a station (features `greenpro` and `elb`) or removes it.

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (docstring list, comment "Set device feature for site_id and smart_plug list, may require owner, usage unknown, {\"site_id\": siteId, \"sma..."); the comment names a smart plug list, the 3.24.3 sender sends an EV charger list.

## Method+URL

`POST /power_service/v1/site/set_device_feature` (asm-traced). Sender: `AKIotEVChargeCommand.setEvChargerStationFeature` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x3960204`). The path literal has no leading slash (`@0x396035c`), the method is the string `"POST"` (`@0x3960374`), and the map keys `path`, `method`, `param` are stored at `@0x3960354`, `@0x3960368`, `@0x3960380`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x39603a8`, call `@0x39603b8`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../sdk_senders.md](../../sdk_senders.md#the-common-envelope), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, dynamic>` map of two pairs (`r2 = 8`, `@0x3960234`); the second value is a growable list with one `<String, Object>` map (`r1 = <Map<String, Object>>` `@0x39602c4`, list length raw `2` `@0x39602dc`, so 1).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | String | yes | `<site id>` | `ev_charge_command.dart @0x3960240`; third argument of the function |
| `ev_charger` | list of map (one element) | yes | `[ { "device_sn": "...", "rel_bizs": ["greenpro", "elb"] } ]` | `ev_charge_command.dart @0x3960254`; the list is stored at `@0x39602ec` |
| `ev_charger[].device_sn` | String | yes | `<charger sn>` | `ev_charge_command.dart @0x396026c`; first argument |
| `ev_charger[].rel_bizs` | list of String | yes | `["greenpro", "elb"]` | `ev_charge_command.dart @0x3960280`; second argument. `EvSelectStationLogic._executeAddSiteDevice` passes the list `["greenpro", "elb"]` (`evselect_station_logic.dart @0x39642c0`, `@0x39642cc`, call `@0x3964300`); the other callers' lists were not read |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): `handle` is called without a type argument (`stp x16, NULL`, `@0x39603a4`).

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "site_id": "<site id>", "ev_charger": [ { "device_sn": "<charger sn>", "rel_bizs": [ "greenpro", "elb" ] } ] }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- `LoadBalancingLogic.disConnectDevice` (`ev_charger/src/ev_charger/page/home/load_balancing/load_balancing_logic.dart @0x395fe9c`)
- `LoadBalancingLogic._executeStationDisconnect` (`ev_charger/src/ev_charger/page/home/load_balancing/load_balancing_logic.dart @0x3961520`)
- `EvSelectStationLogic.removeFromStationAndBind` (`ev_charger/src/ev_charger/page/home/load_balancing/select_station/evselect_station_logic.dart @0x3963eb8`)
- `EvSelectStationLogic._executeAddSiteDevice` (`ev_charger/src/ev_charger/page/home/load_balancing/select_station/evselect_station_logic.dart @0x3964300`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool as `pp+0x82f10` without and `pp+0x125a00` with a leading slash; the 3.18.0 sender of the slash form was `setRemainPluginStatus`, a smart-plug call). 3.24.3: the EV charger command sender uses the no-slash literal (`ev_charge_command.dart @0x396035c`), and the pool still holds both forms. The sender function has no literal difference between 3.18.0 and 3.24.3 (`tools/cmp_since.py`: ordered string, integer and type literals compared; branch logic not compared). since: ≤3.18.0.

## Known unknowns

- The server-side meaning of `rel_bizs` values beyond `greenpro` and `elb` is not known.
- The smart-plug use named by upstream (and by the 3.18.0 sender `setRemainPluginStatus`) uses a different body; that sender is not documented here (not in the 3.24.3 scope).
- Whether the call needs the site owner is not known.

## Device-tested by

none
