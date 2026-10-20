> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# subscription_configs

## Purpose

Asks whether the SMS subscription option is shown; sent by `SmsManager::getIsSHowSmsSubscribe` (`charging/common_business/sms/sms_manager.dart`) and `SubscribeEmailLogic::_getIsSHowSmsSubscribe` (`charging/ui/page/user/subscribe/subscribe_email_logic.dart`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/subscription_configs` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x291b8b4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x291b8ac`, in `HttpRequestControllerImpl::getSubscriptionConfigs` (`charging/http/http_request_repository_impl.dart @0x291b824`), sent through `encryptionRequestHttp` (`@0x291b8dc`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No body field: the sender builds an empty map literal (`Map._fromLiteral` `@0x291b874`, no key store before it).

## `param_type`/`cmd`

n/a

## Response model (link)

no model: the success closure (`charging/http/http_request_repository_impl.dart @0x291b9a0`) tests whether the response value is a `Map<String, dynamic>` (`@0x291ba6c`), reads the key `show_sms` (key string `@0x291baa8`, map lookup `@0x291bab0`), treats a missing key as `false` (`@0x291bac4`), casts the value to `bool` (`@0x291bb08`) and calls the stored callback with it (`ClosureCall` `@0x291bb28`); a response that is not a map yields `false` (`@0x291bb44`, `ClosureCall` `@0x291bb50`).

## Response

(asm-traced) One key is read from the top level of the response: `show_sms` (bool). Nothing else is read.

## Example request/response

Request: no body fields are built (see Request). Response: not synthesized; no capture exists for this endpoint.

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getSubscriptionConfigs` @0x291b824 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/common_business/sms/sms_manager.dart::getIsSHowSmsSubscribe`
- `charging/http/http_request_repository.dart::getSubscriptionConfigs`
- `charging/ui/page/user/subscribe/subscribe_email_logic.dart::_getIsSHowSmsSubscribe`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Other keys the server may send: the app reads only `show_sms`.
- Which regions get `show_sms: true`: not visible in the app. — reclassified: server (2026-10-20: which regions the answer enables is not visible in the app)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
