> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_message_sn_list

## Purpose

Lists the devices that have messages: `MessageMainLogic::requestMessageSnList` (`message_main_logic.dart @0x34e09ac`) calls `getMessageSnList` and fills the message-centre device list.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/get_message_sn_list` (asm-traced): URL string at `http_request_repository_impl.dart @0x34e0b50`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x34e0b48`, in `HttpRequestControllerImpl::getMessageSnList` (`http_request_repository_impl.dart @0x34e0aa0`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is an empty map literal (`ldr x16, [THR, #0xa8]` empty array `@0x34e0af4`, `Map._fromLiteral` `@0x34e0afc`); the builder contains no `[]=` call, so no key is added. The map goes to `encryptionRequestHttp` (`@0x34e0b84`).

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::MessageDeviceSnModel` (`data/models.json` key, no model page), one object per list element. The builder's success closure `http_request_repository_impl.dart @0x34e0c54` checks that the response is a `List` (class-id test `cmp x3, x17`, `@0x34e0cac`; this value is a class id, not an error code) and passes it to the caller's callback (`ClosureCall` `@0x34e0d68`); the caller's callback `message_main_logic.dart @0x34e0d8c` maps the elements with the closure `@0x34e0e7c` (`MessageDeviceSnModel.fromJson` `@0x34e0ea4`) and `addAll`s them.

## Response

The response data is a JSON list. Keys of one element (from `data/models.json`, all nullable String): `device_sn`, `alias_name`, `device_name`.

## Example request/response

Request, synthesized

```json
{}
```

Response, synthesized (keys from `MessageDeviceSnModel.fromJson`; values are placeholders, not a capture)

```json
{"code": 0, "msg": "success", "data": [{"device_sn": "<device_sn>", "alias_name": "<alias_name>", "device_name": "<device_name>"}]}
```

## Errors seen

None traced. The builder's failure callback `charging/http/http_request_repository_impl.dart @0x34e0ba0` logs `"---> getMessageSnList request failed, code: "` and the message, then calls `exeError()`; the caller's failure callback `family_main_page_logic.dart @0x25f6be0` (pool-shared) only logs the code and message; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getMessageSnList` @0x34e0aa0 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getMessageSnList`
- `charging/ui/page/message/Main/message_main_logic.dart::requestMessageSnList`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta. The model `MessageDeviceSnModel` is `≤3.18.0` in `data/models.json`.

## Known unknowns

- Whether the server wraps the list in an object for some accounts: the closure accepts only a bare `List`.
- Ordering and paging of the list: not visible in the app (no parameter is sent). — reclassified: server (not visible in the app: the app sends no ordering or paging parameter)

## Device-tested by

none
