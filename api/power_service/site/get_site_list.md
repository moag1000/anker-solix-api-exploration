> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_site_list

## Purpose

<!-- TODO -->

## Upstream name

`site_list` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/site/get_site_list`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x28c2ffc`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `/power_service/v1/site/get_site_list` | ? | ? | ? | `charging/ui/page/home/home_base_http_reposity.dart @0x238e380` |

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

- `charging/http/http_request_repository_impl.dart`: `getUserSiteList` @0x28c2f6c (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/home/home_base_http_reposity.dart`: `querySiteList` @0x238e380 (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::getUserSiteList`, `charging/ui/page/device/a17c0/select_station/select_station_logic.dart::getUserSiteListReq`, `charging/ui/page/green_energy/site/site_logic.dart::onReady`, `charging/ui/page/user/share_site/manage_system/manage_system_logic.dart::getUserSiteListReq`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
