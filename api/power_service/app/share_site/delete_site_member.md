> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# delete_site_member

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/share_site/delete_site_member`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x405cb40`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `charging/util/demosite_util_impl.dart @0x23f0cf4` |
| `member_id` | ? | ? | ? | `charging/util/demosite_util_impl.dart @0x23f0cf4` |

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

- `charging/http/http_request_repository_impl.dart`: `deleteSiteMember` @0x405cac0 (encryptionRequestHttp; encrypted: true)
- `charging/util/demosite_util_impl.dart`: `anonymousQuitSite` @0x23f0cf4 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::deleteSiteMember`
- `charging/ui/page/home/home_base_logic.dart::useA5101StationWidget`
- `charging/ui/page/user/share_site/home_center/home_center_logic.dart::deleteInviteMemberAlreadyInvited`
- `charging/util/demosite_util_impl.dart::exitDemo`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
