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
| `subscribe` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x35a3920` (`[]=` call `@0x35a392c`, value from a parameter) |
| `sms_subscribe` | ? | optional (null check `cmp w3, NULL` `@0x35a3934`, branch `@0x35a3938`) | ? | `charging/http/http_request_repository_impl.dart @0x35a3940` (`[]=` call `@0x35a3948`) |
| `phone_number` | ? | optional (null check `@0x35a3950`, then a zero-length test `cbz` `@0x35a395c` on a length field) | ? | `charging/http/http_request_repository_impl.dart @0x35a3964` (`[]=` call `@0x35a396c`) |

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

- Types of `subscribe`, `sms_subscribe` and `phone_number`: the map has no type arguments and the values are parameters; the `field_7` load before the `cbz` (`charging/http/http_request_repository_impl.dart @0x35a3958`) looks like a string length, which is not a type proof.
- What the callers pass for `sms_subscribe` and when they omit `phone_number`.
- Error codes: none compared in the callers read (`sms_manager.dart`, `subscribe_email_logic.dart`).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
