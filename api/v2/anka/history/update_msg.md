> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# update_msg

## Purpose

Updates chat messages of the Anka AI assistant history (class `AiChatHomeUpdateChatMsgRequestModel`, sent by `Channel.request`) (string-only: the meaning is taken from the class and URL names).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /v2/anka/history/update_msg` (asm-traced as the string `"POST"` in the envelope).

Transport: the app does not send this request from Dart. `RequestModel.data` (`anka_agent/http/request.dart @0x2dba16c`) builds an envelope map that `Channel.request` (`anka_agent/common/channel.dart @0x2db9df4`) passes to the platform through a Flutter `MethodChannel` call named `"request"` (name `@0x2db9e54`, `invokeMethod` `@0x2db9e64`, `_Future.timeout` `@0x2db9e78`). The envelope holds the keys `url` (`anka_agent/http/request.dart @0x2dba19c`, the URL string chosen by the request class id: `update_msg` for class id 6939 `@0x2dba1b8`..`@0x2dba1c4`, `del_msg` for 6940 `@0x2dba1d0`..`@0x2dba1dc`, otherwise `get_msg` `@0x2dba1e8`), `method` (`@0x2dba1f4`, the string `"POST"` `@0x2dba200`), `country` (`@0x2dba20c`), `cloudVersion` (`@0x2dba248`), `useWebsocket` (`@0x2dba2a4`, `true` `@0x2dba2b0`), `isAIotEnv` (`@0x2dba2b8`), `body` (`@0x2dba570`, the request fields below) and `jsonBody` (`@0x2dba5a4`, `jsonEncode` of the body, `@0x2dba588`). The request class ids are `AiChatHomeUpdateChatMsgRequestModel` 6939, `AiChatHomeDeleteChatMsgRequestModel` 6940 and `AiChatHomeSyncChatMsgRequestModel` 6941 (`anka_agent/pages/home/models/ai_chat_home_request_model.dart` class headers). The page-level `method` is therefore `POST` as a string in the envelope; the native layer that performs the HTTP or websocket call is not part of the Dart asm.

## Encrypted?

encrypted: "unknown (URL literal only, no `*Http*` call)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: not every field type is read) Envelope fields declared on `RequestModel` (`anka_agent/http/request.dart` class listing): `country` is a `bool`, `cloudVersion` a `String`, `isAIotEnv` a `bool` (late fields at offsets 0x8, 0x10, 0xc). The `body` map is built per request class; its literals have no type arguments in the asm (`Map._fromLiteral` `@0x2dba3e0`).

| field | type | required | example | source |
|---|---|---|---|---|
| `user_id` | ? | yes | `"<user_id>"` | `anka_agent/http/request.dart @0x2dba328` (value `LoadField` `@0x2dba338`, store `@0x2dba340`) |
| `msg_list` | ? | yes | `[{...}]` | `anka_agent/http/request.dart @0x2dba344` (a `ListBase::map` over the model's message list `@0x2dba380` with the closure `anka_agent/pages/home/models/ai_chat_home_request_model.dart @0x2dba644`, which returns `AiChatHomeChatMsgModel.toJson` `@0x2dba65c`; a dispatch-table call follows `@0x2dba39c`, selector not named; store `@0x2dba3b4`) |

Each message map is built by `AiChatHomeChatMsgModel.toJson` (`anka_agent/pages/home/models/ai_chat_home_response_model.dart @0x2dba674`) with the keys `msg_id` (`@0x2dba6c0`), `session_id` (`@0x2dba6f0`), `create_time` (`@0x2dba720`), `text` (`@0x2dba750`), `msg_type` (`@0x2dba77c`), `dispatcher` (`@0x2dba7ac`), `dislike` (`@0x2dba7dc`), `tool_name` (`@0x2dba80c`), `role` (`@0x2dba83c`), `intent` (`@0x2dba86c`), `language` (`@0x2dba89c`), `timbre` (`@0x2dba8cc`) and, when `link_list` is non-null, `link_list` (`@0x2dba968`). Their types in the class (`data/models.json`, `anka_agent::AiChatHomeChatMsgModel`) are `msg_id` String?, `session_id` String?, `text` String?, `msg_type` int?, `create_time` int?, `dispatcher` int?, `dislike` int?, `tool_name` String?, `role` String?, `intent` String?, `language` String?, `timbre` String?; the `toJson` stores read only the class fields.

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
  "msg_list": [
    {
      "msg_id": "<msg_id>",
      "text": "<text>"
    }
  ]
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

- Type of `user_id`: a field of the request object (`LoadField` `anka_agent/http/request.dart @0x2dba338`); the class listing shows no declared type for it. — attempted 2026-10-20 (two-hop not readable: the request class (`anka_agent/pages/home/models/ai_chat_home_request_model.dart`, one of `AiChatHomeUpdateChatMsgRequestModel`, `AiChatHomeDeleteChatMsgRequestModel`, `AiChatHomeSyncChatMsgRequestModel`, all `extends RequestModel`) lists no fields and no declared type in the asm; the load is `field_13` at `anka_agent/http/request.dart @0x2dba338`)
- Which response class belongs to this URL and what the callers do with the decoded map: `AiChatHomeLogic` callers were not read.
- What the native layer does with `useWebsocket: true` (websocket or HTTP): not part of the Dart asm. — reclassified: device test row 153 (2026-10-20: native layer, no Dart asm)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
