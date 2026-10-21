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
| `enabled` | int (unboxed, x) | yes | `1` | `anka_agent_http.dart @0x2f24978`; value is the first argument, an unboxed integer 1 or 0 (see below); the models store the switch as `int?` (`memory_switch`) |

Wire type (traced 2026-10-20, app side): `AnkaAgentHttp::setMemorySwitch` (`anka_agent/http/anka_agent_http.dart @0x2f24914`) takes the switch as an unboxed integer and boxes it with `BoxInt64Instr` before the store (`@0x2f2492c`), so `enabled` is a JSON number. The caller `AiChatFlowSettingLogic::toggleMemory` (`anka_agent/pages/setting/ai_chat_flow_setting_logic.dart @0x2f2484c`) converts the bool state of the toggle to 1 or 0 (`tst x1, #0x10`, `cset x2, eq`, `lsl`, `LoadInt32Instr`, `@0x2f248b0`..`@0x2f248bc`) and passes it as the first argument (`@0x2f248e8`); the other caller passes an unboxed integer from a frame slot (`feature_intro_orchestrator.dart @0x35c5138`). So the wire value is 1 (on) or 0 (off), not a boolean.

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the answer is passed to the caller's callbacks, no model.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "enabled": 1 }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `FeatureIntroOrchestrator._setMemorySwitchRemote` (`anka_agent/pages/home/widgets/feature_intro/feature_intro_orchestrator.dart @0x35c513c`)
- `AiChatFlowSettingLogic.toggleMemory` (`anka_agent/pages/setting/ai_chat_flow_setting_logic.dart @0x2f248f4`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0x99800`). since: 3.24.3.

## Known unknowns

- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
