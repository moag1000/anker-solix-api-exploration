> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# proactive_cta

## Purpose

Reads the suggested questions (call-to-action chips) for a proactive scene of the Anka assistant, such as a reminder; the chat controller refreshes them when a proactive message is shown.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /smart_service/v1/app/anka/proactive_cta` (asm-traced). Sender: `AnkaAgentHttp.getProactiveCta` (`anka_agent/http/anka_agent_http.dart @0x2e54470`); the URL literal is loaded at `@0x2e54618` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x2e54610`).

## Encrypted?

Yes by wrapper (asm-traced): `getProactiveCta` calls `HttpServiceImpl.encryptionRequestHttpByGHttpRequest` (`anka_agent/http/anka_agent_http.dart @0x2e54640`) without passing `needEncryption`, so the default `true` applies ([encryption.md](../../../encryption.md#which-calls-are-encrypted)). The wrapper sends through the global `HttpRequest` object (`gHttpRequest`). Whether the call really goes through the SDK is decided at run time ([encryption.md](../../../encryption.md)); asm alone does not decide it.

## Request

Body is a `<String, dynamic>` map; it holds `scene_type` only when the argument `sceneType` is not empty (length check `@0x2e544c0`, key `@0x2e544d0`), otherwise it is empty (`@0x2e54500`; the log prints `(default)`, `@0x2e54598`).

| field | type | required | example | source |
|---|---|---|---|---|
| `scene_type` | String | no | `"power_outage"` | `anka_agent_http.dart @0x2e544d0`; the example scene is a placeholder (the values are not shown by the sender) |

Source of `scene_type` (traced 2026-10-20, app side): `AiChatController::refreshReminderCta` (`anka_agent/pages/home/controller/ai_chat_controller.dart @0x2e54354`, named parameter `sceneType`) is called from `_fetchCtaForSpecialMessages` (`@0x2e5432c`) with the scene taken from the chat message data: the string key `scene_type` is read from message maps at `ai_chat_controller.dart @0x2e6112c`, `@0x2e61b80`, `@0x2e63170` and passed on in the log text ` sceneType=`. So the scene values are delivered with the messages (server data) and are not enumerated in the app.

## `param_type`/`cmd`

n/a

## Response model (link)

`ProactiveCtaResponse` ([../../../../models/anka_agent_models.md](../../../../models/anka_agent_models.md#proactivectaresponse)): `ProactiveCtaResponse.fromJson` is called in the success closure (`anka_agent_http.dart @0x2e54874`).

## Response

The success closure parses the data into the model.

| field | type | required | example | source |
|---|---|---|---|---|
| `questions` | list of `ProactiveCtaItem` (`title`, `value`) | no | `[ { "title": "...", "value": "..." } ]` | `proactive_cta_response_model.dart @0x2e5497c`; items `@0x2e54b08`, `@0x2e54b7c`; [model page](../../../../models/anka_agent_models.md#proactivectaresponse) |

## Example request/response

Request, synthesized

```json
{ "scene_type": "<scene>" }
```

Request, synthesized (default)

```json
{}
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `AiChatController.refreshReminderCta` (`anka_agent/pages/home/controller/ai_chat_controller.dart @0x2e54454`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0xefc88`). since: 3.24.3.

## Known unknowns

- The set of `scene_type` values: delivered with the chat messages, not enumerated in the app — reclassified: server (2026-10-20, see Request)

## Device-tested by

none
