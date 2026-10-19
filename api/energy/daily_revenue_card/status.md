> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# status

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/energy/v1/daily_revenue_card/status`, method: not extracted by the inventory <!-- TODO -->; string-only: `micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart @0x27e8a10`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart @0x27e8698` |

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

- `micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart`: `fetchCardStatus` @0x27e8698 (encryptionRequestHttp; encrypted: true)

Called from: `micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart::onMessageDispatch`, `micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart::updateSiteId`

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
