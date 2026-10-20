> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_devices_power_config

## Purpose

Reads the power configuration (input and output power settings) of several devices in one call; the grid connection settings use it to show and set the default output power of devices.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /devicecontrol/v1/get_devices_power_config` (asm-traced): URL literal `@0x2af18c8` in `GridConnectUtil.getBatchPowerConfig` (`settings/src/sdk/util/grid_connect_util.dart @0x2af17a4`, static), method object `Method.post` (pool entry `pp+0xa7e0`, `@0x2af18c0`).

## Encrypted?

Yes by wrapper (asm-traced): ``getBatchPowerConfig`` calls `encryptionRequestHttp` (`settings/src/sdk/util/grid_connect_util.dart @0x2af18f0`) without passing `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../encryption.md)); asm alone does not decide it.

## Request

Map literal with one pair (`r2 = 4`, `@0x2af183c`).

| field | type | required | example | source |
|---|---|---|---|---|
| `devices` | list of maps | yes | `[ { "device_sn": "<device sn>" } ]` | `settings/src/sdk/util/grid_connect_util.dart @0x2af1844`; value is the function argument stored at `@0x2af1854` |

Element layouts built by the callers:

| caller | element keys | source |
|---|---|---|
| `GridConnectedSettingsController.setTotalPower` (`settings/src/common/page/grid_connected_settings/grid_connected_settings_controller.dart @0x2af1044`, call `@0x2af1224`) | `device_sn` | closure `@0x2af2c9c`, key `@0x2af2cc0`; the elements come from `SiteGridPowerInfo` objects (`.map(...).toList()`) |
| `DeviceInitParameterService._getDeviceOutputPowerInfo` (`settings/src/service/site_settings_service_impl.dart @0x35154c4`, call `@0x35156fc`) | `device_sn`, `install_method`, `package_num` | `@0x351566c`, `@0x3515680`, `@0x3515694`; a one-element growable list (`@0x35156d8`, length field raw `2`, `@0x35156ec`, a tagged length, so 1); the values are the device's install method and package count |

## `param_type`/`cmd`

n/a

## Response model (link)

`DevicePowerConfigItem` ([../../models/device_power_config.md](../../models/device_power_config.md)), `fromJson` called at `settings/src/sdk/util/grid_connect_util.dart @0x2af212c` for each element of the list `power_configs` (see Response).

## Response

The success closure (`settings/src/sdk/util/grid_connect_util.dart @0x2af1920`) checks that the payload is a `Map<String, dynamic>` and reads one key.

| field | type | required | example | source |
|---|---|---|---|---|
| `power_configs` | list of maps | yes | `[ { "device_sn": "...", "config": ..., "output": ..., "input": ... } ]` | `@0x2af1a10`, `@0x2af1af0`; each element is parsed by `DevicePowerConfigItem.fromJson` (`@0x2af212c`) and the result is returned as a list |

The failure closure (`small_charging_platform/src/screen_setting/clock_style/page/clock_style_logic.dart @0x2864f08`, a shared closure) forwards the code and message to the caller.

## Example request/response

Request, synthesized

```json
{ "devices": [ { "device_sn": "<device sn>", "install_method": 1, "package_num": 1 } ] }
```

The values of `install_method` and `package_num` are placeholders. Response: no captured response; the element keys are on the model page.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or logs it; the shared transport codes are in [encryption.md](../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../errors.md).

## Callers in app

- `GridConnectUtil.getBatchPowerConfig` (`settings/src/sdk/util/grid_connect_util.dart @0x2af17a4`), called from `GridConnectedSettingsController` (`setTotalPower` `@0x2af1044` and further calls `@0x2af3edc`, `@0x2af50e8`, `@0x3a533e4`) and from `DeviceInitParameterService._getDeviceOutputPowerInfo` (`@0x35154c4`): the grid connection settings page and the device initialisation of the site settings (package `settings`).

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 pool as a code-referenced URL; see the inventory row `since`). 3.24.3: present (new). since: 3.24.3. `DevicePowerConfigItem` is new in 3.24.3.

## Known unknowns

- The value types of `config`, `output` and `input` in the answer and the meaning of `install_method` and `package_num` values are not decoded. — reclassified: server (2026-10-20: value types and install-method numbers are server data)
- Server behaviour is not known.

## Device-tested by

none
