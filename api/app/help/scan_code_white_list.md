> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# scan_code_white_list

## Purpose

Loads the list of URLs the QR scanner may open; sent by `QrScannerLogic::checkUrlOptional` (`charging/ui/page/qr_Scanner/qr_scanner_logic.dart`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/help/scan_code_white_list` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x33fd958`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x33fd950`, in `HttpRequestControllerImpl::scanodeWhiteListReq` (`charging/http/http_request_repository_impl.dart @0x33fd8cc`), sent through `encryptionRequestHttp` (`@0x33fd988`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No body field: the sender builds an empty map literal (`Map._fromLiteral` `charging/http/http_request_repository_impl.dart @0x33fd918`, no key store before it).

## `param_type`/`cmd`

n/a

## Response model (link)

[`UrlWhiteListModel`](../../../models/account.md#urlwhitelistmodel), parsed by `UrlWhiteListModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x33fd9dc` in the success closure `@0x33fd9a4` (call target `#0x33fda1c`).

## Response

(asm-traced) Top-level key of `charging::UrlWhiteListModel` (`data/models.json`): `white_list` (List). The closure passes the model to the callback (`ClosureCall` `@0x33fd9f8`).

## Example request/response

Request: no body fields are built (see Request). Response: not synthesized; no capture exists for this endpoint.

## Errors seen

none traced: no numeric error code is compared in the sender, its closures or the caller functions read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `scanodeWhiteListReq` @0x33fd8cc (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::scanodeWhiteListReq`
- `charging/ui/page/qr_Scanner/qr_scanner_logic.dart::checkUrlOptional`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The element type of `white_list` (typed `List`) and whether entries are host names, prefixes or patterns: the matching code in `QrScannerLogic` was not read.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
