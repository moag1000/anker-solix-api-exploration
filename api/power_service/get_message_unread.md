> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_message_unread

## Purpose

Reads the unread-message flags: `HomeBaseLogic::initBadge` (home badge) and `getMessageReadStatus` of `MessageMainLogic` and `MessageSystemLogic` call `getMessageUnread` and set red-dot flags.

## Upstream name

`get_message_unread` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`GET /power_service/v1/get_message_unread` (asm-traced): URL string at `http_request_repository_impl.dart @0x297b5fc`, method object `Method.get` (pool entry `pp+0x340e8`) at `@0x297b5f4`, in `HttpRequestControllerImpl::getMessageUnread` (`http_request_repository_impl.dart @0x297b55c`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is an empty map literal (`ldr x16, [THR, #0xa8]` empty array `@0x297b5a0`, `Map._fromLiteral` `@0x297b5a8`); the builder contains no `[]=` call, so no key is added. The map goes to `encryptionRequestHttp` (`@0x297b62c`). The call is a GET, so the empty map is the `data` argument of a GET.

## `param_type`/`cmd`

n/a

## Response model (link)

None: no model class is parsed; the callers read single keys from the response map. The builder passes the `postJML` closure templates (`pp+0x5e670`, `pp+0x5e678`) through to the callers' callbacks.

## Response

The callers read these keys, each tested with a class-id compare (`cmp x4, #0x3f`, 64-bit, so 63) and cast with `bool()`: `has_unread_msg` (`home_base_logic.dart @0x34bc078`, callback `@0x34bc04c`), `system_msg` (`message_main_logic.dart @0x297b6e4` and `message_system_logic.dart @0x338fec8`) and `device_msg` (`message_main_logic.dart @0x297b77c`).

## Example request/response

Request, synthesized (GET, empty `data`)

```json
{}
```

Response, synthesized (keys read by the callers; values are placeholders, not a capture)

```json
{"code": 0, "msg": "success", "data": {"has_unread_msg": false, "system_msg": false, "device_msg": false}}
```

## Errors seen

None traced. The callers' failure callbacks (`home_base_logic.dart @0x34bc010`, `message_main_logic.dart @0x297b648`) only log; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getMessageUnread` @0x297b55c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getMessageUnread`
- `charging/ui/page/home/home_base_logic.dart::initBadge`
- `charging/ui/page/message/Main/message_main_logic.dart::getMessageReadStatus`
- `charging/ui/page/message/system/message_system_logic.dart::getMessageReadStatus`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- Whether the three keys come in one response or are returned according to account type: `initBadge` reads only `has_unread_msg`, the message page reads `system_msg` and `device_msg`. — reclassified: server (which keys the server returns for which account is not recorded in the app)
- Other keys the server may add: the callers read only the three above.

## Device-tested by

none
