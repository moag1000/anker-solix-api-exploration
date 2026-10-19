> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_group_devices

## Purpose

Reads the group of an EV charger: the sub-devices (for example the meter or smart plug) that are grouped with a charger, with their feature relations; the load-balancing and device-removal flows use it.

## Upstream name

`get_device_group` (upstream-confirmed, `api/apitypes.py` line 147; upstream comment: "works as member, shows whether device is grouped with sub devices, {\"device_sn\": deviceSn}").

## Method+URL

`POST /power_service/v1/app/group/get_group_devices` (asm-traced). Sender: `AKIotEVChargeCommand.getGroupDevices` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x27e7154`). The path literal has no leading slash (`@0x27e72b8`), the method is the string `"POST"` (`@0x27e72d0`), and the map keys `path`, `method`, `param` are stored at `@0x27e72b0`, `@0x27e72c4`, `@0x27e72dc`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x27e730c`, call `@0x27e731c`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#the-common-envelope), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, String>` map (`@0x27e7214`) that starts empty. The named arguments `deviceSn` and `subSn` (`SetupParameters` `@0x27e7160`) add their key only when they are not null (null checks `@0x27e7224`, `@0x27e7250`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | no | `<device sn>` | `ev_charge_command.dart @0x27e7238` (`r2 = "device_sn"` before the map `[]=` call at `@0x27e7240`) |
| `sub_sn` | String | no | `<sub device sn>` | `ev_charge_command.dart @0x27e7268` (added only when `subSn` is not null) |

Upstream confirms the `device_sn` form. The callers pass `deviceSn` when they want the group of a charger; whether any caller sends `sub_sn` alone (to find the group a sub-device belongs to) was not traced.

## `param_type`/`cmd`

n/a

## Response model (link)

`GroupDeviceModel` ([../../../../models/ev_charger_device_models.md](../../../../models/ev_charger_device_models.md#groupdevicemodel)), taken from the type argument of `handle<GroupDeviceModel>` (ev_charge_command.dart `@0x27e72fc`)

## Response

The SDK result is typed `IoTAKResult<GroupDeviceModel>`; the keys are on the model page. The wrapper `data` of `GroupDeviceModel.fromJson` is described there. The caller reads the result type before using the data.

| field | type | required | example | source |
|---|---|---|---|---|
| `data` | String (JSON text) or map | no |  | `group_device_model.dart @0x45b4f2c` |
| `device_sn`, `device_pn`, `sub_device_list` | see model page | no | `{ "device_sn": "...", "device_pn": "...", "sub_device_list": [ { "sub_sn": "...", "sub_pn": "...", "rel_bizs": [ ... ] } ] }` | `group_device_model.dart @0x45b5018`, `@0x45b50a0`, `@0x45b5128`; [../../../../models/ev_charger_device_models.md](../../../../models/ev_charger_device_models.md#groupdevicemodel) |

## Example request/response

Request, synthesized

```json
{ "device_sn": "<device sn>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `LoadBalancingLogic.getConnectInfo` (`ev_charger/src/ev_charger/page/home/load_balancing/load_balancing_logic.dart @0x27e6288`)
- `EvSelectStationLogic.removeMeterAndBind` (`ev_charger/src/ev_charger/page/home/load_balancing/select_station/evselect_station_logic.dart @0x3963a04`)
- `ShellyHomeLogic.handleRemoveEvent` (`charging/ui/page/device/third_party_device/shelly/shellyhome/shellyhome_logic.dart @0x4006168`)
- `A17x7settingLogic.handleRemoveEvent` (`charging/ui/page/device/a17x7/a17x7setting/a17x7setting_logic.dart @0x3dce4e4`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x82f00`); the sender function has no literal difference between 3.18.0 and 3.24.3 (`tools/cmp_since.py`: ordered string, integer and type literals compared; branch logic not compared). Not new in 3.24.3: the Task 3.1b inventory change (slashless URL literals) made the URL visible. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- Which `rel_bizs` values exist besides `greenpro` and `elb` is not known.
- No response was captured.

## Device-tested by

none
