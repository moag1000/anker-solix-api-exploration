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

(asm-traced) The body is not a literal in the sender: `HttpRequestControllerImpl::addMessage` (`charging/http/http_request_repository_impl.dart @0x261b534`) passes the result of `AddMsgModel.toJson` (`@0x261b588`). `AddMsgModel.toJson` (`charging/model/msg_http_model.dart @0x261b628`) builds `{"messages": [...]}` from a growable list (`_GrowableList.of` `@0x261b6a0`, key at `@0x261b6bc`); the caller fills it with one `Messages` entry (`charging/ble/ble_business_impl.dart`: `r1 = <Messages>` `@0x261a9b4`, length Smi 1 `@0x261a9d0`). `Messages.toJson` (`@0x261b760`) stores 8 keys without a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `messages` | list | yes | one element | `charging/model/msg_http_model.dart @0x261b6bc` |
| `messages[].type_id` | int (unboxed, x) | yes | ? | `charging/model/msg_http_model.dart @0x261b7c4` (value boxed by `BoxInt64Instr` `@0x261b79c`) |
| `messages[].msg_id` | ? | yes | ? | `charging/model/msg_http_model.dart @0x261b7f4` |
| `messages[].product_code` | ? | yes | ? | `charging/model/msg_http_model.dart @0x261b824` |
| `messages[].content` | string | yes | | `charging/model/msg_http_model.dart @0x261b854` |
| `messages[].title` | ? | yes | ? | `charging/model/msg_http_model.dart @0x261b884` |
| `messages[].device_sn` | ? | yes | ? | `charging/model/msg_http_model.dart @0x261b8b0` |
| `messages[].ble_mac` | string (null when the source field is null) | yes | | `charging/model/msg_http_model.dart @0x261b8e0` |
| `messages[].sub_sn` | string | yes | `""` | `charging/model/msg_http_model.dart @0x261b904` (the caller stores the empty string, `charging/ble/ble_business_impl.dart @0x261a994`) |

Where `addCloudLoMessage` (`charging/ble/ble_business_impl.dart @0x261a7a4`, two untyped parameters `SetupParameters(dynamic _, dynamic _)` `@0x261a7b0`) takes each value (asm-traced; offsets are fields of the first argument unless noted, the class of that argument is not named in the asm): `type_id` is an unboxed 64-bit field (`charging/model/msg_http_model.dart @0x261b798`) set to the immediate `1` (`@0x261a8a0`) or `1027` (`@0x261a8a8`, both raw and real: odd values in an unboxed register) after the first argument's `field_b` (null becomes 0, `@0x261a804`; Smi-untagged `@0x261a80c`) was compared with Smi 0 (`cbz` `@0x261a894`) and Smi 2 (raw `cmp w0, #4` `@0x261a898`, tagged, so 2): 0 or 2 gives 1, any other value gives 1027. `msg_id` is `field_3f` (`@0x261a8b4`), `product_code` is `field_2b` (`@0x261a8f0`) and `title` is `field_1f` (`@0x261a8fc`) of that argument, stored unchanged. `content` is the result of `Trans.trArgs` (`@0x261a8d8`) of `field_27`, replaced by the String literal `""` (`@0x261a8e4`) when null. `device_sn` is the second parameter (`@0x261a984`). `ble_mac` is `StringExt.getUnifiedMac` (`@0x261a928`) applied to `field_33` when that field is not null (`@0x261a908`..`@0x261a910`), else null (`@0x261a920`).

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
      "content": "<string>",
      "title": "<?>",
      "device_sn": "<?>",
      "ble_mac": "<string>",
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

- Types and required-ness of `msg_id`, `product_code`, `title` and `device_sn`: they are `field_3f`, `field_2b`, `field_1f` of the first argument and the second parameter of `addCloudLoMessage` (`charging/ble/ble_business_impl.dart @0x261a8b4`, `@0x261a8f0`, `@0x261a8fc`, `@0x261a984`) — attempted 2026-10-20 (two-hop not readable: the four callers (`station_main_page_logic.dart @0x27a1cd0`, `device_main_logic.dart @0x261a438`, `@0x261a6c8`, `HttpEncryptionDecorator.dart @0x486b624`) pass objects whose field declarations are not shown in the asm)
- What the record means: `type_id` is 1 or 1027 (see Request), the meaning of the two values and of the record is inferred from the function name only — reclassified: server
- What the server does with the record or answers (the app ignores the answer, see Response model).

## Device-tested by

none
