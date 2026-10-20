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

Which UI value reaches which key (app side, traced 2026-10-20): `UserChangePasswordLogic::changePassword` (`charging/ui/page/user/changePassword/user_change_password_logic.dart`) first runs `StringExtensions.processPassword` on the text of the field behind the label `currentPwd` (`field_53`; `charging/ui/page/user/changePassword/user_change_password_view.dart @0x4040a04`) with a variable `EncType` taken from its parameter (`@0x4041d94`, call `@0x4041da0`), then on the text of the field behind the label `retypeNewPwd` (`field_5b`, `user_change_password_view.dart @0x4040d98`) with the constant `EncType` `sha256` (`@0x4041dd4`, call `@0x4041ddc`), and passes the two results to `changePwdRequest` in that order (`@0x4041e0c`, `@0x4041e10`, call `@0x4041e1c`). The sender stores its first parameter (`fp-0x10`) under `original_password` (`charging/http/http_request_repository_impl.dart @0x4041f08`) and its second (`fp-0x18`) under `password` (`@0x4041ef4`), so `original_password` is the processed current password and `password` is the SHA-256 hex text of the retyped new password; the field behind the label `newPwd` (`field_57`, `@0x4040ba4`) is not passed. `processPassword` is described on [login.md](login.md#request).

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

Failure handling (traced 2026-10-20, app side): the failure closure of `UserChangePasswordLogic::changePassword` (`charging/ui/page/user/changePassword/user_change_password_logic.dart @0x4041cc8`, signature `(int, String)`) compares no code; it shows the message string it receives in a dialog with the button text `commonOK` (`Trans.tr` `@0x4041d00`, `GetExtension.showDialog` `@0x4041d28`, `backVisible` and `showTitle` false), so the text shown for a wrong `original_password` is the message of the answer.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `changePwdRequest` @0x4041e8c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::changePwdRequest`
- `charging/ui/page/user/changePassword/user_change_password_logic.dart::changePassword`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Password policy and the code for a wrong `original_password`: the app compares no code and shows the message text of the answer (see Errors seen); the policy and the codes are decided by the server — reclassified: server (2026-10-20)
- Whether other sessions or tokens are invalidated after a change: not visible in the app. — reclassified: server (2026-10-20: session handling on the server is not visible in the app)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
