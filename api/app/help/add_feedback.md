> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# add_feedback

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/app/help/add_feedback`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x311fa4c`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `attachment_key_prefixs` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x311f7dc` |
| `device_name` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x311f7dc` |
| `product_number` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x311f7dc` |
| `device_sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x311f7dc` |
| `user_name` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x311f7dc` |
| `user_email` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x311f7dc` |
| `message_content` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x311f7dc` |
| `type` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x311f7dc` |
| `device_mac` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x311f7dc` |
| `subject` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x311f7dc` |
| `purchase_channel` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x311f7dc` |
| `order_number` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x311f7dc` |

## `param_type`/`cmd`

n/a

## Response model (link)

<!-- TODO -->

## Response

<!-- TODO -->

## Example request/response

<!-- TODO -->

## Errors seen

`api/errors.md`: <!-- TODO -->

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `postFeedback` @0x311f7dc (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::postFeedback`, `charging/ui/page/user/feedback/feedback_logic.dart::submit`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
