> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# device_invite

## Purpose

Invites a person (by email or phone) to share an EV charger: the owner enters a nick name and an email address or phone number and the cloud sends the invitation.

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (line 369, upstream comment: "Sharing of EV charger devices, {\"nick_name\": \"lol***\", \"email\": \"<email>\", \"invites\": [{\"device_sn\": deviceSn, \"member_type\": 1}]}").

## Method+URL

`POST /app/devicerelation/device_invite` (asm-traced). Sender: `DeviceShareNetwork.deviceInvite` (`ev_charger/src/ev_charger/page/home/setting/device_share_members/network/device_share_network.dart @0x396d31c`); the path literal `app/devicerelation/device_invite` is loaded at `@0x396d510` and passed to `AkNetwork.requestHttp` (`@0x396d520`) with the named argument `params`; the method is fixed to `POST` inside the helper (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`). The app calls the path without a leading slash.

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork.requestHttp` (`device_share_network.dart`, call `@0x396d520`): the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory row says `encrypted: false` with the note "plain callee; callee default needEncryption=true"; that note does not apply, because `AkNetwork.requestHttp` has no `needEncryption` switch and goes straight to the SDK (mechanics: [../../sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)). Failures are turned into a `DeviceShareException` (`errorToDeviceShareException`) by the sender.

## Request

Body (`params`) is a `<String, dynamic>` map of five pairs (`r2 = 20`, `@0x396d3e4`). The sender checks first that a nick name is not empty (`DeviceShareException("nickName is required")`, `@0x396d57c`) and that email or phone is not empty (`"email or phone is required"`, `@0x396d540`).

| field | type | required | example | source |
|---|---|---|---|---|
| `email` | String | yes (or `phone`) | `owner@example.org` | `device_share_network.dart @0x396d3f0` |
| `phone` | String | yes (or `email`) | `""` | `device_share_network.dart @0x396d404` |
| `phone_code` | String | yes | `""` | `device_share_network.dart @0x396d418` |
| `nick_name` | String | yes | `Anna` | `device_share_network.dart @0x396d42c` |
| `invites` | list of map (one element) | yes | `[ { "member_type": 1, "device_sn": "..." } ]` | `device_share_network.dart @0x396d440`; list built at `@0x396d494` to `@0x396d4cc` |
| `invites[].member_type` | int | yes (constant) | `1` | `device_share_network.dart @0x396d458`; raw `2` at `@0x396d464`, `stur w16`, a Smi, so 1 (`tools/smi.py`) |
| `invites[].device_sn` | String | yes | `<device sn>` | `device_share_network.dart @0x396d46c` |

Upstream confirms `nick_name`, `email` and the `invites` list with `member_type` 1. The app additionally sends `phone` and `phone_code` (empty strings when the other channel is used; which of them the app fills is not traced).

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the sender returns nothing it parses; the caller reacts to success or to the `DeviceShareException`.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "email": "<email>", "phone": "", "phone_code": "", "nick_name": "Anna", "invites": [ { "member_type": 1, "device_sn": "<device sn>" } ] }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- `DeviceShareInviteLogic.onTapInvite` (`ev_charger/src/ev_charger/page/home/setting/device_share_members/device_share_invite_page/device_share_invite_logic.dart @0x396d004`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x81560`); the sender function was not compared function by function. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- Whether an invitation sent by phone needs `phone_code` (country calling code) and what format it takes is not known.
- The maximum number of invitees (`max_invite_members_count` on [get_shared_device](get_shared_device.md#response)) is enforced by the server; the error for exceeding it is not recorded.

## Device-tested by

none
