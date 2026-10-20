> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_shared_device

## Purpose

Lists the share entries of a device (members the EV charger is shared with, with their status) so the owner can see who has access and how many more members can be invited.

## Upstream name

`get_shared_device` (upstream-confirmed, `api/apitypes.py` line 187; upstream comment: "works as member, list device sharing details, {\"device_sn\": deviceSn}, sharing works only for EV charger or any device?").

## Method+URL

`POST /app/devicerelation/get_shared_device` (asm-traced). Sender: `DeviceShareNetwork.getDeviceShareList` (`ev_charger/src/ev_charger/page/home/setting/device_share_members/network/device_share_network.dart @0x21a4aac`); the path literal `app/devicerelation/get_shared_device` is loaded at `@0x21a4ba0` and passed to `AkNetwork.requestHttp` (`@0x21a4bb0`) with the named argument `params`; the method is fixed to `POST` inside the helper (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`). The app calls the path without a leading slash.

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork.requestHttp` (`device_share_network.dart`, call `@0x21a4bb0`): the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory row says `encrypted: false` with the note "plain callee; callee default needEncryption=true"; that note does not apply, because `AkNetwork.requestHttp` has no `needEncryption` switch and goes straight to the SDK (mechanics: [../../sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)). Failures are turned into a `DeviceShareException` (`errorToDeviceShareException`) by the sender.

## Request

Body (`params`) is a `<String, dynamic>` map of two pairs (`r2 = 8`, `@0x21a4adc`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `<device sn>` | `device_share_network.dart @0x21a4ae8`; value is the argument |
| `status` | list of int | yes | `[1, 2]` | `device_share_network.dart @0x21a4afc`; built from the constant list `[DeviceShareStatus inviting, DeviceShareStatus joined]` (pool `pp+0xaf990`, `@0x21a4b1c`) mapped to `int` by a closure (`@0x21a4b18` to `@0x21a4b30`, `toList` `@0x21a4b4c`) |

The enum `DeviceShareStatus` has five instances (`pp+0xafa80`); the constant list holds `inviting` (index 0, value field `1`, `pp.txt` entry `Obj!DeviceShareStatus@4207e11`) and `joined` (index 1, value field `2`, `Obj!DeviceShareStatus@4207df1`). That the closure returns the value field (so the list is `[1, 2]`) is UNCONFIRMED: its code (`@0x21a4a7c`) is not in the asm dump. Upstream sends only `device_sn` and notes that the call works for a member account.

## `param_type`/`cmd`

n/a

## Response model (link)

`DeviceShareListResponse` ([../../../models/device_share_models.md](../../../models/device_share_models.md#devicesharelistresponse)) with element class `DeviceShareListModel`: `DeviceShareListResponse.fromJson` is called on the helper's result (`device_share_network.dart @0x21a4bdc`); the function's return type is `Future<DeviceShareListResponse>`.

## Response

A null result gives an empty-state path (`@0x21a4bcc`); an exception is logged as `getDeviceShareList error: ...` (`@0x21a4c14`) and rethrown as a `DeviceShareException` (`@0x21a4c3c`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_list` | list of `DeviceShareListModel` | yes | `[ { "user_id": "...", "member_id": "...", "device_sn": "...", "email": "...", "phone": "...", "status": 2, "member_type": 1 } ]` | `device_share_list_model.dart @0x21c2770`; entry keys `user_id`, `member_id`, `device_sn`, `email`, `phone`, `status`, `member_type` (`@0x21c2e34` to `@0x21c3128`) |
| `max_invite_members_count` | int? | no | `5` | `device_share_list_model.dart @0x21c2884`; the example value is a placeholder |

## Example request/response

Request, synthesized

```json
{ "device_sn": "<device sn>", "status": [1, 2] }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- `DeviceShareBiz.getDeviceShareList` (`ev_charger/src/ev_charger/page/home/setting/device_share_members/device_share_biz/device_share_biz.dart @0x2d1336c`)
- `DeviceShareListLogic._getDeviceShareList` (`ev_charger/src/ev_charger/page/home/setting/device_share_members/device_share_list_page/device_share_list_logic.dart @0x2ab13f4`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x81418`); the sender function was not compared function by function. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- The integer values of `status` that the list closure sends (UNCONFIRMED `[1, 2]`) and the meaning of `status` and `member_type` in the answer are not decoded. — reclassified: server (2026-10-20: the meaning of the answer fields is decided by the server; the integer list the closure sends is `[1, 2]` as read by the batch)
- Whether the member type 1 means a family member or something else is not known (the invitation also sends `member_type` 1).

## Device-tested by

none
