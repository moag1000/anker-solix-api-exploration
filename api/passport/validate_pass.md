> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# validate_pass

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/passport/validate_pass`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/account/privacy_policy/verification/verification_http_reposity.dart @0x2faefa4`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `password` | ? | ? | ? | `charging/ui/page/account/privacy_policy/verification/verification_http_reposity.dart @0x2faee20` |
| `verify_kind` | ? | ? | ? | `charging/ui/page/account/privacy_policy/verification/verification_http_reposity.dart @0x2faee20` |
| `client_secret_info.public_key` | ? | ? | ? | `charging/ui/page/account/privacy_policy/verification/verification_http_reposity.dart @0x2faee20` |

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

- `charging/ui/page/account/privacy_policy/verification/verification_http_reposity.dart`: `verifyAccount` @0x2faee20 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
