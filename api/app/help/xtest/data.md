> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# data

## Purpose

Requests the data of the JML info card on the user main page; sent by `UserMainPageLogic::_requestJMLInfoByAnker` (`charging/ui/page/user/main/user_main_page_logic.dart @0x26ffedc`), whose success closure passes the answer to `_handleJMLResponse` (`@0x2700090`) (asm-traced for the call chain; the meaning of `JML` is not visible in the asm, string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/help/xtest/data` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x2268338`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2268330`, in `HttpRequestControllerImpl::postJML` (`charging/http/http_request_repository_impl.dart @0x22682ac`), sent through `encryptionRequestHttp` (`@0x2268358`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No body field: the sender builds an empty map literal (`Map._fromLiteral` `charging/http/http_request_repository_impl.dart @0x22682f8`, no key store before it).

## `param_type`/`cmd`

n/a

## Response model (link)

not resolved (string-only): the success closure is the shared closure `charging/http/http_request_repository_impl.dart @0x2268374`, which forwards the response value to the callback (`ClosureCall` `@0x22683a8`) without a `fromJson`; the caller closure (`charging/ui/page/user/main/user_main_page_logic.dart @0x2700024`) logs `JML API response success: ` and hands the value to `_handleJMLResponse` (`@0x2700090`), which was not read.

## Response

Not listed: the response shape is decoded in `_handleJMLResponse`, which was not read.

## Example request/response

Request: no body fields are built (see Request). Response: not synthesized; no capture exists for this endpoint.

## Errors seen

none traced: no numeric error code is compared in the sender, its closures or the caller functions read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `postJML` @0x22682ac (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::postJML`
- `charging/ui/page/user/main/user_main_page_logic.dart::_requestJMLInfoByAnker`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The response keys: `UserMainPageLogic::_handleJMLResponse` decodes the value and was not read.
- What `JML` stands for and why the path contains `xtest`: not visible in the app. — reclassified: server (2026-10-20: a server-side name that the app does not explain)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
