> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_url_by_country_code

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/device_svc/v1/get_url_by_country_code`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/user/profile/profile_http_request_repository_impl.dart @0x2988750`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `country_code` | ? | ? | ? | `charging/http/user/profile/profile_http_request_repository_impl.dart @0x2988680` |

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

- `charging/http/user/profile/profile_http_request_repository_impl.dart`: `getShopUrlFromCountryCode` @0x2988680 (encryptionRequestHttp; encrypted: true)

Called from: `charging/ui/page/user/main/user_main_page_logic.dart::requestShopLink`

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
