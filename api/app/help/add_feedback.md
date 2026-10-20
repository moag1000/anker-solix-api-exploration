> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# add_feedback

## Purpose

Submits a feedback message with device and contact data and the key prefixes of the uploaded attachments; sent by `FeedbackLogic::submit` (`charging/ui/page/user/feedback/feedback_logic.dart`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/help/add_feedback` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x311fa4c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x311fa44`, in `HttpRequestControllerImpl::postFeedback` (`charging/http/http_request_repository_impl.dart @0x311f7dc`), sent through `encryptionRequestHttp` (`@0x311fa74`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `attachment_key_prefixs` | list | yes | ? | `charging/http/http_request_repository_impl.dart @0x311f8b8` (value store `@0x311f8c8`) |
| `device_name` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x311f8cc` (value store `@0x311f8dc`) |
| `product_number` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x311f8e0` (value store `@0x311f8f0`) |
| `device_sn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x311f8f4` (value store `@0x311f904`) |
| `user_name` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x311f908` (value store `@0x311f918`) |
| `user_email` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x311f91c` (value store `@0x311f92c`) |
| `message_content` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x311f930` (value store `@0x311f940`) |
| `type` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x311f944` (value store `@0x311f950`) |
| `device_mac` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x311f954` (value store `@0x311f964`) |
| `subject` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x311f968` (value store `@0x311f978`) |
| `purchase_channel` | int (unboxed, x) | yes | ? | `charging/http/http_request_repository_impl.dart @0x311f97c` (value store `@0x311f9a4`) |
| `order_number` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x311f9c8` (value store `@0x311f9dc`) |

The body map literal has type arguments `<String, Object>` (`charging/http/http_request_repository_impl.dart @0x311fa00`), which is not evidence of a value type, so the values that are parameters stay `?`. `purchase_channel` is an unboxed int: its value is boxed by `BoxInt64Instr` (`@0x311f98c`) before the store. `attachment_key_prefixs` is built as a growable list (`_GrowableList` `@0x311f834`) in the sender, filled from an argument; the element type was not read. The `type` key is the sender's parameter named in the source, not an upload type.

## `param_type`/`cmd`

n/a

## Response model (link)

not resolved (string-only): the success closure is the shared closure `charging/http/http_request_repository_impl.dart @0x2268374`, which forwards the response value to the caller's callback (`ClosureCall` `@0x22683a8`) without a `fromJson`; what `FeedbackLogic::submit` does with the value was not traced.

## Response

Not listed: the callback's use of the value was not traced (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "attachment_key_prefixs": [],
  "device_name": "<device_name>",
  "product_number": "<product_number>",
  "device_sn": "<device_sn>",
  "user_name": "<user_name>",
  "user_email": "<user_email>",
  "message_content": "<message_content>",
  "type": "<type>",
  "device_mac": "<device_mac>",
  "subject": "<subject>",
  "purchase_channel": "<purchase_channel>",
  "order_number": "<order_number>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender, its closures or the caller functions read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `postFeedback` @0x311f7dc (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::postFeedback`
- `charging/ui/page/user/feedback/feedback_logic.dart::submit`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `device_name`, `product_number`, `device_sn`, `user_name`, `user_email`, `message_content`, `type`, `device_mac`, `subject`, `order_number`: parameters stored into a `<String, Object>` literal.
- Which values `type` takes (the feedback category) and what `purchase_channel` encodes: the callers' arguments were not decoded.
- The response body (the shared closure forwards it unparsed; the caller's reading was not traced).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
