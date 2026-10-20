> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# replace_group_devices

## Purpose

Replaces the sub-devices of the group of an EV charger: the old list is swapped for a new list in one call (the app calls the function `updateGroupDevices`).

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (line 284, docstring list of endpoints "neither implemented nor explored"); no comment on this entry

## Method+URL

`POST /power_service/v1/app/group/replace_group_devices` (asm-traced). Sender: `AKIotEVChargeCommand.updateGroupDevices` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x3f9b2e0`). The path literal has no leading slash (`@0x3f9b490`), the method is the string `"POST"` (`@0x3f9b4a8`), and the map keys `path`, `method`, `param` are stored at `@0x3f9b488`, `@0x3f9b49c`, `@0x3f9b4b4`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x3f9b4dc`, call `@0x3f9b4ec`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#the-common-envelope), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, dynamic>` map of three pairs (`r2 = 12`, `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x3f9b310`). The element map of the list is `SubDeviceModel.toJson` (`ev_charger/src/ev_charger/model/group_device_model.dart @0x27e74c8`; the mapping closure at `@0x27e748c` calls it): `sub_sn` (`@0x27e74e8`), `sub_pn` (`@0x27e7504`), `rel_bizs` (`@0x27e751c`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `<device sn>` | `ev_charge_command.dart @0x3f9b31c` |
| `old_sub_device_list` | list of map | yes | `[ { "sub_sn": "...", "sub_pn": "...", "rel_bizs": [ ... ] } ]` | `ev_charge_command.dart @0x3f9b330`; mapped with the closure at `@0x3f9b33c` |
| `new_sub_device_list` | list of map | yes | `[ { "sub_sn": "...", "sub_pn": "...", "rel_bizs": [ ... ] } ]` | `ev_charge_command.dart @0x3f9b3bc`; mapped with the closure at `@0x3f9b3c8` |
| `<list>[].sub_sn` | String? | yes | `<sub device sn>` | `group_device_model.dart @0x27e74e8` |
| `<list>[].sub_pn` | String? | yes | `<sub device pn>` | `group_device_model.dart @0x27e7504` |
| `<list>[].rel_bizs` | List? | yes | `["greenpro", "elb"]` | `group_device_model.dart @0x27e751c`; the values are the feature names of [set_device_feature](../../site/set_device_feature.md) |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): `handle` is called without a type argument.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "device_sn": "<device sn>", "old_sub_device_list": [ { "sub_sn": "<old sub sn>", "sub_pn": "<pn>", "rel_bizs": [ "elb" ] } ], "new_sub_device_list": [ { "sub_sn": "<new sub sn>", "sub_pn": "<pn>", "rel_bizs": [ "elb" ] } ] }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `AddDevicesLogic.handleLoadBalancingSetting` (`charging/ui/page/device/main/sitation_energy_system/station_home_settings/add_devices/add_devices_logic.dart @0x3f9a4fc`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x98b38`); the sender function has no literal difference between 3.18.0 and 3.24.3 (`tools/cmp_since.py`: ordered string, integer and type literals compared; branch logic not compared). Not new in 3.24.3: the inventory learned URL literals without a leading slash, which made the URL visible. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- What the server does when `old_sub_device_list` does not match the stored group is not known.

## Device-tested by

none
