> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# confirm_invite

## Purpose

Accepts an invitation to share an EV charger (the invited person confirms the share of a device).

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (line 370, upstream comment: "accept invite").

## Method+URL

`POST /app/devicerelation/confirm_invite` (asm-traced). Sender: `DeviceShareNetwork.confirmInvite` (`ev_charger/src/ev_charger/page/home/setting/device_share_members/network/device_share_network.dart @0x2739860`); the path literal `app/devicerelation/confirm_invite` is loaded at `@0x2739968` and passed to `AkNetwork.requestHttp` (`@0x2739978`) with the named argument `params`; the method is fixed to `POST` inside the helper (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`). The app calls the path without a leading slash.

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork.requestHttp` (`device_share_network.dart`, call `@0x2739978`): the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory row says `encrypted: false` with the note "plain callee; callee default needEncryption=true"; that note does not apply, because `AkNetwork.requestHttp` has no `needEncryption` switch and goes straight to the SDK (mechanics: [../../sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)). Failures are turned into a `DeviceShareException` (`errorToDeviceShareException`) by the sender.

## Request

Body (`params`) is a `<String, dynamic>` map of one pair, `invites`, whose value is a one-element list of a `<String, Object>` map (`r2 = 4` `@0x2739890`, `r2 = 8` `@0x27398ac`, list `@0x2739908` to `@0x2739924`).

| field | type | required | example | source |
|---|---|---|---|---|
| `invites` | list of map (one element) | yes | `[ { "invite_id": 0, "device_sn": "..." } ]` | `device_share_network.dart @0x273989c` |
| `invites[].invite_id` | int | yes (constant) | `0` | `device_share_network.dart @0x27398b4`; the value is stored with `stur wzr` (`@0x27398c0`), a Smi 0: the app sends the constant 0, not a real invitation id |
| `invites[].device_sn` | String | yes | `<device sn>` | `device_share_network.dart @0x27398c4`; value is the argument (`@0x27398d4`) |

Because `invite_id` is the constant 0, the invitation is identified by the device serial (and the logged-in account) only; whether the server accepts a real id is not known.

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the sender parses nothing; failures are logged as `confirmInvite error: ...` (`@0x27399c0`) and rethrown as `DeviceShareException`.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "invites": [ { "invite_id": 0, "device_sn": "<device sn>" } ] }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `DeviceShareBiz.confirmInvite` (`ev_charger/src/ev_charger/page/home/setting/device_share_members/device_share_biz/device_share_biz.dart @0x27396d0`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x302c0`); the sender function was not compared function by function. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- The constant `invite_id` 0 is surprising; no capture shows whether the server requires a real value.
- Whether the call needs the invited account to be logged in with the invited email is not known.

## Device-tested by

none
