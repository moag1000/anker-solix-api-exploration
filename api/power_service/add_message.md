> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# add_message

## Purpose

Posts one cloud message record that `BleBusinessImpl::addCloudLoMessage` (`charging/ble/ble_business_impl.dart @0x261a7a4`) builds after a BLE exchange; the function runs only when `SpUtilImpl::isLogin` is true (`@0x261a7e0`) (asm-traced for the call chain; the meaning of the record is inferred from the function name, string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/add_message` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x261b5dc`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x261b5d4`, in `HttpRequestControllerImpl::addMessage` (`charging/http/http_request_repository_impl.dart @0x261b534`), sent through `encryptionRequestHttp` (`@0x261b60c`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) The body is not a literal in the sender: `HttpRequestControllerImpl::addMessage` (`charging/http/http_request_repository_impl.dart @0x261b534`) passes the result of `AddMsgModel.toJson` (`@0x261b588`). `AddMsgModel.toJson` (`charging/model/msg_http_model.dart @0x261b628`) builds `{"messages": [...]}` from a growable list (`_GrowableList.of` `@0x261b6a0`, key at `@0x261b6bc`); the caller fills it with one `Messages` entry (`r1 = <Messages>` `@0x261a9b4`, length Smi 1 `@0x261a9d0`). `Messages.toJson` (`@0x261b760`) stores 8 keys without a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `messages` | list | yes | one element | `charging/model/msg_http_model.dart @0x261b6bc` |
| `messages[].type_id` | int (unboxed, x) | yes | ? | `charging/model/msg_http_model.dart @0x261b7c4` (value boxed by `BoxInt64Instr` `@0x261b79c`) |
| `messages[].msg_id` | ? | ? | ? | `charging/model/msg_http_model.dart @0x261b7f4` |
| `messages[].product_code` | ? | ? | ? | `charging/model/msg_http_model.dart @0x261b824` |
| `messages[].content` | ? | ? | ? | `charging/model/msg_http_model.dart @0x261b854` |
| `messages[].title` | ? | ? | ? | `charging/model/msg_http_model.dart @0x261b884` |
| `messages[].device_sn` | ? | ? | ? | `charging/model/msg_http_model.dart @0x261b8b0` |
| `messages[].ble_mac` | ? | ? | ? | `charging/model/msg_http_model.dart @0x261b8e0` |
| `messages[].sub_sn` | string | yes | `""` | `charging/model/msg_http_model.dart @0x261b904` (the caller stores the empty string, `charging/ble/ble_business_impl.dart @0x261a994`) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the closures `addMessage` passes to `encryptionRequestHttp` (`charging/http/http_request_repository_impl.dart @0x261b59c`, `@0x261b5b0`, `@0x261b5c4`; distinct bodies `@0x261b9a0` and `@0x226824c`) read no response key and build no model: `@0x261b9a0` calls the stored callback with `true` (`@0x261b9cc`), `@0x226824c` forwards its two arguments to a stored callback (`ClosureCall` `@0x2268288`).

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "messages": [
    {
      "type_id": "<int>",
      "msg_id": "<?>",
      "product_code": "<?>",
      "content": "<?>",
      "title": "<?>",
      "device_sn": "<?>",
      "ble_mac": "<?>",
      "sub_sn": ""
    }
  ]
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `addMessage` @0x261b534 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ble/ble_business_impl.dart::addCloudLoMessage`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types and required-ness of `msg_id`, `product_code`, `content`, `title`, `device_sn` and `ble_mac`: they are fields of `Messages` set in `addCloudLoMessage` from values the asm does not type (`@0x261a95c..0x261a98c`).
- Which `type_id` values the app sends and what the record means: the value comes from a field of the argument object (`@0x261a7f4`); the meaning is inferred from the function name only.
- What the server does with the record or answers (the app ignores the answer, see Response model).

## Device-tested by

none
