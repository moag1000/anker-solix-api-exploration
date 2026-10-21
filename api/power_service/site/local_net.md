> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# local_net

## Purpose

Runs the A1782 self-test network check: `A1782SelfTestLogic::startSelfCheckNet` (`a1782_self_test_logic.dart @0x2ad0010`), called from `testing`, calls `selfCheckNetwork`.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/site/local_net` (asm-traced): URL string at `http_request_repository_impl.dart @0x2ad0550`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2ad0548`, in `HttpRequestControllerImpl::selfCheckNetwork` (`http_request_repository_impl.dart @0x2ad04bc`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is a 1-pair map literal typed `<String, List>` (type arguments `@0x2ad0504`) built in `selfCheckNetwork` (`http_request_repository_impl.dart @0x2ad04bc`).

| field | type | required | example | source |
|---|---|---|---|---|
| `list` | list | yes | | key `@0x2ad04f0`, value store `@0x2ad0500` (parameter at `fp-0x10`; the map type says a `List`, element type not given) |

## `param_type`/`cmd`

n/a

## Response model (link)

Not determined. The builder passes callback closures that Blutter does not resolve (no `AnonymousClosure` entry in the function's pool references). The caller's callback `a1782_self_test_logic.dart @0x2acec3c` loads one argument and calls `value()`; its role (success or failure) was not decoded.

## Response

Not determined (see Response model).

## Example request/response

Request, synthesized

```json
{"list": []}
```

Response: not determined.

## Errors seen

None traced. The callbacks were not resolved.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `selfCheckNetwork` @0x2ad04bc (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ui/page/device/a1782/station/self_test/a1782_self_test_logic.dart::startSelfCheckNet`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- Element structure of `list` (the self-test network targets); the caller `startSelfCheckNet` was not followed. — not traced 2026-10-20 in this pass (`startSelfCheckNet` caller); the reason given in the bullet stands
- The response handling: the builder's callbacks are unresolved. Header stays string-only for this reason. — traced 2026-10-20: the builder's callbacks are pool entries with the shared placeholder label (`pp.txt`) and cannot be identified

## Device-tested by

none
