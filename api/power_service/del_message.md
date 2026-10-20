> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# del_message

## Purpose

Deletes messages of the message centre: `MessageMainLogic::deleteMsg` (`message_main_logic.dart @0x401a930`) and `MessageSystemLogic::deleteMessage` (`message_system_logic.dart @0x3bb47ac`) call `delMessage`.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/del_message` (asm-traced): URL string at `http_request_repository_impl.dart @0x3bb4b54`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3bb4b4c`, in `HttpRequestControllerImpl::delMessage` (`http_request_repository_impl.dart @0x3bb49a8`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is an empty `<String, dynamic>` map literal (`empty_array` `@0x3bb4a14`, `Map._fromLiteral` `@0x3bb4a1c`) to which `delMessage` (`http_request_repository_impl.dart @0x3bb49a8`) adds keys with `Map.[]=` (`GDT[cid_x0 + 0x6a9]`). All value types come from parameters of the builder, whose callers were not followed.

| field | type | required | example | source |
|---|---|---|---|---|
| `ids` | list | optional | | key `@0x3bb4a48`, `[]=` `@0x3bb4a50`; added only when the parameter is non-null (`cmp w3, NULL` `@0x3bb4a2c`) and its length field is non-zero (`LoadField field_b`, `cbz` `@0x3bb4a38`) |
| `sns` | ? | optional | | key `@0x3bb4aa0`, `[]=` `@0x3bb4aa8`; added when the parameter is non-null (`@0x3bb4a60`) and a dispatch-table call (`GDT[cid_x0 + 0x3558d]` `@0x3bb4a74`, selector not named) returns true (`tbnz` `@0x3bb4a88`) |
| `all` | ? | yes | | key `@0x3bb4acc`, `[]=` `@0x3bb4ad4` (value: parameter at `fp-0x10`, `@0x3bb4ac8`) |
| `type` | int (unboxed, x) | yes | | key `@0x3bb4af8`, `[]=` `@0x3bb4afc`; `lsl x3, x0, #1` `@0x3bb4ae4` Smi-tags the unboxed parameter; the two callers pass the small constants `r7 = 2` (`message_main_logic.dart @0x401aa40`) and `r7 = 1` (`message_system_logic.dart @0x3bb4874`) to the wrapper `delMessage`, not mapped to the key here |

## `param_type`/`cmd`

n/a

## Response model (link)

None: the response body is not parsed. The builder's success callback `http_request_repository_impl.dart @0x3bb4cb0` loads no argument and calls `exeSuccess()` (log label `"---> delMessage request success"`); the callers' callbacks (`message_main_logic.dart @0x401ab10`, `message_system_logic.dart @0x3bb4d24`) call `exeSuccess()` and have no `fromJson` call.

## Response

No response key is read by the app.

## Example request/response

Request, synthesized (key set of the always-present keys; value types of `all` unresolved)

```json
{"all": "<all>", "type": 0}
```

`ids` and `sns` are added when set. Response: none parsed.

## Errors seen

None traced. The builder's failure callback `@0x3bb4bfc` logs the code and message and calls `exeError()`; the main-page failure callback `message_main_logic.dart @0x401aa68` also shows a message; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `delMessage` @0x3bb49a8 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::delMessage`
- `charging/ui/page/message/Main/message_main_logic.dart::deleteMsg`
- `charging/ui/page/message/system/message_system_logic.dart::deleteMessage`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- Types of `sns` and `all`, and what `ids`/`sns`/`all` mean together (`all` is a parameter; the callers were not followed). Header stays string-only.
- Which of the constants 1 and 2 is the `type` of the system-message list and of the device-message list: both callers pass a constant to the wrapper, the mapping to the builder's parameter slot was not traced.
- The response body: not read by the app, so its keys are unknown.

## Device-tested by

none
