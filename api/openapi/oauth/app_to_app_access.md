> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# app_to_app_access

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/openapi/oauth/app_to_app_access`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x3bceab4`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `client_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bce744` |
| `redirect_uri` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bce744` |
| `response_type` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bce744` |
| `scope` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bce744` |
| `state` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bce744` |
| `Openudid` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bce744` |

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

- `charging/http/http_request_repository_impl.dart`: `getAlexaLinkCodeRequest` @0x3bce744 (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::getAlexaLinkCodeRequest`, `charging/ui/page/account/login/alexa_link_logic.dart::getAlexaLinkCode`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
