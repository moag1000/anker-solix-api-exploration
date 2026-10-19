> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# ignore_invite

## Purpose

Rejects or withdraws a device share: the invited member ignores an invitation, or the owner cancels an invitation to a given receiver.

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (line 371, no comment).

## Method+URL

`POST /app/devicerelation/ignore_invite` (asm-traced). Sender: `DeviceShareNetwork._ignoreInvite` (`ev_charger/src/ev_charger/page/home/setting/device_share_members/network/device_share_network.dart @0x273941c`); the path literal `app/devicerelation/ignore_invite` is loaded at `@0x27395b4` and passed to `AkNetwork.requestHttp` (`@0x27395c4`) with the named argument `params`; the method is fixed to `POST` inside the helper (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`). The app calls the path without a leading slash. Two wrappers call it: `memberIgnoreInvite` (`@0x2739358`, passes the unboxed integer 1, `@0x2739384`) and `ownerIgnoreInvite` (`@0x430bb08`, passes the integer 0 and the named argument `recevicerUserId`, `@0x430bb40`, `@0x430bb44`).

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork.requestHttp` (`device_share_network.dart`, call `@0x27395c4`): the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory row says `encrypted: false` with the note "plain callee; callee default needEncryption=true"; that note does not apply, because `AkNetwork.requestHttp` has no `needEncryption` switch and goes straight to the SDK (mechanics: [../../sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)). Failures are turned into a `DeviceShareException` (`errorToDeviceShareException`) by the sender.

## Request

Body (`params`) is a `<String, dynamic>` map built in two steps: first the inner map `{invite_id, device_sn}` (`r2 = 8`, `@0x27394bc`), then, if `recevicerUserId` is not empty, `recevicer_user_id` is added to it with `[]=` (`@0x2739514`); then the outer map `{invites: [inner], is_inviter}` is built (`@0x2739540`, `@0x273958c`). An empty `recevicerUserId` for the owner wrapper makes the sender throw `DeviceShareException("recevicerUserId is required")` (`@0x27395e4`).

| field | type | required | example | source |
|---|---|---|---|---|
| `invites` | list of map (one element) | yes | `[ { "invite_id": 0, "device_sn": "...", "recevicer_user_id": "..." } ]` | `device_share_network.dart @0x2739540` |
| `invites[].invite_id` | int | yes (constant) | `0` | `device_share_network.dart @0x27394c4`; stored with `stur wzr` (`@0x27394d0`), a Smi 0 |
| `invites[].device_sn` | String | yes | `<device sn>` | `device_share_network.dart @0x27394d4`; value `@0x27394e4` |
| `invites[].recevicer_user_id` | String | owner only | `<receiver user id>` | `device_share_network.dart @0x2739514`; added only when not empty (the spelling `recevicer` is the app's) |
| `is_inviter` | int | yes | `1` (member) or `0` (owner) | `device_share_network.dart @0x273958c`; the argument is an unboxed integer, Smi-tagged with `lsl x2, x1, #1` (`@0x273959c`); member wrapper passes 1, owner wrapper passes 0 |

The member wrapper sends `is_inviter` 1 and the owner wrapper sends 0; the names are the app's and look inverted (a member ignoring an invitation is not the inviter), but the values are what the asm passes.

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the sender parses nothing.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized (member ignores)

```json
{ "invites": [ { "invite_id": 0, "device_sn": "<device sn>" } ], "is_inviter": 1 }
```

Request, synthesized (owner withdraws)

```json
{ "invites": [ { "invite_id": 0, "device_sn": "<device sn>", "recevicer_user_id": "<receiver user id>" } ], "is_inviter": 0 }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- the wrapper `DeviceShareNetwork.memberIgnoreInvite` (`device_share_network.dart @0x273938c`), called by `DeviceShareBiz.memberIgnoreInvite` (`ev_charger/src/ev_charger/page/home/setting/device_share_members/device_share_biz/device_share_biz.dart @0x2738e80`)
- the wrapper `DeviceShareNetwork.ownerIgnoreInvite` (`device_share_network.dart @0x430bb4c`), called from an anonymous closure of `DeviceShareListLogic` (`ev_charger/src/ev_charger/page/home/setting/device_share_members/device_share_list_page/device_share_list_logic.dart @0x430b3b8`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x302a0`); the sender function was not compared function by function. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- Why the app sends the constant `invite_id` 0 and what `is_inviter` selects server-side is not known.

## Device-tested by

none
