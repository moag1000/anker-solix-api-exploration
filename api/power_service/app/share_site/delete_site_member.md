> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# delete_site_member

## Purpose

Removes a member from a shared site: `HomeCenterLogic::deleteInviteMemberAlreadyInvited` (`deleteSiteMember`) removes an already-invited member, and the demo-site helper `DemoSiteUtilImpl::anonymousQuitSite` (called from `HomeBaseLogic::useA5101StationWidget` and `DemoSiteUtilImpl::exitDemo`) leaves the demo site with the same URL.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/share_site/delete_site_member` (asm-traced) in every sender listed here; each sender loads the URL string and the method object (pool entry `pp+0xa7e0`, `Method.post`) in one call setup:

- `HttpRequestControllerImpl::deleteSiteMember` (`http_request_repository_impl.dart @0x405cac0`): URL string `@0x405cb40`, method object `Method.post` (`pp+0xa7e0`) `@0x405cb38`.
- `DemoSiteUtilImpl::anonymousQuitSite` (`demosite_util_impl.dart @0x23f0cf4`): URL string `@0x23f0e2c`, method object `Method.post` (`pp+0xa7e0`) `@0x23f0e24`.

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Two senders; both send `site_id` and `member_id`.

Sender `HttpRequestControllerImpl::deleteSiteMember` (`http_request_repository_impl.dart @0x405cac0`): the body comes from the caller `HomeCenterLogic::deleteInviteMemberAlreadyInvited` (`home_center_logic.dart @0x405c950`), a 2-pair map literal typed `<String, dynamic>` (`AllocateArray r2 = 8` `@0x405c9d4`). The caller also takes a named parameter `isMember` (default false, `@0x405c95c`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | yes | | key `@0x405c9dc`, value store `@0x405c9ec` (parameter r2 of the caller, loaded `@0x405c9e8`) |
| `member_id` | ? | yes | | key `@0x405c9f0`, value store `@0x405ca00` (parameter r3, loaded `@0x405c9fc`) |

Sender `DemoSiteUtilImpl::anonymousQuitSite` (`demosite_util_impl.dart @0x23f0cf4`): the body is a 2-pair map literal typed `<String, String?>` (type arguments `@0x23f0de0`, pool `pp+0x8cb8`), sent with `requestHttp` and a `headers` argument (`@0x23f0d18`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | string | yes | `"<site_id>"` | key `@0x23f0db8`, value store `@0x23f0dc8` (parameter r2; value type `String?`) |
| `member_id` | string | yes | `"<member_id>"` | key `@0x23f0dcc`, value store `@0x23f0ddc` (parameter r3; value type `String?`) |

## `param_type`/`cmd`

n/a

## Response model (link)

No model is parsed in the resolved callbacks. `deleteInviteMemberAlreadyInvited` passes `home_center_logic.dart @0x405cb84` (calls `GetNavigation.back`, `removeRecordSelectionSceneSite`, `getUserSiteListReq`, `getSiteList`, `unSubscribeSiteTopic`; loads no argument) and `station_energy_system_logic.dart @0x238c8d0` (loads `fp+0x10`, calls `show()`); neither calls `fromJson`. For `anonymousQuitSite` the two callbacks are the pool entries `pp+0x2e598` and a second `Function:` entry printed as `Function: [dart:ui] _NativeScene::_NativeScene._ (0x49c1cac)`, a placeholder label that 790 pool entries in the asm share, so the callback code cannot be read.

## Response

Not determined for `anonymousQuitSite` (see Response model); the other sender reads no response key.

## Example request/response

Request, synthesized (`deleteSiteMember`, types unresolved in the caller)

```json
{"site_id": "<site_id>", "member_id": "<member_id>"}
```

Response: not determined.

## Errors seen

None traced. No compare of an error code was found in the resolved callbacks. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `deleteSiteMember` @0x405cac0 (encryptionRequestHttp; encrypted: true)
- `charging/util/demosite_util_impl.dart`: `anonymousQuitSite` @0x23f0cf4 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::deleteSiteMember`
- `charging/ui/page/home/home_base_logic.dart::useA5101StationWidget`
- `charging/ui/page/user/share_site/home_center/home_center_logic.dart::deleteInviteMemberAlreadyInvited`
- `charging/util/demosite_util_impl.dart::exitDemo`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- Types of `site_id` and `member_id` in the `deleteSiteMember` sender: they are parameters of `deleteInviteMemberAlreadyInvited`, which the confirm-dialog closures `home_center_logic.dart @0x405c88c` (and the `deleteInviteMemberReq` sibling) call; those callers were not followed. Header stays string-only.
- Response handling of `anonymousQuitSite`: both callbacks are unresolved placeholder pool entries.
- Whether `isMember` changes the request: it is a parameter of the caller; the builder takes only the body map.
- What the server does when the demo site is left: not derivable from the app.

## Device-tested by

none
