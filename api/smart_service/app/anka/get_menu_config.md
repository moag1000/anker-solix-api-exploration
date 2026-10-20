> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_menu_config

## Purpose

Reads the Anka assistant's menu configuration (menu items with sub items) and, new in 3.24.3, the bill-analysis entry state.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /smart_service/v1/app/anka/get_menu_config` (asm-traced). Sender: `AnkaAgentHttp.getAnkaAgentMenuConfig` (`anka_agent/http/anka_agent_http.dart @0x35c5310`); the URL literal is loaded at `@0x35c53b4` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x35c53ac`).

## Encrypted?

Yes by wrapper (asm-traced): `getAnkaAgentMenuConfig` calls `HttpServiceImpl.encryptionRequestHttpByGHttpRequest` (`anka_agent/http/anka_agent_http.dart @0x35c53dc`) without passing `needEncryption`, so the default `true` applies ([encryption.md](../../../encryption.md#which-calls-are-encrypted)). The wrapper sends through the global `HttpRequest` object (`gHttpRequest`). Whether the call really goes through the SDK is decided at run time ([encryption.md](../../../encryption.md)); asm alone does not decide it.

## Request

No body: the function builds no parameter map.

## `param_type`/`cmd`

n/a

## Response model (link)

`AnkaAgentMenuConfigModel` ([../../../../models/anka_agent_models.md](../../../../models/anka_agent_models.md#ankaagentmenuconfigmodel)): `AnkaAgentMenuConfigModel.fromJson` is called in the success closure (`anka_agent_http.dart @0x35c5428`).

## Response

The success closure parses the data into the model.

| field | type | required | example | source |
|---|---|---|---|---|
| `menu_list` | list of `MenuItem` (`id`, `title`, `sub_items`) | no |  | `anka_agent_menu_config_model.dart @0x35c549c`; [model page](../../../../models/anka_agent_models.md#ankaagentmenuconfigmodel) |
| `bill_analysis_entry` | object (`show`, `privacy_agreed`) | no |  | `anka_agent_menu_config_model.dart @0x35c55b4` (new in 3.24.3) |

## Example request/response

Request, synthesized

```json
{}
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `AiChatController.onInit` (`anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c36d4`)
- `AiChatController._resumeFromPageNavigation` (`anka_agent/pages/home/controller/ai_chat_controller.dart @0x35ccd14`)

## Since/changed

3.18.0: present (pool `pp+0x107660`); the sender function has no literal difference between 3.18.0 and 3.24.3 (`tools/cmp_since.py`: ordered string, integer and type literals compared; branch logic not compared); the model gained `bill_analysis_entry` in 3.24.3. 3.24.3: present (pool `pp+0x14ba38`). since: ≤3.18.0.

## Known unknowns

- The values of the menu item ids are not decoded. — reclassified: server (2026-10-20: the ids arrive in the answer; the app code read here does not name them)

## Device-tested by

none
