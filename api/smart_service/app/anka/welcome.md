> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# welcome

## Purpose

Reads the Anka assistant's welcome greeting for a session: the greeting text and the site selection data; the chat controller calls it when the chat opens and when it resyncs the cloud history.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /smart_service/v1/app/anka/welcome` (asm-traced). Sender: `AnkaAgentHttp.getWelcomeGreeting` (`anka_agent/http/anka_agent_http.dart @0x35c6e48`); the URL literal is loaded at `@0x35c710c` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x35c7104`).

## Encrypted?

Yes by wrapper (asm-traced): `getWelcomeGreeting` calls `HttpServiceImpl.encryptionRequestHttpByGHttpRequest` (`anka_agent/http/anka_agent_http.dart @0x35c7134`) without passing `needEncryption`, so the default `true` applies ([encryption.md](../../../encryption.md#which-calls-are-encrypted)). The wrapper sends through the global `HttpRequest` object (`gHttpRequest`). Whether the call really goes through the SDK is decided at run time ([encryption.md](../../../encryption.md)); asm alone does not decide it.

## Request

Body is a `<String, dynamic>` map built from the arguments (`r2 = 4`, `@0x35c6ed0`); optional keys are added only when their value is not empty.

| field | type | required | example | source |
|---|---|---|---|---|
| `current_time` | String | yes | `"2026-10-19 14:30:00"` | `anka_agent_http.dart @0x35c6ed8`; first argument, format not shown (placeholder in the example) |
| `source` | String | no | `"aiems"` | `anka_agent_http.dart @0x35c6f1c`; added with `[]=` when given (the log prints `null(not provided)` otherwise, `@0x35c7048`); the example value is the `source` the AI EMS entry sends elsewhere |
| `bubble_id` | String | no | `<bubble id>` | `anka_agent_http.dart @0x35c6f58`; from the named argument `bubble`, only when its id is not empty (`@0x35c6f44`) |
| `bubble_type` | String | no | `<bubble type>` | `anka_agent_http.dart @0x35c6f90`; from `bubble`, only when its type is not empty (`@0x35c6f7c`) |

## `param_type`/`cmd`

n/a

## Response model (link)

`WelcomeGreetingModel` ([../../../../models/anka_agent_models.md](../../../../models/anka_agent_models.md#welcomegreetingmodel)): `WelcomeGreetingModel.fromJson` is called in the success closure (`anka_agent_http.dart @0x35c7318`); the closure logs `welcome_type` and `site_count` of the result.

## Response

The success closure parses the data into the model.

| field | type | required | example | source |
|---|---|---|---|---|
| `welcome_type`, `content`, `site_count`, `site_ids_str`, `ai_guide_shown`, `calc_at`, `cleaned_proactive_message_count` | see model page | no |  | `welcome_greeting_model.dart @0x35c7524` to `@0x35c7810`; [model page](../../../../models/anka_agent_models.md#welcomegreetingmodel) |

## Example request/response

Request, synthesized

```json
{ "current_time": "<time>", "source": "aiems" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `AiChatController._syncCloudHistoryUpdate` (`anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c6e0c`)
- `AiChatController._fetchWelcomeGreeting` (`anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c8de8`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0x14beb0`). since: 3.24.3.

## Known unknowns

- The format of `current_time` and the values of `welcome_type` are not decoded. — reclassified: server (2026-10-20: the value formats are a server convention)

## Device-tested by

none
