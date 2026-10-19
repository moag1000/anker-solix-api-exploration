> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# delete_installer_inviting_member

## Purpose

Withdraws the invitation of an installer to a device (the owner removes the installer from the device's invited list).

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (line 471, no comment).

## Method+URL

`POST /charging_hes_svc/share_device/delete_installer_inviting_member` (asm-traced). Sender: `DeviceShareNetwork.deleteInstallerInvite` (`ev_charger/src/ev_charger/page/home/setting/device_share_members/network/device_share_network.dart @0x4309fd0`); the path literal `charging_hes_svc/share_device/delete_installer_inviting_member` is loaded at `@0x430a048` and passed to `AkNetwork.requestHttp` (`@0x430a058`) with the named argument `params`; the method is fixed to `POST` inside the helper (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`). The URL belongs to the `charging_hes_svc` service.

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork.requestHttp` (`device_share_network.dart`, call `@0x430a058`): the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory row says `encrypted: false` with the note "plain callee; callee default needEncryption=true"; that note does not apply, because `AkNetwork.requestHttp` has no `needEncryption` switch and goes straight to the SDK (mechanics: [../../sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)). Failures are turned into a `DeviceShareException` (`errorToDeviceShareException`) by the sender.

## Request

Body (`params`) is a `<String, dynamic>` map of two pairs (`r2 = 8`, `@0x430a008`); the keys are camelCase.

| field | type | required | example | source |
|---|---|---|---|---|
| `installerUserId` | String | yes | `<installer user id>` | `device_share_network.dart @0x430a010`; first argument (the `installerUserId` of the list item) |
| `deviceSn` | String | yes | `<device sn>` | `device_share_network.dart @0x430a024`; second argument |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the sender parses nothing; failures are rethrown as `DeviceShareException` (`@0x430a0c8`).

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "installerUserId": "<installer user id>", "deviceSn": "<device sn>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- an anonymous closure in `DeviceShareInstallerListLogic` (`ev_charger/src/ev_charger/page/home/setting/device_share_installer/device_share_installer_list_logic.dart @0x4309e58`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x11edc8`); the sender function was not compared function by function. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- Whether the call also ends an already accepted installer share, or only a pending invitation (the URL name says "inviting member"), is not known.

## Device-tested by

none
