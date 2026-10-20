> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# set_account_password

## Purpose

Sets the account password from the router-info account settings; sent by `AccountSetPasswordLogic::changePassword` (`charging/ui/page/user/routerInfo/account_set_password/account_set_password_logic.dart`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/set_account_password` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x4055660`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x4055658`, in `HttpRequestControllerImpl::userSetPasswordApi` (`charging/http/http_request_repository_impl.dart @0x4055530`), sent through `encryptionRequestHttp` (`@0x4055688`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `password` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x4055580` (value store `@0x4055590`) |
| `verify_kind` | string | yes | `"export_account"` | `charging/http/http_request_repository_impl.dart @0x4055594` (value store `@0x40555a8`) |
| `client_secret_info` | object | yes | `{"public_key": "<public_key>"}` | `charging/http/http_request_repository_impl.dart @0x40555ac` (value store `@0x40555ec`) |

The body map literal has type arguments `<String, Object>` (`@0x4055610`), which is not evidence of a value type, so `password` stays `?`. `verify_kind` is the constant string `"export_account"` (`@0x40555a0`). `client_secret_info` is a nested map literal `<String, String>` (`@0x40555d8`) with the key `public_key` (`@0x40555c4`), value from a parameter.

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closure (`charging/http/http_request_repository_impl.dart @0x40556a4`) logs `set password success` (`@0x4055710`) and calls the stored callback without an argument (`ClosureCall` `@0x4055704`); no `fromJson`.

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "password": "<password>",
  "verify_kind": "export_account",
  "client_secret_info": {}
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `userSetPasswordApi` @0x4055530 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::userSetPasswordApi`
- `charging/ui/page/user/routerInfo/account_set_password/account_set_password_logic.dart::changePassword`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The type of `password`: a parameter of the sender stored into a `<String, Object>` literal; the caller's value and any processing before the call were not read.
- Why the same `verify_kind` value `"export_account"` is used here and in `validate_pass`: not visible in the app.
- The failure closure and error codes of the caller were not decoded: none compared in the caller function.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
