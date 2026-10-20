> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# freeze_account

## Purpose

Freezes the logged-in account; sent by `FreezeAccountLogic::_freezeAccountRequest` (`charging/ui/page/user/freeze_account/freeze_account_logic.dart @0x404c5b8`), whose success closure logs the user out (`performLogout` `@0x404c8a8`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/freeze_account` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x404c770`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x404c768`, in `HttpRequestControllerImpl::freezeAccount` (`charging/http/http_request_repository_impl.dart @0x404c6bc`), sent through `encryptionRequestHttp` (`@0x404c798`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `account` | string | yes | `"<account>"` | `charging/http/http_request_repository_impl.dart @0x404c710` (value store `@0x404c720`) |

The value is a String: map literal with type arguments `<String, String>` (`charging/http/http_request_repository_impl.dart @0x404c724`). The caller (`charging/ui/page/user/freeze_account/freeze_account_logic.dart`) reads the stored user phone (`getUserPhone` `@0x404c604`) before the send; that this is the value of `account` was not decoded.

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closure (`charging/http/http_request_repository_impl.dart @0x261b9a0`) reads no response key and calls the stored callback with `true` (`@0x261b9cc`, `ClosureCall` `@0x261b9d4`).

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "account": "<account>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `freezeAccount` @0x404c6bc (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::freezeAccount`
- `charging/ui/page/user/freeze_account/freeze_account_logic.dart::_freezeAccountRequest`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Whether `account` is the phone number or the e-mail: `FreezeAccountLogic::_freezeAccountRequest` loads the user phone (`charging/ui/page/user/freeze_account/freeze_account_logic.dart @0x404c604`) but the link to the argument was not decoded.
- What the server does with the frozen account (reversibility, session invalidation): not visible in the app; the app logs out after success (`@0x404c8a8`).
- The failure closure (`charging/http/http_request_repository_impl.dart @0x404c7b4`) logs the code and message; no code is compared there, and the caller's failure closure is a shared closure that is not in the caller's file and was not read.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
