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

Keys read (traced 2026-10-20, app side): `UserMainPageLogic::_handleJMLResponse` (`charging/ui/page/user/main/user_main_page_logic.dart @0x2700090`) logs `JML response parsing: data=` (`@0x27000e0`), requires the value to be a `Map<String, dynamic>` (`@0x2700144`) and reads two keys: `h5_link` (`@0x2700184`, converted to text by a one-receiver call whose selector Blutter does not name, `@0x27001c8`) and `new_msg_count` (`@0x2700200`, text then `int.tryParse`, `@0x2700244`..`@0x270026c`). It logs both (`JML h5_link: `, `JML new_msg_count: `), stores the link in an observable of the logic (`value=` `@0x2700330`), sets a second observable from a comparison of the count with 0 (`cmp x4, #0` `@0x2700344`, `value=` `@0x2700360`) and logs `JML red dot status updated: ` (`@0x270036c`). So the app reads a link to an H5 page and a count of new messages, and shows a red-dot flag when the count is positive (reading of the comparison; the widget that shows the flag was not read).

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

- What `JML` stands for and why the path contains `xtest`: not visible in the app. — reclassified: server (2026-10-20: the app does not explain the name; not derivable here)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
