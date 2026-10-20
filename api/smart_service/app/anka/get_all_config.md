> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_all_config

## Purpose

Reads the Anka AI assistant's entry configuration for the account: whether the entry is shown, the agent domain, the switches (proactive messages, memory, bill analysis, power outage), the setting images and the current bubble. This is the 3.24.3 name of the 3.18.0 call `get_entry_config`.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /smart_service/v1/app/anka/get_all_config` (asm-traced). Sender: `AnkaAgentHttp.getAnkaAgentEntry` (`anka_agent/http/anka_agent_http.dart @0x273702c`); the URL literal is loaded at `@0x27370d0` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x27370c8`).

## Encrypted?

Yes by wrapper (asm-traced): `getAnkaAgentEntry` calls `HttpServiceImpl.encryptionRequestHttpByGHttpRequest` (`anka_agent/http/anka_agent_http.dart @0x27370f8`) without passing `needEncryption`, so the default `true` applies ([encryption.md](../../../encryption.md#which-calls-are-encrypted)). The wrapper sends through the global `HttpRequest` object (`gHttpRequest`). Whether the call really goes through the SDK is decided at run time ([encryption.md](../../../encryption.md)); asm alone does not decide it.

## Request

No body: the function builds no parameter map.

## `param_type`/`cmd`

n/a

## Response model (link)

`AnkaAgentEntryConfigModel` ([../../../../models/anka_agent_models.md](../../../../models/anka_agent_models.md#ankaagententryconfigmodel)): `AnkaAgentEntryConfigModel.fromJson` is called in the success closure of `getAnkaAgentEntry` (`anka_agent_http.dart @0x2737280`).

## Response

The success closure parses the data into the model; the callers read the switches from it.

| field | type | required | example | source |
|---|---|---|---|---|
| `show`, `domain`, `key_exchange_domain`, `setting_switch`, `enable`, `setting_images` | see model page | no |  | `anka_agent_entry_config_model.dart @0x27372ec` to `@0x273757c`; [model page](../../../../models/anka_agent_models.md#ankaagententryconfigmodel) |
| `has_proactive_message`, `proactive_message_*`, `memory_switch`, `bill_analysis_*`, `power_outage_switch`, `bubble_config` | see model page (new in 3.24.3) | no |  | `anka_agent_entry_config_model.dart @0x27376a8` to `@0x2737b20` |

## Example request/response

Request, synthesized

```json
{}
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `AnkaAgentSettingLogic._loadSettings` (`charging/ui/page/user/ankaAgent/anka_agent_setting_logic.dart @0x36508e4`)
- `AnkaAgentEntryConfigService.fetchEntryConfig` (`anka_agent/services/anka_agent_entry_config_service.dart @0x2736a30`)

## Since/changed

3.18.0: the same function `getAnkaAgentEntry` sent `/smart_service/v1/app/anka/get_entry_config` (pool `pp+0xafc30`); that string is gone from the 3.24.3 pool. 3.24.3: sends `get_all_config` (pool `pp+0x318b0`) and the model gained eight keys (switches, proactive message, bill analysis, bubble). since: 3.24.3 for the URL name.

## Known unknowns

- Whether the server still answers `get_entry_config` is not known.
- The wire shape of the empty request is not shown. — reclassified: device test row 160 (2026-10-20: whether an empty body is sent as `{}`, as no body or as null is decided by the HTTP layer and the SDK, which a capture shows)

## Device-tested by

none
