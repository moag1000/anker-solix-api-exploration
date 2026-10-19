> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# setting

## Purpose

Reads the user's Anka assistant settings: the proactive and power-outage push switches, the memory switch and whether the assistant holds memory.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /smart_service/v1/app/anka/setting` (asm-traced). Sender: `AnkaAgentHttp.getSetting` (`anka_agent/http/anka_agent_http.dart @0x364e26c`); the URL literal is loaded at `@0x364e394` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x364e38c`).

## Encrypted?

Yes by wrapper (asm-traced): `getSetting` calls `HttpServiceImpl.encryptionRequestHttpByGHttpRequest` (`anka_agent/http/anka_agent_http.dart @0x364e3bc`) without passing `needEncryption`, so the default `true` applies ([encryption.md](../../../encryption.md#which-calls-are-encrypted)). The wrapper sends through the global `HttpRequest` object (`gHttpRequest`). Whether the call really goes through the SDK is decided at run time ([encryption.md](../../../encryption.md)); asm alone does not decide it.

## Request

No body: the function builds no parameter map; it logs `AnkaAgentHttp.getSetting: [REQUEST]` first (`@0x364e310`).

## `param_type`/`cmd`

n/a

## Response model (link)

`GetSettingResponse` ([../../../../models/anka_agent_models.md](../../../../models/anka_agent_models.md#getsettingresponse)): `GetSettingResponse.fromJson` is called in the success closure (`anka_agent_http.dart @0x364e5ec`).

## Response

The success closure parses the data into the model; the settings page (`AiChatFlowSettingLogic._loadSettingFromApi`) reads the switches.

| field | type | required | example | source |
|---|---|---|---|---|
| `proactive_switch`, `power_outage_switch`, `memory_switch`, `has_memory` | int? each | no | `{ "proactive_switch": 1, "power_outage_switch": 1, "memory_switch": 1, "has_memory": 0 }` | `memory_consent_model.dart @0x364e64c`, `@0x364e6e4`, `@0x364e77c`, `@0x364e814`; [model page](../../../../models/anka_agent_models.md#getsettingresponse) |

## Example request/response

Request, synthesized

```json
{}
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `AiChatFlowSettingLogic._loadSettingFromApi` (`anka_agent/pages/setting/ai_chat_flow_setting_logic.dart @0x364e250`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0x11a698`). since: 3.24.3.

## Known unknowns

- The values of the switches (0/1 or other) are not shown by the model.

## Device-tested by

none
