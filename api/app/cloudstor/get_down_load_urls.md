> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_down_load_urls

## Purpose

Asks for temporary download URLs for stored files of the Anka agent (`AnkaAgentHttp::getDownLoadUrls`, called from `AiChatController`, `anka_agent/pages/home/controller/ai_chat_controller.dart @0x2bf2364`) (asm-traced for the call, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/cloudstor/get_down_load_urls` (asm-traced): URL string at `anka_agent/http/anka_agent_http.dart @0x2bf2518`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2bf2510`, in `AnkaAgentHttp::getDownLoadUrls` (`anka_agent/http/anka_agent_http.dart @0x2bf2378`), sent through `encryptionRequestHttpByGHttpRequest` (`@0x2bf2540`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `urls` | ? | yes | ? | `anka_agent/http/anka_agent_http.dart @0x2bf23c8` (value store `@0x2bf23d8`) |
| `expire` | int (Smi, w) | yes | `604800` | `anka_agent/http/anka_agent_http.dart @0x2bf23dc` (value store `@0x2bf23f0`) |

The map literal has type arguments `<String, dynamic>` (`anka_agent/http/anka_agent_http.dart @0x2bf23f4`), not evidence of a value type; `urls` stays `?`. `expire` is the Smi raw 1209600 stored with a 32-bit store (`@0x2bf23e8`..), so 604800 (seven days in seconds by arithmetic, the unit is not named in the asm).

## `param_type`/`cmd`

n/a

## Response model (link)

no model: the success closure (`anka_agent/http/anka_agent_http.dart @0x2bf268c`) tests that the response is a `Map<String, dynamic>` (`@0x2bf273c`), reads the key `down_load_urls` (key string `@0x2bf2780`, lookup `@0x2bf2788`), tests it for `List` (`@0x2bf2874`) and logs the element count; it then passes a value to the stored callback (`ClosureCall`, after `@0x2bf2940`).

What the callback receives (traced 2026-10-20, app side): the success closure of `AnkaAgentHttp::getDownLoadUrls` (`anka_agent/http/anka_agent_http.dart @0x2bf268c`) accepts the answer only when it is a `Map<String, dynamic>` (`InstanceOf` `@0x2bf2744`), reads the key `down_load_urls` (`@0x2bf2780`), logs the count (`ms count=`, `@0x2bf27d4`) and, when the value is a `List` (`InstanceOf` `@0x2bf2858`), hands it to the stored callback (`ClosureCall` `@0x2bf2954`); otherwise it logs `unexpected data type` (`@0x2bf2968`) and fails with the text `Unexpected response data type` (`@0x2bf2988`). The only caller `_resolveFileKeysToDownloadUrls` (`anka_agent/pages/home/controller/ai_chat_controller.dart @0x2bf229c`) returns `Future<List<String>>`: for an input list of length 0 it returns an empty `List<String>` without a request (`cbnz` `@0x2bf22b0`, `_GrowableList` `@0x2bf22bc`), otherwise its success closure (`@0x2bf2a68`, argument `Map<String, dynamic>`) maps the entries to strings (`<String>` `@0x2bf2bac`) and completes the future, and its failure closure logs `_resolveFileKeysToDownloadUrls failed:` and completes the future (`@0x2bf29bc`, `@0x2bf2a4c`). What the agent does with the resulting URLs is native code (see device test row 153).

## Response

(string-only for the callback value) One key is read from the top level of the response: `down_load_urls` (a list). What the callback receives (the list or a count) was not decoded.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "urls": "<urls>",
  "expire": 604800
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `anka_agent/http/anka_agent_http.dart`: `getDownLoadUrls` @0x2bf2378 (encryptionRequestHttpByGHttpRequest; encrypted: true)

## Since/changed

3.18.0: absent. 3.24.3: present. since: 3.24.3 (listed under "Added endpoints" in `tools/out/diff_3.18.0_3.24.3.md`, string-level evidence).

## Known unknowns

- The type of `urls` (a list of storage keys or a string): a parameter of the sender, the caller's value was not typed. — attempted 2026-10-20 (two-hop not readable: `_resolveFileKeysToDownloadUrls` (`anka_agent/pages/home/controller/ai_chat_controller.dart @0x2bf2364`) pass slots or fields of their own frames; no literal or declared type in the argument setups)
- What the native agent kit does with the URLs once `_resolveFileKeysToDownloadUrls` has returned them: the Dart side hands them on (see Response model) — traced 2026-10-20 — reclassified: device test row 153
- The unit of `expire` (the sender logs it with the text ` expire=`, `@0x2bf2494`): seconds are an assumption from the value 604800. — reclassified: server (2026-10-20: the app only logs `expire`; the unit is not derivable from the app)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
