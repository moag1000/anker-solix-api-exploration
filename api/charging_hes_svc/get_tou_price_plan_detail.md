> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_tou_price_plan_detail

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/get_tou_price_plan_detail`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart @0x3ed5af4`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `template_id` | ? | ? | ? | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart @0x3ed59ac` |
| `template_name` | ? | ? | ? | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart @0x3ed59ac` |
| `customer_segment_type` | ? | ? | ? | `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart @0x3ed59ac` |

Rows are the union over 2 senders; `source` is the first sender that sets the key.

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

- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart`: `resetNemPeakData` @0x3ed59ac (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_logic.dart`: `nextStep` @0x29746e8 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_plan_edit/nem_plan_edit_logic.dart::showTipsDialog`
- `charging/ui/page/device/a5101/setting/utility_rate_plan/rate_plan_structure/nem_rate/nem_rate_view.dart::build`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
