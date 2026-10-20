> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# read_message

## Purpose

Marks messages as read: `MessageMainLogic::markAllMessageIsReaded`, `MessageMainLogic::pushToDetailPage`, `MessageSystemLogic::pushToDetail` and `MessageSystemLogic::readAllMsg` call `setMessageRead`.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/read_message` (asm-traced): URL string at `http_request_repository_impl.dart @0x3bb5938`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3bb5930`, in `HttpRequestControllerImpl::setMessageRead` (`http_request_repository_impl.dart @0x3bb5760`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is an empty `<String, dynamic>` map (`empty_array` `@0x3bb57c0`, `Map._fromLiteral` `@0x3bb57c8`) to which `setMessageRead` (`http_request_repository_impl.dart @0x3bb5760`) adds keys with `Map.[]=`.

| field | type | required | example | source |
|---|---|---|---|---|
| `id` | int (unboxed, x) | optional | | key `@0x3bb5828`, `[]=` `@0x3bb5830`; the value is `int.parse(...)` of a string field of the parameter object (`parse()` `@0x3bb57f4`, `BoxInt64Instr` `@0x3bb57fc`); added only when the parameter object is non-null (`cmp w0, NULL` `@0x3bb57d8`) |
| `all` | ? | yes | | key `@0x3bb5858`, `[]=` `@0x3bb5860` (parameter at `fp-0x10`, loaded `@0x3bb5854`) |
| `type` | int (Smi, w) | yes | | key `@0x3bb5884`, `[]=` `@0x3bb5888`; `lsl x3, x0, #1` `@0x3bb5870` Smi-tags the unboxed parameter |
| `sns` | ? | optional | | key `@0x3bb58d8`, `[]=` `@0x3bb58e0`; added when the parameter is non-null (`@0x3bb5898`) and a dispatch-table call (`GDT[cid_x0 + 0x3558d]` `@0x3bb58ac`, selector not named) returns true (`tbnz` `@0x3bb58c0`) |

## `param_type`/`cmd`

n/a

## Response model (link)

None: the response body is not parsed. The success callback `http_request_repository_impl.dart @0x3bb5988` uses its argument only in the log string `"---> setMessageRead request success"` and calls `exeSuccess()`.

## Response

No response key is read by the app.

## Example request/response

Request, synthesized (types of `all` and `sns` unresolved)

```json
{"id": "<id>", "all": "<all>", "type": "<type>"}
```

`sns` is added when set. Response: none parsed.

## Errors seen

None traced. The builder passes the `postJML` failure template (`@0x226824c`) to the callers' failure callbacks, which were not read. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `setMessageRead` @0x3bb5760 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::setMessageRead`
- `charging/ui/page/message/Main/message_main_logic.dart::markAllMessageIsReaded`
- `charging/ui/page/message/Main/message_main_logic.dart::pushToDetailPage`
- `charging/ui/page/message/system/message_system_logic.dart::pushToDetail`
- `charging/ui/page/message/system/message_system_logic.dart::readAllMsg`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- Types and meaning of `all` and `sns` (parameters; the four UI callers were not followed). Header stays string-only.
- Whether `id` is the message id returned by [get_message](get_message.md): the value is parsed from a string field of the passed object.
- Failure handling in the callers was not read. — traced 2026-10-20: the call sites pass no `fail` closure among their named arguments: `MessageSystemLogic.readAllMsg` (`charging/ui/page/message/system/message_system_logic.dart @0x3bb564c`): no named argument; `MessageSystemLogic.pushToDetail` (`charging/ui/page/message/system/message_system_logic.dart @0x3bb7ff0`): named arguments `model`; `MessageSystemLogic.pushToDetail` (`charging/ui/page/message/system/message_system_logic.dart @0x3bb8180`): named arguments `model`; `MessageSystemLogic.pushToDetail` (`charging/ui/page/message/system/message_system_logic.dart @0x3bb8270`): named arguments `model`; `MessageMainLogic.markAllMessageIsReaded` (`charging/ui/page/message/Main/message_main_logic.dart @0x401b28c`): named arguments `snList`; `MessageMainLogic.pushToDetailPage` (`charging/ui/page/message/Main/message_main_logic.dart @0x401e24c`): named arguments `model`. Failure then falls to the callee's default or to the awaiting code, neither of which was read

## Device-tested by

none
