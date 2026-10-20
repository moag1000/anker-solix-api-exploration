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
- What the callback receives from the response and how the agent uses the URLs: only the log line and the `List` test were read.
- The unit of `expire` (the sender logs it with the text ` expire=`, `@0x2bf2494`): seconds are an assumption from the value 604800. — reclassified: server (2026-10-20: the lifetime of a download link is a storage-service property; the app only logs the number)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
