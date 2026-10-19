> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_token_by_userid

## Purpose

<!-- TODO -->

## Upstream name

`get_token_by_userid` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/app/get_token_by_userid`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x3f2e064`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `user_id` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3f2dfb0` |

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

- `charging/http/http_request_repository_impl.dart`: `getAccessTokenByUserID` @0x3f2dfb0 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getAccessTokenByUserID`
- `charging/ui/page/device/connect/third_party_platform_list/third_party_platform_list_logic.dart::navigateToShellyPage`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
