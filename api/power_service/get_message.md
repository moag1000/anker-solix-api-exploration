> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_message

## Purpose

Fetches a page of cloud messages: `MessageMainLogic::requestCloudMessage`, `MessageMainLogic::requestOtherCloudMessage` and `MessageSystemLogic::requestCloudMessage` call `getMessage` with a time and id cursor.

## Upstream name

`get_message` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/get_message` (asm-traced): URL string at `http_request_repository_impl.dart @0x297c524`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x297c51c`, in `HttpRequestControllerImpl::getMessage` (`http_request_repository_impl.dart @0x297c340`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is a 5-pair map literal typed `<String, dynamic>` built in `getMessage` (`http_request_repository_impl.dart @0x297c340`; `Map._fromLiteral` `@0x297c4d0`).

| field | type | required | example | source |
|---|---|---|---|---|
| `last_time` | int (unboxed, x) | yes | | key `@0x297c3ac`, `BoxInt64Instr` `@0x297c3bc`, store `@0x297c3d4` |
| `device_sns` | list (`<String>` growable list at the callers) | yes | | key `@0x297c3f8`, value store `@0x297c40c` (parameter at `fp-0x18`) |
| `limit` | int (Smi, w) | yes | `10` | key `@0x297c430`, `mov x16, #20` `@0x297c43c` + `stur w16` `@0x297c440`, tagged, so 10 |
| `message_type` | string | yes | | key `@0x297c444`, value store `@0x297c458` (stack parameter `fp+0x20`) |
| `last_msg_id` | int (unboxed, x) | yes | | key `@0x297c47c`, `BoxInt64Instr` `@0x297c48c`, store `@0x297c4a4` |

Typing (two-hop, asm-traced): the builder `getMessage` takes `device_sns` and `message_type` as untyped parameters (`SetupParameters(dynamic _ ...)`). The callers build `device_sns` as a growable list with type argument `<String>` (`r1 = <String>`, `_GrowableList` length 0 in `MessageSystemLogic.requestCloudMessage`, `charging/ui/page/message/system/message_system_logic.dart @0x338eeec`, `@0x338eef0`; the same in `MessageMainLogic.requestCloudMessage`, `charging/ui/page/message/Main/message_main_logic.dart @0x297f2dc`, `@0x297f2e0`), so it is a list of strings. `message_type` is a String literal at two callers: `"system"` (`message_system_logic.dart @0x338ef34`) and `"others"` (`MessageMainLogic.requestOtherCloudMessage`, `message_main_logic.dart @0x297c28c`); the third caller passes it from a stack slot loaded earlier.

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::MsgHttpModel` (`data/models.json` key; fields on [`models/other.md`](../../models/other.md#msghttpmodel)), parsed in the success closure `http_request_repository_impl.dart @0x297c628` by `MsgHttpModel.fromJson`.

## Response

Top-level keys of the model (from `data/models.json`): `data` (element type not resolved there), `last_time` (int), `last_msg_id` (int).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders)

```json
{"last_time": "<last_time>", "device_sns": ["<device_sn>"], "limit": 10, "message_type": "system", "last_msg_id": "<last_msg_id>"}
```

## Errors seen

None traced. The builder's failure callback `@0x297c574` logs `"---> getMessage request failed, code: "` and the message, then calls `exeError()`; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getMessage` @0x297c340 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getMessage`
- `charging/ui/page/message/Main/message_main_logic.dart::requestCloudMessage`
- `charging/ui/page/message/Main/message_main_logic.dart::requestOtherCloudMessage`
- `charging/ui/page/message/system/message_system_logic.dart::requestCloudMessage`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- What `message_type` values the callers use and how `last_time`/`last_msg_id` page the list: cursor semantics are server side.
- The structure of `data` items in `MsgHttpModel` (the model keeps them untyped). — reclassified: server (items of an untyped list; the content is server data)

## Device-tested by

none
