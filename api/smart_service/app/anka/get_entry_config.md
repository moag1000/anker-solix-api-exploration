> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

Removed in 3.24.3 — present in 3.18.0 only

# get_entry_config

## Purpose

Read the entry configuration of the Anka AI assistant for the account (3.18.0 only). 3.24.3 replaced it with [`get_all_config`](get_all_config.md), which reads the same configuration under the new name (the wording of what it carries is taken from that page; the 3.18.0 sender could not be re-read here, string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`/smart_service/v1/app/anka/get_entry_config`, method not re-read (string-only): the inventory records the sender `getAnkaAgentEntry` of `anka_agent/http/anka_agent_http.dart` (`(3.18.0 address 0x1fe414c)`, URL literal `(3.18.0 address 0x1fe41f0)`) in the 3.18.0 tree, wrapped by `encryptionRequestHttpByGHttpRequest`. The workspace holds only the 3.24.3 asm (`v3.24.3/blutter_output/asm`), where these addresses do not exist (the function `getAnkaAgentEntry` is now at `anka_agent/http/anka_agent_http.dart @0x273702c` and sends `get_all_config`), so the method object, the body and the response parse could not be read.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys are known for the 3.18.0 call: the extractor found none and the 3.18.0 asm is not available. The 3.24.3 successor `get_all_config` builds no body (see its page), which suggests the same for this call (inference, not read).

## `param_type`/`cmd`

n/a

## Response model (link)

Unknown (string-only): the 3.18.0 asm is not available. The 3.24.3 successor parses `AnkaAgentEntryConfigModel` (see [`get_all_config`](get_all_config.md)).

## Response

Unknown (string-only); see the successor page for the 3.24.3 response keys.

## Example request/response

None: nothing to synthesize without the 3.18.0 asm.

## Errors seen

none traced: the 3.18.0 sender is not readable here.

## Callers in app

- `anka_agent/http/anka_agent_http.dart`: `getAnkaAgentEntry` (3.18.0 address 0x1fe414c) (encryptionRequestHttpByGHttpRequest; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: absent (listed under "Removed endpoints" in `tools/out/diff_3.18.0_3.24.3.md`, with the sender `getAnkaAgentEntry`; the 3.24.3 function of that name sends `get_all_config`). since: <=3.18.0.

## Known unknowns

- Method, body and response of the 3.18.0 call: the 3.18.0 asm tree is not in the workspace (only `v3.24.3/`), and the addresses in the inventory belong to it.
- Whether the 3.18.0 server still answers this URL: not tested; the 3.24.3 app no longer sends it.
- Whether `get_all_config` is a pure rename or also changed the response keys: the successor page documents only the 3.24.3 side.

## Device-tested by

none
