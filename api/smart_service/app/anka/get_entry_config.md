> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

Removed in 3.24.3 — present in 3.18.0 only

# get_entry_config

## Purpose

Read the entry configuration of the Anka AI assistant for the account (3.18.0 only). 3.24.3 replaced it with [`get_all_config`](get_all_config.md), which reads the same configuration under the new name (the wording of what it carries is taken from that page; the 3.18.0 sender could not be re-read here, string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`/smart_service/v1/app/anka/get_entry_config`, method not re-read (string-only): the inventory records the sender `getAnkaAgentEntry` of `anka_agent/http/anka_agent_http.dart` (`(3.18.0 address 0x1fe414c)`, URL literal `(3.18.0 address 0x1fe41f0)`) in the 3.18.0 tree, wrapped by `encryptionRequestHttpByGHttpRequest`. The workspace holds only the 3.24.3 asm (`v3.24.3/blutter_output/asm`), where these addresses do not exist (the function `getAnkaAgentEntry` is now at `anka_agent/http/anka_agent_http.dart @0x273702c` and sends `get_all_config`), so the method object, the body and the response parse could not be read.

3.18.0 sender (traced 2026-10-20 in the 3.18.0 asm tree, which is in the workspace at `ankerAPK/blutter_output/asm`; addresses are written without the at sign so that the 3.24.3 citation check skips them): `getAnkaAgentEntry` (`anka_agent/http/anka_agent_http.dart`, 3.18.0 address 0x1fe414c) takes three parameters, loads the method object `Instance_Method` (3.18.0 address 0x1fe41e8, 3.18.0 pool `pp+0x9b18`, enum index 1, name `post`) and the URL string (3.18.0 address 0x1fe41f0), and calls `HttpServiceImpl::encryptionRequestHttpByGHttpRequest` (3.18.0 address 0x1fe4218) with the first parameter as an argument (3.18.0 address 0x1fe4200); the method is therefore `POST`. No map literal is built in the function, so the call sends no body of its own. The response parse was not read.

## Encrypted?

not readable (3.18.0-only endpoint): the inventory records the wrapper `encryptionRequestHttpByGHttpRequest` for the 3.18.0 sender, but no asm of it is available here. Scheme and header rules: `api/encryption.md`.

## Request

No request keys are known for the 3.18.0 call: the extractor found none, and the 3.18.0 sender builds no map literal of its own (see Method+URL). The 3.24.3 successor `get_all_config` builds no body (see its page), which suggests the same for this call (inference, not read).

## `param_type`/`cmd`

n/a

## Response model (link)

Unknown (string-only): the 3.18.0 response parse was not read. The 3.24.3 successor parses `AnkaAgentEntryConfigModel` (see [`get_all_config`](get_all_config.md)).

## Response

Unknown (string-only); see the successor page for the 3.24.3 response keys.

3.18.0 parse read (traced 2026-10-20, 3.18.0 asm tree): `getAnkaAgentEntry` (`anka_agent/http/anka_agent_http.dart`, URL load `0x1fe41f0`) parses the answer with `AnkaAgentEntryConfigModel.fromJson` (`0x1fe4364`); that model reads the keys `show`, `domain`, `key_exchange_domain`, `setting_switch`, `enable` and `setting_images` (elements with `function_description` and `image_url`) in `anka_agent/bean/anka_agent_entry_config_model.dart` of 3.18.0, which are the same first six keys that the 3.24.3 model reads (see [get_all_config](get_all_config.md#response)); 3.24.3 reads further keys (`has_proactive_message`, `memory_switch`, the `bill_analysis_*`, `power_outage_switch` and `bubble_config` keys). So `get_all_config` is not a pure rename of the call: the answer model gained keys while the six older keys stayed.

## Example request/response

None: nothing to synthesize without the 3.18.0 asm.

## Errors seen

none traced: the 3.18.0 sender is not readable here.

## Callers in app

- `anka_agent/http/anka_agent_http.dart`: `getAnkaAgentEntry` (3.18.0 address 0x1fe414c) (encryptionRequestHttpByGHttpRequest; encrypted: inventory flag only, 3.18.0 asm not available)

## Since/changed

3.18.0: present. 3.24.3: absent (listed under "Removed endpoints" in `tools/out/diff_3.18.0_3.24.3.md`, with the sender `getAnkaAgentEntry`; the 3.24.3 function of that name sends `get_all_config`). since: <=3.18.0.

## Known unknowns

- The response parse of the 3.18.0 call (the method POST and the absence of a body literal are in Method+URL; the 3.18.0 asm tree is in the workspace) — traced 2026-10-20.
- Whether the 3.18.0 server still answers this URL: not tested; the 3.24.3 app no longer sends it.

## Device-tested by

none
