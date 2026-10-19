> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_installer_invited_list

## Purpose

Lists the installers that were invited to a device (masked email, installer user id, source type); the installer-sharing screen of the EV charger settings uses it.

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (line 473, no comment).

## Method+URL

`POST /charging_hes_svc/share_device/get_installer_invited_list` (asm-traced). Sender: `DeviceShareNetwork.getDeviceShareInstallerList` (`ev_charger/src/ev_charger/page/home/setting/device_share_members/network/device_share_network.dart @0x2aaf398`); the path literal `charging_hes_svc/share_device/get_installer_invited_list` is loaded at `@0x2aaf3f8` and passed to `AkNetwork.requestHttp` (`@0x2aaf408`) with the named argument `params`; the method is fixed to `POST` inside the helper (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`). The URL belongs to the `charging_hes_svc` service.

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork.requestHttp` (`device_share_network.dart`, call `@0x2aaf408`): the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory row says `encrypted: false` with the note "plain callee; callee default needEncryption=true"; that note does not apply, because `AkNetwork.requestHttp` has no `needEncryption` switch and goes straight to the SDK (mechanics: [../../sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)). Failures are turned into a `DeviceShareException` (`errorToDeviceShareException`) by the sender.

## Request

Body (`params`) is a `<String, dynamic>` map of one pair (`r2 = 4`, `@0x2aaf3c8`). The key is camelCase.

| field | type | required | example | source |
|---|---|---|---|---|
| `deviceSn` | String | yes | `<device sn>` | `device_share_network.dart @0x2aaf3d0`; value is the argument (`@0x2aaf3e0`) |

## `param_type`/`cmd`

n/a

## Response model (link)

`DeviceShareInstallerListModel` ([../../../models/device_share_models.md](../../../models/device_share_models.md#deviceshareinstallerlistmodel)): `DeviceShareInstallerListModel.fromJson` is called on the helper's result (`device_share_network.dart @0x2aaf43c`).

## Response

An exception is rethrown as a `DeviceShareException` (`@0x2aaf4a0`).

| field | type | required | example | source |
|---|---|---|---|---|
| `installerList` | list of `DeviceShareInstallerItem` | no | `[ { "installerUserId": "...", "deviceSn": "...", "installerMaskedEmail": "a***@example.org", "sourceType": 1 } ]` | `device_share_installer_list_model.dart @0x2aaf4fc`; item keys `installerUserId`, `deviceSn`, `installerMaskedEmail`, `sourceType` (`@0x2aaf9a4` to `@0x2aafb3c`) |

## Example request/response

Request, synthesized

```json
{ "deviceSn": "<device sn>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `DeviceShareInstallerListLogic._getDeviceShareInstallerList` (`ev_charger/src/ev_charger/page/home/setting/device_share_installer/device_share_installer_list_logic.dart @0x2aaf320`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x824b8`); the sender function was not compared function by function. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- The meaning of `sourceType` is not decoded.
- Whether the installer app (variant of the same URLs) reads the same list is not known.

## Device-tested by

none
