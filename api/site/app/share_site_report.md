> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# share_site_report

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/site/v1/app/share_site_report`, method: not extracted by the inventory <!-- TODO -->; string-only: `ats_ax170/src/ats_ax170/page/station/ax170_station_controller.dart @0x23595c8`
(literal also at 2 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `ats_ax170/src/ats_ax170/page/station/ax170_station_controller.dart @0x23594fc` |

Rows are the union over 3 senders; `source` is the first sender that sets the key.

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

- `ats_ax170/src/ats_ax170/page/station/ax170_station_controller.dart`: `_shareSiteReport` @0x23594fc (encryptionRequestHttp; encrypted: true)
- `micro_hes/src/a17e2/station/home/base_station_logic.dart`: `_shareSiteReport` @0x2348b00 (encryptionRequestHttp; encrypted: true)
- `micro_hes/src/common_business/basic_station/station/basic_station_logic.dart`: `_shareSiteReport` @0x2360884 (encryptionRequestHttp; encrypted: true)

Called from:

- `ats_ax170/src/ats_ax170/page/station/ax170_station_controller.dart::requestSceneInfo`
- `micro_hes/src/common_business/basic_station/station/basic_station_logic.dart::requestSceneInfo`

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
