> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# update_user_param

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/passport/update_user_param`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x293fa08`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `param_type` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x293f888` |
| `param_value` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x293f888` |

## `param_type`/`cmd`

see `api/param_types.md`

param_type is a variable at this sender (traced by heuristic — verify against the callers in `data/param_types.json`).

## Response model (link)

<!-- TODO -->

## Response

<!-- TODO -->

## Example request/response

<!-- TODO -->

## Errors seen

`api/errors.md`: <!-- TODO -->

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `setAppSwitchApi` @0x293f888 (encryptionRequestHttp; encrypted: true, param_type/cmd: see `api/param_types.md`)

Called from:

- `charging/http/http_request_repository.dart::setAppSwitchApi`
- `charging/ui/page/user/about/analyticsAndImprovement/analytics_and_improvement_logic.dart::setAppSwitchStatus`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
