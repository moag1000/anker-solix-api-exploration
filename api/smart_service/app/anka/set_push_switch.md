> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# set_push_switch

## Purpose

Turns one of the Anka push notification switches on or off: proactive messages, power-outage messages or bill analysis.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /smart_service/v1/app/anka/set_push_switch` (asm-traced). Sender: `AnkaAgentHttp.setPushSwitch` (`anka_agent/http/anka_agent_http.dart @0x35c4934`); the URL literal is loaded at `@0x35c4afc` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x35c4af4`).

## Encrypted?

Yes by wrapper (asm-traced): `setPushSwitch` calls `HttpServiceImpl.encryptionRequestHttpByGHttpRequest` (`anka_agent/http/anka_agent_http.dart @0x35c4b24`) without passing `needEncryption`, so the default `true` applies ([encryption.md](../../../encryption.md#which-calls-are-encrypted)). The wrapper sends through the global `HttpRequest` object (`gHttpRequest`). Whether the call really goes through the SDK is decided at run time ([encryption.md](../../../encryption.md)); asm alone does not decide it.

## Request

Body is a `<String, dynamic>` map of two pairs (`r2 = 8`, `@0x35c49a8`); the function logs `setPushSwitch: [REQUEST] switch_name=... enabled=...` first (`@0x35c4a54`).

| field | type | required | example | source |
|---|---|---|---|---|
| `switch_name` | String | yes | `"proactive_message"` | `anka_agent_http.dart @0x35c49b0`; the callers pass `"proactive_message"` (`AnkaAgentEntryConfigService.setProactivePushSwitch`, `anka_agent/services/anka_agent_entry_config_service.dart @0x37fe9a8`), `"power_outage"` (`setPowerOutagePushSwitch`, `@0x37fec40`) and `"bill_analysis"` (`FeatureIntroOrchestrator._setBillAnalysisSwitchRemote`, `anka_agent/pages/home/widgets/feature_intro/feature_intro_orchestrator.dart @0x35c4918`) |
| `enabled` | int (unboxed, x) | yes | `1` | `anka_agent_http.dart @0x35c49c4`; `setPushSwitch` takes the switch as an unboxed integer and boxes it with `BoxInt64Instr` before the store (`@0x35c495c`); `setProactivePushSwitch` tags it with `lsl x2, x0, #1` (`@0x37fe8bc`) and forwards it as an unboxed integer (`LoadInt32Instr`, `@0x37fe970`, `@0x37fec08`); the two dialog callers pass the constants `r3 = 1` (`ai_chat_content_edit_dialog.dart @0x37fe62c`) and `r3 = 0` (`@0x37fee1c`), unboxed, so real values. Same wire type as [set_memory_switch](set_memory_switch.md) |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the answer is passed to the caller's callbacks, no model.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "switch_name": "power_outage", "enabled": 1 }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `FeatureIntroOrchestrator._setBillAnalysisSwitchRemote` (`anka_agent/pages/home/widgets/feature_intro/feature_intro_orchestrator.dart @0x35c4920`)
- `AnkaAgentEntryConfigService.setProactivePushSwitch` (`anka_agent/services/anka_agent_entry_config_service.dart @0x37fe9b0`)
- `AnkaAgentEntryConfigService.setPowerOutagePushSwitch` (`anka_agent/services/anka_agent_entry_config_service.dart @0x37fec48`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0xef068`). since: 3.24.3.

## Known unknowns

- Whether other `switch_name` values exist is not known; the three above are the ones the asm passes.

## Device-tested by

none
