> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# validate_email

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/passport/validate_email`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x29156f8`
(literal also at 2 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `email` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x3bc84c0` |

Rows are the union over 3 senders; `source` is the first sender that sets the key.

## `param_type`/`cmd`

n/a

## Response model (link)

<!-- TODO -->

## Response

<!-- TODO -->

## Example request/response

<!-- TODO -->

## Errors seen

`api/errors.md`: <!-- TODO -->

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `checkIsRegisterRequest` @0x3bc84c0 (encryptionRequestHttp; encrypted: true); `validateAccountRequest` @0x2915640 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/account/login/installer_login_logic.dart`: `checkIsRegisterRequest` @0x31921c0 (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::checkIsRegisterRequest`, `charging/http/http_request_repository.dart::validateAccountRequest`, `charging/ui/page/account/forget_pwd/forget_pwd_logic.dart::checkIsRegister`, `charging/ui/page/account/login/login_logic.dart::checkIsPwdEmpty`, `charging/ui/page/account/login/login_logic.dart::checkIsRegister`, `charging/ui/page/account/login/login_logic.dart::login`, `charging/ui/page/account/privacy_policy/verification/verification_logic.dart::passwordVerify`, `charging/ui/page/user/accountSetting/account_setting_page_logic.dart::checkIsPwdEmpty`, `charging/ui/page/user/changePassword/user_change_password_logic.dart::changePassword`, `charging/ui/page/user/routerInfo/account_verification/account_verification_logic.dart::confirmChangePwd`, `charging/ui/page/user/routerInfo/router_info_logic.dart::checkIsPwdEmpty`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
