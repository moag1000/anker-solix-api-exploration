> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# delete_group_devices

## Purpose

Removes sub-devices from the group of an EV charger (for example when the charger is disconnected from load balancing or the meter is removed).

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (line 288, docstring list of endpoints "neither implemented nor explored"); no comment on this entry

## Method+URL

`POST /power_service/v1/app/group/delete_group_devices` (asm-traced). Sender: `AKIotEVChargeCommand.deleteGroupDevices` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x396062c`). The path literal has no leading slash (`@0x396074c`), the method is the string `"POST"` (`@0x3960764`), and the map keys `path`, `method`, `param` are stored at `@0x3960744`, `@0x3960758`, `@0x3960770`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x3960798`, call `@0x39607a8`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#the-common-envelope), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, dynamic>` map. The element map of the list is `SubDeviceModel.toJson` (`ev_charger/src/ev_charger/model/group_device_model.dart @0x27e74c8`; the mapping closure at `@0x27e748c` calls it): `sub_sn` (`@0x27e74e8`), `sub_pn` (`@0x27e7504`), `rel_bizs` (`@0x27e751c`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `<device sn>` | `ev_charge_command.dart @0x3960664` |
| `sub_device_list` | list of map | yes | `[ { "sub_sn": "...", "sub_pn": "...", "rel_bizs": [ ... ] } ]` | `ev_charge_command.dart @0x3960678`; the list of sub-devices to remove (the function maps its second argument with the closure at `@0x3960684`) |
| `<list>[].sub_sn` | String? | yes | `<sub device sn>` | `group_device_model.dart @0x27e74e8` |
| `<list>[].sub_pn` | String? | yes | `<sub device pn>` | `group_device_model.dart @0x27e7504` |
| `<list>[].rel_bizs` | List? | yes | `["greenpro", "elb"]` | `group_device_model.dart @0x27e751c`; the values are the feature names of [set_device_feature](../../site/set_device_feature.md) |

Whether an empty list deletes the whole group is not known; the callers listed below are the load-balancing disconnect and station flows.

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): `handle` is called without a type argument.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "device_sn": "<device sn>", "sub_device_list": [ { "sub_sn": "<sub sn>", "sub_pn": "<sub pn>", "rel_bizs": [ "elb" ] } ] }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `LoadBalancingLogic.disConnectDevice` (`ev_charger/src/ev_charger/page/home/load_balancing/load_balancing_logic.dart @0x395fb78`)
- `EvSelectStationLogic.removeMeterAndBind` (`ev_charger/src/ev_charger/page/home/load_balancing/select_station/evselect_station_logic.dart @0x3963af4`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x82ef8`); the sender function has no literal difference between 3.18.0 and 3.24.3 (`tools/cmp_since.py`: ordered string, integer and type literals compared; branch logic not compared). Not new in 3.24.3: the Task 3.1b inventory change (slashless URL literals) made the URL visible. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- The difference between `save_group_devices` and `force_save_group_devices` (presumably that the forced variant overrides a conflict the plain one rejects) is not documented in the app; both are sent from the add-devices flows.
- No response was captured; the sender ignores the answer body.

## Device-tested by

none
