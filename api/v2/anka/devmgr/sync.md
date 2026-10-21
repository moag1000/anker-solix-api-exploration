> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

Removed in 3.24.3 — present in 3.18.0 only

# sync

## Purpose

Synced device-manager data of the Anka AI assistant (the fourth branch of the 3.18.0 `RequestModel.data`, with the keys `messageId`, `userId`, `manufacturerName`) (3.18.0 asm for the keys; the meaning is string-only, the request class of this branch was not located).

## Upstream name

`none` (no upstream name)

## Method+URL

`/v2/anka/devmgr/sync`, method `POST` as a string in the envelope in the 3.18.0 asm: `RequestModel.data` (`anka_agent/http/request.dart 0x220d1ec`, 3.18.0 addresses) stores `"POST"` under `method` (`0x220d288`, `0x220d294`) and chooses the URL by class id (11138 `update_msg`, 11139 `del_msg`, 11140 `get_msg`); every other class falls through to `/v2/anka/devmgr/sync` (`0x220d27c`). In 3.24.3 the string `/v2/anka/devmgr/sync` occurs nowhere in the object pool (`pp.txt`) or the asm, and the 3.24.3 `RequestModel.data` has only the three history URLs.

## Encrypted?

encrypted: "unknown (URL literal only, no `*Http*` call)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys in 3.24.3. In the 3.18.0 asm the default branch builds a `body` map with three keys and no type arguments (`Map._fromLiteral` `anka_agent/http/request.dart 0x220d654`; array length raw 12 at `0x220d600`):

| field | type | required | example | source |
|---|---|---|---|---|
| `messageId` | ? | yes | `"<message_id>"` | `anka_agent/http/request.dart 0x220d608` (3.18.0) (value `LoadField` `0x220d614`, store `0x220d61c`) |
| `userId` | ? | yes | `"<user_id>"` | `anka_agent/http/request.dart 0x220d620` (3.18.0) (`ArrayLoad` `0x220d62c`, store `0x220d634`) |
| `manufacturerName` | ? | yes | `"<manufacturer>"` | `anka_agent/http/request.dart 0x220d638` (3.18.0) (`LoadField` `0x220d644`, store `0x220d64c`) |

The envelope keys (`url`, `method`, `country`, `cloudVersion`, `useWebsocket`, `isAIotEnv`, `body`, `jsonBody`) are the same as in 3.24.3 (see [get_msg](../history/get_msg.md)).

Types and sources (traced 2026-10-20, 3.18.0 tree, so this page stays `string-only`): the request class is `AiChatDeviceControlDevmgrSyncRequestModel` (`anka_agent/pages/home/models/ai_chat_device_control_request_model.dart`, class id 11141, extends `RequestModel`). `AiChatController::syncCloudAuthorizeDeviceDataRequest` (`anka_agent/pages/home/controller/ai_chat_controller.dart 0x24cf26c`) builds it: `messageId` (field at 0x13) is the result of `generateTimestampId` (`0x24cf264`; `anka_agent/utils/uuid_util.dart`, declared `String`), `userId` (field 0x17) is a `String?` cast of a value read under the key `userID` with `""` for null (`0x24cf1fc`..`0x24cf258`), and `manufacturerName` (field 0x1b) is stored as the constant empty list `const []` (`0x24cf288`, `0x24cf28c`), so it is sent as `[]`, not as a string.

## `param_type`/`cmd`

n/a

## Response model (link)

not read: the 3.18.0 transport and response handling of this URL were not read.

## Response

Not read (3.18.0 only).

## Example request/response

Request, synthesized from the 3.18.0 asm (the `body` map; `<...>` are placeholders, not captured values)

```json
{
  "messageId": "<message_id>",
  "userId": "<user_id>",
  "manufacturerName": "<manufacturer>"
}
```

Response: not synthesized (no capture exists for this endpoint).

## Errors seen

none traced: no 3.24.3 sender. Code meanings are owned by `api/errors.md`.

## Callers in app

- `anka_agent/http/request.dart`: `data` @0x220d1ec (URL literal only, no `*Http*` call)

## Since/changed

3.18.0: present (read in the 3.18.0 asm, addresses above are 3.18.0 addresses). 3.24.3: absent (removed). since: <=3.18.0. `tools/out/diff_3.18.0_3.24.3.md` lists the endpoint under removed endpoints and lists `manufacturerName`, `messageId`, `userId` as removed from the three history URLs, which in 3.18.0 shared the builder.

## Known unknowns

- Whether the server still serves this URL: the 3.24.3 app has no code for it.
- What the request meant: the key names suggest a per-message device-manager sync; not shown by the asm. — reclassified: server (2026-10-20: the request class is not in the 3.24.3 asm, so its meaning is not derivable from the app)
- Server behaviour is not known from the app: this page states what the app built in 3.18.0.

## Device-tested by

none
