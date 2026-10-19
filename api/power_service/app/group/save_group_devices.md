> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# save_group_devices

## Purpose

Adds sub-devices to the group of an EV charger (the meter or other devices of a load-balancing group).

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (line 286, docstring list of endpoints "neither implemented nor explored"); no comment on this entry

## Method+URL

`POST /power_service/v1/app/group/save_group_devices` (asm-traced). Sender: `AKIotEVChargeCommand.saveGroupDevices` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x3f9b504`). The path literal has no leading slash (`@0x3f9b624`), the method is the string `"POST"` (`@0x3f9b63c`), and the map keys `path`, `method`, `param` are stored at `@0x3f9b61c`, `@0x3f9b630`, `@0x3f9b648`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x3f9b670`, call `@0x3f9b680`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#the-common-envelope), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, dynamic>` map. The element map of the list is `SubDeviceModel.toJson` (`ev_charger/src/ev_charger/model/group_device_model.dart @0x27e74c8`; the mapping closure at `@0x27e748c` calls it): `sub_sn` (`@0x27e74e8`), `sub_pn` (`@0x27e7504`), `rel_bizs` (`@0x27e751c`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `<device sn>` | `ev_charge_command.dart @0x3f9b53c` |
| `sub_devices` | list of map | yes | `[ { "sub_sn": "...", "sub_pn": "...", "rel_bizs": [ ... ] } ]` | `ev_charge_command.dart @0x3f9b550`; the sub-devices to add (mapped with the closure at `@0x3f9b55c`) |
| `<list>[].sub_sn` | String? | yes | `<sub device sn>` | `group_device_model.dart @0x27e74e8` |
| `<list>[].sub_pn` | String? | yes | `<sub device pn>` | `group_device_model.dart @0x27e7504` |
| `<list>[].rel_bizs` | List? | yes | `["greenpro", "elb"]` | `group_device_model.dart @0x27e751c`; the values are the feature names of [set_device_feature](../../site/set_device_feature.md) |

The key is `sub_devices` here, but `sub_device_list` on [delete_group_devices](delete_group_devices.md).

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): `handle` is called without a type argument.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "device_sn": "<device sn>", "sub_devices": [ { "sub_sn": "<sub sn>", "sub_pn": "<sub pn>", "rel_bizs": [ "elb" ] } ] }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `AddDevicesLogic.handleLoadBalancingSetting` (`charging/ui/page/device/main/sitation_energy_system/station_home_settings/add_devices/add_devices_logic.dart @0x3f9a370`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x98b48`); the sender function has the same sequence of string, integer and type literals in 3.18.0 (compared with a throwaway script, not committed). Not new in 3.24.3: the Task 3.1b inventory change (slashless URL literals) made the URL visible, nothing changed in the app. 3.24.3: present, unchanged. since: ≤3.18.0.

## Known unknowns

- The difference between `save_group_devices` and `force_save_group_devices` (presumably that the forced variant overrides a conflict the plain one rejects) is not documented in the app; both are sent from the add-devices flows.
- No response was captured; the sender ignores the answer body.

## Device-tested by

none
