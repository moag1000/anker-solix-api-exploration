> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# manual_list

## Purpose

Loads the list of user manuals per device category; sent by `UserManualsLogic::getUserManualsDataList` and `UserMainPageLogic::_updateTutorial` (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/help/manual_list` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x2700e20`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2700e18`, in `HttpRequestControllerImpl::getUserManualsDeviceList` (`charging/http/http_request_repository_impl.dart @0x2700d90`), sent through `encryptionRequestHttp` (`@0x2700e50`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No body field: the sender builds an empty map literal (`Map._fromLiteral` `charging/http/http_request_repository_impl.dart @0x2700de0`, no key store before it).

## `param_type`/`cmd`

n/a

## Response model (link)

[`UserManualsModel`](../../../models/account.md#usermanualsmodel), parsed by `UserManualsModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x2700ea4` in the success closure `@0x2700e6c` (call target `#0x2700ee4`).

## Response

(asm-traced) Top-level keys of `charging::UserManualsModel` (`data/models.json`): `trace_id` (String?), `category_products` (List), `related_and_bind_device` (List). The closure passes the model to the callback (`ClosureCall` `@0x2700ec0`).

## Example request/response

Request: no body fields are built (see Request). Response: not synthesized; no capture exists for this endpoint.

## Errors seen

none traced: no numeric error code is compared in the sender, its closures or the caller functions read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getUserManualsDeviceList` @0x2700d90 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getUserManualsDeviceList`
- `charging/ui/page/user/main/user_main_page_logic.dart::_updateTutorial`
- `charging/ui/page/user/userManuals/user_manuals_logic.dart::getUserManualsDataList`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The element classes of `category_products` and `related_and_bind_device` (typed `List` in `data/models.json`).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
