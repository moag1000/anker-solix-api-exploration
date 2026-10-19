> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_subscriptions

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/passport/get_subscriptions`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x291bfa4`

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

- `charging/http/http_request_repository_impl.dart`: `getSubscription` @0x291bf14 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/common_business/sms/sms_manager.dart::_getSubscribe`
- `charging/http/http_request_repository.dart::getSubscription`
- `charging/ui/page/user/accountSetting/account_setting_page_logic.dart::getSubscribe`
- `charging/ui/page/user/subscribe/subscribe_email_logic.dart::_getSubscribe`
- `charging/ui/page/user/subscribe/subscribe_email_logic.dart::subscribeSms`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
