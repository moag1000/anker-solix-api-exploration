> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_popups

## Purpose

Loads the news popups of the AIoT platform; sent by `AIOTRequestControllerImpl::getAIOTPopupListApi` (the inventory lists no caller, so the screen that shows the popups is unknown, string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/news/get_popups` (asm-traced): URL string at `charging/http/aiot/aiot_http_request_repository_impl.dart @0x260dd8c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x260dd84`, in `AIOTRequestControllerImpl::getAIOTPopupListApi` (`charging/http/aiot/aiot_http_request_repository_impl.dart @0x260dcf8`), sent through `aiotPlatformRequestHttp` (`@0x260ddb8`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No body: the function builds no parameter map (no `Map._fromLiteral` in `charging/http/aiot/aiot_http_request_repository_impl.dart @0x260dcf8`).

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::AIOTPopupModel` (`data/models.json`, no page under `models/`), parsed by `AIOTPopupModel.fromJson` at `charging/http/aiot/aiot_http_request_repository_impl.dart @0x260dfb8` in the success closure `@0x260df88` and passed to the stored callback (`ClosureCall` `@0x260dfd4`).

## Response

(asm-traced) Top-level key of `charging::AIOTPopupModel` (`data/models.json`): `popups` (List?).

## Example request/response

Request: no body fields are built (see Request). Response: not synthesized; no capture exists for this endpoint.

## Errors seen

none traced: no numeric error code is compared in the sender or its closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/aiot/aiot_http_request_repository_impl.dart`: `getAIOTPopupListApi` @0x260dcf8 (aiotPlatformRequestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::getAIOTPopupList`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which screen calls `getAIOTPopupListApi`: the inventory lists none.
- The element class of `popups` (typed `List?`).
- What `aiotPlatformRequestHttp` (`charging/http/aiot/aiot_http_request_repository_impl.dart @0x260ddb8`) adds to the request (host, signing): the wrapper was not read here.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
