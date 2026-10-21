> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# update_share

## Purpose

Removes a member from the share of an EV charger: the owner deletes the share for a user (the request carries `is_delete: true`).

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (line 372, no comment).

## Method+URL

`POST /app/devicerelation/update_share` (asm-traced). Sender: `DeviceShareNetwork.deleteDeviceShareMember` (`ev_charger/src/ev_charger/page/home/setting/device_share_members/network/device_share_network.dart @0x430b8e4`); the path literal `app/devicerelation/update_share` is loaded at `@0x430ba68` and passed to `AkNetwork.requestHttp` (`@0x430ba78`) with the named argument `params`; the method is fixed to `POST` inside the helper (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`). The app calls the path without a leading slash.

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork.requestHttp` (`device_share_network.dart`, call `@0x430ba78`): the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory row says `encrypted: false` with the note "plain callee; callee default needEncryption=true"; that note does not apply, because `AkNetwork.requestHttp` has no `needEncryption` switch and goes straight to the SDK (mechanics: [../../sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)). Failures are turned into a `DeviceShareException` (`errorToDeviceShareException`) by the sender.

## Request

Body (`params`) is a `<String, dynamic>` map of two pairs, `user_id` and `devices` (`r2 = 8`, `@0x430b91c`); `devices` is a one-element list of a `<String, Object>` map of four pairs (`r2 = 16`, `@0x430b94c`).

| field | type | required | example | source |
|---|---|---|---|---|
| `user_id` | String | yes | `<member user id>` | `device_share_network.dart @0x430b928`; first argument |
| `devices` | list of map (one element) | yes | `[ { "device_sn": "...", "sub_devices": [], "is_delete": true, "member_type": 1 } ]` | `device_share_network.dart @0x430b93c`; list built at `@0x430ba04` to `@0x430ba24` |
| `devices[].device_sn` | String | yes | `<device sn>` | `device_share_network.dart @0x430b958`; second argument |
| `devices[].sub_devices` | list | yes (constant) | `[]` | `device_share_network.dart @0x430b96c`; an empty growable list (`_GrowableList` `@0x430b980`) |
| `devices[].is_delete` | bool | yes (constant) | `true` | `device_share_network.dart @0x430b9b0`; value `true` `@0x430b9bc` |
| `devices[].member_type` | int | yes (constant) | `1` | `device_share_network.dart @0x430b9c4`; raw `2` at `@0x430b9d0`, `stur w16`, a Smi, so 1 (`tools/smi.py`) |

The URL name (`update_share`) and the constant `is_delete: true` mean that the same URL probably also updates a share when the flag is false; the app only sends the delete form.

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the sender parses nothing.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "user_id": "<member user id>", "devices": [ { "device_sn": "<device sn>", "sub_devices": [], "is_delete": true, "member_type": 1 } ] }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- an anonymous closure in `DeviceShareListLogic` (`ev_charger/src/ev_charger/page/home/setting/device_share_members/device_share_list_page/device_share_list_logic.dart @0x430b3ec`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x1256d0`); the sender function was not compared function by function. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- The role of `sub_devices` (always empty here) and of `is_delete: false` is not known.
- The meaning of `member_type` 1 (also sent by `device_invite`) is not decoded. — reclassified: server (2026-10-20: the app sends the constant 1 (decoded on this page); what the number means is not derivable from the app)

## Device-tested by

none
