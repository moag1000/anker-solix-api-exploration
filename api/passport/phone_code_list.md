> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# phone_code_list

## Purpose

Fetches the list of phone country-code prefixes for the phone input; sent by `SmsManager::getDirectionPhoneNum` (`charging/common_business/sms/sms_manager.dart @0x34e8890`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/phone_code_list` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x34e8fd4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x34e8fcc`, in `HttpRequestControllerImpl::getPreDirectionPhoneCode` (`charging/http/http_request_repository_impl.dart @0x34e8f48`), sent through `encryptionRequestHttp` (`@0x34e8ffc`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No body field: the sender builds an empty map literal (`Map._fromLiteral` `@0x34e8f94`, no key store before it).

## `param_type`/`cmd`

n/a

## Response model (link)

no model: the success closure (`charging/http/http_request_repository_impl.dart @0x34e90c0`) logs `---> getPreDirectionPhoneCode request success` and calls the stored callback with the response value (`ClosureCall` `@0x34e9110`) without a `fromJson`. The caller treats the value as a comma-separated string: it applies an interface call with the argument `","` (`sms_manager.dart @0x34e88fc`, selector not named by Blutter) and maps the parts with `map` to `int?` (`@0x34e8930`, closure `@0x34e9ba0`) (my reading of the shape).

## Response

Not a keyed object in the code read: the value is consumed as a list of `int?` built from a comma-separated string (see Response model).

## Example request/response

Request: no body fields are built (see Request). Response: not synthesized; no capture exists for this endpoint.

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getPreDirectionPhoneCode` @0x34e8f48 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/common_business/sms/sms_manager.dart::getDirectionPhoneNum`
- `charging/http/http_request_repository.dart::getPreDirectionPhoneCode`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The exact selector of the call at `sms_manager.dart @0x34e88fc` (Blutter prints `GDT[cid_x0 + -0xffc]`): the `","` argument and the `map` to `int?` make it a split in my reading, not a named call.
- The closure `@0x34e9ba0` (the per-part parse) was not decoded.
- Whether the list is the order the picker shows: not read.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
