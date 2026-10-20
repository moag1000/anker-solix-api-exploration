> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# clear_count

## Purpose

Clears the push badge counter at the Baidu push service, used for China-region accounts; sent by `HttpBusinessImpl::clearBaiDuPushBadge` from `AppLifeCycleDelegate::didChangeAppLifecycleState` and `ThirdPartyService::openAppOptional` (asm-traced, caller chain in `data/endpoints.json`); the sender runs only when the user is logged in (`isLogin`, `charging/http/http_business_impl.dart @0x296d47c`) and the region is China (`isChinaRegion`, `charging/http/http_business_impl.dart @0x296d484`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/push/clear_count` (asm-traced): URL string at `charging/http/http_business_impl.dart @0x296d4d4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x296d4cc`, in `HttpBusinessImpl::clearBaiDuPushBadge` (`charging/http/http_business_impl.dart @0x296d444`), sent through `requestHttp` (`@0x296d4f4`).

## Encrypted?

encrypted: `true` (asm-traced default): `HttpBusinessImpl::requestHttp` (`charging/http/http_business_impl.dart @0x239ba88`) declares `needEncryption = true` (`@0x239ba94`) and the sender passes no named arguments (`@0x296d4f0`). Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No body field: the sender builds an empty map literal (`Map._fromLiteral` `charging/http/http_business_impl.dart @0x296d494`, no key store before it).

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closure (`charging/http/http_business_impl.dart @0x296d594`) only logs the response value in the text `清除百度推送badge角标数量成功: data-- ` (`@0x296d5c4` reads the argument for the log line) and reads no key. No `fromJson`.

## Response

No response key is read by the app (see Response model).

## Example request/response

Request: no body fields are built (see Request). Response: not synthesized; no capture exists for this endpoint.

## Errors seen

none traced: no numeric error code is compared in the sender or its closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_business_impl.dart`: `clearBaiDuPushBadge` @0x296d444 (requestHttp; encrypted: true, `needEncryption` default)

Called from:

- `charging/base/app_life_cycle_delegate.dart::didChangeAppLifecycleState`
- `charging/util/third_party_service.dart::openAppOptional`

Failure handling (traced 2026-10-20, app side): the failure closure (`charging/http/http_business_impl.dart @0x296d51c`, signature `(int, String)`) only logs `清除百度推送badge角标数量失败: msg-- …, code-- …` ("clearing the Baidu push badge count failed", my translation, `@0x296d540`, `@0x296d554`, `exeError` `@0x296d578`); it compares no code and does nothing else.

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the server does with the call (it may call the push provider): not visible in the app.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
