> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# register

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/passport/register`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x3be24d4`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `email` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3be23dc` |
| `password` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3be23dc` |
| `is_subscribe` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3be23dc` |
| `country_code` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3be23dc` |

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

- `charging/http/http_request_repository_impl.dart`: `registerRequest` @0x3be23dc (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::registerRequest`, `charging/ui/page/account/register/register_logic.dart::register`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
