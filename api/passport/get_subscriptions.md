> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_subscriptions

## Purpose

Reads the e-mail and SMS subscription state of the account; sent by `SmsManager::_getSubscribe`, `AccountSettingPageLogic::getSubscribe` and the subscribe-e-mail screen (`SubscribeEmailLogic::_getSubscribe`, `subscribeSms`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/get_subscriptions` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x291bfa4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x291bf9c`, in `HttpRequestControllerImpl::getSubscription` (`charging/http/http_request_repository_impl.dart @0x291bf14`), sent through `encryptionRequestHttp` (`@0x291bfcc`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No body field: the sender builds an empty map literal (`Map._fromLiteral` `@0x291bf64`, no key store before it).

## `param_type`/`cmd`

n/a

## Response model (link)

[`SubscribeEmailModel`](../../models/account.md#subscribeemailmodel), parsed by `SubscribeEmailModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x291c10c` in the success closure `@0x291c0a0`.

## Response

(asm-traced) Top-level keys of `SubscribeEmailModel` (`data/models.json`, `charging::SubscribeEmailModel`): `email` (String?), `accept_survery` (bool?), `subscribe` (bool?), `phone_number` (String?), `sms_subscribe` (bool?). The callers store the `subscribe` flag with `setSubScribe` (`sms_manager.dart @0x291c630`, `account_setting_page_logic.dart @0x29839a0`) and a null value counts as false (`@0x291c62c`).

## Example request/response

Request: no body fields are built (see Request). Response: not synthesized; no capture exists for this endpoint.

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getSubscription` @0x291bf14 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/common_business/sms/sms_manager.dart::_getSubscribe`
- `charging/http/http_request_repository.dart::getSubscription`
- `charging/ui/page/user/accountSetting/account_setting_page_logic.dart::getSubscribe`
- `charging/ui/page/user/subscribe/subscribe_email_logic.dart::_getSubscribe`
- `charging/ui/page/user/subscribe/subscribe_email_logic.dart::subscribeSms`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which of the two flags `subscribe` and `sms_subscribe` is read by which caller: the field offsets were read (`charging/common_business/sms/sms_manager.dart @0x291c61c`), not mapped to names.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
