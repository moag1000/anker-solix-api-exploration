> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# delete_all_memory

## Purpose

Deletes everything the Anka assistant remembers about the user (the "delete all memory" action of the assistant settings).

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /smart_service/v1/app/anka/delete_all_memory` (asm-traced). Sender: `AnkaAgentHttp.deleteAllMemory` (`anka_agent/http/anka_agent_http.dart @0x2f23cec`); the URL literal is loaded at `@0x2f23e14` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x2f23e0c`).

## Encrypted?

Yes by wrapper (asm-traced): `deleteAllMemory` calls `HttpServiceImpl.encryptionRequestHttpByGHttpRequest` (`anka_agent/http/anka_agent_http.dart @0x2f23e3c`) without passing `needEncryption`, so the default `true` applies ([encryption.md](../../../encryption.md#which-calls-are-encrypted)). The wrapper sends through the global `HttpRequest` object (`gHttpRequest`). Whether the call really goes through the SDK is decided at run time ([encryption.md](../../../encryption.md)); asm alone does not decide it.

## Request

No body: the function builds no parameter map; it logs `[AnkaAgent] AnkaAgentHttp.deleteAllMemory: [REQUEST]` first (`@0x2f23d90`).

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the answer is passed to the caller's callbacks, no model.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{}
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `AiChatFlowSettingLogic.deleteAllMemory` (`anka_agent/pages/setting/ai_chat_flow_setting_logic.dart @0x2f23cd8`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0x998c0`). since: 3.24.3.

## Known unknowns

- Whether the deletion is immediate and irreversible is not known.

## Device-tested by

none
