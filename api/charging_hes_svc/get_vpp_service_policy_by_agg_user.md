> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_vpp_service_policy_by_agg_user

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/get_vpp_service_policy_by_agg_user`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x2979b78`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `current_version` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x2979a6c` |

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

- `charging/http/http_request_repository_impl.dart`: `getVppDisclaimer` @0x2979a6c (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from: `charging/http/http_request_repository.dart::getVppDisclaimer`, `charging/ui/page/device/a5101/setting/vpp/controller.dart::requestVppDisclaimer`, `charging/ui/page/user/main/user_main_page_logic.dart::requestVppDisclaimer`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
