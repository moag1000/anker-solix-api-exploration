> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# anonymous_join_site

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/share_site/anonymous_join_site`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/util/demosite_util_impl.dart @0x23f0c9c`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `charging/util/demosite_util_impl.dart @0x23f0b70` |

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

- `charging/util/demosite_util_impl.dart`: `anonymousJoinSite` @0x23f0b70 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from: `charging/ui/page/home/home_base_logic.dart::useA5101StationWidget`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
