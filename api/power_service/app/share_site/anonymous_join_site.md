> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# anonymous_join_site

## Purpose

Joins the anonymous demo site: `HomeBaseLogic::useA5101StationWidget` (`home_base_logic.dart @0x23ad97c`) calls `DemoSiteUtilImpl::anonymousQuitSite` and then `DemoSiteUtilImpl::anonymousJoinSite` (`@0x23adad0`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/share_site/anonymous_join_site` (asm-traced): URL string at `demosite_util_impl.dart @0x23f0c9c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x23f0c94`, in `DemoSiteUtilImpl::anonymousJoinSite` (`demosite_util_impl.dart @0x23f0b70`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is a 1-pair map literal typed `<String, String?>` (`AllocateArray r2 = 4` `@0x23f0c1c`, type arguments `@0x23f0c3c`, pool `pp+0x8cb8`). The sender is `requestHttp`, not `encryptionRequestHttp` (`@0x23f0cc4`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | string | yes | `"<site_id>"` | key `@0x23f0c28`, value store `@0x23f0c38` (parameter r2; the map's value type is `String?`, so the value is a String or null; the caller passes `field_7` of a model object, `home_base_logic.dart @0x23adabc`) |

## `param_type`/`cmd`

n/a

## Response model (link)

Not determined. The success and failure callbacks are the pool entries `pp+0x2e570` and `pp+0x2e578` (`@0x23f0c4c`, `@0x23f0c60`), printed as `Function: [dart:ui] _NativeScene::_NativeScene._ (0x49c1cac)`, a placeholder label that 790 pool entries in the asm share, so the callback code cannot be read. The `complete` callback (`@0x22bb130`, printed under `power_usage_scenario_controller.dart`) only calls `complete()` on the async completer.

## Response

Not determined (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by `anonymousJoinSite`)

```json
{"site_id": "<site_id>"}
```

Response: not determined.

## Errors seen

None traced. No compare of an error code was found in the sender or in the resolved `complete` callback. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/util/demosite_util_impl.dart`: `anonymousJoinSite` @0x23f0b70 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/home/home_base_logic.dart::useA5101StationWidget`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- What the response contains and whether the app reads it: the success callback is an unresolved placeholder pool entry. The header stays string-only for this reason.
- Whether the sender encrypts: it calls `requestHttp` (default `needEncryption` is true, see `api/encryption.md`); the demo-site path was not decoded further.
- What the server does for an anonymous (demo) session: not derivable from the app.

## Device-tested by

none
