> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# set_entry_switch

## Purpose

Turns the Anka assistant entry (the AI entry on the user page) on or off for the account.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /smart_service/v1/app/anka/set_entry_switch` (asm-traced). Sender: `AnkaAgentHttp.setAnkaAgentEntrySwitch` (`anka_agent/http/anka_agent_http.dart @0x403f000`); the URL literal is loaded at `@0x403f0d8` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x403f0d0`).

## Encrypted?

Yes by wrapper (asm-traced): `setAnkaAgentEntrySwitch` calls `HttpServiceImpl.encryptionRequestHttpByGHttpRequest` (`anka_agent/http/anka_agent_http.dart @0x403f100`) without passing `needEncryption`, so the default `true` applies ([encryption.md](../../../encryption.md#which-calls-are-encrypted)). The wrapper sends through the global `HttpRequest` object (`gHttpRequest`). Whether the call really goes through the SDK is decided at run time ([encryption.md](../../../encryption.md)); asm alone does not decide it.

## Request

Body is a `<String, bool>` map of one pair (`r2 = 4`, `@0x403f048`).

| field | type | required | example | source |
|---|---|---|---|---|
| `setting_switch` | bool | yes | `true` | `anka_agent_http.dart @0x403f050`; value is the first argument; the model key of the same name is `setting_switch` (`bool?`) |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the answer is passed to the caller's callbacks, no model.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "setting_switch": true }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `AnkaAgentSettingLogic.toggleAnkaAI` (`charging/ui/page/user/ankaAgent/anka_agent_setting_logic.dart @0x403efec`)

Other screens (traced 2026-10-20, app side): the entry visibility is held by the singleton `AnkaAgentEntryConfigService` (`anka_agent/services/anka_agent_entry_config_service.dart`, `updateVisibility` `@0x3650998` region, getter `show` at line 1702 of the dump); other screens read it from the singleton, for example the message detail view (`charging/ui/page/message/messageDetailInfo/message_detail_info_view.dart @0x4020bc8`..`@0x4020bd0`, `_instance` then `show`), and the service is also referenced by `settings_page_logic.dart`, `message_push_handler.dart` and `anka_agent_entry_logic.dart`. So the setting acts on the shared entry state, not on one screen; which widgets hide on `show == false` was not traced one by one.

## Since/changed

3.18.0: present (pool `pp+0xafe50`); the sender function has no literal difference between 3.18.0 and 3.24.3 (`tools/cmp_since.py`: ordered string, integer and type literals compared; branch logic not compared). 3.24.3: present (pool `pp+0xdd090`). since: ≤3.18.0.

## Known unknowns

- Which widgets of the other screens hide when `show` is false (the shared state is described in Callers in app) — traced 2026-10-20

## Device-tested by

none
