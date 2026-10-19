> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# set_memory_switch

## Purpose

Turns the Anka assistant's memory (remembering conversation facts) on or off.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /smart_service/v1/app/anka/set_memory_switch` (asm-traced). Sender: `AnkaAgentHttp.setMemorySwitch` (`anka_agent/http/anka_agent_http.dart @0x2f24908`); the URL literal is loaded at `@0x2f24a98` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x2f24a90`).

## Encrypted?

Yes by wrapper (asm-traced): `setMemorySwitch` calls `HttpServiceImpl.encryptionRequestHttpByGHttpRequest` (`anka_agent/http/anka_agent_http.dart @0x2f24ac0`) without passing `needEncryption`, so the default `true` applies ([encryption.md](../../../encryption.md#which-calls-are-encrypted)). The wrapper sends through the global `HttpRequest` object (`gHttpRequest`). Whether the call really goes through the SDK is decided at run time ([encryption.md](../../../encryption.md)); asm alone does not decide it.

## Request

Body is a `<String, dynamic>` map of one pair (`r2 = 4`, `@0x2f24970`); the function logs `AnkaAgentHttp.setMemorySwitch: [REQUEST] enabled=...` first (`@0x2f24a08`).

| field | type | required | example | source |
|---|---|---|---|---|
| `enabled` | bool (inferred) | yes | `true` | `anka_agent_http.dart @0x2f24978`; value is the first argument. The map type is `dynamic` and the entry switch uses `bool`, so a boolean is expected; the models store the switch as `int?` (`memory_switch`) |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the answer is passed to the caller's callbacks, no model.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "enabled": true }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `FeatureIntroOrchestrator._setMemorySwitchRemote` (`anka_agent/pages/home/widgets/feature_intro/feature_intro_orchestrator.dart @0x35c513c`)
- `AiChatFlowSettingLogic.toggleMemory` (`anka_agent/pages/setting/ai_chat_flow_setting_logic.dart @0x2f248f4`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0x99800`). since: 3.24.3.

## Known unknowns

- Whether the wire value is a boolean or 0/1 is not shown by the sender.

## Device-tested by

none
