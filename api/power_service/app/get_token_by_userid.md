> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_token_by_userid

## Purpose

Fetches an access token for a user id before opening the Shelly third-party platform page (callers `ThirdPartyPlatformListLogic::navigateToShellyPage`) (asm-traced, caller chain in `data/endpoints.json`). The token value is not printed on this page.

## Upstream name

`get_token_by_userid` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/get_token_by_userid` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3f2e064`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3f2e05c`, in `HttpRequestControllerImpl::getAccessTokenByUserID` (`charging/http/http_request_repository_impl.dart @0x3f2dfb0`), sent through `encryptionRequestHttp` (`@0x3f2e08c`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) The body is one map literal of 1 pair (`AllocateArray`, raw `r2 = 4` at `@0x3f2dffc`, so 2 slots) with type arguments `<String, String>` at `@0x3f2e018`, so every value is typed in the literal; all keys are stored unconditionally.

| field | type | required | example | source |
|---|---|---|---|---|
| `user_id` | string | yes | `"<user_id>"` | `charging/http/http_request_repository_impl.dart @0x3f2e004` |

## `param_type`/`cmd`

n/a

## Response model (link)

no model class (asm-traced): the success closure (`charging/http/http_request_repository_impl.dart @0x3f2e0a8`) reads the key `token` (string literal `@0x3f2e0e4`), casts it to a non-null `String` (`@0x3f2e124`) and passes it to the stored callback (`ClosureCall` `@0x3f2e144`).

## Response

| field | type | required | example | source |
|---|---|---|---|---|
| `token` | string (non-null cast) | yes (a null value fails the cast) | `"<token>"` | `charging/http/http_request_repository_impl.dart @0x3f2e0e4` |

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "user_id": "<user_id>"
}
```

Response, synthesized (key read by the success closure; the value is a placeholder)

```json
{
  "data": {
    "token": "<token>"
  }
}
```

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getAccessTokenByUserID` @0x3f2dfb0 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getAccessTokenByUserID`
- `charging/ui/page/device/connect/third_party_platform_list/third_party_platform_list_logic.dart::navigateToShellyPage`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the token is valid for: server behaviour, not visible from the app. Token handling beyond the cast is in [../../auth.md](../../auth.md).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
