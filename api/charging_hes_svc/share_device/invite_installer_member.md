> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# invite_installer_member

## Purpose

Invites an installer, by email, to one or more devices (the owner shares the devices with an installer so that the installer can commission or service them).

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (line 472, no comment).

## Method+URL

`POST /charging_hes_svc/share_device/invite_installer_member` (asm-traced). Sender: `DeviceShareNetwork.shareDeviceInstallerInvite` (`ev_charger/src/ev_charger/page/home/setting/device_share_members/network/device_share_network.dart @0x396be18`); the path literal `charging_hes_svc/share_device/invite_installer_member` is loaded at `@0x396be90` and passed to `AkNetwork.requestHttp` (`@0x396bea0`) with the named argument `params`; the method is fixed to `POST` inside the helper (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`). The URL belongs to the `charging_hes_svc` service.

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork.requestHttp` (`device_share_network.dart`, call `@0x396bea0`): the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory row says `encrypted: false` with the note "plain callee; callee default needEncryption=true"; that note does not apply, because `AkNetwork.requestHttp` has no `needEncryption` switch and goes straight to the SDK (mechanics: [../../sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)). Failures are turned into a `DeviceShareException` (`errorToDeviceShareException`) by the sender.

## Request

Body (`params`) is a `<String, dynamic>` map of two pairs (`r2 = 8`, `@0x396be50`); the keys are camelCase.

| field | type | required | example | source |
|---|---|---|---|---|
| `installerEmail` | String | yes | `installer@example.org` | `device_share_network.dart @0x396be58`; first argument |
| `deviceSnList` | list of String | yes | `["<device sn>"]` | `device_share_network.dart @0x396be6c`; second argument, passed through unchanged (element type not shown) |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the sender parses nothing; failures are rethrown as `DeviceShareException` (`@0x396bf10`).

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "installerEmail": "installer@example.org", "deviceSnList": ["<device sn>"] }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `DeviceShareInstallerInviteLogic.onTapInvite` (`ev_charger/src/ev_charger/page/home/setting/device_share_installer/device_share_installer_invite_logic.dart @0x396bac4`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x82620`); the sender function was not compared function by function. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- The element type of `deviceSnList` is not read in the sender (strings expected).
- What the installer sees after accepting (commissioning access, read-only access) is not known; see the installer service ([../../charging_hes_installer_svc/README.md](../../charging_hes_installer_svc/README.md)).

## Device-tested by

none
