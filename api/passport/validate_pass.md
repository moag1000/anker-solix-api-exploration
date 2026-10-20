> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# validate_pass

## Purpose

Verifies the account password before a sensitive action (the verify kind is the constant `"export_account"`); sent by `VerifyHttpReposity::verifyAccount` (`charging/ui/page/account/privacy_policy/verification/verification_http_reposity.dart @0x2faee20`), called from `charging/ui/page/account/privacy_policy/verification/verification_logic.dart @0x2faed6c` and `charging/ui/page/user/routerInfo/account_verification/account_verification_logic.dart @0x4055a18` (asm-traced for the call sites; the purpose is read from the constant and the response key `check_token`, string-only for the wording).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/validate_pass` (asm-traced): URL string at `charging/ui/page/account/privacy_policy/verification/verification_http_reposity.dart @0x2faefa4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2faef9c`, in `VerifyHttpReposity::verifyAccount` (`charging/ui/page/account/privacy_policy/verification/verification_http_reposity.dart @0x2faee20`), sent through `encryptionRequestHttp` (`@0x2faefcc`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `password` | ? | yes | ? | `charging/ui/page/account/privacy_policy/verification/verification_http_reposity.dart @0x2faeec8` (value store `@0x2faeed8`) |
| `verify_kind` | string | yes | `"export_account"` | `charging/ui/page/account/privacy_policy/verification/verification_http_reposity.dart @0x2faeedc` (value store `@0x2faeef0`) |
| `client_secret_info` | object | yes | `{"public_key": "<public_key>"}` | `charging/ui/page/account/privacy_policy/verification/verification_http_reposity.dart @0x2faeef4` (value store `@0x2faef34`) |

The body map literal has type arguments `<String, Object>` (`@0x2faef58`), which is not evidence of a value type, so `password` stays `?`. `verify_kind` is the constant string `"export_account"` (`@0x2faeee8`). `client_secret_info` is a nested map literal `<String, String>` (`@0x2faef20`) with the key `public_key` (`@0x2faef0c`), value from a parameter.

## `param_type`/`cmd`

n/a

## Response model (link)

no model: the success closure (`charging/ui/page/account/privacy_policy/verification/verification_http_reposity.dart @0x2faf064`) reads the key `check_token` from the response value with a dynamic call (key string `@0x2faf12c`, call `@0x2faf14c`), casts the result to `String` (`@0x2faf188`) and passes it to the `success` callback (`ClosureCall` `@0x2faf19c`).

## Response

(asm-traced) One key is read from the top level of the response: `check_token` (String). What the app does with it next (which later request sends it back) was not traced.

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

- `charging/ui/page/account/privacy_policy/verification/verification_http_reposity.dart`: `verifyAccount` @0x2faee20 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The type of `password`: a parameter of the sender stored into a `<String, Object>` literal; the callers' values were not read. — attempted 2026-10-20 (two-hop not readable: an anonymous closure (`charging/ui/page/user/routerInfo/account_verification/account_verification_logic.dart @0x4055a18`), an anonymous closure (`charging/ui/page/account/privacy_policy/verification/verification_logic.dart @0x2faed6c`) pass slots or fields of their own frames; no literal or declared type in the argument setups)
- Which later request consumes `check_token`, and its lifetime: not traced.
- The success closure logs `sendVerifyCode success: ` (a copied log text, `@0x2faf09c`) with the `check_token` value.
- Error codes: none traced in the two call sites.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
