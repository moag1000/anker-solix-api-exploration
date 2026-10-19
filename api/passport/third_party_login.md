> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# third_party_login

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/passport/third_party_login`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x3bd1a9c`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `third_party` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bd1858` |
| `access_token` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bd1858` |
| `country_code` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bd1858` |
| `user_identity` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bd1858` |
| `client_secret_info.public_key` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bd1858` |
| `Openudid` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bd1858` |

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

- `charging/http/http_request_repository_impl.dart`: `thirdLoginRequest` @0x3bd1858 (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::thirdLoginRequest`, `charging/ui/page/account/login/login_logic.dart::amazonLogin`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
