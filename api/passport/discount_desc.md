> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# discount_desc

## Purpose

Fetches the text of the promotion offered for the e-mail/SMS subscription; sent by `SmsManager::_getDisCountDesc` (`charging/common_business/sms/sms_manager.dart @0x291c688`), which passes the answer to `_showDiscountDialog` (`@0x291c9b0`) (asm-traced for the call chain; the content of the promotion is inferred from the function names, string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/discount_desc` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x291c7f0`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x291c7e8`, in `HttpRequestControllerImpl::getDisCountDesc` (`charging/http/http_request_repository_impl.dart @0x291c764`), sent through `encryptionRequestHttp` (`@0x291c818`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No body field: the sender builds an empty map literal (`Map._fromLiteral` `@0x291c7b0`, no key store before it).

## `param_type`/`cmd`

n/a

## Response model (link)

not resolved (string-only): the success closure (`charging/http/http_request_repository_impl.dart @0x291c8dc`) logs `---> getDisCountDesc request success` and calls the stored callback with the response value (`ClosureCall` `@0x291c92c`) without a `fromJson`; the caller closure (`sms_manager.dart @0x291c950`) hands two fields of that value (`@0x291c99c`, `@0x291c9a4`) to `_showDiscountDialog` (`@0x291c9b0`). Which class or map those two fields belong to was not decoded.

## Response

Not listed: the shape of the response value is not resolved (see Response model). The caller reads two fields at offsets `field_f` and `field_13` (`sms_manager.dart @0x291c99c`, `@0x291c9a4`).

## Example request/response

Request: no body fields are built (see Request). Response: not synthesized; no capture exists for this endpoint.

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getDisCountDesc` @0x291c764 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/common_business/sms/sms_manager.dart::_getDisCountDesc`
- `charging/http/http_request_repository.dart::getDisCountDesc`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The type of the callback argument and the names of the two fields the dialog reads (`field_f`, `field_13`, `sms_manager.dart @0x291c99c`/`@0x291c9a4`): no `fromJson` is applied in the sender or in the caller closure, so no model key is known. — attempted 2026-10-20 (two-hop not readable: `_getDisCountDesc` (`charging/common_business/sms/sms_manager.dart @0x291c6f4`) pass slots or fields of their own frames; no literal or declared type in the argument setups)
- What the server returns when no promotion exists: the caller logs `getDisCountDesc result is null.` for a null value (`@0x291c97c`).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
