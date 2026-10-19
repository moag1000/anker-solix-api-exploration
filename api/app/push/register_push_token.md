> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# register_push_token

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/app/push/register_push_token`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x2741938`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `is_notification_enable` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x2741818` |
| `token` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x2741818` |
| `Openudid` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x2741818` |

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

- `charging/http/http_request_repository_impl.dart`: `uploadDeviceToken` @0x2741818 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::uploadDeviceToken`
- `charging/http/http_request_repository_impl.dart::uploadDeviceToken`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
