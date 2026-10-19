> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# set_account_password

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/passport/set_account_password`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x4055660`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `password` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x4055530` |
| `verify_kind` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x4055530` |
| `client_secret_info.public_key` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x4055530` |

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

- `charging/http/http_request_repository_impl.dart`: `userSetPasswordApi` @0x4055530 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::userSetPasswordApi`
- `charging/ui/page/user/routerInfo/account_set_password/account_set_password_logic.dart::changePassword`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
