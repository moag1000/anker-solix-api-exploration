> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# visualization

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/ems/v1/strategy/visualization`, method: not extracted by the inventory <!-- TODO -->; string-only: `ak_soft_ems/aiems/api/ai_ems_request.dart @0x24a41f8`

## Encrypted?

encrypted: "unknown (URL literal only, no `*Http*` call)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `ak_soft_ems/aiems/api/ai_ems_request.dart @0x24a40fc` |

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

- `ak_soft_ems/aiems/api/ai_ems_request.dart`: `getVisualizationDetail` @0x24a40fc (URL literal only, no `*Http*` call)

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
