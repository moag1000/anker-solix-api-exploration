> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_msg

## Purpose

Fetches a page of the Anka AI assistant chat history (class `AiChatHomeSyncChatMsgRequestModel`, sent by `Channel.request`) (string-only: the meaning is taken from the class and URL names).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /v2/anka/history/get_msg` (asm-traced as the string `"POST"` in the envelope).

Transport: the app does not send this request from Dart. `RequestModel.data` (`anka_agent/http/request.dart @0x2dba16c`) builds an envelope map that `Channel.request` (`anka_agent/common/channel.dart @0x2db9df4`) passes to the platform through a Flutter `MethodChannel` call named `"request"` (name `@0x2db9e54`, `invokeMethod` `@0x2db9e64`, `_Future.timeout` `@0x2db9e78`). The envelope holds the keys `url` (`anka_agent/http/request.dart @0x2dba19c`, the URL string chosen by the request class id: `update_msg` for class id 6939 `@0x2dba1b8`..`@0x2dba1c4`, `del_msg` for 6940 `@0x2dba1d0`..`@0x2dba1dc`, otherwise `get_msg` `@0x2dba1e8`), `method` (`@0x2dba1f4`, the string `"POST"` `@0x2dba200`), `country` (`@0x2dba20c`), `cloudVersion` (`@0x2dba248`), `useWebsocket` (`@0x2dba2a4`, `true` `@0x2dba2b0`), `isAIotEnv` (`@0x2dba2b8`), `body` (`@0x2dba570`, the request fields below) and `jsonBody` (`@0x2dba5a4`, `jsonEncode` of the body, `@0x2dba588`). The request class ids are `AiChatHomeUpdateChatMsgRequestModel` 6939, `AiChatHomeDeleteChatMsgRequestModel` 6940 and `AiChatHomeSyncChatMsgRequestModel` 6941 (`anka_agent/pages/home/models/ai_chat_home_request_model.dart` class headers). The page-level `method` is therefore `POST` as a string in the envelope; the native layer that performs the HTTP or websocket call is not part of the Dart asm.

## Encrypted?

encrypted: "unknown (URL literal only, no `*Http*` call)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: not every field type is read) Envelope fields declared on `RequestModel` (`anka_agent/http/request.dart` class listing): `country` is a `bool`, `cloudVersion` a `String`, `isAIotEnv` a `bool` (late fields at offsets 0x8, 0x10, 0xc). The `body` map is built per request class; its literals have no type arguments in the asm (`Map._fromLiteral` `@0x2dba550`).

| field | type | required | example | source |
|---|---|---|---|---|
| `user_id` | ? | yes | `"<user_id>"` | `anka_agent/http/request.dart @0x2dba4e0` (value `LoadField` `@0x2dba4f0`, store `@0x2dba4f8`) |
| `page` | int (unboxed, x) | yes | `<page>` | `anka_agent/http/request.dart @0x2dba4fc` (`ArrayLoad` of an unboxed field `@0x2dba508`, `BoxInt64Instr` `@0x2dba50c`, store `@0x2dba520`) |
| `num` | int (unboxed, x) | yes | `<count>` | `anka_agent/http/request.dart @0x2dba524` (`LoadField` `@0x2dba530`, `BoxInt64Instr` `@0x2dba534`, store `@0x2dba548`) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed here: `Channel.request` (`anka_agent/common/channel.dart @0x2db9df4`) receives a `Map?` from the platform (type test `@0x2db9edc`), reads `error` (`@0x2db9ef0`, tested as `bool?` `@0x2db9f34`) and `data` (`@0x2db9f64`, tested as `String?` `@0x2db9fac`), decodes `data` with `jsonDecode` (`@0x2dba01c`, tested as `Map<String, dynamic>` `@0x2dba03c`) and hands the map to a callback (`ClosureCall` `@0x2dba058`). The callers that turn it into a model were not read.

## Response

No response key is read at this layer (see Response model). The response classes are `AiChatHomeUpdateChatMsgResponseModel`, `AiChatHomeDeleteChatMsgResponseModel` and `AiChatHomeSyncChatMsgResponseModel` (`data/models.json`, package `anka_agent`); which one the callers apply to this URL was not read.

## Example request/response

Request, synthesized (the `body` map as built by `RequestModel.data`; `<...>` are placeholders, not captured values)

```json
{
  "user_id": "<user_id>",
  "page": "<page>",
  "num": "<count>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in `Channel.request`; failures are logged (`[AnkaAgent] Bridge.request: error:` `@0x2dba0f4`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `anka_agent/http/request.dart`: `data` @0x2dba16c (URL literal only, no `*Http*` call; caller walk reaches a deduplicated mixin function absent from the dump (UNCONFIRMED))

Called from:

- `anka_agent/common/channel.dart::request`
- `anka_agent/http/request.dart::data`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. `tools/out/diff_3.18.0_3.24.3.md` lists `manufacturerName`, `messageId`, `userId` as removed for this URL; those three keys belong to the removed 3.18.0 branch of the same builder that sends `/v2/anka/devmgr/sync` (see [sync](../devmgr/sync.md)), so the keys are not request fields of this URL in either version.

## Known unknowns

- Type of `user_id`: a field of the request object (`LoadField` `anka_agent/http/request.dart @0x2dba338`); the class listing shows no declared type for it.
- Which response class belongs to this URL and what the callers do with the decoded map: `AiChatHomeLogic` callers were not read.
- What the native layer does with `useWebsocket: true` (websocket or HTTP): not part of the Dart asm.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
