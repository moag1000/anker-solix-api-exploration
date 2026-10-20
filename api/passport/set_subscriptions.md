> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# set_subscriptions

## Purpose

Saves the e-mail and SMS subscription choices; sent by `SmsManager::subscribeSms` (`charging/common_business/sms/sms_manager.dart`) and `SubscribeEmailLogic::_setSubscribe` (`charging/ui/page/user/subscribe/subscribe_email_logic.dart`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/set_subscriptions` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x35a39a8`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x35a39a0`, in `HttpRequestControllerImpl::setSubscription` (`charging/http/http_request_repository_impl.dart @0x35a38ac`), sent through `encryptionRequestHttp` (`@0x35a39d0`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body map is built at run time: the sender creates an empty map (`Map._fromLiteral` with an empty array `@0x35a3914`, no type arguments) and fills it with `[]=` calls.

| field | type | required | example | source |
|---|---|---|---|---|
| `subscribe` | bool | yes |  | `charging/http/http_request_repository_impl.dart @0x35a3920` (`[]=` call `@0x35a392c`, value from a parameter) |
| `sms_subscribe` | bool | optional (null check `cmp w3, NULL` `@0x35a3934`, branch `@0x35a3938`) | ? | `charging/http/http_request_repository_impl.dart @0x35a3940` (`[]=` call `@0x35a3948`) |
| `phone_number` | ? | optional (null check `@0x35a3950`, then a zero-length test `cbz` `@0x35a395c` on a length field) | ? | `charging/http/http_request_repository_impl.dart @0x35a3964` (`[]=` call `@0x35a396c`) |

Caller values (traced 2026-10-20, app side): `SmsManager::subscribeSms` (`charging/common_business/sms/sms_manager.dart @0x3bbcd74`, parameters: an int flag, the phone number, named `result` and `showLoading`) passes `subscribe` as the stored flag (`getSubscribe` `@0x3bbce5c`, text length test `cbnz` `@0x3bbce94`, bool class-id test `cmp x1, #0x3f` `@0x3bbceb4`, fallback `false` `@0x3bbce98`, `@0x3bbcebc`), so a bool; `smsSubscribe` is a bool formed from the flag (`cmp x0, #1`, `csel` of `true`/`false`, `@0x3bbcecc`..`@0x3bbced8`); and `phoneNumber` is the second parameter (`@0x3bbcf1c`..`@0x3bbcf24`, named list `@0x3bbcf28`). `SubscribeEmailLogic::subscribeSms` (`charging/ui/page/user/subscribe/subscribe_email_logic.dart @0x4064304`) calls it with the flag 0 (raw 0, Smi 0, `r2 = 0` `@0x40642f8`), a phone number from a field of the logic (`fp-0x20`, `@0x40642f4`) and `showLoading` true (`@0x40642e8`), so it sends `sms_subscribe` false there; `showReplyDialog` (`@0x3bbbacc`) passes values of its own frame. `SubscribeEmailLogic::_setSubscribe` (`@0x35a36a4`) calls the sender without named arguments (`r4 = const [0, 0x4, 0, 0x4, null]` `@0x35a3734`), so the two optional keys are omitted there.

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closure (`charging/http/http_request_repository_impl.dart @0x35a3a94`) logs `---> setSubscription request success` (`@0x35a3ac8`) and calls the stored callback with `true` (`@0x35a3ad8`, `ClosureCall` `@0x35a3ae4`).

## Response

No response key is read by the app (see Response model).

## Example request/response

Request: the keys are listed under Request; the values are parameters, so no body is synthesized. Response: not synthesized; no capture exists for this endpoint.

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `setSubscription` @0x35a38ac (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/common_business/sms/sms_manager.dart::subscribeSms`
- `charging/http/http_request_repository.dart::setSubscription`
- `charging/ui/page/user/subscribe/subscribe_email_logic.dart::_setSubscribe`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which user actions in `showReplyDialog` (`charging/common_business/sms/sms_manager.dart @0x3bbbacc`) lead to the flag values 1 or 0: the dialog callbacks pass values of their own frame slots and were not decoded; the calls of `SubscribeEmailLogic` are listed under Request — traced 2026-10-20
- Error codes: none compared in the callers read (`sms_manager.dart`, `subscribe_email_logic.dart`). — traced 2026-10-20: `SubscribeEmailLogic::_setSubscribe` passes a success closure (`charging/ui/page/user/subscribe/subscribe_email_logic.dart @0x35a3b7c`, stores the value with `setSubScribe` `@0x35a3be4`) and a failure closure (`@0x35a3b08`, `(int, String)`) that shows a dialog with the button text `commonOK` (`Trans.tr` `@0x35a3b40`, `showDialog` `@0x35a3b60`) and compares no code; `SmsManager::subscribeSms` passes its `result` callback through the shared closure `charging/base/get/get_extension.dart @0x23f3d20` (calls the stored callback when it is not null) and a second closure whose code compare was not decoded
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
