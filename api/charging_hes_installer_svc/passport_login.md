> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# passport_login

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_installer_svc/passport_login`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/account/login/installer_login_logic.dart @0x3192110`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `email` | ? | ? | ? | `charging/ui/page/account/login/installer_login_logic.dart @0x3191e48` |
| `password` | ? | ? | ? | `charging/ui/page/account/login/installer_login_logic.dart @0x3191e48` |
| `client_secret_info.public_key` | ? | ? | ? | `charging/ui/page/account/login/installer_login_logic.dart @0x3191e48` |
| `support_anker_login` | ? | ? | ? | `charging/ui/page/account/login/installer_login_logic.dart @0x3191e48` |
| `Openudid` | ? | ? | ? | `charging/ui/page/account/login/installer_login_logic.dart @0x3191e48` |
| `App-Name` | ? | ? | ? | `charging/ui/page/account/login/installer_login_logic.dart @0x3191e48` |

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

- `charging/ui/page/account/login/installer_login_logic.dart`: `verifyInstallerAccountPwd` @0x3191e48 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
