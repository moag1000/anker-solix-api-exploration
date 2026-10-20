> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# change_password

## Purpose

Changes the password of the logged-in account; sent by `UserChangePasswordLogic::changePassword` (`charging/ui/page/user/changePassword/user_change_password_logic.dart`) with the old and the new password (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/change_password` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x4041f58`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x4041f50`, in `HttpRequestControllerImpl::changePwdRequest` (`charging/http/http_request_repository_impl.dart @0x4041e8c`), sent through `encryptionRequestHttp` (`@0x4041f80`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `password` | string | yes | `"<password>"` | `charging/http/http_request_repository_impl.dart @0x4041ee4` (value store `@0x4041ef4`) |
| `original_password` | string | yes | `"<original_password>"` | `charging/http/http_request_repository_impl.dart @0x4041ef8` (value store `@0x4041f08`) |

Both values are Strings: the sender stores them in a map literal with type arguments `<String, String>` (`@0x4041f0c`). Which argument of the sender is the old and which the new password was not traced into the UI: `@0x4041ef4` stores the `fp-0x18` argument under `password`, `@0x4041f08` the `fp-0x10` argument under `original_password`.

## `param_type`/`cmd`

n/a

## Response model (link)

[`Result`](../../models/other.md#result), parsed by `Result.fromJson` at `charging/http/http_request_repository_impl.dart @0x4042098` in the success closure `@0x4042050`.

## Response

(asm-traced) Top-level keys of `Result` (`data/models.json`, `charging::Result`): `code` (int?), `msg` (String?), `data` (unknown), `signature` (String?). The success closure hands the parsed `Result` to the stored callback (`ClosureCall` `@0x40420b4`).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "password": "<password>",
  "original_password": "<original_password>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `changePwdRequest` @0x4041e8c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::changePwdRequest`
- `charging/ui/page/user/changePassword/user_change_password_logic.dart::changePassword`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which UI value reaches `password` and which reaches `original_password`: the sender stores its two arguments in that order (`charging/http/http_request_repository_impl.dart @0x4041ef4`, `@0x4041f08`); the mapping in `changePassword` was not decoded, the key names suggest new and old.
- Password policy and the error codes for a wrong `original_password`: the failure closure (`charging/http/http_request_repository_impl.dart @0x4041f9c`) logs code and message and forwards both; no code is compared in it or read in the caller.
- Whether other sessions or tokens are invalidated after a change: not visible in the app.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
