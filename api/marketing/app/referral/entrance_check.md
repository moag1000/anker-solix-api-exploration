> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# entrance_check

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/marketing/v1/app/referral/entrance_check`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x2701a90`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys found by the extractor. <!-- TODO -->

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

- `charging/http/http_request_repository_impl.dart`: `getReferralEntranceCheck` @0x2701a04 (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::getReferralEntranceCheck`, `charging/ui/page/user/main/user_main_page_logic.dart::_updateReferralEnabled`

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
