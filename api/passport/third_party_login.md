> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# third_party_login

## Purpose

Logs a user in with an access token from a third-party identity provider (the only provider the app sends is Amazon) instead of e-mail and password; the response is the same session data as for [login](login.md).

## Upstream name

`none` (no upstream name): `api/apitypes.py` has no key for this URL; it appears only in the upstream list of known passport URLs (comment block in `apitypes.py`, upstream-confirmed as a known URL, not as a tested call).

## Method+URL

`POST /passport/third_party_login` (asm-traced): URL string `pp+0x4b548` at `charging/http/http_request_repository_impl.dart @0x3bd1a9c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3bd1a94`, in `HttpRequestControllerImpl::thirdLoginRequest` (`@0x3bd1858`).

## Encrypted?

Sent through `encryptionRequestHttp` with `needEncryption` at its default `true`, like [login](login.md#encrypted); the real transport path is decided at run time (see [../encryption.md](../encryption.md#which-calls-are-encrypted)). The client public key in the body is the same value as in login.

## Request

Body keys of `thirdLoginRequest`; `Openudid` is a header, not a body key (the inventory skeleton listed it as a field).

| field | type | required | example | source |
|---|---|---|---|---|
| `third_party` | String | yes | `"amazon"` | key `@0x3bd1924`; the value is the string literal `"amazon"` at `@0x3bd1930`, not an argument |
| `access_token` | String | yes | `"<provider access token>"` | `@0x3bd193c`; argument |
| `country_code` | String | yes | `"US"` | `@0x3bd1950`; argument |
| `user_identity` | String | yes | `""` | key `@0x3bd19a0`; the value is the empty string literal at `@0x3bd19ac` |
| `client_secret_info.public_key` | String | yes | `"<client public key>"` | map `client_secret_info` at `@0x3bd19b4`, inner key at `@0x3bd19cc`; argument |

| header | carries | source |
|---|---|---|
| `Openudid` | the terminal id (see [terminal_id.md](terminal_id.md)) | `@0x3bd1a3c` |

Other call arguments: `showLoading: true` (`r30 = true`, `@0x3bd1ab4`, call descriptor `@0x3bd1ac4`).

## `param_type`/`cmd`

n/a

## Response model (link)

`IotUserModel`, same as [login](login.md#response-model-link); the success closure of this call also ends in `AKIoTKitManagerImpl::loginIoTSDK` (`http_request_repository_impl.dart @0x3bd1d00`).

## Response

Same wrapper as [login](login.md#response); token semantics in [../auth.md](../auth.md#token-lifecycle).

| field | type | required | example | source |
|---|---|---|---|---|
| (see login) | | | | `http_request_repository_impl.dart @0x3bd1d00` |

## Example request/response

Request, synthesized

```json
{
  "third_party": "amazon",
  "access_token": "<provider access token>",
  "country_code": "US",
  "user_identity": "",
  "client_secret_info": { "public_key": "<client public key>" }
}
```

Response, synthesized: same shape as the login response.

## Errors seen

The code catalog is [errors.md](../errors.md). The failure closure of the Amazon login goes through the same `LoginLogic::handleLoginFail` as the password login; its code table is in [login.md](login.md#errors-seen). `/passport/third_party_login` is also exempted by name from the "start the login flow again" step after a forced logout (`HttpEncryptionDecorator.dart @0x486ba00`, see [../encryption.md](../encryption.md#response-handling-and-error-codes)).

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `thirdLoginRequest` @0x3bd1858 (`encryptionRequestHttp`).
- Called from `charging/http/http_request_repository.dart::thirdLoginRequest` and `charging/ui/page/account/login/login_logic.dart::amazonLogin` (`@0x3bd161c`): it first runs the native Amazon sign-in (`ChannelHelper::amazonLogin`, `@0x3bd1728`) and then `thirdLoginRequest` (`@0x3bd1780`). There is no other sender of this URL in 3.24.3.

Call sites (grep of the asm, traced 2026-10-20): the name `thirdLoginRequest` has one call site, `LoginLogic::amazonLogin` (`charging/ui/page/account/login/login_logic.dart @0x3bd1780`); `callWeChatLogin` calls `weChatLogin` (`@0x3bd1138`) and neither function calls `thirdLoginRequest`, so the WeChat login does not send this endpoint.

## Since/changed

3.18.0: present (`http_request_repository_impl.dart`, 3.18.0 `@0x2d2347c`). 3.24.3: present, same body keys. since: ≤3.18.0.

## Known unknowns

- Whether providers other than `"amazon"` are accepted by the server; the app hardcodes one.
- Response differences from the password login (if any).

## Device-tested by

none
